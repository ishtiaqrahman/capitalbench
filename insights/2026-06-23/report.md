# CapitalBench Insights

Generated at: `2026-06-23T22:04:45Z`
Data as of: `2026-06-23`
Engine: `deterministic_insights_v1`

## AI consensus portfolio scored -29.3 versus the oracle

Context: Monthly result · CB-2026-05-17-1M · Resolved result · Oracle: Taiwan Equities (EWT)

If the monthly model allocations were averaged into one consensus portfolio, it returned -4.44% versus +0.24% for the S&P 500 and +15.15% for the hindsight best asset.

Why it matters: The consensus portfolio tests whether the combined AI view is more useful than any single model's portfolio or the S&P 500 benchmark.

Category: `consensus_performance`

## AI consensus portfolio scored 38.2 versus the oracle

Context: Weekly result · CB-2026-06-15-1W · Resolved result · Oracle: Biotechnology (XBI)

If the weekly model allocations were averaged into one consensus portfolio, it returned +2.69% versus -1.13% for the S&P 500 and +7.04% for the hindsight best asset.

Why it matters: The consensus portfolio tests whether the combined AI view is more useful than any single model's portfolio or the S&P 500 benchmark.

Category: `consensus_performance`

## Monthly round had +38.09% asset dispersion

Context: Monthly result · CB-2026-05-17-1M · Resolved result · Oracle: Taiwan Equities (EWT)

The best scored asset returned +15.15%, the worst returned -22.94%, and +66.15% of the universe was positive. The S&P 500 ranked 42 out of 65 options.

Why it matters: Benchmark difficulty matters because model scores should be interpreted against the opportunity set and the market window they faced.

Category: `benchmark_difficulty`

## Weekly round had +14.22% asset dispersion

Context: Weekly result · CB-2026-06-15-1W · Resolved result · Oracle: Biotechnology (XBI)

The best scored asset returned +7.04%, the worst returned -7.18%, and +31.43% of the universe was positive. The S&P 500 ranked 43 out of 70 options.

Why it matters: Benchmark difficulty matters because model scores should be interpreted against the opportunity set and the market window they faced.

Category: `benchmark_difficulty`

## Models missed the monthly oracle asset

Context: Monthly result · CB-2026-05-17-1M · Resolved result · Oracle: Taiwan Equities (EWT)

The hindsight best asset was Taiwan Equities (EWT) at +15.15%. 0 of 4 models held it, with +0.00% average allocation.

Why it matters: This shows whether models identified the eventual best asset before scoring, even when portfolio weights were too small to fully capture the oracle return.

Category: `oracle_comparison`

## Models found the weekly oracle asset

Context: Weekly result · CB-2026-06-15-1W · Resolved result · Oracle: Biotechnology (XBI)

The hindsight best asset was Biotechnology (XBI) at +7.04%. 3 of 5 models held it, with +6.00% average allocation. The largest allocation came from Claude Opus 4.7 at +10.00%.

Why it matters: This shows whether models identified the eventual best asset before scoring, even when portfolio weights were too small to fully capture the oracle return.

Category: `oracle_comparison`

## Live AI risk posture is risk-seeking

Context: Latest live portfolios · Live portfolios

The newest live portfolios have a deterministic risk-taking score of 79.7 out of 100.

Why it matters: The score translates allocations into a common risk scale, so readers can see whether models are collectively leaning defensive, balanced, or aggressive.

Category: `risk_regime`

## High-confidence model calls have outperformed lower-confidence calls

Context: All resolved official results · Resolved history

Across resolved official results, submissions at or above the median confidence of 0.56 averaged -0.72%, while lower-confidence submissions averaged -0.82%.

Why it matters: Confidence calibration helps readers judge whether model self-reported confidence carries useful information about realized benchmark performance.

Category: `confidence_calibration`

## Weekly and monthly AI portfolios both favor broad and cyclical equity

Context: Latest live portfolios · Live portfolios

The newest weekly portfolios allocate +48.00% to broad and cyclical equity, while the newest monthly portfolios allocate +42.00%.

Why it matters: Agreement across horizons signals that the current model posture is not just a short-term tactical move.

Category: `horizon_agreement`

## Model allocation styles are separating into clear behavior profiles

Context: Model behavior profiles

GPT-5.5 has the highest average risk-taking score at 86.2/100. Gemini 3.1 Pro has the largest average top holding at +38.78%. GPT-5.5 has the lowest measured turnover at +41.00%.

Why it matters: Behavior profiles help readers separate model style from short-term score noise: some models seek more risk, some concentrate harder, and some change portfolios less between rounds.

Category: `model_behavior`

## Grok 4.3's result was driven by Semiconductors

Context: Monthly result · CB-2026-05-17-1M · Resolved result

In the latest monthly result, Semiconductors contributed +4.25% to Grok 4.3's portfolio. The largest drag came from Energy Sector at -3.21%.

Why it matters: Attribution turns a model score into an explanation of which holdings actually helped or hurt the frozen portfolio.

Category: `performance_attribution`

## GPT-5.5's result was driven by Semiconductors

Context: Weekly result · CB-2026-06-15-1W · Resolved result

In the latest weekly result, Semiconductors contributed +1.18% to GPT-5.5's portfolio. No holding detracted; the smallest positive contribution came from US Momentum Equities at +0.52%.

Why it matters: Attribution turns a model score into an explanation of which holdings actually helped or hurt the frozen portfolio.

Category: `performance_attribution`

## Monthly models are leaning into recent winners

Context: Monthly live round · CB-2026-06-23-1M · Live portfolios

The newest monthly portfolios allocate +78.00% to the top 20% of assets by prior 30-day return. The strongest 30-day asset in the input table was Biotechnology (XBI).

Why it matters: This measures whether models are chasing recent momentum or allocating away from it before outcomes are known.

Category: `model_behavior`

## Weekly models are leaning into recent winners

Context: Weekly live round · CB-2026-06-23-1W · Live portfolios

The newest weekly portfolios allocate +95.00% to the top 20% of assets by prior 30-day return. The strongest 30-day asset in the input table was Biotechnology (XBI).

Why it matters: This measures whether models are chasing recent momentum or allocating away from it before outcomes are known.

Category: `model_behavior`

## Live AI portfolios are concentrated in Biotechnology (XBI)

Context: Latest live portfolios · Live portfolios

Across the newest live weekly and monthly portfolios, Biotechnology (XBI) is the largest aggregate allocation at +25.00%.

Why it matters: This shows the current crowding point in model capital allocation, before the open rounds receive their final market scores.

Category: `current_positioning`

## GPT-5.5 has the strongest live alpha

Context: Open-round interim performance · Interim, not final

Using the latest available interim close, GPT-5.5 in CB-2026-06-16-1M is ahead of the S&P 500 by +7.30 percentage points, while GPT-5.5 in CB-2026-06-02-1M is at -6.28 percentage points.

Why it matters: Live alpha is provisional, but it shows how open model portfolios are moving before the final official score.

Category: `live_performance`

## Live model portfolios are tightly clustered

Context: Latest live portfolios · Live portfolios

The closest live allocation pair is Claude Opus 4.7 and Claude Opus 4.8 with +93.15% cosine similarity. The current allocation outlier is Gemini 3.1 Pro.

Why it matters: Similarity analysis shows whether models are independently converging on the same portfolio or expressing meaningfully different capital-allocation behavior.

Category: `model_similarity`
