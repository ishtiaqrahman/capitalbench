# CapitalBench Report: CB-2026-10-12-1M / official-20261012-1M-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20261012-1M-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-10-12-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-10-12
- Decision deadline: 2026-10-13T13:25:00Z
- Horizon: one month
- Entry date: 2026-10-12
- Exit date: 2026-11-12
- Entry rule: Use the October 12, 2026 official adjusted close supplied in prices/entry_prices.csv; CASH is fixed at 1.0.
- Exit rule: Use the November 12, 2026 official adjusted close supplied in prices/exit_prices.csv; CASH is fixed at 1.0.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-6-astra | openai | portfolio | SP500 | 2 | 0.57 | Cross-sectional outcomes are widely dispersed, although the aggregate dispersion statistic is missing and Ethereum is an extreme outlier. Strong spending and expansionary ISM readings coexist with weak payroll growth, elevated inflation and a tightening Fed. This supports selective earnings-linked reversals and energy exposure rather than indiscriminate dip buying. Recent-return and active-return columns cover different windows; neither is treated as a forecast. Quality scores measure price behavior, not verified balance-sheet quality. | Hot CPI or PCE releases and further Fed tightening could depress equities and duration assets simultaneously.; Bank earnings could reveal credit deterioration or funding pressure, invalidating the financials reversal thesis.; Faster restoration of Middle East production could reverse energy's fundamental support.; Korea's selloff could reflect unreported fundamental deterioration rather than temporary price pressure.; Ethereum's extreme supplied observations and holiday-dated bond inputs increase measurement and calibration uncertainty. |
| anthropic-claude-opus-5-5 | anthropic | portfolio | SP500 | 2 | 0.55 | Stagflationary backdrop: Fed hiked to 3.75-4.00% with more likely, PCE 3.4%, ISM prices 74, Brent ~$107, 10y 5.24%, weak payrolls. Only 32% of assets positive over 21 sessions; SPY narrow leadership (RSP -2.47% vs SPY over 21s). Dense catalyst calendar (CPI, FOMC, jobs, CPI again) raises dispersion. Reversal edges are modest; high-beta pullbacks carry rate and energy risk. | Hot Oct 14 CPI or hawkish Oct 28 FOMC triggering broad risk-off; Bank earnings disappointing on credit costs from lower-income consumer stress; Oil shock escalation hurting cyclicals; Semiconductor selloff spilling into mega-cap leadership |
| xai-grok-4-5 | xai | portfolio | SOUTH_KOREA | 3 | 0.59 | Elevated cross-asset dispersion with soft payrolls, sticky PCE/ISM prices, and hawkish Fed minutes favoring selective reversals in high-quality pullbacks over pure momentum; energy shock and holiday-delayed data add near-term uncertainty within the one-month window. | Further Fed hawkishness or hot CPI/PPI could extend equity drawdowns and pressure high-beta Korea; Energy price spike persistence (Brent ~106) may keep inflation elevated and delay rate relief; Geopolitical or semiconductor-specific shocks could invalidate Korea/Taiwan mean-reversion; Low positive-asset share on 21s window signals fragile breadth if risk-off resumes |
| xai-grok-4-3 | xai | portfolio | SOUTH_KOREA | 3 | 0.5833 | US data shows modest growth with payroll revisions and stable services; several international and commodity exposures display sharp recent pullbacks against prior strength, favoring reversal candidates over continuation. | US payroll revisions may signal slower growth; Energy price volatility from Middle East supply data; FOMC October meeting outcome uncertainty; High volume dislocation in bond proxies may reverse |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SOUTH_KOREA | 3 | 0.555 | Macro backdrop is stagflationary: payrolls 29k, core PCE 3.0%, ISM services prices at 74, Fed hiking to 3.75-4.00% with another hike likely, 10y at 5.24%, Brent above $106. Breadth is weak (31.88% of assets positive over 21 sessions, RSP lagging SPY by 2.47%) while mega-cap tech and energy hold the index up. Dispersion is high with a crypto outlier and a sharp Korea drawdown. Rate-sensitive assets face a hawkish FOMC on Oct 27-28 and two CPI prints inside the window, so duration and rate-sensitive reversals look premature; equity pullbacks with intact prior trends (Korea, financials into bank earnings) are the best reversal tests. | Hawkish Oct 27-28 FOMC or hot Oct 14 / Nov 10 CPI prints extend the rate-driven selloff and hit high-beta Korea and financials; Semiconductor weakness (SMH -6.77% over 5 sessions) deepens, dragging Korea further despite its prior trend; Bank earnings reveal credit deterioration from energy-cost-strained lower-income households; Brent above $106 and Middle East supply shut-ins escalate into a broader risk-off that favors the mega-cap-weighted index |
| xai-grok-4-6 | xai | portfolio | SP500 | 2 | 0.58 | SPY is near a 52-week high with mixed 10/12 session internals while 21-session breadth is weak; Fed minutes still point to another hike risk into the Oct 27-28 FOMC, and energy/inflation prints remain elevated. Shock-lane EM and commodity names show large recent active drawdowns against strong prior Korea strength, while cyber/ETH/Taiwan are continuation-style but stretched or high-vol. One-month edge versus SPY is limited outside a Korea mean-reversion test. | Another Fed hike path after the Oct 27-28 FOMC if CPI/PCE stay hot.; Korea/EM beta and 50%+ vol can extend the shock rather than reverse.; Brent near $106 and ISM services prices at 74 keep inflation and rate-sensitive assets under pressure.; Bank earnings from Oct 13 can reprice financials and risk appetite independently of the Korea bounce. |
| google-gemini-3-1-pro | google | portfolio | SOUTH_KOREA | 3 | 0.58 | The market is digesting mixed economic signals, with solid services activity but downward payroll revisions and elevated inflation concerns noted in Fed minutes. The upcoming earnings season and CPI data will be key drivers. | Continued strength in the US dollar could negatively impact international equities and commodities.; Higher-than-expected inflation data could lead to a more hawkish Fed, pressuring risk assets. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| INDIA | India Equities | 46.36 | 51.55 | 0.11194995685936138 | 1 |
| HEALTHCARE | Healthcare Sector | 171.99 | 187.83 | 0.09209837781266361 | 2 |
| DIVIDEND | US Dividend Equities | 33.26 | 35.93 | 0.08027660853878538 | 3 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.41 | 91.06 | 0.07878213481814966 | 4 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.27 | 120.46 | 0.07294914046495049 | 5 |
| LOW_VOL | US Low Volatility Equities | 72.79 | 78.02 | 0.07185052891880739 | 6 |
| MEXICO | Mexico Equities | 73.23999786376953 | 77.62000274658203 | 0.0598034545407764 | 7 |
| MATERIALS | Materials Sector | 49.44 | 52.34 | 0.058656957928802766 | 8 |
| REAL_ESTATE | Real Estate Sector | 41.92 | 44.36 | 0.05820610687022887 | 9 |
| FINANCIALS | Financials Sector | 55.05 | 58.21 | 0.05740236148955491 | 10 |
| UTILITIES | Utilities Sector | 41.63 | 43.81 | 0.05236608215229399 | 11 |
| REGIONAL_BANKS | Regional Banks | 69.56 | 72.52 | 0.04255319148936154 | 12 |
| EUROPE | Europe Equities | 85.82 | 88.91 | 0.03600559310184104 | 13 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.19 | 220.72 | 0.03532060603217779 | 14 |
| LARGE_VALUE | US Large-Cap Value | 254.65 | 262.73 | 0.031729825250343735 | 15 |
| MUNICIPAL_BONDS | Municipal Bonds | 101.16000366210938 | 103.94999694824219 | 0.027580003807155196 | 16 |
| SOUTH_AFRICA | South Africa Equities | 63.77000045776367 | 65.36000061035156 | 0.0249333564556109 | 17 |
| UNITED_KINGDOM | United Kingdom Equities | 46.7 | 47.76 | 0.022698072805139136 | 18 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 78.05 | 79.72 | 0.021396540679051945 | 19 |
| AUSTRALIA | Australia Equities | 28.670000076293945 | 29.209999084472656 | 0.018834984539299438 | 20 |
| CANADA | Canada Equities | 59.45 | 60.13 | 0.011438183347350694 | 21 |
| US_DOLLAR | US Dollar | 29.1299991607666 | 29.420000076293945 | 0.009955404184080141 | 22 |
| MID_CAP | US Mid-Cap Stocks | 73.16 | 73.85 | 0.009431383269546068 | 23 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 89.43 | 90.21 | 0.008721905400872032 | 24 |
| SMALL_VALUE | US Small-Cap Value | 211.09 | 212.89 | 0.008527168506324179 | 25 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.970001220703125 | 47.310001373291016 | 0.007238666036866626 | 26 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 89.83000183105469 | 90.44999694824219 | 0.0069018713631281425 | 27 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 94.66 | 95.22 | 0.005915909571096556 | 28 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 102.58 | 103.05 | 0.004581789822577509 | 29 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 91.08000183105469 | 91.33999633789062 | 0.0028545729206088666 | 30 |
| TIPS | Treasury Inflation-Protected Securities | 104.5 | 104.77 | 0.0025837320574162437 | 31 |
| SMALL_CAP | US Small-Cap Stocks | 277.9 | 278.44 | 0.0019431450161928598 | 32 |
| INDUSTRIALS | Industrials Sector | 169.15 | 169.44 | 0.0017144546260714488 | 33 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 34 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.5 | 91.5 | 0.0 | 34 |
| BIOTECH | Biotechnology | 151.4 | 151.2 | -0.0013210039630120463 | 36 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 77.29 | 76.98 | -0.004010868158882186 | 37 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.95 | 69.43 | -0.00743388134381695 | 38 |
| YEN | Japanese Yen | 57.779998779296875 | 57.2599983215332 | -0.008999661972128536 | 39 |
| EURO | Euro | 102.98999786376953 | 102.04000091552734 | -0.009224167083669577 | 40 |
| TOTAL_US_MARKET | Total US Stock Market | 381.57 | 372.62 | -0.02345572241004268 | 41 |
| ENERGY | Energy Sector | 66.01 | 64.33 | -0.02545068928950167 | 42 |
| SOLAR | Solar Energy | 43.48 | 42.33 | -0.02644894204231829 | 43 |
| SP500 | S&P 500 | 778.1 | 757.12 | -0.0269631152808123 | 44 |
| OIL | Crude Oil | 151.02999877929688 | 146.07000732421875 | -0.03284110107374272 | 45 |
| COMMUNICATIONS | Communication Services Sector | 111.45 | 107.56 | -0.03490354419021979 | 46 |
| CHINA | China Equities | 52.15 | 49.75 | -0.0460210930009588 | 47 |
| EMERGING_MARKETS | Emerging Markets | 59.73 | 56.43 | -0.05524861878453036 | 48 |
| JAPAN | Japan Equities | 97.32 | 91.47 | -0.060110974106041826 | 49 |
| GOLD | Gold | 78.34 | 72.79 | -0.07084503446515189 | 50 |
| BROAD_COMMODITIES | Broad Commodities | 19.86 | 18.41 | -0.07301107754279956 | 51 |
| AGRICULTURE | Agriculture Commodities | 28.440000534057617 | 26.299999237060547 | -0.07524617639983389 | 52 |
| NASDAQ100 | Nasdaq 100 | 746.04 | 688.17 | -0.07756956731542541 | 53 |
| COPPER | Copper | 40.630001068115234 | 37.2400016784668 | -0.0834358675985557 | 54 |
| LARGE_GROWTH | US Large-Cap Growth | 127.13 | 116.19 | -0.08605364587430187 | 55 |
| SOFTWARE | Software | 111.28 | 101.45 | -0.08833572969086989 | 56 |
| METALS_MINING | Metals and Mining | 104.85 | 95.25 | -0.09155937052932761 | 57 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 121.6 | 110.27 | -0.0931743421052631 | 58 |
| BROAD_AI_TECH | Broad AI Technology | 65.92 | 59.49 | -0.09754247572815533 | 59 |
| CYBERSECURITY | Cybersecurity | 107.8 | 96.46 | -0.10519480519480517 | 60 |
| TECHNOLOGY | Technology Sector | 196.36 | 173.77 | -0.1150437971073538 | 61 |
| BITCOIN_ETF | Bitcoin ETF | 46.86000061035156 | 40.36000061035156 | -0.1387110523973003 | 62 |
| SOUTH_KOREA | South Korea Equities | 170.11000061035156 | 145.3800048828125 | -0.14537649543711884 | 63 |
| TAIWAN | Taiwan Equities | 114.2699966430664 | 97.25 | -0.14894545500189382 | 64 |
| SEMICONDUCTORS | Semiconductors | 590.99 | 501.73 | -0.1510347044789252 | 65 |
| SILVER | Silver | 54.349998474121094 | 45.119998931884766 | -0.16982520333705653 | 66 |
| ETHEREUM_ETF | Ethereum ETF | 56.95000076293945 | 45.540000915527344 | -0.20035117988685325 | 67 |
| BRAZIL | Brazil Equities | 43.540000915527344 | 31.780000686645508 | -0.27009646259993425 | 68 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 206.03 | 71.73 | -0.6518468184245012 | 69 |
| MOMENTUM | US Momentum Equities | 315.09 | 69.36 | -0.779872417404551 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | SOUTH_KOREA | 35.0 | -0.14537649543711884 | -0.05088177340299159 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | FINANCIALS | 35.0 | 0.05740236148955491 | 0.020090826521344217 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 30.0 | -0.0269631152808123 | -0.008088934584243689 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5-5 | FINANCIALS | 35.0 | 0.05740236148955491 | 0.020090826521344217 | V3 selected model rank 1: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | SP500 | 65.0 | -0.0269631152808123 | -0.017526024932527997 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | SOUTH_KOREA | 35.0 | -0.14537649543711884 | -0.05088177340299159 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SOUTH_AFRICA | 35.0 | 0.0249333564556109 | 0.008726674759463815 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | METALS_MINING | 30.0 | -0.09155937052932761 | -0.027467811158798282 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | FINANCIALS | 35.0 | 0.05740236148955491 | 0.020090826521344217 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 65.0 | -0.0269631152808123 | -0.017526024932527997 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | SOUTH_KOREA | 35.0 | -0.14537649543711884 | -0.05088177340299159 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | SMALL_VALUE | 35.0 | 0.008527168506324179 | 0.0029845089772134624 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | FINANCIALS | 30.0 | 0.05740236148955491 | 0.017220708446866472 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-5 | SOUTH_KOREA | 35.0 | -0.14537649543711884 | -0.05088177340299159 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | SMALL_VALUE | 35.0 | 0.008527168506324179 | 0.0029845089772134624 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | FINANCIALS | 30.0 | 0.05740236148955491 | 0.017220708446866472 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | SOUTH_KOREA | 35.0 | -0.14537649543711884 | -0.05088177340299159 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 65.0 | -0.0269631152808123 | -0.017526024932527997 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-6-astra | SP500 | 2 | 0.57 | -0.0269631152808123 | 0.00256480158881622 | 0.02952791686962852 | 0.10938515527054515 |  | True | True |
| anthropic-claude-opus-5-5 | SP500 | 2 | 0.55 | -0.0269631152808123 | 0.00256480158881622 | 0.02952791686962852 | 0.10938515527054515 |  | True | True |
| xai-grok-4-5 | SOUTH_KOREA | 3 | 0.59 | -0.14537649543711884 | -0.030676555978911658 | -0.003713440698099358 | 0.14262651283827305 |  | False | False |
| xai-grok-4-3 | SOUTH_KOREA | 3 | 0.5833 | -0.14537649543711884 | -0.030676555978911658 | -0.003713440698099358 | 0.14262651283827305 |  | False | False |
| anthropic-claude-fable-5-1 | SOUTH_KOREA | 3 | 0.555 | -0.14537649543711884 | -0.03887988146589106 | -0.01191676618507876 | 0.15082983832525243 |  | False | False |
| xai-grok-4-6 | SP500 | 2 | 0.58 | -0.0269631152808123 | -0.06840779833551959 | -0.04144468305470729 | 0.18035775519488095 |  | False | False |
| google-gemini-3-1-pro | SOUTH_KOREA | 3 | 0.58 | -0.14537649543711884 | -0.06962290980232605 | -0.04265979452151375 | 0.18157286666168743 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 3877de5555e6db243ed48229652e49f15ce48e4bcfc8e24245fe60c3e288f423 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | 27108dfd49371b92822aee082bab71d1ca67ccd4887b80a20e1da8e3d09836ee |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 90465f3df7582b9180ea73f18fe493f23cb2f53e311535bde69299b9ad339eef |
| market_data/universe_decision_context.md | d46aae5a4e41bd9ccca808388ffda8d104d37cfe57b0f7f160b345e8baa7b9b1 |
| market_data/universe_decision_context.json | 0f1ae37871a679da3011577b246b7bb9b250971457d68575146706f5eee29e6a |
| market_data/decision_context_source_history.json | 769354e709c3c1dfb0c782f8f386cccdf743ab85f16ac4d934d824d922f2cce1 |
| market_data/universe_quality_evidence.md | e1c3706fb3b4d43dceb7ea97623c423c96507985898ca82dcec89b088b615d09 |
| market_data/universe_quality_evidence.json | 302977828f4f10febb8d2f876e464a5c7fa2050b41d2c4ffbc43b3e34a9428a8 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | f0c5088cec915b6c5186b2a47c03024a5fe497ab2abd08299775bfe972281484 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | d6c789a95c6acba8a5ed2ff1b78246516e70e070de8e63793d947d021fc8b5a8 | yes |
| Final briefing | research/final_briefing.md | model-facing | 3877de5555e6db243ed48229652e49f15ce48e4bcfc8e24245fe60c3e288f423 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
