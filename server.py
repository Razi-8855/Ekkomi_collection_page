"""
EKKOMI NOCTURNE — Local Server & Waitlist API Controller
Integrates:
1. Static asset server (HTML, CSS, JS, Fonts, High-res WebP photography)
2. POST /api/waitlist endpoint for multi-step waiting list registrations
3. JSON file storage (waitlist_registrations.json)
4. Automated email notifications to info@ekkomi.co.uk & customer confirmations
   (Supports Google Workspace, Microsoft 365, cPanel domain mail, SendGrid, Resend)
"""

import http.server
import socketserver
import json
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Windows terminal UTF-8 support
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PORT = 8000
REGISTRATIONS_FILE = os.path.abspath('waitlist_registrations.json')
ENV_FILE = os.path.abspath('.env')

def load_dotenv(path=ENV_FILE):
    """Loads key=value pairs from .env without external dependencies."""
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        k, v = line.split('=', 1)
                        k = k.strip()
                        v = v.strip().strip('"').strip("'")
                        os.environ[k] = v
        except Exception as e:
            print(f"[ENV WARNING] Could not read {path}: {e}")

# Initial load
load_dotenv()

def get_email_config():
    """Dynamically reads email configuration from environment or .env."""
    load_dotenv()
    host = os.environ.get('SMTP_HOST', '').strip()
    port_str = os.environ.get('SMTP_PORT', '587').strip()
    try:
        port = int(port_str) if port_str else 587
    except ValueError:
        port = 587
    user = os.environ.get('SMTP_USER', '').strip()
    password = os.environ.get('SMTP_PASS', '').strip()
    from_email = os.environ.get('FROM_EMAIL', user or 'info@ekkomi.co.uk').strip()
    admin_email = os.environ.get('ADMIN_EMAIL', 'info@ekkomi.co.uk').strip()

    is_configured = bool(host and user and password)
    return {
        'host': host,
        'port': port,
        'user': user,
        'pass': password,
        'from_email': from_email,
        'admin_email': admin_email,
        'is_configured': is_configured
    }

def send_smtp_email(to_email, subject, body_text, body_html=None):
    """
    Sends an email using configured SMTP credentials.
    Supports STARTTLS (port 587/25) and SSL (port 465).
    """
    cfg = get_email_config()
    if not cfg['is_configured']:
        return False, "SMTP credentials (SMTP_HOST, SMTP_USER, SMTP_PASS) not set in .env."

    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = f"EKKOMI <{cfg['from_email']}>"
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body_text, 'plain', 'utf-8'))

        if body_html:
            msg.attach(MIMEText(body_html, 'html', 'utf-8'))

        if cfg['port'] == 465:
            with smtplib.SMTP_SSL(cfg['host'], cfg['port'], timeout=15) as server:
                server.login(cfg['user'], cfg['pass'])
                server.send_message(msg)
        else:
            with smtplib.SMTP(cfg['host'], cfg['port'], timeout=15) as server:
                server.starttls()
                server.login(cfg['user'], cfg['pass'])
                server.send_message(msg)

        return True, "Email delivered successfully."
    except Exception as e:
        err_msg = str(e)
        print(f"[SMTP ERROR] Failed to send email to {to_email}: {err_msg}")
        return False, err_msg

