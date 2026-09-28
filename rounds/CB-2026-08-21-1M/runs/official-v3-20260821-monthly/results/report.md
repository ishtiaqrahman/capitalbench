# CapitalBench Report: CB-2026-08-21-1M / official-v3-20260821-monthly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260821-monthly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-21-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-08-21
- Decision deadline: 2026-08-21T13:25:00Z
- Horizon: one month
- Entry date: 2026-08-21
- Exit date: 2026-09-21
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | anthropic | portfolio | SEMICONDUCTORS | 3 | 0.575 | A modest broad-market pullback (SPY -1.96% over the last window, VIX 16 from 14.9) sits against firm activity data (Philly Fed 47.4, claims 206k) but sticky inflation (CPI 3.4% y/y, PPI 4.7%) and rising long yields (10y 4.70%, 30y 5.23%). Breadth deteriorated short-term (31.9% positive over 5 sessions) but was broad over 21 sessions (79.7%). The key in-window catalysts are NVIDIA earnings on Aug 26 and the Sept 16 FOMC. Semis pulled back hard (-4.49%, -6.17% active) after a very strong prior trend (+33.3% prior active) with the highest quality-evidence score in the universe, making that the cleanest overreaction candidate ahead of a specific catalyst. Most other slate names are either momentum-chasing (ETHA), structurally impaired (TAN), or offer no reliable one-month edge. | A disappointing NVIDIA report on Aug 26 could sharply reverse the semiconductor thesis given 53.6% horizon volatility and 2.36 SPY beta; Sticky inflation (CPI 3.4%, PPI 4.7%) plus hawkish FOMC dissents could push yields higher and compress high-beta growth multiples into the Sept 16 FOMC; Taiwan carries geopolitical and currency tail risk not visible in trailing data; Persian Gulf tanker disruption could spike oil and pressure risk assets broadly; Labor deterioration (payrolls -23k, downward revisions) could turn the pullback into a broader growth scare |
| openai-gpt-5-6-sol | openai | portfolio | US_DOLLAR | 3 | 0.58 | Large cross-asset return gaps, elevated candidate volatility, firm long yields, and multiple macro events favor selective pullback reversals and defensive exposure rather than broad continuation. | A benign CPI and dovish September FOMC outcome could weaken the dollar and revive broad SPY risk appetite.; NVIDIA results or guidance could disappoint and deepen the semiconductor pullback.; Persistently high inflation and rising long yields could pressure high-beta momentum and semiconductor holdings.; A rapid factor rotation could turn the momentum pullback into sustained fundamental underperformance. |
| google-gemini-3-1-pro | google | portfolio | SP500 | 2 | 0.65 | The market is experiencing a pullback with the S&P 500 down 1.9% over the past week. Yields have risen slightly, and the Fed minutes indicate a cautious approach to inflation. The upcoming NVIDIA earnings report is a significant catalyst for the tech sector. | NVIDIA earnings disappoint, leading to a sharp selloff in SEMICONDUCTORS and the broader market.; Geopolitical tensions in the Persian Gulf ease, causing a reversal in OIL prices.; Inflation data comes in hotter than expected, leading to higher yields and a broader market pullback. |
| xai-grok-4-5 | xai | portfolio | SEMICONDUCTORS | 3 | 0.5867 | Recent equity pullback with elevated rates, sticky inflation signals, and oil strength creates mixed continuation/reversal setup; high cross-asset dispersion and quality pullbacks in semis/momentum favor selective mean-reversion over broad beta. | Sticky inflation and FOMC minutes skewing toward possible further tightening into September meeting; Oil/geopolitical supply disruption sustaining higher yields and equity multiple compression; NVIDIA earnings Aug 26 could extend semis/tech drawdown rather than reverse it; High horizon vols in growth/factor names amplify one-month path risk |
| anthropic-claude-fable-5 | anthropic | portfolio | SEMICONDUCTORS | 3 | 0.5633 | SPY pulled back -1.96% on the week as long yields rose and VIX jumped to 16. Prior strong trends (semis, momentum, tech) saw modest pullbacks into the NVIDIA Aug 26 earnings catalyst, while breadth (RSP outperforming SPY) and low jobless claims suggest a corrective dip rather than regime change. Quality-pullback names with strong prior trends look best over the month. | NVIDIA earnings disappointment on Aug 26 could hit semis and momentum hard given 2.4x beta; Rising long yields (30y >5.2%) and hawkish FOMC minutes could pressure all risk assets into the Sep 16 FOMC; Persistent CPI (3.4% y/y) print on Sep 11 could reprice rate expectations; Oil supply disruption in Persian Gulf could spike inflation expectations and hurt equities |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | SPY sold off ~2% into higher 10y yields (~4.70%), VIX 16, sticky CPI/PCE, and a September FOMC with minutes leaning hawkish if inflation stays elevated. Equal-weight beat cap-weight on the 5s/21s windows while only ~32% of assets were positive on 5s, so the month is a mixed pullback-plus-event window rather than a clean trend. High-beta tech/semis remain prior-strong but recently weak; oil strength is supply/geopolitics rather than a broad risk-on tape. | September FOMC and sticky 3.4% CPI / 3.7% PCE could reprice duration and growth stocks together.; NVIDIA Aug 26 results can dominate semiconductor and momentum residuals.; Persian Gulf oil-flow uncertainty can spike energy vol while pressuring equities.; July payrolls -23k with downward revisions raise a growth-scare path for small caps if claims reverse higher. |
| xai-grok-4-3 | xai | portfolio | UTILITIES | 3 | 0.5833 | Equity weakness amid rising yields and inflation uncertainty, with isolated strength in oil and defensive factors; cross-sectional dispersion moderate. | Rising Treasury yields pressuring rate-sensitive assets; Inflation persistence per FOMC minutes; Equity volatility from upcoming GDP and employment data; Geopolitical oil supply uncertainty |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 18.239999771118164 | 20.85 | 0.1430921196070738 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 43.68000030517578 | 49.01 | 0.12202380168464999 | 2 |
| TAIWAN | Taiwan Equities | 104.30000305175781 | 115.64 | 0.1087247997741172 | 3 |
| OIL | Crude Oil | 134.63999938964844 | 148.16 | 0.10041592893375362 | 4 |
| CYBERSECURITY | Cybersecurity | 94.8499984741211 | 103.09 | 0.08687402908211017 | 5 |
| BRAZIL | Brazil Equities | 35.060001373291016 | 38.07 | 0.08585278119817841 | 6 |
| SEMICONDUCTORS | Semiconductors | 560.4199829101562 | 596.03 | 0.0635416619245579 | 7 |
| TECHNOLOGY | Technology Sector | 183.30999755859375 | 194.85 | 0.06295348096176578 | 8 |
| SOUTH_KOREA | South Korea Equities | 178.33999633789062 | 189.16 | 0.060670650915621405 | 9 |
| BROAD_AI_TECH | Broad AI Technology | 63.43000030517578 | 66.31 | 0.04540437775449946 | 10 |
| BROAD_COMMODITIES | Broad Commodities | 18.649999618530273 | 19.44 | 0.04235927065032219 | 11 |
| NASDAQ100 | Nasdaq 100 | 713.4400024414062 | 741.47 | 0.03928851404837763 | 12 |
| SOFTWARE | Software | 103.37000274658203 | 107.13 | 0.03637416226674417 | 13 |
| MOMENTUM | US Momentum Equities | 305.1700134277344 | 316.25 | 0.036307586213379484 | 14 |
| LARGE_GROWTH | US Large-Cap Growth | 122.38999938964844 | 126.25 | 0.03153852953346803 | 15 |
| COMMUNICATIONS | Communication Services Sector | 111.4000015258789 | 114.75 | 0.03007179917625824 | 16 |
| JAPAN | Japan Equities | 95.18000030517578 | 97.96 | 0.029207813468278054 | 17 |
| US_DOLLAR | US Dollar | 27.899999618530273 | 28.48 | 0.02078854442293654 | 18 |
| COPPER | Copper | 39.9900016784668 | 40.67 | 0.01700420837689931 | 19 |
| AGRICULTURE | Agriculture Commodities | 28.31999969482422 | 28.68 | 0.012711875319743493 | 20 |
| EMERGING_MARKETS | Emerging Markets | 60.45000076293945 | 61.14 | 0.011414379294492516 | 21 |
| SP500 | S&P 500 | 765.719970703125 | 773.5 | 0.010160410586824487 | 22 |
| YEN | Japanese Yen | 57.70000076293945 | 58.2 | 0.008665497928064037 | 23 |
| TOTAL_US_MARKET | Total US Stock Market | 378.239990234375 | 381.1 | 0.0075613627312458576 | 24 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 25 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.5999984741211 | 91.57 | -0.000327494264419359 | 26 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 125.58000183105469 | 125.49 | -0.0007166892000509684 | 27 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.05000305175781 | 81.8 | -0.0030469596887170436 | 28 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.91999816894531 | 105.09 | -0.00783608556734905 | 29 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.650001525878906 | 47.21 | -0.009234029628308327 | 30 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.72000122070312 | 93.78 | -0.009923999246081783 | 31 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.61000061035156 | 78.68 | -0.011681957081038252 | 32 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.3499984741211 | 96.21 | -0.011710308084125431 | 33 |
| TIPS | Treasury Inflation-Protected Securities | 107.12999725341797 | 105.68 | -0.013534932237400987 | 34 |
| LARGE_VALUE | US Large-Cap Value | 257.2900085449219 | 253.45 | -0.01492482575067211 | 35 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.41999816894531 | 72.3 | -0.015254674433089921 | 36 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.12000274658203 | 91.59 | -0.01643044138159877 | 37 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.81999969482422 | 91.15 | -0.01799180888078944 | 38 |
| ENERGY | Energy Sector | 63.63999938964844 | 62.46 | -0.01854178819870278 | 39 |
| EURO | Euro | 107.80000305175781 | 105.8 | -0.0185529034799522 | 40 |
| INDIA | India Equities | 49.63999938964844 | 48.5 | -0.022965338510583577 | 41 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.33999633789062 | 102.86 | -0.023542779799761382 | 42 |
| UNITED_KINGDOM | United Kingdom Equities | 48.939998626708984 | 47.69 | -0.025541452018488675 | 43 |
| FINANCIALS | Financials Sector | 57.47999954223633 | 55.9 | -0.027487814106110897 | 44 |
| CHINA | China Equities | 55.65999984741211 | 54.0 | -0.02982392835003378 | 45 |
| CANADA | Canada Equities | 62.36000061035156 | 60.43 | -0.030949335975971604 | 46 |
| HEALTHCARE | Healthcare Sector | 174.6199951171875 | 169.01 | -0.032126877070536186 | 47 |
| AUSTRALIA | Australia Equities | 30.139999389648438 | 29.04 | -0.036496330853484804 | 48 |
| EUROPE | Europe Equities | 92.72000122070312 | 89.24 | -0.03753236815020766 | 49 |
| REGIONAL_BANKS | Regional Banks | 74.86000061035156 | 71.99 | -0.038338239205874425 | 50 |
| SMALL_VALUE | US Small-Cap Value | 224.80999755859375 | 215.95 | -0.03941104779508087 | 51 |
| DIVIDEND | US Dividend Equities | 35.11000061035156 | 33.72 | -0.039589877134372564 | 52 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 221.6699981689453 | 212.68 | -0.04055577319080228 | 53 |
| LOW_VOL | US Low Volatility Equities | 75.30999755859375 | 72.18 | -0.04156151454072876 | 54 |
| BIOTECH | Biotechnology | 165.72999572753906 | 158.23 | -0.045254304717832095 | 55 |
| MID_CAP | US Mid-Cap Stocks | 76.7699966430664 | 73.25 | -0.04585120225330008 | 56 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.98999786376953 | 81.92 | -0.04733106134294207 | 57 |
| MEXICO | Mexico Equities | 77.37999725341797 | 73.7 | -0.047557474593415194 | 58 |
| SMALL_CAP | US Small-Cap Stocks | 299.9599914550781 | 285.58 | -0.047939698175487155 | 59 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.0199966430664 | 112.23 | -0.049059454395489976 | 60 |
| SILVER | Silver | 62.720001220703125 | 59.63 | -0.04926660013653106 | 61 |
| UTILITIES | Utilities Sector | 42.77000045776367 | 40.66 | -0.04933365525322708 | 62 |
| SOLAR | Solar Energy | 49.31999969482422 | 46.71 | -0.05291970216897868 | 63 |
| REAL_ESTATE | Real Estate Sector | 45.08000183105469 | 42.59 | -0.05523517590763216 | 64 |
| INDUSTRIALS | Industrials Sector | 180.25 | 169.98 | -0.05697642163661587 | 65 |
| GOLD | Gold | 86.79000091552734 | 81.67 | -0.0589929814669623 | 66 |
| SOUTH_AFRICA | South Africa Equities | 72.51000213623047 | 68.23 | -0.05902636891651547 | 67 |
| MATERIALS | Materials Sector | 53.540000915527344 | 49.71 | -0.07153531658638035 | 68 |
| METALS_MINING | Metals and Mining | 119.33999633789062 | 109.0 | -0.08664317626267315 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 237.33999633789062 | 216.14 | -0.08932331956266282 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 35.0 | 0.0635416619245579 | 0.022239581673595264 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | MOMENTUM | 35.0 | 0.036307586213379484 | 0.012707655174682819 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | SMALL_VALUE | 30.0 | -0.03941104779508087 | -0.01182331433852426 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SEMICONDUCTORS | 35.0 | 0.0635416619245579 | 0.022239581673595264 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | TAIWAN | 35.0 | 0.1087247997741172 | 0.03805367992094102 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SP500 | 30.0 | 0.010160410586824487 | 0.0030481231760473458 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 35.0 | 0.0635416619245579 | 0.022239581673595264 | V3 selected model rank 1: overreaction with 65% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SP500 | 65.0 | 0.010160410586824487 | 0.006604266881435917 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| openai-gpt-5-6-sol | US_DOLLAR | 35.0 | 0.02078854442293654 | 0.0072759905480277885 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 35.0 | 0.0635416619245579 | 0.022239581673595264 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | MOMENTUM | 30.0 | 0.036307586213379484 | 0.010892275864013845 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-3 | UTILITIES | 35.0 | -0.04933365525322708 | -0.017266779338629478 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | US_DOLLAR | 35.0 | 0.02078854442293654 | 0.0072759905480277885 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | SMALL_VALUE | 30.0 | -0.03941104779508087 | -0.01182331433852426 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-5 | SEMICONDUCTORS | 35.0 | 0.0635416619245579 | 0.022239581673595264 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | MOMENTUM | 35.0 | 0.036307586213379484 | 0.012707655174682819 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | SMALL_VALUE | 30.0 | -0.03941104779508087 | -0.01182331433852426 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 100.0 | 0.010160410586824487 | 0.010160410586824487 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | SEMICONDUCTORS | 3 | 0.575 | 0.0635416619245579 | 0.06334138477058363 | 0.05318097418375914 | 0.07975073483649017 |  | True | True |
| openai-gpt-5-6-sol | US_DOLLAR | 3 | 0.58 | 0.02078854442293654 | 0.0404078480856369 | 0.03024743749881241 | 0.1026842715214369 |  | True | True |
| google-gemini-3-1-pro | SP500 | 2 | 0.65 | 0.010160410586824487 | 0.02884384855503118 | 0.018683437968206693 | 0.11424827105204262 |  | True | True |
| xai-grok-4-5 | SEMICONDUCTORS | 3 | 0.5867 | 0.0635416619245579 | 0.02312392250975382 | 0.012963511922929334 | 0.11996819709731998 |  | True | True |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 3 | 0.5633 | 0.0635416619245579 | 0.02312392250975382 | 0.012963511922929334 | 0.11996819709731998 |  | True | True |
| xai-grok-4-6 | SP500 | 1 | 0.5 | 0.010160410586824487 | 0.010160410586824487 | 0.0 | 0.1329317090202493 |  | False | True |
| xai-grok-4-3 | UTILITIES | 3 | 0.5833 | -0.04933365525322708 | -0.021814103129125947 | -0.031974513715950434 | 0.16490622273619976 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 372f50f24fa959af52ec28cce32c44f66688daa9ba59b9ef2f4c3307d4923470 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | 80e2d18d152d5b23ef1071d97b056dda7aed5da9d629fbc864ac7c6e4c2b8e91 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 831250ef610658f9ebe56ae2f3bdacb7db30ed13e3d0198f3578b756af7f7a52 |
| market_data/universe_decision_context.md | 8d3499cf7ee26a2c596ac147fb92c5b50af5a13922dff6e0b9017513f28b73fd |
| market_data/universe_decision_context.json | 8a483b7b504ecb363a3f7a2a1c64edba5a8e805f2b7e45dbe1d4b2941ecc8b6a |
| market_data/decision_context_source_history.json | c435a1fcf7df786a6ce0a9753b7f557f0a0e0f59173dfc8cc6e9ca4d52ec5323 |
| market_data/universe_quality_evidence.md | fe972b62f64a7799525277a89623b4a97a072384449a7ca548f2f94643b78258 |
| market_data/universe_quality_evidence.json | 0bdd003daa6dbff4490aa10327e3077e4bafc958cf7e82bb4432fc178fd297ee |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | b799bad6842f0384d16df626fb10a05cbef220ff299d47a7beb265d3874c8fcc | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 9d295a31b55247f6431c13617f5395df910b100c4fc0a865e22fb6e7990e5c0d | yes |
| Final briefing | research/final_briefing.md | model-facing | 372f50f24fa959af52ec28cce32c44f66688daa9ba59b9ef2f4c3307d4923470 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
