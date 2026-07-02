# CapitalBench Report: CB-2026-06-24-1W / official-20260624-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260624-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-24-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-06-24
- Decision deadline: 2026-06-25T02:30:00Z
- Horizon: one week
- Entry date: 2026-06-24
- Exit date: 2026-07-01
- Entry rule: Use adjusted close prices on Wednesday, June 24, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Wednesday, July 1, 2026 as the one-week exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 5 | 0.55 | Overweight relative-strength cyclicals and defensives benefiting from improved breadth and falling yields, underweighting mega-cap tech that is pressuring the benchmark. | Mega-cap tech rebound could lift SPX faster than these holdings, eroding alpha; Regional banks and financials are sensitive to a yield reversal higher if PCE data surprises hot on June 25; Sector rotation could reverse, with recent leaders (KRE, XLI) seeing profit-taking into quarter/month-end and the July 3 holiday's thin liquidity; Strong May CPI energy/gasoline figures could resurface inflation fears, pressuring rate-sensitive holdings |
| xai-grok-4-3 | xai | portfolio | SMALL_CAP | 5 | 0.65 | Focus on domestic growth-sensitive areas with positive recent positioning and macro support from June flash PMI and sales data. | Weaker-than-expected Q1 GDP third estimate or personal income data on June 25 could pressure risk assets.; Continued energy price volatility may affect inflation-sensitive sectors before exit close.; Large-cap tech weakness could spill over to broader equity sentiment. |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 4 | 0.58 | Favor high-beta semiconductor upside from Micron's earnings catalyst plus selective exposure to recent breadth leaders outside mega-cap indices. The allocation accepts elevated volatility to maximize expected one-week alpha versus SPY. | A hot PCE, durable goods, or jobless-claims surprise could push yields higher and pressure high-beta semiconductors, biotech, and small caps.; Micron-specific enthusiasm may fail to translate to the broader semiconductor ETF, or investors may sell the news after very large prior 6-month and 1-year gains.; Recent strength in biotech and regional banks has limited independent catalyst support in the briefing and could reverse quickly if momentum or risk appetite fades.; Mega-cap S&P 500 constituents could rebound sharply after the June 24 weakness, causing this smaller-cap and thematic tilt to lag the benchmark. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | MID_CAP | 5 | 0.55 | Cyclical broadening trade with defensive healthcare and duration hedge, capitalizing on falling yields, strong manufacturing PMI, and visible rotation under the index surface. | Hot May PCE print on 6/25 could reverse the duration and small-cap rally; Mega-cap tech rebound would lift SPY benchmark and hurt relative performance of equal-weight tilt; Sticky CPI (4.2% YoY headline) limits Fed easing optionality; Small/mid-cap reversal risk after strong recent run into 52w highs; Holiday-shortened week with July 3 closure may amplify volatility around exit |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.65 | Overweighting semiconductors based on a specific positive catalyst (Micron earnings), balanced with small caps and regional banks for diversification and momentum. | A broader market sell-off driven by macroeconomic concerns or a hawkish shift in Fed expectations.; Semiconductor stocks failing to rally despite Micron's positive results, potentially due to high valuations or broader tech sector weakness.; Regional banks facing renewed pressure from commercial real estate concerns or deposit flight.; Small caps underperforming if economic growth slows more than expected. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| CYBERSECURITY | Cybersecurity | 83.7278415327 | 91.11 | 0.08816850323815983 | 1 |
| SOFTWARE | Software | 86.17 | 93.34 | 0.08320761285830347 | 2 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 124.22 | 130.44 | 0.05007245210111089 | 3 |
| BIOTECH | Biotechnology | 149.71 | 156.55 | 0.04568833077282752 | 4 |
| HEALTHCARE | Healthcare Sector | 153.35000610351562 | 159.54 | 0.0403651362902846 | 5 |
| SILVER | Silver | 51.78 | 53.58 | 0.03476245654692933 | 6 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 236.19 | 243.86 | 0.032473855794064255 | 7 |
| COMMUNICATIONS | Communication Services Sector | 106.54000091552734 | 109.74 | 0.030035658503606122 | 8 |
| REGIONAL_BANKS | Regional Banks | 73.97 | 76.18 | 0.02987697715289994 | 9 |
| LARGE_GROWTH | US Large-Cap Growth | 119.66999816894531 | 123.02 | 0.02799366493116584 | 10 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.06999969482422 | 118.09 | 0.02624489713378897 | 11 |
| COPPER | Copper | 36.31 | 37.21 | 0.02478656017626002 | 12 |
| ETHEREUM_ETF | Ethereum ETF | 11.92 | 12.19 | 0.022651006711409405 | 13 |
| NASDAQ100 | Nasdaq 100 | 710.6199951171875 | 725.17 | 0.02047508511270224 | 14 |
| MEXICO | Mexico Equities | 73.79 | 75.27 | 0.020056918281609937 | 15 |
| FINANCIALS | Financials Sector | 53.720001220703125 | 54.78 | 0.01973192023845982 | 16 |
| TOTAL_US_MARKET | Total US Stock Market | 362.60693359375 | 369.27 | 0.01837545228441506 | 17 |
| INDUSTRIALS | Industrials Sector | 180.2100067138672 | 183.36 | 0.017479569218008528 | 18 |
| SP500 | S&P 500 | 733.239990234375 | 745.76 | 0.017074913987742413 | 19 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 210.38 | 213.41 | 0.014402509744272374 | 20 |
| SMALL_VALUE | US Small-Cap Value | 218.58999633789062 | 221.71 | 0.014273314032571482 | 21 |
| TECHNOLOGY | Technology Sector | 183.0500030517578 | 185.62 | 0.014039862908472811 | 22 |
| GOLD | Gold | 74.99 | 75.96 | 0.012935058007734312 | 23 |
| LARGE_VALUE | US Large-Cap Value | 241.0 | 243.88 | 0.011950207468879759 | 24 |
| AGRICULTURE | Agriculture Commodities | 26.56 | 26.86 | 0.011295180722891596 | 25 |
| UNITED_KINGDOM | United Kingdom Equities | 45.45 | 45.94 | 0.010781078107810593 | 26 |
| BRAZIL | Brazil Equities | 33.85 | 34.18 | 0.009748892171344226 | 27 |
| EUROPE | Europe Equities | 86.95 | 87.77 | 0.009430707303047736 | 28 |
| TAIWAN | Taiwan Equities | 104.72 | 105.69 | 0.009262796027501796 | 29 |
| MID_CAP | US Mid-Cap Stocks | 75.76000213623047 | 76.44 | 0.008975684326760769 | 30 |
| SMALL_CAP | US Small-Cap Stocks | 296.69000244140625 | 299.32 | 0.008864463031959202 | 31 |
| SOUTH_AFRICA | South Africa Equities | 62.18 | 62.73 | 0.008845287873914476 | 32 |
| LOW_VOL | US Low Volatility Equities | 74.69000244140625 | 75.24 | 0.007363737322477748 | 33 |
| CANADA | Canada Equities | 57.29 | 57.67 | 0.006632920230406736 | 34 |
| JAPAN | Japan Equities | 92.61 | 93.05 | 0.004751106791923032 | 35 |
| EMERGING_MARKETS | Emerging Markets | 58.97 | 59.22 | 0.004239443784975316 | 36 |
| DIVIDEND | US Dividend Equities | 31.719999313354492 | 31.85 | 0.004098382391539923 | 37 |
| BITCOIN_ETF | Bitcoin ETF | 33.87 | 34.0 | 0.0038382049010925456 | 38 |
| BROAD_AI_TECH | Broad AI Technology | 63.3895538449 | 63.63 | 0.0037931510874540386 | 39 |
| SEMICONDUCTORS | Semiconductors | 618.92 | 620.46 | 0.0024882052607768657 | 40 |
| EURO | Euro | 104.7000669396 | 104.95 | 0.0023871337211673893 | 41 |
| CHINA | China Equities | 51.43 | 51.525 | 0.0018471709119189939 | 42 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.171870015 | 107.34 | 0.0015687883861359442 | 43 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.27999877929688 | 70.36 | 0.0011383213160596206 | 44 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 45 |
| BROAD_COMMODITIES | Broad Commodities | 15.78 | 15.78 | 0.0 | 45 |
| MOMENTUM | US Momentum Equities | 328.4100036621094 | 328.1 | -0.0009439531641926013 | 47 |
| US_DOLLAR | US Dollar | 28.53 | 28.49 | -0.001402032947774412 | 48 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.1696769436 | 96.02 | -0.0015563839700509785 | 49 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.58999633789062 | 91.4 | -0.002074422376759255 | 50 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.3885269485 | 48.27 | -0.0024494845364098072 | 51 |
| MATERIALS | Materials Sector | 51.15999984741211 | 51.02 | -0.0027365099263030324 | 52 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.8499984741211 | 79.59 | -0.0032560861501500504 | 53 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.4112962113 | 94.02 | -0.004144591028855782 | 54 |
| YEN | Japanese Yen | 56.7 | 56.43 | -0.004761904761904856 | 55 |
| SOLAR | Solar Energy | 58.16 | 57.8 | -0.0061898211829436445 | 56 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 99.19000244140625 | 98.5 | -0.006956370848098858 | 57 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.7300033569336 | 94.03 | -0.007389457744407024 | 58 |
| REAL_ESTATE | Real Estate Sector | 44.5099983215332 | 44.18 | -0.007414026824924758 | 59 |
| AUSTRALIA | Australia Equities | 27.91 | 27.7 | -0.007524184879971418 | 60 |
| INDIA | India Equities | 49.63 | 49.21 | -0.008462623413258097 | 61 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.41000366210938 | 108.46 | -0.008682968927076096 | 62 |
| TIPS | Treasury Inflation-Protected Securities | 109.31999969482422 | 108.17 | -0.010519572795778753 | 63 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.44000244140625 | 83.3 | -0.0135007390862798 | 64 |
| ENERGY | Energy Sector | 53.56999969482422 | 52.81 | -0.014187039371920007 | 65 |
| UTILITIES | Utilities Sector | 45.540000915527344 | 44.77 | -0.016908232324272965 | 66 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 87.37999725341797 | 85.52 | -0.021286304782359267 | 67 |
| METALS_MINING | Metals and Mining | 107.22 | 104.36 | -0.026674127961201277 | 68 |
| OIL | Crude Oil | 106.29 | 103.27 | -0.02841283281588114 | 69 |
| SOUTH_KOREA | South Korea Equities | 197.26 | 185.5 | -0.059616749467707564 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | MID_CAP | 25.0 | 0.008975684326760769 | 0.0022439210816901922 | Strong breadth participation with positive 30d benchmark-relative return; supported by Russell 2000 and equal-weight strength signaling rotation away from mega-cap tech. |
| anthropic-claude-opus-4-7 | SMALL_VALUE | 20.0 | 0.014273314032571482 | 0.0028546628065142968 | Housing-related strength (KB Home +16.7%, DRH +6.7%) and falling 10Y yield (4.40%) support small value; at 52w high with positive catalysts. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 20.0 | 0.017479569218008528 | 0.0034959138436017057 | Manufacturing PMI at 55.7 and output at 57.7 (strong expansion); benefits from cyclical rotation visible in Dow outperformance. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 20.0 | 0.0403651362902846 | 0.00807302725805692 | Defensive sector with positive momentum; biotech strength (XBI +7.5% 7d) and low beta provide ballast against tech weakness. |
| anthropic-claude-opus-4-7 | LONG_TREASURY | 15.0 | -0.021286304782359267 | -0.00319294571735389 | 10Y yield dropped to 4.40% from 4.50%; falling oil/gold suggests disinflation impulse benefiting duration into PCE data on 6/25. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | 0.01973192023845982 | 0.004932980059614955 | Strong 30d relative outperformance (+5.2% vs SPX), low volatility, regional bank strength (KRE +4.6% week) and falling yields support financials into quarter-end. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 20.0 | 0.017479569218008528 | 0.0034959138436017057 | Robust manufacturing PMI (55.7) and output index (57.7), strong relative momentum (+6.6% 30d), low drawdown, broad participation. |
| anthropic-claude-opus-4-8 | MID_CAP | 20.0 | 0.008975684326760769 | 0.0017951368653521538 | Broadening rally favors mid-caps; positive weekly return, low drawdown, beneficiary of falling rates and strong retail sales without mega-cap tech drag. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 20.0 | 0.0403651362902846 | 0.00807302725805692 | Defensive low-beta sector with positive weekly (+2.2%) and 30d relative gains; biotech strength (XBI +7.5%) supports the group. |
| anthropic-claude-opus-4-8 | REGIONAL_BANKS | 15.0 | 0.02987697715289994 | 0.004481546572934991 | Falling 10yr yield to 4.40% and steepening dynamics aid regional banks; strongest weekly momentum (+4.6%) with broad up-day participation and at 52w high. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | 0.0024882052607768657 | 0.0009952821043107463 | Micron's strong fiscal Q3 results and Q4 guidance, along with HBM4 production updates, provide a positive catalyst for the semiconductor sector. |
| google-gemini-3-1-pro | SMALL_CAP | 30.0 | 0.008864463031959202 | 0.0026593389095877604 | Small caps have shown recent relative strength and may benefit from a broadening market if mega-cap tech continues to consolidate. |
| google-gemini-3-1-pro | REGIONAL_BANKS | 30.0 | 0.02987697715289994 | 0.008963093145869983 | Regional banks have demonstrated recent momentum and could benefit from a stable rate environment and potential steepening of the yield curve. |
| openai-gpt-5-5 | SEMICONDUCTORS | 50.0 | 0.0024882052607768657 | 0.0012441026303884328 | Micron reported exceptionally strong fiscal Q3 revenue, margins, Q4 guidance, and HBM shipment progress after the entry close context, providing a near-term industry catalyst despite high volatility and reversal risk. |
| openai-gpt-5-5 | BIOTECH | 20.0 | 0.04568833077282752 | 0.009137666154565505 | Biotech has shown strong recent relative strength with high up-day participation and a 52-week high; independent catalyst support is limited, so this is mainly a risk-appetite and momentum allocation. |
| openai-gpt-5-5 | REGIONAL_BANKS | 15.0 | 0.02987697715289994 | 0.004481546572934991 | Regional banks have strong recent relative performance and are at a 52-week high, with broader market breadth favoring smaller and cyclically sensitive shares; support beyond price action is limited. |
| openai-gpt-5-5 | SMALL_VALUE | 15.0 | 0.014273314032571482 | 0.0021409971048857225 | Small-cap value has outperformed recently with lower volatility than broad small caps and benefits if the broadening market breadth continues after large technology weights dragged the cap-weighted S&P 500. |
| xai-grok-4-3 | SMALL_CAP | 30.0 | 0.008864463031959202 | 0.0026593389095877604 | Positive domestic growth signals from PMI and retail sales support small-cap sensitivity over the one-week window. |
| xai-grok-4-3 | BIOTECH | 25.0 | 0.04568833077282752 | 0.01142208269320688 | Recent strength aligns with risk appetite and sector-specific positioning ahead of economic releases. |
| xai-grok-4-3 | REGIONAL_BANKS | 20.0 | 0.02987697715289994 | 0.005975395430579989 | Yield curve stability and domestic economic data favor regional bank exposure in the short term. |
| xai-grok-4-3 | UTILITIES | 15.0 | -0.016908232324272965 | -0.0025362348486409445 | Defensive characteristics provide balance amid inflation and rate datapoints. |
| xai-grok-4-3 | EQUAL_WEIGHT_SP500 | 10.0 | 0.014402509744272374 | 0.0014402509744272374 | Broad participation reduces concentration risk while capturing equity upside. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | FINANCIALS | 5 | 0.55 | 0.01973192023845982 | 0.022778604599560725 | 0.005703690611818312 | 0.0653898986385991 |  | True | True |
| xai-grok-4-3 | SMALL_CAP | 5 | 0.65 | 0.008864463031959202 | 0.018960833159160924 | 0.0018859191714185111 | 0.06920767007899892 |  | True | True |
| openai-gpt-5-5 | SEMICONDUCTORS | 4 | 0.58 | 0.0024882052607768657 | 0.017004312462774653 | -7.060152496776023e-05 | 0.07116419077538519 |  | False | True |
| anthropic-claude-opus-4-7 | MID_CAP | 5 | 0.55 | 0.008975684326760769 | 0.013474579272509224 | -0.003600334715233189 | 0.07469392396565061 |  | False | True |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.65 | 0.0024882052607768657 | 0.012617714159768489 | -0.004457199827973924 | 0.07555078907839134 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 0699b051cc515eb2156c7207329dedd7eaee82ba919a87c4e16d6167fabbf636 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 66320ebc013af445c33450b3005ec684487d06b5bca45c52a3ff9e8e24373e4c |
| manifest.yaml | b9255e4c0f34837a7cbe08d0b05678bc4fea9129ad85d5e8a1a7078b3cd0d3b6 |
| market_data/universe_trailing_returns.csv | 8bb99f56fda6f532d2662d3f0c3c3887bdbbd5b5a41fb3a99caa9b2f47db2060 |
| market_data/universe_trailing_returns.md | 1648c81233bf787f247ad8fdc4ca44688be4feb34160b890a60b435ace1596fe |
| market_data/universe_trailing_returns.json | 0c6fae6055297130af761bbedcbdb4007e68fc4bd90bf56f5641f8af2631c938 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | fe810c6d4999e4a20e62ad16b418f69029733161f84c89ca2a555a24db923955 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 8e5b8c5ff1c00bbfb5e2c8593cd6400df7ee8dd64696e28df2f515aa2a786705 | yes |
| Final briefing | research/final_briefing.md | model-facing | 0699b051cc515eb2156c7207329dedd7eaee82ba919a87c4e16d6167fabbf636 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
