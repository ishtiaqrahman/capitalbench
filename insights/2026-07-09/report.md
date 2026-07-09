# CapitalBench Insights

Generated at: `2026-07-09T07:54:45Z`
Data as of: `2026-07-08`
Engine: `deterministic_insights_v1`

## AI consensus portfolio scored 2.7 versus the oracle

Context: Monthly result · CB-2026-06-08-1M · Resolved result · Oracle: Biotechnology (XBI)

If the monthly model allocations were averaged into one consensus portfolio, it returned +0.72% versus +1.09% for the S&P 500 and +27.01% for the hindsight best asset.

Why it matters: The consensus portfolio tests whether the combined AI view is more useful than any single model's portfolio or the S&P 500 benchmark.

Category: `consensus_performance`

## AI consensus portfolio scored 9.7 versus the oracle

Context: Weekly result · CB-2026-07-01-1W · Resolved result · Oracle: Crude Oil (USO)

If the weekly model allocations were averaged into one consensus portfolio, it returned +0.84% versus -0.05% for the S&P 500 and +8.66% for the hindsight best asset.

Why it matters: The consensus portfolio tests whether the combined AI view is more useful than any single model's portfolio or the S&P 500 benchmark.

Category: `consensus_performance`

## Monthly round had +43.99% asset dispersion

Context: Monthly result · CB-2026-06-08-1M · Resolved result · Oracle: Biotechnology (XBI)

The best scored asset returned +27.01%, the worst returned -16.97%, and +62.86% of the universe was positive. The S&P 500 ranked 30 out of 70 options.

Why it matters: Benchmark difficulty matters because model scores should be interpreted against the opportunity set and the market window they faced.

Category: `benchmark_difficulty`

## Weekly round had +14.99% asset dispersion

Context: Weekly result · CB-2026-07-01-1W · Resolved result · Oracle: Crude Oil (USO)

The best scored asset returned +8.66%, the worst returned -6.33%, and +37.14% of the universe was positive. The S&P 500 ranked 29 out of 70 options.

Why it matters: Benchmark difficulty matters because model scores should be interpreted against the opportunity set and the market window they faced.

Category: `benchmark_difficulty`

## Models missed the monthly oracle asset

Context: Monthly result · CB-2026-06-08-1M · Resolved result · Oracle: Biotechnology (XBI)

The hindsight best asset was Biotechnology (XBI) at +27.01%. 0 of 5 models held it, with +0.00% average allocation.

Why it matters: This shows whether models identified the eventual best asset before scoring, even when portfolio weights were too small to fully capture the oracle return.

Category: `oracle_comparison`

## Models missed the weekly oracle asset

Context: Weekly result · CB-2026-07-01-1W · Resolved result · Oracle: Crude Oil (USO)

The hindsight best asset was Crude Oil (USO) at +8.66%. 0 of 6 models held it, with +0.00% average allocation.

Why it matters: This shows whether models identified the eventual best asset before scoring, even when portfolio weights were too small to fully capture the oracle return.

Category: `oracle_comparison`

## Live AI risk posture is risk-seeking

Context: Latest live portfolios · Live portfolios

The newest live portfolios have a deterministic risk-taking score of 64.9 out of 100.

Why it matters: The score translates allocations into a common risk scale, so readers can see whether models are collectively leaning defensive, balanced, or aggressive.

Category: `risk_regime`

## High-confidence model calls have underperformed lower-confidence calls

Context: All resolved official results · Resolved history

Across resolved official results, submissions at or above the median confidence of 0.56 averaged -1.07%, while lower-confidence submissions averaged -0.22%.

Why it matters: Confidence calibration helps readers judge whether model self-reported confidence carries useful information about realized benchmark performance.

Category: `confidence_calibration`

## Model allocation styles are separating into clear behavior profiles

Context: Model behavior profiles

GPT-5.5 has the highest average risk-taking score at 85.3/100. Gemini 3.1 Pro has the largest average top holding at +39.56%. GPT-5.5 has the lowest measured turnover at +44.00%.

Why it matters: Behavior profiles help readers separate model style from short-term score noise: some models seek more risk, some concentrate harder, and some change portfolios less between rounds.

Category: `model_behavior`

## Claude Opus 4.7's result was driven by Healthcare Sector

Context: Monthly result · CB-2026-06-08-1M · Resolved result

In the latest monthly result, Healthcare Sector contributed +1.70% to Claude Opus 4.7's portfolio. The largest drag came from Semiconductors at -0.17%.

Why it matters: Attribution turns a model score into an explanation of which holdings actually helped or hurt the frozen portfolio.

Category: `performance_attribution`

## Grok 4.3's result was driven by Biotechnology

Context: Weekly result · CB-2026-07-01-1W · Resolved result

In the latest weekly result, Biotechnology contributed +1.23% to Grok 4.3's portfolio. No holding detracted; the smallest positive contribution came from Financials Sector at +0.07%.

Why it matters: Attribution turns a model score into an explanation of which holdings actually helped or hurt the frozen portfolio.

Category: `performance_attribution`

## Weekly and monthly AI portfolios point to different regimes

Context: Latest live portfolios · Live portfolios

The newest weekly portfolios lean toward real assets and inflation, while the newest monthly portfolios lean toward defensive equity.

Why it matters: A horizon split helps readers separate short-window positioning from the longer one-month model view.

Category: `horizon_agreement`

## Monthly models are leaning into recent winners

Context: Monthly live round · CB-2026-07-08-1M · Live portfolios

The newest monthly portfolios allocate +77.86% to the top 20% of assets by prior 30-day return. The strongest 30-day asset in the input table was Biotechnology (XBI).

Why it matters: This measures whether models are chasing recent momentum or allocating away from it before outcomes are known.

Category: `model_behavior`

## Weekly models are leaning into recent winners

Context: Weekly live round · CB-2026-07-08-1W · Live portfolios

The newest weekly portfolios allocate +56.43% to the top 20% of assets by prior 30-day return. The strongest 30-day asset in the input table was Biotechnology (XBI).

Why it matters: This measures whether models are chasing recent momentum or allocating away from it before outcomes are known.

Category: `model_behavior`

## Live AI portfolios are concentrated in Healthcare Sector (XLV)

Context: Latest live portfolios · Live portfolios

Across the newest live weekly and monthly portfolios, Healthcare Sector (XLV) is the largest aggregate allocation at +20.00%.

Why it matters: This shows the current crowding point in model capital allocation, before the open rounds receive their final market scores.

Category: `current_positioning`

## Gemini 3.1 Pro has the strongest live alpha

Context: Open-round interim performance · Interim, not final

Using the latest available interim close, Gemini 3.1 Pro in CB-2026-07-07-1W is ahead of the S&P 500 by +1.53 percentage points, while GPT-5.5 in CB-2026-06-22-1M is at -8.16 percentage points.

Why it matters: Live alpha is provisional, but it shows how open model portfolios are moving before the final official score.

Category: `live_performance`

## Live model portfolios are tightly clustered

Context: Latest live portfolios · Live portfolios

The closest live allocation pair is Claude Opus 4.7 and Claude Opus 4.8 with +94.56% cosine similarity. The current allocation outlier is GPT-5.5.

Why it matters: Similarity analysis shows whether models are independently converging on the same portfolio or expressing meaningfully different capital-allocation behavior.

Category: `model_similarity`
