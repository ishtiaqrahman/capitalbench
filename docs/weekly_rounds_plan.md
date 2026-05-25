# Weekly CapitalBench Rounds Plan

This plan adds a weekly CapitalBench cadence alongside the existing one-month
cadence as a separate benchmark track. Weekly and monthly results must not be
mixed in leaderboards, cumulative scores, homepage summary cards, or public
read-model tables.

## Hard Track Separation

CapitalBench should have two independent tracks:

- Monthly track: one-month allocation rounds such as `CB-2026-05-24-1M`
- Weekly track: one-week allocation rounds such as `CB-2026-05-24-1W`

The tracks may share source research work when they are launched on the same
decision date, but the benchmark artifacts must remain separate:

- separate round directory
- separate manifest
- separate prompt
- separate model input packet
- separate hashes
- separate official run
- separate entry/exit price files
- separate automation job
- separate latest leaderboard
- separate cumulative leaderboard
- separate website display lane

There should be no combined weekly-plus-monthly model score. If a page shows
both tracks, it must present them as adjacent but distinct sections.

## First Weekly Round

Start with a weekly round dated Sunday, May 24, 2026:

- Round ID: `CB-2026-05-24-1W`
- Cadence: weekly
- Horizon: one week
- Decision date: `2026-05-24`
- Decision deadline: `2026-05-25T01:00:00Z`
- Entry date: `2026-05-22`
- Exit date: `2026-05-29`
- Resolution target: `2026-05-29T23:30:00Z`
- Universe: `v2.0`
- Submission format: `portfolio`
- Portfolio constraints: same as current monthly portfolio rounds

Because May 24, 2026 is the same decision date as the current monthly round,
the first weekly round can reuse the same research artifacts and trailing-return
table. The prompt and manifest must be different because the scoring horizon is
one week, not one month.

## Weekly Protocol

Use one round directory per weekly run:

```text
rounds/CB-YYYY-MM-DD-1W/
```

Use the existing monthly naming convention for monthly runs:

```text
rounds/CB-YYYY-MM-DD-1M/
```

Weekly rounds should use:

- the same model roster as the monthly official run
- the same 65-option universe unless the monthly protocol changes the universe
- the same portfolio protocol unless explicitly changed before a round freezes
- the same no-browsing/no-tool provider execution rules
- entry price from the last completed trading close before the decision deadline
- exit price from the next Friday close, adjusted to the prior trading day when Friday is a market holiday

The weekly prompt must say "one week" throughout. The current default prompt text
contains one-month wording, so weekly rounds should not use it unchanged.

## Input Generation

For weeks with both a weekly and monthly run on the same decision date:

1. Generate or import the monthly research packet once.
2. Reuse `research/`, `briefing.md`, and `market_data/universe_trailing_returns.*`
   only as source material for the weekly round.
3. Use separate `manifest.yaml`, `prompt.md`, `hashes.json`, `model_input.md`,
   run folders, price files, and automation jobs.
4. Re-hash each track independently after the weekly prompt and manifest are
   finalized.

For weeks with only a weekly run:

1. Produce a compact fact packet focused on the last 7 calendar days and the
   next 7 calendar days.
2. Include market-moving facts, scheduled releases, major earnings/events, and
   asset-specific headlines.
3. Avoid long monthly-style macro tables unless the value and recent change are
   both directly relevant.
4. Always include the full-universe trailing-return table as of the latest
   available trading close.

The weekly model-facing briefing should stay factual. It should not rank
options, map facts to options, or tell models which assets benefit.

## Manual First-Run Procedure

For the first weekly round, create the round manually from the current monthly
round artifacts:

```bash
capitalbench init-round \
  --round-id CB-2026-05-24-1W \
  --rounds-dir rounds \
  --universe configs/universes/capitalbench_universe_v2_0.yaml \
  --universe-version v2.0 \
  --submission-format portfolio
```

Then edit `manifest.yaml`:

```yaml
round_id: CB-2026-05-24-1W
title: CapitalBench May 24 2026 One-Week Portfolio Round
description: One-week CapitalBench portfolio evaluation round using the frozen May 24, 2026 briefing and expanded v2.0 universe.
decision_date: '2026-05-24'
decision_deadline: '2026-05-25T01:00:00Z'
horizon: one week
methodology_version: portfolio-v1.0-weekly
universe_version: v2.0
submission_format: portfolio
entry_date: '2026-05-22'
exit_date: '2026-05-29'
```

