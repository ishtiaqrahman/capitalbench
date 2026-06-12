# CapitalBench Report: CB-2026-05-10-1M / official-round-1-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-round-1-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench May 10 2026 One-Month Round
- Description: One-month CapitalBench official evaluation round using the frozen May 10, 2026 briefing.
- Decision date: 2026-05-10
- Decision deadline: 2026-05-11T01:00:00Z
- Horizon: one month
- Entry date: 2026-05-08
- Exit date: 2026-06-10
- Entry rule: Use Tiingo EOD adjusted close from the last trading close before the decision deadline; CASH return is 0 unless explicitly priced.
- Exit rule: Use Tiingo EOD adjusted close on the exit_date for each selected option; CASH return is 0 unless explicitly priced.
- Options: 40

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | single_pick | SEMICONDUCTORS | 1 | 0.6 | Semiconductors have exhibited exceptional momentum, returning over 29% in the last 30 days and 58% over the last 6 months. Despite broader macroeconomic uncertainties and geopolitical tensions, the sector's strong trend and potential AI-driven earnings growth make it a compelling candidate for continued outperformance over a one-month horizon. | Geopolitical escalation in the Middle East or elsewhere could disrupt global semiconductor supply chains.; A sudden spike in long-term Treasury yields could disproportionately compress valuations for high-growth technology stocks.; Extreme recent outperformance leaves the sector vulnerable to sharp mean-reversion or profit-taking. |
| anthropic-claude-opus-4-7 | anthropic | single_pick | SEMICONDUCTORS | 1 | 0.58 | Semiconductors show dominant momentum (+29.7% 30d, +154% 1y) with strong Q1 earnings growth (27.7%) and AI capex tailwinds, while the Fed remains on hold with easing bias and credit/volatility conditions stay benign. The sector's trend persistence combined with broad risk-on positioning (Russell 2000 +12.3% April, EM +22% YTD) supports continued outperformance over a one-month horizon. | Middle East escalation (Iran ceasefire rejection, drone activity, Strait of Hormuz risk) could spike oil and crush high-beta tech; Hot March CPI (3.3% YoY, 0.9% MoM) and upcoming April CPI print could push real yields higher, compressing semiconductor multiples; Weak April payrolls (115k) signal slowing growth that could undermine cyclical chip demand; Extended valuations and crowded positioning after parabolic run make sector vulnerable to sharp factor rotation; Concentration risk in a few mega-cap names with binary earnings/guidance sensitivity |
| xai-grok-4-3 | xai | single_pick | SEMICONDUCTORS | 1 | 0.55 | Semiconductors show the strongest recent 30-day momentum at 29.68% amid sustained AI-driven demand and earnings growth estimates of 27.7% for Q1. Weakening labor data and geopolitical tensions favor high-growth tech themes over cyclicals or defensives in the one-month window. | Geopolitical escalation in the Middle East disrupting semiconductor supply chains; Sticky inflation readings on May 12 CPI release prompting delayed rate cuts; Potential rotation out of momentum stocks if Q1 earnings disappoint |
| openai-gpt-5-5 | openai | single_pick | SEMICONDUCTORS | 1 | 0.34 | Semiconductors show the strongest cross-horizon price momentum in the allowed universe, with very large 7-day, 30-day, 6-month, and 1-year trailing returns. With broad equity risk appetite still positive, volatility contained, and reported S&P 500 earnings growth strong, the highest-beta AI/technology exposure has a plausible chance to remain the top one-month performer. | A hot May 12 CPI release could push yields higher and compress high-multiple semiconductor valuations.; The recent 29.68% 30-day gain creates elevated reversal or profit-taking risk over a one-month horizon.; Middle East escalation or oil-price-driven inflation could trigger a risk-off rotation away from growth equities.; Any disappointment in AI-capex expectations or mega-cap technology guidance could disproportionately hurt semiconductor stocks. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| HEALTHCARE | Healthcare Sector | 143.49 | 152.85 | 0.06523102655237278 | 1 |
| ENERGY | Energy Sector | 55.7 | 58.25 | 0.04578096947935362 | 2 |
| DIVIDEND | US Dividend Equities | 31.62 | 32.26 | 0.020240354206198408 | 3 |
| FINANCIALS | Financials Sector | 51.24 | 52.23 | 0.01932084309133475 | 4 |
| LOW_VOL | US Low Volatility Equities | 72.4953925408 | 73.89 | 0.01923718750009007 | 5 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.18 | 85.49 | 0.015561891185554622 | 6 |
| REAL_ESTATE | Real Estate Sector | 44.41 | 44.99 | 0.01306012159423564 | 7 |
| MOMENTUM | US Momentum Equities | 301.8 | 304.92 | 0.010337972166998055 | 8 |
| SEMICONDUCTORS | Semiconductors | 566.54 | 570.91 | 0.007713488897518328 | 9 |
| TECHNOLOGY | Technology Sector | 175.52 | 176.63 | 0.006324065633545928 | 10 |
| LARGE_VALUE | US Large-Cap Value | 233.9 | 235.24 | 0.005728943993159374 | 11 |
| SOFTWARE | Software | 91.15 | 91.58 | 0.00471749862863402 | 12 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.1914123568 | 91.47 | 0.0030549767351994994 | 13 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 14 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.7315555334 | 79.47 | -0.0032804519070298577 | 15 |
| SMALL_VALUE | US Small-Cap Value | 211.63 | 210.92 | -0.00335491187449799 | 16 |
| MID_CAP | US Mid-Cap Stocks | 73.99 | 73.65 | -0.0045952155696714625 | 17 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.8484350224 | 98.31 | -0.005447076853346 | 18 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.787540126 | 108.16 | -0.005768492653415724 | 19 |
| SMALL_CAP | US Small-Cap Stocks | 284.17 | 282.05 | -0.007460323046064032 | 20 |
| TIPS | Treasury Inflation-Protected Securities | 110.1203688724 | 109.21 | -0.008267034352698821 | 21 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.6414131044 | 93.69 | -0.010052820147037456 | 22 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.742927068 | 84.88 | -0.010064119543244043 | 23 |
| TOTAL_US_MARKET | Total US Stock Market | 362.87 | 358.04 | -0.013310551988315322 | 24 |
| UTILITIES | Utilities Sector | 44.72 | 44.0 | -0.01610017889087656 | 25 |
| EUROPE | Europe Equities | 88.12 | 86.69 | -0.016227871084884327 | 26 |
| SP500 | S&P 500 | 737.62 | 725.43 | -0.01652612456278313 | 27 |
| INDUSTRIALS | Industrials Sector | 173.2 | 169.66 | -0.020438799076212377 | 28 |
| NASDAQ100 | Nasdaq 100 | 711.23 | 693.69 | -0.02466150190515015 | 29 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.83 | 68.81 | -0.028518989128900163 | 30 |
| LARGE_GROWTH | US Large-Cap Growth | 123.54 | 119.69 | -0.031163995467055283 | 31 |
| JAPAN | Japan Equities | 92.22 | 89.29 | -0.03177184992409443 | 32 |
| BROAD_COMMODITIES | Broad Commodities | 18.07 | 17.43 | -0.035417819590481514 | 33 |
| MATERIALS | Materials Sector | 51.59 | 49.6 | -0.03857336693157587 | 34 |
| EMERGING_MARKETS | Emerging Markets | 60.54 | 57.72 | -0.04658077304261643 | 35 |
| COMMUNICATIONS | Communication Services Sector | 116.94 | 111.01 | -0.05070976569180774 | 36 |
| INDIA | India Equities | 49.84 | 47.3 | -0.050963081861958415 | 37 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 120.2 | 113.49 | -0.05582362728785362 | 38 |
| CHINA | China Equities | 58.32 | 54.11 | -0.07218792866941015 | 39 |
| GOLD | Gold | 88.87 | 76.79 | -0.13592888488803867 | 40 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 100.0 | 0.007713488897518328 | 0.007713488897518328 | Semiconductors show dominant momentum (+29.7% 30d, +154% 1y) with strong Q1 earnings growth (27.7%) and AI capex tailwinds, while the Fed remains on hold with easing bias and credit/volatility conditions stay benign. The sector's trend persistence combined with broad risk-on positioning (Russell 2000 +12.3% April, EM +22% YTD) supports continued outperformance over a one-month horizon. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 100.0 | 0.007713488897518328 | 0.007713488897518328 | Semiconductors have exhibited exceptional momentum, returning over 29% in the last 30 days and 58% over the last 6 months. Despite broader macroeconomic uncertainties and geopolitical tensions, the sector's strong trend and potential AI-driven earnings growth make it a compelling candidate for continued outperformance over a one-month horizon. |
| openai-gpt-5-5 | SEMICONDUCTORS | 100.0 | 0.007713488897518328 | 0.007713488897518328 | Semiconductors show the strongest cross-horizon price momentum in the allowed universe, with very large 7-day, 30-day, 6-month, and 1-year trailing returns. With broad equity risk appetite still positive, volatility contained, and reported S&P 500 earnings growth strong, the highest-beta AI/technology exposure has a plausible chance to remain the top one-month performer. |
| xai-grok-4-3 | SEMICONDUCTORS | 100.0 | 0.007713488897518328 | 0.007713488897518328 | Semiconductors show the strongest recent 30-day momentum at 29.68% amid sustained AI-driven demand and earnings growth estimates of 27.7% for Q1. Weakening labor data and geopolitical tensions favor high-growth tech themes over cyclicals or defensives in the one-month window. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | SEMICONDUCTORS | 1 | 0.6 | 0.007713488897518328 |  | 0.024239613460301457 | 0.057517537654854456 | 9 | True | True |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 1 | 0.58 | 0.007713488897518328 |  | 0.024239613460301457 | 0.057517537654854456 | 9 | True | True |
| xai-grok-4-3 | SEMICONDUCTORS | 1 | 0.55 | 0.007713488897518328 |  | 0.024239613460301457 | 0.057517537654854456 | 9 | True | True |
| openai-gpt-5-5 | SEMICONDUCTORS | 1 | 0.34 | 0.007713488897518328 |  | 0.024239613460301457 | 0.057517537654854456 | 9 | True | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | cea86d1651e4dd4ed86f33bfe3e4fd5d4ff2a6fa3b068c611c7aa4fc01844479 |
| options.yaml | 451c26dbfd8a498bef50df205d8c7489acf8edde5c48c21e132bda42e47cf056 |
| prompt.md | 3e45c33a3f6e05123183178793e55b179febd00a121af2f63ba41b825981c998 |
| manifest.yaml | 6e2a34c3e1a363db1dcc89476a02867c0ce47fbe5110aa85782780f4f193b860 |
| market_data/universe_trailing_returns.csv | 5df42a20f8737269af41183cf74d4497fc521a8dc4a3b010357b514dd1149b1e |
| market_data/universe_trailing_returns.md | f8591c9853b2636007ac0791a1a1c4bc400e54113f5eacee27ca6050f08ddc49 |
| market_data/universe_trailing_returns.json | fecfc3b0246786c2d25772808fd421d28c149b87c2bc33ebde572f02ac0a4535 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | caa9ad75678d373dd619d9d68bc1a074fe4c9e3fdb2ed4ba67a5dd8f752b3bb3 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 79ff758a09c9c8da014c19cfa04afc8ce4462a46166da0327cd0a50e812c6e23 | yes |
| Final briefing | research/final_briefing.md | model-facing | cea86d1651e4dd4ed86f33bfe3e4fd5d4ff2a6fa3b068c611c7aa4fc01844479 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
