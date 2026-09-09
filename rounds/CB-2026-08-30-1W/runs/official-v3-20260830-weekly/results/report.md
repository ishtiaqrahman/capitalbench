# CapitalBench Report: CB-2026-08-30-1W / official-v3-20260830-weekly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260830-weekly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-30-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-08-30
- Decision deadline: 2026-08-31T13:25:00Z
- Horizon: one week
- Entry date: 2026-08-31
- Exit date: 2026-09-08
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | SILVER | 3 | 0.5767 | The market is digesting mixed economic signals, with solid GDP growth but a slight contraction in payrolls and a downward benchmark revision. The Fed remains focused on inflation, which is still above target, suggesting rates will stay higher for longer. This environment favors defensive positioning and selective opportunities in sectors with strong fundamentals or recent overreactions. | A stronger-than-expected employment report on September 4 could lead to a reassessment of Fed policy, negatively impacting precious metals.; Continued weakness in global manufacturing could weigh on industrial commodities like Silver and Oil. |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Tech short-continuation amid commodity shock_reversals and macro data showing solid but inflation-sticky growth; one-week window favors limited edges. | Fed policy signals on persistent inflation; One-week volatility in tech and commodities; Labor market revisions and upcoming employment data |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | Five-session active-return dispersion is only 1.62% with 40.6% of assets positive versus 73.9% over 21 sessions, SPY is 1.1% from its 52-week high, and a hawkish Chair speech plus a jobs print and Labor Day close sit inside the week, so breadth is mixed and a one-week SPY-relative edge is thin. | August employment report on September 4 can reprice rates and risk assets before the September 8 close.; Labor Day closure on September 7 compresses liquidity and can exaggerate residual moves in high-vol metals and crypto.; Chair Warsh restated a firm 2% PCE objective with inflation still too high, which can keep real-rate pressure on gold, silver, and duration-sensitive growth.; Software and cybersecurity already posted large short-window gains with weak volume confirmation, raising mean-reversion risk if mega-cap tech fades. |
| openai-gpt-5-6-sol | openai | portfolio | SILVER | 3 | 0.57 | Breadth weakened while mega-cap technology held firm, creating a mixed setup of narrow continuation and selective reversal. The employment report is the main in-window catalyst, while high real yields and dollar strength constrain precious metals and other high-duration exposures. | A stronger-than-expected employment report could lift yields and the dollar, extending precious-metals weakness.; A broad risk-off response to labor deterioration could overwhelm the reversal signals in South African and other high-beta assets.; Recent pullbacks may reflect an emerging regime change rather than temporary overreaction.; Holiday-shortened trading and high volatility could amplify gap risk before the September 8 exit. |
| anthropic-claude-fable-5 | anthropic | portfolio | SILVER | 3 | 0.58 | SPY grinds higher but breadth is weak (RSP lagging, only 41% of assets positive over 5 sessions). Inflation remains sticky (PCE 3.7%, six-month annualized 4.1%) with a hawkish Fed chair, which supports real-asset trends. Precious metals had strong prior-window active returns (+9% to +14%) and pulled back sharply last week with no fundamental change, making them the best-tested overreaction candidates ahead of a payrolls week that could pressure the dollar. | Strong August payrolls could lift the dollar and real yields, extending the metals pullback; High-volatility candidates (silver 39%, EZA 30%) can produce large adverse excess returns in a week; Hawkish Fed communication ahead of the Sep 15-16 FOMC may pressure non-yielding assets; South Africa carries idiosyncratic currency and power-supply risk uncorrelated to the metals thesis |
| xai-grok-4-5 | xai | portfolio | HEALTHCARE | 3 | 0.59 | Low cross-sectional dispersion with mixed short-term signals: sticky inflation and hawkish Fed tone support limited risk appetite, while quality pullbacks in metals and select defensives offer modest reversal potential versus strong short-term software/cyber momentum that lacks fresh catalysts inside the one-week window. | Hawkish Fed speech and elevated PCE could pressure risk assets and precious metals if real yields rise further; Low dispersion and Labor Day shortened week may mute reversal magnitude; High-beta metals and robotics remain vulnerable to any equity risk-off move; Employment report on Sept 4 could reverse defensive or commodity bounces |
| anthropic-claude-opus-5 | anthropic | portfolio | GOLD | 3 | 0.5633 | SPY is near highs with modest gains while breadth narrowed (RSP -0.44% vs SPY +0.47% over 5 sessions, positive asset share 40.6%). Rates rose sharply at the long end (2y 4.20%->4.34%, 30y ~5.22%) with Warsh signaling firm 2% target and inflation too high, which pressured precious metals and rate-sensitive defensives. Gold and silver saw a sharp one-week pullback after a strong prior 16-session run, a classic real-rate-driven overreaction that often partially mean-reverts into a heavy macro week (Sept 4 payrolls, pre-FOMC positioning). Crypto is drifting lower with elevated volume z-scores, and software/cybersecurity have parabolic recent moves with very high volatility and no in-window catalyst. | A strong August employment report on September 4 could push yields higher and extend the gold and silver selloff rather than reverse it; Pre-FOMC hawkish positioning after Warsh's inflation remarks keeps real yields elevated, a direct headwind to precious metals; Silver's 38.7% volatility means a modest adverse move produces large negative excess return; Healthcare's low beta underperforms if the S&P 500 continues grinding to new highs; Shortened week around the September 7 Labor Day holiday reduces liquidity and can amplify momentum rather than mean reversion |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 133.6999969482422 | 146.02999877929688 | 0.09222140697451064 | 1 |
| BRAZIL | Brazil Equities | 36.029998779296875 | 38.61000061035156 | 0.07160704741786383 | 2 |
| SOUTH_KOREA | South Korea Equities | 180.86000061035156 | 189.91000366210938 | 0.05003872067464665 | 3 |
| YEN | Japanese Yen | 57.38999938964844 | 59.560001373291016 | 0.03781150037847869 | 4 |
| BROAD_COMMODITIES | Broad Commodities | 18.649999618530273 | 19.299999237060547 | 0.0348525271756277 | 5 |
| SOLAR | Solar Energy | 47.56999969482422 | 49.130001068115234 | 0.032793806670146974 | 6 |
| TAIWAN | Taiwan Equities | 108.02999877929688 | 111.54000091552734 | 0.032490994870798096 | 7 |
| SEMICONDUCTORS | Semiconductors | 556.6300048828125 | 573.72998046875 | 0.03072054225595977 | 8 |
| UTILITIES | Utilities Sector | 42.22999954223633 | 43.45000076293945 | 0.028889444326963387 | 9 |
| MOMENTUM | US Momentum Equities | 300.3599853515625 | 308.69000244140625 | 0.02773344485316076 | 10 |
| JAPAN | Japan Equities | 95.87999725341797 | 97.95999908447266 | 0.021693803615336904 | 11 |
| METALS_MINING | Metals and Mining | 118.12999725341797 | 119.94999694824219 | 0.015406753044443722 | 12 |
| COPPER | Copper | 40.0 | 40.56999969482422 | 0.014249992370605424 | 13 |
| ENERGY | Energy Sector | 63.959999084472656 | 64.7699966430664 | 0.012664127113635182 | 14 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.5 | 124.05000305175781 | 0.012653086136798386 | 15 |
| EMERGING_MARKETS | Emerging Markets | 60.52000045776367 | 61.22999954223633 | 0.011731643739298248 | 16 |
| SOUTH_AFRICA | South Africa Equities | 70.5 | 71.30000305175781 | 0.01134756101784129 | 17 |
| REGIONAL_BANKS | Regional Banks | 73.55999755859375 | 74.30999755859375 | 0.010195758902827423 | 18 |
| TECHNOLOGY | Technology Sector | 186.5 | 187.8699951171875 | 0.007345818322721076 | 19 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.91999816894531 | 73.44999694824219 | 0.007268222608411756 | 20 |
| SMALL_VALUE | US Small-Cap Value | 221.8000030517578 | 222.75999450683594 | 0.0043281850399889965 | 21 |
| LARGE_GROWTH | US Large-Cap Growth | 122.70999908447266 | 123.0199966430664 | 0.0025262615997605486 | 22 |
| SMALL_CAP | US Small-Cap Stocks | 293.92999267578125 | 294.6700134277344 | 0.002517676897197063 | 23 |
| NASDAQ100 | Nasdaq 100 | 716.760009765625 | 718.3599853515625 | 0.00223223333352629 | 24 |
| TIPS | Treasury Inflation-Protected Securities | 106.81999969482422 | 107.05000305175781 | 0.0021531862721464456 | 25 |
| CANADA | Canada Equities | 61.43000030517578 | 61.4900016784668 | 0.0009767438221217617 | 26 |
| COMMUNICATIONS | Communication Services Sector | 111.45999908447266 | 111.5199966430664 | 0.0005382878080617548 | 27 |
| BROAD_AI_TECH | Broad AI Technology | 64.30000305175781 | 64.31999969482422 | 0.00031098976854337934 | 28 |
| MID_CAP | US Mid-Cap Stocks | 75.3499984741211 | 75.36000061035156 | 0.0001327423547845541 | 29 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 30 |
| ETHEREUM_ETF | Ethereum ETF | 18.719999313354492 | 18.719999313354492 | 0.0 | 30 |
| EURO | Euro | 107.25 | 107.2300033569336 | -0.00018644888640007018 | 32 |
| UNITED_KINGDOM | United Kingdom Equities | 48.369998931884766 | 48.349998474121094 | -0.00041348890232217883 | 33 |
| MEXICO | Mexico Equities | 76.72000122070312 | 76.66999816894531 | -0.0006517603097263569 | 34 |
| AUSTRALIA | Australia Equities | 30.020000457763672 | 30.0 | -0.000666237756785204 | 35 |
| SP500 | S&P 500 | 767.0499877929688 | 765.9600219726562 | -0.0014209840788195205 | 36 |
| TOTAL_US_MARKET | Total US Stock Market | 378.1499938964844 | 377.6000061035156 | -0.0014544170351601382 | 37 |
| LOW_VOL | US Low Volatility Equities | 74.69000244140625 | 74.55000305175781 | -0.0018744060124815665 | 38 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.66000366210938 | 91.45999908447266 | -0.002182026725353503 | 39 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.54999923706055 | 47.38999938964844 | -0.0033648759196489575 | 40 |
| BIOTECH | Biotechnology | 162.5 | 161.92999267578125 | -0.003507737379807696 | 41 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.5199966430664 | 82.19999694824219 | -0.0038778442540218228 | 42 |
| INDUSTRIALS | Industrials Sector | 175.1300048828125 | 174.4199981689453 | -0.0040541694402526085 | 43 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.7699966430664 | 94.36000061035156 | -0.0043262218765187654 | 44 |
| US_DOLLAR | US Dollar | 28.1200008392334 | 27.989999771118164 | -0.004623081942937035 | 45 |
| REAL_ESTATE | Real Estate Sector | 44.11000061035156 | 43.900001525878906 | -0.0047608043882768625 | 46 |
| EUROPE | Europe Equities | 91.66000366210938 | 91.19000244140625 | -0.005127658759819798 | 47 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.41000366210938 | 96.9000015258789 | -0.005235623827708036 | 48 |
| LARGE_VALUE | US Large-Cap Value | 256.9100036621094 | 255.52999877929688 | -0.005371549815660348 | 49 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.0999984741211 | 92.52999877929688 | -0.006122445802001386 | 50 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.73999786376953 | 92.16000366210938 | -0.006253981184171864 | 51 |
| BITCOIN_ETF | Bitcoin ETF | 44.66999816894531 | 44.38999938964844 | -0.006268161870925049 | 52 |
| AGRICULTURE | Agriculture Commodities | 29.31999969482422 | 29.1299991607666 | -0.006480236563275232 | 53 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.20999908447266 | 105.4800033569336 | -0.00687313561652958 | 54 |
| FINANCIALS | Financials Sector | 57.709999084472656 | 57.29999923706055 | -0.00710448542568809 | 55 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.80999755859375 | 79.12000274658203 | -0.00864546840143865 | 56 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.0999984741211 | 104.0199966430664 | -0.010275945259129782 | 57 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.9800033569336 | 84.0199966430664 | -0.011296854270939072 | 58 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 219.38999938964844 | 216.72999572753906 | -0.012124543823827882 | 59 |
| INDIA | India Equities | 49.70000076293945 | 49.09000015258789 | -0.012273653943410623 | 60 |
| SILVER | Silver | 60.130001068115234 | 59.369998931884766 | -0.012639316858975902 | 61 |
| DIVIDEND | US Dividend Equities | 34.88999938964844 | 34.40999984741211 | -0.01375751076621512 | 62 |
| CHINA | China Equities | 54.720001220703125 | 53.95000076293945 | -0.014071645478552108 | 63 |
| MATERIALS | Materials Sector | 52.689998626708984 | 51.939998626708984 | -0.014234200408952402 | 64 |
| HEALTHCARE | Healthcare Sector | 170.5399932861328 | 167.1300048828125 | -0.01999524180582679 | 65 |
| GOLD | Gold | 83.70999908447266 | 81.94999694824219 | -0.021024992897854755 | 66 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 228.35000610351562 | 223.52999877929688 | -0.021107979835278567 | 67 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.58999633789062 | 113.98999786376953 | -0.02230035642668704 | 68 |
| CYBERSECURITY | Cybersecurity | 100.1500015258789 | 94.01000213623047 | -0.06130803091462611 | 69 |
| SOFTWARE | Software | 109.9800033569336 | 102.66000366210938 | -0.06655755111288364 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SILVER | 35.0 | -0.012639316858975902 | -0.004423760900641565 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | GOLD | 35.0 | -0.021024992897854755 | -0.007358747514249164 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | SOUTH_AFRICA | 30.0 | 0.01134756101784129 | 0.003404268305352387 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | GOLD | 35.0 | -0.021024992897854755 | -0.007358747514249164 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SILVER | 35.0 | -0.012639316858975902 | -0.004423760900641565 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | HEALTHCARE | 30.0 | -0.01999524180582679 | -0.005998572541748037 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SILVER | 35.0 | -0.012639316858975902 | -0.004423760900641565 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | OIL | 35.0 | 0.09222140697451064 | 0.03227749244107873 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | GOLD | 30.0 | -0.021024992897854755 | -0.006307497869356427 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SILVER | 35.0 | -0.012639316858975902 | -0.004423760900641565 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SOUTH_AFRICA | 35.0 | 0.01134756101784129 | 0.003971646356244451 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | HEALTHCARE | 30.0 | -0.01999524180582679 | -0.005998572541748037 | V3 selected model rank 3: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 100.0 | -0.0014209840788195205 | -0.0014209840788195205 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | HEALTHCARE | 35.0 | -0.01999524180582679 | -0.006998334632039377 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | SILVER | 35.0 | -0.012639316858975902 | -0.004423760900641565 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | GOLD | 30.0 | -0.021024992897854755 | -0.006307497869356427 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 100.0 | -0.0014209840788195205 | -0.0014209840788195205 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | SILVER | 3 | 0.5767 | -0.012639316858975902 | 0.021546233671080734 | 0.022967217749900255 | 0.07067517330342991 |  | True | True |
| xai-grok-4-3 | SP500 | 1 | 0.5 | -0.0014209840788195205 | -0.0014209840788195205 | 0.0 | 0.09364239105333017 |  | False | False |
| xai-grok-4-6 | SP500 | 1 | 0.5 | -0.0014209840788195205 | -0.0014209840788195205 | 0.0 | 0.09364239105333017 |  | False | False |
| openai-gpt-5-6-sol | SILVER | 3 | 0.57 | -0.012639316858975902 | -0.006450687086145151 | -0.0050297030073256305 | 0.0986720940606558 |  | False | False |
| anthropic-claude-fable-5 | SILVER | 3 | 0.58 | -0.012639316858975902 | -0.008378240109538342 | -0.006957256030718822 | 0.10059964708404899 |  | False | False |
| xai-grok-4-5 | HEALTHCARE | 3 | 0.59 | -0.01999524180582679 | -0.017729593402037367 | -0.016308609323217847 | 0.10995100037654801 |  | False | False |
| anthropic-claude-opus-5 | GOLD | 3 | 0.5633 | -0.021024992897854755 | -0.017781080956638766 | -0.016360096877819245 | 0.11000248793114942 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | dc33b9403b6139387955eaac68b60988e308f37d5cc50d4c22b7397585fae895 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | 0852fc640e41a176cb82b7d7423143fe6b1f0d40d55266663f935537d87b5336 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | b46bf5e626a3e067474e02203a49a71703a9f81552f101b217094a8e61846088 |
| market_data/universe_decision_context.md | c6c3d318b0a05e2cb7fd6f4e637b9042c861dec3fa3c5aa23f6779cc52d80212 |
| market_data/universe_decision_context.json | a343087fcdd632b7f54adb1293e81d73b1f749dd0a1167ebdb88b8a4f209965e |
| market_data/decision_context_source_history.json | 86cc16cb273acf308a16da73194aed51d7343c1c34c5c97ef95374ee69086a2a |
| market_data/universe_quality_evidence.md | e834db9c2028431a1882f2f84cadd795b2a7f36e78d4df4aa3bff004fb3dabc6 |
| market_data/universe_quality_evidence.json | 25a75862667b5a07f2b1f29343cf866683b3f2538b7b78b6a2cef1f6c781b87e |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 07e6b24724d3e7905fd27951e43e4fd8f8a2e92fe48a2a704feb88a75c71131c | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | c8ab34b6742bbfb0fadabe88c61187acab248acec84760a88a4e42a5717f81b3 | yes |
| Final briefing | research/final_briefing.md | model-facing | dc33b9403b6139387955eaac68b60988e308f37d5cc50d4c22b7397585fae895 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
