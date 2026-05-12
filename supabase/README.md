# CapitalBench Supabase

This directory contains the public website read model for CapitalBench.

The benchmark CLI remains the producer of record. Supabase stores normalized,
published copies for `www.capitalbench.org`.

## Apply Locally Or To A Linked Project

Use the dedicated CapitalBench Supabase project, not an operator's personal
Supabase org. Keep the project ref and account-specific details in local CLI
state or hosted secret stores, not in committed files.

```bash
supabase login
supabase link --project-ref <project-ref>
supabase db push
```

Required runtime secrets:

- Frontend, Cloudflare Pages: `PUBLIC_SUPABASE_URL`, `PUBLIC_SUPABASE_ANON_KEY`
- CLI/server only: `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`
- Resolver GitHub Action: `TIINGO_API_KEY`, `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`
- Optional resolver deploy trigger: `CLOUDFLARE_PAGES_DEPLOY_HOOK`

Never expose the service-role key to frontend code.

## Automation Jobs

`automation_jobs` stores one service-role-only resolver job per accepted
official run. `capitalbench accept-run` creates or updates the job when a valid
manual provider run is accepted.

The permanent `.github/workflows/capitalbench-resolver.yml` workflow wakes on a
fixed schedule, claims due jobs through `claim_due_automation_job`, resolves the
round, syncs Supabase, commits generated artifacts, and optionally calls the
Cloudflare Pages deploy hook.

The optional Edge Function in
`supabase/functions/dispatch-due-capitalbench-jobs` can wake the same GitHub
workflow more frequently through Supabase scheduled functions. It only
dispatches the workflow; the Python resolver still owns job locking and
publication gates.

Required Edge Function secrets:

- `GITHUB_OWNER`
- `GITHUB_REPO`
- `GITHUB_WORKFLOW` default: `capitalbench-resolver.yml`
- `GITHUB_REF` default: `main`
- `GITHUB_TOKEN` with Actions write access

## Access Model

All public benchmark tables have RLS enabled.

- `anon`: read only rows where `published = true`
- `service_role`: insert/update/delete published read-model rows
- `sync_events`: service-role-only audit trail
- `automation_jobs`: service-role-only scheduler state
- `capitalbench-public-artifacts`: public storage bucket
- `capitalbench-gated-artifacts`: private reserved bucket for future Pro work
