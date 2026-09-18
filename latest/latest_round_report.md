# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-08-15-1M
- Decision deadline: 2026-08-17T13:25:00Z
- Horizon: one month
- Official run ID: official-v3-20260815-monthly-clean
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | YEN | 3 | 0.65 | The market is showing mixed signals with recent inflation data coming in soft (CPI +0.1%, PPI unchanged) and retail sales falling 0.6%, suggesting a cooling economy. However, the S&P 500 recently hit an all-time high, and the Fed held rates steady at 3.50%-3.75%. This environment favors a balanced approach, looking for opportunities in both defensive and cyclical sectors depending on specific asset dynamics. | Inflation data could reverse course, leading to higher yields and negatively impacting LONG_TREASURY.; A broader market sell-off could disproportionately affect SMALL_VALUE stocks.; YEN's reversal may not materialize if interest rate differentials remain wide. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 1 | 0.5 | SPY near all-time highs after +13.7% YTD, with cooling labor market (-23k payrolls, downward revisions), sticky inflation (CPI 3.4%, core PCE 3.3%), and a hawkish-hold FOMC. High cross-sectional dispersion with energy/commodities/foreign strong and rate-sensitive defensives weak. The monthly window includes CPI, PPI, jobs, and a Sept 16 FOMC decision, all high-variance catalysts. Few candidates show durable, supported edge over SPY; most extreme moves lack independent in-window support, so a SPY-heavy stance is warranted. | Sept 16 FOMC decision and CPI/PPI/jobs prints could sharply reprice both equities and rate-sensitive assets within the window; Elevated volatility in commodity and thematic names (oil 54%, semis 54%) can produce large realized deviations in either direction; Cooling labor market and slowing GDP (1.5%) raise recession/risk-off potential that could hurt cyclicals and small caps |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Energy and select tech show relative strength amid mixed macro data on labor, inflation, and GDP; broad equities stable but with reversal candidates in rate-sensitive and commodity areas. | Labor market revisions and weak payrolls; Inflation persistence above target; FOMC policy uncertainty in window; Commodity volatility from inventories |
| xai-grok-4-5 | xai | portfolio | SP500 | 1 | 0.5 | SPY near highs with solid ISM/PMI and mixed labor; sticky CPI/PPI and elevated long yields keep rate-sensitive assets pressured while energy/oil show independent strength; one-month path hinges on Sept FOMC/CPI with limited clean reversal catalysts versus continuation in medium-strength names. | September FOMC decision and SEP could reprice the long end and hit duration/rate-sensitive equities; August CPI/PPI prints may reinforce sticky inflation and pressure risk assets; Oil/energy continuation can reverse sharply on supply or demand headlines given 50%+ horizon vol; Soft labor revisions and weak retail sales could widen equity drawdowns if growth fears reaccelerate |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | SPY is near a fresh high with solid YTD gains while yields rose into a still-elevated inflation print, a divided FOMC hold, and a September FOMC inside the window. Breadth is mixed rather than one-way: equal-weight slightly led recently, oil and some cyclicals were strong, while duration, EM, solar, and crypto lagged. One-month edge versus SPY looks limited. | September 15-16 FOMC, SEP, and press conference can reprice duration, growth, and high-beta equities inside the window.; August CPI/PPI and the jobs report can extend the energy-driven inflation surprise already in the July CPI.; Soft July payrolls and downward revisions raise recession-scare risk for cyclicals if follow-through data weaken.; Oil’s high vol and negative equity beta can reverse quickly if the recent crude spike fades. |
| anthropic-claude-opus-5 | anthropic | portfolio | SMALL_CAP | 3 | 0.555 | S&P 500 at all-time highs with breadth improving (RSP > SPY over 5 sessions, Russell 2000 +23.6% YTD). Macro is mixed: payrolls negative with downward revisions, GDP slowing to 1.5%, but ISM manufacturing and services both expanding and core CPI at 2.5% y/y. Long-end yields rose and are at 5.25% at 20-30y, so duration and rate-sensitive defensives lack support. A September 16 FOMC with SEP falls inside the window and is the dominant swing factor; a weak August payroll print (Sept 4) could push cuts back onto the table, supporting small caps and rate-sensitive equity. Energy/oil just spiked sharply and precious metals/mining ran hot, arguing against fresh continuation entries at extended levels. Overall few high-conviction non-SPY overreaction cases; benchmark exposure dominates. | A hawkish September 16 FOMC or upside August CPI on Sept 11 would hit small caps and rate-sensitive equity harder than SPY; Continued payroll weakness could shift leadership to mega-cap defensives, causing small caps to underperform on growth fear rather than benefit from cut odds; Elevated long-end yields at 5.25% keep pressure on real estate and small-cap financing conditions; Mega-cap tech concentration means SPY can outrun broad-market candidates on a narrow AI-led rally; Oil at $88.52 Brent sustaining higher energy costs could re-accelerate inflation and delay easing |
| openai-gpt-5-6-sol | openai | portfolio | SMALL_VALUE | 3 | 0.57 | Broad participation and solid business surveys favor selective equity exposure, but weak payrolls, soft retail sales, elevated inflation, and an unusually consequential FOMC meeting create substantial reversal risk. Quality pullbacks offer better one-month setups than extreme momentum or structurally weak losers. | August CPI or PPI reaccelerates and pushes long yields higher before the FOMC; The September FOMC delivers a hawkish hold or rate increase, hurting real estate and utilities; Weak payrolls and retail sales develop into a sharper growth scare that pressures small-value earnings; Mega-cap technology leadership resumes, causing SPY to outperform broader and defensive exposures |
| anthropic-claude-fable-5 | anthropic | portfolio | SMALL_VALUE | 3 | 0.57 | SPY near all-time highs after soft July payrolls (-23k) and downward revisions, with a September 16 FOMC inside the window that likely tilts dovish given cooling labor data and moderating core CPI. Rate-sensitive and quality pullback assets (utilities, real estate, small value) have room to recover; extended high-vol names (oil, semis, cyber) face reversal risk after large prior runs. | Hot August CPI (Sep 11) or hawkish Sep 16 FOMC would hurt rate-sensitive picks; Energy-driven inflation (gasoline +24.6% y/y, Brent $88) could push yields higher; Small-cap reversal if labor-market weakness broadens into growth fears; Utilities/real estate edge is modest; picks may simply track SPY minus fees |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.4 | 18.47 | 0.2826388888888889 | 1 |
| OIL | Crude Oil | 130.29 | 155.31 | 0.19203315680405253 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 36.42 | 43.3 | 0.18890719384953303 | 3 |
| BRAZIL | Brazil Equities | 33.97 | 37.74 | 0.1109802767147483 | 4 |
| BROAD_COMMODITIES | Broad Commodities | 18.21 | 19.71 | 0.08237232289950569 | 5 |
| CYBERSECURITY | Cybersecurity | 97.79 | 101.66 | 0.039574598629716684 | 6 |
| SOFTWARE | Software | 101.99 | 105.78 | 0.03716050593195419 | 7 |
| ENERGY | Energy Sector | 62.58 | 64.48 | 0.030361137743688094 | 8 |
| TAIWAN | Taiwan Equities | 107.8 | 110.64 | 0.026345083487940624 | 9 |
| YEN | Japanese Yen | 57.53 | 58.76 | 0.02138014948722411 | 10 |
| COMMUNICATIONS | Communication Services Sector | 110.82 | 112.35 | 0.01380617217108826 | 11 |
| HEALTHCARE | Healthcare Sector | 167.05 | 168.81 | 0.010535767734211277 | 12 |
| US_DOLLAR | US Dollar | 28.1 | 28.38 | 0.009964412811387824 | 13 |
| AGRICULTURE | Agriculture Commodities | 28.14 | 28.42 | 0.00995024875621886 | 14 |
| SOUTH_AFRICA | South Africa Equities | 68.19 | 68.69 | 0.00733245343892075 | 15 |
| BROAD_AI_TECH | Broad AI Technology | 64.0 | 64.37 | 0.005781250000000071 | 16 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 81.35 | 81.78 | 0.005285802089735725 | 17 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 18 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.55 | 91.53 | -0.00021845985800106327 | 19 |
| JAPAN | Japan Equities | 98.17 | 97.91 | -0.0026484669450952403 | 20 |
| UNITED_KINGDOM | United Kingdom Equities | 48.16 | 47.95 | -0.0043604651162789665 | 21 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.7 | 105.16 | -0.005108798486281985 | 22 |
| EMERGING_MARKETS | Emerging Markets | 60.39 | 59.91 | -0.007948335817188346 | 23 |
| BIOTECH | Biotechnology | 159.53 | 158.25 | -0.00802356923462677 | 24 |
| MEXICO | Mexico Equities | 74.91 | 74.29 | -0.008276598584968542 | 25 |
| EURO | Euro | 106.86 | 105.91 | -0.008890136627362932 | 26 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.25 | 96.33 | -0.009460154241645258 | 27 |
| TIPS | Treasury Inflation-Protected Securities | 106.77 | 105.71 | -0.009927882363959917 | 28 |
| SILVER | Silver | 59.57 | 58.97 | -0.010072183985227467 | 29 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.7 | 93.66 | -0.010982048574445735 | 30 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.61 | 78.72 | -0.011179500062806214 | 31 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.65 | 47.11 | -0.011332633788037727 | 32 |
| DIVIDEND | US Dividend Equities | 34.29 | 33.89 | -0.011665208515602155 | 33 |
| COPPER | Copper | 40.13 | 39.66 | -0.011711936207326357 | 34 |
| TECHNOLOGY | Technology Sector | 190.32 | 188.06 | -0.011874737284573333 | 35 |
| SP500 | S&P 500 | 772.67 | 762.6 | -0.013032730661213687 | 36 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.05 | 91.81 | -0.013326168726491061 | 37 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.68 | 83.49 | -0.014052905054322329 | 38 |
| AUSTRALIA | Australia Equities | 29.55 | 29.13 | -0.014213197969543234 | 39 |
| SOUTH_KOREA | South Korea Equities | 185.1 | 182.39 | -0.014640734737979555 | 40 |
| LARGE_VALUE | US Large-Cap Value | 256.62 | 252.82 | -0.014807887148312715 | 41 |
| GOLD | Gold | 83.11 | 81.69 | -0.017085789916977512 | 42 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.84 | 91.25 | -0.017126238690219786 | 43 |
| NASDAQ100 | Nasdaq 100 | 729.87 | 716.92 | -0.017742885719374768 | 44 |
| TOTAL_US_MARKET | Total US Stock Market | 382.13 | 375.34 | -0.017768822128594985 | 45 |
| LARGE_GROWTH | US Large-Cap Growth | 125.08 | 122.53 | -0.020386952350495702 | 46 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.69 | 72.15 | -0.020898357986158134 | 47 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.56 | 103.16 | -0.022735884804850337 | 48 |
| CANADA | Canada Equities | 62.18 | 60.41 | -0.028465744612415578 | 49 |
| MATERIALS | Materials Sector | 52.24 | 50.71 | -0.02928790199081166 | 50 |
| FINANCIALS | Financials Sector | 57.58 | 55.88 | -0.02952414032650219 | 51 |
| EUROPE | Europe Equities | 92.1 | 89.37 | -0.029641693811074843 | 52 |
| INDIA | India Equities | 49.58 | 48.01 | -0.031665994352561566 | 53 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.79 | 213.31 | -0.0338783459395805 | 54 |
| LOW_VOL | US Low Volatility Equities | 75.74 | 73.06 | -0.03538420913651963 | 55 |
| REAL_ESTATE | Real Estate Sector | 44.83 | 42.94 | -0.04215926834708905 | 56 |
| SMALL_VALUE | US Small-Cap Value | 226.46 | 216.73 | -0.04296564514704593 | 57 |
| CHINA | China Equities | 55.06 | 52.67 | -0.043407192154013785 | 58 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.75 | 111.39 | -0.045910064239828685 | 59 |
| MOMENTUM | US Momentum Equities | 322.07 | 306.12 | -0.049523395535132075 | 60 |
| SEMICONDUCTORS | Semiconductors | 594.07 | 560.61 | -0.05632332890063463 | 61 |
| UTILITIES | Utilities Sector | 44.18 | 41.69 | -0.056360344047080124 | 62 |
| METALS_MINING | Metals and Mining | 118.1 | 111.32 | -0.05740897544453849 | 63 |
| REGIONAL_BANKS | Regional Banks | 77.39 | 72.74 | -0.06008528233621924 | 64 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 130.47 | 122.52 | -0.06093354794205563 | 65 |
| SMALL_CAP | US Small-Cap Stocks | 304.06 | 285.43 | -0.0612708018154311 | 66 |
| MID_CAP | US Mid-Cap Stocks | 78.48 | 73.21 | -0.06715086646279322 | 67 |
| SOLAR | Solar Energy | 50.92 | 46.36 | -0.08955223880597019 | 68 |
| INDUSTRIALS | Industrials Sector | 186.32 | 169.01 | -0.09290468012022324 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 251.2 | 213.88 | -0.14856687898089171 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | portfolio | YEN | 3 | 0.65 | 0.02138014948722411 | -0.0035566104921778367 | 0.00947612016903585 | 0.2861954993810667 |  | True | False |
| anthropic-claude-opus-4-8 | portfolio | SP500 | 1 | 0.5 | -0.013032730661213687 | -0.013032730661213687 | 0.0 | 0.29567161955010257 |  | False | False |
| xai-grok-4-3 | portfolio | SP500 | 1 | 0.5 | -0.013032730661213687 | -0.013032730661213687 | 0.0 | 0.29567161955010257 |  | False | False |
| xai-grok-4-5 | portfolio | SP500 | 1 | 0.5 | -0.013032730661213687 | -0.013032730661213687 | 0.0 | 0.29567161955010257 |  | False | False |
| xai-grok-4-6 | portfolio | SP500 | 1 | 0.5 | -0.013032730661213687 | -0.013032730661213687 | 0.0 | 0.29567161955010257 |  | False | False |
| anthropic-claude-opus-5 | portfolio | SMALL_CAP | 3 | 0.555 | -0.0612708018154311 | -0.04039257563523106 | -0.027359844974017375 | 0.32303146452411996 |  | False | False |
| openai-gpt-5-6-sol | portfolio | SMALL_VALUE | 3 | 0.57 | -0.04296564514704593 | -0.04670182293707127 | -0.033669092275857584 | 0.32934071182596014 |  | False | False |
| anthropic-claude-fable-5 | portfolio | SMALL_VALUE | 3 | 0.57 | -0.04296564514704593 | -0.04741187672207083 | -0.034379146060857145 | 0.3300507656109597 |  | False | False |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1M has no scored official run.
- Round CB-2026-08-18-1M has no scored official run.
- Round CB-2026-08-19-1M has no scored official run.
- Round CB-2026-08-20-1M has no scored official run.
- Round CB-2026-08-21-1M has no scored official run.
- Round CB-2026-08-23-1M has no scored official run.
- Round CB-2026-08-24-1M has no scored official run.
- Round CB-2026-08-25-1M has no scored official run.
- Round CB-2026-08-26-1M has no scored official run.
- Round CB-2026-08-27-1M has no scored official run.
- Round CB-2026-08-30-1M has no scored official run.
- Round CB-2026-09-01-1M has no scored official run.
- Round CB-2026-09-02-1M has no scored official run.
- Round CB-2026-09-03-1M has no scored official run.
- Round CB-2026-09-04-1M has no scored official run.
- Round CB-2026-09-09-1M has no scored official run.
- Round CB-2026-09-10-1M has no scored official run.
- Round CB-2026-09-11-1M has no scored official run.
- Round CB-2026-09-13-1M has no scored official run.
- Round CB-2026-09-15-1M has no scored official run.
- Round CB-2026-09-16-1M has no scored official run.
- Round example-round has no scored official run.
- Round example-round-2 has no scored official run.
