# Prompt Sensitivity Research

Generated at: `2026-06-25T04:06:41Z`

Scope: observational analysis of saved CapitalBench prompts, official model submissions, and generated market-data appendices. This is not a controlled rerun experiment, so findings are stated as associations unless the evidence is purely textual.

## Executive Findings

1. Prompt wording changed more than formatting. Across the saved history, the largest prompt shifts were: single-pick to portfolio construction, permission to use internal priors, explicit scoring-window discipline, briefing-bias discipline around mechanical return tables, a temporary benchmark/mean-reversion check, and the June 24 price-history discipline.
2. The June 24 price-history rule is associated with a sharp drop in pure named momentum exposure: explicit `MOMENTUM` average allocation fell to 0.0% in both weekly and monthly rounds.
3. That same rule did not make models broadly avoid recent winners. Allocation to top-30-day-quintile assets was flat in the weekly transition and higher in the monthly transition, because models rotated into catalyst-backed recent winners such as semiconductors.
4. The temporary June 18/22 benchmark-asset instruction is associated with the clearest defensive prompt response: average S&P 500 allocation rose during that regime, especially in monthly rounds.
5. Prompt guardrails often changed rationales before they fully changed risk appetite. Catalyst and reversal language rose under stricter prompts, but high-risk equity allocations often remained high.
6. Model sensitivity is heterogeneous. Some models completely rotated around prompt/regime changes, while others retained recurring exposures such as small caps, biotech, or regional banks.

## Evidence Confidence

| Claim | Confidence | Basis |
| --- | --- | --- |
| June 24 prompt text explicitly changed price-history instructions. | High | Direct prompt diff and prompt feature flag. |
| Explicit MOMENTUM allocation fell after the June 24 rule. | High | Direct allocation comparison in adjacent weekly and monthly official runs. |
| The June 24 rule made models less affected by broad recent-winner exposure. | Low | Top-30-day-quintile allocation did not fall; it was flat weekly and higher monthly. |
| The benchmark-asset instruction increased S&P 500 allocation. | Medium | Both weekly and monthly adjacent transitions show +18 pp S&P 500 average allocation, but market context changed too. |
| Semiconductor allocation rose because of the prompt alone. | Low | Micron briefing facts arrived in the same round and are a strong confounder. |

## Prompt Regime Summary

| Regime | Rounds | First | Last | Risk | S&P 500 % | MOMENTUM % | Top 30d Quintile % | Reversal Lang % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R0_single_pick_closed_prompt | 1 | CB-2026-05-10-1M | CB-2026-05-10-1M | 90.0 | 0.0 | 0.0 | 100.0 | 75.0 |
| R1_portfolio_internal_priors | 6 | CB-2026-05-17-1M | CB-2026-05-28-1W | 80.4 | 0.0 | 9.7 | 87.5 | 88.3 |
| R2_scoring_window_and_briefing_bias | 26 | CB-2026-05-29-1M | CB-2026-06-23-1W | 73.6 | 3.1 | 8.8 | 76.9 | 91.8 |
| R3_benchmark_asset_mean_reversion_check | 4 | CB-2026-06-18-1M | CB-2026-06-22-1W | 75.4 | 18.2 | 12.8 | 70.2 | 95.0 |
| R4_price_history_discipline | 2 | CB-2026-06-24-1M | CB-2026-06-24-1W | 75.7 | 0.0 | 0.0 | 94.5 | 90.0 |

## Prompt Family Inventory

The raw prompts produce many hashes because dates and horizons are embedded. The `prompt_family` hash normalizes routine metadata, but still preserves instruction wording changes.

