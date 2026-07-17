# How CapitalBench Should Improve Portfolio V2

Generated on: `2026-07-17`

Protocol: `docs/v2_improvement_research_protocol.md`

Status: pre-resolution research. The active July 13 V2 pilot is frozen and its interim or final returns were not used.

## Bottom Line

The most important V2.1 change is not simply more market data. CapitalBench must make the model's candidate search auditable and systematic before asking it to allocate. Historical V1 decisions lose most of their available return before weighting: the best submitted holding is already far below the best allowed option. V2 still exposes only the final selected holdings, so it cannot distinguish a considered rejection from an option the model never evaluated.

The first V2 treatment also produced an average 62.5% pairwise allocation overlap across models, versus 60.0% in paired V1. Every model chose OIL and/or ENERGY, no model allocated to SPY, and the prompt's soft correlation instruction allowed a 100% ENERGY/OIL portfolio. V2 improved instrumentation, but it did not solve candidate breadth, calibration, or correlated-thesis control.

The recommended V2.1 treatment is one single-turn call with a compact nonredundant table, a required 6-8 candidate ledger spanning economic-exposure groups, forecasts for SPY and all finalists, a holding-level SPY hurdle, and a hard 50% cap on one economic exposure. Confidence-based sizing should wait until enough prospective forecasts exist to calibrate it.

## Where Historical Return Was Lost

`Search regret` is the best allowed return minus the best return among a model's submitted holdings. `Sizing regret` is the best submitted holding minus the submitted weighted portfolio. Both are hindsight diagnostics, not tradable strategies.

| Track | Decisions | Model alpha | Total regret | Search regret | Sizing regret | Search share | Top-5 capture |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Weekly | 154 | -0.75% | 9.58% | 6.29% | 3.29% | 65.70% | 41.56% |
| Monthly | 74 | -1.42% | 19.39% | 13.63% | 5.76% | 70.29% | 32.43% |

The selected holdings themselves do not show positive discrimination: equal-weighting each submitted selected set produced -0.72% weekly alpha and -1.46% monthly alpha. Relative to equal weight across the whole risky universe, the selected sets added -0.36% weekly and -0.83% monthly. This is why weight optimization alone cannot repair V2.

The 29 weekly and 15 monthly rounds overlap, and several model decisions share each market episode. These averages are stage diagnostics rather than independent observations or evidence that the hindsight-best option was knowable.

## Portfolio-Rule Counterfactuals

These rules reuse the exact submitted candidate set. They diagnose weighting and concentration; they do not establish a new predictive strategy.

| Rule | Weekly alpha | Weekly change | Monthly alpha | Monthly change |
| --- | --- | --- | --- | --- |
| Submitted | -0.75% | 0.00% | -1.42% | 0.00% |
| Equal selected | -0.72% | 0.03% | -1.46% | -0.04% |
| 50% holding cap | -0.75% | 0.00% | -1.49% | -0.07% |
| 35% holding cap | -0.72% | 0.03% | -1.53% | -0.10% |
| 25% SPY reserve | -0.56% | 0.19% | -1.07% | 0.36% |
| 50% SPY reserve | -0.37% | 0.37% | -0.71% | 0.71% |

A fixed SPY sleeve predictably moves a negative-alpha portfolio closer to zero, but it cannot create selection skill: its alpha is exactly a scaled version of submitted alpha. Holding caps and equal weighting are useful controls only if their paired improvements are stable; the moving-block intervals in `portfolio_rule_summary.csv` show the uncertainty.

## What V2 Actually Changed

| Model | V1 to V2 overlap | Turnover | V2 max weight | Effective holdings | SPY | Forecast alpha | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | 40.00% | 45.00% | 30.00% | 3.92 | 0.00% | 2.85% | 0.58 |
| openai-gpt-5-6-sol | 66.67% | 25.00% | 30.00% | 4.44 | 0.00% | 2.24% | 0.61 |
| xai-grok-4-3 | 50.00% | 60.00% | 60.00% | 1.92 | 0.00% | 4.48% | 0.62 |
| xai-grok-4-5 | 60.00% | 35.00% | 35.00% | 3.77 | 0.00% | 2.50% | 0.58 |

The V2 portfolio forecasts average 2.89% while SPY forecasts average -0.12%. The four confidence values cluster tightly around 0.60. Until outcomes accumulate, those numbers are declarations, not calibrated probabilities.

V2 input tokens increased 3.7% over paired V1. Despite the instruction to separate the latest five sessions from the prior sixteen, models placed an average 66.2% in the latest-window top quintile and only 26.2% in the prior-window top quintile. This does not prove the recent choices were wrong before resolution, but it shows that the new table did not prevent convergence on the most recent oil/energy move.

Explicit response text used the requested evidence unevenly:

