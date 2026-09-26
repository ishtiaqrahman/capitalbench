# CapitalBench Report: CB-2026-08-25-1M / official-v3-20260825-monthly-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260825-monthly-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-25-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-08-25
- Decision deadline: 2026-08-26T13:25:00Z
- Horizon: one month
- Entry date: 2026-08-26
- Exit date: 2026-09-25
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | openai | portfolio | SEMICONDUCTORS | 3 | 0.57 | Broad participation and falling Treasury yields favor selective pullback reversals, but weak labor and consumer data, persistent inflation, and major policy and earnings events create high cross-sectional dispersion and limit conviction. | Nvidia results could trigger a broad semiconductor and growth-stock reversal after the entry close.; The September CPI and FOMC outcomes could push yields higher and hurt rate-sensitive real estate.; Weak employment, retail, and housing data could deteriorate further and pressure cyclical risk assets.; High thematic volatility could overwhelm the modest estimated median excess returns. |
| anthropic-claude-fable-5 | anthropic | portfolio | SEMICONDUCTORS | 3 | 0.5667 | Yields are falling (10y 4.63% from 4.74%) on weak payrolls, weak retail sales, and cooling CPI, raising odds of a dovish September FOMC. Prior leaders in tech/semis pulled back modestly while rate-sensitive groups sold off; a Nvidia earnings catalyst on Aug 26 and the Sept 15-16 FOMC dominate the window. Favor quality pullbacks in strong-trend groups and rate-sensitive reversal candidates. | Nvidia earnings miss could hit semiconductors hard given 2.4 beta and 53% vol; Hot August CPI/PPI or hawkish FOMC on Sept 16 would reverse the rates tailwind for banks and industrials; Labor market deterioration (Sept 4 payrolls) could trigger broad risk-off, hurting cyclical picks; Payroll benchmark revisions Aug 28 could shift Fed expectations abruptly |
| xai-grok-4-3 | xai | portfolio | US_DOLLAR | 3 | 0.5833 | Mixed signals with crypto short-term continuation offset by quality pullbacks in defensives and dollar; recent equity weakness shows limited reversal support within one-month window. | crypto volatility spillover; macro data releases within window; rate sensitivity in defensives; volume dislocation reversal failure |
| anthropic-claude-opus-5 | anthropic | portfolio | INDUSTRIALS | 3 | 0.57 | Broad indices near highs with 88% of assets positive over 21 sessions, but leadership is rotating hard: precious metals, EM and biotech leading while defense, industrials, utilities and regional banks sold off. Macro is soft-growth/sticky-inflation (payrolls -23k, core CPI 2.5%, PCE 3.3% core y/y) with the Fed on hold and a hawkish minority; 10y fell to 4.63%. Big in-window catalysts: Nvidia earnings, Jackson Hole, Sept 4 payrolls, Sept 11 CPI, Sept 15-16 FOMC. Dispersion is high, so a small number of high-quality relative pullbacks offers the cleanest reversal setups. | Nvidia results on Aug 26 could drive a broad index move that swamps sector reversal edges; Sept 4 payrolls and Sept 11 CPI plus the Sept 15-16 FOMC could shift rates sharply against cyclicals and regional banks; Consumer softening (confidence 89.4, retail sales -0.6%, home sales -10.5%) could extend weakness in domestic cyclicals and small caps; Reversal candidates' pullbacks may reflect early fundamental deterioration not captured in the frozen briefing; Continued momentum in gold, metals and crypto could keep leadership away from value/cyclicals for the whole window |
| xai-grok-4-6 | xai | portfolio | AEROSPACE_DEFENSE | 3 | 0.565 | SPY is within 1.54% of its 52-week high after a modest 5-session dip while 21-session breadth is still broad. Soft July payrolls, cooling confidence, and a packed September data/FOMC calendar favor mixed mean-reversion in shocked cyclicals over chasing crypto or high-beta continuation. | September 4 Employment Situation and September 15-16 FOMC/SEP can reprice rates and defensives quickly; August 26 Nvidia results can dominate semis and growth beta independently of sector reversals; Further crude weakness after the 3.6% Brent drop can spill into cyclicals; Crypto 20%+ 5-session spikes can reverse violently given 40-60% horizon vol |
| xai-grok-4-5 | xai | portfolio | AEROSPACE_DEFENSE | 3 | 0.59 | Cross-sectional dispersion is elevated with crypto short-term strength, rate-sensitive and industrial shock pullbacks, soft labor/housing prints, and a dense macro/Fed calendar inside the one-month window; edge is selective mean-reversion in quality pullbacks rather than broad momentum chase. | Nvidia earnings and Jackson Hole/FOMC path could reverse growth and rate-sensitive factors within the scoring window; Further labor or CPI downside could extend industrial and bank underperformance rather than reverse it; Oil and dollar residual volatility may spill into beta and financials if energy keeps sliding; Crypto momentum failure would not directly hit top ranks but would raise overall risk-off correlation |
| google-gemini-3-1-pro | google | portfolio | SOLAR | 3 | 0.58 | The market is showing mixed signals with some sectors experiencing pullbacks while others continue to show strength. The upcoming Jackson Hole symposium and employment data will be key drivers. | Unexpected macroeconomic data releases, particularly employment and inflation figures.; Geopolitical events impacting energy prices and defense spending. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 127.3499984741211 | 148.33 | 0.16474284866318456 | 1 |
| SEMICONDUCTORS | Semiconductors | 555.77001953125 | 606.56 | 0.09138668636999792 | 2 |
| ETHEREUM_ETF | Ethereum ETF | 18.649999618530273 | 20.31 | 0.08900806517016657 | 3 |
| TAIWAN | Taiwan Equities | 106.38999938964844 | 114.78 | 0.07886080137686236 | 4 |
| CYBERSECURITY | Cybersecurity | 93.66000366210938 | 100.95 | 0.07783467918910447 | 5 |
| TECHNOLOGY | Technology Sector | 182.83999633789062 | 196.27 | 0.07345222014383856 | 6 |
| BROAD_COMMODITIES | Broad Commodities | 18.18000030517578 | 19.5 | 0.07260724272091568 | 7 |
| BITCOIN_ETF | Bitcoin ETF | 44.459999084472656 | 47.57 | 0.06995053935152895 | 8 |
| MOMENTUM | US Momentum Equities | 304.0 | 318.5 | 0.047697368421052655 | 9 |
| NASDAQ100 | Nasdaq 100 | 711.3699951171875 | 744.5 | 0.046572114525795794 | 10 |
| BROAD_AI_TECH | Broad AI Technology | 63.06999969482422 | 65.97 | 0.045980661474678275 | 11 |
| SOUTH_KOREA | South Korea Equities | 179.17999267578125 | 187.18 | 0.04464788286209176 | 12 |
| LARGE_GROWTH | US Large-Cap Growth | 121.75 | 126.25 | 0.03696098562628336 | 13 |
| SOFTWARE | Software | 102.38999938964844 | 106.01 | 0.03535502130999668 | 14 |
| BRAZIL | Brazil Equities | 35.720001220703125 | 36.82 | 0.030795037561737848 | 15 |
| JAPAN | Japan Equities | 95.43000030517578 | 97.93 | 0.026197209334899663 | 16 |
| US_DOLLAR | US Dollar | 28.020000457763672 | 28.62 | 0.021413259544400987 | 17 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.33000183105469 | 124.42 | 0.017084918970505125 | 18 |
| COPPER | Copper | 40.060001373291016 | 40.61 | 0.013729371139654667 | 19 |
| YEN | Japanese Yen | 57.54999923706055 | 58.3 | 0.013032159389786191 | 20 |
| SP500 | S&P 500 | 766.0800170898438 | 771.35 | 0.00687915464780775 | 21 |
| TOTAL_US_MARKET | Total US Stock Market | 378.2300109863281 | 379.77 | 0.004071567482590632 | 22 |
| COMMUNICATIONS | Communication Services Sector | 112.61000061035156 | 112.96 | 0.003108066670379328 | 23 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 24 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.62999725341797 | 91.62 | -0.00010910459148349982 | 25 |
| AGRICULTURE | Agriculture Commodities | 28.59000015258789 | 28.54 | -0.0017488685666678938 | 26 |
| ENERGY | Energy Sector | 62.43000030517578 | 62.04 | -0.006247001493982829 | 27 |
| EMERGING_MARKETS | Emerging Markets | 60.65999984741211 | 60.16 | -0.008242661534286877 | 28 |
| HEALTHCARE | Healthcare Sector | 173.5399932861328 | 170.7 | -0.016365065091654363 | 29 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.779998779296875 | 46.94 | -0.017580552548294492 | 30 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.44999694824219 | 71.84 | -0.021919632609061823 | 31 |
| EURO | Euro | 107.5999984741211 | 105.15 | -0.022769502870488734 | 32 |
| LARGE_VALUE | US Large-Cap Value | 258.4599914550781 | 251.93 | -0.025264999113849607 | 33 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.9000015258789 | 77.86 | -0.025531933503382565 | 34 |
| TIPS | Treasury Inflation-Protected Securities | 107.51000213623047 | 104.54 | -0.027625356499082265 | 35 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.86000061035156 | 95.12 | -0.027999188567976785 | 36 |
| UNITED_KINGDOM | United Kingdom Equities | 48.86000061035156 | 47.32 | -0.03151863673995314 | 37 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.30999755859375 | 92.18 | -0.032840180870527425 | 38 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.77999877929688 | 103.21 | -0.03343321614636552 | 39 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.58000183105469 | 90.34 | -0.03462280153514041 | 40 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.31999969482422 | 90.0 | -0.03557650777626775 | 41 |
| INDIA | India Equities | 49.75 | 47.86 | -0.0379899497487437 | 42 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.44999694824219 | 101.17 | -0.040587928611728 | 43 |
| REGIONAL_BANKS | Regional Banks | 74.58000183105469 | 71.55 | -0.040627537632923705 | 44 |
| CANADA | Canada Equities | 62.22999954223633 | 59.59 | -0.042423261476075114 | 45 |
| EUROPE | Europe Equities | 92.69999694824219 | 88.63 | -0.04390503864325501 | 46 |
| CHINA | China Equities | 55.099998474121094 | 52.62 | -0.04500904796369243 | 47 |
| MID_CAP | US Mid-Cap Stocks | 76.62000274658203 | 72.99 | -0.047376698204881884 | 48 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.30000305175781 | 79.32 | -0.047779146529981165 | 49 |
| SMALL_VALUE | US Small-Cap Value | 224.33999633789062 | 213.49 | -0.048364074685767755 | 50 |
| CONSUMER_STAPLES | Consumer Staples Sector | 86.2699966430664 | 82.06 | -0.04880024118332649 | 51 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 222.11000061035156 | 211.11 | -0.04952501274199217 | 52 |
| DIVIDEND | US Dividend Equities | 35.04999923706055 | 33.21 | -0.052496413041715595 | 53 |
| MEXICO | Mexico Equities | 77.55000305175781 | 73.34 | -0.054287593631015096 | 54 |
| INDUSTRIALS | Industrials Sector | 180.33999633789062 | 170.43 | -0.05495173860003266 | 55 |
| SILVER | Silver | 61.59000015258789 | 58.14 | -0.05601558928463368 | 56 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.16000366210938 | 110.56 | -0.05633324902535719 | 57 |
| SMALL_CAP | US Small-Cap Stocks | 298.92999267578125 | 281.97 | -0.0567356675185684 | 58 |
| AUSTRALIA | Australia Equities | 30.149999618530273 | 28.43 | -0.05704808093838776 | 59 |
| FINANCIALS | Financials Sector | 58.2599983215332 | 54.84 | -0.05870234157334586 | 60 |
| LOW_VOL | US Low Volatility Equities | 75.87999725341797 | 71.3 | -0.060358426715832136 | 61 |
| GOLD | Gold | 86.37000274658203 | 80.66 | -0.06611094784071891 | 62 |
| MATERIALS | Materials Sector | 53.66999816894531 | 49.8 | -0.0721072908697169 | 63 |
| SOUTH_AFRICA | South Africa Equities | 71.68000030517578 | 66.48 | -0.07254464680576045 | 64 |
| REAL_ESTATE | Real Estate Sector | 45.09000015258789 | 41.56 | -0.07828787182617225 | 65 |
| BIOTECH | Biotechnology | 168.38999938964844 | 155.03 | -0.0793396249069036 | 66 |
| UTILITIES | Utilities Sector | 43.5099983215332 | 39.51 | -0.09193285396091588 | 67 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 236.3800048828125 | 213.81 | -0.09548186994074126 | 68 |
| SOLAR | Solar Energy | 48.779998779296875 | 44.06 | -0.09676094500642196 | 69 |
| METALS_MINING | Metals and Mining | 120.30999755859375 | 108.33 | -0.09957607681572112 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 35.0 | 0.09138668636999792 | 0.03198534022949927 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | REGIONAL_BANKS | 35.0 | -0.040627537632923705 | -0.014219638171523295 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | INDUSTRIALS | 30.0 | -0.05495173860003266 | -0.016485521580009797 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | INDUSTRIALS | 35.0 | -0.05495173860003266 | -0.01923310851001143 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | REGIONAL_BANKS | 35.0 | -0.040627537632923705 | -0.014219638171523295 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SMALL_VALUE | 30.0 | -0.048364074685767755 | -0.014509222405730327 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SOLAR | 35.0 | -0.09676094500642196 | -0.03386633075224768 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | UTILITIES | 35.0 | -0.09193285396091588 | -0.032176498886320556 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 30.0 | -0.09548186994074126 | -0.028644560982222376 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 35.0 | 0.09138668636999792 | 0.03198534022949927 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | CYBERSECURITY | 35.0 | 0.07783467918910447 | 0.027242137716186565 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | REAL_ESTATE | 30.0 | -0.07828787182617225 | -0.023486361547851674 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-3 | US_DOLLAR | 35.0 | 0.021413259544400987 | 0.007494640840540345 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | SMALL_VALUE | 35.0 | -0.048364074685767755 | -0.016927426140018714 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | UTILITIES | 30.0 | -0.09193285396091588 | -0.027579856188274764 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-5 | AEROSPACE_DEFENSE | 35.0 | -0.09548186994074126 | -0.03341865447925944 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | REGIONAL_BANKS | 35.0 | -0.040627537632923705 | -0.014219638171523295 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | INDUSTRIALS | 30.0 | -0.05495173860003266 | -0.016485521580009797 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | AEROSPACE_DEFENSE | 35.0 | -0.09548186994074126 | -0.03341865447925944 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | UTILITIES | 35.0 | -0.09193285396091588 | -0.032176498886320556 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 30.0 | 0.00687915464780775 | 0.002063746394342325 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 3 | 0.57 | 0.09138668636999792 | 0.03574111639783416 | 0.028861961750026408 | 0.1290017322653504 |  | True | True |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 3 | 0.5667 | 0.09138668636999792 | 0.0012801804779661759 | -0.0055989741698415744 | 0.16346266818521837 |  | False | True |
| xai-grok-4-3 | US_DOLLAR | 3 | 0.5833 | 0.021413259544400987 | -0.03701264148775313 | -0.04389179613556088 | 0.2017554901509377 |  | False | False |
| anthropic-claude-opus-5 | INDUSTRIALS | 3 | 0.57 | -0.05495173860003266 | -0.04796196908726505 | -0.0548411237350728 | 0.2127048177504496 |  | False | False |
| xai-grok-4-6 | AEROSPACE_DEFENSE | 3 | 0.565 | -0.09548186994074126 | -0.06353140697123767 | -0.07041056161904542 | 0.22827425563442222 |  | False | False |
| xai-grok-4-5 | AEROSPACE_DEFENSE | 3 | 0.59 | -0.09548186994074126 | -0.06412381423079253 | -0.07100296887860028 | 0.22886666289397709 |  | False | False |
| google-gemini-3-1-pro | SOLAR | 3 | 0.58 | -0.09676094500642196 | -0.09468739062079061 | -0.10156654526859836 | 0.2594302392839752 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | f80b43cbb211635532aa200e6f0bb830f1cfa3c34b67c84311f51497a3a9f02b |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | c2e976bf2568f2f50f9d55c5285bd32d5ca76c67888ac6dea690eab9e901b192 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 32ad6cdfdb755021e01f943de580068fb0e39c3c3cb32c011858353b99e98dc7 |
| market_data/universe_decision_context.md | 056fdf3cae375fbcfc0df2605b4b503f2bb266937881b8277174a5f04e21db0c |
| market_data/universe_decision_context.json | be3e5f55b68b8d0733fb842eedda580174fe228c628992ea2250c52a08800e17 |
| market_data/decision_context_source_history.json | a7ac46bbc2dbe576ddc845d1c9adbfa4ce94095e16c42136be95f7e838e8ab87 |
| market_data/universe_quality_evidence.md | a8867a88b498d2ab601b687d00807bd0715970725600cf149b6d43571b74ec1a |
| market_data/universe_quality_evidence.json | 8a1224dda72d86b8f60eb5086893afd8a21cbab9630b7132e3a5e4ef551180aa |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | fea2ce583f511a928c8ad143ddc49912f10b1f67f39127a844b526c2473ef697 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | b6e5821ef98a7fb55e227b36298f660dd1b55eb7f23bbae2731ca935e77c16c9 | yes |
| Final briefing | research/final_briefing.md | model-facing | f80b43cbb211635532aa200e6f0bb830f1cfa3c34b67c84311f51497a3a9f02b | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
