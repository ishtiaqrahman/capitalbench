# CapitalBench Report: CB-2026-08-07-1M / official-v2-2-all-monthly-20260807

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-monthly-20260807
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-07-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-08-07
- Decision deadline: 2026-08-07T13:25:00Z
- Horizon: one month
- Entry date: 2026-08-07
- Exit date: 2026-09-08
- Entry rule: Use the Friday, August 7, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Tuesday, September 8, 2026 adjusted close supplied in prices/exit_prices.csv; Monday, September 7 is the U.S. Labor Day market holiday.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | SEMICONDUCTORS | 4 | 0.58 | SPY base set modestly positive on solid GDP final sales, strong ISM, and earnings; selected higher-beta quality leaders in semis, biotech, Taiwan, and cyber for alpha. Caps and hurdle rules enforced; no pure momentum or low-quality laggards. | Elevated PCE and ISM prices indices could trigger hawkish Fed minutes or Jackson Hole surprise; Middle East/oil spike renewing inflation and risk-off; High vol and distance-to-high in selected tech names amplify drawdown risk; July employment or CPI miss shifting rate path |
| xai-grok-4-3 | xai | portfolio | SEMICONDUCTORS | 2 | 0.62 | Selects SEMICONDUCTORS and BIOTECH for superior base-case expected returns driven by quality evidence metrics. | Technology and biotech sector volatility spikes on inflation data; Labor Day holiday liquidity reduction near exit; Potential reversal in recent momentum names within semiconductors |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.65 | A balanced approach favoring broad market beta, technology, and healthcare. | Inflation surprises leading to higher interest rates.; Geopolitical tensions impacting global supply chains.; A slowdown in economic growth. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 3 | 0.55 | Overweight quality US equity with SOFTWARE and FINANCIALS tilts that clear the SPY hurdle on recent relative strength and shallow drawdowns. | Hotter July CPI on Aug 12 triggering equity/rate shock; AI/tech growth rotation reversing SOFTWARE gains; Financials hit by yield-curve flattening or credit stress |
| anthropic-claude-fable-5 | anthropic | portfolio | SEMICONDUCTORS | 4 | 0.55 | Barbell of high-quality-evidence pullback candidates (SMH, MTUM, XLU) over a 20% SPY core, targeting ~0.8% alpha over the one-month window. | Hot July CPI (Aug 12) or hawkish Jackson Hole lifting yields, hurting both growth and utilities; Semiconductor momentum reversal given 55% annualized volatility and 2.4 beta; Momentum factor crowding unwind extending the recent -5.2% active drawdown; Middle East/Strait of Hormuz escalation lifting oil and inflation expectations |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 5 | 0.53 | Mildly constructive one-month view on US equities with diversified, moderate-beta tilts rather than crowded semiconductor/momentum exposure that carries very high volatility and deep drawdowns. | July CPI/PPI surprise on the upside given 5.1% Q2 PCE inflation, pressuring multiples; Hawkish Jackson Hole or FOMC minutes with three voters already favoring a hike; Momentum/growth unwind hitting cybersecurity and high-beta tilts; Middle East escalation spiking oil and hurting cyclicals; Weak July payrolls released hours after entry |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.56 | SPY has supportive earnings and activity data but already strong near-term gains. The selected basket seeks one-month alpha from high-quality relative trend plus identifiable macro and earnings catalysts, while respecting the cluster cap. | A hotter CPI/PPI or hawkish Fed communication could pressure high-beta technology and cyclical exposures.; The unreleased July and August employment reports could trigger a growth scare or rate shock before exit.; Recent winners could reverse sharply because several selected holdings have elevated volatility and drawdowns.; Geopolitical or commodity headlines could move oil, rates, and risk appetite in ways that undermine copper and defense exposure. |
| openai-gpt-5-6-sol | openai | portfolio | CYBERSECURITY | 3 | 0.56 | Relative-strength and pullback evidence favor a diversified active-equity portfolio over SPY, but the edge is modest because inflation, rates, and labor releases can rapidly reverse risk appetite. | Hot CPI or PPI data could lift already-high Treasury yields and pressure growth and biotech valuations.; Weak employment, retail-sales, or GDP revisions could undermine the solid-activity and earnings backdrop.; A broad momentum reversal could disproportionately hurt cybersecurity and biotech.; Middle East de-escalation could remove the near-term support for aerospace-defense exposure. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.47 | 18.719999313354492 | 0.2937110790155142 | 1 |
| OIL | Crude Oil | 117.98 | 146.02999877929688 | 0.23775215103658986 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 36.8 | 44.38999938964844 | 0.20624998341435985 | 3 |
| SOUTH_KOREA | South Korea Equities | 166.09 | 189.91000366210938 | 0.14341624217056648 | 4 |
| ENERGY | Energy Sector | 57.5 | 64.7699966430664 | 0.1264347242272419 | 5 |
| BROAD_COMMODITIES | Broad Commodities | 17.25 | 19.299999237060547 | 0.11884053548177076 | 6 |
| BRAZIL | Brazil Equities | 35.34 | 38.61000061035156 | 0.09252972864605424 | 7 |
| TAIWAN | Taiwan Equities | 103.09 | 111.54000091552734 | 0.08196722199560913 | 8 |
| AGRICULTURE | Agriculture Commodities | 27.62 | 29.1299991607666 | 0.05467049821747283 | 9 |
| METALS_MINING | Metals and Mining | 115.74 | 119.94999694824219 | 0.036374606430293666 | 10 |
| SILVER | Silver | 57.5 | 59.369998931884766 | 0.03252172055451763 | 11 |
| BIOTECH | Biotechnology | 157.37 | 161.92999267578125 | 0.028976251355285365 | 12 |
| SOUTH_AFRICA | South Africa Equities | 69.65 | 71.30000305175781 | 0.023689921776852918 | 13 |
| YEN | Japanese Yen | 58.24 | 59.560001373291016 | 0.022664858744694705 | 14 |
| COPPER | Copper | 39.9 | 40.56999969482422 | 0.01679197230135898 | 15 |
| BROAD_AI_TECH | Broad AI Technology | 63.35 | 64.31999969482422 | 0.015311755245843939 | 16 |
| DIVIDEND | US Dividend Equities | 33.9 | 34.40999984741211 | 0.015044243286493009 | 17 |
| EMERGING_MARKETS | Emerging Markets | 60.47 | 61.22999954223633 | 0.0125682080740257 | 18 |
| JAPAN | Japan Equities | 96.9 | 97.95999908447266 | 0.010939103038933418 | 19 |
| HEALTHCARE | Healthcare Sector | 165.68 | 167.1300048828125 | 0.008751840190804439 | 20 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.89 | 73.44999694824219 | 0.007682767845276217 | 21 |
| EURO | Euro | 106.68 | 107.2300033569336 | 0.005155637016625247 | 22 |
| GOLD | Gold | 81.68 | 81.94999694824219 | 0.0033055453996349016 | 23 |
| CANADA | Canada Equities | 61.3 | 61.4900016784668 | 0.003099537984776468 | 24 |
| COMMUNICATIONS | Communication Services Sector | 111.25 | 111.5199966430664 | 0.0024269361174509285 | 25 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 26 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.48 | 91.45999908447266 | -0.00021863703025082337 | 27 |
| TIPS | Treasury Inflation-Protected Securities | 107.08 | 107.05000305175781 | -0.0002801358633002238 | 28 |
| SOFTWARE | Software | 102.69 | 102.66000366210938 | -0.0002921057346443323 | 29 |
| TECHNOLOGY | Technology Sector | 187.97 | 187.8699951171875 | -0.0005320257637522197 | 30 |
| MOMENTUM | US Momentum Equities | 309.32 | 308.69000244140625 | -0.0020367178281188725 | 31 |
| US_DOLLAR | US Dollar | 28.07 | 27.989999771118164 | -0.002850025966577685 | 32 |
| UTILITIES | Utilities Sector | 43.61 | 43.45000076293945 | -0.0036688657890517895 | 33 |
| FINANCIALS | Financials Sector | 57.6 | 57.29999923706055 | -0.005208346578809975 | 34 |
| UNITED_KINGDOM | United Kingdom Equities | 48.64 | 48.349998474121094 | -0.005962202423497209 | 35 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.61 | 79.12000274658203 | -0.006154971152091071 | 36 |
| NASDAQ100 | Nasdaq 100 | 723.03 | 718.3599853515625 | -0.00645895004140562 | 37 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.76 | 82.19999694824219 | -0.006766590765560854 | 38 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.6 | 96.9000015258789 | -0.007172115513535693 | 39 |
| LARGE_VALUE | US Large-Cap Value | 257.56 | 255.52999877929688 | -0.007881663382136694 | 40 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.27 | 92.52999877929688 | -0.007933968271717773 | 41 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.24 | 94.36000061035156 | -0.009239808795132642 | 42 |
| SP500 | S&P 500 | 773.26 | 765.9600219726562 | -0.009440521981408212 | 43 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.55 | 105.4800033569336 | -0.010042202187389937 | 44 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.17 | 92.16000366210938 | -0.010840359964480295 | 45 |
| TOTAL_US_MARKET | Total US Stock Market | 381.78 | 377.6000061035156 | -0.01094869793201414 | 46 |
| MEXICO | Mexico Equities | 77.52 | 76.66999816894531 | -0.010964935901118245 | 47 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.95 | 47.38999938964844 | -0.01167884484570525 | 48 |
| SMALL_VALUE | US Small-Cap Value | 225.52 | 222.75999450683594 | -0.01223840676287724 | 49 |
| LARGE_GROWTH | US Large-Cap Growth | 124.6 | 123.0199966430664 | -0.012680604790799244 | 50 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.12 | 84.0199966430664 | -0.01292297176848678 | 51 |
| AUSTRALIA | Australia Equities | 30.41 | 30.0 | -0.013482407102926697 | 52 |
| EUROPE | Europe Equities | 92.6 | 91.19000244140625 | -0.015226755492373067 | 53 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 220.09 | 216.72999572753906 | -0.015266501306106295 | 54 |
| SEMICONDUCTORS | Semiconductors | 582.7 | 573.72998046875 | -0.015393889705251462 | 55 |
| MATERIALS | Materials Sector | 52.86 | 51.939998626708984 | -0.01740449060331095 | 56 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.94 | 104.0199966430664 | -0.018123497800014987 | 57 |
| LOW_VOL | US Low Volatility Equities | 76.21 | 74.55000305175781 | -0.021781878339354188 | 58 |
| SMALL_CAP | US Small-Cap Stocks | 301.56 | 294.6700134277344 | -0.022847813278503826 | 59 |
| REAL_ESTATE | Real Estate Sector | 44.98 | 43.900001525878906 | -0.02401063748601806 | 60 |
| REGIONAL_BANKS | Regional Banks | 76.21 | 74.30999755859375 | -0.024931143437950998 | 61 |
| INDIA | India Equities | 50.365 | 49.09000015258789 | -0.0253151960173158 | 62 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 127.85 | 124.05000305175781 | -0.029722306986642022 | 63 |
| MID_CAP | US Mid-Cap Stocks | 77.79 | 75.36000061035156 | -0.03123794047626227 | 64 |
| CYBERSECURITY | Cybersecurity | 97.85 | 94.01000213623047 | -0.039243718587322673 | 65 |
| CHINA | China Equities | 56.57 | 53.95000076293945 | -0.046314287379539465 | 66 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 119.86 | 113.98999786376953 | -0.048973820592611905 | 67 |
| INDUSTRIALS | Industrials Sector | 185.18 | 174.4199981689453 | -0.05810563684552705 | 68 |
| SOLAR | Solar Energy | 52.75 | 49.130001068115234 | -0.06862557216843157 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 250.75 | 223.52999877929688 | -0.10855434185724078 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 30.0 | -0.015393889705251462 | -0.004618166911575438 | Strongest prior trend in universe (46% prior active return) with a recent pullback; strongest earnings season since 2021 supports AI-driven chip demand into September. |
| anthropic-claude-fable-5 | MOMENTUM | 25.0 | -0.0020367178281188725 | -0.0005091794570297181 | Top-decile prior trend with deep recent relative pullback (0.93 pullback rank), a favorable mean-reversion-plus-trend setup in a strong earnings tape. |
| anthropic-claude-fable-5 | UTILITIES | 25.0 | -0.0036688657890517895 | -0.0009172164472629474 | Deepest recent relative pullback (0.955 rank) after a positive prior trend; stable rates and defensive rotation support a bounce. |
| anthropic-claude-fable-5 | SP500 | 20.0 | -0.009440521981408212 | -0.0018881043962816425 | Benchmark ballast: solid GDP, strong earnings season, expanding ISM readings. |
| anthropic-claude-opus-4-8 | SP500 | 50.0 | -0.009440521981408212 | -0.004720260990704106 | Broad large-cap core with strongest earnings season since 2021 and solid GDP/services activity backdrop. |
| anthropic-claude-opus-4-8 | SOFTWARE | 25.0 | -0.0002921057346443323 | -7.302643366108308e-05 | Strong recent 21s active return (+4.4%) with deep prior pullback, leadership in AI/tech with room to run vs stretched semis. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | -0.005208346578809975 | -0.0013020866447024937 | Positive active 21s return (+2.06%), shallowest drawdown, strong quality drawdown rank amid solid economy and elevated rates. |
| anthropic-claude-opus-5 | SP500 | 40.0 | -0.009440521981408212 | -0.003776208792563285 | Core benchmark exposure with strong earnings season and solid activity data. |
| anthropic-claude-opus-5 | FINANCIALS | 20.0 | -0.005208346578809975 | -0.001041669315761995 | Positive 21-day active return, lowest drawdown among sectors, steep curve (30y 5.22% vs 2y 4.25%) supports margins. |
| anthropic-claude-opus-5 | CYBERSECURITY | 20.0 | -0.039243718587322673 | -0.007848743717464536 | Strong prior active trend (+28.9%) with positive recent active return and only -1.6% from 52-week high; less crowded than semis. |
| anthropic-claude-opus-5 | AEROSPACE_DEFENSE | 10.0 | -0.10855434185724078 | -0.010855434185724079 | Positive recent active return, near 52-week high, geopolitical risk premium from Middle East conflict cited by the Fed. |
| anthropic-claude-opus-5 | EQUAL_WEIGHT_SP500 | 10.0 | -0.015266501306106295 | -0.0015266501306106296 | Low volatility and shallow drawdown breadth exposure; hedges mega-cap concentration risk. |
| google-gemini-3-1-pro | SP500 | 50.0 | -0.009440521981408212 | -0.004720260990704106 | Core holding to capture broad market beta amid solid economic expansion and strong earnings growth. |
| google-gemini-3-1-pro | TECHNOLOGY | 25.0 | -0.0005320257637522197 | -0.00013300644093805492 | Strong momentum and high quality evidence score, supported by solid economic activity. |
| google-gemini-3-1-pro | HEALTHCARE | 25.0 | 0.008751840190804439 | 0.0021879600477011096 | Defensive growth characteristics with a solid quality evidence score. |
| openai-gpt-5-5 | SEMICONDUCTORS | 30.0 | -0.015393889705251462 | -0.004618166911575438 | Highest quality evidence score among major high-beta growth candidates, with very strong prior active trend and deep recent pullback; positioned for continuation if earnings-led risk appetite persists. |
| openai-gpt-5-5 | CYBERSECURITY | 20.0 | -0.039243718587322673 | -0.007848743717464536 | Positive recent and prior active returns with smaller drawdown than semiconductors; offers technology-growth exposure with less extreme beta than the most volatile AI-linked funds. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 20.0 | -0.10855434185724078 | -0.021710868371448158 | Recent price strength and positive 21-day active return combine with geopolitical uncertainty cited in the briefing, while avoiding the technology cluster cap. |
| openai-gpt-5-5 | FINANCIALS | 15.0 | -0.005208346578809975 | -0.0007812519868214962 | Financials show positive 21-day active return, shallow drawdown, and potential support from firm activity data and a high-rate environment. |
| openai-gpt-5-5 | COPPER | 15.0 | 0.01679197230135898 | 0.0025187958452038473 | Copper has strong recent active return and near-52-week-high positioning, supported by expanding manufacturing and services survey activity. |
| openai-gpt-5-6-sol | CYBERSECURITY | 40.0 | -0.039243718587322673 | -0.01569748743492907 | Strong prior and recent benchmark-relative performance, proximity to its 52-week high, and lower volatility than several other technology themes support continued relative strength. |
| openai-gpt-5-6-sol | BIOTECH | 30.0 | 0.028976251355285365 | 0.00869287540658561 | The highest quality evidence score in the universe combines strong prior relative performance with a deep recent pullback, creating a supported mean-reversion opportunity. |
| openai-gpt-5-6-sol | AEROSPACE_DEFENSE | 30.0 | -0.10855434185724078 | -0.03256630255717223 | Positive one-month active performance, strong recent gains, and geopolitical uncertainty provide a distinct industrial and defense catalyst despite weaker prior trend. |
| xai-grok-4-3 | SEMICONDUCTORS | 50.0 | -0.015393889705251462 | -0.007696944852625731 | Highest quality evidence score and strong prior active rank support outperformance versus SPY over the one-month window. |
| xai-grok-4-3 | BIOTECH | 50.0 | 0.028976251355285365 | 0.014488125677642683 | Top quality evidence score with recent pullback rank and shallow drawdown support relative strength versus SPY. |
| xai-grok-4-5 | SEMICONDUCTORS | 30.0 | -0.015393889705251462 | -0.004618166911575438 | Highest quality score with extreme prior active trend and pullback support plus strong earnings backdrop favors outperformance vs broad market over one month. |
| xai-grok-4-5 | BIOTECH | 25.0 | 0.028976251355285365 | 0.007244062838821341 | Top quality-evidence score driven by deep recent pullback after strong prior trend supports mean-reversion plus risk-on continuation. |
| xai-grok-4-5 | TAIWAN | 25.0 | 0.08196722199560913 | 0.020491805498902282 | Very high quality score, semiconductor linkage, and recent relative strength after pullback position it above SPY base case. |
| xai-grok-4-5 | CYBERSECURITY | 20.0 | -0.039243718587322673 | -0.007848743717464536 | Strong prior active return and solid quality metrics with lower drawdown than pure semis support elevated base forecast. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | SEMICONDUCTORS | 4 | 0.58 | -0.015393889705251462 | 0.015268957708683648 | 0.024709479690091858 | 0.27844212130683055 |  | True | True |
| xai-grok-4-3 | SEMICONDUCTORS | 2 | 0.62 | -0.015393889705251462 | 0.006791180825016951 | 0.016231702806425163 | 0.28691989819049724 |  | True | True |
| google-gemini-3-1-pro | SP500 | 3 | 0.65 | -0.009440521981408212 | -0.0026653073839410513 | 0.006775214597467161 | 0.29637638639945524 |  | True | False |
| anthropic-claude-opus-4-8 | SP500 | 3 | 0.55 | -0.009440521981408212 | -0.006095374069067683 | 0.0033451479123405292 | 0.29980645308458187 |  | True | False |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 4 | 0.55 | -0.015393889705251462 | -0.007932667212149747 | 0.0015078547692584654 | 0.30164374622766393 |  | True | False |
| anthropic-claude-opus-5 | SP500 | 5 | 0.53 | -0.009440521981408212 | -0.025048706142124524 | -0.015608184160716312 | 0.3187597851576387 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.56 | -0.015393889705251462 | -0.032440235142105776 | -0.022999713160697564 | 0.32615131415761994 |  | False | False |
| openai-gpt-5-6-sol | CYBERSECURITY | 3 | 0.56 | -0.039243718587322673 | -0.03957091458551569 | -0.030130392604107478 | 0.3332819936010299 |  | False | False |

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
| prompt.md | ef3cf65c548d3cc3229f74393dc61292363e4cb8a6e609b4a75e4c2062b6698e |
| manifest.yaml | cd6d79bc192548b62cfa5446af2579276698d1876dd134644d1a39557b1dbd8a |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 449a13669e9c3c11b93393f187194a3b8247379c43375f926419a57e80e48d83 |
| market_data/universe_decision_context.md | 7d0960fd830739c87862a3db9880df5ea6ce0ab7d90d5e582a59c2f7c84d935c |
| market_data/universe_decision_context.json | 45c07d743c1a7fea839ef51d3f6a37bb76219cf0b6ad78be24914241816fa3aa |
| market_data/decision_context_source_history.json | 06ffc300b0d2cda899324e99ea80866c86b2ca592bc5a31b831f8414cfae2e28 |
| market_data/universe_quality_evidence.md | aebddc14b1343fca8aab364ed092b0311263c34bbc0720a630c5a8b01b5f3d39 |
| market_data/universe_quality_evidence.json | 471f5a31cb900bd78ceff36ecd481dbf3bf51721cc6fe51e63fe416fccca5999 |

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
