# CapitalBench Report: CB-2026-06-08-1W / official-20260608

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260608
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 8 2026 One-Week Portfolio Round
- Description: One-week CapitalBench portfolio evaluation round scored from the June 8, 2026 adjusted close to the June 15, 2026 adjusted close.
- Decision date: 2026-06-08
- Decision deadline: 2026-06-08T20:35:00Z
- Horizon: one week
- Entry date: 2026-06-08
- Exit date: 2026-06-15
- Entry rule: Use adjusted close on Monday, June 8, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Monday, June 15, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Position defensively ahead of CPI/PPI with sectors showing positive relative momentum, avoiding rate-sensitive long duration and stretched growth/tech. | Hot CPI could spike yields and hurt defensive rate-sensitive names; Tech/growth mean-reversion bounce would cause underperformance vs SPY; Healthcare policy headline risk from CMS drug pricing; ECB decision and Treasury auctions could shift rate expectations |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Rotate toward defensive and inflation-resilient sectors ahead of CPI/PPI and FOMC positioning, avoiding the high-beta tech/growth that led the recent selloff. | Cooler-than-expected CPI/PPI sparks a relief rally in growth/tech, causing defensive tilt to lag SPY; Energy reverses if oil inventory data or geopolitics shift supply outlook; Healthcare drug-pricing policy headlines (CMS negotiation) pressure the sector; Defensive sectors underperform if equity risk appetite broadly recovers into FOMC |
| xai-grok-4-3 | xai | portfolio | ENERGY | 3 | 0.55 | Allocates to ENERGY, HEALTHCARE, and FINANCIALS to capture relative strength and inflation sensitivity over the one-week window. | Adverse CPI surprise on June 10 triggering broad equity selloff; PPI release on June 11 amplifying volatility in rate-sensitive sectors; Unexpected strength in upcoming ECB decision spillover effects |
| openai-gpt-5-5 | openai | portfolio | ENERGY | 5 | 0.58 | Hot inflation data, resilient labor and manufacturing indicators, elevated oil, and tight credit spreads favor value, energy, financials, and defensive healthcare over duration-sensitive growth for the one-week window. The dollar allocation adds a hedge against hotter data and risk-off conditions. | A softer-than-expected CPI/PPI print could trigger a sharp rebound in technology and growth stocks, causing this value/defensive tilt to lag the S&P 500.; Oil prices could fall on EIA data, demand concerns, or positioning unwind, hurting the largest allocation.; Regional banks could underperform if Treasury yields rise in a disorderly way, credit concerns resurface, or deposit/CRE worries return.; Healthcare could reverse recent gains if investors rotate aggressively back into higher-beta growth after favorable macro data. |
| google-gemini-3-1-pro | google | portfolio | SHORT_TREASURY | 3 | 0.65 | A defensive allocation favoring short-term Treasuries, Healthcare, and Energy to navigate potential volatility from upcoming inflation data. | A significant downside surprise in inflation data could lead to a rapid equity market rally, causing this defensive portfolio to underperform the S&P 500.; A sharp drop in oil prices could negatively impact the Energy allocation.; Unexpected regulatory news or drug pricing developments could adversely affect the Healthcare sector. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOUTH_KOREA | South Korea Equities | 185.64 | 211.45 | 0.13903253609135957 | 1 |
| SEMICONDUCTORS | Semiconductors | 598.16 | 647.1 | 0.08181757389327271 | 2 |
| ETHEREUM_ETF | Ethereum ETF | 12.72 | 13.76 | 0.08176100628930816 | 3 |
| SOUTH_AFRICA | South Africa Equities | 63.4859715282 | 67.75 | 0.06716489279692217 | 4 |
| BIOTECH | Biotechnology | 128.43 | 136.4 | 0.06205715175582038 | 5 |
| MOMENTUM | US Momentum Equities | 314.7422164986 | 333.63 | 0.060010327535721775 | 6 |
| TAIWAN | Taiwan Equities | 100.43 | 106.37 | 0.05914567360350498 | 7 |
| MEXICO | Mexico Equities | 73.8198530251 | 77.76 | 0.05337516688851007 | 8 |
| BITCOIN_ETF | Bitcoin ETF | 35.89 | 37.74 | 0.05154639175257736 | 9 |
| MATERIALS | Materials Sector | 49.96 | 52.5 | 0.050840672538030374 | 10 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 227.1035147728 | 237.4 | 0.04533829094411357 | 11 |
| INDIA | India Equities | 47.21 | 49.26 | 0.043423003600931986 | 12 |
| EMERGING_MARKETS | Emerging Markets | 58.33 | 60.84 | 0.043031030344591104 | 13 |
| TECHNOLOGY | Technology Sector | 184.18 | 191.79 | 0.04131827559995638 | 14 |
| SMALL_CAP | US Small-Cap Stocks | 283.4413193691 | 294.64 | 0.039509696948301976 | 15 |
| NASDAQ100 | Nasdaq 100 | 716.07 | 744.0 | 0.0390045665926515 | 16 |
| BRAZIL | Brazil Equities | 33.371410924 | 34.64 | 0.038014247551267255 | 17 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.86 | 72.39 | 0.03621528771829374 | 18 |
| AUSTRALIA | Australia Equities | 27.6781509331 | 28.6 | 0.03330602066330868 | 19 |
| BROAD_AI_TECH | Broad AI Technology | 64.44 | 66.55 | 0.03274363749224074 | 20 |
| SMALL_VALUE | US Small-Cap Value | 210.4896026779 | 217.3 | 0.03235502958557812 | 21 |
| SILVER | Silver | 61.58 | 63.47 | 0.03069178304644371 | 22 |
| LARGE_VALUE | US Large-Cap Value | 236.5311433847 | 243.78 | 0.03064652084106445 | 23 |
| FINANCIALS | Financials Sector | 51.97 | 53.56 | 0.0305945737925728 | 24 |
| MID_CAP | US Mid-Cap Stocks | 73.9260584549 | 76.16 | 0.030218593981482966 | 25 |
| INDUSTRIALS | Industrials Sector | 173.63 | 178.68 | 0.029084835569890055 | 26 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.07 | 85.48 | 0.02901167689900097 | 27 |
| COPPER | Copper | 38.55 | 39.65 | 0.02853437094682243 | 28 |
| JAPAN | Japan Equities | 91.4628335149 | 94.06 | 0.028395867318902868 | 29 |
| UTILITIES | Utilities Sector | 43.52 | 44.74 | 0.028033088235294157 | 30 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.39 | 118.57 | 0.027558713926683298 | 31 |
| EUROPE | Europe Equities | 87.52 | 89.87 | 0.026851005484460844 | 32 |
| REGIONAL_BANKS | Regional Banks | 70.36 | 72.23 | 0.0265776009096077 | 33 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 207.61 | 212.88 | 0.025384133712248902 | 34 |
| CHINA | China Equities | 53.5776002353 | 54.93 | 0.02524188763140911 | 35 |
| LOW_VOL | US Low Volatility Equities | 72.47 | 74.2 | 0.023871947012557015 | 36 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 131.68 | 134.69 | 0.022858444714459303 | 37 |
| TOTAL_US_MARKET | Total US Stock Market | 364.47 | 372.53 | 0.022114302960462906 | 38 |
| REAL_ESTATE | Real Estate Sector | 44.03 | 44.99 | 0.021803315920962962 | 39 |
| SP500 | S&P 500 | 739.22 | 754.83 | 0.02111685289900156 | 40 |
| CANADA | Canada Equities | 57.7898303367 | 58.93 | 0.01972959007937991 | 41 |
| METALS_MINING | Metals and Mining | 118.59 | 120.63 | 0.017202124968378474 | 42 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.28 | 96.71 | 0.015008396305625338 | 43 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.62 | 85.72 | 0.012999290947766529 | 44 |
| LARGE_GROWTH | US Large-Cap Growth | 122.8744757638 | 124.36 | 0.012089770694571289 | 45 |
| DIVIDEND | US Dividend Equities | 32.29 | 32.63 | 0.01052957572003721 | 46 |
| COMMUNICATIONS | Communication Services Sector | 111.09 | 112.19 | 0.009901881357457842 | 47 |
| UNITED_KINGDOM | United Kingdom Equities | 45.7700437108 | 46.21 | 0.009612319620664556 | 48 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.7 | 94.52 | 0.008751334044823755 | 49 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.06 | 108.99 | 0.008606329816768454 | 50 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.52 | 94.28 | 0.008126603934987209 | 51 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.17 | 98.85 | 0.0069267597025566285 | 52 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.95 | 48.27 | 0.0066736183524505055 | 53 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.54 | 80.04 | 0.006286145335680171 | 54 |
| TIPS | Treasury Inflation-Protected Securities | 109.13 | 109.76 | 0.0057729313662604476 | 55 |
| EURO | Euro | 106.42 | 106.89 | 0.004416463070851417 | 56 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.94 | 107.17 | 0.0021507387319992244 | 57 |
| AGRICULTURE | Agriculture Commodities | 26.33 | 26.38 | 0.0018989745537409952 | 58 |
| CYBERSECURITY | Cybersecurity | 86.13 | 86.27 | 0.0016254499013119705 | 59 |
| HEALTHCARE | Healthcare Sector | 152.65 | 152.89 | 0.0015722240419258071 | 60 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.46 | 91.51 | 0.0005466870763175535 | 61 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 62 |
| YEN | Japanese Yen | 57.28 | 57.24 | -0.0006983240223463749 | 63 |
| GOLD | Gold | 81.38 | 81.26 | -0.0014745637748831975 | 64 |
| US_DOLLAR | US Dollar | 28.03 | 27.97 | -0.002140563681769625 | 65 |
| SOLAR | Solar Energy | 63.58 | 62.7 | -0.013840830449826869 | 66 |
| SOFTWARE | Software | 95.6326317603 | 92.68 | -0.030874730789597682 | 67 |
| BROAD_COMMODITIES | Broad Commodities | 17.62 | 16.89 | -0.04143019296254258 | 68 |
| ENERGY | Energy Sector | 58.33 | 55.55 | -0.04765986627807306 | 69 |
| OIL | Crude Oil | 135.15 | 121.21 | -0.1031446540880504 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 35.0 | 0.0015722240419258071 | 0.0005502784146740325 | Defensive sector with positive 7d/30d momentum amid broad market weakness; resilient ahead of hot CPI print. |
| anthropic-claude-opus-4-7 | LOW_VOL | 25.0 | 0.023871947012557015 | 0.005967986753139254 | Defensive factor outperforming with VIX elevated and sticky inflation pressuring growth/tech. |
| anthropic-claude-opus-4-7 | CONSUMER_STAPLES | 15.0 | 0.02901167689900097 | 0.004351751534850145 | Defensive positioning into CPI/PPI week with positive recent momentum. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 15.0 | 0.04533829094411357 | 0.006800743641617035 | Strong FY27 defense budget backdrop; lower beta to tech selloff. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 10.0 | 0.0005466870763175535 | 5.4668707631755356e-05 | Dry powder yielding ~3.6% with no duration risk into hot CPI print. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 35.0 | 0.0015722240419258071 | 0.0005502784146740325 | Strong defensive momentum (+3.25% 7d, +6.38% 30d) amid recent tech selloff; lower beta heading into hot CPI/PPI prints that could pressure growth. |
| anthropic-claude-opus-4-8 | ENERGY | 20.0 | -0.04765986627807306 | -0.009531973255614612 | Crude at $91 WTI with EIA forecasting global inventory draws; energy positive recent momentum and benefits if inflation surprises hot. |
| anthropic-claude-opus-4-8 | LARGE_VALUE | 20.0 | 0.03064652084106445 | 0.00612930416821289 | Value held up best among broad styles (-0.08% 7d) and is less rate-sensitive into CPI/PPI/FOMC-positioning week. |
| anthropic-claude-opus-4-8 | CONSUMER_STAPLES | 15.0 | 0.02901167689900097 | 0.004351751534850145 | Defensive sector positive (+1.27% 7d) with elevated inflation prints likely to favor staples over discretionary. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 10.0 | 0.0005466870763175535 | 5.4668707631755356e-05 | Cash-like ballast yielding positively with no duration risk into hot inflation data and FOMC-eve uncertainty. |
| google-gemini-3-1-pro | SHORT_TREASURY | 40.0 | 0.0005466870763175535 | 0.00021867483052702142 | Provides a stable, low-risk yield while avoiding equity market volatility ahead of key inflation data. |
| google-gemini-3-1-pro | HEALTHCARE | 30.0 | 0.0015722240419258071 | 0.00047166721257774213 | A defensive sector that has shown recent positive momentum and is less sensitive to immediate macroeconomic shocks. |
| google-gemini-3-1-pro | ENERGY | 30.0 | -0.04765986627807306 | -0.014297959883421918 | Offers exposure to elevated oil prices and strong recent sector performance, providing a hedge against inflation surprises. |
| openai-gpt-5-5 | ENERGY | 30.0 | -0.04765986627807306 | -0.014297959883421918 | High oil prices, EIA expectations for global inventory draws, and recent relative strength give energy favorable one-week inflation and commodity beta. |
| openai-gpt-5-5 | HEALTHCARE | 25.0 | 0.0015722240419258071 | 0.0003930560104814518 | Defensive sector with strong recent relative performance that can hold up if CPI/PPI or Treasury auctions pressure broad equity multiples. |
| openai-gpt-5-5 | REGIONAL_BANKS | 20.0 | 0.0265776009096077 | 0.005315520181921541 | Positive recent performance, a still-positive yield curve, and solid banking profitability support upside if growth remains resilient. |
| openai-gpt-5-5 | US_DOLLAR | 15.0 | -0.002140563681769625 | -0.00032108455226544373 | Sticky inflation and high U.S. yields ahead of CPI/PPI favor dollar strength, while it can also cushion risk-off equity moves. |
| openai-gpt-5-5 | INDUSTRIALS | 10.0 | 0.029084835569890055 | 0.0029084835569890056 | Improving ISM manufacturing and strong durable goods and factory orders support economically sensitive industrial exposure without as much mega-cap growth duration risk. |
| xai-grok-4-3 | ENERGY | 35.0 | -0.04765986627807306 | -0.01668095319732557 | Recent positive 7d return and sensitivity to inflation data releases within window |
| xai-grok-4-3 | HEALTHCARE | 30.0 | 0.0015722240419258071 | 0.00047166721257774213 | Strong recent performance and defensive characteristics ahead of CPI |
| xai-grok-4-3 | FINANCIALS | 35.0 | 0.0305945737925728 | 0.01070810082740048 | Positive trailing returns and exposure to rate environment |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.55 | 0.0015722240419258071 | 0.017725429051912222 | -0.0033914238470893372 | 0.12130710703944735 |  | False | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.55 | 0.0015722240419258071 | 0.0015540295697542112 | -0.019562823329247348 | 0.13747850652160537 |  | False | True |
| xai-grok-4-3 | ENERGY | 3 | 0.55 | -0.04765986627807306 | -0.005501185157347349 | -0.02661803805634891 | 0.14453372124870692 |  | False | False |
| openai-gpt-5-5 | ENERGY | 5 | 0.58 | -0.04765986627807306 | -0.006001984686295364 | -0.027118837585296922 | 0.14503452077765494 |  | False | False |
| google-gemini-3-1-pro | SHORT_TREASURY | 3 | 0.65 | 0.0005466870763175535 | -0.013607617840317155 | -0.03472447073931871 | 0.15264015393167674 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 9de9dfde5df095583b38a45473b628abb58e0768bc66dbc54b7646404756dc4e |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 29bcc94b677b8d749c2f807b79033b2524c83629237985ad667cb31fa57d6b22 |
| manifest.yaml | 71fe3dce4dad1c744a3be054f21fe223d06a97a78cfb32d8a52a3e0f23b3e6e7 |
| market_data/universe_trailing_returns.csv | a3fa1ed2b2573c3f609afc99e5e6af35d394cdc7cbc7411c4c1b1ee2c03995e0 |
| market_data/universe_trailing_returns.md | 42e92ab117d34e1be7af0cfc861ab4bd3ef1c3228e1a4b7c784b82490ddb83ab |
| market_data/universe_trailing_returns.json | a54fc5f6c27fea2eafb744e212b452df1b0dc5601e8ab84416d5b8611ee6527d |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | c0ad196d0ea058927ae572c735f83ee095a0ca7874201a5450b0859a8f8bd2b0 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 2a0a1ae1de2370822b4d8866e86244b13be50f22899e0ac666d12af7907acf37 | yes |
| Final briefing | research/final_briefing.md | model-facing | 9de9dfde5df095583b38a45473b628abb58e0768bc66dbc54b7646404756dc4e | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