Copy or import the research artifacts from the monthly round, then replace the
weekly prompt text so every horizon reference says one week. Build the
model-facing packet, hash the round, run providers, validate, accept, fetch
entry prices, sync web rows, commit, and push using the same official run
protocol as monthly rounds.

## Required Code Changes

These changes should be made before the first weekly result resolves.

### CLI And Prompting

- Add a first-class horizon/cadence option to `init-round`, for example
  `--horizon weekly|monthly`.
- Generate horizon-specific default prompt text so weekly rounds do not inherit
  one-month wording.
- Keep `manifest.horizon`, `entry_date`, and `exit_date` as the scoring source
  of truth.
- Add a validation check that flags prompt text containing "one month" when
  `manifest.horizon` is one week.

### Result Aggregation

Do not mix one-week and one-month results in the same latest view, cumulative
score, or public read-model row set.

Add a horizon filter to:

- `cumulative_status`
- `publish_latest`
- `publish_cumulative`
- `sync_latest_leaderboard`
- `sync_cumulative_leaderboards`

Use either `horizon_days` or an explicit cadence field. `horizon_days` already
exists in the public round record and Supabase schema, so the fastest safe rule
is:

- weekly: `horizon_days <= 10`
- monthly: `horizon_days >= 28`

The existing Supabase `latest_leaderboard` table already has `slot`, so it can
store `latest_weekly` and `latest_monthly`. The cumulative read tables currently
key only by `model_id`; they need a `slot` or `cadence` key before weekly and
monthly cumulative views can coexist. The sync code must delete/upsert only the
slot being refreshed, never all published cumulative rows across both tracks.

### Automation

The existing resolver can resolve weekly rounds because it uses `exit_date`.
No separate resolver is needed.

Keep the scheduled resolver every 30 minutes. Weekly rounds should schedule
resolution for Friday at `23:30:00Z`. If price data is not available yet, the
existing retry path can keep trying.

## Website Display

### Homepage

Replace the single "latest round" concept with two visible current tracks:

- Latest Weekly Round
- Latest Monthly Round

Each card should show:

- round id
- status
- entry date
- exit date
- official run id
- scoring target countdown
- allocation summary while pending
- realized leaderboard link after resolution

Do not use combined headline counts unless the label explicitly says "all
tracks." Prefer separate weekly and monthly counts in the primary homepage UI.

### Rounds Index

Add:

- Horizon column
- Cadence filter or tabs: All, Weekly, Monthly
- Status filter if the table gets crowded

Default sort remains decision deadline descending. When weekly and monthly
rounds share a decision deadline, show the weekly and monthly rows adjacent.

### Leaderboards

Add separate horizon-aware routes:

```text
/leaderboards/latest-weekly
/leaderboards/latest-monthly
/leaderboards/cumulative-weekly
/leaderboards/cumulative-monthly
```

The existing `/leaderboards/latest` can remain as a hub or redirect to the
monthly view for backward compatibility, but it should not silently switch to
weekly just because a weekly round has the newest deadline. If it becomes a
hub, it should link to both tracks and avoid showing a mixed leaderboard table.

### Round Page

The current round page works for weekly rounds with small copy changes:

- show the horizon prominently near the status strip
- call the unresolved state "Exit pending" as today
- keep weekly interim tracking optional

For a one-week round, interim weekly charting is usually not useful because the
first weekly snapshot is the final exit snapshot. Do not add intraweek charts
unless daily tracking becomes a deliberate feature.

## Suggested Implementation Order

1. Add the first weekly round manually using copied May 24 research artifacts.
2. Patch the weekly prompt so the model sees one-week instructions only.
3. Add horizon/cadence filtering to cumulative/latest publishing and web sync.
4. Update Supabase cumulative read tables to support `slot` or `cadence`.
5. Update website homepage, rounds table, and leaderboard routes.
6. Run and accept `CB-2026-05-24-1W`.
7. Sync web rows and deploy.
8. Before May 29, verify that weekly and monthly cumulative views remain
   separate.

## Non-Goals For The First Weekly Round

- Do not add a new model roster.
- Do not change portfolio constraints.
- Do not change the universe.
- Do not create a combined weekly-plus-monthly model score.
- Do not add daily performance charts unless the benchmark explicitly adopts
  daily interim tracking.