| Evidence field | Models explicitly referencing it |
| --- | --- |
| recent window | 4/4 |
| prior window | 2/4 |
| spy relative | 4/4 |
| volatility | 2/4 |
| drawdown | 1/4 |
| volume | 0/4 |
| correlation or beta | 2/4 |
| 52 week position | 0/4 |
| catalyst | 4/4 |
| counter case | 2/4 |

Keyword traces are conservative, but they show why adding fields is not the same as using them. The model-facing contract should make comparison fields auditable rather than relying on narrative rationales.

## Decision-Table Audit

The V2 context has 70 rows and 15 columns. A nonredundant research variant retains every unique numeric signal in 12 columns and is 15.0% smaller. Five-session raw return and five-session SPY-relative return have within-round rank correlation 1.000; with the SPY return already in the header, one is mechanically reconstructable from the other. The date is repeated on every row and pass status is repeated on 69 rows.

The compact variant is not yet a benchmark input. It demonstrates that V2 can reduce retrieval burden without deleting an option or adding a recommendation score.

## Contract Gaps

| Check | Present | Interpretation |
| --- | --- | --- |
| full universe shortlist | No | No auditable shortlist; the prompt explicitly prohibits a ranked list. |
| forecasts for rejected finalists | No | Only selected holdings receive expected-return forecasts. |
| explicit spy forecast | Yes | SPY forecast is required. |
| selected holding must beat spy | No | The portfolio is compared with SPY, but no holding-level hurdle is enforced. |
| hard economic exposure cap | No | Correlation is a soft consideration, not a validated constraint. |
| forecast interval | No | Only point forecasts are recorded. |
| beat spy probability | Yes | A probability is recorded but has no prior calibration. |
| holding invalidation | Yes | Every selected holding requires an invalidation condition. |
| allows spy | Yes | SPY is available but no fallback rule is specified. |
| single turn non agentic | Yes | The benchmark contract is preserved. |

## Hypothesis Results

| Hypothesis | Verdict | Evidence | Limit |
| --- | --- | --- | --- |
| candidate search is primary bottleneck | supported as diagnosis | Search accounts for 65.7% of weekly and 70.3% of monthly oracle regret; equal-selected alpha remains negative. | Oracle regret uses hindsight and does not prove the winner was predictable. |
| flat context encourages selective use | partially supported | V2 added 3.7% input tokens, allocated 66.2% to latest-window top-quintile assets, and explicitly referenced several supplied fields rarely or never. | No paid order-permutation experiment was run, so positional causality is unproven. |
| relative spy hurdle is too weak | contract gap confirmed | V2 requires a portfolio-level SPY comparison but no finalist or holding is required to clear SPY. | The return effect of a hard holding-level hurdle requires prospective forecasts and outcomes. |
| forecast confidence is not ready for sizing | instrument first | Only four unresolved probabilities exist and their cross-model standard deviation is 0.018. | No resolved V2 confidence history exists yet. |
| soft correlation wording allows shared bets | supported structurally | Average V2 pairwise allocation overlap is 62.5%, and a valid portfolio allocated 100% to ENERGY plus OIL. | Diversification can lower or raise realized return; a hard cluster cap must be prospectively tested. |
| more unstructured context will not fix v2 | supported as rejection of default | The first V2 input expansion did not broaden the dominant thesis, while a 15% table reduction can remove only repeated or reconstructable fields. | Specific complete data families may still add value and require separate ablations. |

## Evidence-Ranked Interventions

| Priority | Intervention | Rating | Why |
| --- | --- | --- | --- |
| 1 | auditable full universe candidate ledger | implement | Search regret is 65.7% of weekly and 70.3% of monthly total oracle regret; current V2 records only selected holdings. |
| 2 | compact nonredundant decision table | prospective_test | The current table is dense and contains fields that do not add within-round ordering information; long-context and table-reference errors are established LLM failure modes. |
| 3 | holding level spy hurdle | prospective_test | V2 asks for portfolio-level comparison but does not enforce a holding-level relative-return condition. |
| 4 | economic exposure clusters and cap | prospective_test | V2 pairwise allocation overlap averages 62.5%; one valid portfolio used only ENERGY and OIL despite the soft correlation instruction. |
| 5 | forecast ranges and calibration ledger | instrument_first | The first V2 confidences occupy only a narrow 0.018 standard-deviation band and have no resolved calibration history. |
| 6 | structured event exposure matrix | prospective_test | All four V2 models concentrated on briefing catalysts, but the briefing is narrative and does not provide complete option-by-event comparison. |
| 7 | fixed spy sleeve as alpha solution | reject | It mechanically shrinks both positive and negative alpha; it can control risk but cannot create selection skill. |
| 8 | add all available data | reject | V2 already increased input size while producing high cross-model thesis overlap; more context does not guarantee better retrieval. |
| 9 | increase reasoning effort only | instrument_first | Observed V2 reasoning usage ranges from 367 to 4088 tokens, but one unresolved round cannot link more tokens to better returns. |

## Additional Data

