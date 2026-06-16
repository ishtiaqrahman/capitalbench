# Benchmark Comparison Sets

Benchmark Comparison Sets keep model rankings fair when new models enter CapitalBench.

## Definitions

- **Comparison Set**: a fixed model roster scored only on rounds every model in that roster completed.
- **Current Benchmark**: the newest qualified comparison set for a track.
- **Shared Rounds**: resolved rounds included because every set model has an official result.
- **Excluded For Fairness**: resolved rounds after the set started where at least one set model is missing.
- **All Available History**: context across all resolved rounds in a track. It can include unequal model histories and is not the primary fair ranking view.

## Qualification

- Weekly comparison sets qualify at 6 shared resolved weekly rounds.
- Monthly comparison sets qualify at 3 shared resolved monthly rounds.
- If multiple sets qualify in one track, the newest qualified set becomes the Current Benchmark.
- There is exactly one Current Weekly Benchmark and one Current Monthly Benchmark when qualified sets exist.

## Missed Round Rule

If any model in a comparison set misses a resolved round, that round is excluded from the set for every model.

This keeps every ranked row on the exact same market windows, same volatility, and same hindsight oracle opportunity set.

## Score Formula

For each model in a set:

```text
CapitalBench Score =
100 * sum(model portfolio returns across included shared rounds)
/
sum(max possible returns across included shared rounds)
```

The max possible reference is the best eligible asset in each included round in hindsight. The max possible row is always 100.

## Automatic Set Creation

CapitalBench automatically creates comparison sets from selected official run
rosters. During the site-data build, each weekly and monthly official run is
checked in chronological order:

1. Read the accepted model roster from the operator-selected official run.
2. Check whether that roster is already contained in an existing set for the
   same track.
3. If yes, do not create a new set.
4. If no, create a new set starting at that round.

This means temporary model outages do not create smaller benchmark sets. If a
six-model set already exists and one model is unavailable for several weekly or
monthly runs, those smaller rosters are already covered by the larger set, so no
new set is created. Resolved rounds where a required set model is missing are
excluded from that set for everyone.

## Configuration Overrides

`benchmark_sets.yaml` defines the policy and optional explicit set metadata:

```yaml
version: benchmark_sets_v1
qualification_thresholds:
  weekly: 6
  monthly: 3
sets:
  - set_id: weekly-set-2026-05-28
    track: weekly
    label: "Weekly Set: May 28, 2026"
    short_label: "May 28 Weekly"
    description: "Weekly comparison set that adds Claude Opus 4.8."
    started_round_id: CB-2026-05-28-1W
    model_ids:
      - anthropic-claude-opus-4-7
      - anthropic-claude-opus-4-8
      - google-gemini-3-1-pro
      - openai-gpt-5-5
      - xai-grok-4-3
```

Configured sets are loaded first. The automatic discovery step then adds any
uncovered official rosters. A set only covers rounds at or after its own
`started_round_id`; future set metadata cannot hide an earlier new-model cohort.
Validation also fails if a later set is redundant because an earlier set or
larger roster already covers it. Use `benchmark_sets.yaml` when a set needs a
stable label, description, or manually chosen start round; otherwise a new model
roster does not require a manual YAML entry.

The build computes included rounds, excluded rounds, scores, qualification, and current benchmark status.

## Adding A New Model

1. Add the model to future official weekly and monthly runs only.
2. Run the official round normally.
3. Build the site data.
4. The generator opens a new comparison set automatically if no already-started
   set for that track contains the official run roster.
5. Add a YAML override only if the generated label, description, or start round
   needs to be curated.
6. Run the validation commands.

Do not rerun old rounds for the new model after outcomes may be knowable.

## Website Surfaces

- Homepage: shows the featured weekly and monthly comparison sets. A qualified set appears as the Current Benchmark; otherwise the best available set appears as forming.
- `/leaderboards/benchmark-sets/`: lists every living comparison set.
- `/leaderboards/benchmark-sets/<set_id>/`: dedicated score page for one set, including roster, included rounds, excluded rounds, and score calculation.
- `/leaderboards/cumulative-weekly/` and `/leaderboards/cumulative-monthly/`: all-available history context.

## Validation

Run:

```bash
npm --prefix apps/web run build
npm --prefix apps/web run seo:check
```

The public data validation checks that:

- each configured set references real models and a real start round;
- every selected official run roster is covered by at least one generated set;
- included rounds contain every set model;
- excluded rounds identify missing set models;
- no weekly set is current before 6 shared rounds;
- no monthly set is current before 3 shared rounds;
- at most one current set exists per track;
- API and rendered pages are generated from the same read model.
