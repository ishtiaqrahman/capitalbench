# CapitalBench Insights

Generated at: `2026-08-29T21:46:33Z`
Data as of: `2026-08-28`
Engine: `deterministic_insights_v4`

## AI consensus portfolio scored 14.4 versus the oracle

Context: Monthly result · CB-2026-07-30-1M · Resolved result · Oracle: Ethereum ETF (ETHA)

If the monthly model allocations were averaged into one consensus portfolio, it returned +3.83% versus +3.73% for the S&P 500 and +26.60% for the hindsight best asset.

Why it matters: The consensus portfolio tests whether the combined AI view is more useful than any single model's portfolio or the S&P 500 benchmark.

Category: `consensus_performance`

## AI consensus portfolio scored 26.9 versus the oracle

Context: Weekly result · CB-2026-08-21-1W · Resolved result · Oracle: Software (IGV)

If the weekly model allocations were averaged into one consensus portfolio, it returned +1.59% versus +0.47% for the S&P 500 and +5.93% for the hindsight best asset.

Why it matters: The consensus portfolio tests whether the combined AI view is more useful than any single model's portfolio or the S&P 500 benchmark.

Category: `consensus_performance`

## Monthly round had +30.92% asset dispersion

Context: Monthly result · CB-2026-07-30-1M · Resolved result · Oracle: Ethereum ETF (ETHA)

The best scored asset returned +26.60%, the worst returned -4.32%, and +67.14% of the universe was positive. The S&P 500 ranked 25 out of 70 options.

Why it matters: Benchmark difficulty matters because model scores should be interpreted against the opportunity set and the market window they faced.

Category: `benchmark_difficulty`

## Weekly round had +8.53% asset dispersion

Context: Weekly result · CB-2026-08-21-1W · Resolved result · Oracle: Software (IGV)

The best scored asset returned +5.93%, the worst returned -2.60%, and +55.56% of the universe was positive. The S&P 500 ranked unranked out of 9 options.

Why it matters: Benchmark difficulty matters because model scores should be interpreted against the opportunity set and the market window they faced.

Category: `benchmark_difficulty`

## Models missed the monthly oracle asset

Context: Monthly result · CB-2026-07-30-1M · Resolved result · Oracle: Ethereum ETF (ETHA)

The hindsight best asset was Ethereum ETF (ETHA) at +26.60%. 0 of 8 models held it, with +0.00% average allocation.

Why it matters: This shows whether models identified the eventual best asset before scoring, even when portfolio weights were too small to fully capture the oracle return.

Category: `oracle_comparison`

## Models found the weekly oracle asset

Context: Weekly result · CB-2026-08-21-1W · Resolved result · Oracle: Software (IGV)

The hindsight best asset was Software (IGV) at +5.93%. 4 of 7 models held it, with +17.86% average allocation. The largest allocation came from Claude Fable 5 at +35.00%.

Why it matters: This shows whether models identified the eventual best asset before scoring, even when portfolio weights were too small to fully capture the oracle return.

Category: `oracle_comparison`

## Live AI portfolios are concentrated in S&P 500 (SPY)

Context: Latest live portfolios · Live portfolios

Across the newest live weekly and monthly portfolios, S&P 500 (SPY) is the largest aggregate allocation at +39.64%.

Why it matters: This shows the current crowding point in model capital allocation, before the open rounds receive their final market scores.

Category: `current_positioning`

## Monthly model leadership changes with the S&P 500 environment

Context: Monthly market environments · Ready sample

Grok 4.3 leads down environments at -1.22% across 6 tests; Claude Opus 4.8 leads flat environments at -2.79% across 11 tests.

Why it matters: Leadership that changes with the broad-market backdrop shows why a single all-history ranking can hide meaningful model strengths and weaknesses.

Category: `market_environment`

## Live AI risk posture is risk-seeking

Context: Latest live portfolios · Live portfolios

The newest live portfolios have a deterministic risk-taking score of 69.2 out of 100.

Why it matters: The score translates allocations into a common risk scale, so readers can see whether models are collectively leaning defensive, balanced, or aggressive.

Category: `risk_regime`

## High-confidence model calls have underperformed lower-confidence calls

Context: All resolved official results · Resolved history

Across resolved official results, submissions at or above the median confidence of 0.58 averaged +0.03%, while lower-confidence submissions averaged +0.49%.

Why it matters: Confidence calibration helps readers judge whether model self-reported confidence carries useful information about realized benchmark performance.

Category: `confidence_calibration`

## Weekly and monthly AI portfolios both favor broad and cyclical equity

Context: Latest live portfolios · Live portfolios

