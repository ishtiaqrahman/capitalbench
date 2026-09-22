# CapitalBench Report: CB-2026-08-20-1M / official-v3-20260820-monthly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260820-monthly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-20-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-08-20
- Decision deadline: 2026-08-20T13:25:00Z
- Horizon: one month
- Entry date: 2026-08-20
- Exit date: 2026-09-21
- Entry rule: Use the Thursday, August 20, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Monday, September 21, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | openai | portfolio | SEMICONDUCTORS | 3 | 0.57 | Broad participation and falling long yields support selective pullback reversals, but weak employment, persistent inflation risk, and major earnings and central-bank events make continuation unreliable and dispersion likely to remain high. | NVIDIA results could disappoint and extend the high-beta technology selloff.; August inflation data or the September FOMC could push long yields higher, hurting both technology and real estate.; Weak payrolls could develop into broader growth and credit stress rather than a benign easing catalyst.; High cross-sectional volatility makes one-month reversal timing unusually uncertain. |
| xai-grok-4-5 | xai | portfolio | SEMICONDUCTORS | 3 | 0.5633 | SPY near flat on 5s after solid 21s; equal-weight outperforming; VIX mid-teens; sticky inflation and elevated long yields with Sept FOMC and Jackson Hole ahead; AI/semicap prior strength with recent pullbacks; commodity and factor dispersion mixed rather than one-way trend. | NVIDIA and broader AI/semicap earnings disappointment could extend SMH drawdown given 2+ beta; Sticky inflation prints and hawkish Jackson Hole/FOMC path could pressure equities and rate-sensitive names; High-vol commodity and EM reversals (oil, silver, metals, Brazil) can gap against mean-reversion bets; Sudden USD rebound would hurt international and precious-metal adjacent exposures |
| anthropic-claude-opus-5 | anthropic | portfolio | SEMICONDUCTORS | 3 | 0.565 | Index level is near highs with modest week-to-date softness, VIX ~15.7, but cross-sectional dispersion is very high: semis, Korea and Japan sold off sharply while healthcare, biotech, energy, gold/silver and crypto surged. Rates are mildly easing at the long end with Treasury announcing larger longer-dated purchases; Fed remains on hold with hawkish dissents and hot 3.4% CPI / 4.7% PPI. NVIDIA earnings (Aug 26), Jackson Hole, Sept CPI and the Sept 15-16 FOMC all fall inside the window, making AI-complex names the highest-variance bet. I treat the semiconductor drawdown as an overreaction within an intact prior uptrend (prior active +32%), and see modest reversal value in the dollar and utilities. Most other slate names lack independent support. | A weak NVIDIA print or AI capex guidance cut on Aug 26 would extend the semiconductor drawdown sharply given 54% volatility and 2.38 beta.; Dovish Jackson Hole or soft Sept 4 payrolls could push the dollar lower and invalidate the UUP reversal.; Persistent 3.4% CPI / 4.7% PPI could force a hawkish Sept 16 FOMC, hitting both long-duration equities and utilities.; High cross-sectional dispersion means concentrated 35% sleeves carry large tracking error versus SPY over one month. |
| anthropic-claude-fable-5 | anthropic | portfolio | SP500 | 2 | 0.58 | SPY is near highs with modest weekly pullback; breadth is broadening (RSP outpacing SPY). The dominant setup is a quality pullback in strong prior-trend tech (semis) into the NVIDIA earnings catalyst on Aug 26, while shock-reversal names like solar and silver show fundamental or trendless weakness. Rate cuts are constrained by sticky inflation, capping bond upside. | NVIDIA earnings disappointment could extend the semiconductor drawdown sharply given 2.4 beta; Sticky inflation prints (Sep 10-11 PPI/CPI) or a hawkish Sep 15-16 FOMC could hit high-beta tech; Oil above $90 and rising long yields could pressure equity multiples broadly; BoJ tightening on Sep 17-18 could trigger carry-trade unwind volatility |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | SPY is within about 1% of its 52-week high with VIX near 16, equal-weight outperforming, and a one-month window that includes Jackson Hole, August CPI/PPI, NVIDIA results, and the mid-September FOMC. Sticky inflation, a hawkish-leaning July minutes split, and cooling payrolls favor mixed rather than a clean continuation or reversal regime. | September FOMC and August CPI/PPI can reprice duration, the dollar, and growth beta together.; NVIDIA results and semiconductor beta can dominate one-month tech and SMH outcomes.; Sticky energy CPI and inventory builds can reverse oil and commodity continuation.; Jackson Hole commentary can move rates and utilities independently of earnings. |
| xai-grok-4-3 | xai | portfolio | SEMICONDUCTORS | 3 | 0.6 | Mixed cross-asset signals with recent equity pullbacks in growth and commodities offset by stable macro data and limited dispersion; reversal candidates in high-vol sectors show overreaction potential within one-month window. | Inflation persistence per FOMC minutes; Equity volatility from AI concentration; Commodity inventory surprises in energy |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.58 | The market is showing mixed signals with recent volatility and a slight pullback in major indices, while inflation data remains somewhat sticky and the Fed maintains its current rate stance. | Inflation remains persistent, leading to a more hawkish Fed stance.; A broader market downturn impacts high-beta sectors like semiconductors. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BITCOIN_ETF | Bitcoin ETF | 41.2 | 49.01 | 0.18956310679611632 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 17.55 | 20.85 | 0.18803418803418803 | 2 |
| BRAZIL | Brazil Equities | 34.14 | 38.07 | 0.11511423550087874 | 3 |
| TAIWAN | Taiwan Equities | 104.07 | 115.64 | 0.11117517055827819 | 4 |
| CYBERSECURITY | Cybersecurity | 93.45 | 103.09 | 0.10315676832530762 | 5 |
| OIL | Crude Oil | 134.54 | 148.16 | 0.10123383380407325 | 6 |
| TECHNOLOGY | Technology Sector | 183.1 | 194.85 | 0.06417258328782083 | 7 |
| SOUTH_KOREA | South Korea Equities | 178.16 | 189.16 | 0.06174225415356993 | 8 |
| SEMICONDUCTORS | Semiconductors | 562.65 | 596.03 | 0.05932640184839588 | 9 |
| BROAD_AI_TECH | Broad AI Technology | 63.03 | 66.31 | 0.052038711724575526 | 10 |
| SOFTWARE | Software | 101.91 | 107.13 | 0.05122166617603763 | 11 |
| BROAD_COMMODITIES | Broad Commodities | 18.55 | 19.44 | 0.04797843665768187 | 12 |
| NASDAQ100 | Nasdaq 100 | 710.93 | 741.47 | 0.042957815818716494 | 13 |
| JAPAN | Japan Equities | 94.27 | 97.96 | 0.039142887450938746 | 14 |
| COMMUNICATIONS | Communication Services Sector | 110.68 | 114.75 | 0.036772677990603464 | 15 |
| MOMENTUM | US Momentum Equities | 305.11 | 316.25 | 0.036511422110058644 | 16 |
| LARGE_GROWTH | US Large-Cap Growth | 121.82 | 126.25 | 0.03636512887867349 | 17 |
| COPPER | Copper | 39.35 | 40.67 | 0.03354510800508259 | 18 |
| US_DOLLAR | US Dollar | 27.91 | 28.48 | 0.02042278753135074 | 19 |
| EMERGING_MARKETS | Emerging Markets | 60.02 | 61.14 | 0.018660446517827278 | 20 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 123.68 | 125.49 | 0.014634540750323222 | 21 |
| SP500 | S&P 500 | 762.6 | 773.5 | 0.014293207448203393 | 22 |
| TOTAL_US_MARKET | Total US Stock Market | 376.58 | 381.1 | 0.012002761697381903 | 23 |
| AGRICULTURE | Agriculture Commodities | 28.38 | 28.68 | 0.010570824524313016 | 24 |
| YEN | Japanese Yen | 57.66 | 58.2 | 0.009365244536940764 | 25 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 26 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.57 | 91.57 | 0.0 | 26 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.34 | 81.8 | -0.006558173427252956 | 28 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.84 | 72.3 | -0.007413509060955614 | 29 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.06 | 105.09 | -0.009145766547237422 | 30 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.65 | 47.21 | -0.009233997901364033 | 31 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.67 | 93.78 | -0.009401077426851145 | 32 |
| LARGE_VALUE | US Large-Cap Value | 256.17 | 253.45 | -0.01061794901823021 | 33 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.56 | 78.68 | -0.011060834590246316 | 34 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.49 | 96.21 | -0.013129551748897295 | 35 |
| TIPS | Treasury Inflation-Protected Securities | 107.52 | 105.68 | -0.017113095238095122 | 36 |
| UNITED_KINGDOM | United Kingdom Equities | 48.54 | 47.69 | -0.017511330861145424 | 37 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.3 | 91.59 | -0.018327974276527215 | 38 |
| FINANCIALS | Financials Sector | 56.95 | 55.9 | -0.01843722563652339 | 39 |
| EURO | Euro | 107.8 | 105.8 | -0.01855287569573283 | 40 |
| HEALTHCARE | Healthcare Sector | 172.39 | 169.01 | -0.019606705725390028 | 41 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.0 | 91.15 | -0.019892473118279463 | 42 |
| ENERGY | Energy Sector | 63.75 | 62.46 | -0.020235294117647018 | 43 |
| INDIA | India Equities | 49.55 | 48.5 | -0.021190716448032276 | 44 |
| CANADA | Canada Equities | 61.77 | 60.43 | -0.021693378662781315 | 45 |
| MEXICO | Mexico Equities | 75.5 | 73.7 | -0.02384105960264893 | 46 |
| AUSTRALIA | Australia Equities | 29.75 | 29.04 | -0.023865546218487466 | 47 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.47 | 102.86 | -0.024746373376315578 | 48 |
| CHINA | China Equities | 55.51 | 54.0 | -0.02720230589083039 | 49 |
| EUROPE | Europe Equities | 92.01 | 89.24 | -0.030105423323551928 | 50 |
| BIOTECH | Biotechnology | 163.38 | 158.23 | -0.0315216060717346 | 51 |
| SOUTH_AFRICA | South Africa Equities | 70.47 | 68.23 | -0.03178657584787847 | 52 |
| DIVIDEND | US Dividend Equities | 34.83 | 33.72 | -0.031869078380706295 | 53 |
| SILVER | Silver | 61.66 | 59.63 | -0.032922478105741115 | 54 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.28 | 212.68 | -0.03450154349010348 | 55 |
| SMALL_VALUE | US Small-Cap Value | 223.81 | 215.95 | -0.03511907421473581 | 56 |
| REGIONAL_BANKS | Regional Banks | 74.71 | 71.99 | -0.036407442109489985 | 57 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.68 | 112.23 | -0.0381384984573192 | 58 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.32 | 81.92 | -0.03984997655883726 | 59 |
| SMALL_CAP | US Small-Cap Stocks | 297.67 | 285.58 | -0.04061544663553607 | 60 |
| GOLD | Gold | 85.13 | 81.67 | -0.04064372136732053 | 61 |
| MID_CAP | US Mid-Cap Stocks | 76.37 | 73.25 | -0.04085373837894468 | 62 |
| LOW_VOL | US Low Volatility Equities | 75.66 | 72.18 | -0.04599524187153037 | 63 |
| METALS_MINING | Metals and Mining | 114.7 | 109.0 | -0.04969485614646907 | 64 |
| MATERIALS | Materials Sector | 52.42 | 49.71 | -0.0516978252575353 | 65 |
| INDUSTRIALS | Industrials Sector | 179.77 | 169.98 | -0.05445847471769494 | 66 |
| REAL_ESTATE | Real Estate Sector | 45.08 | 42.59 | -0.055235137533274026 | 67 |
| SOLAR | Solar Energy | 49.73 | 46.71 | -0.06072793082646277 | 68 |
| UTILITIES | Utilities Sector | 43.77 | 40.66 | -0.07105323280785936 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 237.56 | 216.14 | -0.09016669472975258 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 35.0 | 0.05932640184839588 | 0.020764240646938558 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | SP500 | 65.0 | 0.014293207448203393 | 0.009290584841332206 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5 | SEMICONDUCTORS | 35.0 | 0.05932640184839588 | 0.020764240646938558 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | US_DOLLAR | 35.0 | 0.02042278753135074 | 0.007147975635972758 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SP500 | 30.0 | 0.014293207448203393 | 0.004287962234461018 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 35.0 | 0.05932640184839588 | 0.020764240646938558 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SMALL_VALUE | 35.0 | -0.03511907421473581 | -0.012291675975157533 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | UTILITIES | 30.0 | -0.07105323280785936 | -0.021315969842357806 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 35.0 | 0.05932640184839588 | 0.020764240646938558 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | CYBERSECURITY | 35.0 | 0.10315676832530762 | 0.03610486891385767 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | REAL_ESTATE | 30.0 | -0.055235137533274026 | -0.016570541259982207 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | SEMICONDUCTORS | 35.0 | 0.05932640184839588 | 0.020764240646938558 | V3 selected model rank 2: overreaction with 61% estimated probability of beating SPY. |
| xai-grok-4-3 | SMALL_VALUE | 35.0 | -0.03511907421473581 | -0.012291675975157533 | V3 selected model rank 4: overreaction with 59% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 30.0 | 0.014293207448203393 | 0.004287962234461018 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | SEMICONDUCTORS | 35.0 | 0.05932640184839588 | 0.020764240646938558 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | SMALL_VALUE | 35.0 | -0.03511907421473581 | -0.012291675975157533 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-5 | CYBERSECURITY | 30.0 | 0.10315676832530762 | 0.030947030497592287 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 100.0 | 0.014293207448203393 | 0.014293207448203393 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 3 | 0.57 | 0.05932640184839588 | 0.04029856830081402 | 0.026005360852610626 | 0.1492645384953023 |  | True | True |
| xai-grok-4-5 | SEMICONDUCTORS | 3 | 0.5633 | 0.05932640184839588 | 0.03941959516937331 | 0.025126387721169915 | 0.150143511626743 |  | True | True |
| anthropic-claude-opus-5 | SEMICONDUCTORS | 3 | 0.565 | 0.05932640184839588 | 0.032200178517372335 | 0.017906971069168942 | 0.15736292827874399 |  | True | True |
| anthropic-claude-fable-5 | SP500 | 2 | 0.58 | 0.014293207448203393 | 0.030054825488270764 | 0.01576161804006737 | 0.15950828130784556 |  | True | True |
| xai-grok-4-6 | SP500 | 1 | 0.5 | 0.014293207448203393 | 0.014293207448203393 | 0.0 | 0.17526989934791293 |  | False | True |
| xai-grok-4-3 | SEMICONDUCTORS | 3 | 0.6 | 0.05932640184839588 | 0.012760526906242043 | -0.0015326805419613506 | 0.17680257988987427 |  | False | True |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.58 | 0.05932640184839588 | -0.01284340517057678 | -0.027136612618780174 | 0.2024065119666931 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 4ad11240b473c99230551b0bc157ddcf090ed4d882ab174ff983565818e67531 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | 0aa5e66a1dbe81d6c5bc127084667478c59a10e167dcb27205b6a5cd497c1ea7 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 0c0d627677dfe8409497e0b7f73647793d38b8d1ec837354512c376b0ede4b2d |
| market_data/universe_decision_context.md | fbc62aa91a3fd8c02ade1e372b0325cd9c819f38de7cb89e2a1c8f87320e46bd |
| market_data/universe_decision_context.json | beeff64b7ed352039fd93d703d78809ee698f7c8a18b557e27c535f95bcf3b53 |
| market_data/decision_context_source_history.json | 5f0860998c161b302198e92804f6d7b346a263985ca648aa33e8af2617cf4467 |
| market_data/universe_quality_evidence.md | a663f5cde0e6bc4b100ecd4034100b3420eee6596b71d0d186c698496796f8ae |
| market_data/universe_quality_evidence.json | 829dfcfd04810115035b41967abd8bb88af588c6e784b17a9177badf9f28da6c |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | eaeaa350102a156008b5437e8e63108d2100b59865c6a32284413f2901ed448b | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | aaf4c8267fded99b7bd7599ca4d9ad9e8edea283e38d3337d6dfc5d277c86d84 | yes |
| Final briefing | research/final_briefing.md | model-facing | 4ad11240b473c99230551b0bc157ddcf090ed4d882ab174ff983565818e67531 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
