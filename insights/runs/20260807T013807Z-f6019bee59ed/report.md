# CapitalBench Insights

Generated at: `2026-08-07T01:38:07Z`
Data as of: `2026-08-06`
Engine: `deterministic_insights_v4`

## AI consensus portfolio scored -2.1 versus the oracle

Context: Monthly result · CB-2026-07-06-1M · Resolved result · Oracle: Crude Oil (USO)

If the monthly model allocations were averaged into one consensus portfolio, it returned -0.29% versus +2.30% for the S&P 500 and +13.91% for the hindsight best asset.

Why it matters: The consensus portfolio tests whether the combined AI view is more useful than any single model's portfolio or the S&P 500 benchmark.

Category: `consensus_performance`

## AI consensus portfolio scored 23.5 versus the oracle

Context: Weekly result · CB-2026-07-30-1W · Resolved result · Oracle: Taiwan Equities (EWT)

If the weekly model allocations were averaged into one consensus portfolio, it returned +1.99% versus +3.62% for the S&P 500 and +8.49% for the hindsight best asset.

Why it matters: The consensus portfolio tests whether the combined AI view is more useful than any single model's portfolio or the S&P 500 benchmark.

Category: `consensus_performance`

## Monthly round had +27.47% asset dispersion

Context: Monthly result · CB-2026-07-06-1M · Resolved result · Oracle: Crude Oil (USO)

The best scored asset returned +13.91%, the worst returned -13.55%, and +58.57% of the universe was positive. The S&P 500 ranked 17 out of 70 options.

Why it matters: Benchmark difficulty matters because model scores should be interpreted against the opportunity set and the market window they faced.

Category: `benchmark_difficulty`

## Weekly round had +15.24% asset dispersion

Context: Weekly result · CB-2026-07-30-1W · Resolved result · Oracle: Taiwan Equities (EWT)

The best scored asset returned +8.49%, the worst returned -6.75%, and +77.14% of the universe was positive. The S&P 500 ranked 16 out of 70 options.

Why it matters: Benchmark difficulty matters because model scores should be interpreted against the opportunity set and the market window they faced.

Category: `benchmark_difficulty`

## Models missed the monthly oracle asset

Context: Monthly result · CB-2026-07-06-1M · Resolved result · Oracle: Crude Oil (USO)

The hindsight best asset was Crude Oil (USO) at +13.91%. 0 of 6 models held it, with +0.00% average allocation.

Why it matters: This shows whether models identified the eventual best asset before scoring, even when portfolio weights were too small to fully capture the oracle return.

Category: `oracle_comparison`

## Models missed the weekly oracle asset

Context: Weekly result · CB-2026-07-30-1W · Resolved result · Oracle: Taiwan Equities (EWT)

The hindsight best asset was Taiwan Equities (EWT) at +8.49%. 0 of 8 models held it, with +0.00% average allocation.

Why it matters: This shows whether models identified the eventual best asset before scoring, even when portfolio weights were too small to fully capture the oracle return.

Category: `oracle_comparison`

## Live AI portfolios are concentrated in S&P 500 (SPY)

Context: Latest live portfolios · Live portfolios

Across the newest live weekly and monthly portfolios, S&P 500 (SPY) is the largest aggregate allocation at +34.38%.

Why it matters: This shows the current crowding point in model capital allocation, before the open rounds receive their final market scores.

Category: `current_positioning`

## Grok 4.3 leads across multiple monthly market environments

Context: Monthly market environments · Ready sample

Grok 4.3 leads down environments at -1.22% across 6 tests; Grok 4.3 leads up environments at +2.21% across 3 tests.

Why it matters: Leadership that changes with the broad-market backdrop shows why a single all-history ranking can hide meaningful model strengths and weaknesses.

Category: `market_environment`

## Live AI risk posture is risk-seeking

Context: Latest live portfolios · Live portfolios

The newest live portfolios have a deterministic risk-taking score of 73.6 out of 100.

Why it matters: The score translates allocations into a common risk scale, so readers can see whether models are collectively leaning defensive, balanced, or aggressive.

Category: `risk_regime`

## High-confidence model calls have underperformed lower-confidence calls

Context: All resolved official results · Resolved history

Across resolved official results, submissions at or above the median confidence of 0.58 averaged -1.31%, while lower-confidence submissions averaged -0.44%.

Why it matters: Confidence calibration helps readers judge whether model self-reported confidence carries useful information about realized benchmark performance.

Category: `confidence_calibration`

## Model allocation styles are separating into clear behavior profiles

Context: Model behavior profiles

GPT-5.5 has the highest average risk-taking score at 79.9/100. Grok 4.3 has the largest average top holding at +43.48%. Claude Opus 5 has the lowest measured turnover at +38.21%.

Why it matters: Behavior profiles help readers separate model style from short-term score noise: some models seek more risk, some concentrate harder, and some change portfolios less between rounds.

Category: `model_behavior`

## Claude Opus 4.8's result was driven by Financials Sector

Context: Monthly result · CB-2026-07-06-1M · Resolved result

In the latest monthly result, Financials Sector contributed +0.74% to Claude Opus 4.8's portfolio. The largest drag came from Industrials Sector at -0.09%.

Why it matters: Attribution turns a model score into an explanation of which holdings actually helped or hurt the frozen portfolio.

Category: `performance_attribution`

