create extension if not exists pgcrypto;

create or replace function public.set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create table if not exists public.model_providers (
  provider text primary key,
  display_name text not null,
  website_url text,
  published boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.rounds (
  round_id text primary key,
  title text not null default '',
  description text not null default '',
  decision_date date,
  decision_deadline_utc timestamptz,
  horizon text not null default '',
  horizon_days integer,
  entry_rule text not null default '',
  exit_rule text not null default '',
  entry_date date,
  exit_date date,
  status text not null default 'pending' check (status in ('pending', 'resolved', 'archived')),
  methodology_version text not null default '',
  published boolean not null default false,
  notes text not null default '',
  created_at_utc timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.models (
  model_id text primary key,
  provider text not null references public.model_providers(provider),
  display_name text not null,
  api_model_name text,
  first_eligible_round text,
  first_eligible_date_utc timestamptz,
  model_release_date date,
  official_score_eligible boolean,
  metadata jsonb not null default '{}'::jsonb,
  published boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.runs (
  round_id text not null references public.rounds(round_id) on delete cascade,
  run_id text not null,
  run_type text not null check (run_type in ('official', 'stability', 'mock', 'provider_smoke', 'retrospective')),
  mode text not null default '',
  mock boolean not null default false,
  official_score_eligible boolean not null default false,
  operator_selected_official boolean not null default false,
  methodology_version text not null default '',
  replicates integer not null default 1,
  model_count integer,
  valid_submissions integer,
  invalid_submissions integer,
  created_at_utc timestamptz,
  completed_at_utc timestamptz,
  report_path text,
  report_sha256 text,
  published boolean not null default false,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (round_id, run_id)
);

create table if not exists public.options (
  round_id text not null references public.rounds(round_id) on delete cascade,
  option_id text not null,
  name text not null,
  symbol text,
  tiingo_symbol text,
  asset_class text not null,
  category text not null,
  option_group text not null,
  risk_bucket text not null,
  exposure_description text not null,
  currency text not null default 'USD',
  is_cash boolean not null default false,
  is_benchmark boolean not null default false,
  include_in_universe boolean not null default true,
  entry_price numeric,
  entry_price_source text,
  entry_price_date date,
  published boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (round_id, option_id)
);

create table if not exists public.submissions (
  round_id text not null,
  run_id text not null,
  model_id text not null references public.models(model_id),
  provider text not null references public.model_providers(provider),
  mode text not null,
  run_type text not null,
  replicate_index integer not null default 1,
  replicate_count integer not null default 1,
  is_official_score boolean not null default false,
  selected_option_id text not null,
  confidence numeric not null,
  rationale_summary text not null,
  key_risks jsonb not null default '[]'::jsonb,
  usage jsonb,
  cost_usd numeric,
  metadata jsonb not null default '{}'::jsonb,
  submission_sha256 text not null,
  published boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (round_id, run_id, model_id, replicate_index),
  foreign key (round_id, run_id) references public.runs(round_id, run_id) on delete cascade,
  foreign key (round_id, selected_option_id) references public.options(round_id, option_id)
);

create table if not exists public.official_results (
  round_id text not null,
  run_id text not null,
  model_id text not null references public.models(model_id),
  provider text not null references public.model_providers(provider),
  mode text not null,
  selected_option_id text not null,
  confidence numeric not null,
  selected_asset_return numeric not null,
  sp500_return numeric not null,
  alpha_vs_sp500 numeric not null,
  regret_vs_best_option numeric,
  rank_among_options integer,
  beats_sp500 boolean not null,
  beats_cash boolean not null,
  cost_usd numeric,
  alpha_per_dollar numeric,
  rationale_summary text not null default '',
  key_risks jsonb not null default '[]'::jsonb,
  published boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (round_id, run_id, model_id),
  foreign key (round_id, run_id) references public.runs(round_id, run_id) on delete cascade,
  foreign key (round_id, selected_option_id) references public.options(round_id, option_id)
);

create table if not exists public.stability_results (
  round_id text not null,
  run_id text not null,
  model_id text not null references public.models(model_id),
  provider text not null references public.model_providers(provider),
  replicate_count integer not null,
  valid_replicates integer not null,
  invalid_replicates integer not null,
  selected_option_ids jsonb not null default '[]'::jsonb,
  pick_distribution jsonb not null default '{}'::jsonb,
  modal_pick text,
  modal_pick_count integer,
  consistency_rate numeric,
  average_repeated_return numeric,
  average_repeated_alpha_vs_sp500 numeric,
  best_replicate_return numeric,
  worst_replicate_return numeric,
  best_replicate_option_id text,
  worst_replicate_option_id text,
  modal_pick_return numeric,
  modal_pick_alpha_vs_sp500 numeric,
  total_cost_usd numeric,
  average_cost_usd numeric,
  notes text not null default '',
  published boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (round_id, run_id, model_id),
  foreign key (round_id, run_id) references public.runs(round_id, run_id) on delete cascade
);

create table if not exists public.option_returns (
  round_id text not null,
  run_id text not null,
  option_id text not null,
  label text not null,
  asset_symbol text not null,
  entry_price numeric,
  exit_price numeric,
  entry_price_source text,
  exit_price_source text,
  realized_return numeric,
  rank integer,
  is_benchmark boolean not null default false,
  is_cash boolean not null default false,
  published boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (round_id, run_id, option_id),
  foreign key (round_id, run_id) references public.runs(round_id, run_id) on delete cascade,
  foreign key (round_id, option_id) references public.options(round_id, option_id)
);

create table if not exists public.latest_leaderboard (
  slot text not null default 'latest',
  round_id text not null,
  run_id text not null,
  model_id text not null,
  provider text not null,
  selected_option_id text not null,
  confidence numeric not null,
  selected_asset_return numeric not null,
  sp500_return numeric not null,
  alpha_vs_sp500 numeric not null,
  regret_vs_best_option numeric,
  rank_among_options integer,
  beats_sp500 boolean not null,
  beats_cash boolean not null,
  published boolean not null default true,
  updated_at timestamptz not null default now(),
  primary key (slot, model_id)
);

create table if not exists public.cumulative_official_leaderboard (
  model_id text primary key,
  provider text not null,
  resolved_rounds integer not null,
  average_official_return numeric,
  average_sp500_return numeric,
  average_alpha_vs_sp500 numeric,
  median_alpha_vs_sp500 numeric,
  cumulative_model_return numeric,
  cumulative_sp500_return numeric,
  cumulative_log_alpha numeric,
  hit_rate_vs_sp500 numeric,
  hit_rate_vs_cash numeric,
  average_regret_vs_best_option numeric,
  best_round_alpha numeric,
  worst_round_alpha numeric,
  total_cost_usd numeric,
  average_cost_usd numeric,
  rounds_included text not null default '',
  published boolean not null default true,
  updated_at timestamptz not null default now()
);

create table if not exists public.cumulative_stability_leaderboard (
  model_id text primary key,
  provider text not null,
  resolved_rounds integer not null,
  total_replicates integer not null,
  average_repeated_return numeric,
  average_repeated_alpha_vs_sp500 numeric,
  median_repeated_alpha_vs_sp500 numeric,
  average_consistency_rate numeric,
  average_modal_pick_alpha_vs_sp500 numeric,
  average_modal_pick_return numeric,
  average_best_replicate_return numeric,
  average_worst_replicate_return numeric,
  best_round_repeated_alpha numeric,
  worst_round_repeated_alpha numeric,
  total_cost_usd numeric,
  average_cost_per_round numeric,
  rounds_included text not null default '',
  published boolean not null default true,
  updated_at timestamptz not null default now()
);

create table if not exists public.research_artifacts (
  round_id text not null references public.rounds(round_id) on delete cascade,
  path text not null,
  artifact_type text not null,
  model_facing boolean not null default false,
  sha256 text not null,
  size_bytes bigint not null,
  storage_bucket text,
  storage_path text,
  published boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (round_id, path)
);

create table if not exists public.audit_artifacts (
  round_id text not null references public.rounds(round_id) on delete cascade,
  run_id text not null default '',
  path text not null,
  artifact_type text not null,
  sha256 text not null,
  size_bytes bigint not null,
  validation_summary jsonb,
  warnings jsonb not null default '[]'::jsonb,
  storage_bucket text,
  storage_path text,
  published boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (round_id, run_id, path)
);

create table if not exists public.sync_events (
  id bigserial primary key,
  event_type text not null,
  round_id text,
  run_id text,
  status text not null check (status in ('success', 'skipped', 'failed')),
  message text not null default '',
  row_counts jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

do $$
declare
  target_table text;
begin
  foreach target_table in array array[
    'model_providers',
    'rounds',
    'models',
    'runs',
    'options',
    'submissions',
    'official_results',
    'stability_results',
    'option_returns',
    'research_artifacts',
    'audit_artifacts'
  ]
  loop
    execute format(
      'drop trigger if exists %I on public.%I',
      'set_' || target_table || '_updated_at',
      target_table
    );
    execute format(
      'create trigger %I before update on public.%I for each row execute function public.set_updated_at()',
      'set_' || target_table || '_updated_at',
      target_table
    );
  end loop;
end $$;

insert into public.model_providers (provider, display_name, website_url, published)
values
  ('openai', 'OpenAI', 'https://openai.com', true),
  ('anthropic', 'Anthropic', 'https://anthropic.com', true),
  ('google', 'Google', 'https://google.com', true),
  ('xai', 'xAI', 'https://x.ai', true)
on conflict (provider) do update
set display_name = excluded.display_name,
    website_url = excluded.website_url,
    published = excluded.published;

alter table public.model_providers enable row level security;
alter table public.rounds enable row level security;
alter table public.models enable row level security;
alter table public.runs enable row level security;
alter table public.options enable row level security;
alter table public.submissions enable row level security;
alter table public.official_results enable row level security;
alter table public.stability_results enable row level security;
alter table public.option_returns enable row level security;
alter table public.latest_leaderboard enable row level security;
alter table public.cumulative_official_leaderboard enable row level security;
alter table public.cumulative_stability_leaderboard enable row level security;
alter table public.research_artifacts enable row level security;
alter table public.audit_artifacts enable row level security;
alter table public.sync_events enable row level security;

do $$
declare
  target_table text;
begin
  foreach target_table in array array[
    'model_providers',
    'rounds',
    'models',
    'runs',
    'options',
    'submissions',
    'official_results',
    'stability_results',
    'option_returns',
    'latest_leaderboard',
    'cumulative_official_leaderboard',
    'cumulative_stability_leaderboard',
    'research_artifacts',
    'audit_artifacts'
  ]
  loop
    execute format(
      'drop policy if exists %I on public.%I',
      'anon can read published ' || target_table,
      target_table
    );
    execute format(
      'create policy %I on public.%I for select to anon using (published = true)',
      'anon can read published ' || target_table,
      target_table
    );
    execute format(
      'drop policy if exists %I on public.%I',
      'service role can manage ' || target_table,
      target_table
    );
    execute format(
      'create policy %I on public.%I for all to service_role using (true) with check (true)',
      'service role can manage ' || target_table,
      target_table
    );
  end loop;
end $$;

drop policy if exists "service role can insert sync events" on public.sync_events;
create policy "service role can insert sync events"
on public.sync_events
for insert
to service_role
with check (true);

drop policy if exists "service role can read sync events" on public.sync_events;
create policy "service role can read sync events"
on public.sync_events
for select
to service_role
using (true);

insert into storage.buckets (id, name, public)
values
  ('capitalbench-public-artifacts', 'capitalbench-public-artifacts', true),
  ('capitalbench-gated-artifacts', 'capitalbench-gated-artifacts', false)
on conflict (id) do update set public = excluded.public;

drop policy if exists "anon can read public benchmark artifacts" on storage.objects;
create policy "anon can read public benchmark artifacts"
on storage.objects
for select
to anon
using (bucket_id = 'capitalbench-public-artifacts');

drop policy if exists "service role can manage benchmark artifacts" on storage.objects;
create policy "service role can manage benchmark artifacts"
on storage.objects
for all
to service_role
using (bucket_id in ('capitalbench-public-artifacts', 'capitalbench-gated-artifacts'))
with check (bucket_id in ('capitalbench-public-artifacts', 'capitalbench-gated-artifacts'));
