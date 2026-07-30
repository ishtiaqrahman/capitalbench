# CapitalBench Report: CB-2026-06-29-1M / official-20260629-no-fable-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260629-no-fable-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-29-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-06-29
- Decision deadline: 2026-06-30T03:30:00Z
- Horizon: one month
- Entry date: 2026-06-29
- Exit date: 2026-07-29
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | HEALTHCARE | 5 | 0.6 | Prioritize areas with documented recent outperformance and macro support from expansionary PMI and solid growth readings while maintaining a defensive component. | Hotter-than-expected CPI release on July 14 pressuring rate-sensitive holdings; Adverse surprise in July 2 employment report or July FOMC outcome; Reversal in recent healthcare and biotech momentum before exit close; Geopolitical developments affecting energy and broader risk appetite |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Overweight semis on Micron's exceptional results and supply-demand backdrop, paired with cyclical and defensive sector diversification and broad market core. | Semiconductor and SMH high beta (2.23) and elevated 30d volatility could amplify losses if the recent AI sentiment swings resume before exit close; Hot inflation prints (PCE 4.1%, sticky core) or hawkish July 28-29 FOMC commentary could pressure rate-sensitive cyclicals and growth; July 2 jobs report and July 14 CPI could trigger volatility against this equity-heavy allocation; Healthcare and financials recent strength may mean-revert; sector rotation could reverse the 30d leadership |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.6 | Combines leading defensive sector (healthcare), cyclical industrials supported by PMI strength, semis riding fresh Micron HBM catalyst, equal-weight broadening, and TLT as macro hedge. | Semiconductor reversal after huge YTD gains (SMH +73% 6m) if AI sentiment cracks; Hot June CPI (July 14) reigniting rate fears and hurting long Treasuries; Healthcare momentum reversal after sharp 30d rally; Geopolitical re-escalation Iran/oil shock pressuring cyclicals; Weak July payrolls undermining industrials/cyclical thesis |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.58 | A pro-risk but diversified allocation is favored because growth, employment, and PMI data remain solid while AI-linked stocks have a fresh fundamental catalyst from Micron. Healthcare and biotech add leadership outside the broad tech complex, and regional banks/small value add exposure to improving market breadth. | Semiconductor positioning is crowded after very large six- and twelve-month gains, and another AI or memory-stock reversal could dominate portfolio returns.; June CPI/PPI or the July 28-29 FOMC outcome could push yields higher and pressure high-beta equities, biotech financing conditions, and small caps.; Regional banks could underperform if credit-quality, deposit, commercial real estate, or yield-curve concerns re-emerge during earnings season.; Biotech and healthcare recent strength may reverse if leadership rotates back to mega-cap growth or if sector-specific regulatory and clinical-news risks hit sentiment.; Geopolitical headlines around Iran or oil could revive inflation fears and reduce risk appetite before the exit close. |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 4 | 0.7 | Overweighting semiconductors and technology based on strong earnings and AI demand, with tactical allocations to communications and consumer discretionary. | A reversal in the recent rebound of AI-linked stocks could negatively impact the semiconductor and technology allocations.; Higher-than-expected inflation data in the upcoming CPI and PPI releases could lead to higher interest rates, pressuring growth stocks.; A broader market downturn or increased volatility could disproportionately affect the high-beta technology and consumer discretionary sectors. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 107.08 | 129.31 | 0.20760179305192383 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 12.24 | 14.24 | 0.1633986928104576 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 15.84 | 17.56999969482422 | 0.10921715245102392 | 3 |
| ENERGY | Energy Sector | 53.58 | 58.650001525878906 | 0.09462488850091288 | 4 |
| CHINA | China Equities | 50.79 | 55.06999969482422 | 0.08426855079394024 | 5 |
| DIVIDEND | US Dividend Equities | 31.93 | 33.83000183105469 | 0.05950522489992749 | 6 |
| FINANCIALS | Financials Sector | 53.72 | 56.68000030517578 | 0.0551005269020064 | 7 |
| BITCOIN_ETF | Bitcoin ETF | 34.18 | 36.0 | 0.05324751316559384 | 8 |
| UNITED_KINGDOM | United Kingdom Equities | 46.15 | 47.9 | 0.037919826652220934 | 9 |
| AGRICULTURE | Agriculture Commodities | 26.51 | 27.49 | 0.03696718219539785 | 10 |
| AUSTRALIA | Australia Equities | 28.11 | 29.11 | 0.03557452863749555 | 11 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.37 | 87.36000061035156 | 0.03543914436827733 | 12 |
| HEALTHCARE | Healthcare Sector | 160.74 | 166.24000549316406 | 0.034216781716835065 | 13 |
| CANADA | Canada Equities | 57.49 | 59.29 | 0.03130979300747949 | 14 |
| COPPER | Copper | 37.23 | 38.35 | 0.030083266183185797 | 15 |
| LARGE_VALUE | US Large-Cap Value | 242.75 | 249.52 | 0.027888774459320365 | 16 |
| LOW_VOL | US Low Volatility Equities | 75.4498392066 | 77.54000091552734 | 0.02770266618069228 | 17 |
| SOFTWARE | Software | 89.89 | 92.37 | 0.027589275781510825 | 18 |
| BRAZIL | Brazil Equities | 34.55 | 35.47 | 0.026628075253256167 | 19 |
| REAL_ESTATE | Real Estate Sector | 44.92 | 45.959999084472656 | 0.023152250322187262 | 20 |
| MATERIALS | Materials Sector | 50.66 | 51.7400016784668 | 0.021318627683908353 | 21 |
| REGIONAL_BANKS | Regional Banks | 74.75 | 76.18 | 0.019130434782608896 | 22 |
| COMMUNICATIONS | Communication Services Sector | 107.88 | 109.51000213623047 | 0.015109400595388234 | 23 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.05 | 215.73 | 0.012579206758976724 | 24 |
| EUROPE | Europe Equities | 88.07 | 88.86000061035156 | 0.008970144321012397 | 25 |
| GOLD | Gold | 75.53 | 76.04000091552734 | 0.00675229598209115 | 26 |
| CYBERSECURITY | Cybersecurity | 88.5 | 88.79 | 0.0032768361581920757 | 27 |
| EURO | Euro | 105.3796130455 | 105.7 | 0.003040312497272879 | 28 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.3724586419 | 91.64 | 0.0029280306350136787 | 29 |
| US_DOLLAR | US Dollar | 28.37 | 28.42 | 0.0017624250969334732 | 30 |
| SMALL_VALUE | US Small-Cap Value | 221.28 | 221.60000610351562 | 0.0014461591807466423 | 31 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 32 |
| INDIA | India Equities | 49.18 | 49.16999816894531 | -0.00020337192059138864 | 33 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.6409728106 | 79.23999786376953 | -0.005034782131354221 | 34 |
| MEXICO | Mexico Equities | 76.12 | 75.57 | -0.007225433526011682 | 35 |
| YEN | Japanese Yen | 56.66 | 56.13 | -0.009354041651958966 | 36 |
| TIPS | Treasury Inflation-Protected Securities | 108.8354679824 | 107.7699966430664 | -0.00978974372128305 | 37 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 239.13 | 236.26 | -0.012001840003345476 | 38 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.4084809802 | 47.81 | -0.012363143153464873 | 39 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.6305097751 | 93.23 | -0.014799769951873487 | 40 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 99.0375074592 | 97.55000305175781 | -0.01501960666826141 | 41 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.4211996958 | 105.77 | -0.015371264708232135 | 42 |
| SP500 | S&P 500 | 741.0 | 729.46 | -0.015573549257759778 | 43 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.7465705256 | 93.16999816894531 | -0.016639888366499878 | 44 |
| SILVER | Silver | 52.68 | 51.77 | -0.01727410782080474 | 45 |
| TOTAL_US_MARKET | Total US Stock Market | 367.12 | 360.42 | -0.018250163434299416 | 46 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.4186045894 | 94.56 | -0.019276410370331454 | 47 |
| SOUTH_AFRICA | South Africa Equities | 63.42 | 62.08 | -0.021128981393882085 | 48 |
| MID_CAP | US Mid-Cap Stocks | 76.53 | 74.73 | -0.02352018816150525 | 49 |
| UTILITIES | Utilities Sector | 46.02 | 44.90999984741211 | -0.024119951164447984 | 50 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.92 | 68.94999694824219 | -0.027777820808767784 | 51 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.3154597394 | 106.22000122070312 | -0.028316749763265148 | 52 |
| INDUSTRIALS | Industrials Sector | 182.76 | 176.66000366210938 | -0.03337708655006899 | 53 |
| SMALL_CAP | US Small-Cap Stocks | 298.97 | 288.57000732421875 | -0.034786074441520154 | 54 |
| EMERGING_MARKETS | Emerging Markets | 59.18 | 56.91999816894531 | -0.038188608162465165 | 55 |
| JAPAN | Japan Equities | 93.21 | 89.3499984741211 | -0.04141188204998281 | 56 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.12 | 111.61000061035156 | -0.047045759815987354 | 57 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 87.1259976493 | 82.8499984741211 | -0.049078338160220336 | 58 |
| LARGE_GROWTH | US Large-Cap Growth | 121.98 | 114.05 | -0.06501065748483359 | 59 |
| BIOTECH | Biotechnology | 158.31 | 147.91 | -0.06569389173141305 | 60 |
| METALS_MINING | Metals and Mining | 106.52 | 97.58 | -0.08392790086368751 | 61 |
| NASDAQ100 | Nasdaq 100 | 724.08 | 661.73 | -0.08610926969395649 | 62 |
| TECHNOLOGY | Technology Sector | 185.41 | 166.57000732421875 | -0.10161260274948092 | 63 |
| BROAD_AI_TECH | Broad AI Technology | 64.22 | 55.98 | -0.12830893802553722 | 64 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 128.39 | 109.56 | -0.1466625126567489 | 65 |
| TAIWAN | Taiwan Equities | 105.79 | 89.41 | -0.15483505057188773 | 66 |
| MOMENTUM | US Momentum Equities | 336.0 | 283.1099853515625 | -0.15741075788225445 | 67 |
| SOLAR | Solar Energy | 57.6 | 47.68 | -0.17222222222222228 | 68 |
| SEMICONDUCTORS | Semiconductors | 631.98 | 504.2200012207031 | -0.2021582942170589 | 69 |
| SOUTH_KOREA | South Korea Equities | 197.5 | 144.21 | -0.26982278481012656 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 25.0 | 0.034216781716835065 | 0.008554195429208766 | Strong recent leadership (+8% 30d), defensive with low beta, biotech strength, and earnings season catalyst supportive into July. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 20.0 | -0.03337708655006899 | -0.006675417310013799 | Flash PMI manufacturing at 59-month high (55.7) and output expansion support cyclical industrials into Q2 earnings. |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 20.0 | -0.2021582942170589 | -0.04043165884341178 | Micron blowout with HBM demand exceeding supply through 2027 is a fresh sector catalyst; AI capex backdrop intact. |
| anthropic-claude-opus-4-7 | EQUAL_WEIGHT_SP500 | 20.0 | 0.012579206758976724 | 0.002515841351795345 | Broadening market participation; reduces mega-cap tech concentration risk while keeping equity beta near 1. |
| anthropic-claude-opus-4-7 | LONG_TREASURY | 15.0 | -0.049078338160220336 | -0.00736175072403305 | Hedge against growth scare/AI tech reversal; FOMC July 28-29 and softening employment in PMI could pull long yields lower. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 25.0 | -0.2021582942170589 | -0.05053957355426472 | Micron's blowout Q3 (revenue $41B vs $24B prior quarter) and guidance for $50B Q4 with 86% margins, plus commentary that memory demand runs ahead of supply through 2027, support continued semiconductor strength; strong fundamental catalyst beyond price momentum. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 20.0 | -0.03337708655006899 | -0.006675417310013799 | Flash manufacturing PMI at 55.7 with output index at 59-month high, plus solid GDP revision to 2.1%, support cyclicals; positive 30d benchmark-relative return with moderate volatility. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 20.0 | 0.034216781716835065 | 0.006843356343367014 | Strongest 7d (+7.1%) and 30d (+8.0%) sector with low beta (0.38) and defensive characteristics; supported by broad sector rotation, not price alone, and offers downside protection if AI swings resume. |
| anthropic-claude-opus-4-8 | FINANCIALS | 20.0 | 0.0551005269020064 | 0.01102010538040128 | Solid 30d alpha (+6.3%) with low drawdown; regional banks and financials benefit from steady Fed at 3.50-3.75% and healthy claims data; lower volatility cyclical exposure. |
| anthropic-claude-opus-4-8 | SP500 | 15.0 | -0.015573549257759778 | -0.0023360323886639665 | Core benchmark exposure to capture broad market rebound after the five-day losing streak ended, controlling tracking risk against the scoring benchmark. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | -0.2021582942170589 | -0.08086331768682356 | Micron's strong earnings and guidance, along with commentary on memory demand exceeding supply through 2027, provide a strong fundamental catalyst for semiconductors. |
| google-gemini-3-1-pro | NASDAQ100 | 30.0 | -0.08610926969395649 | -0.025832780908186945 | The Nasdaq 100 provides broad exposure to the technology sector, which is supported by the strong semiconductor outlook and the recent rebound in AI-linked stocks. |
| google-gemini-3-1-pro | COMMUNICATIONS | 15.0 | 0.015109400595388234 | 0.002266410089308235 | Communication services were reported among the stronger sectors, and Alphabet's addition to the Dow Jones Industrial Average could drive positive sentiment. |
| google-gemini-3-1-pro | CONSUMER_DISCRETIONARY | 15.0 | -0.047045759815987354 | -0.007056863972398103 | Consumer discretionary was also reported as a stronger sector, and positive personal income and consumption data support consumer spending. |
| openai-gpt-5-5 | SEMICONDUCTORS | 40.0 | -0.2021582942170589 | -0.08086331768682356 | Micron's exceptionally strong Q3 results, Q4 guide, and commentary that memory demand is running ahead of supply provide near-term fundamental support for AI-linked semiconductor sentiment despite very high volatility and crowded recent gains. |
| openai-gpt-5-5 | BIOTECH | 20.0 | -0.06569389173141305 | -0.01313877834628261 | Biotech has strong recent relative performance and sits at a 52-week high, while its healthcare linkage offers some diversification from mega-cap tech and rates-sensitive cyclicals; support beyond price action is limited, so reversal risk is material. |
| openai-gpt-5-5 | REGIONAL_BANKS | 15.0 | 0.019130434782608896 | 0.0028695652173913342 | Solid domestic growth data, lower jobless claims, and a still-high yield environment can support bank earnings and risk appetite, with recent relative strength and broad participation reinforcing the near-term setup. |
| openai-gpt-5-5 | HEALTHCARE | 15.0 | 0.034216781716835065 | 0.005132517257525259 | Healthcare combines recent sector leadership with lower beta than the S&P 500, offering defensive ballast if July inflation or Fed risks pressure higher-duration growth stocks. |
| openai-gpt-5-5 | SMALL_VALUE | 10.0 | 0.0014461591807466423 | 0.00014461591807466423 | Small-cap value has been outperforming with improving breadth, and solid PMI, income, spending, and labor data support domestic cyclicals over the one-month window. |
| xai-grok-4-3 | HEALTHCARE | 30.0 | 0.034216781716835065 | 0.010265034515050519 | Strong 30-day outperformance with supportive macro expansion signals from PMI and GDP data. |
| xai-grok-4-3 | BIOTECH | 25.0 | -0.06569389173141305 | -0.01642347293285326 | Leading recent returns amid positive manufacturing and services activity readings. |
| xai-grok-4-3 | INDUSTRIALS | 20.0 | -0.03337708655006899 | -0.006675417310013799 | Benefiting from flash PMI strength and solid economic activity indicators. |
| xai-grok-4-3 | SMALL_VALUE | 15.0 | 0.0014461591807466423 | 0.00021692387711199634 | Domestic growth exposure aligned with low claims and consumption data. |
| xai-grok-4-3 | LOW_VOL | 10.0 | 0.02770266618069228 | 0.002770266618069228 | Defensive tilt to navigate elevated inflation and upcoming data releases. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | HEALTHCARE | 5 | 0.6 | 0.034216781716835065 | -0.009846665232635316 | 0.005726884025124461 | 0.21744845828455914 |  | True | False |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.55 | -0.2021582942170589 | -0.04168756152917419 | -0.02611401227141441 | 0.24928935458109802 |  | False | False |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.6 | 0.034216781716835065 | -0.04339879009645451 | -0.027825240838694733 | 0.25100058314837836 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.58 | -0.2021582942170589 | -0.08585539764011492 | -0.07028184838235514 | 0.29345719069203874 |  | False | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 4 | 0.7 | -0.2021582942170589 | -0.11148655247810037 | -0.09591300322034059 | 0.3190883455300242 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 73765871e99df8b3698748a0947e5d669444b0b9ccaa2c481d82ab979927242e |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 7858eef0aa73ea38b28daacc4aaa57e57b110de6456378f1697ff1cd79ca213c |
| manifest.yaml | d331ea7f1203b56ec4442933c6e8487acaa58124f31248ff46eb65d43b60b758 |
| market_data/universe_trailing_returns.csv | 47896b757739d247dbf752630b66a15b56d7837e980d86db81c8bdfbf196ae1c |
| market_data/universe_trailing_returns.md | ecc7c68b2d5f32fdd96dc2de8c4c7c8c4528b2232c02ba17d9ea0117ad289d08 |
| market_data/universe_trailing_returns.json | 3df499e4af0a9a716b6d49960e294c72c33f47f01779e480cb4cbc8e6218200f |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 68ea14f7cdf7ce35eb687d4ec9be8a27bbecd2dc2b1155c78d0e438cff3e84ab | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 4707ce1223ffd1865d3864f299dfbe7baefaaff92c12f892dcf64bfa3945a86b | yes |
| Final briefing | research/final_briefing.md | model-facing | 73765871e99df8b3698748a0947e5d669444b0b9ccaa2c481d82ab979927242e | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
