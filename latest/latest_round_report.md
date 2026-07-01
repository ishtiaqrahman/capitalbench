# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-06-23-1W
- Decision deadline: 2026-06-24T02:30:00Z
- Horizon: one week
- Official run ID: official-20260623-no-fable
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | openai | portfolio | BIOTECH | 5 | 0.54 | Favoring short-horizon momentum and breadth over defensive assets, with concentrated exposure to biotech, regional banks, small caps, Taiwan, and semiconductors. The portfolio is designed to beat SPY if the June 23 selloff broadens into rotation rather than a full risk-off move. | Semiconductor weakness from Micron, Nvidia, Samsung, or Korea could persist and drag Taiwan and SMH lower.; May personal income and outlays data could revive inflation or rate concerns, pressuring small caps, banks, and biotech.; High-beta momentum sectors could reverse sharply if investors de-risk before the June 30 exit close.; Regional banks could underperform if credit-quality, deposit, or commercial real estate concerns re-emerge.; Biotech’s recent surge may mean near-term overextension and vulnerability to profit-taking. |
| google-gemini-3-1-pro | google | portfolio | BIOTECH | 3 | 0.6 | Allocating to Biotech, Regional Banks, and Small Caps based on their positive 7-day and 30-day returns, aiming to capture short-term momentum and relative strength against the S&P 500. | A sudden reversal in recent sector momentum could lead to underperformance.; Biotech is highly volatile and sensitive to specific company news or clinical trial results.; Regional banks remain sensitive to interest rate expectations and potential credit concerns. |
| xai-grok-4-3 | xai | portfolio | SMALL_CAP | 4 | 0.65 | Recent data show small caps, biotech, and momentum outperforming amid tech weakness and positive breadth; allocations target these factors for one-week alpha. | Reversal in small-cap and biotech momentum if macro data disappoints on June 25; Tech stabilization pulling flows back from small caps before exit close; Holiday-week liquidity reducing follow-through on June 30 |
| anthropic-claude-opus-4-7 | anthropic | portfolio | BIOTECH | 5 | 0.5 | Avoid mega-cap tech drag; lean into biotech momentum, small caps, and broadening breadth themes for a one-week window. | Biotech momentum reversal after sharp 7d gain; Sticky CPI (+4.2% YoY) triggers further rate-driven equity selloff; Small-cap and regional bank exposure vulnerable if credit/growth fears intensify; Continued semiconductor weakness spilling into broader risk assets |
| anthropic-claude-opus-4-8 | anthropic | portfolio | BIOTECH | 5 | 0.55 | Lean into the breadth-positive, non-mega-cap segments showing recent relative strength while holding a cash-like buffer against renewed tech volatility and sticky inflation. | Tech rebound could cause cap-weight leaders (QQQ/SMH) to outperform the chosen breadth tilt and SPY benchmark.; Biotech's sharp recent rally could mean-revert sharply within the week.; Hot PCE on June 25 could lift rates and pressure small caps and regional banks.; Risk-off escalation from Korea/semiconductor weakness could spill into high-beta small caps and biotech. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 147.03 | 158.25 | 0.07631095694756174 | 1 |
| CYBERSECURITY | Cybersecurity | 84.1374884901 | 89.85 | 0.06789496112154758 | 2 |
| SEMICONDUCTORS | Semiconductors | 622.05 | 655.89 | 0.05440077164215107 | 3 |
| SOUTH_KOREA | South Korea Equities | 192.2 | 201.9 | 0.05046826222684708 | 4 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 126.36 | 132.22 | 0.046375435264324194 | 5 |
| HEALTHCARE | Healthcare Sector | 152.18 | 158.66000366210938 | 0.04258117796102878 | 6 |
| INDUSTRIALS | Industrials Sector | 178.15 | 185.22999572753906 | 0.03974176664349738 | 7 |
| MOMENTUM | US Momentum Equities | 329.76 | 342.8299865722656 | 0.03963484525796224 | 8 |
| SOFTWARE | Software | 87.32 | 90.6 | 0.037562986715529156 | 9 |
| LARGE_GROWTH | US Large-Cap Growth | 119.81 | 124.16999816894531 | 0.03639093705821983 | 10 |
| BROAD_AI_TECH | Broad AI Technology | 63.3495541265 | 65.61 | 0.035682111810703576 | 11 |
| TECHNOLOGY | Technology Sector | 184.19 | 190.52000427246094 | 0.034366709769590775 | 12 |
| TAIWAN | Taiwan Equities | 105.23999786376953 | 108.61 | 0.032022065798527066 | 13 |
| NASDAQ100 | Nasdaq 100 | 713.65 | 736.4000244140625 | 0.031878405960992895 | 14 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 113.76 | 117.27999877929688 | 0.030942324009290312 | 15 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 235.93 | 242.42 | 0.027508159199762572 | 16 |
| MID_CAP | US Mid-Cap Stocks | 75.3 | 77.11000061035156 | 0.024037192700552046 | 17 |
| REGIONAL_BANKS | Regional Banks | 73.12 | 74.85 | 0.023659737417943028 | 18 |
| TOTAL_US_MARKET | Total US Stock Market | 362.655046458 | 370.0400085449219 | 0.020363599401276078 | 19 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 208.89 | 212.77 | 0.018574369285269787 | 20 |
| SP500 | S&P 500 | 733.58 | 746.77001953125 | 0.01798034233655499 | 21 |
| SMALL_CAP | US Small-Cap Stocks | 295.32 | 300.45001220703125 | 0.017371028738423666 | 22 |
| SMALL_VALUE | US Small-Cap Value | 217.55 | 221.1999969482422 | 0.016777738213018534 | 23 |
| EUROPE | Europe Equities | 87.16 | 88.54000091552734 | 0.01583296139889101 | 24 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.17 | 71.25 | 0.015391192817443278 | 25 |
| UNITED_KINGDOM | United Kingdom Equities | 45.57 | 46.14 | 0.012508229098090906 | 26 |
| COPPER | Copper | 37.31999969482422 | 37.73 | 0.010986074719412153 | 27 |
| BRAZIL | Brazil Equities | 34.150001525878906 | 34.5 | 0.01024885676376508 | 28 |
| SOLAR | Solar Energy | 58.56 | 59.15 | 0.010075136612021751 | 29 |
| LOW_VOL | US Low Volatility Equities | 74.21 | 74.9000015258789 | 0.009297958844884935 | 30 |
| MEXICO | Mexico Equities | 74.7300033569336 | 75.27 | 0.007225968403710814 | 31 |
| INDIA | India Equities | 49.07 | 49.38999938964844 | 0.006521283669216116 | 32 |
| LARGE_VALUE | US Large-Cap Value | 240.95 | 242.42999267578125 | 0.006142322788052601 | 33 |
| UTILITIES | Utilities Sector | 45.07 | 45.34000015258789 | 0.005990684548211389 | 34 |
| JAPAN | Japan Equities | 92.75 | 93.2699966430664 | 0.005606432809341255 | 35 |
| EMERGING_MARKETS | Emerging Markets | 59.36 | 59.689998626708984 | 0.005559276056418261 | 36 |
| AUSTRALIA | Australia Equities | 28.02 | 28.16 | 0.0049964311206280865 | 37 |
| TIPS | Treasury Inflation-Protected Securities | 108.9 | 109.43000030517578 | 0.0048668531237445745 | 38 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.12 | 94.56999969482422 | 0.004781127229326554 | 39 |
| EURO | Euro | 105.02999877929688 | 105.44 | 0.0039036582449616386 | 40 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.26000213623047 | 107.62 | 0.00335631042886142 | 41 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.71 | 98.9800033569336 | 0.002735319186846219 | 42 |
| AGRICULTURE | Agriculture Commodities | 26.600000381469727 | 26.67 | 0.0026315645686620925 | 43 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 86.2 | 86.41999816894531 | 0.0025521829344004043 | 44 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.33999633789062 | 94.52 | 0.0019080312603010352 | 45 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.26000213623047 | 96.44 | 0.0018699133573132354 | 46 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.91 | 109.06999969482422 | 0.0014691001269324655 | 47 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.87 | 79.97000122070312 | 0.0012520498397785573 | 48 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.380001068115234 | 48.43 | 0.0010334628106842825 | 49 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.58 | 91.63999938964844 | 0.0006551582184803895 | 50 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 51 |
| CANADA | Canada Equities | 57.67 | 57.64 | -0.0005202011444425114 | 52 |
| MATERIALS | Materials Sector | 50.87 | 50.83000183105469 | -0.0007862820708730567 | 53 |
| COMMUNICATIONS | Communication Services Sector | 107.27 | 107.12999725341797 | -0.0013051435311086657 | 54 |
| US_DOLLAR | US Dollar | 28.450000762939453 | 28.41 | -0.0014060021745785356 | 55 |
| DIVIDEND | US Dividend Equities | 31.7666280925 | 31.709999084472656 | -0.0017826571917689549 | 56 |
| FINANCIALS | Financials Sector | 53.88 | 53.61000061035156 | -0.005011124529481048 | 57 |
| YEN | Japanese Yen | 56.79999923706055 | 56.44 | -0.006338014822113935 | 58 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.72 | 83.06999969482422 | -0.007763978800475191 | 59 |
| SOUTH_AFRICA | South Africa Equities | 63.93000030517578 | 63.19 | -0.011575165049950265 | 60 |
| REAL_ESTATE | Real Estate Sector | 44.64 | 44.029998779296875 | -0.013664901897471493 | 61 |
| CHINA | China Equities | 51.81 | 51.025001525878906 | -0.01515148570007907 | 62 |
| BROAD_COMMODITIES | Broad Commodities | 16.18 | 15.88 | -0.018541409147095123 | 63 |
| GOLD | Gold | 77.33 | 75.51 | -0.023535497219707713 | 64 |
| ENERGY | Energy Sector | 54.46 | 53.11000061035156 | -0.024788824635483597 | 65 |
| METALS_MINING | Metals and Mining | 110.9 | 106.93 | -0.03579801623083856 | 66 |
| SILVER | Silver | 55.72999954223633 | 53.47 | -0.04055265675219566 | 67 |
| OIL | Crude Oil | 111.26000213623047 | 106.44 | -0.04332196695743995 | 68 |
| ETHEREUM_ETF | Ethereum ETF | 12.520000457763672 | 11.89 | -0.050319523540672595 | 69 |
| BITCOIN_ETF | Bitcoin ETF | 35.310001373291016 | 33.29 | -0.05720762658533829 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | portfolio | BIOTECH | 5 | 0.54 | 0.07631095694756174 | 0.044740258777884914 | 0.026759916441329926 | 0.03157069816967682 |  | True | True |
| google-gemini-3-1-pro | portfolio | BIOTECH | 3 | 0.6 | 0.07631095694756174 | 0.0428336126259347 | 0.02485327028937971 | 0.03347734432162704 |  | True | True |
| xai-grok-4-3 | portfolio | SMALL_CAP | 4 | 0.65 | 0.017371028738423666 | 0.03944644145253229 | 0.0214660991159773 | 0.03686451549502945 |  | True | True |
| anthropic-claude-opus-4-7 | portfolio | BIOTECH | 5 | 0.5 | 0.07631095694756174 | 0.038777489755006375 | 0.020797147418451387 | 0.03753346719255536 |  | True | True |
| anthropic-claude-opus-4-8 | portfolio | BIOTECH | 5 | 0.55 | 0.07631095694756174 | 0.03419594442655135 | 0.01621560208999636 | 0.04211501252101039 |  | True | True |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-06-24-1W has no scored official run.
- Round CB-2026-06-25-1W has no scored official run.
- Round CB-2026-06-26-1W has no scored official run.
- Round CB-2026-06-29-1W has no scored official run.
