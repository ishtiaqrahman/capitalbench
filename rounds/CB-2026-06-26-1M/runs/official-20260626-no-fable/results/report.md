# CapitalBench Report: CB-2026-06-26-1M / official-20260626-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260626-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-26-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-06-26
- Decision deadline: 2026-06-27T03:30:00Z
- Horizon: one month
- Entry date: 2026-06-26
- Exit date: 2026-07-24
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.58 | Overweight sectors with current leadership and fundamental catalysts (healthcare regulatory, financials/curve, industrials PMI) plus equal-weight and low-vol to capture market breadth while limiting mega-cap AI drawdown exposure. | AI/semiconductor rebound could cause cap-weighted indexes to outperform this defensive tilt, generating negative alpha vs SPY; Hot June CPI (July 14) or weak jobs report could pressure rate-sensitive financials and broad equities; Healthcare leadership may reverse if EMA catalyst fades or drug-pricing policy headlines emerge; Geopolitical escalation after US strike on Iran could spike volatility and hit cyclicals like industrials and financials |
| openai-gpt-5-5 | openai | portfolio | BIOTECH | 5 | 0.58 | Favor rotation beneficiaries over large-cap growth for the one-month window, anchored by healthcare catalysts and broadening market participation. Add selective cyclical and energy exposure where macro activity and geopolitical facts could matter before exit. | A rapid rebound in AI-linked mega-cap technology or semiconductors would likely cause the portfolio to lag the S&P 500.; Biotech and regional banks have already risen sharply, creating reversal and crowded short-term positioning risk.; July CPI, PPI, employment, or FOMC minutes could push yields higher or revive recession concerns, hurting small caps, banks, and biotech financing sentiment.; Oil prices could keep falling despite geopolitical tension if demand concerns or de-escalation dominate, weighing on the energy allocation. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.6 | Rotate from concentrated AI leadership into broadening sectors with catalysts (healthcare EMA approvals, biotech breakout, regional banks) plus duration hedge as yields ease. | AI/semiconductor rebound could drive cap-weighted indexes higher, leaving equal-weight tilt behind; Hot June CPI on July 14 could lift yields and hurt long Treasuries and rate-sensitive sectors; Iran/Hormuz escalation could spike oil and pressure equity risk appetite broadly; Biotech and regional banks at 52w highs face reversal risk on any credit or clinical disappointment; July FOMC could surprise hawkish, pressuring duration and small/regional exposures |
| xai-grok-4-3 | xai | portfolio | BIOTECH | 4 | 0.55 | Portfolio tilts to sectors with positive catalysts and recent relative strength while avoiding tech/growth areas hit by recent declines and geopolitical oil moves. | Weaker-than-expected June CPI or employment data on July 2/14 could pressure risk assets; Escalation in Iran-related geopolitics may increase volatility before July 24; FOMC minutes on July 8 could shift rate expectations and affect small-cap and bank holdings |
| google-gemini-3-1-pro | google | portfolio | HEALTHCARE | 4 | 0.65 | Overweight healthcare and biotech due to positive regulatory news. Diversify with small caps and equal-weight S&P 500 to mitigate mega-cap tech concentration risk. | Reversal of recent healthcare and biotech momentum if regulatory optimism fades.; Continued weakness in AI and tech stocks dragging down broader market sentiment.; Macroeconomic data, such as upcoming employment or inflation reports, negatively impacting small caps and broader equities.; Geopolitical escalation in the Middle East causing a spike in oil prices and market volatility. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 105.48 | 136.69000244140625 | 0.29588549906528483 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 11.89 | 14.039999961853027 | 0.18082421882699973 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 15.87 | 17.95 | 0.13106490233144297 | 3 |
| ENERGY | Energy Sector | 53.84000015258789 | 59.62 | 0.10735512316179441 | 4 |
| BITCOIN_ETF | Bitcoin ETF | 33.85 | 36.349998474121094 | 0.07385519864464074 | 5 |
| CHINA | China Equities | 50.47999954223633 | 53.33 | 0.05645801274976425 | 6 |
| AGRICULTURE | Agriculture Commodities | 26.8 | 28.239999771118164 | 0.05373133474321512 | 7 |
| FINANCIALS | Financials Sector | 53.56999969482422 | 56.31 | 0.05114803660229472 | 8 |
| DIVIDEND | US Dividend Equities | 32.09000015258789 | 33.29 | 0.037394822116114446 | 9 |
| CYBERSECURITY | Cybersecurity | 85.36 | 88.4 | 0.03561387066541721 | 10 |
| UNITED_KINGDOM | United Kingdom Equities | 45.76 | 47.23 | 0.03212412587412583 | 11 |
| BRAZIL | Brazil Equities | 34.67 | 35.73 | 0.030573983270839156 | 12 |
| COPPER | Copper | 37.33 | 38.349998474121094 | 0.027323827327112138 | 13 |
| AUSTRALIA | Australia Equities | 27.97 | 28.72 | 0.026814444047193353 | 14 |
| LARGE_VALUE | US Large-Cap Value | 242.75999450683594 | 248.24 | 0.022573758515263664 | 15 |
| CANADA | Canada Equities | 57.8 | 59.07 | 0.021972318339100294 | 16 |
| LOW_VOL | US Low Volatility Equities | 75.62049865722656 | 77.19 | 0.020754972139071626 | 17 |
| REAL_ESTATE | Real Estate Sector | 45.2400016784668 | 45.95 | 0.015694038355245077 | 18 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 210.31 | 213.57 | 0.015500927202700687 | 19 |
| EUROPE | Europe Equities | 87.12999725341797 | 88.41 | 0.014690724055219873 | 20 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 236.78 | 240.14 | 0.014190387701664031 | 21 |
| HEALTHCARE | Healthcare Sector | 160.33999633789062 | 162.57 | 0.013907968772869372 | 22 |
| SP500 | S&P 500 | 728.989990234375 | 738.93 | 0.013635317218044563 | 23 |
| INDUSTRIALS | Industrials Sector | 181.1999969482422 | 182.66 | 0.008057412121120766 | 24 |
| REGIONAL_BANKS | Regional Banks | 75.17 | 75.73 | 0.00744978049753886 | 25 |
| TOTAL_US_MARKET | Total US Stock Market | 362.2200012207031 | 364.8 | 0.007122739690249347 | 26 |
| US_DOLLAR | US Dollar | 28.46 | 28.579999923706055 | 0.004216441451372344 | 27 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.36202239990234 | 91.61 | 0.0027142306352658796 | 28 |
| UTILITIES | Utilities Sector | 46.20000076293945 | 46.29 | 0.0019480354020413593 | 29 |
| COMMUNICATIONS | Communication Services Sector | 106.18000030517578 | 106.3 | 0.0011301534609089448 | 30 |
| MEXICO | Mexico Equities | 75.37 | 75.45 | 0.0010614302772986584 | 31 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 32 |
| SMALL_VALUE | US Small-Cap Value | 221.42999267578125 | 221.42 | -4.5127923550492e-05 | 33 |
| EURO | Euro | 105.0198533424 | 104.9469985961914 | -0.0006937235569265399 | 34 |
| SOFTWARE | Software | 88.2 | 87.98 | -0.0024943310657595807 | 35 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.4616470336914 | 79.23 | -0.0029152055405192723 | 36 |
| GOLD | Gold | 76.55999755859375 | 76.23 | -0.004310313076240524 | 37 |
| MID_CAP | US Mid-Cap Stocks | 76.22000122070312 | 75.77 | -0.005903978135609056 | 38 |
| MATERIALS | Materials Sector | 51.599998474121094 | 51.26 | -0.006589117910373865 | 39 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.70999908447266 | 84.13 | -0.006846878653537503 | 40 |
| TIPS | Treasury Inflation-Protected Securities | 108.63938903808594 | 107.5 | -0.010487807858404863 | 41 |
| LARGE_GROWTH | US Large-Cap Growth | 119.04000091552734 | 117.65 | -0.011676754912944842 | 42 |
| YEN | Japanese Yen | 56.71 | 56.040000915527344 | -0.011814478654076144 | 43 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.55999755859375 | 69.71 | -0.01204645107715474 | 44 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.3985039643 | 47.79999923706055 | -0.012366182386152391 | 45 |
| SILVER | Silver | 53.28 | 52.59000015258789 | -0.012950447586563607 | 46 |
| EMERGING_MARKETS | Emerging Markets | 58.58000183105469 | 57.8 | -0.013315155457048644 | 47 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.1397654107 | 94.63999938964844 | -0.015599851056892988 | 48 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 99.0077896118164 | 97.46 | -0.015633008452010544 | 49 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.5906527635 | 93.11000061035156 | -0.015653260759817766 | 50 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.3114946362 | 105.55000305175781 | -0.01641475212337573 | 51 |
| JAPAN | Japan Equities | 92.80000305175781 | 91.21 | -0.017133653011530803 | 52 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.71748352050781 | 93.03 | -0.01781596657540474 | 53 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.11650085449219 | 106.23 | -0.026453385435639687 | 54 |
| TECHNOLOGY | Technology Sector | 181.11000061035156 | 175.88 | -0.02887748104867849 | 55 |
| SMALL_CAP | US Small-Cap Stocks | 299.8299865722656 | 291.17 | -0.028882990228125016 | 56 |
| SOUTH_AFRICA | South Africa Equities | 63.01 | 61.07 | -0.03078876368830341 | 57 |
| INDIA | India Equities | 49.560001373291016 | 48.02 | -0.03107347317631337 | 58 |
| BIOTECH | Biotechnology | 155.38 | 150.48 | -0.03153559016604457 | 59 |
| NASDAQ100 | Nasdaq 100 | 706.52001953125 | 684.23 | -0.03154902750814981 | 60 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.37000274658203 | 109.41 | -0.04336803906153852 | 61 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 87.03854370117188 | 83.25 | -0.043527195424811205 | 62 |
| TAIWAN | Taiwan Equities | 102.81 | 98.01 | -0.04668806536329151 | 63 |
| METALS_MINING | Metals and Mining | 108.01 | 101.74 | -0.058050180538839036 | 64 |
| MOMENTUM | US Momentum Equities | 325.739990234375 | 306.39 | -0.05940317681121188 | 65 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 123.6 | 114.015 | -0.07754854368932029 | 66 |
| BROAD_AI_TECH | Broad AI Technology | 63.1495555341 | 57.98 | -0.08186210481415834 | 67 |
| SEMICONDUCTORS | Semiconductors | 611.61 | 561.19 | -0.08243815503343632 | 68 |
| SOLAR | Solar Energy | 56.85 | 51.28 | -0.09797713280562881 | 69 |
| SOUTH_KOREA | South Korea Equities | 197.28 | 162.96 | -0.17396593673965932 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 30.0 | 0.013907968772869372 | 0.004172390631860812 | EMA approvals catalyst, defensive with strong recent breadth, low beta supports outperformance amid AI/mega-cap weakness. |
| anthropic-claude-opus-4-7 | REGIONAL_BANKS | 20.0 | 0.00744978049753886 | 0.0014899560995077722 | Steeper curve, declining claims, strong Q1 GDP revision, and breakout near 52w highs support continuation through July earnings. |
| anthropic-claude-opus-4-7 | BIOTECH | 15.0 | -0.03153559016604457 | -0.0047303385249066856 | Strong M&A/approval backdrop with EMA catalyst, breaking out at 52w highs with improving sentiment. |
| anthropic-claude-opus-4-7 | EQUAL_WEIGHT_SP500 | 20.0 | 0.015500927202700687 | 0.0031001854405401374 | Broad market participation (2/3 stocks up) favors equal-weight over cap-weighted while AI mega-caps wobble. |
| anthropic-claude-opus-4-7 | LONG_TREASURY | 15.0 | -0.043527195424811205 | -0.006529079313721681 | Yields easing, soft sentiment data, contained inflation expectations, and FOMC minutes catalyst support duration. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.013907968772869372 | 0.004172390631860812 | Healthcare led the market on positive EMA regulatory catalysts, has low beta (0.38) and is near 52w highs; defensive with fundamental support amid AI-stock weakness. |
| anthropic-claude-opus-4-8 | FINANCIALS | 20.0 | 0.05114803660229472 | 0.010229607320458946 | Financials and regional banks show broadening leadership with strong benchmark-relative returns; firming yields and steepening curve plus solid GDP/claims data support. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 15.0 | 0.008057412121120766 | 0.001208611818168115 | Strong flash manufacturing PMI (59-month high output) and cyclical broadening support industrials; positive 30d alpha and near highs. |
| anthropic-claude-opus-4-8 | EQUAL_WEIGHT_SP500 | 20.0 | 0.015500927202700687 | 0.0031001854405401374 | Two-thirds of S&P stocks rose while cap-weighted indexes were dragged by AI names; equal-weight captures the broadening and avoids mega-cap semis concentration risk. |
| anthropic-claude-opus-4-8 | LOW_VOL | 15.0 | 0.020754972139071626 | 0.0031132458208607437 | Low-vol factor (beta 0.08) is near highs with positive alpha; defensive ballast against AI/tech drawdown risk and a heavy macro data calendar. |
| google-gemini-3-1-pro | HEALTHCARE | 40.0 | 0.013907968772869372 | 0.005563187509147749 | Healthcare stocks showed strong upward momentum following positive European Medicines Agency recommendations, providing a near-term catalyst. |
| google-gemini-3-1-pro | BIOTECH | 30.0 | -0.03153559016604457 | -0.009460677049813371 | Biotech benefits from the same positive regulatory catalysts as broader healthcare, with strong recent performance and high beta for potential outperformance. |
| google-gemini-3-1-pro | SMALL_CAP | 15.0 | -0.028882990228125016 | -0.004332448534218753 | Small caps have shown resilience and positive year-to-date performance, offering diversification away from mega-cap tech weakness. |
| google-gemini-3-1-pro | EQUAL_WEIGHT_SP500 | 15.0 | 0.015500927202700687 | 0.002325139080405103 | Equal-weight S&P 500 reduces concentration risk in mega-cap tech stocks, which have recently weighed on cap-weighted indexes. |
| openai-gpt-5-5 | BIOTECH | 30.0 | -0.03153559016604457 | -0.009460677049813371 | Biotech has strong recent relative strength, and the briefing provides independent healthcare support from EMA medicine recommendations; it can benefit from continued rotation into healthcare during a weak AI-linked tape. |
| openai-gpt-5-5 | REGIONAL_BANKS | 25.0 | 0.00744978049753886 | 0.001862445124384715 | Regional banks have led recently as market breadth improved and domestic cyclical risk appetite broadened; supportive macro data include better PMI, strong income and spending, and lower jobless claims, though support beyond price action is limited. |
| openai-gpt-5-5 | SMALL_VALUE | 20.0 | -4.5127923550492e-05 | -9.025584710098401e-06 | Small-cap value offers exposure to the broadening away from cap-weighted AI leaders, with Russell 2000 strength and nearly two-thirds of S&P 500 constituents rising despite index weakness. |
| openai-gpt-5-5 | HEALTHCARE | 15.0 | 0.013907968772869372 | 0.002086195315930406 | Healthcare was specifically cited as a strong upward force on June 26 after European regulatory recommendations, with lower beta than the benchmark and potential defensive appeal before July macro data. |
| openai-gpt-5-5 | ENERGY | 10.0 | 0.10735512316179441 | 0.010735512316179441 | Energy provides exposure to geopolitical and inventory-tightness risk after low crude inventories and a U.S.-Iran escalation, while using equities rather than direct oil to reduce commodity futures volatility. |
| xai-grok-4-3 | BIOTECH | 30.0 | -0.03153559016604457 | -0.009460677049813371 | Strong 30-day outperformance and positive EMA recommendations for medicines support near-term gains before July 24 exit. |
| xai-grok-4-3 | HEALTHCARE | 25.0 | 0.013907968772869372 | 0.003476992193217343 | Sector led market gains on June 26 with favorable regulatory news and defensive characteristics amid mixed macro data. |
| xai-grok-4-3 | SMALL_VALUE | 25.0 | -4.5127923550492e-05 | -1.1281980887623e-05 | Domestic small-value exposure benefits from improving consumer sentiment and low unemployment claims over the one-month window. |
| xai-grok-4-3 | REGIONAL_BANKS | 20.0 | 0.00744978049753886 | 0.0014899560995077722 | Recent strength in regional banks aligns with stable rates and positive GDP revision likely to support credit conditions before exit. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.58 | 0.013907968772869372 | 0.021824041031888754 | 0.008188723813844192 | 0.2740614580333961 |  | True | True |
| openai-gpt-5-5 | BIOTECH | 5 | 0.58 | -0.03153559016604457 | 0.005214450121971093 | -0.00842086709607347 | 0.29067104894331375 |  | False | True |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.6 | 0.013907968772869372 | -0.0024968856667196447 | -0.016132202884764208 | 0.29838238473200446 |  | False | False |
| xai-grok-4-3 | BIOTECH | 4 | 0.55 | -0.03153559016604457 | -0.004505010737975879 | -0.01814032795602044 | 0.3003905098032607 |  | False | False |
| google-gemini-3-1-pro | HEALTHCARE | 4 | 0.65 | 0.013907968772869372 | -0.0059047989944792725 | -0.019540116212523835 | 0.3017902980597641 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 1c9ea285a309fc37909ee033f834dd0ec72df267f2f661e2a332c29432fe5bb5 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 7858eef0aa73ea38b28daacc4aaa57e57b110de6456378f1697ff1cd79ca213c |
| manifest.yaml | b22c258a84e92ccbcf16cb0ebd9f0cadfdc2f87c3ab3009d6a632edef57ea9b0 |
| market_data/universe_trailing_returns.csv | 6e4b3cd4b1284abbd59faf5ff3d1c7eece182b1c3b26a5b7306b2a0aeafb414c |
| market_data/universe_trailing_returns.md | 95fb16347d221c8413bcfc8147edae69c474ee549438610e0bbdb0ecbc3185c8 |
| market_data/universe_trailing_returns.json | 350fce324d33007f47dbd4ccf216efc206721e0e127bdb93e8ae473ceaec186a |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 323cf0a0134355cc5a58a844e8473570cc2375f1c4bb7a894c5997f403a6de79 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | d808f67f0f680bf0baec85b279dffa5d3884ddd51abea33252648f64f41c3a5a | yes |
| Final briefing | research/final_briefing.md | model-facing | 1c9ea285a309fc37909ee033f834dd0ec72df267f2f661e2a332c29432fe5bb5 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
