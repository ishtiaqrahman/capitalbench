# CapitalBench Report: CB-2026-10-12-1W / official-20261012-1W-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20261012-1W-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-10-12-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-10-12
- Decision deadline: 2026-10-13T13:25:00Z
- Horizon: one week
- Entry date: 2026-10-12
- Exit date: 2026-10-19
- Entry rule: Use the October 12, 2026 official adjusted close supplied in prices/entry_prices.csv; CASH is fixed at 1.0.
- Exit rule: Use the October 19, 2026 official adjusted close supplied in prices/exit_prices.csv; CASH is fixed at 1.0.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 2 | 0.55 | Commodity and value exposures show relative strength while growth and international equities exhibit pullbacks amid mixed macro data and elevated dispersion. | Macro data releases within window; Commodity price volatility; Equity sector rotation risk |
| anthropic-claude-opus-5-5 | anthropic | portfolio | SP500 | 2 | 0.55 | The Fed is hiking into 3.4% PCE inflation, Brent is above $106, and ISM prices are at 74. A rotation out of tech and semis into defensives and energy happened this week. CPI, PPI and retail sales land inside the window and could swing rate-sensitive growth either way. Dispersion is high, but the macro backdrop does not cleanly support either reversal or continuation. | A hot CPI or PPI pushes yields higher and extends the growth and semiconductor selloff; The oil shock escalates and further rotation into energy and defensives follows; Bank earnings disappoint and broad risk-off hits high-beta names |
| openai-gpt-6-astra | openai | portfolio | SEMICONDUCTORS | 3 | 0.555 | Energy has independent supply-side support, while selected technology pullbacks offer modest reversal potential rather than a confirmed renewed uptrend. Weak payrolls and wage growth compete with elevated services prices and a tightening Fed ahead of CPI and PPI. Reported dispersion is high, but Ethereum's anomalous statistics inflate its apparent magnitude. Quality scores are price-derived evidence, not independent confirmation of business fundamentals. | Hot October 14 CPI or October 15 PPI could reinforce further Fed tightening and extend technology underperformance.; Faster restoration of Middle East production or bearish petroleum data could reverse oil's supply-supported rally.; Weak retail sales or disappointing bank earnings could turn rotation into broader risk reduction.; Ethereum's anomalous inputs and differing reported return windows reduce confidence in mechanical cross-sectional comparisons. |
| google-gemini-3-1-pro | google | portfolio | SOUTH_KOREA | 3 | 0.58 | The market is experiencing a pullback in technology and growth sectors, while energy and defensive sectors show strength. High dispersion suggests opportunities in mean reversion for oversold quality assets. | Continued selling pressure in technology and growth sectors could lead to further underperformance.; Macroeconomic data releases, such as CPI and retail sales, could negatively impact market sentiment and trigger broader market declines. |
| xai-grok-4-5 | xai | portfolio | SOUTH_KOREA | 3 | 0.5667 | High cross-sectional dispersion with tech/semiconductor/Korea shock pullbacks against oil strength, elevated inflation prints, and upcoming CPI/PPI/bank earnings; mixed reversal vs continuation signals into a data-heavy week. | September CPI/PPI and bank earnings can extend growth/tech selloff; oil/energy shock persistence raises inflation and rate-path risk; high-vol EM/semiconductor names can gap further on geopolitics or USD strength; Fed minutes already signal another hike possible, limiting duration/risk appetite |
| xai-grok-4-6 | xai | portfolio | SOUTH_KOREA | 3 | 0.5633 | Five-session active-return dispersion is elevated while SPY is nearly unchanged and near a 52-week high. Growth/Asia/semis sold off sharply against still-positive prior relative trends, while energy, REITs, and some EM names rose. CPI/PPI and bank earnings land inside the week against a hiking Fed and elevated oil, so mean-reversion in the shock names is possible but not a clean continuation tape. | September CPI and PPI on Oct 14-15 can extend the growth/Asia selloff if inflation stays sticky.; Fed minutes already pointed to another hike by year-end, limiting duration-sensitive and high-beta rebounds.; Oil near $106 and ISM services prices at 74 keep energy-shock risk on EM exporters and global cyclicals.; Bank earnings start Oct 13 and can dominate the tape versus country/sector mean reversion. |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SEMICONDUCTORS | 3 | 0.5567 | Macro backdrop is stagflationary: weak payrolls (29k), hot ISM services prices (74.0), 10y at 5.24% with the Fed still hiking, Brent above $106. Last week showed sharp rotation out of semis/AI leaders and Korea into defensives and energy, with SPY roughly flat. Active return dispersion of 21.66% is elevated. The week contains CPI, PPI, retail sales and the start of bank earnings, which are binary for rate-sensitive growth. High-beta semi and Korea pullbacks against strong prior relative trends look like position-driven overreactions rather than new fundamental breaks, but catalyst risk keeps conviction moderate. | Hot September CPI/PPI on Oct 14-15 pushing yields higher and extending the high-beta tech/semi drawdown; The Korea and semiconductor selloff reflecting an unreported fundamental or geopolitical event that persists; Bank earnings disappointments from Oct 13 triggering broad risk-off that hits beta 2+ holdings hardest; Energy shock escalation (Brent >$106) worsening stagflation and favoring defensives over growth |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 151.02999877929688 | 160.80999755859375 | 0.06475533906074227 | 1 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.41 | 87.21 | 0.03317142518658933 | 2 |
| MATERIALS | Materials Sector | 49.44 | 50.95 | 0.030542071197411147 | 3 |
| DIVIDEND | US Dividend Equities | 33.26 | 34.24 | 0.029464822609741592 | 4 |
| MEXICO | Mexico Equities | 73.23999786376953 | 75.36000061035156 | 0.0289459695305474 | 5 |
| ENERGY | Energy Sector | 66.01 | 67.8 | 0.02711710346917129 | 6 |
| INDIA | India Equities | 46.36 | 47.4 | 0.022433132010353685 | 7 |
| HEALTHCARE | Healthcare Sector | 171.99 | 175.65 | 0.0212803069945926 | 8 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.27 | 114.46 | 0.019506546717733997 | 9 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 78.05 | 79.46 | 0.01806534272901983 | 10 |
| CANADA | Canada Equities | 59.45 | 60.28 | 0.013961312026913308 | 11 |
| UNITED_KINGDOM | United Kingdom Equities | 46.7 | 47.34 | 0.013704496788008669 | 12 |
| SOUTH_AFRICA | South Africa Equities | 63.77000045776367 | 64.61000061035156 | 0.01317234038824 | 13 |
| MUNICIPAL_BONDS | Municipal Bonds | 101.16000366210938 | 102.33999633789062 | 0.011664616776039471 | 14 |
| LOW_VOL | US Low Volatility Equities | 72.79 | 73.57 | 0.010715757659018887 | 15 |
| BROAD_COMMODITIES | Broad Commodities | 19.86 | 20.07 | 0.010574018126888296 | 16 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 206.03 | 207.755 | 0.008372567101878392 | 17 |
| TIPS | Treasury Inflation-Protected Securities | 104.5 | 105.26 | 0.0072727272727273196 | 18 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 89.43 | 90.08 | 0.007268254500726767 | 19 |
| EUROPE | Europe Equities | 85.82 | 86.43 | 0.007107900256350552 | 20 |
| AUSTRALIA | Australia Equities | 28.670000076293945 | 28.829999923706055 | 0.005580741087768848 | 21 |
| EURO | Euro | 102.98999786376953 | 103.4800033569336 | 0.004757796905794809 | 22 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 94.66 | 95.11 | 0.004753855905345494 | 23 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 89.83000183105469 | 90.22000122070312 | 0.0043415271256692645 | 24 |
| LARGE_VALUE | US Large-Cap Value | 254.65 | 255.43 | 0.0030630276850578397 | 25 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 102.58 | 102.88 | 0.002924546695262098 | 26 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.970001220703125 | 47.029998779296875 | 0.0012773591022881003 | 27 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.19 | 213.4 | 0.0009850368216146599 | 28 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.5 | 91.57 | 0.0007650273224042436 | 29 |
| FINANCIALS | Financials Sector | 55.05 | 55.06 | 0.00018165304268857874 | 30 |
| YEN | Japanese Yen | 57.779998779296875 | 57.790000915527344 | 0.00017310724198305039 | 31 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 91.08000183105469 | 91.08999633789062 | 0.00010973327442909131 | 32 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 33 |
| REGIONAL_BANKS | Regional Banks | 69.56 | 69.26 | -0.004312823461759541 | 34 |
| US_DOLLAR | US Dollar | 29.1299991607666 | 29.0 | -0.004462724494056602 | 35 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 77.29 | 76.83 | -0.005951610816405828 | 36 |
| REAL_ESTATE | Real Estate Sector | 41.92 | 41.67 | -0.0059637404580152875 | 37 |
| GOLD | Gold | 78.34 | 77.85 | -0.006254786826653147 | 38 |
| UTILITIES | Utilities Sector | 41.63 | 41.36 | -0.00648570742253185 | 39 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.95 | 69.36 | -0.008434596140100115 | 40 |
| AGRICULTURE | Agriculture Commodities | 28.440000534057617 | 28.200000762939453 | -0.008438810359049032 | 41 |
| MID_CAP | US Mid-Cap Stocks | 73.16 | 72.38 | -0.010661563696008791 | 42 |
| BITCOIN_ETF | Bitcoin ETF | 46.86000061035156 | 46.29999923706055 | -0.011950519974327722 | 43 |
| COMMUNICATIONS | Communication Services Sector | 111.45 | 110.09 | -0.012202781516375105 | 44 |
| INDUSTRIALS | Industrials Sector | 169.15 | 166.68 | -0.01460242388412647 | 45 |
| SP500 | S&P 500 | 778.1 | 766.48 | -0.014933813134558549 | 46 |
| SMALL_VALUE | US Small-Cap Value | 211.09 | 207.85 | -0.015348903311383832 | 47 |
| TOTAL_US_MARKET | Total US Stock Market | 381.57 | 375.54 | -0.01580312917682203 | 48 |
| BIOTECH | Biotechnology | 151.4 | 147.86 | -0.0233817701453104 | 49 |
| SMALL_CAP | US Small-Cap Stocks | 277.9 | 271.28 | -0.023821518531845998 | 50 |
| JAPAN | Japan Equities | 97.32 | 94.99 | -0.02394163584052611 | 51 |
| CHINA | China Equities | 52.15 | 50.87 | -0.02454458293384465 | 52 |
| COPPER | Copper | 40.630001068115234 | 39.56999969482422 | -0.0260891298406305 | 53 |
| EMERGING_MARKETS | Emerging Markets | 59.73 | 58.03 | -0.028461409676879268 | 54 |
| METALS_MINING | Metals and Mining | 104.85 | 101.37 | -0.03319027181688117 | 55 |
| LARGE_GROWTH | US Large-Cap Growth | 127.13 | 122.61 | -0.0355541571619602 | 56 |
| BRAZIL | Brazil Equities | 43.540000915527344 | 41.93000030517578 | -0.03697750520205889 | 57 |
| NASDAQ100 | Nasdaq 100 | 746.04 | 718.36 | -0.03710256822690461 | 58 |
| BROAD_AI_TECH | Broad AI Technology | 65.92 | 62.96 | -0.04490291262135926 | 59 |
| SOFTWARE | Software | 111.28 | 105.99 | -0.047537742631200586 | 60 |
| ETHEREUM_ETF | Ethereum ETF | 56.95000076293945 | 54.11000061035156 | -0.0498683075424301 | 61 |
| SOLAR | Solar Energy | 43.48 | 41.31 | -0.04990800367985271 | 62 |
| SILVER | Silver | 54.349998474121094 | 51.540000915527344 | -0.05170188845417789 | 63 |
| TECHNOLOGY | Technology Sector | 196.36 | 185.96 | -0.05296394377673663 | 64 |
| TAIWAN | Taiwan Equities | 114.2699966430664 | 107.26000213623047 | -0.06134588879644709 | 65 |
| MOMENTUM | US Momentum Equities | 315.09 | 295.71 | -0.061506236313434215 | 66 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 121.6 | 113.51 | -0.06652960526315777 | 67 |
| SEMICONDUCTORS | Semiconductors | 590.99 | 548.46 | -0.0719639926225486 | 68 |
| CYBERSECURITY | Cybersecurity | 107.8 | 99.92 | -0.07309833024118739 | 69 |
| SOUTH_KOREA | South Korea Equities | 170.11000061035156 | 156.5800018310547 | -0.079536762863744 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | SEMICONDUCTORS | 35.0 | -0.0719639926225486 | -0.02518739741789201 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SOUTH_KOREA | 35.0 | -0.079536762863744 | -0.0278378670023104 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | TAIWAN | 30.0 | -0.06134588879644709 | -0.018403766638934126 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | SEMICONDUCTORS | 35.0 | -0.0719639926225486 | -0.02518739741789201 | V3 selected model rank 1: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | SP500 | 65.0 | -0.014933813134558549 | -0.009706978537463056 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | SOUTH_KOREA | 35.0 | -0.079536762863744 | -0.0278378670023104 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 35.0 | -0.0719639926225486 | -0.02518739741789201 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | TECHNOLOGY | 30.0 | -0.05296394377673663 | -0.015889183133020988 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | SEMICONDUCTORS | 35.0 | -0.0719639926225486 | -0.02518739741789201 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | TECHNOLOGY | 35.0 | -0.05296394377673663 | -0.01853738032185782 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 30.0 | -0.014933813134558549 | -0.004480143940367565 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | REAL_ESTATE | 35.0 | -0.0059637404580152875 | -0.0020873091603053505 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 65.0 | -0.014933813134558549 | -0.009706978537463056 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | SOUTH_KOREA | 35.0 | -0.079536762863744 | -0.0278378670023104 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | SEMICONDUCTORS | 35.0 | -0.0719639926225486 | -0.02518739741789201 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-5 | TAIWAN | 30.0 | -0.06134588879644709 | -0.018403766638934126 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | SOUTH_KOREA | 35.0 | -0.079536762863744 | -0.0278378670023104 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | SEMICONDUCTORS | 35.0 | -0.0719639926225486 | -0.02518739741789201 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | TAIWAN | 30.0 | -0.06134588879644709 | -0.018403766638934126 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SP500 | 2 | 0.55 | -0.014933813134558549 | -0.011794287697768406 | 0.003139525436790143 | 0.07654962675851068 |  | True | False |
| anthropic-claude-opus-5-5 | SP500 | 2 | 0.55 | -0.014933813134558549 | -0.034894375955355064 | -0.019960562820796515 | 0.09964971501609733 |  | False | False |
| openai-gpt-6-astra | SEMICONDUCTORS | 3 | 0.555 | -0.0719639926225486 | -0.0482049216801174 | -0.03327110854555885 | 0.11296026074085966 |  | False | False |
| google-gemini-3-1-pro | SOUTH_KOREA | 3 | 0.58 | -0.079536762863744 | -0.0689144475532234 | -0.05398063441866485 | 0.13366978661396567 |  | False | False |
| xai-grok-4-5 | SOUTH_KOREA | 3 | 0.5667 | -0.079536762863744 | -0.07142903105913653 | -0.056495217924577984 | 0.1361843701198788 |  | False | False |
| xai-grok-4-6 | SOUTH_KOREA | 3 | 0.5633 | -0.079536762863744 | -0.07142903105913653 | -0.056495217924577984 | 0.1361843701198788 |  | False | False |
| anthropic-claude-fable-5-1 | SEMICONDUCTORS | 3 | 0.5567 | -0.0719639926225486 | -0.07142903105913653 | -0.056495217924577984 | 0.1361843701198788 |  | False | False |

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
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | 76cb296effedd4128e67d9aa37925d1688ac22b2bf3cb77562b69d7e198e612d |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | c64094fe25414720f216e7ae7739953bdfe2174ac4125a0f7f6bfda8426818db |
| market_data/universe_decision_context.md | 5ac3672708bb9c0ed676b78461fc0ee1af9e7806b2b61552431b1297371defe3 |
| market_data/universe_decision_context.json | eb5a62b1c1b236b54abc3dfab5e69c5b4313d30e1a78b2bab83cc4eae7105870 |
| market_data/decision_context_source_history.json | 769354e709c3c1dfb0c782f8f386cccdf743ab85f16ac4d934d824d922f2cce1 |
| market_data/universe_quality_evidence.md | d92ae9c260cf7b3fe5ec00f0f68809bf28c3c6f93cd873bc46aac224f4c3d154 |
| market_data/universe_quality_evidence.json | 5292b7815295343cf966447e769574301345bd560fff5cdb834a8795db34110d |

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
