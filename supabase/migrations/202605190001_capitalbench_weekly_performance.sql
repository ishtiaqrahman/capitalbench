create table if not exists public.round_weekly_prices (
  round_id text not null references public.rounds(round_id) on delete cascade,
  target_date date not null,
  price_date date not null,
  option_id text not null,
  symbol text,
  price numeric,
  price_source text,
  published boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (round_id, target_date, option_id),
  foreign key (round_id, option_id) references public.options(round_id, option_id)
);

create table if not exists public.round_weekly_performance (
  round_id text not null,
  run_id text not null,
  model_id text not null references public.models(model_id),
  provider text not null references public.model_providers(provider),
  target_date date not null,
  price_date date not null,
  days_elapsed integer not null,
  run_type text not null default 'official',
  submission_format text not null default 'single_pick' check (submission_format in ('single_pick', 'portfolio')),
  selected_option_id text not null,
  holding_count integer not null default 1 check (holding_count >= 1),
  model_return numeric not null,
  sp500_return numeric not null,
  alpha_vs_sp500 numeric not null,
  price_status text not null default 'complete',
  published boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (round_id, run_id, model_id, target_date),
  foreign key (round_id, run_id) references public.runs(round_id, run_id) on delete cascade,
  foreign key (round_id, selected_option_id) references public.options(round_id, option_id)
);

create index if not exists round_weekly_performance_round_date_idx
  on public.round_weekly_performance (round_id, run_id, target_date);

create index if not exists round_weekly_prices_round_date_idx
  on public.round_weekly_prices (round_id, target_date);

drop trigger if exists set_round_weekly_prices_updated_at on public.round_weekly_prices;
create trigger set_round_weekly_prices_updated_at
before update on public.round_weekly_prices
for each row execute function public.set_updated_at();

drop trigger if exists set_round_weekly_performance_updated_at on public.round_weekly_performance;
create trigger set_round_weekly_performance_updated_at
before update on public.round_weekly_performance
for each row execute function public.set_updated_at();

alter table public.round_weekly_prices enable row level security;
alter table public.round_weekly_performance enable row level security;

drop policy if exists "anon can read published round_weekly_prices" on public.round_weekly_prices;
create policy "anon can read published round_weekly_prices"
on public.round_weekly_prices
for select
to anon
using (published = true);

drop policy if exists "service role can manage round_weekly_prices" on public.round_weekly_prices;
create policy "service role can manage round_weekly_prices"
on public.round_weekly_prices
for all
to service_role
using (true)
with check (true);

drop policy if exists "anon can read published round_weekly_performance" on public.round_weekly_performance;
create policy "anon can read published round_weekly_performance"
on public.round_weekly_performance
for select
to anon
using (published = true);

drop policy if exists "service role can manage round_weekly_performance" on public.round_weekly_performance;
create policy "service role can manage round_weekly_performance"
on public.round_weekly_performance
for all
to service_role
using (true)
with check (true);
