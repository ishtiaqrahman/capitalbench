# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-07-02-1W
- Decision deadline: 2026-07-03T07:30:00Z
- Horizon: one week
- Official run ID: official-20260702
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | SP500 | 4 | 0.65 | A balanced approach combining broad US equities, defensive sectors (Healthcare), potential beneficiaries of the rate environment (Financials), and a cash-like buffer (Short-Term Treasuries). | Unexpected negative earnings surprises from major banks could weigh on the Financials sector.; A sudden shift in interest rate expectations could negatively impact both equities and fixed income.; Broader market volatility could lead to underperformance relative to a more concentrated or aggressive strategy. |
| anthropic-claude-fable-5 | anthropic | portfolio | HEALTHCARE | 5 | 0.5 | Tilt toward healthcare, low-vol, and financials on soft labor data and bank earnings positioning, with biotech for rate-cut beta and SPY as ballast; underweight extended semis/tech showing drawdown risk. | Renewed mega-cap tech rally (e.g., strong TSMC June sales July 10 read-through) would leave this defensive tilt lagging SPY; Hot ISM Services or inflation-related surprise pushes yields up, hurting biotech and low-vol rate-sensitive holdings; Biotech and healthcare momentum reverses from 52-week highs with limited independent catalyst support in the window; Pre-earnings de-risking in banks before July 14 could stall financials |
| openai-gpt-5-5 | openai | portfolio | BIOTECH | 5 | 0.58 | Favor healthcare/biotech, financials, aerospace-defense, and low-volatility equities over cap-weighted S&P 500 exposure for a one-week window marked by weak jobs data, elevated inflation, and recent factor rotation away from mega-cap tech. The portfolio keeps enough risk to seek alpha while diversifying across 5 holdings. | Biotech and healthcare have already rallied sharply and could mean-revert or suffer idiosyncratic drug-policy, clinical, or financing headlines.; If mega-cap technology and semiconductors rebound strongly after recent weakness, the portfolio may lag the S&P 500 benchmark.; Financials could underperform if weak payroll data raises credit-quality concerns or if the yield curve/rates move unfavorably before bank earnings.; A stronger-than-expected ISM Services release or renewed risk-on move could reduce demand for low-volatility and defensive sectors.; Holiday-shortened trading and low liquidity around July 4 could amplify reversals in recent factor momentum. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Overweight healthcare, financials, low-vol and value leadership with a cash-like anchor to seek positive alpha versus SPY in a low-catalyst week. | Sharp tech/semiconductor rebound would drive SPY/QQQ up and cause defensive tilt to lag the benchmark; Healthcare and value recent strength could reverse (crowding/mean reversion) before exit close; Rate spike or hawkish data ahead of ISM Services (July 6) could pressure rate-sensitive financials and low-vol names; Bank pre-earnings de-risking or negative guidance chatter could weigh on financials before July 14 reports |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Defensive-leaning equity mix leveraging recent sector rotation into healthcare, financials, and low-vol, with equal-weight breadth and T-bill ballast to manage tech reversal risk over the one-week window. | Mega-cap tech rebound could cause equal-weight/defensive tilt to lag SPY; Bank earnings anticipation could reverse if credit or NII guidance disappoints (though outside window); Healthcare momentum reversal after +12% 30d run; Softer labor data triggering risk-off across cyclicals including financials |
| xai-grok-4-3 | xai | portfolio | HEALTHCARE | 3 | 0.55 | Soft labor data favors defensives; allocate across healthcare, staples, and low-vol to capture relative stability before exit close. | Stronger-than-expected ISM Services PMI on July 6 could reverse defensive rotation; Holiday liquidity may amplify any equity rebound on positive sentiment; Unexpected Fed commentary could shift rate expectations rapidly |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 103.98 | 109.01 | 0.04837468743989226 | 1 |
| CHINA | China Equities | 50.90999984741211 | 53.19 | 0.044784917686535586 | 2 |
| CYBERSECURITY | Cybersecurity | 90.66999816894531 | 94.26 | 0.03959415356296181 | 3 |
| AGRICULTURE | Agriculture Commodities | 26.74 | 27.71 | 0.036275243081525854 | 4 |
| BROAD_COMMODITIES | Broad Commodities | 15.869999885559082 | 16.42 | 0.03465659221216466 | 5 |
| BROAD_AI_TECH | Broad AI Technology | 61.849998474121094 | 63.83 | 0.03201295997941478 | 6 |
| ENERGY | Energy Sector | 53.220001220703125 | 54.82 | 0.030063862130736974 | 7 |
| BITCOIN_ETF | Bitcoin ETF | 34.87 | 35.81 | 0.026957269859478217 | 8 |
| TECHNOLOGY | Technology Sector | 180.58999633789062 | 185.35 | 0.026358069431505093 | 9 |
| SEMICONDUCTORS | Semiconductors | 592.2899780273438 | 607.73 | 0.02606834919625034 | 10 |
| ETHEREUM_ETF | Ethereum ETF | 12.86 | 13.19 | 0.025660964230171057 | 11 |
| SOUTH_KOREA | South Korea Equities | 180.14 | 184.75 | 0.025591206839125302 | 12 |
| BIOTECH | Biotechnology | 160.46 | 164.28 | 0.02380655615106564 | 13 |
| LARGE_GROWTH | US Large-Cap Growth | 121.16000366210938 | 123.3 | 0.017662564156556426 | 14 |
| BRAZIL | Brazil Equities | 34.43 | 34.96 | 0.01539355213476612 | 15 |
| NASDAQ100 | Nasdaq 100 | 712.5999755859375 | 723.28 | 0.014987404967675921 | 16 |
| MOMENTUM | US Momentum Equities | 316.5299987792969 | 321.2 | 0.014753739736243165 | 17 |
| COPPER | Copper | 37.29 | 37.75 | 0.012335746849021278 | 18 |
| CANADA | Canada Equities | 57.77 | 58.38 | 0.010559113726847924 | 19 |
| SP500 | S&P 500 | 744.780029296875 | 751.71 | 0.00930472143522354 | 20 |
| COMMUNICATIONS | Communication Services Sector | 109.5999984741211 | 110.51 | 0.008302933745877539 | 21 |
| EMERGING_MARKETS | Emerging Markets | 59.040000915527344 | 59.49 | 0.007621935594420259 | 22 |
| TOTAL_US_MARKET | Total US Stock Market | 368.760009765625 | 371.45 | 0.00729469075587863 | 23 |
| JAPAN | Japan Equities | 93.13999938964844 | 93.52 | 0.004079886330703442 | 24 |
| AUSTRALIA | Australia Equities | 28.09 | 28.2 | 0.00391598433606255 | 25 |
| SOFTWARE | Software | 93.56999969482422 | 93.88 | 0.003313030952087459 | 26 |
| TAIWAN | Taiwan Equities | 104.86 | 105.05 | 0.0018119397291627148 | 27 |
| US_DOLLAR | US Dollar | 28.34 | 28.36 | 0.0007057163020465218 | 28 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.70999908447266 | 79.75 | 0.000501830585708074 | 29 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.44000244140625 | 91.46 | 0.00021869595428491984 | 30 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 31 |
| GOLD | Gold | 77.51000213623047 | 77.51 | -2.7560707049900657e-08 | 32 |
| EURO | Euro | 105.47 | 105.42 | -0.0004740684554849217 | 33 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.80999755859375 | 70.73 | -0.00112974948950606 | 34 |
| SMALL_CAP | US Small-Cap Stocks | 297.5799865722656 | 297.24 | -0.0011425048309928743 | 35 |
| FINANCIALS | Financials Sector | 55.619998931884766 | 55.54 | -0.0014383123592421887 | 36 |
| LARGE_VALUE | US Large-Cap Value | 246.80999755859375 | 246.38 | -0.001742220991237109 | 37 |
| TIPS | Treasury Inflation-Protected Securities | 108.33000183105469 | 108.12 | -0.0019385380550642761 | 38 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.12000274658203 | 116.85 | -0.0023053512657974506 | 39 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.2 | 95.96 | -0.002494802494802606 | 40 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.13 | 93.82 | -0.0032933177520451107 | 41 |
| DIVIDEND | US Dividend Equities | 32.38999938964844 | 32.26 | -0.004013565671445729 | 42 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.12000274658203 | 93.71 | -0.004356170151056715 | 43 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.61000061035156 | 98.18 | -0.004360618676503836 | 44 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.24 | 48.02 | -0.004560530679933672 | 45 |
| REGIONAL_BANKS | Regional Banks | 75.02 | 74.65 | -0.004932018128498972 | 46 |
| MID_CAP | US Mid-Cap Stocks | 76.08999633789062 | 75.7 | -0.00512546138337 | 47 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.5 | 106.94 | -0.005209302325581366 | 48 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 214.91 | 213.5 | -0.006560885952259121 | 49 |
| YEN | Japanese Yen | 56.95 | 56.48 | -0.008252853380158132 | 50 |
| SMALL_VALUE | US Small-Cap Value | 221.3300018310547 | 219.5 | -0.00826820501475245 | 51 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.63999938964844 | 107.71 | -0.00856037734603543 | 52 |
| HEALTHCARE | Healthcare Sector | 163.74000549316406 | 162.17 | -0.009588405035381609 | 53 |
| REAL_ESTATE | Real Estate Sector | 44.68000030517578 | 44.23 | -0.010071627173280362 | 54 |
| EUROPE | Europe Equities | 89.3499984741211 | 88.41 | -0.010520408395903402 | 55 |
| INDIA | India Equities | 49.560001373291016 | 49.02 | -0.01089591118498301 | 56 |
| SOUTH_AFRICA | South Africa Equities | 64.0 | 63.28 | -0.011249999999999982 | 57 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.51000213623047 | 84.49 | -0.011928454107689723 | 58 |
| UTILITIES | Utilities Sector | 45.7599983215332 | 45.13 | -0.013767446342688006 | 59 |
| INDUSTRIALS | Industrials Sector | 183.91000366210938 | 181.11 | -0.015224857845436701 | 60 |
| UNITED_KINGDOM | United Kingdom Equities | 47.16 | 46.41 | -0.01590330788804073 | 61 |
| SILVER | Silver | 55.02 | 54.14 | -0.015994183933115247 | 62 |
| LOW_VOL | US Low Volatility Equities | 76.7300033569336 | 75.5 | -0.016030278940714293 | 63 |
| MEXICO | Mexico Equities | 75.5 | 74.24 | -0.016688741721854417 | 64 |
| METALS_MINING | Metals and Mining | 105.12999725341797 | 103.24 | -0.017977716187532078 | 65 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.98999786376953 | 83.2 | -0.02106127672386482 | 66 |
| SOLAR | Solar Energy | 56.31999969482422 | 54.95 | -0.02432527880411406 | 67 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 127.94000244140625 | 124.7 | -0.025324389397992197 | 68 |
| MATERIALS | Materials Sector | 52.0099983215332 | 50.26 | -0.0336473443185763 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 248.19 | 239.62 | -0.03452999717958016 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | portfolio | SP500 | 4 | 0.65 | 0.00930472143522354 | 0.0015602842860216407 | -0.007744437149201899 | 0.04681440315387062 |  | False | True |
| anthropic-claude-fable-5 | portfolio | HEALTHCARE | 5 | 0.5 | -0.009588405035381609 | -0.001403548132662402 | -0.010708269567885943 | 0.04977823557255466 |  | False | False |
| openai-gpt-5-5 | portfolio | BIOTECH | 5 | 0.58 | 0.02380655615106564 | -0.0023253243563826024 | -0.011630045791606142 | 0.05070001179627486 |  | False | False |
| anthropic-claude-opus-4-8 | portfolio | HEALTHCARE | 5 | 0.55 | -0.009588405035381609 | -0.006681618941824963 | -0.0159863403770485 | 0.05505630638171723 |  | False | False |
| anthropic-claude-opus-4-7 | portfolio | HEALTHCARE | 5 | 0.55 | -0.009588405035381609 | -0.007404418685978265 | -0.016709140121201803 | 0.055779106125870524 |  | False | False |
| xai-grok-4-3 | portfolio | HEALTHCARE | 3 | 0.55 | -0.009588405035381609 | -0.014962828713526378 | -0.024267550148749917 | 0.06333751615341864 |  | False | False |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-06-1W has no scored official run.
- Round CB-2026-07-07-1W has no scored official run.
- Round CB-2026-07-08-1W has no scored official run.
