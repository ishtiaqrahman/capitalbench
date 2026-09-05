# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-08-27-1W
- Decision deadline: 2026-08-28T13:25:00Z
- Horizon: one week
- Official run ID: official-v3-20260828-weekly
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | OIL | 3 | 0.58 | The market is showing mixed signals with some sectors experiencing pullbacks while others continue to show strength. The recent GDP and inflation data suggest a stable economic environment, but there are underlying concerns about specific sectors like energy and consumer discretionary. | Continued weakness in the energy sector despite inventory draws.; Further deterioration in consumer spending impacting the consumer discretionary sector. |
| openai-gpt-5-6-sol | openai | portfolio | ENERGY | 3 | 0.575 | High dispersion and narrow mega-cap leadership favor selective reversals over broad continuation. Elevated inflation and weak labor and consumption data create competing risks around the employment report, while rising yields constrain defensive and long-duration exposures. | A stronger-than-expected August employment report could lift yields and favor SPY over commodity-linked reversals.; Weak September 2 petroleum data could extend losses in energy and broad commodities.; A rapid reversal in inflation expectations or dollar strength could pressure commodity and precious-metal exposures.; Narrow AI-led equity momentum could persist and leave the selected reversal candidates behind. |
| xai-grok-4-5 | xai | portfolio | ENERGY | 3 | 0.5633 | SPY firm on mega-cap/tech strength post-NVIDIA; soft labor and mixed growth data with elevated but stable inflation; low-to-normal cross-sectional dispersion favors selective mean-reversion in quality pullbacks over pure momentum continuation into the short window. | Continued mega-cap/tech momentum could keep SPY elevated and delay mean-reversion in cyclicals and commodities; August employment report on 4 Sep may reprice rates and risk appetite sharply; High idiosyncratic vol in oil and energy complex can extend the recent shock rather than reverse; Soft retail sales and labor data may pressure consumer discretionary further if confirmed |
| anthropic-claude-fable-5 | anthropic | portfolio | SP500 | 2 | 0.58 | SPY up 1.11% on the week with narrow breadth (RSP -0.58% vs SPY, majority of S&P constituents declined on Aug 27), tech-led continuation after NVIDIA's strong report already printed. Dispersion 2.38% is moderate. Post-earnings, the biggest catalyst inside the window is the September 4 payrolls report; prior payrolls fell 23k, keeping rate-cut expectations alive. Best edge is in high-quality pullbacks (Energy) rather than chasing extended tech. | Further crude price weakness would drag XLE despite the quality pullback setup; September 4 payrolls surprise could reprice rates and hit both equities and metals; Narrow breadth reverses and extended tech leadership continues, leaving SPY hard to beat; Dollar rebound pressuring commodity-linked positions |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Mixed signals with software continuation supported by earnings strength offset by energy and commodity pullbacks amid stable macro data and rising yields. | Rising Treasury yields pressuring growth assets; NVIDIA China revenue assumption uncertainty; September employment data volatility; Commodity inventory revisions |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | SPY is near a 52-week high with mega-cap/Nasdaq leadership (NVDA print) while a majority of S&P names fell, equal-weight lagged, and 5-session active dispersion is only 2.38%. Labor softening and the Aug payrolls print on 2026-09-04 sit inside the scoring window, so one-week edges versus SPY are mixed rather than a clean continuation or reversal regime. | BLS August employment on 2026-09-04 can reprice rates, growth, and mega-cap leadership inside the exit close.; Elevated PCE/CPI prints and a still-restrictive funds range leave duration-sensitive defensives and cyclicals two-way.; High-vol continuations (software, crypto, Korea) can reverse without volume confirmation.; Oil/energy bounce can fail if commercial inventories keep building despite SPR draws. |
| anthropic-claude-opus-5 | anthropic | portfolio | CONSUMER_DISCRETIONARY | 3 | 0.555 | SPY is near highs after a strong 21-day run (+5.71%) led by mega-cap tech and a blowout NVIDIA print, while breadth is weak (RSP -3.06% active over 21 sessions, majority of S&P constituents down on Aug 27). Rates rose modestly with 10y at 4.67% and PCE at 3.7% y/y, keeping duration and rate-sensitive defensives capped. The week contains the August employment report on Sept 4, the exact exit date, which caps conviction in high-beta reversal bets. Dispersion (2.38% weekly active) is normal, so few candidates carry genuine mechanical edge; most slate pullbacks look like modest noise rather than exploitable overreaction. | August employment report on September 4 lands at the exit close and can reprice high-beta and rate-sensitive positions within the scoring window; Mega-cap tech leadership post-NVIDIA can keep SPY ahead of the weak-breadth reversal candidates; China exposure is subject to policy and geopolitical headlines with sub-50 PMIs signaling genuine slowdown; Rising long yields (30y 5.19%) with 3.7% PCE inflation could pressure cyclicals and discretionary consumption; Crude inventory and OPEC surprises could extend energy weakness rather than reverse it |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 129.7 | 141.96 | 0.0945258288357751 | 1 |
| BRAZIL | Brazil Equities | 35.55 | 37.86 | 0.06497890295358655 | 2 |
| SOUTH_KOREA | South Korea Equities | 180.2 | 188.87 | 0.04811320754716997 | 3 |
| TAIWAN | Taiwan Equities | 107.9 | 112.18 | 0.03966635773864691 | 4 |
| BROAD_COMMODITIES | Broad Commodities | 18.39 | 19.01 | 0.033713974986405715 | 5 |
| BITCOIN_ETF | Bitcoin ETF | 43.9 | 45.23 | 0.030296127562642328 | 6 |
| JAPAN | Japan Equities | 95.87 | 98.28 | 0.02513820798998645 | 7 |
| SEMICONDUCTORS | Semiconductors | 553.11 | 567.01 | 0.0251306250112997 | 8 |
| YEN | Japanese Yen | 57.25 | 58.67 | 0.02480349344978161 | 9 |
| ENERGY | Energy Sector | 62.68 | 64.06 | 0.022016592214422426 | 10 |
| MOMENTUM | US Momentum Equities | 299.71 | 304.86 | 0.017183277167929223 | 11 |
| REGIONAL_BANKS | Regional Banks | 74.3 | 75.27 | 0.013055181695827756 | 12 |
| SOUTH_AFRICA | South Africa Equities | 70.72 | 71.64 | 0.01300904977375561 | 13 |
| EMERGING_MARKETS | Emerging Markets | 60.79 | 61.44 | 0.010692548116466583 | 14 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.06 | 73.76 | 0.009581166164796207 | 15 |
| BIOTECH | Biotechnology | 162.38 | 163.81 | 0.008806503263948828 | 16 |
| TECHNOLOGY | Technology Sector | 185.69 | 187.28 | 0.008562658193763895 | 17 |
| UTILITIES | Utilities Sector | 42.73 | 43.08 | 0.008190966534051158 | 18 |
| ETHEREUM_ETF | Ethereum ETF | 18.37 | 18.52 | 0.008165487207403288 | 19 |
| AUSTRALIA | Australia Equities | 30.0 | 30.23 | 0.0076666666666667105 | 20 |
| INDIA | India Equities | 49.56 | 49.91 | 0.007062146892655274 | 21 |
| COPPER | Copper | 39.67 | 39.95 | 0.007058230400806664 | 22 |
| SMALL_VALUE | US Small-Cap Value | 223.14 | 224.62 | 0.006632607331719997 | 23 |
| LARGE_GROWTH | US Large-Cap Growth | 122.75 | 123.41 | 0.005376782077393116 | 24 |
| CANADA | Canada Equities | 61.73 | 62.04 | 0.005021869431394821 | 25 |
| NASDAQ100 | Nasdaq 100 | 716.43 | 718.96 | 0.003531398740979741 | 26 |
| MEXICO | Mexico Equities | 76.48 | 76.63 | 0.001961297071129575 | 27 |
| HEALTHCARE | Healthcare Sector | 171.16 | 171.45 | 0.0016943211030613359 | 28 |
| EURO | Euro | 106.978 | 107.15 | 0.0016078072126981535 | 29 |
| BROAD_AI_TECH | Broad AI Technology | 64.22 | 64.32 | 0.0015571473061350982 | 30 |
| MID_CAP | US Mid-Cap Stocks | 75.76 | 75.85 | 0.0011879619852164236 | 31 |
| SP500 | S&P 500 | 769.35 | 770.19 | 0.0010918307662313165 | 32 |
| TOTAL_US_MARKET | Total US Stock Market | 379.36 | 379.73 | 0.000975326866301085 | 33 |
| SMALL_CAP | US Small-Cap Stocks | 295.75 | 296.01 | 0.0008791208791207872 | 34 |
| UNITED_KINGDOM | United Kingdom Equities | 48.55 | 48.59 | 0.0008238928939239276 | 35 |
| TIPS | Treasury Inflation-Protected Securities | 106.94 | 106.97 | 0.0002805311389564302 | 36 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 37 |
| FINANCIALS | Financials Sector | 58.1 | 58.1 | 0.0 | 37 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.32 | 122.25 | -0.0005722694571614895 | 39 |
| METALS_MINING | Metals and Mining | 118.74 | 118.62 | -0.001010611419908991 | 40 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.65 | 91.45 | -0.0021822149481723896 | 41 |
| EUROPE | Europe Equities | 91.98 | 91.74 | -0.002609262883235597 | 42 |
| LARGE_VALUE | US Large-Cap Value | 258.33 | 257.63 | -0.0027097123833855763 | 43 |
| DIVIDEND | US Dividend Equities | 34.9 | 34.8 | -0.002865329512893977 | 44 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.6 | 47.45 | -0.0031512605042016695 | 45 |
| SILVER | Silver | 60.02 | 59.82 | -0.003332222592469236 | 46 |
| US_DOLLAR | US Dollar | 28.18 | 28.08 | -0.0035486160397445454 | 47 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.89 | 94.47 | -0.0044261776794183305 | 48 |
| LOW_VOL | US Low Volatility Equities | 75.08 | 74.74 | -0.0045285029302077895 | 49 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.17 | 92.715 | -0.00488354620586029 | 50 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.49 | 97.0 | -0.005026156528874726 | 51 |
| GOLD | Gold | 83.82 | 83.39 | -0.005130040563111393 | 52 |
| CHINA | China Equities | 55.23 | 54.91 | -0.005793952562013427 | 53 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.85 | 92.25 | -0.006462035541195399 | 54 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.74 | 79.16 | -0.007273639327815329 | 55 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.69 | 219.0 | -0.007657800534686676 | 56 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.88 | 82.21 | -0.00808397683397688 | 57 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.35 | 105.48 | -0.008180535966149427 | 58 |
| COMMUNICATIONS | Communication Services Sector | 112.99 | 112.03 | -0.008496327108593604 | 59 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.45 | 84.58 | -0.010181392627267472 | 60 |
| INDUSTRIALS | Industrials Sector | 177.14 | 175.27 | -0.01055662188099793 | 61 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.22 | 104.03 | -0.011309636951149948 | 62 |
| AGRICULTURE | Agriculture Commodities | 29.19 | 28.85 | -0.011647824597464829 | 63 |
| REAL_ESTATE | Real Estate Sector | 44.48 | 43.93 | -0.01236510791366896 | 64 |
| SOLAR | Solar Energy | 48.65 | 48.04 | -0.012538540596094494 | 65 |
| MATERIALS | Materials Sector | 53.18 | 52.44 | -0.013915005641218503 | 66 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.21 | 114.91 | -0.01962289907004522 | 67 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 232.82 | 225.61 | -0.030968129885748596 | 68 |
| CYBERSECURITY | Cybersecurity | 98.56 | 94.59 | -0.04028003246753242 | 69 |
| SOFTWARE | Software | 109.5 | 104.57 | -0.04502283105022842 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | portfolio | OIL | 3 | 0.58 | 0.0945258288357751 | 0.03490297764655556 | 0.033811146880324244 | 0.05962285118921953 |  | True | True |
| openai-gpt-5-6-sol | portfolio | ENERGY | 3 | 0.575 | 0.022016592214422426 | 0.019833247750159242 | 0.018741416983927926 | 0.07469258108561586 |  | True | True |
| xai-grok-4-5 | portfolio | ENERGY | 3 | 0.5633 | 0.022016592214422426 | 0.010951985096453737 | 0.00986015433022242 | 0.08357384373932136 |  | True | True |
| anthropic-claude-fable-5 | portfolio | SP500 | 2 | 0.58 | 0.0010918307662313165 | 0.008415497273098205 | 0.007323666506866888 | 0.08611033156267689 |  | True | True |
| xai-grok-4-3 | portfolio | SP500 | 1 | 0.5 | 0.0010918307662313165 | 0.0010918307662313165 | 0.0 | 0.09343399806954378 |  | False | True |
| xai-grok-4-6 | portfolio | SP500 | 1 | 0.5 | 0.0010918307662313165 | 0.0010918307662313165 | 0.0 | 0.09343399806954378 |  | False | True |
| anthropic-claude-opus-5 | portfolio | CONSUMER_DISCRETIONARY | 3 | 0.555 | -0.01962289907004522 | -0.008568348841351131 | -0.009660179607582448 | 0.10309417767712623 |  | False | False |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1W has no scored official run.
- Round CB-2026-08-30-1W has no scored official run.
- Round CB-2026-09-01-1W has no scored official run.
- Round CB-2026-09-02-1W has no scored official run.
- Round CB-2026-09-03-1W has no scored official run.
- Round CB-2026-09-04-1W has no scored official run.
