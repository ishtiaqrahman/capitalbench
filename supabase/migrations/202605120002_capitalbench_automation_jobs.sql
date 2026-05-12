create table if not exists public.automation_jobs (
  job_id text primary key,
  round_id text not null,
  run_id text not null,
  job_type text not null default 'resolve_round' check (job_type in ('resolve_round')),
  due_at_utc timestamptz not null,
  next_attempt_at_utc timestamptz,
  status text not null default 'scheduled' check (status in ('scheduled', 'running', 'succeeded', 'failed', 'blocked', 'cancelled')),
  attempts integer not null default 0,
  max_attempts integer not null default 30,
  last_error text not null default '',
  locked_at_utc timestamptz,
  locked_by text,
  completed_at_utc timestamptz,
  output_commit_sha text,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (round_id, run_id, job_type)
);

create index if not exists automation_jobs_due_idx
on public.automation_jobs (status, coalesce(next_attempt_at_utc, due_at_utc), due_at_utc);

create index if not exists automation_jobs_round_idx
on public.automation_jobs (round_id, run_id);

drop trigger if exists set_automation_jobs_updated_at on public.automation_jobs;
create trigger set_automation_jobs_updated_at
before update on public.automation_jobs
for each row execute function public.set_updated_at();

alter table public.automation_jobs enable row level security;

drop policy if exists "service role can manage automation jobs" on public.automation_jobs;
create policy "service role can manage automation jobs"
on public.automation_jobs
for all
to service_role
using (true)
with check (true);

create or replace function public.claim_due_automation_job(
  due_before timestamptz default now(),
  worker text default 'capitalbench-automation'
)
returns setof public.automation_jobs
language plpgsql
security definer
set search_path = public
as $$
declare
  claimed_job_id text;
begin
  update public.automation_jobs
  set status = 'running',
      attempts = attempts + 1,
      locked_at_utc = now(),
      locked_by = worker,
      last_error = ''
  where job_id = (
    select job_id
    from public.automation_jobs
    where status in ('scheduled', 'failed')
      and coalesce(next_attempt_at_utc, due_at_utc) <= due_before
      and attempts < max_attempts
    order by coalesce(next_attempt_at_utc, due_at_utc), due_at_utc, created_at
    limit 1
    for update skip locked
  )
  returning job_id into claimed_job_id;

  if claimed_job_id is null then
    return;
  end if;

  return query
  select *
  from public.automation_jobs
  where job_id = claimed_job_id;
end;
$$;

grant execute on function public.claim_due_automation_job(timestamptz, text) to service_role;
