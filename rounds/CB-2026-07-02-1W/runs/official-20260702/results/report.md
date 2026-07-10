# CapitalBench Report: CB-2026-07-02-1W / official-20260702

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260702
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-02-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-02
- Decision deadline: 2026-07-03T07:30:00Z
- Horizon: one week
- Entry date: 2026-07-02
- Exit date: 2026-07-09
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | SP500 | 4 | 0.65 | A balanced approach combining broad US equities, defensive sectors (Healthcare), potential beneficiaries of the rate environment (Financials), and a cash-like buffer (Short-Term Treasuries). | Unexpected negative earnings surprises from major banks could weigh on the Financials sector.; A sudden shift in interest rate expectations could negatively impact both equities and fixed income.; Broader market volatility could lead to underperformance relative to a more concentrated or aggressive strategy. |
| anthropic-claude-fable-5 | anthropic | portfolio | HEALTHCARE | 5 | 0.5 | Tilt toward healthcare, low-vol, and financials on soft labor data and bank earnings positioning, with biotech for rate-cut beta and SPY as ballast; underweight extended semis/tech showing drawdown risk. | Renewed mega-cap tech rally (e.g., strong TSMC June sales July 10 read-through) would leave this defensive tilt lagging SPY; Hot ISM Services or inflation-related surprise pushes yields up, hurting biotech and low-vol rate-sensitive holdings; Biotech and healthcare momentum reverses from 52-week highs with limited independent catalyst support in the window; Pre-earnings de-risking in banks before July 14 could stall financials |
| openai-gpt-5-5 | openai | portfolio | BIOTECH | 5 | 0.58 | Favor healthcare/biotech, financials, aerospace-defense, and low-volatility equities over cap-weighted S&P 500 exposure for a one-week window marked by weak jobs data, elevated inflation, and recent factor rotation away from mega-cap tech. The portfolio keeps enough risk to seek alpha while diversifying across 5 holdings. | Biotech and healthcare have already rallied sharply and could mean-revert or suffer idiosyncratic drug-policy, clinical, or financing headlines.; If mega-cap technology and semiconductors rebound strongly after recent weakness, the portfolio may lag the S&P 500 benchmark.; Financials could underperform if weak payroll data raises credit-quality concerns or if the yield curve/rates move unfavorably before bank earnings.; A stronger-than-expected ISM Services release or renewed risk-on move could reduce demand for low-volatility and defensive sectors.; Holiday-shortened trading and low liquidity around July 4 could amplify reversals in recent factor momentum. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Overweight healthcare, financials, low-vol and value leadership with a cash-like anchor to seek positive alpha versus SPY in a low-catalyst week. | Sharp tech/semiconductor rebound would drive SPY/QQQ up and cause defensive tilt to lag the benchmark; Healthcare and value recent strength could reverse (crowding/mean reversion) before exit close; Rate spike or hawkish data ahead of ISM Services (July 6) could pressure rate-sensitive financials and low-vol names; Bank pre-earnings de-risking or negative guidance chatter could weigh on financials before July 14 reports |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Defensive-leaning equity mix leveraging recent sector rotation into healthcare, financials, and low-vol, with equal-weight breadth and T-bill ballast to manage tech reversal risk over the one-week window. | Mega-cap tech rebound could cause equal-weight/defensive tilt to lag SPY; Bank earnings anticipation could reverse if credit or NII guidance disappoints (though outside window); Healthcare momentum reversal after +12% 30d run; Softer labor data triggering risk-off across cyclicals including financials |
| xai-grok-4-3 | xai | portfolio | HEALTHCARE | 3 | 0.55 | Soft labor data favors defensives; allocate across healthcare, staples, and low-vol to capture relative stability before exit close. | Stronger-than-expected ISM Services PMI on July 6 could reverse defensive rotation; Holiday liquidity may amplify any equity rebound on positive sentiment; Unexpected Fed commentary could shift rate expectations rapidly |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 103.98 | 109.01 | 0.04837468743989226 | 1 |
| CHINA | China Equities | 50.90999984741211 | 53.19 | 0.044784917686535586 | 2 |
| CYBERSECURITY | Cybersecurity | 90.66999816894531 | 94.26 | 0.03959415356296181 | 3 |
| AGRICULTURE | Agriculture Commodities | 26.74 | 27.71 | 0.036275243081525854 | 4 |
| BROAD_COMMODITIES | Broad Commodities | 15.869999885559082 | 16.42 | 0.03465659221216466 | 5 |
| BROAD_AI_TECH | Broad AI Technology | 61.849998474121094 | 63.83 | 0.03201295997941478 | 6 |
| ENERGY | Energy Sector | 53.220001220703125 | 54.82 | 0.030063862130736974 | 7 |
| BITCOIN_ETF | Bitcoin ETF | 34.87 | 35.81 | 0.026957269859478217 | 8 |
| TECHNOLOGY | Technology Sector | 180.58999633789062 | 185.35 | 0.026358069431505093 | 9 |
| SEMICONDUCTORS | Semiconductors | 592.2899780273438 | 607.73 | 0.02606834919625034 | 10 |
| ETHEREUM_ETF | Ethereum ETF | 12.86 | 13.19 | 0.025660964230171057 | 11 |
| SOUTH_KOREA | South Korea Equities | 180.14 | 184.75 | 0.025591206839125302 | 12 |
| BIOTECH | Biotechnology | 160.46 | 164.28 | 0.02380655615106564 | 13 |
| LARGE_GROWTH | US Large-Cap Growth | 121.16000366210938 | 123.3 | 0.017662564156556426 | 14 |
| BRAZIL | Brazil Equities | 34.43 | 34.96 | 0.01539355213476612 | 15 |
| NASDAQ100 | Nasdaq 100 | 712.5999755859375 | 723.28 | 0.014987404967675921 | 16 |
| MOMENTUM | US Momentum Equities | 316.5299987792969 | 321.2 | 0.014753739736243165 | 17 |
| COPPER | Copper | 37.29 | 37.75 | 0.012335746849021278 | 18 |
| CANADA | Canada Equities | 57.77 | 58.38 | 0.010559113726847924 | 19 |
| SP500 | S&P 500 | 744.780029296875 | 751.71 | 0.00930472143522354 | 20 |
| COMMUNICATIONS | Communication Services Sector | 109.5999984741211 | 110.51 | 0.008302933745877539 | 21 |
| EMERGING_MARKETS | Emerging Markets | 59.040000915527344 | 59.49 | 0.007621935594420259 | 22 |
| TOTAL_US_MARKET | Total US Stock Market | 368.760009765625 | 371.45 | 0.00729469075587863 | 23 |
| JAPAN | Japan Equities | 93.13999938964844 | 93.52 | 0.004079886330703442 | 24 |
| AUSTRALIA | Australia Equities | 28.09 | 28.2 | 0.00391598433606255 | 25 |
| SOFTWARE | Software | 93.56999969482422 | 93.88 | 0.003313030952087459 | 26 |
| TAIWAN | Taiwan Equities | 104.86 | 105.05 | 0.0018119397291627148 | 27 |
| US_DOLLAR | US Dollar | 28.34 | 28.36 | 0.0007057163020465218 | 28 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.70999908447266 | 79.75 | 0.000501830585708074 | 29 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.44000244140625 | 91.46 | 0.00021869595428491984 | 30 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 31 |
| GOLD | Gold | 77.51000213623047 | 77.51 | -2.7560707049900657e-08 | 32 |
| EURO | Euro | 105.47 | 105.42 | -0.0004740684554849217 | 33 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.80999755859375 | 70.73 | -0.00112974948950606 | 34 |
| SMALL_CAP | US Small-Cap Stocks | 297.5799865722656 | 297.24 | -0.0011425048309928743 | 35 |
| FINANCIALS | Financials Sector | 55.619998931884766 | 55.54 | -0.0014383123592421887 | 36 |
| LARGE_VALUE | US Large-Cap Value | 246.80999755859375 | 246.38 | -0.001742220991237109 | 37 |
| TIPS | Treasury Inflation-Protected Securities | 108.33000183105469 | 108.12 | -0.0019385380550642761 | 38 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.12000274658203 | 116.85 | -0.0023053512657974506 | 39 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.2 | 95.96 | -0.002494802494802606 | 40 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.13 | 93.82 | -0.0032933177520451107 | 41 |
| DIVIDEND | US Dividend Equities | 32.38999938964844 | 32.26 | -0.004013565671445729 | 42 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.12000274658203 | 93.71 | -0.004356170151056715 | 43 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.61000061035156 | 98.18 | -0.004360618676503836 | 44 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.24 | 48.02 | -0.004560530679933672 | 45 |
| REGIONAL_BANKS | Regional Banks | 75.02 | 74.65 | -0.004932018128498972 | 46 |
| MID_CAP | US Mid-Cap Stocks | 76.08999633789062 | 75.7 | -0.00512546138337 | 47 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.5 | 106.94 | -0.005209302325581366 | 48 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 214.91 | 213.5 | -0.006560885952259121 | 49 |
| YEN | Japanese Yen | 56.95 | 56.48 | -0.008252853380158132 | 50 |
| SMALL_VALUE | US Small-Cap Value | 221.3300018310547 | 219.5 | -0.00826820501475245 | 51 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.63999938964844 | 107.71 | -0.00856037734603543 | 52 |
| HEALTHCARE | Healthcare Sector | 163.74000549316406 | 162.17 | -0.009588405035381609 | 53 |
| REAL_ESTATE | Real Estate Sector | 44.68000030517578 | 44.23 | -0.010071627173280362 | 54 |
| EUROPE | Europe Equities | 89.3499984741211 | 88.41 | -0.010520408395903402 | 55 |
| INDIA | India Equities | 49.560001373291016 | 49.02 | -0.01089591118498301 | 56 |
| SOUTH_AFRICA | South Africa Equities | 64.0 | 63.28 | -0.011249999999999982 | 57 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.51000213623047 | 84.49 | -0.011928454107689723 | 58 |
| UTILITIES | Utilities Sector | 45.7599983215332 | 45.13 | -0.013767446342688006 | 59 |
| INDUSTRIALS | Industrials Sector | 183.91000366210938 | 181.11 | -0.015224857845436701 | 60 |
| UNITED_KINGDOM | United Kingdom Equities | 47.16 | 46.41 | -0.01590330788804073 | 61 |
| SILVER | Silver | 55.02 | 54.14 | -0.015994183933115247 | 62 |
| LOW_VOL | US Low Volatility Equities | 76.7300033569336 | 75.5 | -0.016030278940714293 | 63 |
| MEXICO | Mexico Equities | 75.5 | 74.24 | -0.016688741721854417 | 64 |
| METALS_MINING | Metals and Mining | 105.12999725341797 | 103.24 | -0.017977716187532078 | 65 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.98999786376953 | 83.2 | -0.02106127672386482 | 66 |
| SOLAR | Solar Energy | 56.31999969482422 | 54.95 | -0.02432527880411406 | 67 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 127.94000244140625 | 124.7 | -0.025324389397992197 | 68 |
| MATERIALS | Materials Sector | 52.0099983215332 | 50.26 | -0.0336473443185763 | 69 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 248.19 | 239.62 | -0.03452999717958016 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | HEALTHCARE | 30.0 | -0.009588405035381609 | -0.0028765215106144825 | Strong recent breadth (66.7% up days), at 52-week high with low beta; defensive tilt fits soft payrolls and slowing labor data, low reversal-drawdown profile. |
| anthropic-claude-fable-5 | FINANCIALS | 20.0 | -0.0014383123592421887 | -0.00028766247184843776 | Positive pre-positioning into JPMorgan/Wells Fargo Q2 earnings on July 14, steep 2s10s curve supports net interest margins; broad 30d strength with modest volatility. |
| anthropic-claude-fable-5 | LOW_VOL | 20.0 | -0.016030278940714293 | -0.003206055788142859 | Rotation toward defensives evidenced by Dow outperformance and weak payrolls; near-zero beta cushions any tech-led pullback while capturing equity upside. |
| anthropic-claude-fable-5 | BIOTECH | 15.0 | 0.02380655615106564 | 0.0035709834226598457 | At 52-week high with 71% up-day share; benefits from falling rate expectations after +57k payrolls; momentum supported by improving financing conditions, though continuation evidence beyond price action is limited. |
| anthropic-claude-fable-5 | SP500 | 15.0 | 0.00930472143522354 | 0.0013957082152835309 | Benchmark ballast to control tracking error in a quiet holiday-shortened week. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 30.0 | -0.009588405035381609 | -0.0028765215106144825 | Strong defensive leadership with XLV +12.3% 30d and +5.2% 7d; low beta 0.37 offers relative safety in a quiet holiday-shortened week. |
| anthropic-claude-opus-4-7 | FINANCIALS | 25.0 | -0.0014383123592421887 | -0.0003595780898105472 | XLF +8.5% 30d with JPM and WFC earnings July 14 providing positioning tailwind; steep curve (30y 4.98%, 2y 4.18%) supports banks. |
| anthropic-claude-opus-4-7 | LOW_VOL | 20.0 | -0.016030278940714293 | -0.003206055788142859 | SPLV +7.3% 30d, low 14.9% vol, and near 52w high; defensive tilt fits quiet post-holiday week with soft payrolls. |
| anthropic-claude-opus-4-7 | EQUAL_WEIGHT_SP500 | 15.0 | -0.006560885952259121 | -0.0009841328928388681 | RSP avoids mega-cap tech drawdown risk (SMH -7% week, MTUM -6.7%) while retaining broad equity exposure at near 52w high. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 10.0 | 0.00021869595428491984 | 2.1869595428491984e-05 | Cash-like ballast given soft payrolls (+57k), negative revisions, and elevated core PCE 3.4% creating mixed macro. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | -0.009588405035381609 | -0.0028765215106144825 | Strong recent leadership (+5.2% 7d, +12.3% 30d, +14% vs SPX) with low beta and defensive tilt; XLV at 52w high with broad participation supports near-term continuation while inflation stays elevated. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | -0.0014383123592421887 | -0.0003595780898105472 | Positive momentum (+4% 7d, +8.5% 30d) with big-bank earnings (JPM, WFC) approaching July 14 driving constructive positioning into the window; steep yield curve supportive. |
| anthropic-claude-opus-4-8 | LOW_VOL | 20.0 | -0.016030278940714293 | -0.003206055788142859 | Defensive factor outperforming (+2.4% 7d, +9% vs SPX 30d) with lowest volatility and small drawdown; ballast given weak payrolls and elevated core PCE. |
| anthropic-claude-opus-4-8 | LARGE_VALUE | 15.0 | -0.001742220991237109 | -0.00026133314868556634 | Value leadership (+5.15% vs SPX 30d) at 52w high, low beta, cyclical/financial tilt aligning with rotation away from stretched tech. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 10.0 | 0.00021869595428491984 | 2.1869595428491984e-05 | Cash-like ballast with positive carry to reduce drawdown risk in a holiday-shortened, catalyst-light week for defensive posture. |
| google-gemini-3-1-pro | SP500 | 40.0 | 0.00930472143522354 | 0.003721888574089416 | Broad US equity exposure provides a baseline for the portfolio, capturing general market trends and economic resilience. |
| google-gemini-3-1-pro | HEALTHCARE | 20.0 | -0.009588405035381609 | -0.0019176810070763218 | Healthcare offers defensive characteristics and has shown recent strength, providing stability in a potentially volatile market. |
| google-gemini-3-1-pro | FINANCIALS | 20.0 | -0.0014383123592421887 | -0.00028766247184843776 | Financials may benefit from the current interest rate environment and upcoming earnings reports from major banks. |
| google-gemini-3-1-pro | SHORT_TREASURY | 20.0 | 0.00021869595428491984 | 4.373919085698397e-05 | Short-term Treasuries provide a cash-like buffer to mitigate downside risk and preserve capital. |
| openai-gpt-5-5 | BIOTECH | 30.0 | 0.02380655615106564 | 0.0071419668453196914 | Biotech has shown strong near-term leadership and is at a 52-week high, with support from broader healthcare strength; allocation is capped because the move is extended and reversal risk is high. |
| openai-gpt-5-5 | HEALTHCARE | 25.0 | -0.009588405035381609 | -0.002397101258845402 | Healthcare has the strongest 30-day benchmark-relative performance among broad sectors, lower beta than the S&P 500, and may benefit if weak payrolls keep investors favoring defensive growth. |
| openai-gpt-5-5 | FINANCIALS | 20.0 | -0.0014383123592421887 | -0.00028766247184843776 | Financials have positive 7-day and 30-day relative strength, low recent drawdown, and may see pre-earnings positioning ahead of large-bank reports just after the scoring window. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 15.0 | -0.03452999717958016 | -0.005179499576937024 | Aerospace and defense has strong recent relative performance and sector-specific demand/geopolitical support, while maintaining roughly market-level beta. |
| openai-gpt-5-5 | LOW_VOL | 10.0 | -0.016030278940714293 | -0.0016030278940714294 | Low-volatility equities provide defensive participation after weak labor data and have strong recent relative performance, though recent price strength alone could reverse. |
| xai-grok-4-3 | HEALTHCARE | 40.0 | -0.009588405035381609 | -0.0038353620141526436 | Weak June payrolls and downward revisions signal slowing growth, favoring defensive healthcare exposure over the holiday-shortened week. |
| xai-grok-4-3 | CONSUMER_STAPLES | 30.0 | -0.02106127672386482 | -0.006318383017159445 | Defensive staples sector benefits from lower risk appetite following soft labor data and potential rate-cut expectations. |
| xai-grok-4-3 | LOW_VOL | 30.0 | -0.016030278940714293 | -0.004809083682214288 | Low-volatility equities provide stability amid economic uncertainty and limited catalysts before July 9 close. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | SP500 | 4 | 0.65 | 0.00930472143522354 | 0.0015602842860216407 | -0.007744437149201899 | 0.04681440315387062 |  | False | True |
| anthropic-claude-fable-5 | HEALTHCARE | 5 | 0.5 | -0.009588405035381609 | -0.001403548132662402 | -0.010708269567885943 | 0.04977823557255466 |  | False | False |
| openai-gpt-5-5 | BIOTECH | 5 | 0.58 | 0.02380655615106564 | -0.0023253243563826024 | -0.011630045791606142 | 0.05070001179627486 |  | False | False |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.55 | -0.009588405035381609 | -0.006681618941824963 | -0.0159863403770485 | 0.05505630638171723 |  | False | False |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.55 | -0.009588405035381609 | -0.007404418685978265 | -0.016709140121201803 | 0.055779106125870524 |  | False | False |
| xai-grok-4-3 | HEALTHCARE | 3 | 0.55 | -0.009588405035381609 | -0.014962828713526378 | -0.024267550148749917 | 0.06333751615341864 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | HEALTHCARE | -0.010708269567885943 | 0.27189 | -0.03938456569894421 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 665508a1f43a6420716b2088c4ea4c58c7093fecfab26ae08b6d31e16110c67b |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 66320ebc013af445c33450b3005ec684487d06b5bca45c52a3ff9e8e24373e4c |
| manifest.yaml | 30e9e2534e00038bbb87cad4645de110c92799c939c23cd83014dc3a2d8cd2c1 |
| market_data/universe_trailing_returns.csv | d0b2637ab6beaf6936a83d10e4a4349ee1dfae22b344fc2d448bc6c3223000da |
| market_data/universe_trailing_returns.md | 7a0319653ef701364c37ed807b6b1ce1fa8c5393dde17fbec300bc96b6e12ba9 |
| market_data/universe_trailing_returns.json | a45afe4818e7b03b647778a0160024552f321f873c975c816d62d429dca7e83e |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 43c8e389b97d1460a319cc06b5a85f0ce83e68ef5495d3634730ab60abc95d28 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 8490095f22998d14f4967888865c2b43616b597a34346f3f98ed92b0a37ee8e4 | yes |
| Final briefing | research/final_briefing.md | model-facing | 665508a1f43a6420716b2088c4ea4c58c7093fecfab26ae08b6d31e16110c67b | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
