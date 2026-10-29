"""
EKKOMI NOCTURNE — Migration Utility
Migrates local customer registrations from waitlist_registrations.json
into your live Supabase PostgreSQL database.

Usage:
  python scripts/migrate_local_to_supabase.py
"""

import os
import sys
import json
import urllib.request
import urllib.error

# Windows terminal UTF-8 support
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG_FILE = os.path.join(ROOT_DIR, 'waitlist_registrations.json')
ENV_FILE = os.path.join(ROOT_DIR, '.env')

def load_dotenv():
    if os.path.exists(ENV_FILE):
        try:
            with open(ENV_FILE, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        k, v = line.split('=', 1)
                        os.environ[k.strip()] = v.strip().strip('"').strip("'")
        except Exception:
            pass

load_dotenv()

def migrate():
    supabase_url = os.environ.get('SUPABASE_URL', '').strip().rstrip('/')
    service_key = os.environ.get('SUPABASE_SERVICE_ROLE_KEY', '').strip()

    if not supabase_url or not service_key:
        print("\n[ERROR] Missing SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY in .env.")
        print("Please add your Supabase credentials to .env before running migration.\n")
        return False

    if not os.path.exists(REG_FILE):
        print("\n[NOTICE] No waitlist_registrations.json file found to migrate.\n")
        return False

    try:
        with open(REG_FILE, 'r', encoding='utf-8') as f:
            registrations = json.load(f)
    except Exception as e:
        print(f"\n[ERROR] Failed to read {REG_FILE}: {e}\n")
        return False

    if not registrations:
        print("\n[NOTICE] Registrations list is empty.\n")
        return False

    print(f"\nFound {len(registrations)} local registration(s) to migrate to Supabase:\n")
    endpoint = f"{supabase_url}/rest/v1/waitlist_registrations"
    headers = {
        'apikey': service_key,
        'Authorization': f'Bearer {service_key}',
        'Content-Type': 'application/json',
        'Prefer': 'resolution=ignore-duplicates'
    }

    migrated_count = 0
    for idx, r in enumerate(registrations, 1):
        payload = {
            'registration_id': r.get('registrationId') or f"NOCT-MIG-{idx}",
            'full_name': r.get('fullName', 'Anonymous'),
            'email': (r.get('email') or '').lower().strip(),
            'phone': r.get('phone') or 'Not provided',
            'collection': r.get('collection', 'Men'),
            'jacket_name': (r.get('jacketName') or '').upper(),
            'jacket_colour': r.get('jacketColour', ''),
            'size': r.get('size', 'M'),
            'consent': r.get('consent', True),
            'email_dispatched': bool(r.get('emailDispatchedToAdmin')),
            'created_at': r.get('storedAt') or r.get('timestamp')
        }

        print(f"[{idx}/{len(registrations)}] Migrating {payload['full_name']} ({payload['jacket_name']} - {payload['size']})...", end=' ')

        req = urllib.request.Request(endpoint, data=json.dumps([payload]).encode('utf-8'), headers=headers, method='POST')
        try:
            with urllib.request.urlopen(req) as resp:
                if resp.status in (200, 201):
                    migrated_count += 1
                    print("OK")
                else:
                    print(f"Status {resp.status}")
        except urllib.error.HTTPError as he:
            err_body = he.read().decode('utf-8', errors='ignore')
            print(f"FAILED ({he.code}: {err_body})")
        except Exception as ex:
            print(f"FAILED ({ex})")

    print(f"\nMigration complete: {migrated_count}/{len(registrations)} record(s) migrated to Supabase.\n")
    return True

if __name__ == '__main__':
    migrate()