| Family | Regime | Rounds | First | Last | Briefing Bias | Benchmark Case | Price History |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6790d2198627 | R0_single_pick_closed_prompt | 1 | CB-2026-05-10-1M | CB-2026-05-10-1M | False | False | False |
| 866f3b1e0cd7 | R1_portfolio_internal_priors | 1 | CB-2026-05-17-1M | CB-2026-05-17-1M | False | False | False |
| 3b6e9f64e251 | R1_portfolio_internal_priors | 1 | CB-2026-05-24-1M | CB-2026-05-24-1M | False | False | False |
| a637719fc3f5 | R1_portfolio_internal_priors | 1 | CB-2026-05-24-1W | CB-2026-05-24-1W | False | False | False |
| a80a42d59f24 | R1_portfolio_internal_priors | 1 | CB-2026-05-27-1W | CB-2026-05-27-1W | False | False | False |
| fd26f32a5de8 | R1_portfolio_internal_priors | 1 | CB-2026-05-28-1M | CB-2026-05-28-1M | False | False | False |
| ae2fbc35a4f3 | R1_portfolio_internal_priors | 1 | CB-2026-05-28-1W | CB-2026-05-28-1W | False | False | False |
| ff6111f4ae40 | R2_scoring_window_and_briefing_bias | 1 | CB-2026-05-29-1M | CB-2026-05-29-1M | True | False | False |
| 9b13d59cb6fa | R2_scoring_window_and_briefing_bias | 1 | CB-2026-05-29-1W | CB-2026-05-29-1W | True | False | False |
| fd5c9fcb18f2 | R2_scoring_window_and_briefing_bias | 1 | CB-2026-06-01-1M | CB-2026-06-01-1M | True | False | False |
| fd441a49f17e | R2_scoring_window_and_briefing_bias | 1 | CB-2026-06-01-1W | CB-2026-06-01-1W | True | False | False |
| ed86ed06ff7a | R2_scoring_window_and_briefing_bias | 1 | CB-2026-06-02-1M | CB-2026-06-02-1M | True | False | False |
| d89b07d4c2a3 | R2_scoring_window_and_briefing_bias | 1 | CB-2026-06-02-1W | CB-2026-06-02-1W | True | False | False |
| 8e54478050a9 | R2_scoring_window_and_briefing_bias | 4 | CB-2026-06-03-1M | CB-2026-06-08-1W | True | False | False |
| a4958f1c8a9c | R2_scoring_window_and_briefing_bias | 16 | CB-2026-06-05-1M | CB-2026-06-23-1W | True | False | False |
| f6e856285ca0 | R3_benchmark_asset_mean_reversion_check | 4 | CB-2026-06-18-1M | CB-2026-06-22-1W | True | True | False |
| f464c4a7c660 | R4_price_history_discipline | 2 | CB-2026-06-24-1M | CB-2026-06-24-1W | True | False | True |

## Regime Change Event Study

| Track | From | To | From Regime | To Regime | Model Turnover | Delta S&P 500 | Delta MOMENTUM | Delta Top 30d Quintile | Delta Semis | Delta Reversal Lang |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| weekly | CB-2026-05-28-1W | CB-2026-05-29-1W | R1_portfolio_internal_priors | R2_scoring_window_and_briefing_bias | 47.0 | 2.0 | -1.0 | -4.0 | -13.0 | -40.0 |
| weekly | CB-2026-06-17-1W | CB-2026-06-18-1W | R2_scoring_window_and_briefing_bias | R3_benchmark_asset_mean_reversion_check | 52.0 | 18.0 | -6.0 | -33.0 | 2.0 | -20.0 |
| weekly | CB-2026-06-22-1W | CB-2026-06-23-1W | R3_benchmark_asset_mean_reversion_check | R2_scoring_window_and_briefing_bias | 73.0 | -16.0 | -6.0 | 16.0 | -28.0 | 0.0 |
| weekly | CB-2026-06-23-1W | CB-2026-06-24-1W | R2_scoring_window_and_briefing_bias | R4_price_history_discipline | 65.0 | 0.0 | -11.0 | 0.0 | 16.0 | -20.0 |
| monthly | CB-2026-05-10-1M | CB-2026-05-17-1M | R0_single_pick_closed_prompt | R1_portfolio_internal_priors | 76.2 | 0.0 | 0.0 | -21.2 | -76.2 | 0.0 |
| monthly | CB-2026-05-28-1M | CB-2026-05-29-1M | R1_portfolio_internal_priors | R2_scoring_window_and_briefing_bias | 43.0 | 0.0 | -11.0 | -2.0 | -14.0 | 0.0 |
| monthly | CB-2026-06-17-1M | CB-2026-06-18-1M | R2_scoring_window_and_briefing_bias | R3_benchmark_asset_mean_reversion_check | 42.0 | 18.0 | -9.0 | -29.0 | -8.0 | 0.0 |
| monthly | CB-2026-06-22-1M | CB-2026-06-23-1M | R3_benchmark_asset_mean_reversion_check | R2_scoring_window_and_briefing_bias | 59.0 | -13.0 | 4.0 | 6.0 | -27.0 | 0.0 |
| monthly | CB-2026-06-23-1M | CB-2026-06-24-1M | R2_scoring_window_and_briefing_bias | R4_price_history_discipline | 63.0 | -8.0 | -18.0 | 16.0 | 26.0 | 0.0 |

## Case Study: June 24 Price-History Discipline

The June 24 prompt changed the mechanical table wording from `mechanical return table` to `mechanical price-context table`, added a rule that trailing returns are descriptive rather than forecasts, and required momentum rationales to cite independent support or disclose limited support plus reversal risk.

| Track | From | To | Turnover | Delta MOMENTUM | Delta Top 30d Quintile | Delta Semis | Delta Catalyst Lang | Delta Reversal Lang |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| weekly | CB-2026-06-23-1W | CB-2026-06-24-1W | 65.0 | -11.0 | 0.0 | 16.0 | 20.0 | -20.0 |
| monthly | CB-2026-06-23-1M | CB-2026-06-24-1M | 63.0 | -18.0 | 16.0 | 26.0 | 0.0 | 0.0 |

