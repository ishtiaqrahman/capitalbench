# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-07-23-1W
- Decision deadline: 2026-07-24T09:30:00Z
- Horizon: one week
- Official run ID: official-v2-2-20260723-1w-r2
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | ENERGY | 4 | 0.62 | Selected holdings exceed SPY base forecast; energy cluster at 40% drives alpha in one-week window. | FOMC outcome surprises rates higher; Oil reversal on inventory build; Broader equity selloff extends |
| openai-gpt-5-5 | openai | portfolio | ENERGY | 5 | 0.56 | SPY faces near-term earnings and policy-event risk after a broad down day. Selected holdings have base forecasts above SPY, supported by supplied relative strength, quality evidence, commodity shock data, or defensive rotation potential. | Oil and commodity prices could reverse sharply after the large July move and inventory builds.; The FOMC statement or GDP/personal income data could trigger a broad risk-off move that hurts equities and cyclicals.; Mega-cap technology could rebound after earnings-related declines, causing SPY to outperform equal-weight and defensive tilts.; Energy-price inflation could pressure margins and consumer demand, weakening non-energy equity holdings. |
| openai-gpt-5-6-sol | openai | portfolio | ENERGY | 4 | 0.6 | Energy, aerospace and defense, healthcare, and the dollar each have base forecasts above SPY's. The allocation respects the 50% cluster cap and targets resilience through a catalyst-heavy week. | A rapid de-escalation could reverse crude oil, energy, and defense risk premiums.; A dovish FOMC outcome could weaken the dollar and trigger a growth-led rebound that leaves defensive holdings behind.; The July 30 GDP and inflation-related releases could produce an abrupt rates and factor rotation.; Energy inventories rose and the demand proxy was down year over year, increasing oil reversal risk. |
| xai-grok-4-5 | xai | portfolio | ENERGY | 4 | 0.58 | SPY base is modest after the July 23 selloff; selected sleeves show stronger base forecasts from oil momentum, defense earnings and factor quality. Horizon catalysts are FOMC, GDP and residual commodity momentum. | FOMC hawkish surprise drives rates higher and equities lower; Oil mean-reversion after 7% single-day jump; Growth data (GDP/durables) disappoints cyclical sleeves; Mega-cap earnings (MSFT) dominate and leave cyclicals behind |
| anthropic-claude-fable-5 | anthropic | portfolio | ENERGY | 5 | 0.62 | Overweight energy and inflation-shock beneficiaries with defensive equity ballast; underweight rate-sensitive mega-cap growth that just sold off on Tesla and Alphabet results. | Rapid conflict de-escalation collapses oil, commodities, and gold simultaneously; Dovish FOMC surprise sparks a growth/tech rally that leaves defensive tilts behind; High-volatility oil positioning (USO vol 50.7%) can reverse violently within the week; Strong Microsoft results July 29 lift SPY via mega-cap concentration |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 4 | 0.55 | Overweight defensives and energy given deteriorating breadth and an oil supply shock, while retaining SPY exposure ahead of FOMC. | FOMC surprise triggering risk-on rally hurting defensives; Crude oil reversing sharply, undercutting energy; Mega-cap earnings (MSFT) driving broad rebound above defensives |
| google-gemini-3-1-pro | google | portfolio | OIL | 4 | 0.65 | Overweight energy and gold to capture momentum and hedge against volatility, balanced with core equity exposure. | A hawkish surprise from the FOMC could negatively impact equities and gold.; A sudden reversal in crude oil prices would hurt the energy overweight.; Disappointing mega-cap tech earnings could drag down the broader market. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOFTWARE | Software | 87.1 | 93.31 | 0.07129735935706094 | 1 |
| SOUTH_AFRICA | South Africa Equities | 60.43 | 64.11 | 0.06089690551050797 | 2 |
| AUSTRALIA | Australia Equities | 28.49 | 29.82 | 0.04668304668304679 | 3 |
| INDIA | India Equities | 47.63 | 49.7 | 0.043460004199034286 | 4 |
| UNITED_KINGDOM | United Kingdom Equities | 46.7 | 48.68 | 0.042398286937901375 | 5 |
| CHINA | China Equities | 53.35 | 55.5 | 0.0402999062792877 | 6 |
| EUROPE | Europe Equities | 87.83 | 90.99 | 0.03597859501309353 | 7 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 108.76000213623047 | 112.39 | 0.03337622096791315 | 8 |
| COPPER | Copper | 38.24 | 39.34 | 0.028765690376569175 | 9 |
| ETHEREUM_ETF | Ethereum ETF | 14.11 | 14.51 | 0.028348688873139682 | 10 |
| MEXICO | Mexico Equities | 75.0 | 77.11 | 0.028133333333333344 | 11 |
| YEN | Japanese Yen | 56.01 | 57.58 | 0.02803070880199976 | 12 |
| SILVER | Silver | 52.06 | 53.5 | 0.027660391855551136 | 13 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.20999908447266 | 85.47 | 0.027160208393140817 | 14 |
| MATERIALS | Materials Sector | 50.290000915527344 | 51.64 | 0.026844284348697123 | 15 |
| CYBERSECURITY | Cybersecurity | 87.72 | 90.02 | 0.026219790241678087 | 16 |
| JAPAN | Japan Equities | 91.1 | 93.29 | 0.024039517014270206 | 17 |
| FINANCIALS | Financials Sector | 55.83000183105469 | 57.0 | 0.020956441529158543 | 18 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.78 | 71.09 | 0.01877328747492113 | 19 |
| DIVIDEND | US Dividend Equities | 32.79999923706055 | 33.41 | 0.01859758466854511 | 20 |
| LARGE_VALUE | US Large-Cap Value | 246.17999267578125 | 250.71 | 0.018401200174641197 | 21 |
| CANADA | Canada Equities | 58.82 | 59.79 | 0.016490989459367444 | 22 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 211.92 | 215.38 | 0.016326915817289622 | 23 |
| GOLD | Gold | 76.15 | 77.3 | 0.0151017728168088 | 24 |
| EURO | Euro | 105.03 | 106.47 | 0.01371036846615259 | 25 |
| HEALTHCARE | Healthcare Sector | 161.44000244140625 | 163.52 | 0.012884028290006233 | 26 |
| COMMUNICATIONS | Communication Services Sector | 105.37999725341797 | 106.58 | 0.0113873863907612 | 27 |
| REGIONAL_BANKS | Regional Banks | 75.15 | 75.9 | 0.009980039920159722 | 28 |
| BRAZIL | Brazil Equities | 36.17 | 36.53 | 0.0099529997235277 | 29 |
| REAL_ESTATE | Real Estate Sector | 44.95000076293945 | 45.3 | 0.007786412260733844 | 30 |
| SMALL_VALUE | US Small-Cap Value | 220.5800018310547 | 221.79 | 0.005485529780129728 | 31 |
| SP500 | S&P 500 | 738.1799926757812 | 741.69 | 0.004754947789218145 | 32 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.26 | 105.76 | 0.004750142504275079 | 33 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.88 | 93.29 | 0.004414298018949214 | 34 |
| TOTAL_US_MARKET | Total US Stock Market | 364.69000244140625 | 366.27 | 0.004332440012110306 | 35 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.8499984741211 | 93.21 | 0.003877237822241142 | 36 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.71 | 47.88 | 0.003563194298889183 | 37 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.2300033569336 | 79.47 | 0.003029113125051941 | 38 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.33999633789062 | 97.62 | 0.002876553037226559 | 39 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.53 | 94.79 | 0.0027504495927219708 | 40 |
| TIPS | Treasury Inflation-Protected Securities | 107.48999786376953 | 107.74 | 0.002325817668610508 | 41 |
| SMALL_CAP | US Small-Cap Stocks | 292.0899963378906 | 292.59 | 0.0017118137162457359 | 42 |
| EMERGING_MARKETS | Emerging Markets | 58.1 | 58.19 | 0.001549053356282304 | 43 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.26000213623047 | 106.41 | 0.0014116117142293216 | 44 |
| BITCOIN_ETF | Bitcoin ETF | 36.65 | 36.7 | 0.0013642564802183177 | 45 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.58000183105469 | 91.65 | 0.0007643390210283485 | 46 |
| LOW_VOL | US Low Volatility Equities | 76.36000061035156 | 76.38 | 0.00026190923898083973 | 47 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 48 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 238.23 | 238.13 | -0.00041976241447339024 | 49 |
| MID_CAP | US Mid-Cap Stocks | 75.44999694824219 | 75.35 | -0.001325340653238083 | 50 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.16999816894531 | 82.8 | -0.004448697572335236 | 51 |
| BIOTECH | Biotechnology | 152.23 | 151.46 | -0.005058135715693246 | 52 |
| ENERGY | Energy Sector | 59.380001068115234 | 58.96 | -0.007073106442578969 | 53 |
| LARGE_GROWTH | US Large-Cap Growth | 118.58999633789062 | 117.43 | -0.009781569893851039 | 54 |
| BROAD_AI_TECH | Broad AI Technology | 59.33 | 58.69 | -0.010787122872071508 | 55 |
| NASDAQ100 | Nasdaq 100 | 691.9600219726562 | 683.55 | -0.012153913095558355 | 56 |
| METALS_MINING | Metals and Mining | 103.17 | 101.86 | -0.012697489580304366 | 57 |
| US_DOLLAR | US Dollar | 28.56 | 28.14 | -0.014705882352941124 | 58 |
| TECHNOLOGY | Technology Sector | 178.4499969482422 | 175.73 | -0.015242347967263425 | 59 |
| INDUSTRIALS | Industrials Sector | 181.94000244140625 | 178.39 | -0.01951194016582225 | 60 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 116.85 | 113.98 | -0.024561403508771895 | 61 |
| AGRICULTURE | Agriculture Commodities | 28.24 | 27.48 | -0.026912181303116123 | 62 |
| BROAD_COMMODITIES | Broad Commodities | 18.06 | 17.5 | -0.03100775193798444 | 63 |
| UTILITIES | Utilities Sector | 46.189998626708984 | 44.66 | -0.033124024078759695 | 64 |
| MOMENTUM | US Momentum Equities | 313.9800109863281 | 298.77 | -0.048442609255754276 | 65 |
| SOLAR | Solar Energy | 52.85 | 49.84 | -0.05695364238410594 | 66 |
| TAIWAN | Taiwan Equities | 99.84 | 94.0 | -0.05849358974358976 | 67 |
| SEMICONDUCTORS | Semiconductors | 580.17 | 538.9 | -0.07113432269851938 | 68 |
| SOUTH_KOREA | South Korea Equities | 173.86 | 161.21 | -0.0727596917059703 | 69 |
| OIL | Crude Oil | 139.49 | 127.48 | -0.08609936196143098 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | portfolio | ENERGY | 4 | 0.62 | -0.007073106442578969 | 0.003854898903906689 | -0.0009000488853114557 | 0.06744246045315425 |  | False | True |
| openai-gpt-5-5 | portfolio | ENERGY | 5 | 0.56 | -0.007073106442578969 | -0.00015417306040210743 | -0.004909120849620252 | 0.07145153241746305 |  | False | False |
| openai-gpt-5-6-sol | portfolio | ENERGY | 4 | 0.6 | -0.007073106442578969 | -0.001232735937555318 | -0.005987683726773463 | 0.07253009529461626 |  | False | False |
| xai-grok-4-5 | portfolio | ENERGY | 4 | 0.58 | -0.007073106442578969 | -0.0031893125416992915 | -0.007944260330917436 | 0.07448667189876024 |  | False | False |
| anthropic-claude-fable-5 | portfolio | ENERGY | 5 | 0.62 | -0.007073106442578969 | -0.003245654523856912 | -0.008000602313075056 | 0.07454301388091786 |  | False | False |
| anthropic-claude-opus-4-8 | portfolio | HEALTHCARE | 4 | 0.55 | 0.012884028290006233 | -0.005233084585489167 | -0.009988032374707311 | 0.07653044394255011 |  | False | False |
| google-gemini-3-1-pro | portfolio | OIL | 4 | 0.65 | -0.08609936196143098 | -0.01832893694949575 | -0.023083884738713895 | 0.08962629630655669 |  | False | False |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1W has no scored official run.
- Round CB-2026-07-24-1W has no scored official run.
- Round CB-2026-07-27-1W has no scored official run.
- Round CB-2026-07-28-1W has no scored official run.
- Round CB-2026-07-29-1W has no scored official run.
