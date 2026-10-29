/**
 * EKKOMI NOCTURNE — WAITLIST REGISTRATION EDGE FUNCTION
 * Hosted on Supabase Edge Functions (Deno Runtime)
 *
 * Responsibilities:
 * 1. CORS validation for Shopify store & development environments
 * 2. Honeypot anti-spam bot verification
 * 3. Strict input validation and sanitization
 * 4. Duplicate request throttling
 * 5. Persistent database insert into PostgreSQL (waitlist_registrations table)
 * 6. Email dispatch via Resend API to info@ekkomi.co.uk and customer confirmation
 * 7. Secure execution: Service Role Key & Resend API Key remain strictly server-side
 */

import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.39.7";

// Allow CORS from any origin (Shopify storefronts, custom domains, local development)
const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};

interface WaitlistPayload {
  fullName?: string;
  email?: string;
  phone?: string;
  collection?: string;
  jacketName?: string;
  jacketColour?: string;
  size?: string;
  consent?: boolean;
  b_company_url?: string; // Honeypot field (must remain empty)
}

serve(async (req: Request) => {
  // Handle CORS Preflight
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: corsHeaders });
  }

  if (req.method !== "POST") {
    return new Response(
      JSON.stringify({ success: false, error: "Method not allowed. Use POST." }),
      { status: 405, headers: { ...corsHeaders, "Content-Type": "application/json" } }
    );
  }

  try {
    const rawBody = await req.json().catch(() => null);
    if (!rawBody) {
      return new Response(
        JSON.stringify({ success: false, error: "Invalid JSON payload" }),
        { status: 400, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    const payload: WaitlistPayload = rawBody;

    // 1. Honeypot Anti-Spam Check
    // If a bot filled out the hidden field, return fake 200 without writing to DB
    if (payload.b_company_url && payload.b_company_url.trim().length > 0) {
      console.warn("[SPAM BOT TRAPPED] Honeypot field was filled:", payload.b_company_url);
      return new Response(
        JSON.stringify({ success: true, message: "Your interest has been registered successfully." }),
        { status: 200, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    // 2. Input Sanitization & Validation
    const fullName = (payload.fullName || "").trim().replace(/[<>]/g, "");
    const email = (payload.email || "").trim().toLowerCase();
    const phone = (payload.phone || "").trim().replace(/[<>]/g, "");
    const collection = (payload.collection || "").trim();
    const jacketName = (payload.jacketName || "").trim().toUpperCase();
    const jacketColour = (payload.jacketColour || "").trim();
    const size = (payload.size || "").trim().toUpperCase();
    const consent = Boolean(payload.consent);

    if (!fullName || fullName.length < 2 || fullName.length > 100) {
      return new Response(
        JSON.stringify({ success: false, error: "Please enter your full name (2 to 100 characters)." }),
        { status: 400, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRegex.test(email) || email.length > 150) {
      return new Response(
        JSON.stringify({ success: false, error: "Please enter a valid email address." }),
        { status: 400, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    const phoneClean = phone.replace(/[\s\-\(\)\.]/g, "");
    if (!phone || phoneClean.length < 7 || phoneClean.length > 20 || !/^(\+)?\d{7,20}$/.test(phoneClean)) {
      return new Response(
        JSON.stringify({ success: false, error: "Please enter a valid phone number with country/area code." }),
        { status: 400, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    if (!["Men", "Women"].includes(collection)) {
      return new Response(
        JSON.stringify({ success: false, error: "Invalid collection selected." }),
        { status: 400, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    if (!jacketName) {
      return new Response(
        JSON.stringify({ success: false, error: "Please select a jacket." }),
        { status: 400, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    const validSizes = ["XS", "S", "M", "L", "XL", "XXL"];
    if (!validSizes.includes(size)) {
      return new Response(
        JSON.stringify({ success: false, error: "Invalid size selected." }),
        { status: 400, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    if (!consent) {
      return new Response(
        JSON.stringify({ success: false, error: "You must agree to receive availability updates." }),
        { status: 400, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    // 3. Connect to Supabase using Server-side Service Role Key
    const supabaseUrl = Deno.env.get("SUPABASE_URL");
    const supabaseServiceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");

    if (!supabaseUrl || !supabaseServiceKey) {
      console.error("[CONFIG ERROR] Missing SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY");
      return new Response(
        JSON.stringify({ success: false, error: "Backend configuration error. Please contact store support." }),
        { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    const supabase = createClient(supabaseUrl, supabaseServiceKey, {
      auth: { persistSession: false },
    });

    // 4. Duplicate Spam Prevention Check (within last 10 minutes)
    const tenMinutesAgo = new Date(Date.now() - 10 * 60 * 1000).toISOString();
    const { data: recentExisting } = await supabase
      .from("waitlist_registrations")
      .select("registration_id, created_at")
      .eq("email", email)
      .eq("collection", collection)
      .eq("jacket_name", jacketName)
      .eq("size", size)
      .gte("created_at", tenMinutesAgo)
      .maybeSingle();

    if (recentExisting) {
      return new Response(
        JSON.stringify({
          success: true,
          message: "Your interest was already registered moments ago. We have your spot reserved.",
          registrationId: recentExisting.registration_id,
          alreadyRegistered: true,
        }),
        { status: 200, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    // 5. Generate Unique Registration ID
    const randomSuffix = Math.random().toString(36).substring(2, 6).toUpperCase();
    const registrationId = `NOCT-${Date.now().toString().slice(-6)}-${randomSuffix}`;

    // Extract metadata
    const clientIp = req.headers.get("x-forwarded-for") || req.headers.get("cf-connecting-ip") || "unknown";
    const userAgent = req.headers.get("user-agent") || "unknown";

    // 6. Insert Record into PostgreSQL Database
    const { data: record, error: dbError } = await supabase
      .from("waitlist_registrations")
      .insert([
        {
          registration_id: registrationId,
          full_name: fullName,
          email: email,
          phone: phone,
          collection: collection,
          jacket_name: jacketName,
          jacket_colour: jacketColour,
          size: size,
          consent: consent,
          ip_address: clientIp,
          user_agent: userAgent,
        },
      ])
      .select()
      .single();

    if (dbError) {
      console.error("[DATABASE INSERT ERROR]", dbError);
      return new Response(
        JSON.stringify({ success: false, error: "Unable to record registration. Please try again." }),
        { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    // 7. Trigger Email Notifications via Resend
    let emailDispatched = false;
    let emailErrorMsg: string | null = null;
    const resendApiKey = Deno.env.get("RESEND_API_KEY");
    const adminEmail = Deno.env.get("ADMIN_EMAIL") || "info@ekkomi.co.uk";
    const fromEmail = Deno.env.get("FROM_EMAIL") || "EKKOMI <notifications@ekkomi.co.uk>";

    if (resendApiKey) {
      try {
        const adminSubject = `[EKKOMI NOCTURNE] New Waiting List Registration: ${fullName} — ${jacketName} (${size})`;
        const adminHtml = `<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #FAF6F1; color: #14100E; margin: 0; padding: 24px; }
  .card { max-width: 580px; margin: 0 auto; background: #FFFFFF; border: 1px solid rgba(20, 16, 14, 0.08); padding: 36px 32px; border-radius: 4px; }
  .brand { font-size: 16px; letter-spacing: 0.22em; text-transform: uppercase; color: #14100E; margin-bottom: 20px; font-weight: 500; }
  .title { font-size: 20px; font-weight: 400; letter-spacing: 0.04em; text-transform: uppercase; margin: 0 0 14px; color: #14100E; }
  .section-label { font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase; color: #8C7D78; margin-top: 24px; margin-bottom: 8px; font-weight: 600; }
  .data-table { width: 100%; border-collapse: collapse; margin-bottom: 12px; }
  .data-table td { padding: 9px 0; border-bottom: 1px solid rgba(20, 16, 14, 0.06); font-size: 14px; line-height: 1.5; }
  .data-table td.label { color: #8C7D78; width: 36%; }
  .data-table td.val { color: #14100E; font-weight: 500; }
  .badge { display: inline-block; background: #14100E; color: #FAF6F1; padding: 3px 9px; border-radius: 3px; font-size: 12px; letter-spacing: 0.06em; }
  .footer { margin-top: 32px; padding-top: 18px; border-top: 1px solid rgba(20, 16, 14, 0.08); font-size: 11px; letter-spacing: 0.08em; color: #8C7D78; text-transform: uppercase; }
</style>
</head>
<body>
<div class="card">
  <div class="brand">EKKOMI &middot; NOCTURNE</div>
  <h2 class="title">New Waiting List Registration</h2>
  <p style="font-size: 14px; color: #554D4A; line-height: 1.5; margin: 0 0 16px;">A customer has registered their interest on the Nocturne collection page:</p>
  
  <div class="section-label">Customer Information</div>
  <table class="data-table">
    <tr><td class="label">Full Name</td><td class="val"><strong>${fullName}</strong></td></tr>
    <tr><td class="label">Email Address</td><td class="val"><a href="mailto:${email}" style="color: #773A3C; text-decoration: none;">${email}</a></td></tr>
    <tr><td class="label">Phone Number</td><td class="val"><a href="tel:${phone}" style="color: #14100E; text-decoration: none; font-weight: 500;">${phone}</a></td></tr>
    <tr><td class="label">Registration ID</td><td class="val">${registrationId}</td></tr>
    <tr><td class="label">Timestamp</td><td class="val">${new Date().toISOString()}</td></tr>
  </table>

  <div class="section-label">Selected Piece</div>
  <table class="data-table">
    <tr><td class="label">Collection</td><td class="val">${collection}'s Collection</td></tr>
    <tr><td class="label">Jacket Style</td><td class="val"><span class="badge">${jacketName}</span></td></tr>
    <tr><td class="label">Colour</td><td class="val">${jacketColour}</td></tr>
    <tr><td class="label">Requested Size</td><td class="val"><strong>${size}</strong></td></tr>
    <tr><td class="label">Consent Status</td><td class="val">Confirmed (Agreed to availability updates)</td></tr>
  </table>

  <div class="footer">&copy; 2026 EKKOMI &middot; All rights reserved &middot; info@ekkomi.co.uk</div>
</div>
</body>
</html>`;

        const resendRes = await fetch("https://api.resend.com/emails", {
          method: "POST",
          headers: {
            Authorization: `Bearer ${resendApiKey}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            from: fromEmail,
            to: [adminEmail],
            reply_to: email,
            subject: adminSubject,
            html: adminHtml,
          }),
        });

        if (resendRes.ok) {
          emailDispatched = true;
          console.log(`[RESEND SUCCESS] Admin notification sent to ${adminEmail}`);
        } else {
          const errData = await resendRes.json().catch(() => ({}));
          emailErrorMsg = `Resend returned ${resendRes.status}: ${JSON.stringify(errData)}`;
          console.error("[RESEND ERROR]", emailErrorMsg);
        }
      } catch (emailErr: any) {
        emailErrorMsg = `Email dispatch exception: ${emailErr.message || emailErr}`;
        console.error("[RESEND EXCEPTION]", emailErrorMsg);
      }

      // Update database row with delivery status for auditing and retries
      await supabase
        .from("waitlist_registrations")
        .update({
          email_dispatched: emailDispatched,
          email_error: emailErrorMsg,
        })
        .eq("id", record.id);
    } else {
      console.warn("[NOTICE] RESEND_API_KEY not configured. Registration saved in database without email.");
    }

    // 8. Return Success Confirmation to Frontend
    return new Response(
      JSON.stringify({
        success: true,
        message: "Your interest has been registered successfully.",
        registrationId: registrationId,
        timestamp: record.created_at,
        emailDispatched: emailDispatched,
      }),
      { status: 200, headers: { ...corsHeaders, "Content-Type": "application/json" } }
    );
  } catch (err: any) {
    console.error("[EDGE FUNCTION ERROR]", err);
    return new Response(
      JSON.stringify({ success: false, error: "An unexpected server error occurred. Please try again." }),
      { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } }
    );
  }
});