def build_admin_email(data):
    """Generates the notification sent to info@ekkomi.co.uk."""
    full_name = data.get('fullName', '')
    email = data.get('email', '')
    phone = data.get('phone', 'Not provided')
    collection = data.get('collection', '')
    jacket_name = data.get('jacketName', '')
    jacket_colour = data.get('jacketColour', '')
    size = data.get('size', '')
    reg_id = data.get('registrationId', '')
    stored_at = data.get('storedAt', datetime.now().isoformat())

    subject = f"[EKKOMI NOCTURNE] New Waiting List Registration: {full_name} — {jacket_name} ({size})"

    text = (
        f"EKKOMI NOCTURNE — NEW WAITING LIST REGISTRATION\n"
        f"=============================================================\n\n"
        f"A customer has registered their interest on the Nocturne collection page:\n\n"
        f"CUSTOMER DETAILS:\n"
        f"  • Full Name:       {full_name}\n"
        f"  • Email Address:   {email}\n"
        f"  • Phone Number:    {phone}\n"
        f"  • Registration ID: {reg_id}\n"
        f"  • Date & Time:     {stored_at}\n\n"
        f"SELECTED PIECE:\n"
        f"  • Collection:      {collection}'s Collection\n"
        f"  • Jacket Style:    {jacket_name}\n"
        f"  • Leather / Tone:  {jacket_colour}\n"
        f"  • Requested Size:  {size}\n"
        f"  • Consent Given:   Yes (confirmed availability updates)\n\n"
        f"DATA RECORD:\n"
        f"  Saved locally in waitlist_registrations.json.\n\n"
        f"=============================================================\n"
        f"EKKOMI House of Nocturne\n"
    )

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #FAF6F1; color: #14100E; margin: 0; padding: 24px; }}
  .card {{ max-width: 580px; margin: 0 auto; background: #FFFFFF; border: 1px solid rgba(20, 16, 14, 0.08); padding: 36px 32px; border-radius: 4px; }}
  .brand {{ font-size: 16px; letter-spacing: 0.22em; text-transform: uppercase; color: #14100E; margin-bottom: 20px; font-weight: 500; }}
  .title {{ font-size: 20px; font-weight: 400; letter-spacing: 0.04em; text-transform: uppercase; margin: 0 0 14px; color: #14100E; }}
  .section-label {{ font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase; color: #8C7D78; margin-top: 24px; margin-bottom: 8px; font-weight: 600; }}
  .data-table {{ width: 100%; border-collapse: collapse; margin-bottom: 12px; }}
  .data-table td {{ padding: 9px 0; border-bottom: 1px solid rgba(20, 16, 14, 0.06); font-size: 14px; line-height: 1.5; }}
  .data-table td.label {{ color: #8C7D78; width: 36%; }}
  .data-table td.val {{ color: #14100E; font-weight: 500; }}
  .badge {{ display: inline-block; background: #14100E; color: #FAF6F1; padding: 3px 9px; border-radius: 3px; font-size: 12px; letter-spacing: 0.06em; }}
  .footer {{ margin-top: 32px; padding-top: 18px; border-top: 1px solid rgba(20, 16, 14, 0.08); font-size: 11px; letter-spacing: 0.08em; color: #8C7D78; text-transform: uppercase; }}
</style>
</head>
<body>
<div class="card">
  <div class="brand">EKKOMI &middot; NOCTURNE</div>
  <h2 class="title">New Waiting List Registration</h2>
  <p style="font-size: 14px; color: #554D4A; line-height: 1.5; margin: 0 0 16px;">A customer has registered their interest on the Nocturne collection page:</p>
  
  <div class="section-label">Customer Information</div>
  <table class="data-table">
    <tr><td class="label">Full Name</td><td class="val"><strong>{full_name}</strong></td></tr>
    <tr><td class="label">Email Address</td><td class="val"><a href="mailto:{email}" style="color: #773A3C; text-decoration: none;">{email}</a></td></tr>
    <tr><td class="label">Phone Number</td><td class="val"><a href="tel:{phone}" style="color: #14100E; text-decoration: none; font-weight: 500;">{phone}</a></td></tr>
    <tr><td class="label">Registration ID</td><td class="val">{reg_id}</td></tr>
    <tr><td class="label">Timestamp</td><td class="val">{stored_at}</td></tr>
  </table>

  <div class="section-label">Selected Piece</div>
  <table class="data-table">
    <tr><td class="label">Collection</td><td class="val">{collection}'s Collection</td></tr>
    <tr><td class="label">Jacket Style</td><td class="val"><span class="badge">{jacket_name}</span></td></tr>
    <tr><td class="label">Colour</td><td class="val">{jacket_colour}</td></tr>
    <tr><td class="label">Requested Size</td><td class="val"><strong>{size}</strong></td></tr>
  </table>

  <div class="footer">&copy; 2026 EKKOMI &middot; All rights reserved &middot; info@ekkomi.co.uk</div>
</div>
</body>
</html>"""
    return subject, text, html

def build_customer_email(data):
    """Generates the confirmation email sent to the customer."""
    full_name = data.get('fullName', 'Valued Customer')
    collection = data.get('collection', '')
    jacket_name = data.get('jacketName', '')
    jacket_colour = data.get('jacketColour', '')
    size = data.get('size', '')

    subject = "Your EKKOMI NOCTURNE Waiting List Confirmation"

    text = (
        f"Dear {full_name},\n\n"
        f"Thank you for joining the EKKOMI NOCTURNE waiting list.\n\n"
        f"We've successfully received your request for the following piece:\n\n"
        f"  • Collection: {collection}'s Collection\n"
        f"  • Jacket:     {jacket_name} ({jacket_colour})\n"
        f"  • Size:       {size}\n\n"
        f"We will notify you about your selected jacket's availability.\n\n"
        f"Thank you for your interest in EKKOMI.\n\n"
        f"Warm regards,\n"
        f"EKKOMI\n"
        f"info@ekkomi.co.uk\n"
    )

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #FAF6F1; color: #14100E; margin: 0; padding: 24px; }}
  .card {{ max-width: 580px; margin: 0 auto; background: #FFFFFF; border: 1px solid rgba(20, 16, 14, 0.08); padding: 40px 36px; border-radius: 4px; }}
  .brand {{ font-size: 16px; letter-spacing: 0.22em; text-transform: uppercase; color: #14100E; margin-bottom: 24px; font-weight: 500; }}
  .title {{ font-size: 22px; font-weight: 400; letter-spacing: 0.04em; text-transform: uppercase; margin: 0 0 16px; color: #14100E; }}
  .p {{ font-size: 14px; line-height: 1.6; color: #3F3734; margin: 0 0 16px; }}
  .box {{ background: #FAF6F1; border: 1px solid rgba(20, 16, 14, 0.08); padding: 18px 20px; border-radius: 3px; margin: 24px 0; }}
  .box-row {{ display: flex; justify-content: space-between; padding: 6px 0; font-size: 13.5px; border-bottom: 1px solid rgba(20, 16, 14, 0.05); }}
  .box-row:last-child {{ border-bottom: none; }}
  .footer {{ margin-top: 32px; padding-top: 18px; border-top: 1px solid rgba(20, 16, 14, 0.08); font-size: 11px; letter-spacing: 0.08em; color: #8C7D78; text-transform: uppercase; }}
</style>
</head>
<body>
<div class="card">
  <div class="brand">EKKOMI &middot; NOCTURNE</div>
  <h2 class="title">You&#8217;re on the list</h2>
  <p class="p">Dear {full_name},</p>
  <p class="p">Thank you for joining the EKKOMI NOCTURNE waiting list. Your interest has been registered successfully.</p>
  
  <div class="box">
    <div style="font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase; color: #8C7D78; margin-bottom: 10px; font-weight: 600;">Selected Piece</div>
    <div style="font-size: 14px; line-height: 1.8; color: #14100E;">
      <strong>Collection:</strong> {collection}'s Collection<br>
      <strong>Jacket:</strong> {jacket_name} ({jacket_colour})<br>
      <strong>Requested Size:</strong> {size}
    </div>
  </div>

  <p class="p">We will notify you about your selected jacket&#8217;s availability.</p>
  <p class="p" style="margin-top: 24px;">Warm regards,<br><strong>EKKOMI</strong></p>

  <div class="footer">&copy; 2026 EKKOMI &middot; <a href="mailto:info@ekkomi.co.uk" style="color: #8C7D78; text-decoration: none;">info@ekkomi.co.uk</a></div>
</div>
</body>
</html>"""
    return subject, text, html

class EkkomiHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/waitlist':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
            except Exception:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': 'Invalid JSON format'}).encode('utf-8'))
                return

            # Anti-Spam Honeypot Verification
            honeypot = data.get('b_company_url', '').strip()
            if honeypot:
                print(f"[SPAM BOT TRAPPED] Honeypot field filled: {honeypot}. Dropping.")
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True, 'message': 'Your interest has been registered successfully.'}).encode('utf-8'))
                return

            full_name = data.get('fullName', '').strip()
            email = data.get('email', '').strip()
            phone = data.get('phone', '').strip()
            collection = data.get('collection', '').strip()
            jacket_name = data.get('jacketName', '').strip()
            jacket_colour = data.get('jacketColour', '').strip()
            size = data.get('size', '').strip()

            if not full_name or not email or not phone or not collection or not jacket_name or not size:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': 'Missing required fields'}).encode('utf-8'))
                return

            registration_id = f"NOCT-{int(datetime.now().timestamp())}"
            data['registrationId'] = registration_id
            data['storedAt'] = datetime.now().isoformat()

            # Build email templates
            admin_subj, admin_text, admin_html = build_admin_email(data)
            cust_subj, cust_text, cust_html = build_customer_email(data)

            # Send Email Notifications
            cfg = get_email_config()
            admin_sent, admin_status = send_smtp_email(cfg['admin_email'], admin_subj, admin_text, admin_html)
            cust_sent, cust_status = send_smtp_email(email, cust_subj, cust_text, cust_html)

            data['emailDispatchedToAdmin'] = admin_sent
            data['adminDeliveryStatus'] = admin_status
            data['emailDispatchedToCustomer'] = cust_sent
            data['customerDeliveryStatus'] = cust_status

            # Append to waitlist_registrations.json
            registrations = []
            if os.path.exists(REGISTRATIONS_FILE):
                try:
                    with open(REGISTRATIONS_FILE, 'r', encoding='utf-8') as f:
                        registrations = json.load(f)
                except Exception:
                    registrations = []

            registrations.append(data)

            try:
                with open(REGISTRATIONS_FILE, 'w', encoding='utf-8') as f:
                    json.dump(registrations, f, indent=2, ensure_ascii=False)
            except Exception as write_err:
                print(f"[STORAGE ERROR] Could not write to {REGISTRATIONS_FILE}: {write_err}")

            # Console reporting
            print(f"\n=======================================================")
            print(f" [WAITLIST REGISTRATION: {registration_id}]")
            print(f" Customer: {full_name} <{email}> · Tel: {phone}")
            print(f" Request:  {collection} · {jacket_name} ({jacket_colour}) · Size {size}")
            print(f" Storage:  Saved locally in waitlist_registrations.json")
            if cfg['is_configured']:
                print(f" Admin Mail to {cfg['admin_email']}: Dispatched = {admin_sent} ({admin_status})")
                print(f" Customer Mail to {email}: Dispatched = {cust_sent} ({cust_status})")
            else:
                print(f" NOTE: Outgoing email paused. SMTP credentials not set in .env.")
                print(f"       All details are stored in waitlist_registrations.json.")
                print(f"       To deliver emails to {cfg['admin_email']}, configure .env.")
            print(f"=======================================================\n")
            sys.stdout.flush()

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response_payload = {
                'success': True,
                'message': 'Your interest has been registered successfully.',
                'registrationId': registration_id,
                'adminEmail': cfg['admin_email'],
                'adminNotified': admin_sent,
                'emailDispatched': cust_sent,
                'smtpConfigured': cfg['is_configured']
            }
            self.wfile.write(json.dumps(response_payload).encode('utf-8'))
            return

        super().do_POST()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    cfg = get_email_config()
    with socketserver.TCPServer(("", PORT), EkkomiHandler) as httpd:
        print(f"=======================================================")
        print(f" Serving EKKOMI NOCTURNE on http://localhost:{PORT}")
        print(f" Waitlist API: http://localhost:{PORT}/api/waitlist")
        print(f" Storage: {REGISTRATIONS_FILE}")
        print(f" Admin Target Email: {cfg['admin_email']}")
        print(f" SMTP Configured: {cfg['is_configured']} ({cfg['host'] or 'No SMTP host set'})")
        print(f"=======================================================")
        sys.stdout.flush()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
