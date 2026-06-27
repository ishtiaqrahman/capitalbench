# CapitalBench Report: CB-2026-05-28-1M / official-20260528-1M

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260528-1M
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench May 28 2026 One-Month Portfolio Round
- Description: One-month CapitalBench portfolio evaluation round scored from the May 28, 2026 adjusted close to the June 26, 2026 adjusted close.
- Decision date: 2026-05-28
- Decision deadline: 2026-05-28T22:00:00Z
- Horizon: one month
- Entry date: 2026-05-28
- Exit date: 2026-06-26
- Entry rule: Use adjusted close on Thursday, May 28, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Friday, June 26, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 65

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SEMICONDUCTORS | 3 | 0.55 | Recent trailing returns and AI-related facts favor semiconductors, technology, and momentum over the one-month window ending June 26. | Hotter May CPI or employment data on June 5/10 could raise rate concerns before FOMC; Taiwan/China geopolitical flare-up could hit semiconductor holdings sharply; FOMC June 17 statement disappoints growth expectations priced into tech |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.6 | Overweight the leading AI/semiconductor and momentum complex which shows the strongest near-term trend and fundamental support, with a gold sleeve to dampen event risk around June macro releases. | Semiconductor/AI momentum reverses sharply given stretched valuations and crowded positioning, hitting SMH, TECHNOLOGY, TAIWAN, and MOMENTUM together due to high correlation.; Hot May CPI (June 10) or sticky PCE (June 26) revives rate-hike fears, pressuring growth and tech multiples.; Hawkish surprise or geopolitical Taiwan-strait stress around the June 16-17 FOMC triggers a risk-off drawdown.; Gold sells off on stronger dollar or rising real yields, weakening the intended hedge. |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.58 | Over the one-month scoring window, the best expected alpha appears to come from continuing AI/semiconductor momentum rather than defensive assets or broad beta. The allocation emphasizes high-upside leaders while retaining some diversification through broader technology and momentum exposure. | A hotter-than-expected June CPI or PCE release could lift yields and trigger a sharp growth-stock and semiconductor multiple compression.; AI and semiconductor leaders may be crowded after very large trailing gains, making the portfolio vulnerable to profit-taking or factor rotation before June 26.; South Korea and Taiwan exposures add currency, geopolitical, and export-cycle risk that could overwhelm sector fundamentals over a short window.; Any disappointment in chip demand, AI capex commentary, or supply-chain data could cause semiconductor-linked assets to underperform the S&P 500. |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 4 | 0.75 | Allocating to high-momentum technology and semiconductor assets, along with heavily correlated Asian markets (South Korea and Taiwan), to capture the ongoing AI infrastructure boom. | A sudden reversal in the AI/semiconductor momentum trade due to valuation concerns or profit-taking.; A hawkish surprise from the June FOMC meeting, which could disproportionately impact high-duration growth and tech equities.; Geopolitical tensions affecting Taiwan or South Korea, disrupting semiconductor supply chains. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.6 | Concentrated in highest-momentum AI/tech complex with defense and gold hedges for a one-month window dominated by Fed hold and continued AI capex narrative. | Semiconductor/AI sentiment reversal or negative guide from a mega-cap chipmaker; Hot May CPI (June 10) reigniting rate-cut delay fears and hitting growth multiples; Oil shock from OPEC+/geopolitics pressuring tech margins via inflation; Gold pullback if real yields rise on hawkish June FOMC dots; Momentum factor crash / sharp rotation to value |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 135.8613722724 | 155.3800048828125 | 0.14366579907111454 | 1 |
| REGIONAL_BANKS | Regional Banks | 69.1497106809 | 75.16999816894531 | 0.0870616439138363 | 2 |
| HEALTHCARE | Healthcare Sector | 150.2230350049 | 160.33999633789062 | 0.06734627171299423 | 3 |
| FINANCIALS | Financials Sector | 51.0920028831 | 53.56999969482422 | 0.04850067861684626 | 4 |
| INDUSTRIALS | Industrials Sector | 173.376482642 | 181.1999969482422 | 0.04512442626025992 | 5 |
| UTILITIES | Utilities Sector | 44.3479511955 | 46.20000076293945 | 0.04176178419776422 | 6 |
| LOW_VOL | US Low Volatility Equities | 72.7831589161 | 75.76000213623047 | 0.040900165154441614 | 7 |
| MOMENTUM | US Momentum Equities | 314.3126774828 | 325.739990234375 | 0.036356512384710715 | 8 |
| SMALL_VALUE | US Small-Cap Value | 214.5847683336 | 221.42999267578125 | 0.03189986127784916 | 9 |
| SMALL_CAP | US Small-Cap Stocks | 291.3426502677 | 299.8299865722656 | 0.029131801666412604 | 10 |
| REAL_ESTATE | Real Estate Sector | 44.0287760127 | 45.2400016784668 | 0.02750986458077831 | 11 |
| US_DOLLAR | US Dollar | 27.7 | 28.459999084472656 | 0.02743679005316446 | 12 |
| MID_CAP | US Mid-Cap Stocks | 74.2652525078 | 76.22000122070312 | 0.026321175070371128 | 13 |
| LARGE_VALUE | US Large-Cap Value | 237.2887913067 | 242.75999450683594 | 0.023057149770990604 | 14 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.4042584435 | 87.36000061035156 | 0.022899820248956315 | 15 |
| SEMICONDUCTORS | Semiconductors | 599.83 | 611.6099853515625 | 0.019638873266696333 | 16 |
| INDIA | India Equities | 48.69 | 49.560001373291016 | 0.017868173614520755 | 17 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 207.4482547057 | 210.30999755859375 | 0.013794971941092582 | 18 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.8441844176 | 84.70999908447266 | 0.010326472526231756 | 19 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.2228221872 | 95.02999877929688 | 0.008566678150365714 | 20 |
| MATERIALS | Materials Sector | 51.168447418 | 51.599998474121094 | 0.008433929069524337 | 21 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.7504961761 | 107.5999984741211 | 0.007957829972234709 | 22 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.1458150593 | 48.5099983215332 | 0.007564172748652176 | 23 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.8237893732 | 96.54000091552734 | 0.007474256100830523 | 24 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.6690367737 | 99.33999633789062 | 0.006800102505606587 | 25 |
| JAPAN | Japan Equities | 92.2088842675 | 92.80000305175781 | 0.0064106489190669524 | 26 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.8473134997 | 109.5 | 0.005996349191492056 | 27 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.3763986423 | 94.93000030517578 | 0.005865890951974206 | 28 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 235.4077927265 | 236.77999877929688 | 0.005829059594433694 | 29 |
| TAIWAN | Taiwan Equities | 102.34 | 102.80999755859375 | 0.004592510832458041 | 30 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.3609131233 | 91.63 | 0.0029453172861444443 | 31 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.8210968361 | 79.83000183105469 | 0.00011156192169314849 | 32 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 33 |
| TIPS | Treasury Inflation-Protected Securities | 109.9028959715 | 109.69999694824219 | -0.0018461663040292287 | 34 |
| EUROPE | Europe Equities | 87.8367849906 | 87.12999725341797 | -0.008046602995062546 | 35 |
| CANADA | Canada Equities | 58.3074135836 | 57.79999923706055 | -0.008702398466224781 | 36 |
| DIVIDEND | US Dividend Equities | 32.3718012073 | 32.09000015258789 | -0.008705139788408367 | 37 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.2881305099 | 70.55999755859375 | -0.010213943697192751 | 38 |
| UNITED_KINGDOM | United Kingdom Equities | 46.3319891701 | 45.7599983215332 | -0.012345484379417293 | 39 |
| YEN | Japanese Yen | 57.65 | 56.709999084472656 | -0.016305306427187194 | 40 |
| AUSTRALIA | Australia Equities | 28.5656295427 | 27.969999313354492 | -0.02085129013016007 | 41 |
| EMERGING_MARKETS | Emerging Markets | 59.8300981246 | 58.58000183105469 | -0.020894104016709214 | 42 |
| EURO | Euro | 107.4349364496 | 105.08999633789062 | -0.021826606774319024 | 43 |
| TOTAL_US_MARKET | Total US Stock Market | 370.5921764272 | 362.22 | -0.022591346929971223 | 44 |
| AGRICULTURE | Agriculture Commodities | 27.58 | 26.799999237060547 | -0.028281390969523312 | 45 |
| TECHNOLOGY | Technology Sector | 186.6286311509 | 181.11000061035156 | -0.029570117438659782 | 46 |
| MEXICO | Mexico Equities | 77.6734336924 | 75.37000274658203 | -0.029655325332210047 | 47 |
| BRAZIL | Brazil Equities | 35.7685221321 | 34.66999816894531 | -0.030712031072953727 | 48 |
| SP500 | S&P 500 | 752.6813389245 | 728.99 | -0.03147592174711322 | 49 |
| NASDAQ100 | Nasdaq 100 | 734.7899934795 | 706.52 | -0.03847356895217269 | 50 |
| SOUTH_KOREA | South Korea Equities | 206.41 | 197.27999877929688 | -0.04423235899764122 | 51 |
| COPPER | Copper | 39.06 | 37.33000183105469 | -0.04429078773541517 | 52 |
| ENERGY | Energy Sector | 56.5474150405 | 53.84000015258789 | -0.04787866759202031 | 53 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 121.8128346155 | 114.37000274658203 | -0.06110055555649063 | 54 |
| LARGE_GROWTH | US Large-Cap Growth | 127.0109478854 | 119.04 | -0.06275795920043092 | 55 |
| CHINA | China Equities | 54.6306737797 | 50.47999954223633 | -0.07597699150117387 | 56 |
| SOUTH_AFRICA | South Africa Equities | 68.2648250883 | 63.0099983215332 | -0.0769770780188731 | 57 |
| SOFTWARE | Software | 95.6626263128 | 88.19999694824219 | -0.07800987336638998 | 58 |
| COMMUNICATIONS | Communication Services Sector | 116.3610258689 | 106.18000030517578 | -0.0874951512991543 | 59 |
| GOLD | Gold | 84.59 | 76.55999755859375 | -0.09492850740520453 | 60 |
| BROAD_COMMODITIES | Broad Commodities | 17.72 | 15.869999885559082 | -0.10440181232736556 | 61 |
| BITCOIN_ETF | Bitcoin ETF | 41.56 | 33.849998474121094 | -0.18551495490565229 | 62 |
| OIL | Crude Oil | 130.78 | 105.4800033569336 | -0.19345463100677784 | 63 |
| ETHEREUM_ETF | Ethereum ETF | 15.19 | 11.890000343322754 | -0.21724816699652705 | 64 |
| SILVER | Silver | 68.36 | 53.279998779296875 | -0.22059685811444008 | 65 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 35.0 | 0.019638873266696333 | 0.006873605643343716 | Strongest momentum (+22% 30d), SIA chip sales +25% QoQ, AI capex set to grow 75% in 2026. |
| anthropic-claude-opus-4-7 | TECHNOLOGY | 25.0 | -0.029570117438659782 | -0.0073925293596649455 | Leading sector with strong AI-driven earnings tailwind and momentum into June FOMC hold. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 15.0 | 0.005829059594433694 | 0.0008743589391650541 | FY2027 defense budget request +28%, strong 7d/30d momentum, geopolitical bid. |
| anthropic-claude-opus-4-7 | GOLD | 15.0 | -0.09492850740520453 | -0.014239276110780678 | Hedge against sticky 3.8% CPI and geopolitical risk; spot near record highs. |
| anthropic-claude-opus-4-7 | MOMENTUM | 10.0 | 0.036356512384710715 | 0.0036356512384710716 | Factor with strongest trailing performance, likely to persist through June FOMC. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 35.0 | 0.019638873266696333 | 0.006873605643343716 | Strongest momentum (5.6% 7d, 22% 30d) backed by 79% YoY chip sales growth and massive AI capex acceleration; leadership likely to persist through window. |
| anthropic-claude-opus-4-8 | MOMENTUM | 25.0 | 0.036356512384710715 | 0.009089128096177679 | Momentum factor up 14% in 30d with broad trend persistence; lower single-name risk than thematic plays while capturing the leading equity trend. |
| anthropic-claude-opus-4-8 | TECHNOLOGY | 20.0 | -0.029570117438659782 | -0.005914023487731956 | Tech sector up 18% in 30d with AI infrastructure and software pricing tailwinds; Fed on hold removes near-term rate risk for growth. |
| anthropic-claude-opus-4-8 | TAIWAN | 10.0 | 0.004592510832458041 | 0.0004592510832458041 | Semiconductor supply-chain leverage with 8.3% 7d momentum; benefits from same AI chip demand cycle as SMH. |
| anthropic-claude-opus-4-8 | GOLD | 10.0 | -0.09492850740520453 | -0.009492850740520455 | Hedge against sticky 3.8% PCE inflation and risk-off into the June 16-17 FOMC; near-record gold price provides ballast if growth equities wobble. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | 0.019638873266696333 | 0.007855549306678533 | Strong momentum and fundamental support from AI infrastructure buildout, with global chip sales up 25% QoQ and 79.2% YoY. |
| google-gemini-3-1-pro | TECHNOLOGY | 30.0 | -0.029570117438659782 | -0.008871035231597935 | Broad tech exposure benefits from the same AI tailwinds and strong software pricing power noted in the briefing. |
| google-gemini-3-1-pro | SOUTH_KOREA | 15.0 | -0.04423235899764122 | -0.006634853849646183 | High beta to the semiconductor cycle and strong recent momentum (up 10.7% in 7 days, 132% in 6 months). |
| google-gemini-3-1-pro | TAIWAN | 15.0 | 0.004592510832458041 | 0.0006888766248687061 | Direct beneficiary of semiconductor and AI hardware demand, showing strong momentum (up 8.33% in 7 days). |
| openai-gpt-5-5 | SEMICONDUCTORS | 40.0 | 0.019638873266696333 | 0.007855549306678533 | Strongest AI-linked fundamental backdrop, with global chip sales sharply higher and very strong 7-day, 30-day, 6-month, and 1-year momentum. |
| openai-gpt-5-5 | SOUTH_KOREA | 25.0 | -0.04423235899764122 | -0.011058089749410305 | Exceptionally strong recent and medium-term momentum, with heavy sensitivity to the global semiconductor and export cycle. |
| openai-gpt-5-5 | TAIWAN | 15.0 | 0.004592510832458041 | 0.0006888766248687061 | High semiconductor supply-chain exposure and strong trailing performance support potential continued AI hardware leadership. |
| openai-gpt-5-5 | TECHNOLOGY | 10.0 | -0.029570117438659782 | -0.002957011743865978 | Broad technology exposure benefits from AI capex, strong sector momentum, and easier diversification than a pure semiconductor position. |
| openai-gpt-5-5 | MOMENTUM | 10.0 | 0.036356512384710715 | 0.0036356512384710716 | Captures persistence in recent market leaders during a low-volatility, tight-spread risk-on environment. |
| xai-grok-4-3 | SEMICONDUCTORS | 50.0 | 0.019638873266696333 | 0.009819436633348166 | Strong 30d momentum and Q1 chip sales growth plus AI infrastructure spend point to continued outperformance into June data window. |
| xai-grok-4-3 | TECHNOLOGY | 30.0 | -0.029570117438659782 | -0.008871035231597935 | Sector leadership and software price acceleration support relative gains ahead of FOMC and inflation prints. |
| xai-grok-4-3 | MOMENTUM | 20.0 | 0.036356512384710715 | 0.007271302476942143 | Factor has led recent returns and should capture continuation of growth tilt through the June 17 FOMC decision. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SEMICONDUCTORS | 3 | 0.55 | 0.019638873266696333 | 0.008219703878692374 | 0.0396956256258056 | 0.13544609519242218 |  | True | True |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.6 | 0.019638873266696333 | 0.0010151105945147877 | 0.03249103234162801 | 0.14265068847659976 |  | True | True |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.58 | 0.019638873266696333 | -0.0018350243232579722 | 0.02964089742385525 | 0.1455008233943725 |  | True | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 4 | 0.75 | 0.019638873266696333 | -0.006961463149696878 | 0.024514458597416345 | 0.1506272622208114 |  | True | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.6 | 0.019638873266696333 | -0.010248189649465783 | 0.021227732097647438 | 0.15391398872058032 |  | True | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 7374fa733d9fd85e9c64d435abb9ad786f73c89fa2e8bd226dc8d9e4cde94384 |
| options.yaml | 8e07e0a1d09976c253d8b385fffa546b2e406bbad7499c7fc9f3fe35f15afcb1 |
| prompt.md | 89a7945fd04cdf604089a077dab431ec90b45ca9475f8af9e0749d3e653f7419 |
| manifest.yaml | 82a26ae3e613d179bd05a368dcc728ef9da14a9a30dc4f0d75d413413cf0c12f |
| market_data/universe_trailing_returns.csv | 095124e477ab6e8a42084248334a5b1d3bb36d4192a4ea77c152f7ac49fea380 |
| market_data/universe_trailing_returns.md | 73926262ce4f8fdccc02f0d6251617a114526b1b8bd1d369b4524065e19ef8ac |
| market_data/universe_trailing_returns.json | 47ec7b55b64d30846bb8f3fbb7944a458a5ab63a791a33eabebdb0e5406102d9 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 20fb9a406f4eb8b35566466e5697a048b463b7f74cb72ccbefbc0da7703752d8 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | a3d445624cf7192777c54717fe16bd7650ed3add58abd8ae2986dce5aed4fef2 | yes |
| Final briefing | research/final_briefing.md | model-facing | 7374fa733d9fd85e9c64d435abb9ad786f73c89fa2e8bd226dc8d9e4cde94384 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
