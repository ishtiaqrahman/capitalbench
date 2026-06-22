# CapitalBench Insights

Generated at: `2026-06-22T06:47:33Z`
Data as of: `2026-06-18`
Engine: `deterministic_insights_v1`

## AI consensus portfolio scored -29.3 versus the oracle

Context: Monthly result · CB-2026-05-17-1M · Resolved result · Oracle: Taiwan Equities (EWT)

If the monthly model allocations were averaged into one consensus portfolio, it returned -4.44% versus +0.24% for the S&P 500 and +15.15% for the hindsight best asset.

Why it matters: The consensus portfolio tests whether the combined AI view is more useful than any single model's portfolio or the S&P 500 benchmark.

Category: `consensus_performance`

## AI consensus portfolio scored 35.9 versus the oracle

Context: Weekly result · CB-2026-06-13-1W · Resolved result · Oracle: South Korea Equities (EWY)

If the weekly model allocations were averaged into one consensus portfolio, it returned +3.96% versus +0.67% for the S&P 500 and +11.02% for the hindsight best asset.

Why it matters: The consensus portfolio tests whether the combined AI view is more useful than any single model's portfolio or the S&P 500 benchmark.

Category: `consensus_performance`

## Monthly round had +38.09% asset dispersion

Context: Monthly result · CB-2026-05-17-1M · Resolved result · Oracle: Taiwan Equities (EWT)

The best scored asset returned +15.15%, the worst returned -22.94%, and +66.15% of the universe was positive. The S&P 500 ranked 42 out of 65 options.

Why it matters: Benchmark difficulty matters because model scores should be interpreted against the opportunity set and the market window they faced.

Category: `benchmark_difficulty`

## Weekly round had +19.43% asset dispersion

Context: Weekly result · CB-2026-06-13-1W · Resolved result · Oracle: South Korea Equities (EWY)

The best scored asset returned +11.02%, the worst returned -8.42%, and +52.86% of the universe was positive. The S&P 500 ranked 23 out of 70 options.

Why it matters: Benchmark difficulty matters because model scores should be interpreted against the opportunity set and the market window they faced.

Category: `benchmark_difficulty`

## Models missed the monthly oracle asset

Context: Monthly result · CB-2026-05-17-1M · Resolved result · Oracle: Taiwan Equities (EWT)

The hindsight best asset was Taiwan Equities (EWT) at +15.15%. 0 of 4 models held it, with +0.00% average allocation.

Why it matters: This shows whether models identified the eventual best asset before scoring, even when portfolio weights were too small to fully capture the oracle return.

Category: `oracle_comparison`

## Models found the weekly oracle asset

Context: Weekly result · CB-2026-06-13-1W · Resolved result · Oracle: South Korea Equities (EWY)

The hindsight best asset was South Korea Equities (EWY) at +11.02%. 2 of 6 models held it, with +6.67% average allocation. The largest allocation came from GPT-5.5 at +25.00%.

Why it matters: This shows whether models identified the eventual best asset before scoring, even when portfolio weights were too small to fully capture the oracle return.

Category: `oracle_comparison`

## Live AI portfolios are concentrated in Semiconductors (SMH)

Context: Latest live portfolios · Live portfolios

Across the newest live weekly and monthly portfolios, Semiconductors (SMH) is the largest aggregate allocation at +30.50%.

Why it matters: This shows the current crowding point in model capital allocation, before the open rounds receive their final market scores.

Category: `current_positioning`

## Live AI risk posture is aggressive

Context: Latest live portfolios · Live portfolios

The newest live portfolios have a deterministic risk-taking score of 84.7 out of 100.

Why it matters: The score translates allocations into a common risk scale, so readers can see whether models are collectively leaning defensive, balanced, or aggressive.

Category: `risk_regime`

## High-confidence model calls have outperformed lower-confidence calls

Context: All resolved official results · Resolved history

Across resolved official results, submissions at or above the median confidence of 0.55 averaged -0.95%, while lower-confidence submissions averaged -1.50%.

Why it matters: Confidence calibration helps readers judge whether model self-reported confidence carries useful information about realized benchmark performance.

Category: `confidence_calibration`

## Weekly and monthly AI portfolios both favor growth and technology

Context: Latest live portfolios · Live portfolios

The newest weekly portfolios allocate +62.00% to growth and technology, while the newest monthly portfolios allocate +57.00%.

Why it matters: Agreement across horizons signals that the current model posture is not just a short-term tactical move.

Category: `horizon_agreement`

## Model allocation styles are separating into clear behavior profiles

Context: Model behavior profiles

GPT-5.5 has the highest average risk-taking score at 85.6/100. Gemini 3.1 Pro has the largest average top holding at +38.94%. GPT-5.5 has the lowest measured turnover at +41.45%.

Why it matters: Behavior profiles help readers separate model style from short-term score noise: some models seek more risk, some concentrate harder, and some change portfolios less between rounds.

Category: `model_behavior`

## Grok 4.3's result was driven by Semiconductors

Context: Monthly result · CB-2026-05-17-1M · Resolved result

In the latest monthly result, Semiconductors contributed +4.25% to Grok 4.3's portfolio. The largest drag came from Energy Sector at -3.21%.

Why it matters: Attribution turns a model score into an explanation of which holdings actually helped or hurt the frozen portfolio.

Category: `performance_attribution`

## GPT-5.5's result was driven by South Korea Equities

Context: Weekly result · CB-2026-06-13-1W · Resolved result

In the latest weekly result, South Korea Equities contributed +2.75% to GPT-5.5's portfolio. The largest drag came from Bitcoin ETF at -0.12%.

Why it matters: Attribution turns a model score into an explanation of which holdings actually helped or hurt the frozen portfolio.

Category: `performance_attribution`

## Monthly models are leaning into recent winners

Context: Monthly live round · CB-2026-06-18-1M · Live portfolios

The newest monthly portfolios allocate +66.00% to the top 20% of assets by prior 30-day return. The strongest 30-day asset in the input table was South Korea Equities (EWY).

Why it matters: This measures whether models are chasing recent momentum or allocating away from it before outcomes are known.

Category: `model_behavior`

## Weekly models are leaning into recent winners

Context: Weekly live round · CB-2026-06-18-1W · Live portfolios

The newest weekly portfolios allocate +64.00% to the top 20% of assets by prior 30-day return. The strongest 30-day asset in the input table was South Korea Equities (EWY).

Why it matters: This measures whether models are chasing recent momentum or allocating away from it before outcomes are known.

Category: `model_behavior`

## GPT-5.5 has the strongest live alpha

Context: Open-round interim performance · Interim, not final

Using the latest available interim close, GPT-5.5 in CB-2026-05-24-1M is ahead of the S&P 500 by +6.39 percentage points, while GPT-5.5 in CB-2026-06-02-1M is at -6.28 percentage points.

Why it matters: Live alpha is provisional, but it shows how open model portfolios are moving before the final official score.

Category: `live_performance`

## Live model portfolios are tightly clustered

Context: Latest live portfolios · Live portfolios

The closest live allocation pair is Claude Opus 4.8 and Gemini 3.1 Pro with +92.50% cosine similarity. The current allocation outlier is GPT-5.5.

Why it matters: Similarity analysis shows whether models are independently converging on the same portfolio or expressing meaningfully different capital-allocation behavior.

Category: `model_similarity`