The newest weekly portfolios allocate +60.71% to broad and cyclical equity, while the newest monthly portfolios allocate +81.43%.

Why it matters: Agreement across horizons signals that the current model posture is not just a short-term tactical move.

Category: `horizon_agreement`

## Model allocation styles are separating into clear behavior profiles

Context: Model behavior profiles

GPT-5.5 has the highest average risk-taking score at 79.7/100. Grok 4.6 has the largest average top holding at +67.05%. Claude Opus 4.8 has the lowest measured turnover at +43.35%.

Why it matters: Behavior profiles help readers separate model style from short-term score noise: some models seek more risk, some concentrate harder, and some change portfolios less between rounds.

Category: `model_behavior`

## Grok 4.5's result was driven by Software

Context: Monthly result · CB-2026-07-30-1M · Resolved result

In the latest monthly result, Software contributed +6.07% to Grok 4.5's portfolio. No holding detracted; the smallest positive contribution came from Europe Equities at +0.22%.

Why it matters: Attribution turns a model score into an explanation of which holdings actually helped or hurt the frozen portfolio.

Category: `performance_attribution`

## Claude Fable 5's result was driven by Software

Context: Weekly result · CB-2026-08-21-1W · Resolved result

In the latest weekly result, Software contributed +2.08% to Claude Fable 5's portfolio. The largest drag came from Aerospace and Defense at -0.57%.

Why it matters: Attribution turns a model score into an explanation of which holdings actually helped or hurt the frozen portfolio.

Category: `performance_attribution`

## Grok 4.3 leads when the S&P 500 is negative

Context: Monthly down environments · Ready sample

The model averaged -1.22% across 6 shared-cohort rounds drawn from 8 resolved monthly down environments. The sample meets publication thresholds.

Why it matters: Environment-specific returns show whether a model's all-history result is broad or depends on a particular market direction.

Category: `market_environment`

## Grok 4.3 leads when the S&P 500 is negative

Context: Weekly down environments · Ready sample

The model averaged +2.35% across 4 shared-cohort rounds drawn from 16 resolved weekly down environments. The sample meets publication thresholds.

Why it matters: Environment-specific returns show whether a model's all-history result is broad or depends on a particular market direction.

Category: `market_environment`

## Claude Opus 4.8 has the strongest monthly score floor

Context: Monthly environment consistency · Ready sample

Its lowest CapitalBench Score across 2 tested market directions is -14.2, with at least 6 model observations in each included direction.

Why it matters: A stronger floor identifies models whose benchmark performance is less dependent on one favorable market direction.

Category: `market_environment`

## Grok 4.6 has the strongest current monthly recent-winner tilt

Context: Monthly live round · CB-2026-08-27-1M · Live portfolios

Its score is 50.0 out of 100, with 0.0% in the top recent-return quintile. Gemini 3.1 Pro is lowest at 1.4.

Why it matters: This compares how strongly current model portfolios favor assets that had already outperformed. It describes the allocation and does not infer why the model chose it.

Category: `model_behavior`

## Grok 4.6 has the strongest current weekly recent-winner tilt

Context: Weekly live round · CB-2026-08-27-1W · Live portfolios

Its score is 50.0 out of 100, with 0.0% in the top recent-return quintile. Gemini 3.1 Pro is lowest at 4.1.

Why it matters: This compares how strongly current model portfolios favor assets that had already outperformed. It describes the allocation and does not infer why the model chose it.

Category: `model_behavior`

## Gemini 3.1 Pro has the strongest live alpha

Context: Open-round interim performance · Interim, not final

Using the latest available interim close, Gemini 3.1 Pro in CB-2026-08-04-1M is ahead of the S&P 500 by +4.92 percentage points, while Claude Fable 5 in CB-2026-08-26-1W is at -2.82 percentage points.

Why it matters: Live alpha is provisional, but it shows how open model portfolios are moving before the final official score.

Category: `live_performance`

## Live model portfolios are tightly clustered

Context: Latest live portfolios · Live portfolios

The closest live allocation pair is Claude Fable 5 and Grok 4.3 with +90.88% cosine similarity. The current allocation outlier is Gemini 3.1 Pro.

Why it matters: Similarity analysis shows whether models are independently converging on the same portfolio or expressing meaningfully different capital-allocation behavior.

Category: `model_similarity`

## Claude Opus 4.8 leads when the S&P 500 is flat

Context: Monthly flat environments · Ready sample

The model averaged -2.79% across 11 shared-cohort rounds drawn from 12 resolved monthly flat environments. The sample meets publication thresholds.

Why it matters: Environment-specific returns show whether a model's all-history result is broad or depends on a particular market direction.

Category: `market_environment`
