# CapitalBench Report: CB-2026-09-03-1M / official-v3-20260903-monthly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260903-monthly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-03-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-09-03
- Decision deadline: 2026-09-04T13:25:00Z
- Horizon: one month
- Entry date: 2026-09-04
- Exit date: 2026-10-05
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SEMICONDUCTORS | 3 | 0.555 | SPY is near its 52-week high with low realized vol, but breadth is weak (RSP lagging, 5-session positive share 41%), oil is up 24% over 21 sessions on active Iran conflict, headline PCE inflation is 3.7% and Waller has signaled a possible hike. The window contains payrolls, CPI, and a September FOMC with real two-sided rate risk. Recent laggards with strong prior trends (semis, cybersecurity, momentum) plus Broadcom's AI print give a fair reversal setup, while energy-driven inflation hurts duration-sensitive and consumer names. | Hot CPI on Sep 11 or a hawkish FOMC on Sep 16 triggers a high-beta growth selloff, hurting semis, cyber, and momentum far more than SPY; Escalation in the Iran-Gulf conflict pushes oil above $100 and drives a broad risk-off with correlated drawdowns across all equity candidates; Weak Sep 4 payrolls after ADP 38k shifts market to growth-scare mode, favoring defensives not represented in top ranks; Semiconductor volatility of 53% and beta 2.4 can produce large idiosyncratic losses even with positive AI fundamentals |
| openai-gpt-5-6-sol | openai | portfolio | CYBERSECURITY | 3 | 0.5733 | Wide cross-sectional moves, elevated event risk, and sharp factor pullbacks favor selective reversals rather than broad continuation. Strong activity data is offset by sticky prices, weak hiring, high yields, and geopolitical uncertainty. | A hot inflation release or hawkish September FOMC outcome could pressure high-beta technology and bank exposures.; A weak employment report could deepen credit concerns and hurt regional banks and cyclical equities.; AI-related earnings disappointment could turn semiconductor and cybersecurity pullbacks into sustained de-rating.; Escalating Middle East conflict could lift energy costs and disrupt the broader risk-on rebound. |
| anthropic-claude-opus-5 | anthropic | portfolio | CYBERSECURITY | 3 | 0.5767 | Late-cycle mixed tape: modest growth (Beige Book, 1.5% Q2 GDP), softening labor (ADP 38k, Challenger up 58%), but sticky inflation (CPI 3.4%, PCE 3.7%, energy +14.7% y/y) and a hawkish-leaning Waller ahead of the Sept 15-16 FOMC. Oil near $95 on active Iran conflict keeps inflation risk elevated and caps duration and rate-sensitive plays. Mega-cap tech firm on Sept 3 with Broadcom's blowout AI print supporting semis/AI fundamentals, while quality pullbacks in cybersecurity and regional banks look like flow-driven rather than fundamental damage. Breadth is soft (RSP lagging SPY, 40% positive over 5 sessions), so idiosyncratic pullback reversals are preferred over broad beta. | Sept 15-16 FOMC with hawkish-leaning Waller commentary could trigger a high-beta unwind hitting SMH and CIBR hardest; Sticky inflation (CPI 3.4%, energy +14.7% y/y) plus $95 Brent on active Iran conflict could push long yields higher and compress equity multiples; Sept 4 and Oct 2 payrolls plus Sept 11 CPI land inside the window and could confirm labor deterioration, hurting regional banks via credit concerns; Semiconductor 53% annualized vol means the position outcome is dominated by variance rather than the identified edge; Continued narrow breadth (RSP trailing SPY) can leave equal-weight-like pullback plays lagging a mega-cap-led index |
| xai-grok-4-6 | xai | portfolio | CYBERSECURITY | 3 | 0.555 | SPY is near a 52-week high with modest 5-session gains while many cyclicals, tech, and defense names show larger recent drawdowns; incoming payrolls, CPI, and the mid-September FOMC create two-way event risk, so one-month outcomes look mixed rather than a clean continuation or reversal regime. | Unknown September 4 Employment Situation and September 11 CPI can reprice rate-sensitive growth and small/mid cyclicals immediately.; September 15–16 FOMC and Waller’s data-dependent hike/hold comments can reverse high-beta tech, semis, and crypto.; Active Iran/Hormuz conflict and oil strength can keep energy and defense volatile while pressuring discretionary and industrials.; Broadcom-style AI strength may not lift SMH/XLK if volume remains weak (XLK volume z -1.39). |
| xai-grok-4-5 | xai | portfolio | CYBERSECURITY | 3 | 0.59 | Softening labor signals, elevated services prices, and pending FOMC create mixed one-month setup; quality pullbacks in prior-strong tech/defense/industrials offer selective reversal edges while mega-cap resilience and crypto momentum limit broad risk-on continuation. | Hot August employment or CPI could shift Waller/FOMC toward hike risk and pressure equities; Active Iran-related conflict and energy price uncertainty may reverse defense/industrial bounce; High-vol semis/crypto/Taiwan beta could amplify any growth scare into larger drawdowns; Services PMI prices at 72.6 keep sticky inflation risk alive into September data |
| google-gemini-3-1-pro | google | portfolio | AEROSPACE_DEFENSE | 3 | 0.58 | The market is showing mixed signals with some sectors experiencing pullbacks while others continue to show strength. The upcoming FOMC meeting and employment data will be key drivers. | Upcoming FOMC meeting could introduce volatility.; Employment data release may shift market sentiment. |
| xai-grok-4-3 | xai | portfolio | REGIONAL_BANKS | 3 | 0.6 | Mixed signals with modest equity gains, stable macro data, and sector-specific pullbacks amid geopolitical and policy uncertainty; reversal candidates in quality names show potential edge over benchmark. | FOMC policy surprise on September 16; Geopolitical escalation in Middle East; August employment data release impact; Commodity price volatility |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BRAZIL | Brazil Equities | 37.86 | 42.97999954223633 | 0.1352350645070346 | 1 |
| CYBERSECURITY | Cybersecurity | 94.59 | 106.01 | 0.12073157839095039 | 2 |
| SEMICONDUCTORS | Semiconductors | 567.01 | 633.9 | 0.11796970071074586 | 3 |
| ETHEREUM_ETF | Ethereum ETF | 18.52 | 20.43000030517578 | 0.10313176593821716 | 4 |
| BITCOIN_ETF | Bitcoin ETF | 45.23 | 48.560001373291016 | 0.07362373144574441 | 5 |
| TECHNOLOGY | Technology Sector | 187.28 | 200.93 | 0.07288551900897056 | 6 |
| MOMENTUM | US Momentum Equities | 304.86 | 323.14 | 0.05996194974742486 | 7 |
| TAIWAN | Taiwan Equities | 112.18 | 118.0 | 0.051880905687288204 | 8 |
| NASDAQ100 | Nasdaq 100 | 718.96 | 756.2 | 0.051797040169133224 | 9 |
| SOFTWARE | Software | 104.57 | 109.72 | 0.04924930668451766 | 10 |
| LARGE_GROWTH | US Large-Cap Growth | 123.41 | 128.35 | 0.04002917105583004 | 11 |
| BROAD_AI_TECH | Broad AI Technology | 64.32 | 66.85 | 0.03933457711442778 | 12 |
| US_DOLLAR | US Dollar | 28.08 | 28.989999771118164 | 0.03240739925634495 | 13 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.25 | 125.84 | 0.029366053169734174 | 14 |
| OIL | Crude Oil | 141.96 | 143.99000549316406 | 0.01429984145649521 | 15 |
| SOUTH_KOREA | South Korea Equities | 188.87 | 191.4600067138672 | 0.013713171567041771 | 16 |
| BROAD_COMMODITIES | Broad Commodities | 19.01 | 19.25 | 0.012624934245134112 | 17 |
| JAPAN | Japan Equities | 98.28 | 99.3 | 0.010378510378510342 | 18 |
| SP500 | S&P 500 | 770.19 | 774.83 | 0.0060244874641322 | 19 |
| TOTAL_US_MARKET | Total US Stock Market | 379.73 | 380.6 | 0.002291101572169607 | 20 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 21 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.45 | 91.44 | -0.00010934937124118527 | 22 |
| COPPER | Copper | 39.95 | 39.86000061035156 | -0.0022528007421386276 | 23 |
| COMMUNICATIONS | Communication Services Sector | 112.03 | 111.61 | -0.003748995804695232 | 24 |
| ENERGY | Energy Sector | 64.06 | 63.45 | -0.00952232282235399 | 25 |
| YEN | Japanese Yen | 58.67 | 58.02000045776367 | -0.01107890816833701 | 26 |
| EMERGING_MARKETS | Emerging Markets | 61.44 | 60.61 | -0.01350911458333326 | 27 |
| AGRICULTURE | Agriculture Commodities | 28.85 | 28.459999084472656 | -0.013518229307706964 | 28 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.45 | 46.790000915527344 | -0.013909358998370092 | 29 |
| HEALTHCARE | Healthcare Sector | 171.45 | 167.37 | -0.023797025371828484 | 30 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.16 | 76.98 | -0.027539161192521422 | 31 |
| TIPS | Treasury Inflation-Protected Securities | 106.97 | 103.98 | -0.027951762176311012 | 32 |
| MUNICIPAL_BONDS | Municipal Bonds | 104.03 | 101.12000274658203 | -0.027972673780812918 | 33 |
| LARGE_VALUE | US Large-Cap Value | 257.63 | 250.36 | -0.028218763342778286 | 34 |
| MID_CAP | US Mid-Cap Stocks | 75.85 | 73.68 | -0.028609096901779707 | 35 |
| INDUSTRIALS | Industrials Sector | 175.27 | 170.1 | -0.02949734695041939 | 36 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.0 | 94.13 | -0.029587628865979432 | 37 |
| EURO | Euro | 107.15 | 103.58999633789062 | -0.03322448588062887 | 38 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.48 | 101.83 | -0.03460371634433068 | 39 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.76 | 71.13 | -0.03565618221258149 | 40 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 219.0 | 211.12 | -0.035981735159817285 | 41 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.25 | 88.92 | -0.03609756097560979 | 42 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.91 | 110.42 | -0.03907405795840213 | 43 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.715 | 89.08999633789062 | -0.039098351530058584 | 44 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.58 | 81.04 | -0.041853866162213205 | 45 |
| SMALL_CAP | US Small-Cap Stocks | 296.01 | 283.38 | -0.042667477450086144 | 46 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.47 | 90.33999633789062 | -0.04371762106604604 | 47 |
| BIOTECH | Biotechnology | 163.81 | 156.19 | -0.0465173066357365 | 48 |
| CHINA | China Equities | 54.91 | 52.28 | -0.047896558004006495 | 49 |
| LOW_VOL | US Low Volatility Equities | 74.74 | 71.09 | -0.04883596467754869 | 50 |
| UNITED_KINGDOM | United Kingdom Equities | 48.59 | 46.19 | -0.04939287919324975 | 51 |
| SMALL_VALUE | US Small-Cap Value | 224.62 | 213.27 | -0.050529783634582826 | 52 |
| CANADA | Canada Equities | 62.04 | 58.78 | -0.05254674403610571 | 53 |
| MATERIALS | Materials Sector | 52.44 | 49.5 | -0.05606407322654461 | 54 |
| EUROPE | Europe Equities | 91.74 | 86.28 | -0.059516023544800456 | 55 |
| AUSTRALIA | Australia Equities | 30.23 | 28.43000030517578 | -0.05954348973947132 | 56 |
| DIVIDEND | US Dividend Equities | 34.8 | 32.72 | -0.05977011494252871 | 57 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.21 | 77.11 | -0.062036248631553326 | 58 |
| MEXICO | Mexico Equities | 76.63 | 71.87000274658203 | -0.062116628649588446 | 59 |
| REGIONAL_BANKS | Regional Banks | 75.27 | 70.39 | -0.06483326690580571 | 60 |
| GOLD | Gold | 83.39 | 77.82 | -0.0667945796858137 | 61 |
| INDIA | India Equities | 49.91 | 46.57 | -0.06692045682227998 | 62 |
| UTILITIES | Utilities Sector | 43.08 | 39.97 | -0.07219127205199627 | 63 |
| FINANCIALS | Financials Sector | 58.1 | 53.88 | -0.07263339070567987 | 64 |
| REAL_ESTATE | Real Estate Sector | 43.93 | 40.67 | -0.07420896881402228 | 65 |
| SILVER | Silver | 59.82 | 55.130001068115234 | -0.07840185442803016 | 66 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 225.61 | 206.98 | -0.08257612694472771 | 67 |
| SOLAR | Solar Energy | 48.04 | 43.67 | -0.0909658617818484 | 68 |
| METALS_MINING | Metals and Mining | 118.62 | 107.76 | -0.09155285786545275 | 69 |
| SOUTH_AFRICA | South Africa Equities | 71.64 | 63.16999816894531 | -0.11823006464342112 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | SEMICONDUCTORS | 35.0 | 0.11796970071074586 | 0.041289395248761046 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | CYBERSECURITY | 35.0 | 0.12073157839095039 | 0.042256052436832635 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 30.0 | 0.0060244874641322 | 0.0018073462392396598 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5 | CYBERSECURITY | 35.0 | 0.12073157839095039 | 0.042256052436832635 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | REGIONAL_BANKS | 35.0 | -0.06483326690580571 | -0.022691643417031997 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SEMICONDUCTORS | 30.0 | 0.11796970071074586 | 0.035390910213223756 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 35.0 | -0.08257612694472771 | -0.028901644430654697 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | INDUSTRIALS | 35.0 | -0.02949734695041939 | -0.010324071432646785 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | MOMENTUM | 30.0 | 0.05996194974742486 | 0.017988584924227457 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | CYBERSECURITY | 35.0 | 0.12073157839095039 | 0.042256052436832635 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 35.0 | 0.11796970071074586 | 0.041289395248761046 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | REGIONAL_BANKS | 30.0 | -0.06483326690580571 | -0.019449980071741712 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-3 | REGIONAL_BANKS | 35.0 | -0.06483326690580571 | -0.022691643417031997 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | SMALL_CAP | 35.0 | -0.042667477450086144 | -0.01493361710753015 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 30.0 | 0.0060244874641322 | 0.0018073462392396598 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | CYBERSECURITY | 35.0 | 0.12073157839095039 | 0.042256052436832635 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | REGIONAL_BANKS | 35.0 | -0.06483326690580571 | -0.022691643417031997 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | INDUSTRIALS | 30.0 | -0.02949734695041939 | -0.008849204085125817 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | CYBERSECURITY | 35.0 | 0.12073157839095039 | 0.042256052436832635 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | AEROSPACE_DEFENSE | 35.0 | -0.08257612694472771 | -0.028901644430654697 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 30.0 | 0.0060244874641322 | 0.0018073462392396598 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | SEMICONDUCTORS | 3 | 0.555 | 0.11796970071074586 | 0.08535279392483335 | 0.07932830646070115 | 0.04988227058220125 |  | True | True |
| openai-gpt-5-6-sol | CYBERSECURITY | 3 | 0.5733 | 0.12073157839095039 | 0.06409546761385197 | 0.05807098014971977 | 0.07113959689318262 |  | True | True |
| anthropic-claude-opus-5 | CYBERSECURITY | 3 | 0.5767 | 0.12073157839095039 | 0.054955319233024394 | 0.048930831768892194 | 0.0802797452740102 |  | True | True |
| xai-grok-4-6 | CYBERSECURITY | 3 | 0.555 | 0.12073157839095039 | 0.015161754245417599 | 0.009137266781285399 | 0.120073310261617 |  | True | True |
| xai-grok-4-5 | CYBERSECURITY | 3 | 0.59 | 0.12073157839095039 | 0.010715204934674821 | 0.004690717470542621 | 0.12451985957235978 |  | True | True |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 3 | 0.58 | -0.08257612694472771 | -0.021237130939074023 | -0.027261618403206223 | 0.15647219544610863 |  | False | False |
| xai-grok-4-3 | REGIONAL_BANKS | 3 | 0.6 | -0.06483326690580571 | -0.03581791428532249 | -0.04184240174945469 | 0.1710529787923571 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | CYBERSECURITY | 0.048930831768892194 | 0.25279 | 0.19356316218557773 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | ce9066cc1f09105feac18829716a3a2ddace4b60e820b2902c5308e830d121ca |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | fbe73bfb0c9d5cf7313dcccddf5e3b8ee4a369c9a9a756651755efcb1e3ed898 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 33c1afbafc4dad8a75f6947a8fa82082e5816bf5244b2fa440e88f36c5f1bcd4 |
| market_data/universe_decision_context.md | 0dd469eeff7d429e85b8dbef4a02ccf7787e27dd3a14a8026144f7b2c01b64c0 |
| market_data/universe_decision_context.json | 683d879b3b929513905f2a57fe604e65128f0d960720b0b3a8dbab49554eece8 |
| market_data/decision_context_source_history.json | 4e522074c782f8fcee67dc03b5962be367f504020ed8ef5e31f232924b07b3ac |
| market_data/universe_quality_evidence.md | 86177ca5d1b8720d98a7d36cd66befeb8a08e6d7231b797e3964d3a0f4c574eb |
| market_data/universe_quality_evidence.json | 202be613e234c1f4c3c2fccf9fdc4fce1abaa8f77e09056219730b456365e262 |

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
