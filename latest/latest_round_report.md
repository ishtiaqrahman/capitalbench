# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-07-31-1M
- Decision deadline: 2026-08-03T12:30:00Z
- Horizon: one month
- Official run ID: official-v2-2-all-monthly-20260731-clean
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | ENERGY | 5 | 0.58 | SPY base is modest given mixed July close and elevated macro uncertainty; selected holdings clear the active hurdle on recent relative strength plus catalysts inside the scoring window. Energy pair dominates expected return contribution. | Sudden de-escalation in Middle East oil logistics removing the risk premium; Higher-than-expected core inflation prints forcing rate-hike repricing; Tech earnings disappointment reversing the software bounce; Broad risk-off move hitting high-beta energy and growth names simultaneously |
| openai-gpt-5-6-sol | openai | portfolio | LARGE_VALUE | 4 | 0.58 | Favor independently supported relative trends and near-term catalysts while avoiding the most extreme high-volatility rebound trades. The principal edge is diversified active exposure rather than a single concentrated macro bet. | A benign Hormuz agreement could rapidly unwind the oil and energy risk premium.; Hot August inflation or hawkish Fed minutes could pressure equities and strengthen the dollar against the yen.; Technology leadership could reverse after earnings despite strong cybersecurity trend evidence.; Weak payrolls or consumption data could trigger a broad risk-off move that overwhelms factor selection. |
| openai-gpt-5-5 | openai | portfolio | LARGE_VALUE | 4 | 0.56 | SPY has a positive but modest base case after a flat July and elevated inflation/rate uncertainty. The selected basket targets stronger one-month catalysts from value breadth, tech earnings, energy disruption, and international catch-up. | A broad risk-off move could cause all equity holdings to underperform SPY or decline together.; A confirmed Strait of Hormuz reopening or de-escalation could sharply reverse oil exposure.; Hot CPI/PCE data or hawkish Fed minutes could pressure equities and duration-sensitive valuation multiples.; Nvidia, AMD, or other technology earnings read-throughs could disappoint and weaken cybersecurity sentiment. |
| anthropic-claude-fable-5 | anthropic | portfolio | SP500 | 5 | 0.58 | Overweight energy on constrained oil supply and negative equity correlation; overweight value/dividend/equal-weight on breadth rotation and rate pressure on growth; SPY core for balance. | A sudden Iran agreement reopening the Strait of Hormuz could sharply reverse energy gains; Cooler-than-expected August CPI could reignite growth/tech leadership and hurt the value tilt; Weak July payrolls could pressure cyclicals and financial-heavy value indexes; Nvidia results late August could restore narrow mega-cap dominance vs equal-weight |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.65 | Balanced approach with value and defensive tilts. | Unexpected inflation spikes leading to tighter monetary policy.; Geopolitical tensions escalating, particularly in the Middle East.; A broader economic slowdown impacting corporate earnings. |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | SPY is the default when no active holdings show superior base-case expected return over the one-month window. | FOMC policy uncertainty with 3 dissenters favoring hike; Elevated inflation prints in August data releases |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 5 | 0.53 | Modest positive SPY base case with sticky inflation and a hawkish-leaning Fed; tilt toward lower-volatility, near-highs relative winners with independent macro support rather than extended high-beta tech. | Sticky core inflation (3.3-3.4%) pushes yields above 5% and compresses equity multiples; Mega-cap AI capex enthusiasm resumes and SPY outruns the value/defensive tilt; Middle East oil disruption reverses or worsens, whipsawing sector leadership; Weak August payrolls signal a growth scare hitting financials and cyclicals; Currency swings erode Europe's USD-denominated return |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 4 | 0.55 | Defensive-cyclical quality tilt with financials and value leadership, anchored by SP500 core, aiming for modest alpha in an elevated-rate, uncertain macro backdrop. | Rate volatility around CPI and Fed minutes could hit rate-sensitive value/dividend names; Mega-cap tech rebound could cause SP500 to outperform value tilt; Geopolitical oil shock disrupting broad risk sentiment |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.069999694824219 | 18.719999313354492 | 0.3304903851732719 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 35.63999938964844 | 44.66999816894531 | 0.2533669734551012 | 2 |
| METALS_MINING | Metals and Mining | 100.6500015258789 | 118.12999725341797 | 0.17367109252397417 | 3 |
| SOFTWARE | Software | 94.58000183105469 | 109.9800033569336 | 0.1628251345711269 | 4 |
| SOUTH_KOREA | South Korea Equities | 157.10000610351562 | 180.86000061035156 | 0.1512412067710558 | 5 |
| SILVER | Silver | 52.36000061035156 | 60.130001068115234 | 0.14839572893793185 | 6 |
| TAIWAN | Taiwan Equities | 96.55000305175781 | 108.02999877929688 | 0.11890207524265906 | 7 |
| SOUTH_AFRICA | South Africa Equities | 63.619998931884766 | 70.5 | 0.10814211228581372 | 8 |
| BIOTECH | Biotechnology | 147.00999450683594 | 162.5 | 0.10536702314102708 | 9 |
| GOLD | Gold | 76.16999816894531 | 83.70999908447266 | 0.098989117720649 | 10 |
| BROAD_AI_TECH | Broad AI Technology | 58.88999938964844 | 64.30000305175781 | 0.0918662543416553 | 11 |
| CYBERSECURITY | Cybersecurity | 91.83000183105469 | 100.1500015258789 | 0.09060219458702656 | 12 |
| ENERGY | Energy Sector | 59.54999923706055 | 63.959999084472656 | 0.07405541400355853 | 13 |
| AGRICULTURE | Agriculture Commodities | 27.510000228881836 | 29.31999969482422 | 0.06579423667332884 | 14 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 115.06999969482422 | 122.5 | 0.06456939536700101 | 15 |
| TECHNOLOGY | Technology Sector | 175.35000610351562 | 186.5 | 0.06358707447037171 | 16 |
| BROAD_COMMODITIES | Broad Commodities | 17.559999465942383 | 18.649999618530273 | 0.06207290351585404 | 17 |
| HEALTHCARE | Healthcare Sector | 162.5500030517578 | 170.5399932861328 | 0.04915404542829127 | 18 |
| MATERIALS | Materials Sector | 50.43000030517578 | 52.689998626708984 | 0.04481456093311298 | 19 |
| DIVIDEND | US Dividend Equities | 33.470001220703125 | 34.88999938964844 | 0.042425996927271115 | 20 |
| NASDAQ100 | Nasdaq 100 | 687.989990234375 | 716.760009765625 | 0.041817497259588166 | 21 |
| JAPAN | Japan Equities | 92.38999938964844 | 95.87999725341797 | 0.037774628063917515 | 22 |
| LARGE_GROWTH | US Large-Cap Growth | 118.31999969482422 | 122.70999908447266 | 0.037102767080555266 | 23 |
| OIL | Crude Oil | 129.1699981689453 | 133.6999969482422 | 0.035070053754835184 | 24 |
| CANADA | Canada Equities | 59.38999938964844 | 61.43000030517578 | 0.0343492328084265 | 25 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.62000274658203 | 72.91999816894531 | 0.032568611341134535 | 26 |
| EMERGING_MARKETS | Emerging Markets | 58.75 | 60.52000045776367 | 0.030127667366190103 | 27 |
| SEMICONDUCTORS | Semiconductors | 540.530029296875 | 556.6300048828125 | 0.02978553403754547 | 28 |
| COMMUNICATIONS | Communication Services Sector | 108.23999786376953 | 111.45999908447266 | 0.029748718442842215 | 29 |
| TOTAL_US_MARKET | Total US Stock Market | 368.2099914550781 | 378.1499938964844 | 0.026995471801636084 | 30 |
| SP500 | S&P 500 | 747.030029296875 | 767.0499877929688 | 0.0267994025821654 | 31 |
| AUSTRALIA | Australia Equities | 29.34000015258789 | 30.020000457763672 | 0.023176561064734758 | 32 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 215.00999450683594 | 219.38999938964844 | 0.0203711687582655 | 33 |
| LARGE_VALUE | US Large-Cap Value | 251.82000732421875 | 256.9100036621094 | 0.02021283531827267 | 34 |
| FINANCIALS | Financials Sector | 56.939998626708984 | 57.709999084472656 | 0.013523015039246689 | 35 |
| EUROPE | Europe Equities | 90.58999633789062 | 91.66000366210938 | 0.011811539546019434 | 36 |
| COPPER | Copper | 39.560001373291016 | 40.0 | 0.011122310703610028 | 37 |
| SMALL_CAP | US Small-Cap Stocks | 291.20001220703125 | 293.92999267578125 | 0.00937493253540489 | 38 |
| EURO | Euro | 106.48999786376953 | 107.25 | 0.007136840562272484 | 39 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.08999633789062 | 116.58999633789062 | 0.004307003323048564 | 40 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.4800033569336 | 79.80999755859375 | 0.004151914792683176 | 41 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.25 | 82.5199966430664 | 0.003282633958254122 | 42 |
| MOMENTUM | US Momentum Equities | 299.5899963378906 | 300.3599853515625 | 0.002570142605173853 | 43 |
| SMALL_VALUE | US Small-Cap Value | 221.24000549316406 | 221.8000030517578 | 0.002531176752348596 | 44 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.91999816894531 | 93.0999984741211 | 0.001937153559220972 | 45 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.66000366210938 | 94.7699966430664 | 0.0011619794707558029 | 46 |
| MID_CAP | US Mid-Cap Stocks | 75.2699966430664 | 75.3499984741211 | 0.0010628648149682007 | 47 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.37000274658203 | 97.41000366210938 | 0.00041081354009464555 | 48 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 49 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.68000030517578 | 91.66000366210938 | -0.00021811347076616805 | 50 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.25 | 106.20999908447266 | -0.0003764792049631982 | 51 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.05000305175781 | 84.9800033569336 | -0.0008230416497647663 | 52 |
| UNITED_KINGDOM | United Kingdom Equities | 48.40999984741211 | 48.369998931884766 | -0.000826294477451528 | 53 |
| MEXICO | Mexico Equities | 76.80999755859375 | 76.72000122070312 | -0.0011716747917088766 | 54 |
| US_DOLLAR | US Dollar | 28.170000076293945 | 28.1200008392334 | -0.0017749107889645233 | 55 |
| INDIA | India Equities | 49.79999923706055 | 49.70000076293945 | -0.0020080015191380474 | 56 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.94999694824219 | 92.73999786376953 | -0.0022592694068573893 | 57 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.77000045776367 | 47.54999923706055 | -0.004605426388840872 | 58 |
| YEN | Japanese Yen | 57.65999984741211 | 57.38999938964844 | -0.004682630219878359 | 59 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.63999938964844 | 105.0999984741211 | -0.00511170880961076 | 60 |
| TIPS | Treasury Inflation-Protected Securities | 107.62999725341797 | 106.81999969482422 | -0.007525760283042526 | 61 |
| BRAZIL | Brazil Equities | 36.650001525878906 | 36.029998779296875 | -0.01691685459124037 | 62 |
| CHINA | China Equities | 55.79999923706055 | 54.720001220703125 | -0.019354803425160716 | 63 |
| LOW_VOL | US Low Volatility Equities | 76.2300033569336 | 74.69000244140625 | -0.020202031322451353 | 64 |
| REAL_ESTATE | Real Estate Sector | 45.06999969482422 | 44.11000061035156 | -0.0213001795201454 | 65 |
| INDUSTRIALS | Industrials Sector | 179.83999633789062 | 175.1300048828125 | -0.026189899638503156 | 66 |
| REGIONAL_BANKS | Regional Banks | 76.05999755859375 | 73.55999755859375 | -0.03286878885414235 | 67 |
| SOLAR | Solar Energy | 49.33000183105469 | 47.56999969482422 | -0.03567812833776329 | 68 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 239.66000366210938 | 228.35000610351562 | -0.047191844220028645 | 69 |
| UTILITIES | Utilities Sector | 44.349998474121094 | 42.22999954223633 | -0.04780155591486246 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | portfolio | ENERGY | 5 | 0.58 | 0.07405541400355853 | 0.06490677140745171 | 0.038107368825286314 | 0.2655836137658202 |  | True | True |
| openai-gpt-5-6-sol | portfolio | LARGE_VALUE | 4 | 0.58 | 0.02021283531827267 | 0.0462917266991524 | 0.019492324116987002 | 0.2841986584741195 |  | True | True |
| openai-gpt-5-5 | portfolio | LARGE_VALUE | 4 | 0.56 | 0.02021283531827267 | 0.03942415580153846 | 0.012624753219373064 | 0.29106622937173343 |  | True | True |
| anthropic-claude-fable-5 | portfolio | SP500 | 5 | 0.58 | 0.0267994025821654 | 0.03867584606291601 | 0.011876443480750613 | 0.2918145391103559 |  | True | True |
| google-gemini-3-1-pro | portfolio | SP500 | 3 | 0.65 | 0.0267994025821654 | 0.030741421477723685 | 0.003942018895558286 | 0.2997489636955482 |  | True | True |
| xai-grok-4-3 | portfolio | SP500 | 1 | 0.5 | 0.0267994025821654 | 0.0267994025821654 | 0.0 | 0.3036909825911065 |  | False | True |
| anthropic-claude-opus-5 | portfolio | SP500 | 5 | 0.53 | 0.0267994025821654 | 0.024681221744107393 | -0.0021181808380580057 | 0.3058091634291645 |  | False | True |
| anthropic-claude-opus-4-8 | portfolio | FINANCIALS | 4 | 0.55 | 0.013523015039246689 | 0.024295163372337746 | -0.0025042392098276536 | 0.30619522180093417 |  | False | True |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1M has no scored official run.
- Round CB-2026-08-04-1M has no scored official run.
- Round CB-2026-08-05-1M has no scored official run.
- Round CB-2026-08-07-1M has no scored official run.
- Round CB-2026-08-09-1M has no scored official run.
- Round CB-2026-08-11-1M has no scored official run.
- Round CB-2026-08-13-1M has no scored official run.
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
- Round example-round has no scored official run.
- Round example-round-2 has no scored official run.
