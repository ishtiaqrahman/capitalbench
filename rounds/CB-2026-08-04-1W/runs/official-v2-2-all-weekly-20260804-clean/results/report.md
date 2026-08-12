# CapitalBench Report: CB-2026-08-04-1W / official-v2-2-all-weekly-20260804-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-weekly-20260804-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-04-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-08-04
- Decision deadline: 2026-08-05T12:30:00Z
- Horizon: one week
- Entry date: 2026-08-04
- Exit date: 2026-08-11
- Entry rule: Use the Tuesday, August 4, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Tuesday, August 11, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | openai | portfolio | SOFTWARE | 5 | 0.55 | SPY is near record highs after a strong 5-day move, so the active portfolio favors selected areas with stronger near-term continuation or reversal catalysts. The main expected edge is from software/cybersecurity momentum plus oil geopolitical rebound potential. | A broad equity reversal after record S&P 500 and Dow closes could hit software, cybersecurity, and crypto simultaneously.; Technology-and-growth strength may prove to be a short-covering bounce given weak quality evidence and high volatility in several growth themes.; Hormuz negotiations could de-escalate quickly, removing oil's rebound catalyst after the sharp crude selloff.; The July Employment Situation could strengthen rate-hike concerns and pressure risk assets while also weakening yen exposure. |
| xai-grok-4-5 | xai | portfolio | SOFTWARE | 5 | 0.58 | Selected higher-base active holdings in software, cybersecurity, copper and financials capped by cluster rules, paired with SPY. Focused on momentum continuation and near-term catalysts inside the August 4-11 window. | Post-record profit-taking after 4%+ SPY 5-session gain; July employment miss or hot inflation print triggering rate-hike fears; Geopolitical flare-up in Strait of Hormuz reversing oil and risk assets; Tech concentration reversal given elevated recent returns and volatility |
| openai-gpt-5-6-sol | openai | portfolio | DIVIDEND | 4 | 0.57 | Dividend and real estate combine strong quality scores with recent underperformance, while energy and Ethereum retain strong prior trends after sharp pullbacks. Each selected candidate has a base forecast above SPY's. | The August 7 employment report could lift Treasury yields and pressure real estate and dividend equities.; Final Iran-Oman shipping progress could extend the oil and energy reversal.; The record-setting equity rally could remain concentrated in technology, leaving selected laggards behind.; Ethereum's 40.22% annualized 21-session volatility creates substantial one-week downside risk. |
| anthropic-claude-fable-5 | anthropic | portfolio | SP500 | 5 | 0.55 | Barbell of continuing tech strength and mean-reverting defensives around a SPY core, with gold as a geopolitical hedge into an event-heavy week (ISM services, payrolls, refunding). | Hot July payrolls or hawkish refunding pushes yields up, hurting growth and gold simultaneously; Tech momentum reverses after a 4%+ SPY week, dragging the QQQ overweight; Hormuz resolution triggers a cyclical rally that leaves healthcare and low-vol lagging; Elevated inflation prints keep Fed hawkish, capping equity upside broadly |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 4 | 0.44 | Barbell of SPY core plus mean-reversion defensives/financials rather than chasing semis and software that already ran 7-9% in three sessions with 30-50% volatility. | Momentum/tech continuation extends SPY gains while low-beta laggards stay flat; Hot July payrolls Aug 7 hits rate-sensitive and broad equities; Healthcare single-name event risk from Lilly results; Defensive names continue de-rating in a risk-on tape |
| google-gemini-3-1-pro | google | portfolio | SP500 | 2 | 0.6 | The portfolio balances SP500 momentum with the safety of short-term Treasuries. | Market correction from record highs.; Unexpected inflation data impacting rate expectations.; Geopolitical escalation affecting energy prices and global growth. |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.55 | SP500 selected as benchmark proxy after testing continuation versus reversal across finalists; no cluster allocation exceeds cap. | July employment data surprise on August 7; Inflation reacceleration in upcoming CPI; Geopolitical escalation in Strait of Hormuz |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 3 | 0.53 | Core SPY plus growth/tech tilt to capture continued mega-cap leadership over a one-week window with heavy macro data flow. | Strong July jobs report Aug 7 could lift yields and hit high-beta growth; Tech is extended with high volatility and could mean-revert; Geopolitical oil/Hormuz headlines could spike risk-off |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 115.78 | 127.61000061035156 | 0.10217654698869882 | 1 |
| METALS_MINING | Metals and Mining | 107.86 | 117.83000183105469 | 0.09243465446926291 | 2 |
| SILVER | Silver | 53.84 | 58.54999923706055 | 0.08748141227824191 | 3 |
| GOLD | Gold | 76.69 | 82.18000030517578 | 0.07158691231158931 | 4 |
| BROAD_COMMODITIES | Broad Commodities | 16.9 | 17.90999984741211 | 0.05976330458059831 | 5 |
| ENERGY | Energy Sector | 58.52 | 60.93 | 0.04118250170881743 | 6 |
| BIOTECH | Biotechnology | 151.88 | 158.07000732421875 | 0.040755908113107475 | 7 |
| SOUTH_AFRICA | South Africa Equities | 65.96 | 68.58999633789062 | 0.03987259457081005 | 8 |
| HEALTHCARE | Healthcare Sector | 162.1 | 168.01 | 0.03645897594077718 | 9 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 124.83 | 128.3000030517578 | 0.027797829462131052 | 10 |
| CANADA | Canada Equities | 60.0 | 61.5099983215332 | 0.025166638692220022 | 11 |
| MATERIALS | Materials Sector | 52.0 | 53.24 | 0.02384615384615385 | 12 |
| CYBERSECURITY | Cybersecurity | 97.94 | 99.91999816894531 | 0.020216440360887322 | 13 |
| SOFTWARE | Software | 102.0 | 103.91999816894531 | 0.018823511460248188 | 14 |
| JAPAN | Japan Equities | 94.61 | 96.27999877929688 | 0.01765139815343919 | 15 |
| TAIWAN | Taiwan Equities | 102.21 | 103.94000244140625 | 0.016925960682969032 | 16 |
| DIVIDEND | US Dividend Equities | 33.85 | 34.27 | 0.012407680945347277 | 17 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.29 | 119.24 | 0.008031109983937634 | 18 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.22 | 72.69000244140625 | 0.00650792635566666 | 19 |
| LARGE_VALUE | US Large-Cap Value | 256.63 | 257.92 | 0.005026692124849186 | 20 |
| EUROPE | Europe Equities | 91.84 | 92.30000305175781 | 0.00500874403046403 | 21 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 250.65 | 251.89999389648438 | 0.00498700936159735 | 22 |
| MID_CAP | US Mid-Cap Stocks | 77.48 | 77.77 | 0.0037429013939080935 | 23 |
| ETHEREUM_ETF | Ethereum ETF | 14.15 | 14.180000305175781 | 0.002120162909949208 | 24 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.23 | 220.69000244140625 | 0.0020887365091324384 | 25 |
| COPPER | Copper | 40.14 | 40.220001220703125 | 0.001993054825688123 | 26 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.76 | 105.93000030517578 | 0.0016074158961401075 | 27 |
| EURO | Euro | 106.37 | 106.5199966430664 | 0.0014101404819630847 | 28 |
| EMERGING_MARKETS | Emerging Markets | 60.05 | 60.119998931884766 | 0.0011656774668571401 | 29 |
| BROAD_AI_TECH | Broad AI Technology | 63.13 | 63.20000076293945 | 0.001108835148732057 | 30 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.42 | 91.49 | 0.0007656967840734552 | 31 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 32 |
| TOTAL_US_MARKET | Total US Stock Market | 380.82 | 380.65 | -0.00044640512578120184 | 33 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.55 | 79.51000213623047 | -0.000502801555870902 | 34 |
| US_DOLLAR | US Dollar | 28.16 | 28.139999389648438 | -0.0007102489471435547 | 35 |
| UNITED_KINGDOM | United Kingdom Equities | 48.34 | 48.29999923706055 | -0.0008274878555948328 | 36 |
| SP500 | S&P 500 | 771.33 | 770.56 | -0.0009982757055995162 | 37 |
| FINANCIALS | Financials Sector | 57.88 | 57.8 | -0.0013821700069109877 | 38 |
| TIPS | Treasury Inflation-Protected Securities | 107.05 | 106.88999938964844 | -0.0014946343797436201 | 39 |
| SMALL_CAP | US Small-Cap Stocks | 301.71 | 300.99 | -0.002386397534055784 | 40 |
| AGRICULTURE | Agriculture Commodities | 27.66 | 27.59000015258789 | -0.002530724779902682 | 41 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.295 | 93.02999877929688 | -0.002840465412971005 | 42 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.97 | 47.81999969482422 | -0.0031269607082714534 | 43 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.66 | 97.31999969482422 | -0.00348146943657357 | 44 |
| INDUSTRIALS | Industrials Sector | 186.4 | 185.7 | -0.003755364806867001 | 45 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.25 | 92.87 | -0.004075067024128631 | 46 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.22 | 94.83000183105469 | -0.004095758968129748 | 47 |
| TECHNOLOGY | Technology Sector | 186.9 | 186.09 | -0.004333868378812222 | 48 |
| SEMICONDUCTORS | Semiconductors | 575.71 | 572.9299926757812 | -0.004828832787720838 | 49 |
| LARGE_GROWTH | US Large-Cap Growth | 124.3 | 123.6 | -0.005631536604987941 | 50 |
| AUSTRALIA | Australia Equities | 30.12 | 29.950000762939453 | -0.005644064975449781 | 51 |
| COMMUNICATIONS | Communication Services Sector | 112.04 | 111.27 | -0.006872545519457374 | 52 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.76 | 105.98999786376953 | -0.007212459125425896 | 53 |
| NASDAQ100 | Nasdaq 100 | 723.85 | 718.45 | -0.007460109138633708 | 54 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.82 | 82.19000244140625 | -0.007606828768337848 | 55 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.37 | 84.69 | -0.007965327398383626 | 56 |
| CHINA | China Equities | 56.09 | 55.619998931884766 | -0.008379409308526209 | 57 |
| INDIA | India Equities | 50.53 | 50.09000015258789 | -0.008707695377243474 | 58 |
| SMALL_VALUE | US Small-Cap Value | 226.97 | 224.97 | -0.008811737233995642 | 59 |
| YEN | Japanese Yen | 58.15 | 57.630001068115234 | -0.008942372001457644 | 60 |
| LOW_VOL | US Low Volatility Equities | 76.39 | 75.65 | -0.009687131823537087 | 61 |
| MEXICO | Mexico Equities | 77.06 | 76.23999786376953 | -0.010641086636782648 | 62 |
| UTILITIES | Utilities Sector | 44.11 | 43.63 | -0.01088188619360686 | 63 |
| BITCOIN_ETF | Bitcoin ETF | 36.39 | 35.939998626708984 | -0.01236607236303977 | 64 |
| SOLAR | Solar Energy | 53.37 | 52.70000076293945 | -0.012553854919628016 | 65 |
| REGIONAL_BANKS | Regional Banks | 77.84 | 76.80999755859375 | -0.013232302690213915 | 66 |
| MOMENTUM | US Momentum Equities | 313.35 | 308.34 | -0.015988511249401816 | 67 |
| SOUTH_KOREA | South Korea Equities | 171.14 | 167.24000549316406 | -0.022788328309196748 | 68 |
| REAL_ESTATE | Real Estate Sector | 45.17 | 44.08 | -0.02413106043834412 | 69 |
| BRAZIL | Brazil Equities | 36.09 | 33.97999954223633 | -0.05846496142321067 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SP500 | 40.0 | -0.0009982757055995162 | -0.0003993102822398065 | Record close with strong breadth (79.7% positive assets 5s) and firm ISM manufacturing; core diversified anchor. |
| anthropic-claude-fable-5 | NASDAQ100 | 25.0 | -0.007460109138633708 | -0.001865027284658427 | Strong 5-day recovery (+3.05% active) after prior pullback; earnings momentum and easing oil supports growth beta. |
| anthropic-claude-fable-5 | HEALTHCARE | 15.0 | 0.03645897594077718 | 0.005468846391116577 | Deep recent relative pullback with top-tier quality evidence score (0.80) and Eli Lilly Q2 catalyst Aug 5; defensive ballast. |
| anthropic-claude-fable-5 | LOW_VOL | 10.0 | -0.009687131823537087 | -0.0009687131823537088 | Highest recent-pullback rank (0.94) with solid prior trend; mean-reversion candidate with low downside. |
| anthropic-claude-fable-5 | GOLD | 10.0 | 0.07158691231158931 | 0.007158691231158931 | Hedge against Hormuz escalation and refunding/CPI rate volatility; recent modest gain despite soft dollar backdrop. |
| anthropic-claude-opus-4-8 | SP500 | 50.0 | -0.0009982757055995162 | -0.0004991378527997581 | Broad large-cap momentum with record close and strong breadth; core anchor. |
| anthropic-claude-opus-4-8 | TECHNOLOGY | 30.0 | -0.004333868378812222 | -0.0013001605136436667 | Strong recent tech leadership with 5s active +5.13% and 3s +6.36%, supported by growth-stock resilience. |
| anthropic-claude-opus-4-8 | NASDAQ100 | 20.0 | -0.007460109138633708 | -0.0014920218277267418 | Large-cap growth momentum continuation with 5s active +3.05% and record Nasdaq close. |
| anthropic-claude-opus-5 | SP500 | 45.0 | -0.0009982757055995162 | -0.00044922406751978227 | Core benchmark exposure at record highs with broad participation. |
| anthropic-claude-opus-5 | HEALTHCARE | 20.0 | 0.03645897594077718 | 0.007291795188155437 | Deep relative pullback (-7.2% 5s active) with strong prior trend and low beta; mean-reversion candidate with Lilly Q2 catalyst. |
| anthropic-claude-opus-5 | FINANCIALS | 20.0 | -0.0013821700069109877 | -0.00027643400138219757 | High quality-evidence score, prior positive active trend, at 52w high, steep curve supportive. |
| anthropic-claude-opus-5 | CONSUMER_STAPLES | 15.0 | -0.007965327398383626 | -0.0011947991097575438 | Largest recent relative pullback among defensives with strong prior trend; hedges tech-led drawdown risk. |
| google-gemini-3-1-pro | SP500 | 50.0 | -0.0009982757055995162 | -0.0004991378527997581 | Core holding to capture broad market momentum and record highs. |
| google-gemini-3-1-pro | SHORT_TREASURY | 50.0 | 0.0007656967840734552 | 0.0003828483920367276 | Defensive allocation to balance equity risk and capture yield. |
| openai-gpt-5-5 | SOFTWARE | 25.0 | 0.018823511460248188 | 0.004705877865062047 | Strongest short-term relative price action in the universe among assessed finalists, with a plausible risk-on continuation case into the one-week window despite weak quality evidence. |
| openai-gpt-5-5 | CYBERSECURITY | 25.0 | 0.020216440360887322 | 0.0050541100902218306 | Cybersecurity combines strong 3-day and 5-day active momentum with a 52-week high, offering a cleaner continuation setup than many higher-volatility technology themes. |
| openai-gpt-5-5 | OIL | 20.0 | 0.10217654698869882 | 0.020435309397739767 | Crude exposure has a near-term rebound/geopolitical-risk premium setup after a sharp drop, with Hormuz shipping risks unresolved inside the scoring window. |
| openai-gpt-5-5 | ETHEREUM_ETF | 15.0 | 0.002120162909949208 | 0.0003180244364923812 | Ethereum has strong prior active performance and high quality evidence after a recent pullback, providing convex upside if risk appetite persists. |
| openai-gpt-5-5 | YEN | 15.0 | -0.008942372001457644 | -0.0013413558002186466 | Yen provides a diversifying risk-off component with unusually high volume activity and a small positive short-term price move, while still clearing the SPY base forecast. |
| openai-gpt-5-6-sol | DIVIDEND | 30.0 | 0.012407680945347277 | 0.0037223042836041827 | Strong prior relative trend, deep recent relative pullback, and the universe's highest quality score support a short-term rebound. |
| openai-gpt-5-6-sol | REAL_ESTATE | 20.0 | -0.02413106043834412 | -0.004826212087668824 | High quality evidence and a sizable pullback create a favorable rebound setup if yields stabilize. |
| openai-gpt-5-6-sol | ENERGY | 25.0 | 0.04118250170881743 | 0.010295625427204358 | Strong prior relative trend and unresolved Hormuz risk offer rebound potential after the oil-led selloff. |
| openai-gpt-5-6-sol | ETHEREUM_ETF | 25.0 | 0.002120162909949208 | 0.000530040727487302 | Top-tier prior trend and pullback ranks support a tactical rebound, though volatility keeps the position capped. |
| xai-grok-4-3 | SP500 | 100.0 | -0.0009982757055995162 | -0.0009982757055995162 | No active holding clears the base-forecast hurdle above SP500; market data shows record closes but mixed macro releases with no clear one-week catalyst for outperformance. |
| xai-grok-4-5 | SOFTWARE | 30.0 | 0.018823511460248188 | 0.005647053438074456 | Strong recent rebound and high beta to continued risk-on after record closes supports outperformance vs SPY over one week. |
| xai-grok-4-5 | CYBERSECURITY | 20.0 | 0.020216440360887322 | 0.0040432880721774644 | Positive 3-session momentum and lower relative drawdown than pure semis support continuation above SPY base. |
| xai-grok-4-5 | COPPER | 20.0 | 0.001993054825688123 | 0.00039861096513762464 | Positive active return and industrial demand proxy with base case above SPY amid manufacturing PMI strength. |
| xai-grok-4-5 | FINANCIALS | 15.0 | -0.0013821700069109877 | -0.00020732550103664814 | Solid prior active trend and quality score with rates backdrop supporting modest outperformance. |
| xai-grok-4-5 | SP500 | 15.0 | -0.0009982757055995162 | -0.00014974135583992743 | Core benchmark holding to anchor after record close while active sleeves seek alpha. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | SOFTWARE | 5 | 0.55 | 0.018823511460248188 | 0.029171965989297378 | 0.030170241694896894 | 0.07300458099940145 |  | True | True |
| xai-grok-4-5 | SOFTWARE | 5 | 0.58 | 0.018823511460248188 | 0.009731885618512971 | 0.010730161324112487 | 0.09244466137018585 |  | True | True |
| openai-gpt-5-6-sol | DIVIDEND | 4 | 0.57 | 0.012407680945347277 | 0.009721758350627017 | 0.010720034056226534 | 0.0924547886380718 |  | True | True |
| anthropic-claude-fable-5 | SP500 | 5 | 0.55 | -0.0009982757055995162 | 0.009394486873023565 | 0.010392762578623082 | 0.09278206011567526 |  | True | True |
| anthropic-claude-opus-5 | SP500 | 4 | 0.44 | -0.0009982757055995162 | 0.005371338009495913 | 0.00636961371509543 | 0.09680520897920292 |  | True | True |
| google-gemini-3-1-pro | SP500 | 2 | 0.6 | -0.0009982757055995162 | -0.00011628946076303048 | 0.0008819862448364857 | 0.10229283644946185 |  | True | False |
| xai-grok-4-3 | SP500 | 1 | 0.55 | -0.0009982757055995162 | -0.0009982757055995162 | 0.0 | 0.10317482269429834 |  | False | False |
| anthropic-claude-opus-4-8 | SP500 | 3 | 0.53 | -0.0009982757055995162 | -0.0032913201941701664 | -0.0022930444885706502 | 0.10546786718286899 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 8867d2beab94d6e43833c054c911d08bbab8cceafee0184e7c5b94953efd25bc |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 1a844da9c59ab06e30e88b53a60f08b23075e0cfd4df40bd80afc8570a93c261 |
| manifest.yaml | 7472dd996e1d766fec750eaf0f2aac5c60b3d1d3526aed27f669bde2ba04470f |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | da9dbd052d4380022786951d1cbf96911133205c9d4081501d58d3f96498212d |
| market_data/universe_decision_context.md | 2b59c57cb801896c27221a85251900a3b3de0278a23a6e3e285d693bf026893e |
| market_data/universe_decision_context.json | 589243aec1d507067442ce29a2cf3a7b49b6febbd915be43a68f89a810e85f12 |
| market_data/decision_context_source_history.json | fd01b404826ed74b028c769f0b2af7b495428d20978cd8dea424740b33e259da |
| market_data/universe_quality_evidence.md | 6022171c342b89d4cf29558744059a2103ded8325d5ac74814b5ebb6adbfce23 |
| market_data/universe_quality_evidence.json | 900028b12d5108af3026ba0cdcb145f564cc0d8575a6b671aefe3fe5cc90bf42 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | e9288f14cea5acfdee6d969ab4b469a710fa7c4b6f260b55988bf7169a17ca51 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 191f38bebe6dd1623e871a317f42bcb3491ba0865c486a6a0ec2d8ba493b1902 | yes |
| Final briefing | research/final_briefing.md | model-facing | 8867d2beab94d6e43833c054c911d08bbab8cceafee0184e7c5b94953efd25bc | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
