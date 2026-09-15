# CapitalBench Report: CB-2026-09-03-1W / official-v3-20260903-weekly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260903-weekly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-03-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-09-03
- Decision deadline: 2026-09-04T13:25:00Z
- Horizon: one week
- Entry date: 2026-09-04
- Exit date: 2026-09-14
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Commodity and select international strength contrasts with equity pullbacks and policy uncertainty ahead of FOMC and employment data. | FOMC meeting and employment data release within window; Geopolitical developments in energy markets; Volatility in crypto and commodity prices |
| google-gemini-3-1-pro | google | portfolio | CYBERSECURITY | 3 | 0.58 | The market is showing mixed signals with some sectors experiencing pullbacks while others continue to show strength. The upcoming employment report and FOMC meeting add uncertainty. | The upcoming employment report could cause market volatility.; Uncertainty surrounding the upcoming FOMC meeting could impact interest rate-sensitive sectors. |
| xai-grok-4-5 | xai | portfolio | CYBERSECURITY | 3 | 0.59 | Mixed cross-section with modest SPY gains, elevated oil/geopolitics, soft labor signals ahead of jobs data, and several high-quality pullbacks in prior-strong names amid normal 5s dispersion; FOMC blackout and Labor Day shorten effective window. | August Employment Situation release Sept 4 could swing rates and risk appetite sharply; Active Iran/Hormuz conflict and OPEC+ Sept 6 meeting amplify oil and risk-off volatility; FOMC blackout and Sept 15-16 meeting uncertainty compress equity risk premia; High-vol names (cyber, silver, semis) can extend drawdowns if jobs hot or geopolitics escalate |
| xai-grok-4-6 | xai | portfolio | CYBERSECURITY | 3 | 0.5633 | SPY is near a 52-week high with modest 5-session gains while 5s active-return dispersion is only 2.20% and equal-weight lags. The window includes unknown NFP (Sep 4) and CPI (Sep 11) plus Labor Day, so mega-cap beta is fragile. Oil and Brazil show short continuation after large moves; several high-quality names (cyber, metals, silver, biotech, semis) show sharp relative pullbacks after stronger prior windows. | August Employment Situation (Sep 4) and CPI (Sep 11) can reverse high-beta pullback trades if prints are hot, consistent with Waller’s hike-if-hot comment.; Hormuz/Iran conflict and the Sep 6 OPEC+ meeting can keep oil volatile and crowd out metals/silver mean reversion.; Labor Day short week plus Fed blackout starting Sep 5 can thin liquidity in 30-50% vol names (CIBR, XME, SLV).; Broadcom-supported semis and mega-cap Sep 3 rally can keep SPY concentrated leadership if equal-weight continues to lag. |
| openai-gpt-5-6-sol | openai | portfolio | METALS_MINING | 3 | 0.58 | Breadth is weak despite a rising SPY, while commodity and technology pullbacks coexist with geopolitical and inflation catalysts. The employment, PPI, CPI, OPEC+, ECB, and earnings calendar creates unusually high one-week event risk. | September 4 employment data or September 11 CPI could sharply reprice rates and equity factors.; A rapid de-escalation in the Iran conflict could reverse precious-metals and mining support.; Oracle or Adobe results could disappoint and deepen the software pullback.; Thin post-holiday trading and high volatility could overwhelm cross-sectional reversal signals. |
| anthropic-claude-opus-5 | anthropic | portfolio | SILVER | 3 | 0.5633 | Equities rallied into the decision date with strong AI capex evidence (Broadcom AI revenue +221% y/y), but breadth is weak (positive asset share 40.6% over 5 sessions, RSP -0.90% vs SPY). Macro is stagflationary at the margin: ADP only 38k, GDP 1.5%, CPI 3.4% with energy +14.7% y/y, and long yields at 4.77%/5.25%. The window contains payrolls (Sep 4), PPI (Sep 10), CPI (Sep 11), plus an FOMC blackout, so macro-data risk dominates and duration/defensive trades have limited edge. Precious metals and mining pulled back hard after a very strong prior trend (silver prior active +11.8%, gold +8.3%) alongside a 2% gold rally reported in the session, which is the cleanest overreaction setup. Oil and Brazil are extended continuation trades with OPEC+ meeting Sep 6 and are less reliable. | Payrolls (Sep 4), PPI (Sep 10), and CPI (Sep 11) land inside the window and can reprice real rates, hitting precious metals and miners hard; Precious-metals pullback may extend if the dollar firms or yields rise further from 4.77% ten-year; High-beta reversal picks (silver 38.5% vol, XME 38.4% vol) can lose more than SPY on a broad risk-off week; Iran-Gulf conflict escalation or the OPEC+ Sep 6 meeting could drive an energy-led rotation away from the selected names; Biotech is event-sensitive to idiosyncratic clinical and financing news within a single week |
| anthropic-claude-fable-5-1 | anthropic | portfolio | METALS_MINING | 3 | 0.56 | SPY is near its 52-week high with low realized vol while breadth is narrow (RSP lagging by 0.9% over 5 sessions) and only 41% of assets were positive in the last week. Macro is stagflation-tinged: PCE inflation 3.7%, ISM prices above 70, Fed's Waller open to a hike, 10y at 4.77%, oil up 24% in a month amid an active Iran conflict. The scoring window contains payrolls, PPI, CPI, OPEC+ and Oracle/Adobe earnings with the Fed in blackout, so event risk is high. Recent weekly losers in semis, metals, silver and biotech sit on strong prior trends and look like temporary pullbacks; oil and Brazil are momentum spikes with thin fundamental support at the horizon. | Hot August payrolls or CPI/PPI prints raise hike odds, lifting real yields and hitting silver, miners and high-beta semis simultaneously; De-escalation in the Iran conflict or a dovish OPEC+ outcome unwinds the commodity and safe-haven bid; Oracle or Adobe results on Sept 10 disappoint and drag the broader tech/semiconductor complex; High-beta selections (SMH beta 2.9, XME 1.9) amplify any broad market drawdown from near-record highs |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 141.96 | 156.66 | 0.10355029585798814 | 1 |
| CYBERSECURITY | Cybersecurity | 94.59 | 100.05 | 0.05772280367903582 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 19.01 | 19.78 | 0.040504997369805285 | 3 |
| ETHEREUM_ETF | Ethereum ETF | 18.52 | 19.17 | 0.035097192224622153 | 4 |
| COMMUNICATIONS | Communication Services Sector | 112.03 | 115.07 | 0.02713558868160315 | 5 |
| SOFTWARE | Software | 104.57 | 106.64 | 0.019795352395524546 | 6 |
| YEN | Japanese Yen | 58.67 | 59.43 | 0.012953809442645348 | 7 |
| ENERGY | Energy Sector | 64.06 | 64.53 | 0.007336871682797286 | 8 |
| AGRICULTURE | Agriculture Commodities | 28.85 | 28.96 | 0.003812824956672456 | 9 |
| US_DOLLAR | US Dollar | 28.08 | 28.17 | 0.003205128205128416 | 10 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.45 | 91.5 | 0.0005467468562054822 | 11 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 12 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.58 | 84.42 | -0.0018917001655237575 | 13 |
| BRAZIL | Brazil Equities | 37.86 | 37.72 | -0.003697834125726329 | 14 |
| EURO | Euro | 107.15 | 106.55 | -0.005599626691554005 | 15 |
| JAPAN | Japan Equities | 98.28 | 97.58 | -0.007122507122507171 | 16 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.16 | 78.53 | -0.007958564931783707 | 17 |
| LARGE_VALUE | US Large-Cap Value | 257.63 | 255.37 | -0.008772270310134611 | 18 |
| MUNICIPAL_BONDS | Municipal Bonds | 104.03 | 103.11 | -0.008843602806882678 | 19 |
| TIPS | Treasury Inflation-Protected Securities | 106.97 | 105.82 | -0.010750677760119731 | 20 |
| BITCOIN_ETF | Bitcoin ETF | 45.23 | 44.74 | -0.010833517576829377 | 21 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.45 | 46.93 | -0.010958904109589107 | 22 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.48 | 104.3 | -0.01118695487296173 | 23 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.0 | 95.89 | -0.011443298969072146 | 24 |
| SP500 | S&P 500 | 770.19 | 760.88 | -0.012087926355834333 | 25 |
| LOW_VOL | US Low Volatility Equities | 74.74 | 73.82 | -0.012309339042012368 | 26 |
| BROAD_AI_TECH | Broad AI Technology | 64.32 | 63.47 | -0.013215174129353136 | 27 |
| DIVIDEND | US Dividend Equities | 34.8 | 34.34 | -0.013218390804597524 | 28 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.47 | 93.22 | -0.013231713771567732 | 29 |
| TOTAL_US_MARKET | Total US Stock Market | 379.73 | 374.68 | -0.0132989229189161 | 30 |
| NASDAQ100 | Nasdaq 100 | 718.96 | 709.18 | -0.01360298208523436 | 31 |
| UNITED_KINGDOM | United Kingdom Equities | 48.59 | 47.91 | -0.013994649104754231 | 32 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.25 | 90.93 | -0.01430894308943087 | 33 |
| REGIONAL_BANKS | Regional Banks | 75.27 | 74.11 | -0.015411186395642318 | 34 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.21 | 80.93 | -0.015569882009487723 | 35 |
| TECHNOLOGY | Technology Sector | 187.28 | 184.28 | -0.016018795386586904 | 36 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.715 | 91.22 | -0.01612468316885085 | 37 |
| MOMENTUM | US Momentum Equities | 304.86 | 299.7 | -0.01692580200747895 | 38 |
| LARGE_GROWTH | US Large-Cap Growth | 123.41 | 121.26 | -0.017421602787456414 | 39 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.91 | 112.85 | -0.01792707336176136 | 40 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 219.0 | 215.01 | -0.018219178082191867 | 41 |
| FINANCIALS | Financials Sector | 58.1 | 57.03 | -0.01841652323580034 | 42 |
| REAL_ESTATE | Real Estate Sector | 43.93 | 43.12 | -0.018438424766674344 | 43 |
| HEALTHCARE | Healthcare Sector | 171.45 | 167.75 | -0.02158063575386404 | 44 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.25 | 119.595 | -0.021717791411042908 | 45 |
| SMALL_VALUE | US Small-Cap Value | 224.62 | 219.45 | -0.023016650342801204 | 46 |
| MEXICO | Mexico Equities | 76.63 | 74.82 | -0.023619992170168413 | 47 |
| CANADA | Canada Equities | 62.04 | 60.5 | -0.024822695035460973 | 48 |
| MID_CAP | US Mid-Cap Stocks | 75.85 | 73.79 | -0.027158866183256247 | 49 |
| EUROPE | Europe Equities | 91.74 | 89.23 | -0.02735993023762795 | 50 |
| SMALL_CAP | US Small-Cap Stocks | 296.01 | 287.91 | -0.02736394040741852 | 51 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.76 | 71.72 | -0.02765726681127989 | 52 |
| CHINA | China Equities | 54.91 | 53.32 | -0.028956474230559026 | 53 |
| UTILITIES | Utilities Sector | 43.08 | 41.82 | -0.029247910863509752 | 54 |
| INDIA | India Equities | 49.91 | 48.43 | -0.02965337607693841 | 55 |
| EMERGING_MARKETS | Emerging Markets | 61.44 | 59.61 | -0.02978515625 | 56 |
| INDUSTRIALS | Industrials Sector | 175.27 | 169.93 | -0.030467279055171992 | 57 |
| GOLD | Gold | 83.39 | 80.54 | -0.03417675980333368 | 58 |
| MATERIALS | Materials Sector | 52.44 | 50.49 | -0.03718535469107542 | 59 |
| SOLAR | Solar Energy | 48.04 | 46.22 | -0.03788509575353871 | 60 |
| BIOTECH | Biotechnology | 163.81 | 157.6 | -0.03790977351810032 | 61 |
| AUSTRALIA | Australia Equities | 30.23 | 29.06 | -0.038703274892490924 | 62 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 225.61 | 216.77 | -0.03918266034306994 | 63 |
| COPPER | Copper | 39.95 | 38.26 | -0.042302878598247884 | 64 |
| SOUTH_AFRICA | South Africa Equities | 71.64 | 68.49 | -0.04396984924623126 | 65 |
| TAIWAN | Taiwan Equities | 112.18 | 107.21 | -0.044303797468354555 | 66 |
| SEMICONDUCTORS | Semiconductors | 567.01 | 541.5 | -0.0449903881765753 | 67 |
| SILVER | Silver | 59.82 | 56.84 | -0.04981611501170169 | 68 |
| SOUTH_KOREA | South Korea Equities | 188.87 | 176.22 | -0.06697728596389052 | 69 |
| METALS_MINING | Metals and Mining | 118.62 | 110.17 | -0.07123587927836794 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | METALS_MINING | 35.0 | -0.07123587927836794 | -0.02493255774742878 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SILVER | 35.0 | -0.04981611501170169 | -0.01743564025409559 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SEMICONDUCTORS | 30.0 | -0.0449903881765753 | -0.01349711645297259 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SILVER | 35.0 | -0.04981611501170169 | -0.01743564025409559 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | METALS_MINING | 35.0 | -0.07123587927836794 | -0.02493255774742878 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | BIOTECH | 30.0 | -0.03790977351810032 | -0.011372932055430095 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | CYBERSECURITY | 35.0 | 0.05772280367903582 | 0.020202981287662534 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SOLAR | 35.0 | -0.03788509575353871 | -0.013259783513738549 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | METALS_MINING | 30.0 | -0.07123587927836794 | -0.021370763783510383 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | METALS_MINING | 35.0 | -0.07123587927836794 | -0.02493255774742878 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | GOLD | 35.0 | -0.03417675980333368 | -0.011961865931166786 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SOFTWARE | 30.0 | 0.019795352395524546 | 0.005938605718657363 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 100.0 | -0.012087926355834333 | -0.012087926355834333 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | CYBERSECURITY | 35.0 | 0.05772280367903582 | 0.020202981287662534 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | METALS_MINING | 35.0 | -0.07123587927836794 | -0.02493255774742878 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | SILVER | 30.0 | -0.04981611501170169 | -0.014944834503510506 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | CYBERSECURITY | 35.0 | 0.05772280367903582 | 0.020202981287662534 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | METALS_MINING | 35.0 | -0.07123587927836794 | -0.02493255774742878 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | SILVER | 30.0 | -0.04981611501170169 | -0.014944834503510506 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SP500 | 1 | 0.5 | -0.012087926355834333 | -0.012087926355834333 | 0.0 | 0.11563822221382247 |  | False | False |
| google-gemini-3-1-pro | CYBERSECURITY | 3 | 0.58 | 0.05772280367903582 | -0.014427566009586397 | -0.002339639653752064 | 0.11797786186757453 |  | False | False |
| xai-grok-4-5 | CYBERSECURITY | 3 | 0.59 | 0.05772280367903582 | -0.019674410963276753 | -0.00758648460744242 | 0.12322470682126489 |  | False | False |
| xai-grok-4-6 | CYBERSECURITY | 3 | 0.5633 | 0.05772280367903582 | -0.019674410963276753 | -0.00758648460744242 | 0.12322470682126489 |  | False | False |
| openai-gpt-5-6-sol | METALS_MINING | 3 | 0.58 | -0.07123587927836794 | -0.030955817959938202 | -0.01886789160410387 | 0.13450611381792635 |  | False | False |
| anthropic-claude-opus-5 | SILVER | 3 | 0.5633 | -0.04981611501170169 | -0.05374113005695447 | -0.041653203701120134 | 0.1572914259149426 |  | False | False |
| anthropic-claude-fable-5-1 | METALS_MINING | 3 | 0.56 | -0.07123587927836794 | -0.05586531445449697 | -0.043777388098662634 | 0.1594156103124851 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | SILVER | -0.041653203701120134 | 0.23952500000000002 | -0.17389919090333006 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | ce9066cc1f09105feac18829716a3a2ddace4b60e820b2902c5308e830d121ca |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | f39ddff1eec2623dfa1a065f952f1b88871d8b316104960ab429760f5417a8b9 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 5b9b593af7e70b780683ea39a66aa5a1a6d0c37a7bdba393c36c0334037865bb |
| market_data/universe_decision_context.md | 220e86adb7c77a8ee6315e3ecf8c5516cd5b65934ac6376af4e6733ee34ee102 |
| market_data/universe_decision_context.json | 648ee501a7b7b5df3cb6aef9949acdaf98cd8035a88b3d13ef06d843dbe95795 |
| market_data/decision_context_source_history.json | e11640e5d23c252392c7d83e6f63a966268dd94e80d7ee0c5e6c47638831a673 |
| market_data/universe_quality_evidence.md | fade6d4e9ac0cf599867c1cab05958c95db0c87522c52ac380da272da1247875 |
| market_data/universe_quality_evidence.json | 3c751e5781185403f192fd026e2debbd2342069224a83509e3292def5476ffaa |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 6b083548605f0bf98ad3cb070ba05b582a0537526b80a4ebd136e07451434680 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | db548c5bfefd352499926e76601f5ba655ac50b64babedc29dafbfe34ddb518e | yes |
| Final briefing | research/final_briefing.md | model-facing | ce9066cc1f09105feac18829716a3a2ddace4b60e820b2902c5308e830d121ca | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
