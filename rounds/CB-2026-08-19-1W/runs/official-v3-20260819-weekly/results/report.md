# CapitalBench Report: CB-2026-08-19-1W / official-v3-20260819-weekly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260819-weekly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-19-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-08-19
- Decision deadline: 2026-08-19T13:25:00Z
- Horizon: one week
- Entry date: 2026-08-19
- Exit date: 2026-08-26
- Entry rule: Use the Wednesday, August 19, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Wednesday, August 26, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | anthropic | portfolio | METALS_MINING | 3 | 0.5633 | Modest broad-market pullback (SPY -1.34% over 3 sessions, VIX 15.84) with weak breadth in the last 5 sessions (39% positive) but healthy 21-session breadth (71%). Macro is mixed: cooling labor market (-23k payrolls, downward revisions), still-elevated inflation (CPI 3.4% y/y, PPI 4.7%), FOMC on hold with three hawkish dissents. Cross-sectional active dispersion is only 1.45% over 5 sessions, so single-week edges are small. Recent leadership rotated toward energy/oil and defensives; tech/software/cyber sold off sharply into an NVIDIA print that lands after the exit close, so tech reversal is untested by fundamentals inside the window. Best-supported reversal candidates are the quality-pullback commodity/materials complex where prior relative trend was strong and the pullback is recent and shallow. | Metals and silver carry 38-42% annualized volatility, so a one-week adverse move can far exceed the modest expected edge; China July manufacturing PMI at 49.2 weakens industrial-metals demand and could extend the copper/mining pullback; Hawkish July FOMC minutes on August 19 or firm August 26 PCE could lift real yields and pressure precious metals; Correlated selection: all three top picks share commodity/materials exposure, limiting diversification versus SPY; A tech-led rebound into the NVIDIA print could leave commodity picks lagging a rising SPY |
| anthropic-claude-fable-5 | anthropic | portfolio | METALS_MINING | 3 | 0.58 | SPY fell 0.4% over five sessions with only 39% of assets positive short-term but 71% positive over a month, indicating a shallow pullback within an uptrend. Strong prior relative-strength names that pulled back sharply (metals/mining, silver, cybersecurity) look like temporary dislocations rather than deterioration; macro data (ISM 55.6, contained CPI) does not support a regime break. | Precious/industrial metals could extend their pullback if the dollar strengthens or FOMC minutes read hawkish; China manufacturing PMI at 49.2 could pressure metals demand further; High-beta tech (cybersecurity, software) could fall further into NVIDIA earnings positioning; Aug 26 GDP second estimate and durable goods land on exit day and could add volatility |
| xai-grok-4-5 | xai | portfolio | METALS_MINING | 3 | 0.59 | Low cross-sectional dispersion with soft recent equity tape, energy short-term strength, and quality pullbacks in materials/tech after prior relative strength; mixed macro (soft payrolls, sticky services prices, solid ISM) favors selective mean-reversion over broad continuation into the one-week window. | August 26 GDP second estimate and personal income/outlays can reverse risk appetite before exit close; Elevated ISM prices and sticky core CPI keep rate-volatility risk alive into FOMC minutes; Energy/oil short-term strength can reverse sharply given high horizon vol and negative equity correlation; Tech-related pullbacks (software/cyber) remain sensitive to growth sentiment and NVIDIA after-close print |
| openai-gpt-5-6-sol | openai | portfolio | MATERIALS | 3 | 0.5733 | Moderate dispersion and broad 21-session participation favor selective reversals, but weak labor and retail data, elevated long yields, and major exit-day macro releases limit conviction. Pullbacks backed by prior relative strength and quality dominate unsupported momentum. | August 26 GDP, profits, durable-goods, and income data could abruptly shift rates and cyclicals before the exit close.; FOMC minutes could reinforce inflation concerns and pressure high-beta reversal candidates.; China's contracting manufacturing PMI could extend weakness in metals and mining exposures.; Low volume across several candidates may indicate weak conviction rather than temporary dislocation. |
| google-gemini-3-1-pro | google | portfolio | SOLAR | 3 | 0.58 | The market is experiencing a mixed environment with some sectors showing continuation of recent trends while others are pulling back. The recent FOMC decision to maintain rates and the mixed economic data suggest a cautious approach. | Continued market volatility could lead to further drawdowns in the selected assets.; Macroeconomic data releases during the week could negatively impact the chosen sectors. |
| xai-grok-4-6 | xai | portfolio | MATERIALS | 3 | 0.555 | Five-session active-return dispersion is only 1.45% with 39% of assets positive, while SPY is modestly lower into a data-heavy week (FOMC minutes, retail, GDP second estimate). Energy/oil show short-horizon strength against a broader equity pullback; several materials/tech names show quality pullbacks rather than a single clean continuation regime. | August 26 GDP second estimate, corporate profits, and PCE can reprice the whole equity complex before the weekly exit.; July FOMC minutes (Aug 19) may revive the three-dissent hawkish split and pressure high-beta reversals.; China manufacturing PMI 49.2 can keep copper, metals, and materials from mean-reverting.; Energy/oil continuation could persist if crude stays firm, making defensive index exposure lag a commodity tape. |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Mixed signals from weak July payrolls and GDP offset by resilient PMI and energy price strength; one-week window favors continuation in energy amid scheduled data releases. | July payroll decline and downward revisions; FOMC minutes and GDP second estimate on Aug 26; NVIDIA results after close on exit date |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 15.88 | 18.649999618530273 | 0.1744332253482539 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 38.78 | 44.459999084472656 | 0.14646722755215724 | 2 |
| BRAZIL | Brazil Equities | 34.26 | 35.720001220703125 | 0.042615330435000764 | 3 |
| MEXICO | Mexico Equities | 75.14 | 77.55000305175781 | 0.032073503483601495 | 4 |
| METALS_MINING | Metals and Mining | 117.07 | 120.30999755859375 | 0.027675728697307278 | 5 |
| SOUTH_KOREA | South Korea Equities | 174.43 | 179.17999267578125 | 0.027231512215680986 | 6 |
| SILVER | Silver | 60.01 | 61.59000015258789 | 0.026328947718511797 | 7 |
| MATERIALS | Materials Sector | 52.52 | 53.66999816894531 | 0.021896385547321096 | 8 |
| SOUTH_AFRICA | South Africa Equities | 70.29 | 71.68000030517578 | 0.01977522129998266 | 9 |
| GOLD | Gold | 84.84 | 86.37000274658203 | 0.01803397862543643 | 10 |
| COPPER | Copper | 39.39 | 40.060001373291016 | 0.017009428110967617 | 11 |
| TAIWAN | Taiwan Equities | 104.7 | 106.38999938964844 | 0.016141350426441603 | 12 |
| FINANCIALS | Financials Sector | 57.48 | 58.2599983215332 | 0.013569908168636236 | 13 |
| COMMUNICATIONS | Communication Services Sector | 111.32 | 112.61000061035156 | 0.011588219640240371 | 14 |
| AGRICULTURE | Agriculture Commodities | 28.29 | 28.59000015258789 | 0.010604459264329957 | 15 |
| EMERGING_MARKETS | Emerging Markets | 60.04 | 60.65999984741211 | 0.010326446492540109 | 16 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.83 | 73.44999694824219 | 0.008512933519733368 | 17 |
| JAPAN | Japan Equities | 94.78 | 95.43000030517578 | 0.006857990136904135 | 18 |
| CANADA | Canada Equities | 61.83 | 62.22999954223633 | 0.00646934404393229 | 19 |
| AUSTRALIA | Australia Equities | 29.97 | 30.149999618530273 | 0.006005993277620192 | 20 |
| UNITED_KINGDOM | United Kingdom Equities | 48.57 | 48.86000061035156 | 0.005970776412426604 | 21 |
| EUROPE | Europe Equities | 92.23 | 92.69999694824219 | 0.005095922674207776 | 22 |
| US_DOLLAR | US Dollar | 27.88 | 28.020000457763672 | 0.005021537222513306 | 23 |
| INDIA | India Equities | 49.54 | 49.75 | 0.004238998788857584 | 24 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.02 | 83.30000305175781 | 0.003372718040927758 | 25 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.71 | 79.9000015258789 | 0.0023836598404078924 | 26 |
| REAL_ESTATE | Real Estate Sector | 44.99 | 45.09000015258789 | 0.002222719550742047 | 27 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.11 | 95.30999755859375 | 0.0021028026347782447 | 28 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.57 | 106.77999877929688 | 0.0019705243435945707 | 29 |
| BROAD_AI_TECH | Broad AI Technology | 62.99 | 63.06999969482422 | 0.0012700380191175142 | 30 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.74 | 47.779998779296875 | 0.0008378462357954142 | 31 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.57 | 91.62999725341797 | 0.0006552064368021693 | 32 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.82 | 97.86000061035156 | 0.0004089205719850497 | 33 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 222.07 | 222.11000061035156 | 0.0001801261329832382 | 34 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.57 | 93.58000183105469 | 0.0001068914294612977 | 35 |
| TIPS | Treasury Inflation-Protected Securities | 107.51 | 107.51000213623047 | 1.987006292836213e-08 | 36 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 37 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.38 | 93.31999969482422 | -0.000642539143026144 | 38 |
| DIVIDEND | US Dividend Equities | 35.09 | 35.04999923706055 | -0.0011399476471773973 | 39 |
| LARGE_VALUE | US Large-Cap Value | 258.77 | 258.4599914550781 | -0.0011980080570462848 | 40 |
| LOW_VOL | US Low Volatility Equities | 75.98 | 75.87999725341797 | -0.0013161719739672728 | 41 |
| EURO | Euro | 107.78 | 107.5999984741211 | -0.0016700828157256709 | 42 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.68 | 105.44999694824219 | -0.0021764104064896372 | 43 |
| CONSUMER_STAPLES | Consumer Staples Sector | 86.54 | 86.2699966430664 | -0.0031199833248625186 | 44 |
| SP500 | S&P 500 | 769.06 | 766.0800170898438 | -0.003874837997238423 | 45 |
| SOFTWARE | Software | 102.81 | 102.38999938964844 | -0.0040852116559825236 | 46 |
| TECHNOLOGY | Technology Sector | 183.64 | 182.83999633789062 | -0.004356369321005027 | 47 |
| TOTAL_US_MARKET | Total US Stock Market | 379.99 | 378.2300109863281 | -0.004631671922081804 | 48 |
| CHINA | China Equities | 55.39 | 55.099998474121094 | -0.0052356296421539605 | 49 |
| MID_CAP | US Mid-Cap Stocks | 77.04 | 76.62000274658203 | -0.005451677744262362 | 50 |
| REGIONAL_BANKS | Regional Banks | 75.0 | 74.58000183105469 | -0.0055999755859375 | 51 |
| SMALL_VALUE | US Small-Cap Value | 225.61 | 224.33999633789062 | -0.0056291993356206715 | 52 |
| MOMENTUM | US Momentum Equities | 305.88 | 304.0 | -0.006146201124624051 | 53 |
| NASDAQ100 | Nasdaq 100 | 716.08 | 711.3699951171875 | -0.006577484195638084 | 54 |
| BIOTECH | Biotechnology | 169.55 | 168.38999938964844 | -0.006841643234158479 | 55 |
| LARGE_GROWTH | US Large-Cap Growth | 122.67 | 121.75 | -0.007499796201190234 | 56 |
| YEN | Japanese Yen | 58.02 | 57.54999923706055 | -0.008100668096164387 | 57 |
| BROAD_COMMODITIES | Broad Commodities | 18.33 | 18.18000030517578 | -0.008183289406667571 | 58 |
| INDUSTRIALS | Industrials Sector | 181.95 | 180.33999633789062 | -0.008848604903046842 | 59 |
| SEMICONDUCTORS | Semiconductors | 560.92 | 555.77001953125 | -0.009181310113295926 | 60 |
| SMALL_CAP | US Small-Cap Stocks | 301.72 | 298.92999267578125 | -0.009247008233523757 | 61 |
| UTILITIES | Utilities Sector | 44.02 | 43.5099983215332 | -0.011585681019236738 | 62 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.59 | 117.16000366210938 | -0.012058321425842178 | 63 |
| HEALTHCARE | Healthcare Sector | 175.68 | 173.5399932861328 | -0.012181276832122001 | 64 |
| ENERGY | Energy Sector | 63.58 | 62.43000030517578 | -0.018087444083425885 | 65 |
| CYBERSECURITY | Cybersecurity | 95.54 | 93.66000366210938 | -0.019677583607814908 | 66 |
| OIL | Crude Oil | 130.91 | 127.3499984741211 | -0.02719426725138574 | 67 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 126.01 | 122.33000183105469 | -0.029204016895050477 | 68 |
| SOLAR | Solar Energy | 50.47 | 48.779998779296875 | -0.03348526294240384 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 246.15 | 236.3800048828125 | -0.03969122533897018 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | METALS_MINING | 35.0 | 0.027675728697307278 | 0.009686505044057547 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | SILVER | 35.0 | 0.026328947718511797 | 0.009215131701479128 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | CYBERSECURITY | 30.0 | -0.019677583607814908 | -0.005903275082344472 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | METALS_MINING | 35.0 | 0.027675728697307278 | 0.009686505044057547 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | COPPER | 35.0 | 0.017009428110967617 | 0.005953299838838666 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SILVER | 30.0 | 0.026328947718511797 | 0.00789868431555354 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SOLAR | 35.0 | -0.03348526294240384 | -0.011719842029841342 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | METALS_MINING | 35.0 | 0.027675728697307278 | 0.009686505044057547 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | MATERIALS | 30.0 | 0.021896385547321096 | 0.006568915664196329 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | MATERIALS | 35.0 | 0.021896385547321096 | 0.007663734941562383 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | CYBERSECURITY | 35.0 | -0.019677583607814908 | -0.006887154262735218 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | METALS_MINING | 30.0 | 0.027675728697307278 | 0.008302718609192183 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 100.0 | -0.003874837997238423 | -0.003874837997238423 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | METALS_MINING | 35.0 | 0.027675728697307278 | 0.009686505044057547 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | MATERIALS | 35.0 | 0.021896385547321096 | 0.007663734941562383 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | CYBERSECURITY | 30.0 | -0.019677583607814908 | -0.005903275082344472 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | MATERIALS | 35.0 | 0.021896385547321096 | 0.007663734941562383 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | CYBERSECURITY | 35.0 | -0.019677583607814908 | -0.006887154262735218 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 30.0 | -0.003874837997238423 | -0.0011624513991715269 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | METALS_MINING | 3 | 0.5633 | 0.027675728697307278 | 0.023538489198449752 | 0.027413327195688175 | 0.15089473614980414 |  | True | True |
| anthropic-claude-fable-5 | METALS_MINING | 3 | 0.58 | 0.027675728697307278 | 0.012998361663192202 | 0.016873199660430625 | 0.16143486368506169 |  | True | True |
| xai-grok-4-5 | METALS_MINING | 3 | 0.59 | 0.027675728697307278 | 0.011446964903275458 | 0.015321802900513881 | 0.16298626044497844 |  | True | True |
| openai-gpt-5-6-sol | MATERIALS | 3 | 0.5733 | 0.021896385547321096 | 0.009079299288019349 | 0.012954137285257772 | 0.16535392606023455 |  | True | True |
| google-gemini-3-1-pro | SOLAR | 3 | 0.58 | -0.03348526294240384 | 0.004535578678412534 | 0.008410416675650956 | 0.16989764666984136 |  | True | True |
| xai-grok-4-6 | MATERIALS | 3 | 0.555 | 0.021896385547321096 | -0.0003858707203443616 | 0.0034889672768940614 | 0.17481909606859825 |  | True | False |
| xai-grok-4-3 | SP500 | 1 | 0.5 | -0.003874837997238423 | -0.003874837997238423 | 0.0 | 0.17830806334549232 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 64450a1f3c7aea790b332c55307b7bf8c85ff875eeda33d9ce6144ccfc8a96e2 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | e7873c138b57bbb6c3b9fb90280d9bf35f7a3c69178d01348587b48d9f9a276d |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 1257aa4086ca60cbe849062a83c6cf163711ec393a1fa2a94aadc04bcf074efe |
| market_data/universe_decision_context.md | 2ab39680ffa83b7c499b361da32a7279cac367a8ae6e2a9beadfe811435af1b4 |
| market_data/universe_decision_context.json | 9576888322ebc27e69e032634f086191c77414776517c411dc5ec98251db11de |
| market_data/decision_context_source_history.json | b5dcd8aba46857809781f0bc9f5f76b1c431027856a21739350b59c5140b0e52 |
| market_data/universe_quality_evidence.md | 706e7ec209263bf9cd41ef93c53d5f77d0fb84deaefafa048a18c8794ecfd5fe |
| market_data/universe_quality_evidence.json | 77074d33bdc58984bff4771196394793b428d2bd2032215679566cb4897cb00e |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | b35cc219412791288b65bc39d49bb0b901c101c97bc597cfb79758534cf76b95 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | e7df197b74b91e4fb70ccab37b7595434c378729591ba3b1a829e9aaa55a4d6f | yes |
| Final briefing | research/final_briefing.md | model-facing | 64450a1f3c7aea790b332c55307b7bf8c85ff875eeda33d9ce6144ccfc8a96e2 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
