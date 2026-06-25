# CapitalBench Report: CB-2026-05-24-1M / official-20260524

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260524
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench May 24 2026 One-Month Portfolio Round
- Description: One-month CapitalBench portfolio evaluation round using the frozen May 24, 2026 briefing and expanded v2.0 universe.
- Decision date: 2026-05-24
- Decision deadline: 2026-05-25T01:00:00Z
- Horizon: one month
- Entry date: 2026-05-22
- Exit date: 2026-06-24
- Entry rule: Use adjusted close from the last trading close before the decision deadline; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on the exit_date for each selected option; CASH return is 0 unless explicitly priced.
- Options: 65

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SEMICONDUCTORS | 3 | 0.62 | Recent trailing returns favor semiconductors, technology, and Taiwan exposure; these are overweighted to seek alpha versus SP500 in the entry-to-exit window. | Semiconductor concentration could amplify losses on any AI spending slowdown or earnings disappointment; Taiwan exposure carries elevated geopolitical risk that could trigger sharp one-month drawdowns; Rising CPI to 3.8% and low consumer sentiment may pressure growth stocks if rate expectations shift |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.34 | For a one-month contest, recent relative strength and identifiable catalysts favor semiconductors, Taiwan, South Korea, and technology over diversified S&P 500 exposure. The portfolio accepts high volatility to maximize expected alpha versus SPY. | AI and semiconductor leaders could reverse sharply after extreme trailing gains or any disappointment in earnings guidance and capital-spending expectations.; Hot inflation data and high Treasury yields could trigger a growth-stock valuation compression that hurts semiconductors, Taiwan, South Korea, and technology more than SPY.; Cross-strait or regional geopolitical tension could pressure Taiwan and South Korea equities despite strong export fundamentals.; Oil could fall if OPEC+ supply actions, demand concerns, or de-escalation around shipping routes outweigh geopolitical risk premiums. |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 4 | 0.75 | Overweight technology and semiconductors based on strong earnings and momentum, with a small cash buffer. | A sudden reversal in AI sentiment or a miss in upcoming tech earnings could disproportionately impact the portfolio.; Higher-than-expected inflation data could lead to a hawkish shift in Fed expectations, negatively impacting high-valuation growth stocks.; Geopolitical tensions, particularly concerning Taiwan, could disrupt semiconductor supply chains and cause significant sector volatility. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.6 | Concentrate in AI/semiconductor supply chain (SMH, Taiwan) and defense (ITA) which have demonstrated earnings-backed momentum, balanced by gold hedge against re-accelerating inflation, geopolitical risk, and elevated equity valuations. | Semiconductor/AI factor reversal if rates back up further given 10Y at 4.56% and sticky core PCE 3.2%; Taiwan/Korea geopolitical escalation given referenced cross-strait tensions could hit EWT and SMH simultaneously; Oil spike from Hormuz disruption could lift CPI further and pressure growth/tech multiples without benefiting our energy-light book; Consumer sentiment crash to 44.8 may presage recessionary surprise hurting cyclical semis and defense supply chains; Gold pullback if JPM's revised lower forecast ($5,243 vs prior $5,708) signals near-term consolidation after strong run |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 131.5354678534 | 149.71 | 0.1381721024998066 | 1 |
| SOUTH_KOREA | South Korea Equities | 182.03 | 197.26 | 0.08366752733065974 | 2 |
| MOMENTUM | US Momentum Equities | 303.274523705 | 328.41 | 0.08288027621947469 | 3 |
| TAIWAN | Taiwan Equities | 96.84 | 104.72 | 0.0813713341594382 | 4 |
| SEMICONDUCTORS | Semiconductors | 576.32 | 618.92 | 0.07391726818434186 | 5 |
| REGIONAL_BANKS | Regional Banks | 68.9707466561 | 73.97 | 0.0724836773020181 | 6 |
| INDUSTRIALS | Industrials Sector | 171.3514293637 | 180.2100067138672 | 0.051698298538056076 | 7 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 225.2148161768 | 236.19 | 0.048732068384808924 | 8 |
| SMALL_CAP | US Small-Cap Stocks | 284.4489143044 | 296.69 | 0.04303439064105663 | 9 |
| SMALL_VALUE | US Small-Cap Value | 210.5493471237 | 218.59 | 0.038188923338603686 | 10 |
| FINANCIALS | Financials Sector | 51.7596768042 | 53.72 | 0.0378735594353814 | 11 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.3484092022 | 87.37999725341797 | 0.03594125935381487 | 12 |
| MID_CAP | US Mid-Cap Stocks | 73.3176099305 | 75.76 | 0.033312461655736314 | 13 |
| HEALTHCARE | Healthcare Sector | 149.2373456845 | 153.35 | 0.027557809318013993 | 14 |
| US_DOLLAR | US Dollar | 27.77 | 28.53 | 0.02736766294562476 | 15 |
| INDIA | India Equities | 48.39 | 49.630001068115234 | 0.025625151231974286 | 16 |
| LARGE_VALUE | US Large-Cap Value | 235.5841161266 | 241.0 | 0.0229891724554534 | 17 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 205.7846840677 | 210.38 | 0.02233069945471855 | 18 |
| MATERIALS | Materials Sector | 50.1024380968 | 51.15999984741211 | 0.021107989766263602 | 19 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.7682638954 | 96.57 | 0.019012019747334907 | 20 |
| JAPAN | Japan Equities | 91.1246589833 | 92.61000061035156 | 0.016300106289822036 | 21 |
| TECHNOLOGY | Technology Sector | 180.1762845775 | 183.05 | 0.015949465431805532 | 22 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.8927420257 | 107.46 | 0.014800428663180876 | 23 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 107.9606751232 | 109.41000366210938 | 0.013424596847467551 | 24 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.56503646 | 94.7300033569336 | 0.012450878458553527 | 25 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.9462882667 | 48.5 | 0.011548583911646926 | 26 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.1109088889 | 99.19000244140625 | 0.010998711200690403 | 27 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.74861772 | 94.75 | 0.010681568479130377 | 28 |
| UTILITIES | Utilities Sector | 45.0634010019 | 45.540000915527344 | 0.010576208253949781 | 29 |
| LOW_VOL | US Low Volatility Equities | 73.9509633036 | 74.69 | 0.009993604726498795 | 30 |
| REAL_ESTATE | Real Estate Sector | 44.1774883839 | 44.5099983215332 | 0.007526682701916254 | 31 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.5027277598 | 79.8499984741211 | 0.004368035212204191 | 32 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.32103059 | 91.59 | 0.0029453172863058708 | 33 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.2116171812 | 84.44 | 0.00271201084178907 | 34 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.0943577411 | 70.27999877929688 | 0.002648444813241113 | 35 |
| TIPS | Treasury Inflation-Protected Securities | 109.1120854231 | 109.31999969482422 | 0.001905510933257304 | 36 |
| EMERGING_MARKETS | Emerging Markets | 58.9111717427 | 58.970001220703125 | 0.0009986132725396946 | 37 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 38 |
| EUROPE | Europe Equities | 87.2744243543 | 86.94999694824219 | -0.0037173250749928943 | 39 |
| NASDAQ100 | Nasdaq 100 | 716.7498802628 | 710.62 | -0.008552328269036513 | 40 |
| TOTAL_US_MARKET | Total US Stock Market | 366.79 | 363.65 | -0.008560756836336947 | 41 |
| SP500 | S&P 500 | 743.7441207999 | 733.24 | -0.014123299272070566 | 42 |
| CANADA | Canada Equities | 58.2377393099 | 57.29 | -0.016273628082587588 | 43 |
| AUSTRALIA | Australia Equities | 28.3782816099 | 27.91 | -0.016501408236664905 | 44 |
| YEN | Japanese Yen | 57.7 | 56.7 | -0.017331022530329254 | 45 |
| UNITED_KINGDOM | United Kingdom Equities | 46.4207100004 | 45.45 | -0.02091114074712841 | 46 |
| EURO | Euro | 107.0351785465 | 104.77 | -0.021162935188788756 | 47 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.9386664713 | 115.07 | -0.032526566726166495 | 48 |
| DIVIDEND | US Dividend Equities | 32.83 | 31.72 | -0.033810539141029494 | 49 |
| AGRICULTURE | Agriculture Commodities | 27.56 | 26.56 | -0.036284470246734424 | 50 |
| MEXICO | Mexico Equities | 76.6385763726 | 73.79 | -0.03716896251766 | 51 |
| LARGE_GROWTH | US Large-Cap Growth | 124.8927665645 | 119.67 | -0.04181800682430015 | 52 |
| SOUTH_AFRICA | South Africa Equities | 65.9145800702 | 62.18 | -0.056657875484037334 | 53 |
| BRAZIL | Brazil Equities | 36.0260634158 | 33.85 | -0.060402475582320814 | 54 |
| COPPER | Copper | 38.92 | 36.31 | -0.06706063720452204 | 55 |
| CHINA | China Equities | 55.177079864 | 51.43000030517578 | -0.06791007367660606 | 56 |
| COMMUNICATIONS | Communication Services Sector | 115.1542302805 | 106.54 | -0.07480602544532589 | 57 |
| SOFTWARE | Software | 93.9929295534 | 86.17 | -0.08322891509574215 | 58 |
| ENERGY | Energy Sector | 59.0694595392 | 53.56999969482422 | -0.0931015771479371 | 59 |
| GOLD | Gold | 84.81 | 74.98999786376953 | -0.1157882577081768 | 60 |
| BROAD_COMMODITIES | Broad Commodities | 18.2 | 15.779999732971191 | -0.1329670476389455 | 61 |
| BITCOIN_ETF | Bitcoin ETF | 42.96 | 33.87 | -0.21159217877094982 | 62 |
| ETHEREUM_ETF | Ethereum ETF | 15.57 | 11.92 | -0.23442517662170848 | 63 |
| SILVER | Silver | 68.36 | 51.78 | -0.2425394967817437 | 64 |
| OIL | Crude Oil | 140.92 | 106.29 | -0.24574226511495878 | 65 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 35.0 | 0.07391726818434186 | 0.025871043864519647 | Nvidia Q1 FY27 data center revenue +85% YoY confirms AI capex momentum; SMH strong trend (+13.8% 30d, +70% 6m) with Taiwan/Korea supply chain validation. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 20.0 | 0.048732068384808924 | 0.009746413676961786 | $1.5T FY27 defense budget request plus Iran/Hormuz geopolitical tensions provide strong near-term tailwind; ITA showing positive momentum. |
| anthropic-claude-opus-4-7 | TAIWAN | 15.0 | 0.0813713341594382 | 0.01220570012391573 | Q1 GDP +13.7%, exports +35.3% YoY, semiconductor supply chain leverage; strongest 7d return (+6.09%) signals continuation. |
| anthropic-claude-opus-4-7 | GOLD | 15.0 | -0.1157882577081768 | -0.01736823865622652 | Hedge against sticky inflation (CPI 3.8%, PCE 3.5%), geopolitical risk (Hormuz), consumer sentiment collapse to 44.8, and high CAPE 41.6 equity valuations. |
| anthropic-claude-opus-4-7 | MOMENTUM | 15.0 | 0.08288027621947469 | 0.012432041432921204 | Diversified momentum exposure capturing the prevailing trend regime (+8.08% 30d) while reducing single-theme concentration risk. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | 0.07391726818434186 | 0.029566907273736745 | Strong momentum and exceptional revenue growth from key constituents like Nvidia provide a strong tailwind for the sector. |
| google-gemini-3-1-pro | TECHNOLOGY | 30.0 | 0.015949465431805532 | 0.004784839629541659 | Broad technology exposure captures the ongoing AI and software trends while providing some diversification from pure semiconductors. |
| google-gemini-3-1-pro | MOMENTUM | 20.0 | 0.08288027621947469 | 0.016576055243894938 | Momentum factor captures the current market trend favoring large-cap growth and technology names. |
| google-gemini-3-1-pro | SHORT_TREASURY | 10.0 | 0.0029453172863058708 | 0.0002945317286305871 | Provides a small cash-like buffer against potential short-term volatility while earning a modest yield. |
| openai-gpt-5-5 | SEMICONDUCTORS | 40.0 | 0.07391726818434186 | 0.029566907273736745 | Strongest AI-linked equity momentum in the universe, supported by exceptional reported Nvidia data-center revenue growth and high recent relative strength. |
| openai-gpt-5-5 | TAIWAN | 25.0 | 0.0813713341594382 | 0.02034283353985955 | Taiwan combines very strong recent returns with reported double-digit GDP expansion and export growth, giving leveraged exposure to the semiconductor cycle. |
| openai-gpt-5-5 | SOUTH_KOREA | 20.0 | 0.08366752733065974 | 0.016733505466131948 | South Korea has the strongest 6-month and 1-year trailing country returns and offers additional semiconductor/export beta if momentum persists. |
| openai-gpt-5-5 | TECHNOLOGY | 10.0 | 0.015949465431805532 | 0.0015949465431805534 | Broad technology exposure adds liquidity and captures continued growth-stock and AI-related market leadership beyond pure semiconductors. |
| openai-gpt-5-5 | OIL | 5.0 | -0.24574226511495878 | -0.012287113255747939 | Oil provides a small diversifier with upside from elevated crude prices, inflation pressure, OPEC+ uncertainty, and reported Strait of Hormuz disruption. |
| xai-grok-4-3 | SEMICONDUCTORS | 50.0 | 0.07391726818434186 | 0.03695863409217093 | Led 30d returns at 13.80% with strong Nvidia data center growth momentum likely to persist over the next month. |
| xai-grok-4-3 | TECHNOLOGY | 30.0 | 0.015949465431805532 | 0.004784839629541659 | Delivered 12.59% 30d return and benefits from ongoing AI-related demand tailwinds in the scoring window. |
| xai-grok-4-3 | TAIWAN | 20.0 | 0.0813713341594382 | 0.01627426683188764 | Posted 9.93% 30d return alongside 13.7% Q1 GDP expansion and export strength in semiconductors. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SEMICONDUCTORS | 3 | 0.62 | 0.07391726818434186 | 0.05801774055360023 | 0.0721410398256708 | 0.08015436194620637 |  | True | True |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.34 | 0.07391726818434186 | 0.05595107956716086 | 0.07007437883923143 | 0.08222102293264574 |  | True | True |
| google-gemini-3-1-pro | SEMICONDUCTORS | 4 | 0.75 | 0.07391726818434186 | 0.05122233387580393 | 0.0653456331478745 | 0.08694976862400267 |  | True | True |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.6 | 0.07391726818434186 | 0.04288696044209185 | 0.05701025971416242 | 0.09528514205771475 |  | True | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 3b942e49549af897fa853fcdd9a5a85102f640bab95289f725dee250e84e65ca |
| options.yaml | 8e07e0a1d09976c253d8b385fffa546b2e406bbad7499c7fc9f3fe35f15afcb1 |
| prompt.md | dbe426c4ad2eb54404a7145e178c83af737646765cdde4e3bf5e0b70fdf7a7f1 |
| manifest.yaml | 813d15f7d3c973760002aed634bf5b5e4abc0e07367fcfd83a639f0b58debcd6 |
| market_data/universe_trailing_returns.csv | d245d622914ee6a513e8c78e6349288b6038cf91b84bb0547953a8d6f4a45634 |
| market_data/universe_trailing_returns.md | 26c17ed88d4c7c23ee5a9e6340f1dc8a8a2484e6580adb3f992328308cf5613d |
| market_data/universe_trailing_returns.json | 001eb44a6c57f131b78681f8bd0ff0a26d7b48900b110fffa6d86bf53123d7d5 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 1412dae20c9df1d18dc8b9d3e2023d0711049518a427ce5dd497b8a4fa7ac236 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | f74bac477ae64ecf402b905d6756c2e206a92e107b461befa71d455f7c002ced | yes |
| Final briefing | research/final_briefing.md | model-facing | 3b942e49549af897fa853fcdd9a5a85102f640bab95289f725dee250e84e65ca | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
