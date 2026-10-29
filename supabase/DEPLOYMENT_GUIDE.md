# EKKOMI NOCTURNE — Production Deployment Guide
## Hosted Waiting-List System: Supabase (PostgreSQL) + Resend (Email Delivery)

This guide walks you through deploying the production waiting-list system so that when customers access your collection page on Shopify, their details are securely stored in a hosted PostgreSQL database and automated notification emails are delivered to **info@ekkomi.co.uk**.

---

### Step 1: Set Up Hosted Supabase Database

1. Go to [supabase.com](https://supabase.com) and sign in or create a free account.
2. Click **New Project** and name it `ekkomi-nocturne`.
3. Choose your closest region (e.g. `London (eu-west-2)` for UK low latency).
4. In the left navigation, open the **SQL Editor**.
5. Click **New Query**, copy the complete contents of [`supabase/schema.sql`](file:///c:/Users/razi7/OneDrive/Desktop/Documents/ChatGPT/ekkomi/supabase/schema.sql), paste it into the editor, and click **Run**.
   - This creates the `waitlist_registrations` table.
   - It sets up query indexes.
   - It enables **Row Level Security (RLS)** to protect customer privacy from public access.

---

### Step 2: Set Up Transactional Email (Resend)

1. Go to [resend.com](https://resend.com) and create an account.
2. Go to **API Keys** and click **Create API Key**. Copy your key (`re_...`).
3. *(Optional for instant testing)* Resend allows immediate testing using their sandbox sender (`onboarding@resend.dev`).
4. *(Recommended for production)* In Resend, go to **Domains** -> **Add Domain** -> enter `ekkomi.co.uk`.
   - Add the 3 DNS records provided (MX, TXT/DKIM, SPF) to your domain DNS manager (e.g., Cloudflare, GoDaddy, Namecheap).
   - Once verified, you can send officially from `notifications@ekkomi.co.uk` or `info@ekkomi.co.uk`.

---

### Step 3: Deploy the Supabase Edge Function

The Edge Function handles validation, rate-limiting, database insertion, and triggers Resend.

#### Option A: Deploy via Supabase CLI (Recommended)
1. Install Supabase CLI:
   ```powershell
   winget install Supabase.CLI
   # or via npm:
   npm install -g supabase
   ```
2. Log in and link your project:
   ```bash
   supabase login
   supabase link --project-ref <your-supabase-project-ref>
   ```
3. Set your environment secrets:
   ```bash
   supabase secrets set RESEND_API_KEY=re_your_api_key_here
   supabase secrets set ADMIN_EMAIL=info@ekkomi.co.uk
   supabase secrets set FROM_EMAIL="EKKOMI <notifications@ekkomi.co.uk>"
   ```
4. Deploy the function:
   ```bash
   supabase functions deploy waitlist --no-verify-jwt
   ```
5. Your live endpoint will be:
   `https://<your-project-ref>.supabase.co/functions/v1/waitlist`

---

### Step 4: Connect the Frontend (Shopify Storefront)

Open [`waitlist.js`](file:///c:/Users/razi7/OneDrive/Desktop/Documents/ChatGPT/ekkomi/waitlist.js) or your Shopify theme's collection template:

In [`waitlist.js`](file:///c:/Users/razi7/OneDrive/Desktop/Documents/ChatGPT/ekkomi/waitlist.js#L26):
```javascript
const BACKEND_CONFIG = {
  supabaseEndpoint: 'https://<your-project-ref>.supabase.co/functions/v1/waitlist',
  localEndpoint: '/api/waitlist',
  ...
};
```
Alternatively, in your Shopify liquid theme file (e.g. `collection.liquid` or `theme.liquid`), add before `waitlist.js`:
```html
<script>
  window.EKKOMI_WAITLIST_ENDPOINT = 'https://<your-project-ref>.supabase.co/functions/v1/waitlist';
</script>
```

When visitors submit the form on your Shopify website:
1. `waitlist.js` sends the request directly over HTTPS to your Supabase Edge Function.
2. The Edge Function checks the honeypot and validates all inputs.
3. The customer record is saved in your hosted Supabase PostgreSQL table.
4. Resend dispatches an editorial notification email directly to **info@ekkomi.co.uk**.
5. The frontend displays **"YOU'RE ON THE LIST"** only after confirmation is received.

---

### Step 5: Migrate Local Registrations to Supabase

To transfer the 8 customer registrations gathered during testing from your local computer into Supabase:
1. Add your Supabase credentials to `.env`:
   ```ini
   SUPABASE_URL=https://<your-project-ref>.supabase.co
   SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here
   ```
2. Run the migration script:
   ```bash
   python scripts/migrate_local_to_supabase.py
   ```

