# CapitalBench Report: CB-2026-09-01-1M / official-v3-20260901-monthly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260901-monthly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-01-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-09-01
- Decision deadline: 2026-09-02T13:25:00Z
- Horizon: one month
- Entry date: 2026-09-02
- Exit date: 2026-10-02
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 2 | 0.55 | Mixed sector signals with recent tech and cyber strength offset by broad equity weakness and policy uncertainty ahead of FOMC. | FOMC policy decision volatility; Weak July payroll revisions; Energy price swings from EIA forecasts |
| openai-gpt-5-6-sol | openai | portfolio | REGIONAL_BANKS | 3 | 0.57 | Wide cross-asset return gaps, weakening short-term breadth, high inflation, and a September FOMC create a mixed regime. Selective reversals in high-quality pullbacks appear more attractive than chasing extreme crypto or sector momentum. | Hot CPI or PPI and a hawkish September FOMC could extend pressure on rate-sensitive and smaller companies; Further labor-market or consumption weakness could worsen regional-bank credit concerns and small-cap earnings expectations; Broadcom results or semiconductor guidance could disappoint after entry; Narrow market leadership could persist, preventing the selected pullbacks from recovering before the one-month exit |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | SPY is near a 52-week high after an August gain while equal-weight lagged, breadth was mixed on the latest session, and the one-month window includes FOMC plus CPI/payrolls with sticky PCE and a 4.75% 10-year. Mega-cap tech still has relative strength; rate-sensitive losers lack a clear in-window easing catalyst. | September 15–16 FOMC and August CPI/payrolls can reprice duration and growth simultaneously.; Sticky 3.7% PCE and a 4.75% 10-year can extend underperformance of utilities, REITs, and regional banks.; High-vol semiconductors, solar, oil, and crypto can gap versus SPY on a single risk-off session.; Equal-weight lag versus SPY can persist if mega-cap tech leadership continues. |
| anthropic-claude-opus-5 | anthropic | portfolio | REGIONAL_BANKS | 3 | 0.57 | Index near highs with breadth deteriorating (RSP -1.5% vs SPY over 5 sessions, positive asset share 39%). Macro is stagflationary at the margin: PCE 3.7% y/y, payrolls -23k, GDP 1.5%, hawkish Fed with three members preferring a hike and 10y at 4.75%. That argues against duration-sensitive defensives and against aggressive high-beta reversal bets. Cross-sectional dispersion is high (crypto +22-30% active, metals/software strong, utilities/defense weak). Best risk-adjusted reversal candidates are high-quality domestic pullbacks with sound prior trends (regional banks, small value) rather than broken structural losers (solar, utilities). September carries dense event risk: Sept 4 payrolls, Sept 11 CPI, Sept 15-16 FOMC. | Sept 15-16 FOMC plus Sept 11 CPI with PCE at 3.7% could push yields higher and hit banks, small value, and real estate; Sept 4 payrolls after a -23k print and downward benchmark revision could trigger a small-cap and credit-quality de-rating; Mega-cap AI leadership could continue, making narrow SPY hard to beat with broadening bets; Brent at $90.49 versus EIA's ~$85 Q3 forecast leaves oil-linked exposures exposed to mean reversion |
| anthropic-claude-fable-5 | anthropic | portfolio | REGIONAL_BANKS | 3 | 0.5633 | SPY near highs (+2.6% August) but breadth deteriorating (RSP-SPY -1.5% 5s, positive share 39% over 5 sessions). Sticky inflation (PCE 3.7%) with hawkish Fed and 10y at 4.75% caps upside; quality pullbacks in strong-prior groups (regional banks, small value) offer the best reversal setups into the Sept FOMC. | Hawkish FOMC on Sept 16 or hot Aug CPI/PPI would hurt rate-sensitive picks (KRE, XLRE); Very weak Sept 4 payrolls could trigger credit/recession fears hitting regional banks and small caps; Continued mega-cap tech leadership would leave all breadth-oriented picks lagging SPY; Brent above $90 sustaining inflation pressure keeps yields elevated |
| xai-grok-4-5 | xai | portfolio | REGIONAL_BANKS | 3 | 0.5633 | Sticky PCE/CPI near 3.4-3.7%, soft July payrolls and 1.5% Q2 GDP, 10y at 4.75% and Sept FOMC ahead create mixed one-month setup; recent breadth weak while energy/tech pockets held up, favoring selective quality pullbacks over pure momentum or deep rate-sensitive losers. | September 16 FOMC and sticky 3.7% PCE could reprice rate-sensitive and bank names lower; August employment and CPI prints may extend soft-growth risk-off into small caps; Oil/geopolitical spike or crypto volatility could dominate residual high-beta tails; Volume dislocation in tech may reverse if mega-cap leadership fades post-NVIDIA |
| google-gemini-3-1-pro | google | portfolio | UTILITIES | 3 | 0.58 | The market is digesting mixed economic signals with steady inflation and a potential Fed rate cut in September. Tech earnings remain strong, but broader market breadth is weak. | The Fed may not cut rates as expected, negatively impacting rate-sensitive sectors.; Broader market weakness could drag down all sectors, regardless of quality or recent pullbacks. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SEMICONDUCTORS | Semiconductors | 550.48 | 630.6 | 0.1455457055660514 | 1 |
| CYBERSECURITY | Cybersecurity | 93.54 | 104.7 | 0.11930724823604866 | 2 |
| ETHEREUM_ETF | Ethereum ETF | 18.049999237060547 | 20.110000610351562 | 0.1141275047292738 | 3 |
| BITCOIN_ETF | Bitcoin ETF | 43.790000915527344 | 47.72999954223633 | 0.08997484686765356 | 4 |
| TECHNOLOGY | Technology Sector | 183.6 | 199.81 | 0.08828976034858393 | 5 |
| MOMENTUM | US Momentum Equities | 297.04 | 322.88 | 0.08699165095610017 | 6 |
| SOUTH_KOREA | South Korea Equities | 178.86 | 191.8800048828125 | 0.07279439160691314 | 7 |
| TAIWAN | Taiwan Equities | 109.43 | 116.33000183105469 | 0.06305402386050152 | 8 |
| NASDAQ100 | Nasdaq 100 | 709.24 | 749.58 | 0.05687778467091542 | 9 |
| BROAD_AI_TECH | Broad AI Technology | 63.08 | 66.23 | 0.04993658845909965 | 10 |
| SOFTWARE | Software | 103.42 | 108.43 | 0.048443241152581695 | 11 |
| OIL | Crude Oil | 141.15 | 147.3699951171875 | 0.04406656122697483 | 12 |
| LARGE_GROWTH | US Large-Cap Growth | 121.81 | 127.07 | 0.04318200476151368 | 13 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 120.24 | 124.48 | 0.03526280771789758 | 14 |
| JAPAN | Japan Equities | 96.04 | 98.92 | 0.029987505206164 | 15 |
| US_DOLLAR | US Dollar | 28.17 | 28.889999389648438 | 0.025559083764587598 | 16 |
| BROAD_COMMODITIES | Broad Commodities | 19.06 | 19.44 | 0.019937040923399874 | 17 |
| YEN | Japanese Yen | 57.72999954223633 | 58.06999969482422 | 0.005889488225946371 | 18 |
| SP500 | S&P 500 | 765.16 | 769.64 | 0.005854984578388844 | 19 |
| TOTAL_US_MARKET | Total US Stock Market | 376.88 | 377.99 | 0.0029452345574187966 | 20 |
| BRAZIL | Brazil Equities | 38.09 | 38.189998626708984 | 0.0026253249332890416 | 21 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.4 | 91.43 | 0.0003282275711160576 | 22 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 23 |
| COPPER | Copper | 39.53 | 39.52000045776367 | -0.0002529608458469168 | 24 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.25 | 46.86000061035156 | -0.008253955336474883 | 25 |
| INDUSTRIALS | Industrials Sector | 172.78 | 169.95 | -0.01637921055677749 | 26 |
| COMMUNICATIONS | Communication Services Sector | 112.42 | 110.32 | -0.018679950186799577 | 27 |
| EMERGING_MARKETS | Emerging Markets | 60.77 | 59.56 | -0.01991114036531183 | 28 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.59 | 71.13 | -0.02011296321807421 | 29 |
| MID_CAP | US Mid-Cap Stocks | 75.11 | 73.39 | -0.022899747037678053 | 30 |
| TIPS | Treasury Inflation-Protected Securities | 106.86 | 104.11 | -0.025734606026576845 | 31 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 96.84 | 94.25 | -0.026745146633622485 | 32 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.11 | 76.91 | -0.027809379345215546 | 33 |
| EURO | Euro | 106.9 | 103.81999969482422 | -0.02881197666207469 | 34 |
| LARGE_VALUE | US Large-Cap Value | 257.08 | 249.38 | -0.029951765987241252 | 35 |
| MUNICIPAL_BONDS | Municipal Bonds | 104.22 | 100.95999908447266 | -0.031279993432425046 | 36 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.35 | 101.83 | -0.03341243474133837 | 37 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.18 | 89.05 | -0.033955304838359845 | 38 |
| ENERGY | Energy Sector | 65.1 | 62.82 | -0.03502304147465429 | 39 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.51 | 89.22000122070312 | -0.03556370964541 | 40 |
| AGRICULTURE | Agriculture Commodities | 29.27 | 28.209999084472656 | -0.036214585429700796 | 41 |
| HEALTHCARE | Healthcare Sector | 172.95 | 166.18 | -0.03914426134721005 | 42 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 218.6 | 209.73 | -0.040576395242451935 | 43 |
| CANADA | Canada Equities | 61.27 | 58.72 | -0.041619063163048864 | 44 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.86 | 110.04 | -0.04196413024551626 | 45 |
| UNITED_KINGDOM | United Kingdom Equities | 48.22 | 46.18 | -0.04230609705516386 | 46 |
| SMALL_CAP | US Small-Cap Stocks | 294.01 | 281.52 | -0.042481548246658285 | 47 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.15 | 90.13999938964844 | -0.042591615617116996 | 48 |
| REGIONAL_BANKS | Regional Banks | 74.24 | 70.78 | -0.0466056034482758 | 49 |
| SMALL_VALUE | US Small-Cap Value | 223.04 | 212.34 | -0.04797345767575323 | 50 |
| EUROPE | Europe Equities | 90.96 | 86.38 | -0.05035180299032538 | 51 |
| LOW_VOL | US Low Volatility Equities | 74.66 | 70.89 | -0.05049557996249665 | 52 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 81.95 | 77.48 | -0.054545454545454564 | 53 |
| GOLD | Gold | 82.55 | 77.95 | -0.05572380375529973 | 54 |
| AUSTRALIA | Australia Equities | 30.03 | 28.31999969482422 | -0.05694306710542063 | 55 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.53 | 80.53 | -0.058459020226821035 | 56 |
| CHINA | China Equities | 54.54 | 51.24 | -0.060506050605060424 | 57 |
| DIVIDEND | US Dividend Equities | 35.01 | 32.72 | -0.06540988289060268 | 58 |
| BIOTECH | Biotechnology | 165.37 | 154.43 | -0.06615468343714093 | 59 |
| UTILITIES | Utilities Sector | 42.67 | 39.83 | -0.0665573002109211 | 60 |
| REAL_ESTATE | Real Estate Sector | 43.73 | 40.81 | -0.06677338211753936 | 61 |
| MEXICO | Mexico Equities | 76.22 | 71.08999633789062 | -0.06730521729348427 | 62 |
| SOLAR | Solar Energy | 47.27 | 44.05 | -0.06811931457584108 | 63 |
| INDIA | India Equities | 49.97 | 46.52 | -0.06904142485491283 | 64 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 223.37 | 207.79 | -0.06974974257957656 | 65 |
| FINANCIALS | Financials Sector | 57.66 | 53.49 | -0.07232049947970853 | 66 |
| SILVER | Silver | 59.07 | 54.7400016784668 | -0.07330283259748105 | 67 |
| MATERIALS | Materials Sector | 52.95 | 48.86 | -0.07724268177525973 | 68 |
| SOUTH_AFRICA | South Africa Equities | 69.99 | 63.189998626708984 | -0.0971567562979141 | 69 |
| METALS_MINING | Metals and Mining | 119.46 | 105.74 | -0.11485015904905405 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | REGIONAL_BANKS | 35.0 | -0.0466056034482758 | -0.01631196120689653 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | SMALL_VALUE | 35.0 | -0.04797345767575323 | -0.016790710186513628 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | REAL_ESTATE | 30.0 | -0.06677338211753936 | -0.020032014635261806 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | REGIONAL_BANKS | 35.0 | -0.0466056034482758 | -0.01631196120689653 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SMALL_VALUE | 35.0 | -0.04797345767575323 | -0.016790710186513628 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SP500 | 30.0 | 0.005854984578388844 | 0.0017564953735166532 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | UTILITIES | 35.0 | -0.0665573002109211 | -0.023295055073822384 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | REGIONAL_BANKS | 35.0 | -0.0466056034482758 | -0.01631196120689653 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | REAL_ESTATE | 30.0 | -0.06677338211753936 | -0.020032014635261806 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | REGIONAL_BANKS | 35.0 | -0.0466056034482758 | -0.01631196120689653 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SMALL_VALUE | 35.0 | -0.04797345767575323 | -0.016790710186513628 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 30.0 | 0.1455457055660514 | 0.04366371166981542 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-3 | OIL | 35.0 | 0.04406656122697483 | 0.01542329642944119 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 65.0 | 0.005854984578388844 | 0.003805739975952749 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | REGIONAL_BANKS | 35.0 | -0.0466056034482758 | -0.01631196120689653 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | SMALL_VALUE | 35.0 | -0.04797345767575323 | -0.016790710186513628 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-5 | REAL_ESTATE | 30.0 | -0.06677338211753936 | -0.020032014635261806 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 100.0 | 0.005854984578388844 | 0.005854984578388844 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SP500 | 2 | 0.55 | 0.005854984578388844 | 0.01922903640539394 | 0.013374051827005094 | 0.12631666916065745 |  | True | True |
| openai-gpt-5-6-sol | REGIONAL_BANKS | 3 | 0.57 | -0.0466056034482758 | 0.01056104027640526 | 0.004706055698016416 | 0.13498466528964614 |  | True | True |
| xai-grok-4-6 | SP500 | 1 | 0.5 | 0.005854984578388844 | 0.005854984578388844 | 0.0 | 0.13969072098766255 |  | False | True |
| anthropic-claude-opus-5 | REGIONAL_BANKS | 3 | 0.57 | -0.0466056034482758 | -0.03134617601989351 | -0.03720116059828235 | 0.1768918815859449 |  | False | False |
| anthropic-claude-fable-5 | REGIONAL_BANKS | 3 | 0.5633 | -0.0466056034482758 | -0.05313468602867197 | -0.05898967060706081 | 0.19868039159472337 |  | False | False |
| xai-grok-4-5 | REGIONAL_BANKS | 3 | 0.5633 | -0.0466056034482758 | -0.05313468602867197 | -0.05898967060706081 | 0.19868039159472337 |  | False | False |
| google-gemini-3-1-pro | UTILITIES | 3 | 0.58 | -0.0665573002109211 | -0.05963903091598072 | -0.06549401549436956 | 0.20518473648203212 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 25ea4f21542b2e6d6c391d52fd554e6c5eaea9f16fbe9c2e581843e70c82dcae |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | 526c7948a3e94f754ac2d4ede6990e3541971214ee597a34a4723e4d399a2889 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | a39653f901fb9a76bf2cb0d105128203c66660e1df33f18b6a1777e327df17e7 |
| market_data/universe_decision_context.md | f7823f148e52b918b3905927401607cce387dac96789b6d25592101dcb978421 |
| market_data/universe_decision_context.json | be6e11b00493934773433265e2bd630aa5beb7d0b9e7a17db3afa450fa858bce |
| market_data/decision_context_source_history.json | f8728fe05edae806516311f9bb753397f9ce68a8b7b21bf6df756b9894de03ef |
| market_data/universe_quality_evidence.md | 0fe822de3166a8a303d0ae81cb7f76844b05227a9cc8abab7e448136cadd87f7 |
| market_data/universe_quality_evidence.json | 684b3e60a41b74a28f97b6c0033266796d435f6ed16a9e73d0777b2b83c2394a |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 7aea745e2dbf20316eaed0175da03324cb9f5691bd180609c2fa0d9839bddb29 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | ae8251016abcc88332689fb056803a776ced6dd70dd91775adfa0172e9e4e758 | yes |
| Final briefing | research/final_briefing.md | model-facing | 25ea4f21542b2e6d6c391d52fd554e6c5eaea9f16fbe9c2e581843e70c82dcae | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
