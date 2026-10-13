# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-09-11-1M
- Decision deadline: 2026-09-11T13:25:00Z
- Horizon: one month
- Official run ID: official-v3-20260911-monthly
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 2 | 0.58 | Energy and select tech showing continuation amid broad equity pullback and rate pressure; limited reversal signals in quality names. | Oil volatility from inventory data; Rate path uncertainty post-ECB; Broad equity breadth weakness |
| anthropic-claude-opus-5 | anthropic | portfolio | CYBERSECURITY | 3 | 0.57 | Broad weakness with narrow leadership: SPY -0.96% over 5 sessions, equal-weight lagging by 1.5pp, only ~22% of assets positive. Inflation data is hot (PPI +0.4% m/m, 5.4% y/y; 10y at 4.95%; Brent +6.3% to $107.63), which pressures duration and rate-sensitive equities and supports energy. FOMC Sept 15-16 plus CPI are near-term binary events. Best risk-adjusted setups are high-quality pullbacks (CIBR, IWM/IWN, RSP-like breadth names) rather than chasing oil or crypto momentum. | Hot August CPI on Sept 11 plus a hawkish Sept 15-16 FOMC could lift the 10y above 4.95% and hit small caps and high-beta tech hardest; Brent at $107.63 sustains an inflation shock that compresses margins and consumer demand into October; Breadth deterioration (2.3-to-1 decliners, RSP lagging SPY by 1.76pp over 21 sessions) could persist, favoring mega-cap SPY over the small-cap and thematic tilts; Cybersecurity carries 31.4% volatility, so a growth-factor unwind can overwhelm the pullback thesis within one month |
| openai-gpt-6-astra | openai | portfolio | SP500 | 1 | 0.5 | Large differences between energy, crypto and lagging cyclicals indicate high dispersion, although the aggregate dispersion statistic is missing. Inflation pressure, elevated yields and weak breadth argue against indiscriminate dip buying. Oil has independent inventory support, but its advance already discounts considerable strength. Quality pullbacks offer tentative reversal opportunities rather than compelling one-month edges. CPI occurs before the entry close, so its immediate reaction cannot be captured. | Unknown September 11 CPI can materially change entry prices before the strategy begins earning returns.; The September 15–16 FOMC projections and September 30 PCE release could extend rate pressure or trigger a sharp growth-stock rebound.; Oil could reverse its large advance because crude inventories are at their five-year average, despite tighter product inventories.; October 2 employment and September retail-sales data could overturn the tentative domestic-demand assessment.; No sector earnings, valuation or balance-sheet evidence is supplied; technical pullbacks may conceal genuine deterioration. |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | Narrow equity weakness (SPY -0.96% 5s, RSP lagging, 21.7% positive share) coincides with a PPI goods/energy spike, ECB hike, 4.95% 10y, and a large oil continuation; breadth and rates argue against high-beta continuation while oil/crypto already stretched. | Unknown August CPI on Sep 11 and FOMC Sep 15-16 can reprice duration and growth stocks inside the window.; Further crude strength after Brent $107.63 and tight distillate stocks can keep inflation sticky and pressure cyclicals.; High-beta slate names (SMH, TAN, ETHA, ARKQ) have 30-50% horizon vol and large drawdowns, so reversal or continuation both have wide error bands. |
| xai-grok-4-5 | xai | portfolio | SMALL_CAP | 3 | 0.5633 | Elevated cross-sectional dispersion with oil/crypto strength versus broad equity weakness, sticky PPI, ECB hike, and soft housing; mixed continuation in energy/tech versus potential mean-reversion in quality pullbacks and shock losers over one-month window. | Unknown September 11 CPI print and mid-September FOMC could reverse rate-sensitive small-cap and growth tilts; Oil continuation or further PPI stickiness may sustain energy outperformance and pressure equities; High-vol names (semis, Taiwan, crypto) remain vulnerable to sharp drawdowns if risk appetite fades; ECB hike and European growth downside could spill into global risk assets before October exit |
| anthropic-claude-fable-5-1 | anthropic | portfolio | AEROSPACE_DEFENSE | 3 | 0.56 | Stagflation-tinged tape: PPI hot (0.4% m/m, 5.4% y/y), Brent +6.3% to $107.63, 10y at 4.95%, ECB hiking, mortgage rates rising. Equities soft with weak breadth (RSP lagging SPY by 1.8% over 21 sessions, only 22% of assets positive). FOMC Sept 15-16 and CPI Sept 11 are binary catalysts inside the window. Energy/commodities are the continuation leaders; cyclical industrials and defense are the recent shock losers. Given hot inflation and oil, I treat defensive/quality and energy-linked exposure as most favorable versus SPY, and give measured reversal credit only where the drawdown looks like a sentiment washout rather than a fundamental hit. | Hot CPI on Sept 11 or a hawkish FOMC (Sept 15-16) could extend the equity drawdown, hurting beta-1 cyclicals like ITA and XLI more than SPY; Oil reversal from $107 Brent would unwind energy-linked leadership and could favor the discretionary/tech names ranked low here; Defense and industrials weakness may reflect unreported fundamental news not in the briefing, making the overreaction label wrong; Continued mega-cap tech leadership would keep cap-weighted SPY ahead of equal-weight and cyclical exposures |
| google-gemini-3-1-pro | google | portfolio | AEROSPACE_DEFENSE | 3 | 0.58 | The market is experiencing a mixed environment with some sectors showing strength while others pull back. The ECB rate hike and upcoming US economic data releases add uncertainty. | Unexpected inflation data from the upcoming CPI release could negatively impact equities.; Further rate hikes or hawkish signals from central banks could increase market volatility. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 19.15999984741211 | 56.95000076293945 | 1.9723382680836261 | 1 |
| CYBERSECURITY | Cybersecurity | 94.4 | 107.8 | 0.14194915254237284 | 2 |
| BRAZIL | Brazil Equities | 38.19 | 43.540000915527344 | 0.14008905251446313 | 3 |
| SOFTWARE | Software | 101.52 | 111.28 | 0.09613869188337287 | 4 |
| BITCOIN_ETF | Bitcoin ETF | 43.77000045776367 | 46.86000061035156 | 0.07059630158262431 | 5 |
| TECHNOLOGY | Technology Sector | 187.67 | 196.36 | 0.046304683753397136 | 6 |
| NASDAQ100 | Nasdaq 100 | 714.88 | 746.04 | 0.043587735004476214 | 7 |
| HEALTHCARE | Healthcare Sector | 165.36 | 171.99 | 0.04009433962264142 | 8 |
| LARGE_GROWTH | US Large-Cap Growth | 122.27 | 127.13 | 0.03974809847059779 | 9 |
| SEMICONDUCTORS | Semiconductors | 568.53 | 590.99 | 0.03950539109633633 | 10 |
| US_DOLLAR | US Dollar | 28.06999969482422 | 29.1299991607666 | 0.0377627174017332 | 11 |
| COPPER | Copper | 39.18 | 40.630001068115234 | 0.03700870515863275 | 12 |
| BROAD_AI_TECH | Broad AI Technology | 63.98 | 65.92 | 0.03032197561738048 | 13 |
| TAIWAN | Taiwan Equities | 110.91 | 114.2699966430664 | 0.030294803381718527 | 14 |
| MOMENTUM | US Momentum Equities | 307.04 | 315.09 | 0.02621808233454903 | 15 |
| SP500 | S&P 500 | 764.29 | 778.1 | 0.01806905755668664 | 16 |
| TOTAL_US_MARKET | Total US Stock Market | 376.31 | 381.57 | 0.013977837421274897 | 17 |
| ENERGY | Energy Sector | 65.14 | 66.01 | 0.013355848940743043 | 18 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.38 | 84.41 | 0.012353082273926619 | 19 |
| BROAD_COMMODITIES | Broad Commodities | 19.79 | 19.86 | 0.0035371399696817463 | 20 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 121.36 | 121.6 | 0.0019775873434408897 | 21 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 22 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.5 | 91.5 | 0.0 | 22 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.99 | 46.970001220703125 | -0.00042559649493245644 | 24 |
| LARGE_VALUE | US Large-Cap Value | 255.58 | 254.65 | -0.0036387823773378347 | 25 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.96 | 112.27 | -0.006108356940509929 | 26 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 214.87 | 213.19 | -0.007818681062968347 | 27 |
| COMMUNICATIONS | Communication Services Sector | 112.6 | 111.45 | -0.010213143872113584 | 28 |
| EMERGING_MARKETS | Emerging Markets | 60.35 | 59.73 | -0.010273405136702607 | 29 |
| JAPAN | Japan Equities | 98.56 | 97.32 | -0.012581168831168887 | 30 |
| TIPS | Treasury Inflation-Protected Securities | 105.84 | 104.5 | -0.012660619803476991 | 31 |
| LOW_VOL | US Low Volatility Equities | 73.79 | 72.79 | -0.0135519718118986 | 32 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 95.98 | 94.66 | -0.013752865180245988 | 33 |
| CHINA | China Equities | 52.96 | 52.15 | -0.015294561933534734 | 34 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.6 | 77.29 | -0.016666666666666496 | 35 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 104.32 | 102.58 | -0.016679447852760654 | 36 |
| AGRICULTURE | Agriculture Commodities | 28.93 | 28.440000534057617 | -0.016937416728046384 | 37 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 91.38 | 89.83000183105469 | -0.01696211609701581 | 38 |
| MID_CAP | US Mid-Cap Stocks | 74.44 | 73.16 | -0.017195056421278943 | 39 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 91.01 | 89.43 | -0.01736072959015489 | 40 |
| UTILITIES | Utilities Sector | 42.39 | 41.63 | -0.017928756782259914 | 41 |
| CANADA | Canada Equities | 60.58 | 59.45 | -0.018653020798943487 | 42 |
| INDUSTRIALS | Industrials Sector | 172.37 | 169.15 | -0.018680744909206903 | 43 |
| MUNICIPAL_BONDS | Municipal Bonds | 103.17 | 101.16000366210938 | -0.019482372180775642 | 44 |
| AUSTRALIA | Australia Equities | 29.27 | 28.670000076293945 | -0.02049880162986173 | 45 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 93.34 | 91.08000183105469 | -0.02421253662894063 | 46 |
| OIL | Crude Oil | 154.9 | 151.02999877929688 | -0.02498386843578526 | 47 |
| DIVIDEND | US Dividend Equities | 34.12 | 33.26 | -0.02520515826494718 | 48 |
| UNITED_KINGDOM | United Kingdom Equities | 47.94 | 46.7 | -0.025865665415102157 | 49 |
| MEXICO | Mexico Equities | 75.38 | 73.23999786376953 | -0.02838952157376573 | 50 |
| MATERIALS | Materials Sector | 50.95 | 49.44 | -0.029636898920510357 | 51 |
| BIOTECH | Biotechnology | 156.2 | 151.4 | -0.030729833546734864 | 52 |
| YEN | Japanese Yen | 59.68000030517578 | 57.779998779296875 | -0.031836486530884445 | 53 |
| REAL_ESTATE | Real Estate Sector | 43.42 | 41.92 | -0.03454629203132198 | 54 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 80.87 | 78.05 | -0.034870780264622314 | 55 |
| EURO | Euro | 107.01000213623047 | 102.98999786376953 | -0.03756662173824854 | 56 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.69 | 69.95 | -0.03769431833814818 | 57 |
| SMALL_CAP | US Small-Cap Stocks | 288.89 | 277.9 | -0.03804216137630245 | 58 |
| FINANCIALS | Financials Sector | 57.25 | 55.05 | -0.0384279475982533 | 59 |
| SMALL_VALUE | US Small-Cap Value | 219.69 | 211.09 | -0.03914606946151389 | 60 |
| GOLD | Gold | 81.71 | 78.34 | -0.04124342185778962 | 61 |
| INDIA | India Equities | 48.57 | 46.36 | -0.04550133827465519 | 62 |
| EUROPE | Europe Equities | 90.02 | 85.82 | -0.046656298600311064 | 63 |
| REGIONAL_BANKS | Regional Banks | 73.9 | 69.56 | -0.05872801082543988 | 64 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 219.01 | 206.03 | -0.05926670015067803 | 65 |
| SILVER | Silver | 58.12 | 54.349998474121094 | -0.06486582116102724 | 66 |
| METALS_MINING | Metals and Mining | 113.63 | 104.85 | -0.07726832702631348 | 67 |
| SOLAR | Solar Energy | 47.15 | 43.48 | -0.0778366914103924 | 68 |
| SOUTH_AFRICA | South Africa Equities | 70.1 | 63.77000045776367 | -0.09029956550979068 | 69 |
| SOUTH_KOREA | South Korea Equities | 188.72 | 170.11000061035156 | -0.09861169663866276 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | portfolio | SP500 | 2 | 0.58 | 0.01806905755668664 | 0.061427090801676805 | 0.043358033244990164 | 1.9109111772819494 |  | True | True |
| anthropic-claude-opus-5 | portfolio | CYBERSECURITY | 3 | 0.57 | 0.14194915254237284 | 0.024623626069670463 | 0.006554568512983822 | 1.9477146420139557 |  | True | True |
| openai-gpt-6-astra | portfolio | SP500 | 1 | 0.5 | 0.01806905755668664 | 0.01806905755668664 | 0.0 | 1.9542692105269395 |  | False | True |
| xai-grok-4-6 | portfolio | SP500 | 1 | 0.5 | 0.01806905755668664 | 0.01806905755668664 | 0.0 | 1.9542692105269395 |  | False | True |
| xai-grok-4-5 | portfolio | SMALL_CAP | 3 | 0.5633 | -0.03804216137630245 | 0.015568864969476133 | -0.0025001925872105077 | 1.95676940311415 |  | False | True |
| anthropic-claude-fable-5-1 | portfolio | AEROSPACE_DEFENSE | 3 | 0.56 | -0.05926670015067803 | -0.021860888503953735 | -0.039929946060640376 | 1.9941991565875798 |  | False | False |
| google-gemini-3-1-pro | portfolio | AEROSPACE_DEFENSE | 3 | 0.58 | -0.05926670015067803 | -0.053590410519136725 | -0.07165946807582337 | 2.025928678602763 |  | False | False |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1M has no scored official run.
- Round CB-2026-09-13-1M has no scored official run.
- Round CB-2026-09-15-1M has no scored official run.
- Round CB-2026-09-16-1M has no scored official run.
- Round CB-2026-09-21-1M has no scored official run.
- Round CB-2026-09-28-1M has no scored official run.
- Round CB-2026-10-01-1M has no scored official run.
- Round CB-2026-10-04-1M has no scored official run.
- Round CB-2026-10-06-1M has no scored official run.
- Round CB-2026-10-10-1M has no scored official run.
- Round CB-2026-10-12-1M has no scored official run.
- Round example-round has no scored official run.
- Round example-round-2 has no scored official run.
