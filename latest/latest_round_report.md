# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-08-13-1M
- Decision deadline: 2026-08-13T13:25:00Z
- Horizon: one month
- Official run ID: official-v2-2-all-monthly-20260813
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | ENERGY | 4 | 0.58 | Select active sleeves only where base exceeds SPY; energy leads on oil/geopolitics, healthcare on relative strength, software on recent active gains. Remainder in SPY for diversification under the 50% cluster cap. | Geopolitical de-escalation or oil supply surprise reverses energy; Rates reprice higher on sticky inflation data hurting growth/software; Labor or GDP revisions trigger broad equity drawdown; Concentration in correlated risk assets if risk appetite fades |
| xai-grok-4-6 | xai | portfolio | ENERGY | 4 | 0.56 | SPY is near a record with only a modest expected one-month gain. Energy, healthcare, cybersecurity, and Japan have stronger supplied continuation setups and higher bases, producing positive expected alpha versus SPY. | A broad equity reversal from the August 7 S&P high would drag high-beta cybersecurity and Japan; Oil geopolitics can fade quickly, reversing the energy overweight; Hotter August CPI or a hawkish FOMC-minutes read can compress risk assets before September 14; Labor-market deterioration beyond the July softness can hit cyclicals and international equities together |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.65 | A balanced approach combining core US equities with defensive healthcare and inflation-hedging energy. | Geopolitical tensions easing, leading to a drop in energy prices.; A sudden shift in market sentiment away from defensive sectors like healthcare.; Unexpectedly weak economic data impacting broad equity markets. |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.62 | Selected holdings show base forecasts exceeding SPY while respecting cluster caps and allocation rules. | Labor market revisions could pressure equities; Oil volatility from geopolitical events; Rate-sensitive sector reactions to CPI |
| anthropic-claude-fable-5 | anthropic | portfolio | SP500 | 5 | 0.58 | Breadth is broadening (RSP outperforming), value and healthcare show fresh relative strength with low drawdowns, and energy is supported by Iran-related crude supply risk, all offering modest expected alpha over SPY into mid-September. | Hot August CPI (Sep 11) reprices Fed expectations and hits all equity sleeves; Iran de-escalation drops crude prices, reversing the energy tilt; Mega-cap tech leadership resumes, causing value/equal-weight tilts to lag SPY; Sharp payroll deterioration on Sep 4 triggers broad risk-off despite defensive tilts |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 5 | 0.55 | Modest alpha construction: benchmark core plus low-beta healthcare, improving breadth, and a commodity-linked hedge into a data-heavy month ahead of the September FOMC. | Hot September CPI/PPI revives hike risk given three FOMC dissenters; Mega-cap tech leadership resumes and SPY outruns equal-weight and defensives; Crude reverses lower on Iran de-escalation, hitting the energy sleeve; Further payroll deterioration triggers a broad risk-off drawdown |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 4 | 0.55 | Core SPY with defensive quality and gold overweight to capture recent leadership while managing macro risk. | Hot Aug CPI/PPI reverses rate-cut hopes hurting gold and defensives; Risk-on growth rally leaves defensives lagging SPY; Gold pullback after strong run |
| openai-gpt-5-6-sol | openai | portfolio | SEMICONDUCTORS | 4 | 0.59 | All selected holdings have base forecasts above SPY's 0.70% forecast. The mix targets positive alpha while diversifying the primary technology thesis across healthcare and equal-weight US equities. | Semiconductor volatility and a renewed growth-stock selloff could overwhelm the pullback thesis.; Hot producer or consumer inflation could lift yields and compress technology valuations.; Weak September labor data could turn the current soft-landing interpretation into recession concern.; Recent healthcare and market-breadth leadership could reverse as prior laggards lose momentum.; Geopolitical escalation involving Iran and crude flows could create an inflation shock before exit. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.23 | 19.17 | 0.3471539002108224 | 1 |
| OIL | Crude Oil | 125.03 | 156.66 | 0.2529792849716068 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 35.88 | 44.74 | 0.24693422519509478 | 3 |
| BRAZIL | Brazil Equities | 33.77 | 37.72 | 0.11696772283091494 | 4 |
| BROAD_COMMODITIES | Broad Commodities | 17.77 | 19.78 | 0.11311198649409127 | 5 |
| ENERGY | Energy Sector | 61.06 | 64.53 | 0.056829348182115824 | 6 |
| AGRICULTURE | Agriculture Commodities | 27.62 | 28.96 | 0.04851556842867488 | 7 |
| YEN | Japanese Yen | 57.53 | 59.43 | 0.033026247175386825 | 8 |
| COMMUNICATIONS | Communication Services Sector | 112.55 | 115.07 | 0.02239004886717022 | 9 |
| SOUTH_AFRICA | South Africa Equities | 67.33 | 68.49 | 0.01722857567206293 | 10 |
| BIOTECH | Biotechnology | 156.86 | 157.6 | 0.004717582557694611 | 11 |
| SOFTWARE | Software | 106.28 | 106.64 | 0.0033872788859616865 | 12 |
| EURO | Euro | 106.3994 | 106.55 | 0.0014154215155348648 | 13 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 14 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.51 | 91.5 | -0.0001092776745711399 | 15 |
| US_DOLLAR | US Dollar | 28.18 | 28.17 | -0.0003548616039743546 | 16 |
| DIVIDEND | US Dividend Equities | 34.43 | 34.34 | -0.0026139994191111127 | 17 |
| TAIWAN | Taiwan Equities | 107.5 | 107.21 | -0.0026976744186046897 | 18 |
| HEALTHCARE | Healthcare Sector | 168.38 | 167.75 | -0.0037415369996436354 | 19 |
| UNITED_KINGDOM | United Kingdom Equities | 48.26 | 47.91 | -0.007252382925818535 | 20 |
| MEXICO | Mexico Equities | 75.45 | 74.82 | -0.0083499005964216 | 21 |
| JAPAN | Japan Equities | 98.47 | 97.58 | -0.009038285772316468 | 22 |
| EMERGING_MARKETS | Emerging Markets | 60.34 | 59.61 | -0.01209811070599942 | 23 |
| TIPS | Treasury Inflation-Protected Securities | 107.16 | 105.82 | -0.012504665920119451 | 24 |
| LARGE_VALUE | US Large-Cap Value | 258.7 | 255.37 | -0.012872052570545023 | 25 |
| SOUTH_KOREA | South Korea Equities | 178.62 | 176.22 | -0.01343634531407456 | 26 |
| GOLD | Gold | 81.78 | 80.54 | -0.015162631450232222 | 27 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.79 | 78.53 | -0.01579145256297787 | 28 |
| BROAD_AI_TECH | Broad AI Technology | 64.62 | 63.47 | -0.017796347879913466 | 29 |
| CONSUMER_STAPLES | Consumer Staples Sector | 86.0 | 84.42 | -0.01837209302325582 | 30 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.69 | 95.89 | -0.018425632101545686 | 31 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.59 | 80.93 | -0.020099285627799945 | 32 |
| CHINA | China Equities | 54.42 | 53.32 | -0.020213156927600173 | 33 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.91 | 46.93 | -0.020455019828845677 | 34 |
| CYBERSECURITY | Cybersecurity | 102.2 | 100.05 | -0.021037181996086174 | 35 |
| FINANCIALS | Financials Sector | 58.26 | 57.03 | -0.021112255406797065 | 36 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.55 | 104.3 | -0.021116846550915058 | 37 |
| SP500 | S&P 500 | 777.88 | 760.88 | -0.021854270581580737 | 38 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.36 | 93.22 | -0.02244127516778527 | 39 |
| SILVER | Silver | 58.16 | 56.84 | -0.022696011004126437 | 40 |
| AUSTRALIA | Australia Equities | 29.74 | 29.06 | -0.02286482851378613 | 41 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.49 | 91.22 | -0.024280671729596692 | 42 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.54 | 71.72 | -0.024748436225183634 | 43 |
| TOTAL_US_MARKET | Total US Stock Market | 384.3 | 374.68 | -0.025032526671870947 | 44 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.3 | 90.93 | -0.02540192926045004 | 45 |
| CANADA | Canada Equities | 62.1 | 60.5 | -0.025764895330112725 | 46 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.16 | 103.11 | -0.028730218538055685 | 47 |
| INDIA | India Equities | 49.98 | 48.43 | -0.031012404961984763 | 48 |
| NASDAQ100 | Nasdaq 100 | 732.07 | 709.18 | -0.03126750174163684 | 49 |
| LOW_VOL | US Low Volatility Equities | 76.23 | 73.82 | -0.031614849796668065 | 50 |
| SMALL_VALUE | US Small-Cap Value | 226.77 | 219.45 | -0.032279402037306615 | 51 |
| TECHNOLOGY | Technology Sector | 190.77 | 184.28 | -0.034020024112806024 | 52 |
| EUROPE | Europe Equities | 92.38 | 89.23 | -0.034098289673089366 | 53 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 222.73 | 215.01 | -0.03466080007183581 | 54 |
| MATERIALS | Materials Sector | 52.31 | 50.49 | -0.03479258268017593 | 55 |
| LARGE_GROWTH | US Large-Cap Growth | 125.66 | 121.26 | -0.03501512016552599 | 56 |
| COPPER | Copper | 39.85 | 38.26 | -0.03989962358845678 | 57 |
| METALS_MINING | Metals and Mining | 115.27 | 110.17 | -0.044243948989329374 | 58 |
| REAL_ESTATE | Real Estate Sector | 45.12 | 43.12 | -0.04432624113475181 | 59 |
| REGIONAL_BANKS | Regional Banks | 77.75 | 74.11 | -0.04681672025723471 | 60 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.45 | 112.85 | -0.0472773322076826 | 61 |
| UTILITIES | Utilities Sector | 44.04 | 41.82 | -0.05040871934604907 | 62 |
| SMALL_CAP | US Small-Cap Stocks | 303.5 | 287.91 | -0.05136738056013168 | 63 |
| MOMENTUM | US Momentum Equities | 316.03 | 299.7 | -0.051672309590861554 | 64 |
| MID_CAP | US Mid-Cap Stocks | 78.42 | 73.79 | -0.05904106095383821 | 65 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 130.1 | 119.595 | -0.08074558032282853 | 66 |
| SEMICONDUCTORS | Semiconductors | 589.12 | 541.5 | -0.08083242802824553 | 67 |
| INDUSTRIALS | Industrials Sector | 185.79 | 169.93 | -0.08536519726573 | 68 |
| SOLAR | Solar Energy | 52.47 | 46.22 | -0.11911568515342097 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 249.69 | 216.77 | -0.1318434859225439 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | portfolio | ENERGY | 4 | 0.58 | 0.056829348182115824 | 0.011327308336520993 | 0.03318157891810173 | 0.33582659187430136 |  | True | True |
| xai-grok-4-6 | portfolio | ENERGY | 4 | 0.56 | 0.056829348182115824 | 0.009046467551239001 | 0.03090073813281974 | 0.3381074326595834 |  | True | True |
| google-gemini-3-1-pro | portfolio | SP500 | 3 | 0.65 | -0.021854270581580737 | 0.0023448175048276787 | 0.024199088086408416 | 0.3448090827059947 |  | True | True |
| xai-grok-4-3 | portfolio | SP500 | 4 | 0.62 | -0.021854270581580737 | 6.819684939884984e-05 | 0.021922467430979586 | 0.3470857033614235 |  | True | True |
| anthropic-claude-fable-5 | portfolio | SP500 | 5 | 0.58 | -0.021854270581580737 | -0.0065537168719699505 | 0.015300553709610787 | 0.3537076170827923 |  | True | False |
| anthropic-claude-opus-5 | portfolio | SP500 | 5 | 0.55 | -0.021854270581580737 | -0.011643069405948246 | 0.01021120117563249 | 0.3587969696167706 |  | True | False |
| anthropic-claude-opus-4-8 | portfolio | SP500 | 4 | 0.55 | -0.021854270581580737 | -0.013101718685456315 | 0.008752551896124422 | 0.36025561889627866 |  | True | False |
| openai-gpt-5-6-sol | portfolio | SEMICONDUCTORS | 4 | 0.59 | -0.08083242802824553 | -0.04104751137716872 | -0.019193240795587985 | 0.3882014115879911 |  | False | False |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1M has no scored official run.
- Round CB-2026-08-15-1M has no scored official run.
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
- Round example-round has no scored official run.
- Round example-round-2 has no scored official run.