| Data family | Score / 25 | Rating | Decision |
| --- | --- | --- | --- |
| economic exposure map | 25 | implement | Required to detect ENERGY plus OIL and other cross-asset expressions of the same economic bet. |
| compact price path | 24 | prospective_test | Keep existing path data but remove redundant columns and test a more readable table. |
| structured event calendar | 24 | prospective_test | Convert scheduled events already researched into date, uncertainty, and affected-exposure fields without a directional recommendation. |
| market breadth and regime | 23 | keep_compact | Already present in V2; test whether a short regime label is used more reliably than a dense metric header. |
| valuation | 19 | monthly_only_test | More plausible for the monthly track than a seven-day winner; avoid spending weekly context on it. |
| analyst revision breadth | 17 | instrument_first | Potentially useful around earnings, but ETF/index coverage and reproducible licensing must be solved first. |
| fund flows and crowding | 15 | instrument_first | Evidence is horizon- and market-dependent; define a complete mechanical source before model use. |
| more unstructured news | 13 | reject | The existing briefing already anchors decisions; more narrative increases context and selection bias without complete option comparison. |
| options implied information | 13 | reject_for_now | Coverage, normalization, and cost are poor across a heterogeneous 70-option universe. |

Research supports disciplined use of text and event information, not indiscriminate context expansion. News-derived language-model signals have shown out-of-sample return information, while separate work finds that LLMs over-extrapolate historical stock returns and produce optimistic, narrow forecasts. See [Lopez-Lira and Tang](https://arxiv.org/abs/2304.07619) and [Chen et al.](https://arxiv.org/abs/2409.11540). Short-horizon reversal and medium-horizon momentum also operate at different horizons, so V2 should force a continuation-versus-reversal comparison rather than treating one trailing return as universally directional: [Lehmann](https://www.nber.org/papers/w2533) and [Jegadeesh and Titman](https://doi.org/10.1111/j.1540-6261.1993.tb04702.x).

The V2 confidence field should be treated as an uncalibrated forecast. Research documents overconfidence in post-aligned models, while live forecasting benchmarks rely on proper scores and many resolved questions rather than trusting verbal confidence directly: [Zhang et al.](https://arxiv.org/abs/2404.02655) and [ForecastBench methodology](https://www.forecastbench.org/docs/).

Analyst revisions and option-implied information can contain return information, but CapitalBench uses heterogeneous ETFs and macro assets. Coverage and licensing must be solved before those fields can be fair model inputs. Primary examples include [Asquith, Mikhail, and Au](https://www.nber.org/papers/w9246) and [Muravyev, Pearson, and Pollet](https://doi.org/10.2139/ssrn.2851560).

## Proposed V2.1 Contract

1. Keep one single-turn, non-agentic call and the complete 70-option universe.
2. Replace redundant table fields with the compact decision table; keep frozen option order.
3. Add a static economic-exposure cluster to every option and a compact scheduled-event table.
4. Require a 6-8 row candidate ledger before the final portfolio. It must include SPY, span at least four economic-exposure clusters, and retain rejected finalists.
5. Record low/base/high return forecasts for SPY and every finalist, the evidence used, continuation case, reversal case, and forecast invalidation.
6. Permit an active holding only when its base forecast exceeds the SPY base forecast. If none qualify, 100% SPY is valid.
7. Cap one economic exposure at 50%, including equivalent bets expressed through different asset classes. Do not use confidence to loosen the cap yet.
8. Save the candidate ledger and forecasts for calibration; continue scoring only the final frozen portfolio.

This staged format is an auditable decision scaffold, not hidden chain-of-thought. Long-context research shows that information position can materially affect retrieval, and table research documents incorrect or omitted values even when structure is understood: [Liu et al.](https://aclanthology.org/2024.tacl-1.9/) and [Yang et al.](https://aclanthology.org/2026.acl-long.762/).

## What Not To Claim Yet

- The unresolved V2 forecasts cannot be called accurate or inaccurate.
- A candidate ledger, compact table, or exposure cap has not yet demonstrated positive alpha.
- More reasoning tokens are not proven to improve these portfolios.
- A fixed SPY reserve reduces underperformance mechanically but does not make the model a better selector.
- Historical exact winners are not a valid prompt-tuning target.

## Prospective Test

After the July 20 V2 decision is recorded, freeze one combined V2.1 treatment and compare it with unchanged V2 on the same future weekly date, models, universe, and prices. The primary endpoint is paired realized alpha. Candidate capture, forecast rank correlation, point error, interval coverage, Brier score, and exposure concentration explain the result. One round is a screen; adoption requires multiple non-overlapping weekly windows and later monthly confirmation.

No second model call, provider search, retrospective rerun, or monthly V2.1 call is required for the first screen.

## Reproducibility

```bash
python scripts/analyze_model_predictability.py --rounds-dir rounds --output output/model_performance_predictability --report-copy docs/model_performance_predictability_report.md
python scripts/analyze_v2_improvements.py --rounds-dir rounds --output output/v2_improvement_research --report-copy docs/v2_improvement_research_report.md
```