## Gemini 3.1 Pro's result was driven by S&P 500

Context: Weekly result · CB-2026-07-30-1W · Resolved result

In the latest weekly result, S&P 500 contributed +1.81% to Gemini 3.1 Pro's portfolio. No holding detracted; the smallest positive contribution came from Financials Sector at +0.36%.

Why it matters: Attribution turns a model score into an explanation of which holdings actually helped or hurt the frozen portfolio.

Category: `performance_attribution`

## Weekly and monthly AI portfolios point to different regimes

Context: Latest live portfolios · Live portfolios

The newest weekly portfolios lean toward broad and cyclical equity, while the newest monthly portfolios lean toward growth and technology.

Why it matters: A horizon split helps readers separate short-window positioning from the longer one-month model view.

Category: `horizon_agreement`

## Grok 4.3 leads when the S&P 500 is negative

Context: Monthly down environments · Ready sample

The model averaged -1.22% across 6 shared-cohort rounds drawn from 8 resolved monthly down environments. The sample meets publication thresholds.

Why it matters: Environment-specific returns show whether a model's all-history result is broad or depends on a particular market direction.

Category: `market_environment`

## Grok 4.3 leads when the S&P 500 is positive

Context: Monthly up environments · Ready sample

The model averaged +2.21% across 3 shared-cohort rounds drawn from 7 resolved monthly up environments. The sample meets publication thresholds.

Why it matters: Environment-specific returns show whether a model's all-history result is broad or depends on a particular market direction.

Category: `market_environment`

## Grok 4.3 leads when the S&P 500 is negative

Context: Weekly down environments · Ready sample

The model averaged +2.35% across 4 shared-cohort rounds drawn from 14 resolved weekly down environments. The sample meets publication thresholds.

Why it matters: Environment-specific returns show whether a model's all-history result is broad or depends on a particular market direction.

Category: `market_environment`

## Claude Opus 4.8 has the strongest monthly score floor

Context: Monthly environment consistency · Ready sample

Its lowest CapitalBench Score across 3 tested market directions is -14.2, with at least 3 model observations in each included direction.

Why it matters: A stronger floor identifies models whose benchmark performance is less dependent on one favorable market direction.

Category: `market_environment`

## Claude Opus 4.8 has the strongest current monthly recent-winner tilt

Context: Monthly live round · CB-2026-08-05-1M · Live portfolios

Its score is 59.9 out of 100, with 30.0% in the top recent-return quintile. GPT-5.6 Sol is lowest at 3.7.

Why it matters: This compares how strongly current model portfolios favor assets that had already outperformed. It describes the allocation and does not infer why the model chose it.

Category: `model_behavior`

## Claude Opus 4.8 has the strongest current weekly recent-winner tilt

Context: Weekly live round · CB-2026-08-05-1W · Live portfolios

Its score is 69.4 out of 100, with 50.0% in the top recent-return quintile. Claude Fable 5 is lowest at 24.3.

Why it matters: This compares how strongly current model portfolios favor assets that had already outperformed. It describes the allocation and does not infer why the model chose it.

Category: `model_behavior`

## Grok 4.3 has the strongest live alpha

Context: Open-round interim performance · Interim, not final

Using the latest available interim close, Grok 4.3 in CB-2026-07-09-1M is ahead of the S&P 500 by +2.33 percentage points, while Grok 4.5 in CB-2026-07-24-1M is at -8.99 percentage points.

Why it matters: Live alpha is provisional, but it shows how open model portfolios are moving before the final official score.

Category: `live_performance`

## GPT-5.5 changes most between monthly up and down environments

Context: Monthly up/down split · Ready sample

The model averaged -4.91% in down environments and +0.16% in up environments, a 5.1 percentage-point gap.

Why it matters: A large directional split identifies models whose benchmark behavior is especially sensitive to the market backdrop.

Category: `market_environment`

## Live model portfolios are tightly clustered

Context: Latest live portfolios · Live portfolios

The closest live allocation pair is Claude Opus 4.8 and Gemini 3.1 Pro with +92.07% cosine similarity. The current allocation outlier is GPT-5.6 Sol.

Why it matters: Similarity analysis shows whether models are independently converging on the same portfolio or expressing meaningfully different capital-allocation behavior.

Category: `model_similarity`

## Claude Opus 4.8 leads when the S&P 500 is flat

Context: Monthly flat environments · Ready sample

The model averaged -2.79% across 11 shared-cohort rounds drawn from 12 resolved monthly flat environments. The sample meets publication thresholds.

Why it matters: Environment-specific returns show whether a model's all-history result is broad or depends on a particular market direction.

Category: `market_environment`

## Grok 4.3 leads when the S&P 500 is flat

Context: Weekly flat environments · Forming sample

The model averaged +1.99% across 2 shared-cohort rounds drawn from 9 resolved weekly flat environments. The result remains provisional while the model sample grows.

Why it matters: Environment-specific returns show whether a model's all-history result is broad or depends on a particular market direction.

Category: `market_environment`

## Grok 4.3 has the strongest weekly score floor

Context: Weekly environment consistency · Forming sample

Its lowest CapitalBench Score across 2 tested market directions is 23.5, with at least 2 model observations in each included direction.

Why it matters: A stronger floor identifies models whose benchmark performance is less dependent on one favorable market direction.

Category: `market_environment`
