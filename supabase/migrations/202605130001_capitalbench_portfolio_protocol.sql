alter table public.rounds
  add column if not exists submission_format text not null default 'single_pick',
  add column if not exists portfolio_constraints jsonb not null default '{}'::jsonb;

alter table public.rounds
  drop constraint if exists rounds_submission_format_check,
  add constraint rounds_submission_format_check
    check (submission_format in ('single_pick', 'portfolio'));

alter table public.submissions
  add column if not exists submission_format text not null default 'single_pick',
  add column if not exists holding_count integer not null default 1,
  add column if not exists max_allocation_bps integer not null default 10000,
  add column if not exists cash_allocation_bps integer not null default 0,
  add column if not exists benchmark_allocation_bps integer not null default 0,
  add column if not exists concentration_hhi numeric,
  add column if not exists portfolio jsonb not null default '[]'::jsonb,
  add column if not exists portfolio_rationale text;

alter table public.submissions
  drop constraint if exists submissions_submission_format_check,
  add constraint submissions_submission_format_check
    check (submission_format in ('single_pick', 'portfolio')),
  drop constraint if exists submissions_holding_count_check,
  add constraint submissions_holding_count_check
    check (holding_count >= 1),
  drop constraint if exists submissions_max_allocation_bps_check,
  add constraint submissions_max_allocation_bps_check
    check (max_allocation_bps between 1 and 10000),
  drop constraint if exists submissions_cash_allocation_bps_check,
  add constraint submissions_cash_allocation_bps_check
    check (cash_allocation_bps between 0 and 10000),
  drop constraint if exists submissions_benchmark_allocation_bps_check,
  add constraint submissions_benchmark_allocation_bps_check
    check (benchmark_allocation_bps between 0 and 10000);

create table if not exists public.submission_allocations (
  round_id text not null,
  run_id text not null,
  model_id text not null,
  replicate_index integer not null default 1,
  option_id text not null,
  allocation_bps integer not null check (allocation_bps > 0 and allocation_bps <= 10000),
  allocation_rank integer not null check (allocation_rank >= 1),
  rationale_summary text not null default '',
  published boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (round_id, run_id, model_id, replicate_index, option_id),
  foreign key (round_id, run_id, model_id, replicate_index)
    references public.submissions(round_id, run_id, model_id, replicate_index) on delete cascade,
  foreign key (round_id, option_id) references public.options(round_id, option_id)
);

alter table public.official_results
  add column if not exists submission_format text not null default 'single_pick',
  add column if not exists portfolio_return numeric,
  add column if not exists holding_count integer not null default 1,
  add column if not exists max_allocation_bps integer not null default 10000,
  add column if not exists cash_allocation_bps integer not null default 0,
  add column if not exists benchmark_allocation_bps integer not null default 0,
  add column if not exists concentration_hhi numeric;

alter table public.official_results
  drop constraint if exists official_results_submission_format_check,
  add constraint official_results_submission_format_check
    check (submission_format in ('single_pick', 'portfolio'));

alter table public.latest_leaderboard
  add column if not exists submission_format text not null default 'single_pick',
  add column if not exists portfolio_return numeric,
  add column if not exists holding_count integer not null default 1,
  add column if not exists max_allocation_bps integer not null default 10000,
  add column if not exists cash_allocation_bps integer not null default 0,
  add column if not exists benchmark_allocation_bps integer not null default 0,
  add column if not exists concentration_hhi numeric;

alter table public.latest_leaderboard
  drop constraint if exists latest_leaderboard_submission_format_check,
  add constraint latest_leaderboard_submission_format_check
    check (submission_format in ('single_pick', 'portfolio'));

alter table public.submission_allocations enable row level security;

drop trigger if exists set_submission_allocations_updated_at on public.submission_allocations;
create trigger set_submission_allocations_updated_at
before update on public.submission_allocations
for each row execute function public.set_updated_at();

drop policy if exists "anon can read published submission_allocations" on public.submission_allocations;
create policy "anon can read published submission_allocations"
on public.submission_allocations
for select
to anon
using (published = true);

drop policy if exists "service role can manage submission_allocations" on public.submission_allocations;
create policy "service role can manage submission_allocations"
on public.submission_allocations
for all
to service_role
using (true)
with check (true);
