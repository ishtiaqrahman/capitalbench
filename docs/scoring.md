# Scoring

CapitalBench scores each valid submission against realized local prices.

Preferred price file format:

```text
option_id,symbol,date,close,adj_close
SP500,SPY,2026-06-02,500.00,500.00
NASDAQ100,QQQ,2026-06-02,430.00,430.00
CASH,,2026-06-02,1.00,1.00
```

Rows may use `option_id` or `symbol`; `option_id` is preferred. CapitalBench
uses `adj_close` when available. If only `close` is supplied, scoring is allowed
but a warning is recorded in `results/price_warnings.json`.

For Tiingo price fetching, CapitalBench uses a selected-only workflow:

```bash
capitalbench fetch-prices \
  --round rounds/<id> \
  --run-id <run_id> \
  --entry-date YYYY-MM-DD \
  --exit-date YYYY-MM-DD
```

That command fetches only the assets needed by parsed submissions, plus the
S&P 500 benchmark and CASH. For `single_pick` rounds, that means selected
options. For `portfolio` rounds, it means every holding in every parsed
portfolio. It does not fetch every option in the universe.
If only one side of the scoring window is available, pass `--side entry` or
`--side exit` and provide only the matching date.

To populate `regret_vs_best_option` and `rank_among_options`, fetch scoring
prices for the full frozen option universe:

```bash
capitalbench fetch-prices \
  --round rounds/<id> \
  --run-id <run_id> \
  --entry-date YYYY-MM-DD \
  --exit-date YYYY-MM-DD \
  --full-universe
```

Full-universe scoring prices are different from the prompt-context trailing
return artifact. They write `prices/entry_prices.csv` and
`prices/exit_prices.csv` for every option in `options.yaml`.
For an unresolved round, use `--side entry --full-universe` to write only
`prices/entry_prices.csv` for the full frozen universe; fetch exit prices only
after the exit date resolves.

Price fetching is strict about dates. For each Tiingo request, CapitalBench
requires a returned row whose date exactly matches the requested `entry-date`
or `exit-date`. It does not silently use the nearest available trading day. If
the requested date is a market holiday, weekend, or otherwise absent from
Tiingo EOD data, the command fails clearly and the operator must choose the
correct date according to the round manifest.

Full-universe trailing returns for prompt context use a separate command:

```bash
capitalbench fetch-universe-performance \
  --round rounds/<id> \
  --as-of-date YYYY-MM-DD
```

That command writes `market_data/universe_trailing_returns.csv`,
`market_data/universe_trailing_returns.md`, and
`market_data/universe_trailing_returns.json`. It fetches every non-CASH option
and calculates 7-day, 30-day, 6-month, and 1-year returns from Tiingo adjusted
close data. It does not create scoring prices and does not affect leaderboards.

For each option:

```text
option_return = exit_price / entry_price - 1
```

Cash is treated as a zero return unless cash prices are explicitly supplied.

Each round freezes a versioned universe with CASH plus public tickers that are
priced through the Tiingo EOD workflow. All non-cash universe tickers should
pass Tiingo validation before a public round is frozen.

For a `single_pick` submission:

```text
selected_asset_return = option_return(selected_option_id)
```

For a `portfolio` submission:

```text
portfolio_return = sum(allocation_weight * option_return(option_id))
selected_asset_return = portfolio_return
```

`selected_asset_return` remains the common score-return column so cumulative
reports can compare rounds with different submission formats. Portfolio rounds
also write `portfolio_return` and allocation diagnostics for audit clarity.

For each official model submission:

- `submission_format`: `single_pick` or `portfolio`
- `selected_asset_return`: return of the selected option, or weighted portfolio return
- `portfolio_return`: weighted portfolio return when the round uses portfolio submissions
- `sp500_return`: return of the S&P 500 benchmark option
- `alpha_vs_sp500`: selected return minus S&P 500 return
- `regret_vs_best_option`: best available option return minus selected return, only when full-universe prices are supplied
- `rank_among_options`: realized rank of the selected option among all options for single-pick rounds, only when full-universe prices are supplied
- `holding_count`: number of holdings in the scored submission
- `max_allocation_bps`: largest allocation in basis points
- `cash_allocation_bps`: cash allocation in basis points
- `benchmark_allocation_bps`: benchmark allocation in basis points
- `concentration_hhi`: allocation concentration on a 0 to 1 scale, where 1.0 means one 100% holding
- `beats_sp500`: whether the decision return beat the S&P 500
- `beats_cash`: whether the decision return beat cash
- `alpha_per_dollar`: alpha divided by cost, only when `cost_usd > 0`

