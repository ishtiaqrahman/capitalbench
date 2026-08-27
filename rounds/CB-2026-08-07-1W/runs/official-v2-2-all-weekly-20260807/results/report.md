# CapitalBench Report: CB-2026-08-07-1W / official-v2-2-all-weekly-20260807

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-weekly-20260807
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-07-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-08-07
- Decision deadline: 2026-08-07T13:25:00Z
- Horizon: one week
- Entry date: 2026-08-07
- Exit date: 2026-08-14
- Entry rule: Use the Friday, August 7, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Friday, August 14, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | openai | portfolio | ENERGY | 5 | 0.56 | SPY has positive broad-market momentum and earnings support, but several active candidates have stronger one-week setups from high quality evidence, sharp pullbacks, and identifiable in-window macro or geopolitical catalysts. The expected portfolio base return is 0.965%, or 0.715 percentage points above SPY. | The July employment, CPI, PPI, or retail-sales releases could trigger a broad risk-off move that hurts cyclical and commodity-sensitive holdings more than SPY.; Energy and oil positions could continue reversing lower if the Strait of Hormuz risk premium fades or demand expectations weaken.; Recent strength in metals/mining could be a short-term exhaustion move rather than continuation.; SPY mega-cap growth leadership could resume and outperform the diversified active tilts over the one-week horizon. |
| openai-gpt-5-6-sol | openai | portfolio | ENERGY | 3 | 0.57 | Energy, financials, and UK equities each have base forecasts above SPY and offer differentiated exposure to inflation, yields, global value, and geopolitical developments during the scoring week. | A benign CPI or PPI report could lower yields and reverse the energy and financials theses.; De-escalation around the Strait of Hormuz could sharply reduce crude prices and energy-sector returns.; Weak August 14 retail sales could undermine cyclical and financial exposures.; Recent pullbacks may represent trend deterioration rather than temporary dislocations. |
| xai-grok-4-5 | xai | portfolio | TECHNOLOGY | 4 | 0.58 | SPY base set conservatively after strong 5-session run; active holdings chosen for higher expected one-week returns from momentum, commodities, and inflation hedges with catalysts inside the scoring window. | July employment and CPI surprises trigger broad equity risk-off; Geopolitical de-escalation reverses energy and gold bids; Tech/semiconductor mean-reversion after elevated recent gains; Cluster concentration amplifies sector-specific drawdowns |
| anthropic-claude-fable-5 | anthropic | portfolio | SP500 | 5 | 0.55 | Barbell of benchmark core with inflation-sensitive (energy, gold) and value (UK, financials) exposures positioned for a data-heavy week with elevated inflation prints and Middle East supply risk. | Hot CPI/PPI prints could sink all risk assets including satellites; Middle East de-escalation would reverse oil and energy positioning; Weak July payrolls could trigger growth scare hurting financials and energy; Continued mega-cap tech leadership would leave value tilts lagging SPY |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.55 | 40% SP500 plus three active holdings each with base forecast above SPY base of 0.6%. Weighted expected return 0.84%. | July Employment Situation surprise on August 7; CPI release on August 12 could shift rate expectations; Energy price reversal if Middle East tensions ease |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 5 | 0.5 | After a +3.6% SPY week concentrated in mega-cap tech, mean reversion risk is elevated; the portfolio keeps benchmark beta while tilting to high-quality laggards and an inflation hedge ahead of CPI, PPI, and retail sales. | Hot July CPI/PPI triggering a broad risk-off week; Continued mega-cap tech leadership leaving laggard tilts behind; Oil/Hormuz escalation shocking cyclicals and inflation expectations; Weak payrolls on Aug 7 driving a growth scare |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 3 | 0.52 | US equities carry strong earnings momentum; tilt to growth/tech for modest alpha while keeping SPY as core anchor. | Hot July CPI/PPI reviving rate-hike fears and hitting high-beta growth; Broad risk-off from Middle East oil shock; Tech mean-reversion after recent leadership |
| google-gemini-3-1-pro | google | portfolio | SP500 | 1 | 0.5 | 100% allocation to SP500 due to uncertainty ahead of key economic data releases. | Weaker-than-expected employment data; Higher-than-expected inflation data; Geopolitical tensions escalating |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOUTH_KOREA | South Korea Equities | 166.09 | 179.74 | 0.08218435787825884 | 1 |
| ENERGY | Energy Sector | 57.5 | 61.91 | 0.07669565217391305 | 2 |
| OIL | Crude Oil | 117.98 | 126.6 | 0.07306323105611101 | 3 |
| TAIWAN | Taiwan Equities | 103.09 | 107.07 | 0.03860704239014434 | 4 |
| BROAD_COMMODITIES | Broad Commodities | 17.25 | 17.91 | 0.03826086956521735 | 5 |
| MOMENTUM | US Momentum Equities | 309.32 | 317.21 | 0.025507564981249065 | 6 |
| REGIONAL_BANKS | Regional Banks | 76.21 | 77.93 | 0.022569216638236522 | 7 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 127.85 | 130.39 | 0.019867031677747393 | 8 |
| DIVIDEND | US Dividend Equities | 33.9 | 34.52 | 0.01828908554572295 | 9 |
| CYBERSECURITY | Cybersecurity | 97.85 | 99.6 | 0.017884517118037735 | 10 |
| SILVER | Silver | 57.5 | 58.48 | 0.017043478260869493 | 11 |
| UTILITIES | Utilities Sector | 43.61 | 44.31 | 0.01605136436597121 | 12 |
| COMMUNICATIONS | Communication Services Sector | 111.25 | 112.95 | 0.015280898876404603 | 13 |
| CANADA | Canada Equities | 61.3 | 62.23 | 0.015171288743882627 | 14 |
| SOFTWARE | Software | 102.69 | 104.08 | 0.013535884701528778 | 15 |
| JAPAN | Japan Equities | 96.9 | 98.21 | 0.013519091847265186 | 16 |
| BROAD_AI_TECH | Broad AI Technology | 63.35 | 64.2 | 0.013417521704814472 | 17 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.09 | 222.77 | 0.012176836748602815 | 18 |
| METALS_MINING | Metals and Mining | 115.74 | 117.14 | 0.01209607741489549 | 19 |
| SMALL_CAP | US Small-Cap Stocks | 301.56 | 305.09 | 0.011705796524738021 | 20 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.12 | 86.09 | 0.011395676691729362 | 21 |
| MID_CAP | US Mid-Cap Stocks | 77.79 | 78.67 | 0.011312508034451607 | 22 |
| NASDAQ100 | Nasdaq 100 | 723.03 | 731.07 | 0.0111198705447908 | 23 |
| TECHNOLOGY | Technology Sector | 187.97 | 190.01 | 0.010852795658881753 | 24 |
| HEALTHCARE | Healthcare Sector | 165.68 | 167.37 | 0.010200386286817853 | 25 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 250.75 | 253.215 | 0.009830508474576227 | 26 |
| FINANCIALS | Financials Sector | 57.6 | 58.16 | 0.009722222222222188 | 27 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.89 | 73.58 | 0.009466319110989163 | 28 |
| SEMICONDUCTORS | Semiconductors | 582.7 | 587.82 | 0.008786682684057023 | 29 |
| SMALL_VALUE | US Small-Cap Value | 225.52 | 227.43 | 0.008469315360056795 | 30 |
| GOLD | Gold | 81.68 | 82.28 | 0.007345739471106727 | 31 |
| INDUSTRIALS | Industrials Sector | 185.18 | 186.51 | 0.007182201101630703 | 32 |
| REAL_ESTATE | Real Estate Sector | 44.98 | 45.27 | 0.006447309915518229 | 33 |
| LARGE_GROWTH | US Large-Cap Growth | 124.6 | 125.29 | 0.00553772070626013 | 34 |
| AGRICULTURE | Agriculture Commodities | 27.62 | 27.77 | 0.005430847212165135 | 35 |
| TOTAL_US_MARKET | Total US Stock Market | 381.78 | 383.85 | 0.00542197076850548 | 36 |
| SP500 | S&P 500 | 773.26 | 776.34 | 0.003983136331893622 | 37 |
| LARGE_VALUE | US Large-Cap Value | 257.56 | 258.57 | 0.00392141636900134 | 38 |
| COPPER | Copper | 39.9 | 40.01 | 0.002756892230576513 | 39 |
| LOW_VOL | US Low Volatility Equities | 76.21 | 76.36 | 0.0019682456370555546 | 40 |
| US_DOLLAR | US Dollar | 28.07 | 28.11 | 0.0014250089063057025 | 41 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.61 | 79.71 | 0.0012561236025623312 | 42 |
| EURO | Euro | 106.68 | 106.79 | 0.001031121109861255 | 43 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.48 | 91.53 | 0.0005465675557498884 | 44 |
| BIOTECH | Biotechnology | 157.37 | 157.41 | 0.000254178051725118 | 45 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 46 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.27 | 93.2 | -0.0007505092741502128 | 47 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.94 | 105.86 | -0.0007551444213705905 | 48 |
| TIPS | Treasury Inflation-Protected Securities | 107.08 | 106.99 | -0.0008404930892790263 | 49 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.6 | 97.48 | -0.0012295081967211852 | 50 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.17 | 93.04 | -0.0013952989159600193 | 51 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.24 | 95.05 | -0.0019949601007979156 | 52 |
| EUROPE | Europe Equities | 92.6 | 92.37 | -0.002483801295896204 | 53 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.55 | 106.12 | -0.0040356640075081 | 54 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.95 | 47.72 | -0.0047966631908238355 | 55 |
| EMERGING_MARKETS | Emerging Markets | 60.47 | 60.11 | -0.0059533653051099256 | 56 |
| MATERIALS | Materials Sector | 52.86 | 52.54 | -0.006053726825577033 | 57 |
| UNITED_KINGDOM | United Kingdom Equities | 48.64 | 48.26 | -0.0078125 | 58 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.76 | 82.04 | -0.008699855002416657 | 59 |
| YEN | Japanese Yen | 58.24 | 57.58 | -0.011332417582417653 | 60 |
| INDIA | India Equities | 50.365 | 49.78 | -0.011615208974486313 | 61 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 119.86 | 118.2 | -0.01384949107291833 | 62 |
| SOLAR | Solar Energy | 52.75 | 51.97 | -0.014786729857819925 | 63 |
| ETHEREUM_ETF | Ethereum ETF | 14.47 | 14.18 | -0.020041465100207434 | 64 |
| AUSTRALIA | Australia Equities | 30.41 | 29.65 | -0.024991779020059224 | 65 |
| SOUTH_AFRICA | South Africa Equities | 69.65 | 67.53 | -0.030437903804737987 | 66 |
| BITCOIN_ETF | Bitcoin ETF | 36.8 | 35.63 | -0.03179347826086942 | 67 |
| MEXICO | Mexico Equities | 77.52 | 75.01 | -0.032378740970072095 | 68 |
| CHINA | China Equities | 56.57 | 54.63 | -0.03429379529786103 | 69 |
| BRAZIL | Brazil Equities | 35.34 | 33.93 | -0.0398981324278439 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SP500 | 30.0 | 0.003983136331893622 | 0.0011949408995680865 | Benchmark core with strong earnings season backdrop; anchors the portfolio through jobs/CPI data. |
| anthropic-claude-fable-5 | ENERGY | 20.0 | 0.07669565217391305 | 0.015339130434782612 | Brent at $82.49 with Strait of Hormuz risk premium; sector pulled back -4.98% vs SPY last week despite +6.54% prior trend, offering mean-reversion entry. |
| anthropic-claude-fable-5 | GOLD | 20.0 | 0.007345739471106727 | 0.0014691478942213455 | Elevated inflation (core PCE 3.3% y/y, ISM prices >70) plus geopolitical uncertainty; CPI/PPI prints in window support hedge demand. |
| anthropic-claude-fable-5 | UNITED_KINGDOM | 15.0 | -0.0078125 | -0.001171875 | Strong prior relative trend (+5.21%) with deep recent pullback (-4.40%); value/energy/dividend tilt benefits from firm oil and highest quality evidence score in universe (0.867). |
| anthropic-claude-fable-5 | FINANCIALS | 15.0 | 0.009722222222222188 | 0.0014583333333333282 | Best prior active trend among US sectors (+4.19%) with recent -2.20% pullback; solid growth, hawkish-tilted Fed, and steep 30y at 5.22% support bank margins. |
| anthropic-claude-opus-4-8 | SP500 | 50.0 | 0.003983136331893622 | 0.001991568165946811 | Strong earnings season with best growth since 2021, solid GDP final sales, benign broad equity trend. |
| anthropic-claude-opus-4-8 | TECHNOLOGY | 25.0 | 0.010852795658881753 | 0.0027131989147204383 | Tech leading with strongest 3-session return, positive momentum in growth cluster and earnings strength. |
| anthropic-claude-opus-4-8 | LARGE_GROWTH | 25.0 | 0.00553772070626013 | 0.0013844301765650324 | Large growth showed positive active return and leadership; complements SPY with growth tilt. |
| anthropic-claude-opus-5 | SP500 | 40.0 | 0.003983136331893622 | 0.001593254532757449 | Core benchmark exposure with strong earnings breadth and momentum. |
| anthropic-claude-opus-5 | FINANCIALS | 25.0 | 0.009722222222222188 | 0.002430555555555547 | Best-in-class quality score with low volatility, positive prior active trend, and recent relative pullback offering catch-up potential. |
| anthropic-claude-opus-5 | HEALTHCARE | 15.0 | 0.010200386286817853 | 0.001530057943022678 | Defensive sector, low beta and negative SPY correlation, lagged badly last week (-3.05% active) with solid quality rank. |
| anthropic-claude-opus-5 | CYBERSECURITY | 10.0 | 0.017884517118037735 | 0.0017884517118037736 | Tech exposure with less extreme volatility than semis; positive 5s active return and small drawdown. |
| anthropic-claude-opus-5 | GOLD | 10.0 | 0.007345739471106727 | 0.0007345739471106727 | Inflation hedge with elevated PCE readings and Middle East risk; diversifies equity beta. |
| google-gemini-3-1-pro | SP500 | 100.0 | 0.003983136331893622 | 0.003983136331893622 | Given the uncertainty around the upcoming employment data and the recent market pullback, a broad market exposure is preferred. |
| openai-gpt-5-5 | ENERGY | 30.0 | 0.07669565217391305 | 0.023008695652173915 | Energy has the strongest supplied quality evidence among U.S. sectors, a large prior active trend, and a sharp recent relative pullback while oil-related geopolitical uncertainty remains in-window relevant. |
| openai-gpt-5-5 | OIL | 20.0 | 0.07306323105611101 | 0.014612646211222203 | Crude oil offers direct exposure to the supplied geopolitical oil-risk catalyst after a severe short-term drawdown, with the highest prior active return and pullback ranks but very high volatility. |
| openai-gpt-5-5 | METALS_MINING | 15.0 | 0.01209607741489549 | 0.0018144116122343233 | Metals and mining has recent absolute and relative strength, modest positive prior active return, and leverage to firm manufacturing and commodity demand data. |
| openai-gpt-5-5 | FINANCIALS | 20.0 | 0.009722222222222188 | 0.0019444444444444377 | Financials combine high quality evidence, a strong prior active trend, low relative volatility, and support from solid activity and earnings context despite recent underperformance. |
| openai-gpt-5-5 | UNITED_KINGDOM | 15.0 | -0.0078125 | -0.001171875 | UK equities have the highest supplied quality evidence score, strong prior active return, low volatility, and a recent pullback that creates a one-week rebound setup. |
| openai-gpt-5-6-sol | ENERGY | 50.0 | 0.07669565217391305 | 0.03834782608695653 | Strong prior relative trend and a deep recent pullback are reinforced by elevated crude prices and continuing Strait of Hormuz uncertainty. |
| openai-gpt-5-6-sol | FINANCIALS | 30.0 | 0.009722222222222188 | 0.0029166666666666564 | Strong prior active performance, low recent volatility, and firm activity data support a rebound from recent underperformance. |
| openai-gpt-5-6-sol | UNITED_KINGDOM | 20.0 | -0.0078125 | -0.0015625 | The highest quality-evidence score combines strong prior relative performance, a deep pullback, and comparatively low volatility. |
| xai-grok-4-3 | SP500 | 40.0 | 0.003983136331893622 | 0.001593254532757449 | Broad US equity exposure with solid recent momentum and earnings growth backdrop. |
| xai-grok-4-3 | FINANCIALS | 20.0 | 0.009722222222222188 | 0.0019444444444444377 | High quality evidence score and prior active rank support outperformance versus SPY. |
| xai-grok-4-3 | ENERGY | 20.0 | 0.07669565217391305 | 0.015339130434782612 | Highest quality evidence score with strong prior active rank and commodity support. |
| xai-grok-4-3 | UNITED_KINGDOM | 20.0 | -0.0078125 | -0.0015625 | Top quality evidence score and prior active rank indicate relative strength. |
| xai-grok-4-5 | TECHNOLOGY | 30.0 | 0.010852795658881753 | 0.003255838697664526 | Strong recent relative momentum and earnings backdrop support higher base return than SPY over the one-week window. |
| xai-grok-4-5 | SEMICONDUCTORS | 20.0 | 0.008786682684057023 | 0.0017573365368114048 | Highest recent active return among growth names with quality pullback setup exceeding SPY base case. |
| xai-grok-4-5 | GOLD | 25.0 | 0.007345739471106727 | 0.0018364348677766817 | Elevated inflation readings and Middle East uncertainty support precious-metals bid above SPY base. |
| xai-grok-4-5 | ENERGY | 25.0 | 0.07669565217391305 | 0.019173913043478263 | High quality-evidence score, prior active strength, and oil price spike provide superior base forecast. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | ENERGY | 5 | 0.56 | 0.07669565217391305 | 0.040208322920074875 | 0.03622518658818125 | 0.041976034958183965 |  | True | True |
| openai-gpt-5-6-sol | ENERGY | 3 | 0.57 | 0.07669565217391305 | 0.03970199275362318 | 0.03571885642172956 | 0.04248236512463566 |  | True | True |
| xai-grok-4-5 | TECHNOLOGY | 4 | 0.58 | 0.010852795658881753 | 0.026023523145730875 | 0.022040386813837253 | 0.05616083473252796 |  | True | True |
| anthropic-claude-fable-5 | SP500 | 5 | 0.55 | 0.003983136331893622 | 0.018289677561905374 | 0.014306541230011752 | 0.06389468031635347 |  | True | True |
| xai-grok-4-3 | SP500 | 4 | 0.55 | 0.003983136331893622 | 0.0173143294119845 | 0.013331193080090877 | 0.06487002846627435 |  | True | True |
| anthropic-claude-opus-5 | SP500 | 5 | 0.5 | 0.003983136331893622 | 0.008076893690250121 | 0.004093757358356499 | 0.07410746418800872 |  | True | True |
| anthropic-claude-opus-4-8 | SP500 | 3 | 0.52 | 0.003983136331893622 | 0.006089197257232282 | 0.0021060609253386597 | 0.07609516062102656 |  | True | True |
| google-gemini-3-1-pro | SP500 | 1 | 0.5 | 0.003983136331893622 | 0.003983136331893622 | 0.0 | 0.07820122154636522 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 98e7ad6bd7c1c62faa46aed5130fca41de91f47365859e786a103da1244f34fe |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 1a844da9c59ab06e30e88b53a60f08b23075e0cfd4df40bd80afc8570a93c261 |
| manifest.yaml | 16aeba610813bcd6974212dbc54a80d40682bc4a83a08005181ac8b1885e8346 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 77121eb512d5f3784b244fc12ce24f7bbfc4c84c7b14fa6cd4ac95a1df407459 |
| market_data/universe_decision_context.md | 82dca985ce259b0e4d4cb1b2d3734f13245ed391b5059dc6a9ab00c89ba25ee2 |
| market_data/universe_decision_context.json | b64ac64d180cc8a26e7bb8189b2b2226f201732a81fc4c13fdc97052b1c36702 |
| market_data/decision_context_source_history.json | 72d184a4f5316b95b9645d994c9f5726ec5ccc9cd970e984c7d57dd870a64a6e |
| market_data/universe_quality_evidence.md | f273577e90ae2f7607ce97ca6a217024e735ac649bf75506decb5a8179c7f1a0 |
| market_data/universe_quality_evidence.json | 1c14d13a88bbc0f3d71587eafbd4b3cee9f9d151e8e3cf9bffbd50720896d9c3 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 0dc019cc25e7467c8cf38f46fb81fafbb8b69c1e7ab9b422acc852de872147ab | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 6cad5b791054484263cd6dd4262b9856b41bf5458a94f5aeeff2861cb29e1ea7 | yes |
| Final briefing | research/final_briefing.md | model-facing | 98e7ad6bd7c1c62faa46aed5130fca41de91f47365859e786a103da1244f34fe | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