Interpretation: the prompt appears to reduce pure named momentum anchoring, but not risk-taking or broad recent-winner exposure. Semiconductors rose because the June 24 briefing contained Micron revenue, margin, guidance, and HBM facts, giving models a non-price catalyst. This should be reported as `less pure momentum chasing, more catalyst-justified momentum`, not as a broad de-risking effect.

## Case Study: Benchmark-Asset / Mean-Reversion Check

| Track | From | To | Turnover | Delta S&P 500 | Delta Defensive | Delta High Risk | Delta Similarity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| weekly | CB-2026-06-17-1W | CB-2026-06-18-1W | 52.0 | 18.0 | 3.0 | -12.0 | -0.1 |
| weekly | CB-2026-06-18-1W | CB-2026-06-22-1W | 42.0 | -2.0 | 2.0 | 0.0 | 0.0 |
| monthly | CB-2026-06-17-1M | CB-2026-06-18-1M | 42.0 | 18.0 | -3.0 | -12.0 | -0.2 |
| monthly | CB-2026-06-18-1M | CB-2026-06-22-1M | 31.0 | 3.0 | 2.0 | -9.0 | 0.0 |

Interpretation: this prompt variant is the clearest example of an instruction changing portfolio construction directly. It explicitly legitimized benchmark allocation when active edge was weak, and average S&P 500 allocation rose in the affected windows.

## Model Sensitivity

| Track | Model | Rounds | Regime Turnover | Avg Turnover | Top 30d Quintile % | Risk | Reversal Lang % |
| --- | --- | --- | --- | --- | --- | --- | --- |
| monthly | anthropic-claude-opus-4-7 | 20 | 63.0 | 51.1 | 76.0 | 71.8 | 90.0 |
| monthly | anthropic-claude-opus-4-8 | 17 | 58.8 | 47.5 | 76.2 | 70.2 | 100.0 |
| monthly | openai-gpt-5-5 | 20 | 55.0 | 40.8 | 96.0 | 84.4 | 100.0 |
| monthly | google-gemini-3-1-pro | 20 | 53.0 | 51.3 | 64.5 | 69.8 | 90.0 |
| monthly | xai-grok-4-3 | 20 | 50.0 | 44.5 | 87.2 | 77.5 | 65.0 |
| monthly | anthropic-claude-fable-5 | 2 |  | 75.0 | 65.0 | 69.8 | 100.0 |
| weekly | anthropic-claude-opus-4-7 | 19 | 66.2 | 50.8 | 76.1 | 72.5 | 100.0 |
| weekly | anthropic-claude-opus-4-8 | 17 | 62.5 | 45.3 | 72.6 | 70.4 | 88.2 |
| weekly | google-gemini-3-1-pro | 19 | 60.0 | 53.9 | 74.2 | 74.5 | 89.5 |
| weekly | xai-grok-4-3 | 19 | 56.2 | 50.6 | 78.2 | 75.8 | 89.5 |
| weekly | openai-gpt-5-5 | 19 | 51.2 | 43.3 | 89.7 | 82.3 | 100.0 |
| weekly | anthropic-claude-fable-5 | 3 |  | 65.0 | 60.0 | 67.8 | 100.0 |

## Researcher/Trader Takeaways

- Prompt wording can change portfolio construction, not only response formatting.
- Momentum guardrails do not eliminate risk-on behavior; they redirect it toward positions with a catalyst narrative.
- Benchmark-relative wording and explicit benchmark-option permission can produce more benchmark-like portfolios.
- Rationale text is a leading indicator of prompt compliance: models start mentioning catalysts, limited support, and reversal risk even when allocations remain aggressive.
- Prompt sensitivity differs by model, so comparing raw benchmark scores without prompt regime context can mix model skill with instruction sensitivity.

## Caveats

- These are observational associations over historical official runs, not randomized prompt A/B tests.
- Market facts changed at the same time as prompts. June 24 semiconductors are confounded by Micron facts; June 18/22 behavior is confounded by contemporaneous macro and market context.
- Model roster changed when Fable 5 was excluded, so no-Fable periods should be compared model-by-model where possible.
- The strongest next step is a non-official controlled rerun: same briefing and market appendix, multiple prompt variants, same model roster.

## Output Files

- `prompt_families.csv`: normalized prompt families and feature flags.
- `round_metrics.csv`: per-round aggregate behavior metrics.
- `submission_metrics.csv`: per-model behavior metrics.
- `transition_metrics.csv`: adjacent-round event-study deltas.
- `model_sensitivity.csv`: model-level sensitivity summaries.
- `summary.json`: machine-readable summary used for this report.
