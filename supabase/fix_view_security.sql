-- ===================================================================
-- EKKOMI NOCTURNE — SECURITY REMEDIATION FOR waitlist_summary VIEW
-- ===================================================================
-- Run this script in your Supabase SQL Editor to resolve the
-- "UNRESTRICTED view" warning and secure waiting-list data.
-- ===================================================================

-- 1. Recreate the view with security_invoker = true
-- This forces the view to enforce the underlying table's Row Level Security (RLS).
create or replace view public.waitlist_summary
with (security_invoker = true) as
select 
    collection,
    jacket_name,
    size,
    count(*) as total_requests,
    max(created_at) as latest_request
from public.waitlist_registrations
group by collection, jacket_name, size
order by total_requests desc;

-- 2. Revoke all API access from public, anon, and authenticated users
revoke all on public.waitlist_summary from public, anon, authenticated;

-- 3. Grant access exclusively to service_role (trusted backend/admin)
grant select on public.waitlist_summary to service_role;

-- 4. Reinforce defense-in-depth on the underlying registrations table
revoke all on public.waitlist_registrations from public, anon, authenticated;
grant all on public.waitlist_registrations to service_role;

-- ===================================================================
-- ALTERNATIVE (If you do not need this administrative view at all):
-- You can simply run:
--   DROP VIEW IF EXISTS public.waitlist_summary;
-- The waiting list frontend and Edge Function will continue to work
-- 100% normally because they only interact with waitlist_registrations.
-- ===================================================================

