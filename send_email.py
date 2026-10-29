"""
EKKOMI NOCTURNE — Email Dispatch & Waiting List Management Utility

Usage:
  python send_email.py --status       # Check SMTP config and registration statistics
  python send_email.py --list         # View all saved customer registrations
  python send_email.py --test         # Send a test email to info@ekkomi.co.uk
  python send_email.py --resend-last  # Forward the latest customer registration to info@ekkomi.co.uk
  python send_email.py --resend-all   # Forward all customer registrations to info@ekkomi.co.uk
"""

import os
import sys
import json
import argparse
from datetime import datetime

# Windows terminal UTF-8 support
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Import core server email functions
import server

def cmd_status():
    cfg = server.get_email_config()
    registrations = []
    if os.path.exists(server.REGISTRATIONS_FILE):
        try:
            with open(server.REGISTRATIONS_FILE, 'r', encoding='utf-8') as f:
                registrations = json.load(f)
        except Exception:
            registrations = []

    print("\n=======================================================")
    print(" EKKOMI NOCTURNE — EMAIL & WAITING LIST STATUS")
    print("=======================================================")
    print(f" • Target Admin Inbox:  {cfg['admin_email']}")
    print(f" • .env File Present:   {os.path.exists(server.ENV_FILE)}")
    print(f" • SMTP Configured:     {cfg['is_configured']}")
    if cfg['is_configured']:
        print(f"   - Host:              {cfg['host']}:{cfg['port']}")
        print(f"   - User:              {cfg['user']}")
        print(f"   - From:              {cfg['from_email']}")
    else:
        print("   - Host / User / Pass: Not configured in .env")
        print("   -> To enable real delivery, copy .env.example to .env and add your details.")

    print(f"\n • Total Registrations: {len(registrations)}")
    dispatched_count = sum(1 for r in registrations if r.get('emailDispatchedToAdmin') or r.get('adminNotified'))
    print(f" • Dispatched to Admin: {dispatched_count}")
    print(f" • Pending Dispatch:    {len(registrations) - dispatched_count}")
    print("=======================================================\n")

def cmd_list():
    if not os.path.exists(server.REGISTRATIONS_FILE):
        print("\nNo registrations found (waitlist_registrations.json does not exist yet).\n")
        return

    try:
        with open(server.REGISTRATIONS_FILE, 'r', encoding='utf-8') as f:
            registrations = json.load(f)
    except Exception as e:
        print(f"\nError reading registrations: {e}\n")
        return

    if not registrations:
        print("\nWaiting list is currently empty.\n")
        return

    print(f"\n=======================================================")
    print(f" EKKOMI NOCTURNE — SAVED REGISTRATIONS ({len(registrations)})")
    print("=======================================================")
    for idx, r in enumerate(registrations, 1):
        full_name = r.get('fullName', 'Unknown')
        email = r.get('email', 'No email')
        col = r.get('collection', '')
        jacket = r.get('jacketName', '')
        size = r.get('size', '')
        reg_id = r.get('registrationId', '')
        time_str = r.get('storedAt', r.get('timestamp', ''))
        admin_dispatched = r.get('emailDispatchedToAdmin', False)
        
        status_flag = "✓ DISPATCHED" if admin_dispatched else "○ SAVED LOCALLY (NOT YET SENT VIA SMTP)"
        phone = r.get('phone', '')
        phone_str = f" · Tel: {phone}" if phone else ""
        print(f" [{idx}] {reg_id} | {full_name} <{email}>{phone_str}")
        print(f"     Selection: {col} · {jacket} · Size {size}")
        print(f"     Time:      {time_str}")
        print(f"     Status:    {status_flag}")
        print("-------------------------------------------------------")
    print()

