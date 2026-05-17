alter table public.rounds
  add column if not exists universe_version text;

alter table public.options
  add column if not exists sort_order integer;

create index if not exists options_round_sort_order_idx
  on public.options (round_id, sort_order, option_id);
