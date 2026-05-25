alter table public.cumulative_official_leaderboard
  add column if not exists slot text not null default 'cumulative_monthly';

alter table public.cumulative_stability_leaderboard
  add column if not exists slot text not null default 'cumulative_monthly';

alter table public.cumulative_official_leaderboard
  drop constraint if exists cumulative_official_leaderboard_pkey,
  add primary key (slot, model_id);

alter table public.cumulative_stability_leaderboard
  drop constraint if exists cumulative_stability_leaderboard_pkey,
  add primary key (slot, model_id);

alter table public.latest_leaderboard
  drop constraint if exists latest_leaderboard_slot_check,
  add constraint latest_leaderboard_slot_check
    check (slot in ('latest', 'latest_weekly', 'latest_monthly'));

alter table public.cumulative_official_leaderboard
  drop constraint if exists cumulative_official_leaderboard_slot_check,
  add constraint cumulative_official_leaderboard_slot_check
    check (slot in ('cumulative_all', 'cumulative_weekly', 'cumulative_monthly'));

alter table public.cumulative_stability_leaderboard
  drop constraint if exists cumulative_stability_leaderboard_slot_check,
  add constraint cumulative_stability_leaderboard_slot_check
    check (slot in ('cumulative_all', 'cumulative_weekly', 'cumulative_monthly'));