Latest-test tables sort by `alpha_vs_sp500` descending. Ties are resolved by
lower regret, higher confidence, and then model id. Overall scorecards use
CapitalBench Score, defined as `100 * selected_asset_return / max_possible_return`
for each completed test where full-universe scoring returns exist.

The benchmark option must be identifiable as S&P 500, usually with
`is_benchmark: true` and `asset_symbol: SPY`.

## Official One-Shot Leaderboard

The official leaderboard uses exactly one valid submission per model from a run
with `run_type: official`. It is the public one-shot result for a completed
test. Stability runs do not feed into this leaderboard.

Official scoring writes:

```text
runs/<run_id>/results/returns.csv
runs/<run_id>/results/leaderboard.csv
runs/<run_id>/results/allocations.csv, for portfolio-aware allocation audit rows
```

## Multi-Run Stability Analysis

Stability analysis uses `run_type: stability` and multiple replicates per model,
usually five. It answers a different question: does the model keep choosing the
same asset when asked the same question multiple times?

Stability scoring writes:

```text
runs/<run_id>/results/returns.csv
runs/<run_id>/results/stability.csv
```

`stability.csv` includes:

- pick distribution
- modal pick
- consistency rate
- average repeated return
- average repeated alpha versus S&P 500
- best and worst repeated result
- total and average cost when cost data exists

Tie rule for modal pick: if two or more options are tied for most frequent pick,
choose the tied option with the highest realized return and record a note.

Example:

```text
Model picks: QQQ, QQQ, SPY, QQQ, TLT
Asset returns: QQQ +4%, SPY +2%, TLT -1%

Average repeated return:
(4 + 4 + 2 + 4 - 1) / 5 = 2.6%

Modal pick:
QQQ

Consistency:
3 / 5 = 60%
```

This is not an official leaderboard and should not be combined with the
official score.

## Latest Round Leaderboard

The latest round leaderboard uses only the newest resolved round's official
one-shot run. It is a standalone round result. Cumulative results and stability
results are separate views.

Publishing writes:

```text
latest/
  latest_round_leaderboard.csv
  latest_round_report.md
```

## Cumulative Official Leaderboard

Across multiple resolved rounds, each round counts as one game. For each model,
CapitalBench computes a per-round CapitalBench Score:

```text
capitalbench_score = 100 * selected_asset_return / max_possible_return
```

`max_possible_return` is the highest realized return among scored options in the
frozen universe for that round. A score of 100 means the model matched the
maximum possible return in that completed window. The cumulative score averages
the per-round CapitalBench Scores across resolved rounds where that model has
an official result.

Example:

```text
Round 1:
Model A return = +4%
Max possible return = +8%
Model A CapitalBench Score = 50

Round 2:
Model A return = +3%
Max possible return = +6%
Model A CapitalBench Score = 50

Cumulative CapitalBench Score:
(50 + 50) / 2 = 50
```

The cumulative official view also includes average model return, S&P 500
comparison, hit rates, regret, and cost summaries when cost data exists. Those
fields are supporting context, not the primary benchmark score.

Models may have different `resolved_rounds` counts because new models enter
only in future rounds. CapitalBench does not backfill new models into old
official rounds. The primary cumulative scorecard is sorted by average
CapitalBench Score. Supporting alpha tables may sort by average alpha versus
the S&P 500.

## Cumulative Stability Leaderboard

The cumulative stability table averages repeated-run alpha and consistency
metrics across resolved rounds. It is separate from the official cumulative
leaderboard.

Example:

```text
Round 1:
average repeated alpha = +1.4%
consistency = 60%

Round 2:
average repeated alpha = +0.8%
consistency = 80%

Cumulative stability:
average repeated alpha = +1.1%
average consistency = 70%
```

The cumulative stability leaderboard is sorted by average repeated-run alpha
versus the S&P 500, then average consistency, then average modal-pick alpha.
There is no combined official-plus-stability score.