def cmd_test():
    cfg = server.get_email_config()
    print(f"\nAttempting to send test email to {cfg['admin_email']}...")
    if not cfg['is_configured']:
        print("[ERROR] Cannot send email: SMTP credentials not set.")
        print("Please create a .env file with your SMTP settings (see .env.example).")
        return False

    subj = "[TEST] EKKOMI NOCTURNE — Email Delivery Verification"
    text = (
        "This is an automated test message from the EKKOMI NOCTURNE website.\n\n"
        "If you received this message, your outgoing mail configuration is operating correctly,\n"
        "and all future waiting list registrations will be delivered to this inbox.\n\n"
        "EKKOMI House of Nocturne\n"
    )
    html = f"""<!DOCTYPE html>
<html>
<body style="font-family: sans-serif; background: #FAF6F1; padding: 24px;">
  <div style="max-width: 500px; margin: 0 auto; background: #fff; padding: 32px; border-radius: 4px; border: 1px solid rgba(0,0,0,0.08);">
    <h2 style="font-size: 16px; letter-spacing: 0.16em; text-transform: uppercase;">EKKOMI &middot; NOCTURNE</h2>
    <p style="font-size: 14px; color: #222;">This is a test notification confirming that outgoing email delivery to <strong>{cfg['admin_email']}</strong> is operating correctly.</p>
    <p style="font-size: 12px; color: #888;">All waiting list submissions will automatically forward to this address.</p>
  </div>
</body>
</html>"""

    success, msg = server.send_smtp_email(cfg['admin_email'], subj, text, html)
    if success:
        print(f"SUCCESS: Test email delivered to {cfg['admin_email']}!")
    else:
        print(f"FAILED: {msg}")
    return success

def cmd_resend(last_only=False):
    cfg = server.get_email_config()
    if not cfg['is_configured']:
        print("\n[ERROR] Cannot send emails: SMTP credentials not configured in .env.")
        print("Please copy .env.example to .env and enter your SMTP credentials first.\n")
        return

    if not os.path.exists(server.REGISTRATIONS_FILE):
        print("\nNo registrations file found.\n")
        return

    try:
        with open(server.REGISTRATIONS_FILE, 'r', encoding='utf-8') as f:
            registrations = json.load(f)
    except Exception as e:
        print(f"\nError reading registrations: {e}\n")
        return

    if not registrations:
        print("\nNo registrations to send.\n")
        return

    targets = [registrations[-1]] if last_only else registrations
    print(f"\nDispatching {len(targets)} registration(s) to {cfg['admin_email']}...\n")

    sent_count = 0
    for r in targets:
        subj, text, html = server.build_admin_email(r)
        print(f"Sending: {r.get('fullName')} — {r.get('jacketName')} ({r.get('size')})...", end=' ')
        success, msg = server.send_smtp_email(cfg['admin_email'], subj, text, html)
        if success:
            r['emailDispatchedToAdmin'] = True
            r['adminDeliveryStatus'] = "Delivered via CLI resend"
            sent_count += 1
            print("OK")
        else:
            print(f"FAILED ({msg})")

    # Update file with new status
    try:
        with open(server.REGISTRATIONS_FILE, 'w', encoding='utf-8') as f:
            json.dump(registrations, f, indent=2, ensure_ascii=False)
    except Exception:
        pass

    print(f"\nFinished: {sent_count}/{len(targets)} email(s) successfully delivered to {cfg['admin_email']}.\n")

def main():
    parser = argparse.ArgumentParser(description="EKKOMI NOCTURNE Email Dispatch Utility")
    parser.add_argument('--status', action='store_true', help="Check SMTP configuration and queue counts")
    parser.add_argument('--list', action='store_true', help="List all saved customer registrations")
    parser.add_argument('--test', action='store_true', help="Send a test verification email to admin")
    parser.add_argument('--resend-last', action='store_true', help="Send email for latest customer registration")
    parser.add_argument('--resend-all', action='store_true', help="Send emails for all customer registrations")

    args = parser.parse_args()

    if args.list:
        cmd_list()
    elif args.test:
        cmd_test()
    elif args.resend_last:
        cmd_resend(last_only=True)
    elif args.resend_all:
        cmd_resend(last_only=False)
    else:
        cmd_status()

if __name__ == '__main__':
    main()
