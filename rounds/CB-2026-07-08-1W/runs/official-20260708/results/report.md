# CapitalBench Report: CB-2026-07-08-1W / official-20260708

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260708
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-08-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-08
- Decision deadline: 2026-07-09T07:30:00Z
- Horizon: one week
- Entry date: 2026-07-08
- Exit date: 2026-07-15
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | OIL | 3 | 0.7 | Overweighting oil and energy due to geopolitical catalysts, with a tactical allocation to financials ahead of key bank earnings. | A sudden easing of Middle East tensions could cause a sharp reversal in oil prices.; The July 14 CPI report could come in hotter than expected, triggering a broad market selloff.; Disappointing earnings or guidance from major banks could negatively impact the financials allocation. |
| xai-grok-4-5 | xai | portfolio | OIL | 5 | 0.42 | One-week edge comes from oil geopolitics, bank earnings, and value/cyclical tilt amid sticky inflation signals rather than broad beta or long-duration assets. | Iran de-escalation or inventory data reverse the oil spike before July 15 close; Hotter-than-expected June CPI on July 14 triggers broad risk-off that hits high-beta biotech and energy equities; JPM/WFC earnings miss or guidance disappointment undercuts financials allocation; Sudden risk-off or VIX spike reverses recent biotech and commodity momentum |
| openai-gpt-5-5 | openai | portfolio | OIL | 5 | 0.36 | Position for oil/geopolitical continuation, biotech and healthcare relative strength, and a semiconductor rebound around TSMC sales. Avoid broad duration-sensitive bonds and broad market exposure given elevated inflation risks and rising yields. | A rapid easing of Middle East tensions or crude inventory weakness could reverse the oil spike and hurt both OIL and ENERGY.; June CPI could come in benign, triggering a growth-led rally in broad equities that outperforms the more commodity- and healthcare-tilted portfolio.; TSMC monthly sales could disappoint or be interpreted as already priced in, causing semiconductor weakness to continue.; Biotech's very strong recent gains could reverse sharply on profit-taking or risk-off flows.; Higher yields and weaker payroll revisions could weigh on equity risk appetite broadly, including high-beta biotech and semiconductors. |
| xai-grok-4-3 | xai | portfolio | ENERGY | 3 | 0.55 | Energy and financials positioned for oil and earnings catalysts; healthcare adds defensive tilt before CPI and Beige Book. | Weaker-than-expected CPI could trigger broad equity rally favoring growth over value/energy tilt; Bank earnings misses on July 14 could reverse financials outperformance; Rapid de-escalation in Middle East could reverse oil gains before July 15 close |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.5 | Overweight relative-strength defensives and near-term earnings/oil catalysts while holding short duration cash to buffer rate and geopolitical risk. | Bank earnings (JPM/WFC) disappoint or guidance weakens, dragging Financials below benchmark; Iran truce holds and oil reverses, reversing Energy's recent 5%+ gains; Hot June CPI on July 14 spikes yields and pressures rate-sensitive Utilities; Tech-led rally continues and market-cap weighted SPY outpaces this defensive tilt |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Defensive-leaning barbell with catalyst plays: healthcare and low-vol for stability, financials for bank earnings, energy for geopolitical premium. | Hot June CPI on July 14 could pressure defensives and rate-sensitive sectors; Bank earnings disappointment from JPM/WFC could sink financials allocation; Iran truce holding would reverse oil premium and hit energy sector; Broad risk-on rotation into tech/growth would leave defensive tilt underperforming SPY |
| anthropic-claude-fable-5 | anthropic | portfolio | HEALTHCARE | 5 | 0.5 | Defensive-value and energy tilt with bank earnings and geopolitical oil catalysts, avoiding high-beta tech ahead of a risky CPI print. | A soft CPI print on July 14 could spark a growth/tech rally that this value tilt misses; An Iran truce resolution could quickly reverse energy gains; JPMorgan/Wells Fargo earnings disappointment or weak guidance hitting financials; Biotech momentum reversal after a sharp 30-day run |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 13.11 | 14.520000457763672 | 0.10755152233132503 | 1 |
| OIL | Crude Oil | 112.21 | 121.37999725341797 | 0.08172174720094438 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 35.23 | 36.810001373291016 | 0.04484817976982747 | 3 |
| BRAZIL | Brazil Equities | 34.41 | 35.880001068115234 | 0.04272017053517119 | 4 |
| COPPER | Copper | 37.07 | 38.630001068115234 | 0.0420825753470524 | 5 |
| COMMUNICATIONS | Communication Services Sector | 109.45999908447266 | 113.38 | 0.03581217749236587 | 6 |
| REGIONAL_BANKS | Regional Banks | 73.34 | 75.77999877929688 | 0.03326968610985648 | 7 |
| BROAD_COMMODITIES | Broad Commodities | 16.62 | 17.170000076293945 | 0.03309266403694 | 8 |
| SOLAR | Solar Energy | 54.14 | 55.79999923706055 | 0.030661234522729064 | 9 |
| FINANCIALS | Financials Sector | 54.970001220703125 | 56.560001373291016 | 0.028924870243391076 | 10 |
| CANADA | Canada Equities | 57.97 | 59.4900016784668 | 0.026220487812089077 | 11 |
| CHINA | China Equities | 52.85 | 54.150001525878906 | 0.02459794750953459 | 12 |
| AUSTRALIA | Australia Equities | 28.12 | 28.799999237060547 | 0.02418204968209614 | 13 |
| SOUTH_AFRICA | South Africa Equities | 62.69 | 63.7400016784668 | 0.016749109562399056 | 14 |
| SMALL_VALUE | US Small-Cap Value | 217.67999267578125 | 221.29 | 0.01658401068395654 | 15 |
| ENERGY | Energy Sector | 55.599998474121094 | 56.5 | 0.016187078247813513 | 16 |
| SOFTWARE | Software | 92.48 | 93.94000244140625 | 0.01578722363112295 | 17 |
| CYBERSECURITY | Cybersecurity | 91.66 | 93.08999633789062 | 0.0156010946747831 | 18 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.30000305175781 | 117.0 | 0.01474411884862703 | 19 |
| LARGE_GROWTH | US Large-Cap Growth | 121.80000305175781 | 123.58 | 0.014614096089027084 | 20 |
| AGRICULTURE | Agriculture Commodities | 27.62 | 27.979999542236328 | 0.013034016735565812 | 21 |
| SP500 | S&P 500 | 745.4000244140625 | 754.81 | 0.012624061279491228 | 22 |
| METALS_MINING | Metals and Mining | 101.94 | 103.19999694824219 | 0.012360181952542515 | 23 |
| MID_CAP | US Mid-Cap Stocks | 74.7300033569336 | 75.63 | 0.012043310620069692 | 24 |
| TOTAL_US_MARKET | Total US Stock Market | 368.25 | 372.42 | 0.011323828920570378 | 25 |
| EUROPE | Europe Equities | 88.18 | 89.12000274658203 | 0.010660044755976594 | 26 |
| JAPAN | Japan Equities | 92.54 | 93.5 | 0.0103738923708665 | 27 |
| REAL_ESTATE | Real Estate Sector | 44.150001525878906 | 44.560001373291016 | 0.009286519439229979 | 28 |
| MEXICO | Mexico Equities | 74.71 | 75.38999938964844 | 0.009101852357762619 | 29 |
| NASDAQ100 | Nasdaq 100 | 711.4400024414062 | 717.74 | 0.0088552759712337 | 30 |
| LARGE_VALUE | US Large-Cap Value | 245.1999969482422 | 247.28 | 0.008482883677183972 | 31 |
| SMALL_CAP | US Small-Cap Stocks | 293.4800109863281 | 295.77 | 0.007802878996684193 | 32 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.34 | 70.81999969482422 | 0.006823993386753102 | 33 |
| MATERIALS | Materials Sector | 50.15999984741211 | 50.5 | 0.006778312472531578 | 34 |
| UNITED_KINGDOM | United Kingdom Equities | 46.49 | 46.77000045776367 | 0.006022810448777616 | 35 |
| EMERGING_MARKETS | Emerging Markets | 59.17 | 59.47999954223633 | 0.005239133720404299 | 36 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.83 | 48.029998779296875 | 0.004181450539345155 | 37 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.2 | 212.97000122070312 | 0.0036286579674982278 | 38 |
| EURO | Euro | 105.45 | 105.80999755859375 | 0.003413917103781472 | 39 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.51000213623047 | 93.77999877929688 | 0.0028873557576554187 | 40 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.66 | 79.80999755859375 | 0.0018829721139059785 | 41 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.69 | 93.83000183105469 | 0.0014943092224857235 | 42 |
| INDIA | India Equities | 48.65 | 48.720001220703125 | 0.0014388740123971733 | 43 |
| YEN | Japanese Yen | 56.46 | 56.529998779296875 | 0.0012397941781239208 | 44 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.04 | 98.13999938964844 | 0.0010199856145289843 | 45 |
| TECHNOLOGY | Technology Sector | 181.39999389648438 | 181.58 | 0.0009923159292848371 | 46 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.44999694824219 | 91.52 | 0.0007654789950122254 | 47 |
| TIPS | Treasury Inflation-Protected Securities | 108.05000305175781 | 108.06999969482422 | 0.00018506841741428026 | 48 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 49 |
| DIVIDEND | US Dividend Equities | 32.34000015258789 | 32.34 | -4.718240131929008e-09 | 50 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.79 | 95.7300033569336 | -0.0006263351400607187 | 51 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 107.66999816894531 | 107.58000183105469 | -0.0008358534356934788 | 52 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.91 | 106.76000213623047 | -0.0014030293122208048 | 53 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.36000061035156 | 84.23999786376953 | -0.0014225076542651038 | 54 |
| INDUSTRIALS | Industrials Sector | 180.4199981689453 | 180.05999755859375 | -0.0019953476000729164 | 55 |
| UTILITIES | Utilities Sector | 45.36000061035156 | 45.220001220703125 | -0.0030864062558343397 | 56 |
| SEMICONDUCTORS | Semiconductors | 593.0 | 590.77001953125 | -0.003760506692664367 | 57 |
| US_DOLLAR | US Dollar | 28.36 | 28.25 | -0.003878702397743239 | 58 |
| LOW_VOL | US Low Volatility Equities | 75.86000061035156 | 75.47 | -0.005141057305743657 | 59 |
| GOLD | Gold | 76.74 | 76.27999877929688 | -0.0059942822609215796 | 60 |
| MOMENTUM | US Momentum Equities | 314.8500061035156 | 312.67 | -0.006923951282373109 | 61 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.38999938964844 | 83.47 | -0.010901758458375932 | 62 |
| SILVER | Silver | 52.83 | 52.209999084472656 | -0.01173577352881583 | 63 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 239.63 | 236.4199981689453 | -0.013395659270770244 | 64 |
| TAIWAN | Taiwan Equities | 103.9 | 102.48999786376953 | -0.013570761657656139 | 65 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 123.81 | 121.5199966430664 | -0.01849610982096439 | 66 |
| BROAD_AI_TECH | Broad AI Technology | 62.57 | 61.119998931884766 | -0.023174062140246643 | 67 |
| HEALTHCARE | Healthcare Sector | 162.3000030517578 | 158.29 | -0.02470735043966099 | 68 |
| BIOTECH | Biotechnology | 162.97 | 156.22000122070312 | -0.041418658521794605 | 69 |
| SOUTH_KOREA | South Korea Equities | 182.72 | 171.63999938964844 | -0.06063923276243188 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | HEALTHCARE | 25.0 | -0.02470735043966099 | -0.006176837609915248 | Strong recent relative strength, defensive against elevated inflation and rate risk into CPI, low beta. |
| anthropic-claude-fable-5 | ENERGY | 20.0 | 0.016187078247813513 | 0.0032374156495627027 | Brent up 5% above $78 on Iran truce doubts; geopolitical tension likely supports energy equities through the week. |
| anthropic-claude-fable-5 | FINANCIALS | 20.0 | 0.028924870243391076 | 0.005784974048678216 | JPMorgan and Wells Fargo Q2 earnings July 14; sector showing positive momentum and benefits from higher yields. |
| anthropic-claude-fable-5 | BIOTECH | 15.0 | -0.041418658521794605 | -0.006212798778269191 | Strong persistent momentum (75% up days, near 52w high, +27% 30d) with modest drawdown risk. |
| anthropic-claude-fable-5 | LARGE_VALUE | 20.0 | 0.008482883677183972 | 0.0016965767354367946 | Value outperforming amid rising yields and sticky inflation; lower beta cushion ahead of CPI. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 30.0 | -0.02470735043966099 | -0.007412205131898297 | Strong momentum (+6.8% 30d), defensive with low beta 0.36, outperforming SPY significantly. |
| anthropic-claude-opus-4-7 | FINANCIALS | 25.0 | 0.028924870243391076 | 0.007231217560847769 | JPM/WFC earnings July 14 catalyst; sector +6.1% 30d with steepening curve support. |
| anthropic-claude-opus-4-7 | ENERGY | 20.0 | 0.016187078247813513 | 0.0032374156495627027 | Brent +5% on Iran truce doubts; oil geopolitical premium likely persists through window. |
| anthropic-claude-opus-4-7 | LOW_VOL | 15.0 | -0.005141057305743657 | -0.0007711585958615486 | Defensive tilt with CPI July 14 and Fed minutes flagging elevated inflation risks; low beta hedge. |
| anthropic-claude-opus-4-7 | UTILITIES | 10.0 | -0.0030864062558343397 | -0.000308640625583434 | Defensive with AI power demand tailwind; strong 30d relative outperformance. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 25.0 | -0.02470735043966099 | -0.006176837609915248 | Strong 30d relative outperformance (+5.7% vs SPY), defensive low-beta profile with momentum into a week featuring CPI and elevated inflation risk. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | 0.028924870243391076 | 0.007231217560847769 | JPM and WFC Q2 earnings July 14 are near-term catalysts; sector shows strong relative strength (+5% vs SPY 30d) and higher yields support net interest margins. |
| anthropic-claude-opus-4-8 | ENERGY | 20.0 | 0.016187078247813513 | 0.0032374156495627027 | Brent up 5% above $78 on Iran truce doubts; energy led with +5.3% 7d momentum and low correlation to broad market provides diversification. |
| anthropic-claude-opus-4-8 | UTILITIES | 15.0 | -0.0030864062558343397 | -0.0004629609383751509 | Defensive low-beta with strong 30d relative strength (+3.8% vs SPY) and high up-day share; hedge against elevated VIX and inflation surprises. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 15.0 | 0.0007654789950122254 | 0.0001148218492518338 | Cash-like buffer against rising yields near 4.60%, CPI risk, and geopolitical volatility while preserving allocation flexibility. |
| google-gemini-3-1-pro | OIL | 40.0 | 0.08172174720094438 | 0.03268869888037775 | Brent crude surged 5% on renewed geopolitical tensions, providing a strong short-term catalyst for oil prices. |
| google-gemini-3-1-pro | ENERGY | 30.0 | 0.016187078247813513 | 0.004856123474344054 | Energy equities are positioned to benefit directly from the spike in underlying crude oil prices. |
| google-gemini-3-1-pro | FINANCIALS | 30.0 | 0.028924870243391076 | 0.008677461073017322 | Allocating to financials ahead of major Q2 earnings reports from JPMorgan Chase and Wells Fargo on July 14. |
| openai-gpt-5-5 | OIL | 30.0 | 0.08172174720094438 | 0.024516524160283316 | Direct exposure to the sharp crude move after renewed Iran-truce doubts, with geopolitical and inflation catalysts capable of affecting prices within the one-week window. |
| openai-gpt-5-5 | ENERGY | 20.0 | 0.016187078247813513 | 0.0032374156495627027 | Energy equities can benefit if the oil price spike persists, while offering less futures-specific volatility than direct crude exposure. |
| openai-gpt-5-5 | BIOTECH | 25.0 | -0.041418658521794605 | -0.010354664630448651 | Biotech has strong short-term relative momentum, is near its 52-week high, and may be less directly hurt than broad growth equities by the CPI and rates catalyst. |
| openai-gpt-5-5 | SEMICONDUCTORS | 15.0 | -0.003760506692664367 | -0.0005640760038996551 | TSMC June sales on July 10 provide a near-term AI supply-chain catalyst after a recent pullback in semiconductor shares. |
| openai-gpt-5-5 | HEALTHCARE | 10.0 | -0.02470735043966099 | -0.0024707350439660994 | Healthcare has recent relative strength and defensive characteristics that may help if CPI or yields pressure broad equities. |
| xai-grok-4-3 | ENERGY | 40.0 | 0.016187078247813513 | 0.006474831299125405 | Oil prices rose sharply on geopolitical supply concerns that can persist through the window; sector showed strongest 7d return. |
| xai-grok-4-3 | FINANCIALS | 35.0 | 0.028924870243391076 | 0.010123704585186875 | Major bank earnings on July 14 provide direct catalysts; sector posted solid recent performance amid higher yields. |
| xai-grok-4-3 | HEALTHCARE | 25.0 | -0.02470735043966099 | -0.006176837609915248 | Defensive characteristics and strong 7d/30d returns provide ballast ahead of CPI release. |
| xai-grok-4-5 | OIL | 30.0 | 0.08172174720094438 | 0.024516524160283316 | Geopolitical premium from Iran truce doubts already lifting Brent above $78; short-window supply risk can sustain or extend the 7d surge into the exit close. |
| xai-grok-4-5 | ENERGY | 25.0 | 0.016187078247813513 | 0.004046769561953378 | Direct equity beta to the same oil move plus sector leverage; recent 7d outperformance and elevated ISM prices support continuation versus broad equities. |
| xai-grok-4-5 | BIOTECH | 20.0 | -0.041418658521794605 | -0.008283731704358921 | Strongest 30d and solid 7d relative strength with low drawdown; risk-on factor that can keep running absent a sharp market-wide risk-off before July 15. |
| xai-grok-4-5 | FINANCIALS | 15.0 | 0.028924870243391076 | 0.004338730536508661 | JPM and WFC Q2 prints on July 14 provide a concrete near-term catalyst; higher yields and recent relative strength favor the sector over growth. |
| xai-grok-4-5 | LARGE_VALUE | 10.0 | 0.008482883677183972 | 0.0008482883677183973 | Value tilt benefits from elevated inflation narrative in FOMC minutes and rate resilience; lower beta and positive 7d/30d relative returns versus SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | OIL | 3 | 0.7 | 0.08172174720094438 | 0.046222283427739125 | 0.0335982221482479 | 0.06132923890358591 |  | True | True |
| xai-grok-4-5 | OIL | 5 | 0.42 | 0.08172174720094438 | 0.02546658092210483 | 0.012842519642613601 | 0.08208494140922021 |  | True | True |
| openai-gpt-5-5 | OIL | 5 | 0.36 | 0.08172174720094438 | 0.014364464131531612 | 0.0017404028520403847 | 0.09318705819979342 |  | True | True |
| xai-grok-4-3 | ENERGY | 3 | 0.55 | 0.016187078247813513 | 0.010421698274397033 | -0.0022023630050941947 | 0.097129824056928 |  | False | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.5 | -0.02470735043966099 | 0.003943656511371907 | -0.00868040476811932 | 0.10360786581995313 |  | False | True |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.55 | -0.02470735043966099 | 0.0019766288570671926 | -0.010647432422424035 | 0.10557489347425784 |  | False | True |
| anthropic-claude-fable-5 | HEALTHCARE | 5 | 0.5 | -0.02470735043966099 | -0.0016706699545067252 | -0.014294731233997953 | 0.10922219228583176 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | f48dcdb60f6d674558873430c5c02cbd99b027c8367b957f8ab4b88f4cf877fc |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 03b5e9792d4c6bade89526a62f43cbdf51184fe03753997a0637de246e708b81 |
| manifest.yaml | 94b1ec9b73acb42e599deca3a3c9e3fbf6959aed6e8bdfdde339dd21592efb57 |
| market_data/universe_trailing_returns.csv | 214b5d4c889a81e8b06cac9f4d7678919c1237d16ffd785e4952595e9a280d5d |
| market_data/universe_trailing_returns.md | 74765a42d67967459eaa2ebe43e18bb98ef3504031393e19e404961760a3f4f5 |
| market_data/universe_trailing_returns.json | fbdbb99aa8f75d9f4f56981b952b93392d035c88e01fd08e64450596f25e9208 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 4e31081d10525d7c7e7137ce4bdc21597427a98d5e19bc3da2f23bc1763bbc1f | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | f038f1d0d8943fc5d3ba539209faa3a0cc556ac6f24f33744301c1237f27bfbd | yes |
| Final briefing | research/final_briefing.md | model-facing | f48dcdb60f6d674558873430c5c02cbd99b027c8367b957f8ab4b88f4cf877fc | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
