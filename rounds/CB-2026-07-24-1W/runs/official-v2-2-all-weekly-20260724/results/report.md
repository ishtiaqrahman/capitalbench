# CapitalBench Report: CB-2026-07-24-1W / official-v2-2-all-weekly-20260724

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-weekly-20260724
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-24-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-24
- Decision deadline: 2026-07-25T23:30:00Z
- Horizon: one week
- Entry date: 2026-07-24
- Exit date: 2026-07-31
- Entry rule: Use adjusted close prices on Friday, July 24, 2026 as the one-week entry snapshot, calculated after regular trading ends and supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Friday, July 31, 2026 as the one-week exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | openai | portfolio | COMMUNICATIONS | 5 | 0.6 | Each active holding has a base forecast above SPY's 0.4% forecast. The weighted base return is 0.9775%, implying 0.5775 percentage point of expected alpha. | A hawkish FOMC decision or rate increase could pressure software and communication-services valuations.; Mega-cap earnings disappointments could overwhelm the anticipated rebound in growth exposures.; Tariff escalation could lift inflation expectations, weaken risk appetite, and raise Treasury yields.; The recent defensive and value rotation could reverse abruptly in favor of benchmark mega-caps. |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.55 | SPY base 0.5; selected holdings exceed it with 20% each in energy, financials, healthcare for weighted 0.78 expected return. | FOMC outcome volatility on July 29; Tariff implementation uncertainty; Oil price reversal after sharp drop |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 4 | 0.55 | SPY faces a two-sided week: 38% implied odds of a hike, fresh tariffs, and mega-cap reports, against very strong Q2 earnings growth. Diversifying into healthcare, financials, and energy — all with positive prior active returns, shallow drawdowns, and low SPY correlation — offers modest expected alpha with lower event risk. | Hawkish FOMC hike on July 29 pressures all equity clusters simultaneously; Crude gives back its post-war premium, hitting the energy sleeve; Mega-cap earnings beats drive cap-weighted SPY ahead of defensive sectors; New tariff round dampens cyclical and consumer-linked earnings guidance |
| xai-grok-4-5 | xai | portfolio | ENERGY | 4 | 0.58 | SPY base is modest given recent weekly decline and event risk; higher-base alternatives in energy and cyclicals/defensives are favored for the short horizon. Allocations stay diversified across four clusters and sum to 100%. | Sharp post-FOMC equity rally favoring mega-cap growth/tech would reverse relative value and energy leadership; Further crude oil decline below recent settlement could pressure ENERGY allocation; Tariff pass-through or hotter PCE could lift yields and hit rate-sensitive and cyclical names; Concentrated earnings misses from large reporters could drive broad risk-off |
| anthropic-claude-opus-4-8 | anthropic | portfolio | INDUSTRIALS | 3 | 0.55 | Industrials and financials show the best combination of recent relative strength, low volatility, and shallow drawdown while tech remains under pressure; SPY provides the core anchor. | FOMC surprise hike (38% implied) roiling rates and equities; Mega-cap earnings misses dragging the broad index; Tariff round pass-through hitting cyclicals |
| google-gemini-3-1-pro | google | portfolio | UTILITIES | 4 | 0.65 | An equal-weight allocation across four distinct sectors to navigate FOMC risks and mega-cap earnings. | Hawkish FOMC surprise negatively impacting rate-sensitive sectors like Utilities.; Earnings misses from major Communications constituents dragging down the broader market.; A sudden resurgence in mega-cap tech growth reversing the recent value rotation. |
| anthropic-claude-fable-5 | anthropic | portfolio | ENERGY | 5 | 0.6 | Energy plus defensive value/low-vol/healthcare/utilities barbell to capture the oil shock and hedge FOMC hike risk versus a rate-sensitive, growth-heavy SPY. | Dovish FOMC surprise triggering a growth/mega-cap rally that lifts SPY above defensives; Sharp oil price reversal on geopolitical de-escalation; Strong Microsoft/Amazon/Meta/Apple earnings driving tech-led SPY outperformance; Tariff pass-through fears hitting cyclical value and energy demand expectations |
| openai-gpt-5-5 | openai | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.58 | Selected holdings all have base forecasts above SPY and span diversified US equity, healthcare, financials, energy, and rate-sensitive defensive clusters. The expected edge comes from breadth, defensive balance, and sector-specific momentum into FOMC, GDP/PCE, ECI, and major earnings. | Mega-cap technology earnings lead SPY sharply higher and reverse recent breadth improvement.; FOMC communication or inflation data pushes yields higher, hurting utilities and defensive equities.; Oil continues the July 24 reversal, pressuring energy exposure.; Tariff pass-through concerns or weak GDP data trigger broad risk-off selling across equities. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOFTWARE | Software | 87.9800033569336 | 94.58 | 0.07501700831142633 | 1 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 109.41000366210938 | 116.09 | 0.06105471267984264 | 2 |
| CHINA | China Equities | 53.33000183105469 | 55.8 | 0.04631535878753712 | 3 |
| SOUTH_AFRICA | South Africa Equities | 61.06999969482422 | 63.62 | 0.04175536790434764 | 4 |
| CYBERSECURITY | Cybersecurity | 88.4000015258789 | 91.83 | 0.03880088704655704 | 5 |
| INDIA | India Equities | 48.02000045776367 | 49.8 | 0.03706787849371085 | 6 |
| COPPER | Copper | 38.349998474121094 | 39.56 | 0.03155154039172725 | 7 |
| YEN | Japanese Yen | 56.040000915527344 | 57.66 | 0.028907906102902725 | 8 |
| BRAZIL | Brazil Equities | 35.72999954223633 | 36.65 | 0.025748683726573907 | 9 |
| UNITED_KINGDOM | United Kingdom Equities | 47.22999954223633 | 48.41 | 0.02498413019691914 | 10 |
| EUROPE | Europe Equities | 88.41000366210938 | 90.59 | 0.024657801692015147 | 11 |
| AUSTRALIA | Australia Equities | 28.719999313354492 | 29.34 | 0.021587768156986487 | 12 |
| COMMUNICATIONS | Communication Services Sector | 106.30000305175781 | 108.24 | 0.01825020595058291 | 13 |
| MEXICO | Mexico Equities | 75.44999694824219 | 76.81 | 0.018025223416387348 | 14 |
| EMERGING_MARKETS | Emerging Markets | 57.79999923706055 | 58.75 | 0.01643599957576347 | 15 |
| BROAD_AI_TECH | Broad AI Technology | 57.97999954223633 | 58.89 | 0.015695075283689297 | 16 |
| EURO | Euro | 104.94999694824219 | 106.49 | 0.014673683625901157 | 17 |
| LARGE_VALUE | US Large-Cap Value | 248.24000549316406 | 251.82000732421875 | 0.014421534611000819 | 18 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.70999908447266 | 70.62 | 0.01305409449833217 | 19 |
| JAPAN | Japan Equities | 91.20999908447266 | 92.39 | 0.012937188108449682 | 20 |
| FINANCIALS | Financials Sector | 56.310001373291016 | 56.94 | 0.011188041401963167 | 21 |
| SP500 | S&P 500 | 738.9299926757812 | 747.030029296875 | 0.010961845778870494 | 22 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.12999725341797 | 85.05 | 0.010935490034675421 | 23 |
| TOTAL_US_MARKET | Total US Stock Market | 364.79998779296875 | 368.2099914550781 | 0.009347598070766905 | 24 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 114.01499938964844 | 115.07 | 0.00925317384553992 | 25 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.57000732421875 | 215.01 | 0.006742485491397776 | 26 |
| LARGE_GROWTH | US Large-Cap Growth | 117.6500015258789 | 118.31999969482422 | 0.005694841991123356 | 27 |
| NASDAQ100 | Nasdaq 100 | 684.22998046875 | 687.989990234375 | 0.005495242642026721 | 28 |
| CANADA | Canada Equities | 59.06999969482422 | 59.39 | 0.005417306701015923 | 29 |
| DIVIDEND | US Dividend Equities | 33.290000915527344 | 33.47 | 0.005407001487605756 | 30 |
| REGIONAL_BANKS | Regional Banks | 75.7300033569336 | 76.06 | 0.00435754164054436 | 31 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.2300033569336 | 79.48 | 0.0031553279373239818 | 32 |
| ETHEREUM_ETF | Ethereum ETF | 14.039999961853027 | 14.07 | 0.002136754859578538 | 33 |
| TIPS | Treasury Inflation-Protected Securities | 107.5 | 107.63 | 0.0012093023255812518 | 34 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.55000305175781 | 105.64 | 0.0008526475190915317 | 35 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.61000061035156 | 91.68000030517578 | 0.0007641053854148261 | 36 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.63999938964844 | 94.66 | 0.00021133358495939447 | 37 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.2300033569336 | 106.25 | 0.00018823912674847953 | 38 |
| SMALL_CAP | US Small-Cap Stocks | 291.1700134277344 | 291.20001220703125 | 0.00010302839548526066 | 39 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 40 |
| HEALTHCARE | Healthcare Sector | 162.57000732421875 | 162.55 | -0.00012306897531744188 | 41 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.79999923706055 | 47.77 | -0.0006275991117021817 | 42 |
| GOLD | Gold | 76.2300033569336 | 76.17 | -0.0007871356984288091 | 43 |
| SMALL_VALUE | US Small-Cap Value | 221.4199981689453 | 221.24 | -0.0008129264313694318 | 44 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.02999877929688 | 92.95 | -0.0008599245441963665 | 45 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.45999908447266 | 97.37 | -0.0009234463915256397 | 46 |
| ENERGY | Energy Sector | 59.619998931884766 | 59.55 | -0.0011740847557669687 | 47 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 240.13999938964844 | 239.66 | -0.0019988314769235904 | 48 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.11000061035156 | 92.92 | -0.0020406036849540676 | 49 |
| TECHNOLOGY | Technology Sector | 175.8800048828125 | 175.35 | -0.003013445918230717 | 50 |
| SILVER | Silver | 52.59000015258789 | 52.36 | -0.004373457918245949 | 51 |
| MID_CAP | US Mid-Cap Stocks | 75.7699966430664 | 75.2699966430664 | -0.006598918069844695 | 52 |
| METALS_MINING | Metals and Mining | 101.73999786376953 | 100.65 | -0.010713562872578741 | 53 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.25 | 82.25 | -0.012012012012011963 | 54 |
| LOW_VOL | US Low Volatility Equities | 77.19000244140625 | 76.23 | -0.012436875385966828 | 55 |
| US_DOLLAR | US Dollar | 28.579999923706055 | 28.17 | -0.014345693659921 | 56 |
| TAIWAN | Taiwan Equities | 98.01000213623047 | 96.55 | -0.014896460610225426 | 57 |
| INDUSTRIALS | Industrials Sector | 182.66000366210938 | 179.84 | -0.015438539393253903 | 58 |
| MATERIALS | Materials Sector | 51.2599983215332 | 50.43 | -0.01619193032990285 | 59 |
| REAL_ESTATE | Real Estate Sector | 45.95000076293945 | 45.07 | -0.019151267645880155 | 60 |
| BITCOIN_ETF | Bitcoin ETF | 36.349998474121094 | 35.64 | -0.01953228346423641 | 61 |
| BROAD_COMMODITIES | Broad Commodities | 17.950000762939453 | 17.56 | -0.02172706107871991 | 62 |
| MOMENTUM | US Momentum Equities | 306.3900146484375 | 299.59 | -0.022193982582102367 | 63 |
| BIOTECH | Biotechnology | 150.47999572753906 | 147.01 | -0.023059515058877933 | 64 |
| AGRICULTURE | Agriculture Commodities | 28.239999771118164 | 27.51 | -0.025849850461569512 | 65 |
| SOUTH_KOREA | South Korea Equities | 162.9600067138672 | 157.1 | -0.03595978444058645 | 66 |
| SEMICONDUCTORS | Semiconductors | 561.1900024414062 | 540.53 | -0.03681463025272513 | 67 |
| SOLAR | Solar Energy | 51.279998779296875 | 49.33 | -0.03802649816138737 | 68 |
| UTILITIES | Utilities Sector | 46.290000915527344 | 44.35 | -0.04190971866834847 | 69 |
| OIL | Crude Oil | 136.69000244140625 | 129.17 | -0.055015014317742805 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 25.0 | -0.0011740847557669687 | -0.00029352118894174217 | Oil supply shock intact (Brent $96.78, up from ~$72 pre-Iran war); energy equities lag crude's move and have positive prior-16s active return of 6.30%. |
| anthropic-claude-fable-5 | LARGE_VALUE | 25.0 | 0.014421534611000819 | 0.0036053836527502048 | Value near 52w high, low vol, positive prior active trend; hike risk and hot headline inflation favor value over growth. |
| anthropic-claude-fable-5 | LOW_VOL | 20.0 | -0.012436875385966828 | -0.002487375077193366 | Defensive factor at 52w high with negative SPY beta; hedges FOMC hike risk and tariff uncertainty. |
| anthropic-claude-fable-5 | HEALTHCARE | 20.0 | -0.00012306897531744188 | -2.4613795063488376e-05 | Strong prior active trend (+3.68%), near 52w high, negative beta; defensive earnings resilience amid tariff and rate risk. |
| anthropic-claude-fable-5 | UTILITIES | 10.0 | -0.04190971866834847 | -0.004190971866834848 | Recent defensive bid (+3.05% 3s) and near-zero beta; cushions portfolio against FOMC volatility. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 35.0 | -0.015438539393253903 | -0.005403488787638865 | Strong recent relative momentum (+2.4% active 5s), shallow drawdown, low volatility versus tech; defensive-cyclical tilt with earnings support. |
| anthropic-claude-opus-4-8 | FINANCIALS | 30.0 | 0.011188041401963167 | 0.00335641242058895 | High quality-evidence score (0.689), positive active returns, low beta, strong Q2 earnings tracking; defensive within equities. |
| anthropic-claude-opus-4-8 | SP500 | 35.0 | 0.010961845778870494 | 0.0038366460226046725 | Core broad-market anchor into a heavy mega-cap earnings and FOMC week. |
| anthropic-claude-opus-5 | SP500 | 35.0 | 0.010961845778870494 | 0.0038366460226046725 | Core benchmark exposure into a heavy mega-cap earnings week with Q2 S&P earnings tracking +26.5%. |
| anthropic-claude-opus-5 | HEALTHCARE | 25.0 | -0.00012306897531744188 | -3.076724382936047e-05 | Defensive, near-zero SPY beta, strong prior relative trend and shallow drawdown ahead of a rate-risk-heavy week. |
| anthropic-claude-opus-5 | FINANCIALS | 20.0 | 0.011188041401963167 | 0.0022376082803926335 | Positive prior active return, low drawdown, benefits if FOMC signals higher-for-longer rates; low realized vol. |
| anthropic-claude-opus-5 | ENERGY | 20.0 | -0.0011740847557669687 | -0.00023481695115339375 | Brent near $96.78 versus $72 pre-war; sector has strong prior active return with negative SPY correlation for diversification. |
| google-gemini-3-1-pro | UTILITIES | 25.0 | -0.04190971866834847 | -0.010477429667087118 | Utilities offer defensive positioning ahead of the FOMC meeting and have shown strong recent relative performance. |
| google-gemini-3-1-pro | FINANCIALS | 25.0 | 0.011188041401963167 | 0.0027970103504907917 | Financials benefit from a potential steepening yield curve and have demonstrated positive recent active returns. |
| google-gemini-3-1-pro | COMMUNICATIONS | 25.0 | 0.01825020595058291 | 0.004562551487645727 | Communications holds high quality evidence scores and is positioned for major mega-cap earnings reports. |
| google-gemini-3-1-pro | LARGE_VALUE | 25.0 | 0.014421534611000819 | 0.0036053836527502048 | Large value provides a rotation target away from tech while maintaining broad equity exposure. |
| openai-gpt-5-5 | EQUAL_WEIGHT_SP500 | 20.0 | 0.006742485491397776 | 0.0013484970982795552 | Breadth was better than cap-weighted SPY, with RSP outperforming over 5 and 21 sessions and lower 21-session volatility than SPY. |
| openai-gpt-5-5 | HEALTHCARE | 20.0 | -0.00012306897531744188 | -2.4613795063488376e-05 | Healthcare has positive recent active return, strong prior active return, and low beta/correlation to SPY, offering defensive alpha potential into a catalyst-heavy week. |
| openai-gpt-5-5 | FINANCIALS | 20.0 | 0.011188041401963167 | 0.0022376082803926335 | Financials show strong prior active return, positive 5-session active return, and high quality evidence, with FOMC and economic data as near-term catalysts. |
| openai-gpt-5-5 | ENERGY | 20.0 | -0.0011740847557669687 | -0.00023481695115339375 | Energy retains strong prior and recent active return and is supported by oil-price levels still well above pre-war levels despite the latest pullback. |
| openai-gpt-5-5 | UTILITIES | 20.0 | -0.04190971866834847 | -0.008381943733669696 | Utilities had the strongest recent defensive sector active move with low market beta, useful if FOMC and growth data trigger risk reduction. |
| openai-gpt-5-6-sol | COMMUNICATIONS | 25.0 | 0.01825020595058291 | 0.004562551487645727 | High quality-evidence score, an established prior relative trend, and a sharp pullback create rebound potential around major platform earnings. |
| openai-gpt-5-6-sol | SOFTWARE | 20.0 | 0.07501700831142633 | 0.015003401662285266 | The universe-leading combination of prior relative strength and recent pullback supports a tactical earnings-week rebound. |
| openai-gpt-5-6-sol | HEALTHCARE | 20.0 | -0.00012306897531744188 | -2.4613795063488376e-05 | Persistent relative strength and defensive exposure provide a less rate-sensitive complement to the growth holdings. |
| openai-gpt-5-6-sol | FINANCIALS | 20.0 | 0.011188041401963167 | 0.0022376082803926335 | Strong prior relative performance, solid quality evidence, and multiple rate and growth catalysts support continued leadership. |
| openai-gpt-5-6-sol | AGRICULTURE | 15.0 | -0.025849850461569512 | -0.003877477569235427 | Positive prior and recent active returns, shallow drawdown, and near-zero SPY correlation diversify event-driven equity exposure. |
| xai-grok-4-3 | SP500 | 40.0 | 0.010961845778870494 | 0.004384738311548198 | Broad market exposure with neutral base case amid mixed macro data. |
| xai-grok-4-3 | ENERGY | 20.0 | -0.0011740847557669687 | -0.00023481695115339375 | Strong recent active returns and commodity price support. |
| xai-grok-4-3 | FINANCIALS | 20.0 | 0.011188041401963167 | 0.0022376082803926335 | Value tilt with positive prior active rank and earnings momentum. |
| xai-grok-4-3 | HEALTHCARE | 20.0 | -0.00012306897531744188 | -2.4613795063488376e-05 | Defensive sector with highest prior active rank and low drawdown. |
| xai-grok-4-5 | ENERGY | 30.0 | -0.0011740847557669687 | -0.0003522254267300906 | Elevated oil price level and energy sector relative strength support higher base return than SPY into FOMC and GDP week despite single-day crude pullback. |
| xai-grok-4-5 | AEROSPACE_DEFENSE | 25.0 | -0.0019988314769235904 | -0.0004997078692308976 | Strong 3-session outperformance and defense budget/geopolitical backdrop give higher expected weekly return than benchmark. |
| xai-grok-4-5 | HEALTHCARE | 25.0 | -0.00012306897531744188 | -3.076724382936047e-05 | Positive active returns, defensive characteristics, and quality score support outperformance versus SPY base case. |
| xai-grok-4-5 | LARGE_VALUE | 20.0 | 0.014421534611000819 | 0.002884306922200164 | Value leadership, shallow drawdown, and higher quality evidence score imply modest edge over cap-weighted SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | COMMUNICATIONS | 5 | 0.6 | 0.01825020595058291 | 0.017901470066024716 | 0.006939624287154222 | 0.05711553824540161 |  | True | True |
| xai-grok-4-3 | SP500 | 4 | 0.55 | 0.010961845778870494 | 0.0063629158457239494 | -0.004598929933146544 | 0.06865409246570238 |  | False | True |
| anthropic-claude-opus-5 | SP500 | 4 | 0.55 | 0.010961845778870494 | 0.0058086701080145514 | -0.005153175670855942 | 0.06920833820341177 |  | False | True |
| xai-grok-4-5 | ENERGY | 4 | 0.58 | -0.0011740847557669687 | 0.002001606382409815 | -0.008960239396460679 | 0.07301540192901651 |  | False | True |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 3 | 0.55 | -0.015438539393253903 | 0.0017895696555547571 | -0.009172276123315736 | 0.07322743865587157 |  | False | True |
| google-gemini-3-1-pro | UTILITIES | 4 | 0.65 | -0.04190971866834847 | 0.0004875158237996058 | -0.010474329955070888 | 0.07452949248762672 |  | False | True |
| anthropic-claude-fable-5 | ENERGY | 5 | 0.6 | -0.0011740847557669687 | -0.0033910982752832393 | -0.014352944054153733 | 0.07840810658670956 |  | False | False |
| openai-gpt-5-5 | EQUAL_WEIGHT_SP500 | 5 | 0.58 | 0.006742485491397776 | -0.005055269101214389 | -0.016017114880084882 | 0.08007227741264071 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | SP500 | -0.005153175670855942 | 0.21979500000000002 | -0.023445372601087113 |
| anthropic-claude-fable-5 | ENERGY | -0.014352944054153733 | 0.45469000000000004 | -0.03156643879160248 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 46c5f9e6572e44e96ec1ade82529e43932bf3de57031c303b3a9a463b08d2177 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 1a844da9c59ab06e30e88b53a60f08b23075e0cfd4df40bd80afc8570a93c261 |
| manifest.yaml | 981e8a7fb137b921736dc32e56a38d970951cd833721b8e3f07895d8d4737955 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 759af6de5c971beec666384e001077f4189fbec56f9cf198459116202ffd98b2 |
| market_data/universe_decision_context.md | bd97ad9b9b57375780acfa2112d8b50ee77a9c58b9c2ba2cc8af2cee5e1af464 |
| market_data/universe_decision_context.json | dfa52f7c9679424753db9887f8bafd9358109758b8cd350c4077f0f35911fdf4 |
| market_data/decision_context_source_history.json | 9c6efe62689f7a60a315b45056c98a08a60c26d12e2315b1b6d4f4d50af3d058 |
| market_data/universe_quality_evidence.md | 09fc4f5422bf6835ebc2e9a5c6b4bec795d9c1b49a77c679ab5fa78202d5a202 |
| market_data/universe_quality_evidence.json | ffd6df9cde7a04cd7f5c8add0f6a9e065bacedbba3baa4324791d097489ba31b |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 8c0ecd265368f14faa1b51e514cbddc9894c887549e0cee332687deda61c9ffd | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | c651df739f1323fed0cf451f4593368ba0267b94d99e385cb56e6b0f56e339c2 | yes |
| Final briefing | research/final_briefing.md | model-facing | 46c5f9e6572e44e96ec1ade82529e43932bf3de57031c303b3a9a463b08d2177 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
