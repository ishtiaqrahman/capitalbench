# CapitalBench Report: CB-2026-09-13-1W / official-v3-20260913-weekly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260913-weekly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-13-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-09-13
- Decision deadline: 2026-09-14T13:25:00Z
- Horizon: one week
- Entry date: 2026-09-14
- Exit date: 2026-09-21
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | HEALTHCARE | 3 | 0.59 | Elevated CPI, weaker sentiment, and FOMC week create mixed one-week setup; oil strength continues on unresolved Iran supply risk while several high-quality names show sharp relative pullbacks after solid prior active trends, favoring selective reversal over broad continuation. | FOMC September 15-16 decision and SEP can reverse rate-sensitive and risk-asset moves within the scoring window; Further upside oil shock from unresolved Iran conflict could pressure equities and non-energy cyclicals; Weaker consumer sentiment and sticky CPI may extend defensive rotation or risk-off rather than mean-reversion; High-vol names (crypto, biotech, software) can gap against SPY on any hawkish surprise |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | Five-session active-return dispersion is only 2.24% with just ~20% of assets positive, SPY is near a 52-week high, and the FOMC meeting plus inflation/sentiment prints dominate a one-week window. Oil shows independent continuation versus a slightly weaker equity tape; most shock-reversal names are high-vol pullbacks without in-window fundamental confirmation. | FOMC Sept 15-16 and SEP can reprice duration, growth, and risk assets inside the scoring window; Iran-related oil supply conditions can reverse after the Sept 11 Brent drop from ~$110; CPI 3.4% and Michigan inflation expectations 4.6% can keep real-rate pressure on crypto, software, and silver; Equal-weight lag (RSP-SPY 5s -1.21%) can persist if mega-cap concentration reasserts |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SP500 | 2 | 0.56 | Stagflationary backdrop: CPI 3.4% y/y with 0.4% m/m, 10y at 4.96% and 30y at 5.35%, Michigan sentiment collapsing to 47.8 with inflation expectations rising, Brent above $100 on an unresolved Iran conflict. FOMC on Sept 15-16 is the dominant in-window catalyst with an unknown outcome; positive asset share is only ~20% over 5 and 21 sessions, so breadth is weak and defensive/energy-linked exposures have been the relative leaders. Most slate candidates are volatile pullback names whose one-week outcome is dominated by the Fed decision rather than by mean-reversion mechanics, so edge versus SPY is thin. | FOMC Sept 15-16 delivers a dovish surprise that lifts high-beta growth and crypto sharply, leaving defensive picks lagging SPY; Iran conflict de-escalation or ceasefire collapses crude, pressuring oil and energy-linked exposures; Hot retail sales or continued yield rise (10y near 5%) hits rate-sensitive healthcare and dividend names alongside broad equities; Sector-specific policy or drug-pricing headlines could drive healthcare divergence unrelated to the reversal thesis |
| xai-grok-4-3 | xai | portfolio | SP500 | 2 | 0.55 | Mixed signals from rising CPI, weak sentiment, unresolved Iran supply risks, and upcoming FOMC create short-term uncertainty favoring selective continuation in energy and quality defensives over broad equity momentum. | FOMC policy surprise; Iran supply disruption escalation; CPI revision risk |
| openai-gpt-6-astra | openai | portfolio | HEALTHCARE | 3 | 0.575 | Weak breadth, rising inflation expectations and unresolved energy supply risk favor selective defensiveness rather than a broad loser rebound. Oil has independent supply-side support, but its sharp advance and recent intraday reversal limit conviction. The September 15–16 FOMC and September 16 retail sales fall inside the scoring window and could dominate relative returns. Quality scores are technical composites, not independent evidence of earnings resilience. | A hawkish FOMC or higher projected rates could extend losses in both equities and duration-sensitive assets.; Iran-related de-escalation or improved supply conditions could abruptly reverse oil's premium.; A dovish FOMC and strong retail sales could favor high-beta growth over healthcare and dividend equities.; Low-volume pullbacks do not prove overreaction; unreported sector-specific deterioration could invalidate the defensive reversal cases.; Price adjustments before the September 14 entry close may absorb much of the available edge. |
| google-gemini-3-1-pro | google | portfolio | HEALTHCARE | 3 | 0.57 | The market is facing a mixed environment with upcoming FOMC meeting and retail sales data. Recent inflation data was slightly higher than expected, but consumer sentiment dipped. Oil prices are volatile due to geopolitical tensions. | FOMC meeting outcome surprises the market.; Geopolitical tensions in Iran de-escalate, leading to a drop in oil prices. |
| anthropic-claude-opus-5 | anthropic | portfolio | HEALTHCARE | 3 | 0.5733 | Breadth is weak (positive asset share ~20% over 5 sessions, RSP trailing SPY by 1.2pp), inflation is sticky at 3.4% headline with sentiment deteriorating sharply, and the FOMC meets Sep 15-16 inside the scoring window. Oil is the dominant trend on unresolved Iran supply risk. With a live policy catalyst and modest dispersion (2.24%), I favor defensive quality pullbacks with high prior relative strength (healthcare, dividend) over levered beta, and avoid mechanical extrapolation of the crypto and oil moves. | A hawkish FOMC dot plot on September 16 could hit rate-sensitive and low-beta defensives together with duration; Biotech's 32.8% volatility means the reversal thesis can invert quickly on financing or clinical headlines; Escalation or resolution in the Iran conflict could drive a large energy move that reshapes sector leadership within the week; Breadth deterioration (only 20% of assets positive) may continue, with mega-cap SPY outperforming defensive equal-weight-style exposures |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SEMICONDUCTORS | Semiconductors | 541.5 | 596.03 | 0.10070175438596496 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 44.7400016784668 | 49.01 | 0.09544028076307232 | 2 |
| ETHEREUM_ETF | Ethereum ETF | 19.170000076293945 | 20.85 | 0.08763692837871107 | 3 |
| TAIWAN | Taiwan Equities | 107.20999908447266 | 115.64 | 0.07863073395686904 | 4 |
| SOUTH_KOREA | South Korea Equities | 176.22000122070312 | 189.16 | 0.07343093116365629 | 5 |
| COPPER | Copper | 38.2599983215332 | 40.67 | 0.06299011458948289 | 6 |
| TECHNOLOGY | Technology Sector | 184.27999877929688 | 194.85 | 0.0573583747054518 | 7 |
| MOMENTUM | US Momentum Equities | 299.70001220703125 | 316.25 | 0.05522184557515497 | 8 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 119.59500122070312 | 125.49 | 0.04929134762428844 | 9 |
| SILVER | Silver | 56.84000015258789 | 59.63 | 0.049085148485614294 | 10 |
| NASDAQ100 | Nasdaq 100 | 709.1799926757812 | 741.47 | 0.045531469665953894 | 11 |
| BROAD_AI_TECH | Broad AI Technology | 63.470001220703125 | 66.31 | 0.0447455289849672 | 12 |
| LARGE_GROWTH | US Large-Cap Growth | 121.26000213623047 | 126.25 | 0.04115122691622153 | 13 |
| CYBERSECURITY | Cybersecurity | 100.05000305175781 | 103.09 | 0.030384776167068583 | 14 |
| EMERGING_MARKETS | Emerging Markets | 59.61000061035156 | 61.14 | 0.025666823921869586 | 15 |
| TOTAL_US_MARKET | Total US Stock Market | 374.67999267578125 | 381.1 | 0.017134641426595154 | 16 |
| SP500 | S&P 500 | 760.8800048828125 | 773.5 | 0.016586051724583273 | 17 |
| GOLD | Gold | 80.54000091552734 | 81.67 | 0.0140302839784896 | 18 |
| CHINA | China Equities | 53.31999969482422 | 54.0 | 0.012753194093543696 | 19 |
| US_DOLLAR | US Dollar | 28.170000076293945 | 28.48 | 0.011004612100336209 | 20 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 80.93000030517578 | 81.8 | 0.010750027079495572 | 21 |
| SOLAR | Solar Energy | 46.220001220703125 | 46.71 | 0.010601444533874016 | 22 |
| BRAZIL | Brazil Equities | 37.720001220703125 | 38.07 | 0.009278864474287829 | 23 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.72000122070312 | 72.3 | 0.008086987861475992 | 24 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 104.30000305175781 | 105.09 | 0.007574275408699371 | 25 |
| HEALTHCARE | Healthcare Sector | 167.75 | 169.01 | 0.007511177347242937 | 26 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 93.22000122070312 | 93.78 | 0.006007281398452857 | 27 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.93000030517578 | 47.21 | 0.005966326294554403 | 28 |
| SOFTWARE | Software | 106.63999938964844 | 107.13 | 0.004594904474456651 | 29 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 91.22000122070312 | 91.59 | 0.004056114605849315 | 30 |
| BIOTECH | Biotechnology | 157.60000610351562 | 158.23 | 0.0039974230462311855 | 31 |
| JAPAN | Japan Equities | 97.58000183105469 | 97.96 | 0.003894221785353258 | 32 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 95.88999938964844 | 96.21 | 0.0033371635456085347 | 33 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 90.93000030517578 | 91.15 | 0.0024194401637069873 | 34 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.52999877929688 | 78.68 | 0.0019101136258095064 | 35 |
| INDIA | India Equities | 48.43000030517578 | 48.5 | 0.0014453787813983876 | 36 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.5 | 91.57 | 0.0007650273224042436 | 37 |
| INDUSTRIALS | Industrials Sector | 169.92999267578125 | 169.98 | 0.0002942819182847334 | 38 |
| EUROPE | Europe Equities | 89.2300033569336 | 89.24 | 0.00011203230629064365 | 39 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 40 |
| AUSTRALIA | Australia Equities | 29.059999465942383 | 29.04 | -0.0006882128805894006 | 41 |
| CANADA | Canada Equities | 60.5 | 60.43 | -0.001157024793388417 | 42 |
| TIPS | Treasury Inflation-Protected Securities | 105.81999969482422 | 105.68 | -0.0013229984429026231 | 43 |
| MUNICIPAL_BONDS | Municipal Bonds | 103.11000061035156 | 102.86 | -0.0024246009976889304 | 44 |
| COMMUNICATIONS | Communication Services Sector | 115.06999969482422 | 114.75 | -0.002780913319482825 | 45 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 216.77000427246094 | 216.14 | -0.002906325875553728 | 46 |
| SOUTH_AFRICA | South Africa Equities | 68.48999786376953 | 68.23 | -0.0037961435520362796 | 47 |
| UNITED_KINGDOM | United Kingdom Equities | 47.90999984741211 | 47.69 | -0.0045919400566225566 | 48 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.8499984741211 | 112.23 | -0.005494005161757021 | 49 |
| EURO | Euro | 106.55000305175781 | 105.8 | -0.007038977290253934 | 50 |
| MID_CAP | US Mid-Cap Stocks | 73.79000091552734 | 73.25 | -0.007318077094829123 | 51 |
| LARGE_VALUE | US Large-Cap Value | 255.3699951171875 | 253.45 | -0.007518483588122571 | 52 |
| SMALL_CAP | US Small-Cap Stocks | 287.9100036621094 | 285.58 | -0.008092819396591344 | 53 |
| AGRICULTURE | Agriculture Commodities | 28.959999084472656 | 28.68 | -0.00966847697943407 | 54 |
| METALS_MINING | Metals and Mining | 110.16999816894531 | 109.0 | -0.010619934541081899 | 55 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 215.00999450683594 | 212.68 | -0.010836679997970333 | 56 |
| REAL_ESTATE | Real Estate Sector | 43.119998931884766 | 42.59 | -0.01229125568212519 | 57 |
| MEXICO | Mexico Equities | 74.81999969482422 | 73.7 | -0.01496925553852535 | 58 |
| MATERIALS | Materials Sector | 50.4900016784668 | 49.71 | -0.01544863641387939 | 59 |
| SMALL_VALUE | US Small-Cap Value | 219.4499969482422 | 215.95 | -0.01594894963278437 | 60 |
| BROAD_COMMODITIES | Broad Commodities | 19.780000686645508 | 19.44 | -0.01718911399609091 | 61 |
| DIVIDEND | US Dividend Equities | 34.34000015258789 | 33.72 | -0.018054751014355164 | 62 |
| FINANCIALS | Financials Sector | 57.029998779296875 | 55.9 | -0.019814111932036194 | 63 |
| YEN | Japanese Yen | 59.43000030517578 | 58.2 | -0.02069662289853058 | 64 |
| LOW_VOL | US Low Volatility Equities | 73.81999969482422 | 72.18 | -0.022216197529179915 | 65 |
| UTILITIES | Utilities Sector | 41.81999969482422 | 40.66 | -0.027737917343117258 | 66 |
| REGIONAL_BANKS | Regional Banks | 74.11000061035156 | 71.99 | -0.02860613402903478 | 67 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.41999816894531 | 81.92 | -0.029613814536482153 | 68 |
| ENERGY | Energy Sector | 64.52999877929688 | 62.46 | -0.032078084897794734 | 69 |
| OIL | Crude Oil | 156.66000366210938 | 148.16 | -0.0542576500919949 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | HEALTHCARE | 35.0 | 0.007511177347242937 | 0.0026289120715350276 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 65.0 | 0.016586051724583273 | 0.010780933620979127 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5 | HEALTHCARE | 35.0 | 0.007511177347242937 | 0.0026289120715350276 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | DIVIDEND | 35.0 | -0.018054751014355164 | -0.006319162855024307 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | BIOTECH | 30.0 | 0.0039974230462311855 | 0.0011992269138693557 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | HEALTHCARE | 35.0 | 0.007511177347242937 | 0.0026289120715350276 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | DIVIDEND | 35.0 | -0.018054751014355164 | -0.006319162855024307 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SP500 | 30.0 | 0.016586051724583273 | 0.004975815517374982 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| openai-gpt-6-astra | HEALTHCARE | 35.0 | 0.007511177347242937 | 0.0026289120715350276 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-6-astra | DIVIDEND | 35.0 | -0.018054751014355164 | -0.006319162855024307 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 30.0 | 0.016586051724583273 | 0.004975815517374982 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | DIVIDEND | 35.0 | -0.018054751014355164 | -0.006319162855024307 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 65.0 | 0.016586051724583273 | 0.010780933620979127 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | HEALTHCARE | 35.0 | 0.007511177347242937 | 0.0026289120715350276 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | BIOTECH | 35.0 | 0.0039974230462311855 | 0.0013990980661809148 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | BITCOIN_ETF | 30.0 | 0.09544028076307232 | 0.028632084228921693 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 100.0 | 0.016586051724583273 | 0.016586051724583273 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | HEALTHCARE | 3 | 0.59 | 0.007511177347242937 | 0.03266009436663764 | 0.016074042642054365 | 0.06804166001932732 |  | True | True |
| xai-grok-4-6 | SP500 | 1 | 0.5 | 0.016586051724583273 | 0.016586051724583273 | 0.0 | 0.08411570266138169 |  | False | True |
| anthropic-claude-fable-5-1 | SP500 | 2 | 0.56 | 0.016586051724583273 | 0.013409845692514154 | -0.003176206032069119 | 0.0872919086934508 |  | False | True |
| xai-grok-4-3 | SP500 | 2 | 0.55 | 0.016586051724583273 | 0.00446177076595482 | -0.012124280958628452 | 0.09623998362001014 |  | False | True |
| openai-gpt-6-astra | HEALTHCARE | 3 | 0.575 | 0.007511177347242937 | 0.0012855647338857025 | -0.015300486990697571 | 0.09941618965207925 |  | False | True |
| google-gemini-3-1-pro | HEALTHCARE | 3 | 0.57 | 0.007511177347242937 | 0.0012855647338857025 | -0.015300486990697571 | 0.09941618965207925 |  | False | True |
| anthropic-claude-opus-5 | HEALTHCARE | 3 | 0.5733 | 0.007511177347242937 | -0.002491023869619924 | -0.019077075594203196 | 0.10319277825558489 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | b9ac7fb7f90a1baa6a921c4bc325ee0106a666f42a2ad92dfac735a03d81eaee |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | 444197ccb77b225db48d0d2d9b6609544dd2c97a833b6ff3a4b28f070f653061 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 3bf139701814629c82443dfc8b256bb8c73a19c41e2bd000382352af5ab990c3 |
| market_data/universe_decision_context.md | b30ee8d0ad026f1d1fd1646421e2a46fecfa462ef4a1339a9b04a7ef106d6c55 |
| market_data/universe_decision_context.json | 0e3fda0995ae7c7e8199e7875a4f411c585443dbefecb46f988ad44fcb3ad7e3 |
| market_data/decision_context_source_history.json | fa89ac31cb5d7a25e30bcd97967b35c718e0bdd0d9f800995ddb5bce4cf5b46a |
| market_data/universe_quality_evidence.md | e909bfb516e6f6c21549e5210c632e9511098ed37b4d6bc761ee3647c07b0090 |
| market_data/universe_quality_evidence.json | 0563d93491ab8c26e143fa8709737d328b4e8ab12b7b515c6d239d14133a062e |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | fb1d3eb7614ae479bb67c3844d6cb4d2826b26d96598cbf5552b87bb67d5d1c6 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 616dae7c607a6c8212aec11eb32fbfd211117b717bce498f38af81b077cceb0b | yes |
| Final briefing | research/final_briefing.md | model-facing | b9ac7fb7f90a1baa6a921c4bc325ee0106a666f42a2ad92dfac735a03d81eaee | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
