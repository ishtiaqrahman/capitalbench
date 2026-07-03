# CapitalBench Report: CB-2026-06-25-1W / official-20260625-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260625-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-25-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-06-25
- Decision deadline: 2026-06-26T02:30:00Z
- Horizon: one week
- Entry date: 2026-06-25
- Exit date: 2026-07-02
- Entry rule: Use adjusted close prices on Thursday, June 25, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Thursday, July 2, 2026 as the one-week exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | BIOTECH | 4 | 0.55 | Biotech and healthcare lead due to briefing-highlighted positive data; small-value and equal-weight provide balance against concentration and reversal risks. | July 2 employment report volatility could trigger sharp sector rotations; Micron-related AI enthusiasm may fail to lift broader semis or biotech holdings; Inflation readings embedded in PCE and CPI data could pressure rate-sensitive small caps |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Tilt to healthcare/biotech leadership and cyclical industrials backed by 49-month-high manufacturing PMI, with equal-weight S&P for breadth and T-bills as buffer into July 2 payrolls. | Payrolls surprise on July 2 could whipsaw rate-sensitive defensives; Biotech/healthcare momentum reversal after sharp 7d/30d gains; Mega-cap tech rebound would cause cap-weighted SPY benchmark to outperform our tilts; Sticky CPI/PCE inflation prints could pressure all equity sectors |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Rotate into healthcare, industrials, biotech, banks, and dividends that are outperforming during the Nasdaq drawdown, balancing defensive low-beta names with PMI-supported cyclicals. | July 2 jobs report could surprise and trigger a sharp rotation reversing recent sector leadership before the exit close; Biotech and regional banks carry high volatility; recent strength may mean-revert given stretched up-day shares; A relief rally in mega-cap tech/Nasdaq would cause this defensive/cyclical tilt to underperform the SPX benchmark; Sticky inflation (PCE 4.1%, PPI 6.5%) could pressure rate-sensitive financials and banks if yields spike |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 2 | 0.65 | Allocating to semiconductors based on Micron's strong earnings and guidance, balanced with defensive healthcare exposure. | Semiconductor stocks may sell off if the Micron news is already priced in or if broader tech sentiment weakens.; Healthcare stocks could underperform if there is a sudden rotation back into high-beta growth or cyclical sectors.; Upcoming macro data releases, such as the July 2 Employment Situation report, could cause broad market volatility that overrides sector-specific catalysts. |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 4 | 0.56 | A concentrated allocation to semiconductors is paired with regional banks, biotech, and small value to capture likely post-earnings AI-chip strength and recent broadening in U.S. market leadership. The main bet is that the latest growth data and sector catalysts outweigh inflation and jobs-report risks before the July 2 close. | Micron's results may already be priced in or trigger a sell-the-news reaction across semiconductors after extreme trailing gains and high volatility.; The July 2 employment report could reprice Fed expectations, lift yields, and pressure small caps, banks, biotech, and high-beta technology.; Recent rotation into small value, regional banks, and biotech could reverse quickly if investors return to mega-cap defensives or de-risk ahead of the holiday.; Hot CPI/PPI/PCE inflation readings may keep rate-cut expectations constrained and weigh on duration-sensitive or financing-sensitive equity groups.; A broad risk-off move or renewed weakness in Nasdaq leadership could cause the portfolio's high-beta exposures to underperform SPY. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOFTWARE | Software | 84.76000213623047 | 93.57 | 0.10394051016668993 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 11.74 | 12.86 | 0.09540034071550241 | 2 |
| CYBERSECURITY | Cybersecurity | 83.66000366210938 | 90.67 | 0.08379148973269213 | 3 |
| BIOTECH | Biotechnology | 151.59 | 160.46 | 0.05851309453130149 | 4 |
| HEALTHCARE | Healthcare Sector | 155.6300048828125 | 163.74 | 0.05211074254796966 | 5 |
| SILVER | Silver | 52.36 | 55.02 | 0.050802139037433136 | 6 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 237.38 | 248.19 | 0.04553879855084686 | 7 |
| FINANCIALS | Financials Sector | 53.45000076293945 | 55.62 | 0.040598675511435145 | 8 |
| BITCOIN_ETF | Bitcoin ETF | 33.52 | 34.87 | 0.040274463007159644 | 9 |
| COMMUNICATIONS | Communication Services Sector | 105.58000183105469 | 109.6 | 0.03807537506371683 | 10 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 113.3499984741211 | 117.12 | 0.03325982864251764 | 11 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 123.83999633789062 | 127.94 | 0.03310726569244027 | 12 |
| UNITED_KINGDOM | United Kingdom Equities | 45.88 | 47.16 | 0.027898866608543793 | 13 |
| LARGE_GROWTH | US Large-Cap Growth | 118.0999984741211 | 121.16 | 0.025910258809608955 | 14 |
| LOW_VOL | US Low Volatility Equities | 74.9000015258789 | 76.73 | 0.02443255589906501 | 15 |
| GOLD | Gold | 75.70999908447266 | 77.51 | 0.02377494303650729 | 16 |
| EUROPE | Europe Equities | 87.83000183105469 | 89.35 | 0.01730613841804418 | 17 |
| TOTAL_US_MARKET | Total US Stock Market | 362.9360046386719 | 368.76 | 0.016046893355555314 | 18 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 211.75 | 214.91 | 0.014923258559622177 | 19 |
| SP500 | S&P 500 | 734.2999877929688 | 744.78 | 0.014272112734919462 | 20 |
| DIVIDEND | US Dividend Equities | 31.959999084472656 | 32.39 | 0.013454346928822414 | 21 |
| SOUTH_AFRICA | South Africa Equities | 63.17 | 64.0 | 0.013139148329903483 | 22 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.94000244140625 | 84.99 | 0.012508905504579726 | 23 |
| LARGE_VALUE | US Large-Cap Value | 244.41000366210938 | 246.81 | 0.00981955035362847 | 24 |
| COPPER | Copper | 36.98 | 37.29 | 0.008382909680908712 | 25 |
| BRAZIL | Brazil Equities | 34.18 | 34.43 | 0.007314218841427689 | 26 |
| AUSTRALIA | Australia Equities | 27.93 | 28.09 | 0.005728607232366567 | 27 |
| EURO | Euro | 104.8699534661 | 105.47 | 0.0057218155827061246 | 28 |
| SMALL_VALUE | US Small-Cap Value | 220.11000061035156 | 221.33 | 0.005542680415544288 | 29 |
| YEN | Japanese Yen | 56.69 | 56.95 | 0.004586346798377328 | 30 |
| EMERGING_MARKETS | Emerging Markets | 58.79999923706055 | 59.04 | 0.004081645681182078 | 31 |
| REGIONAL_BANKS | Regional Banks | 74.77 | 75.02 | 0.0033435870001337076 | 32 |
| MATERIALS | Materials Sector | 51.84000015258789 | 52.01 | 0.003279318034562495 | 33 |
| INDIA | India Equities | 49.43000030517578 | 49.56 | 0.0026299756022984955 | 34 |
| CANADA | Canada Equities | 57.62 | 57.77 | 0.0026032627559875454 | 35 |
| CHINA | China Equities | 50.779998779296875 | 50.91 | 0.0025600871175310846 | 36 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.51141357421875 | 79.71 | 0.0024975838921021953 | 37 |
| REAL_ESTATE | Real Estate Sector | 44.59000015258789 | 44.68 | 0.0020183863445644157 | 38 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.2915482618 | 107.5 | 0.0019428532962479927 | 39 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.33211517333984 | 91.44 | 0.001181236484618875 | 40 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.1596824949 | 96.2 | 0.00041927660381091414 | 41 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 42 |
| MEXICO | Mexico Equities | 75.53 | 75.5 | -0.0003971931682774654 | 43 |
| TAIWAN | Taiwan Equities | 104.91 | 104.86 | -0.00047659898961016633 | 44 |
| TIPS | Treasury Inflation-Protected Securities | 108.44132232666016 | 108.33 | -0.0010265674031972871 | 45 |
| INDUSTRIALS | Industrials Sector | 184.1199951171875 | 183.91 | -0.0011405340145368426 | 46 |
| UTILITIES | Utilities Sector | 45.849998474121094 | 45.76 | -0.0019628893591325802 | 47 |
| JAPAN | Japan Equities | 93.38999938964844 | 93.14 | -0.0026769396218258024 | 48 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.3785499326 | 48.24 | -0.002863871132826934 | 49 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.91809844970703 | 98.61 | -0.0031146822930858686 | 50 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.47827911376953 | 94.12 | -0.0037921850094040366 | 51 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.11650085449219 | 108.64 | -0.00436690006333329 | 52 |
| SMALL_CAP | US Small-Cap Stocks | 298.9100036621094 | 297.58 | -0.004449512046484916 | 53 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.5806885106 | 94.13 | -0.0047651219048747695 | 54 |
| MID_CAP | US Mid-Cap Stocks | 76.45999908447266 | 76.09 | -0.004839119656068536 | 55 |
| US_DOLLAR | US Dollar | 28.48 | 28.34 | -0.004915730337078705 | 56 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.16000366210938 | 70.81 | -0.0049185447456031595 | 57 |
| NASDAQ100 | Nasdaq 100 | 716.3800048828125 | 712.6 | -0.005276535996326159 | 58 |
| AGRICULTURE | Agriculture Commodities | 26.92 | 26.74 | -0.006686478454680622 | 59 |
| BROAD_COMMODITIES | Broad Commodities | 16.110000610351562 | 15.87 | -0.014897616465473607 | 60 |
| ENERGY | Energy Sector | 54.09000015258789 | 53.22 | -0.016084306713507468 | 61 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 87.02857971191406 | 85.51 | -0.017449207110364573 | 62 |
| TECHNOLOGY | Technology Sector | 184.57000732421875 | 180.59 | -0.021563673220359125 | 63 |
| SOLAR | Solar Energy | 57.87 | 56.32 | -0.026784171418697045 | 64 |
| METALS_MINING | Metals and Mining | 108.74 | 105.13 | -0.03319845503034757 | 65 |
| BROAD_AI_TECH | Broad AI Technology | 64.18000030517578 | 61.85 | -0.03630414917570324 | 66 |
| OIL | Crude Oil | 109.31 | 103.98 | -0.048760406184246596 | 67 |
| MOMENTUM | US Momentum Equities | 339.29998779296875 | 316.53 | -0.06710871975292376 | 68 |
| SEMICONDUCTORS | Semiconductors | 636.8800048828125 | 592.29 | -0.07001319642782189 | 69 |
| SOUTH_KOREA | South Korea Equities | 205.0 | 180.14 | -0.12126829268292694 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 30.0 | 0.05211074254796966 | 0.015633222764390897 | Defensive leadership with strong recent breadth, low beta, and biotech tailwind; tech weakness rotation beneficiary. |
| anthropic-claude-opus-4-7 | BIOTECH | 20.0 | 0.05851309453130149 | 0.0117026189062603 | Strongest recent momentum supported by sector rotation into healthcare; near 52w high with broad participation. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 20.0 | -0.0011405340145368426 | -0.00022810680290736852 | Flash manufacturing PMI at 49-month high (55.7) supports cyclical industrials; at 52w highs with solid breadth. |
| anthropic-claude-opus-4-7 | EQUAL_WEIGHT_SP500 | 20.0 | 0.014923258559622177 | 0.0029846517119244357 | Broad participation away from mega-cap tech weakness; balanced exposure ahead of payrolls. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 10.0 | 0.001181236484618875 | 0.0001181236484618875 | Dry powder buffer ahead of July 2 payrolls and holiday-shortened week. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 25.0 | 0.05211074254796966 | 0.013027685636992414 | Defensive sector with strongest recent relative strength (+7.17% vs SPX 30d), low beta 0.40, supported by rotation into defensives amid Nasdaq weakness. |
| anthropic-claude-opus-4-8 | BIOTECH | 20.0 | 0.05851309453130149 | 0.0117026189062603 | Leading momentum with +7.83% 7d and +15.71% vs SPX 30d on broad strength; high up-day share supports continuation, though volatile. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 20.0 | -0.0011405340145368426 | -0.00022810680290736852 | Manufacturing PMI 49-month high (55.7) supports cyclicals; +7.81% vs SPX 30d with manageable volatility and at 52w high. |
| anthropic-claude-opus-4-8 | REGIONAL_BANKS | 15.0 | 0.0033435870001337076 | 0.0005015380500200561 | Strong relative strength (+8.90% vs SPX 30d) and steepening curve dynamics favor banks; high up-day share signals breadth. |
| anthropic-claude-opus-4-8 | DIVIDEND | 20.0 | 0.013454346928822414 | 0.002690869385764483 | Defensive quality tilt with positive 7d return and low beta 0.33, provides ballast against tech-led drawdown into jobs report. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 50.0 | -0.07001319642782189 | -0.035006598213910944 | Micron's strong earnings beat and positive guidance, particularly regarding high-volume HBM4 shipments, provides a strong near-term catalyst for the semiconductor sector. |
| google-gemini-3-1-pro | HEALTHCARE | 50.0 | 0.05211074254796966 | 0.02605537127398483 | Healthcare offers defensive characteristics amid mixed macro data (rising unemployment, lower durable goods orders) and has shown recent relative strength. |
| openai-gpt-5-5 | SEMICONDUCTORS | 50.0 | -0.07001319642782189 | -0.035006598213910944 | Micron's exceptionally strong reported revenue, earnings, Q4 guidance, and HBM shipment commentary provide a near-term fundamental catalyst for semiconductor sentiment despite high volatility and recent pullback risk. |
| openai-gpt-5-5 | REGIONAL_BANKS | 20.0 | 0.0033435870001337076 | 0.0006687174000267415 | Recent leadership in smaller domestic cyclicals is supported by resilient claims, stronger GDP revision, and steady policy rates, with regional banks positioned to benefit if risk appetite and yield-curve expectations remain constructive. |
| openai-gpt-5-5 | BIOTECH | 15.0 | 0.05851309453130149 | 0.008776964179695224 | Biotech has shown strong recent relative strength alongside broader healthcare strength, and lower direct sensitivity to the mega-cap tech selloff may help over the one-week window; support beyond price action is limited. |
| openai-gpt-5-5 | SMALL_VALUE | 15.0 | 0.005542680415544288 | 0.0008314020623316432 | Small-cap value has been outperforming the cap-weighted S&P 500 while domestic growth and labor data remain resilient, offering exposure to the current rotation away from large-cap growth concentration. |
| xai-grok-4-3 | BIOTECH | 35.0 | 0.05851309453130149 | 0.02047958308595552 | Strong 7d outperformance amid positive macro data including upward GDP revision and rising PMI readings. |
| xai-grok-4-3 | HEALTHCARE | 25.0 | 0.05211074254796966 | 0.013027685636992414 | 4.63% 7d gain with supportive employment and consumption trends in briefing. |
| xai-grok-4-3 | SMALL_VALUE | 20.0 | 0.005542680415544288 | 0.0011085360831088575 | Recent outperformance in small-value segment alongside broad US growth signals. |
| xai-grok-4-3 | EQUAL_WEIGHT_SP500 | 20.0 | 0.014923258559622177 | 0.0029846517119244357 | Diversified exposure to reduce concentration risk while capturing domestic equity momentum. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | BIOTECH | 4 | 0.55 | 0.05851309453130149 | 0.037600456517981225 | 0.023328343783061763 | 0.06634005364870871 |  | True | True |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.55 | 0.05211074254796966 | 0.03021051022813015 | 0.015938397493210688 | 0.07372999993855978 |  | True | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.55 | 0.05211074254796966 | 0.027694605176129886 | 0.013422492441210424 | 0.07624590499056004 |  | True | True |
| google-gemini-3-1-pro | SEMICONDUCTORS | 2 | 0.65 | -0.07001319642782189 | -0.008951226939926116 | -0.023223339674845578 | 0.11289173710661604 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 4 | 0.56 | -0.07001319642782189 | -0.02472951457185734 | -0.0390016273067768 | 0.12867002473854727 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 833e3b256d8a101b15bbfec9218a8e488aa2043c1c3e26c4fecdfcd334c16dcb |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 66320ebc013af445c33450b3005ec684487d06b5bca45c52a3ff9e8e24373e4c |
| manifest.yaml | 380294a8fdf750b77f918f1bdac6d38ee7f47cdff67fd814d6907ca1e1fb44f2 |
| market_data/universe_trailing_returns.csv | 588a18556cdd760fe00850402f904f0091c916028909ec54a8a91f87d3923222 |
| market_data/universe_trailing_returns.md | 6f45e81899cde555e6a0c994a0a81cc8ed5fd622e04b29c8b822ca16590655f8 |
| market_data/universe_trailing_returns.json | 78ca1f08d33196266f5984801e46bd4fdbec70164784010f15bb7816ab57ac5d |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | d3fef3527a2acece67484f58a15b279dfd41e21b2b5a8ee2044c5abb24864c37 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 070d5246b1455a7f7f46a07871bf4cad854a14f9195f6671a91d5a3a4e088b75 | yes |
| Final briefing | research/final_briefing.md | model-facing | 833e3b256d8a101b15bbfec9218a8e488aa2043c1c3e26c4fecdfcd334c16dcb | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
