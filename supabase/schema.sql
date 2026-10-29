-- ===================================================================
-- EKKOMI NOCTURNE — SUPABASE POSTGRESQL DATABASE SCHEMA
-- Table: waitlist_registrations
-- Description: Secure storage for customer waiting-list registrations.
-- ===================================================================

-- 1. Create the registrations table
create table if not exists public.waitlist_registrations (
    id uuid default gen_random_uuid() primary key,
    registration_id text not null unique,
    full_name text not null,
    email text not null,
    phone text not null,
    collection text not null check (collection in ('Men', 'Women')),
    jacket_name text not null,
    jacket_colour text not null,
    size text not null check (size in ('XS', 'S', 'M', 'L', 'XL', 'XXL')),
    consent boolean not null default true,
    email_dispatched boolean default false,
    email_error text,
    ip_address text,
    user_agent text,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 2. Indexes for search, auditing, and duplicate prevention
create index if not exists idx_waitlist_email on public.waitlist_registrations(email);
create index if not exists idx_waitlist_created_at on public.waitlist_registrations(created_at desc);
create index if not exists idx_waitlist_jacket on public.waitlist_registrations(collection, jacket_name, size);

-- 3. Enable Row Level Security (RLS)
-- CRITICAL SECURITY REQUIREMENT: Protect all customer details.
-- Anon/public users must have ZERO direct read/write permissions.
alter table public.waitlist_registrations enable row level security;

-- Remove any default public policies if they exist
drop policy if exists "Deny all public access" on public.waitlist_registrations;
drop policy if exists "Allow service_role full access" on public.waitlist_registrations;

-- Policy: Only privileged backend (service_role via Edge Functions) can read/write
create policy "Allow service_role full access" 
on public.waitlist_registrations 
for all 
to service_role
using (true)
with check (true);

-- Revoke all direct public permissions from the table as defense-in-depth
revoke all on public.waitlist_registrations from public, anon, authenticated;
grant all on public.waitlist_registrations to service_role;

-- 4. Administrative Summary View (Secured with security_invoker = true)
-- SECURITY NOTE: By setting security_invoker = true, PostgreSQL executes
-- this view using the caller's permissions (enforcing RLS).
-- Furthermore, permissions are explicitly revoked from public and anon roles.
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

-- Explicitly revoke access from public and anon clients
revoke all on public.waitlist_summary from public, anon, authenticated;
grant select on public.waitlist_summary to service_role;
