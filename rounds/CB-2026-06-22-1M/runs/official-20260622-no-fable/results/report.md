# CapitalBench Report: CB-2026-06-22-1M / official-20260622-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260622-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-22-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-06-22
- Decision deadline: 2026-06-23T02:30:00Z
- Horizon: one month
- Entry date: 2026-06-22
- Exit date: 2026-07-22
- Entry rule: Use adjusted close prices on Monday, June 22, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Wednesday, July 22, 2026 as the one-month exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | SP500 | 5 | 0.65 | A balanced approach favoring US equities with a mix of growth, value, and defensive sectors. | Unexpected inflation spikes leading to higher interest rates.; A sudden reversal in technology sector momentum.; Broader economic slowdown impacting small-cap earnings. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.6 | Pro-cyclical, AI-led equity tilt with benchmark anchor and gold hedge for one-month window. | Semiconductor/AI momentum reversal or sharp factor rotation; Hot June CPI/PPI prints reprice rates higher, hitting growth and EM; Geopolitical shock to Taiwan/Korea supply chain; Crude weakness signaling demand slowdown hits industrials |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.58 | Combine AI/semiconductor and momentum continuation with a benchmark core and cyclical industrials for a balanced pro-trend stance into the July exit. | Sticky core/headline CPI (June print July 14) or hawkish rate repricing could hit high-beta semis and momentum hardest.; Crowded momentum/semiconductor positioning is vulnerable to a sharp factor rotation or AI-spending growth scare.; Geopolitical or trade shock affecting Taiwan/semiconductor supply chains.; Higher 10-year yields (4.5%) pressuring richly valued growth multiples before exit. |
| xai-grok-4-3 | xai | portfolio | SEMICONDUCTORS | 4 | 0.55 | Portfolio favors recent outperformers in semis and momentum for the one-month window, supplemented by small-cap and S&P 500 to balance event-driven volatility. | June CPI release on July 14 surprises to the upside, pressuring rate-sensitive growth holdings; July 2 employment report shows weaker-than-expected payrolls, triggering broad equity rotation; Semiconductor sector experiences post-run profit-taking ahead of holiday-shortened trading week |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.58 | Given resilient growth data and strong risk appetite in selected high-beta segments, continuation appears more attractive than defensive or benchmark-only positioning for the one-month window. The allocation accepts elevated volatility to maximize expected relative return versus SPY. | A sharp rotation out of crowded AI, semiconductor, and momentum trades could cause large underperformance versus the S&P 500.; Hot CPI, PPI, or PCE data could push Treasury yields higher and compress valuations for high-growth and high-beta equities.; Taiwan or South Korea exposure could be hurt by adverse currency moves, export concerns, or regional geopolitical headlines.; If investors shift toward defensive, value, or equal-weight exposure, the portfolio's concentrated growth and thematic tilts may lag. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 112.69 | 131.68 | 0.1685153962197179 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 13.06 | 14.52 | 0.11179173047473201 | 2 |
| ENERGY | Energy Sector | 54.06 | 59.20000076293945 | 0.09507955536328994 | 3 |
| BROAD_COMMODITIES | Broad Commodities | 16.36 | 17.809999465942383 | 0.08863077420185728 | 4 |
| CYBERSECURITY | Cybersecurity | 83.5080309702 | 89.33000183105469 | 0.06971749654751491 | 5 |
| BRAZIL | Brazil Equities | 34.27 | 36.62 | 0.0685730960023343 | 6 |
| HEALTHCARE | Healthcare Sector | 150.06 | 159.43 | 0.062441689990670346 | 7 |
| AGRICULTURE | Agriculture Commodities | 26.65 | 28.23 | 0.05928705440900561 | 8 |
| REGIONAL_BANKS | Regional Banks | 71.99 | 75.5999984741211 | 0.05014583239507009 | 9 |
| FINANCIALS | Financials Sector | 53.7 | 56.05 | 0.04376163873370564 | 10 |
| BIOTECH | Biotechnology | 145.86 | 152.11000061035156 | 0.04284931173969242 | 11 |
| LOW_VOL | US Low Volatility Equities | 73.104196633 | 76.2 | 0.042347820092212274 | 12 |
| DIVIDEND | US Dividend Equities | 31.6381515365 | 32.9 | 0.03988376065663135 | 13 |
| UNITED_KINGDOM | United Kingdom Equities | 45.69 | 47.24 | 0.03392427226964334 | 14 |
| UTILITIES | Utilities Sector | 44.72 | 45.93000030517578 | 0.027057251904646362 | 15 |
| CONSUMER_STAPLES | Consumer Staples Sector | 82.18 | 84.38 | 0.026770503772207244 | 16 |
| CANADA | Canada Equities | 57.89 | 59.279998779296875 | 0.024011034363393913 | 17 |
| BITCOIN_ETF | Bitcoin ETF | 36.5 | 37.34 | 0.023013698630137025 | 18 |
| REAL_ESTATE | Real Estate Sector | 44.02 | 45.0099983215332 | 0.02248973924427977 | 19 |
| COMMUNICATIONS | Communication Services Sector | 106.86 | 109.2 | 0.021897810218978186 | 20 |
| SOFTWARE | Software | 87.31 | 89.0199966430664 | 0.019585346959871686 | 21 |
| SMALL_VALUE | US Small-Cap Value | 217.99 | 222.05 | 0.018624707555392472 | 22 |
| LARGE_VALUE | US Large-Cap Value | 243.53 | 247.52 | 0.016384018396090827 | 23 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 209.61 | 212.6999969482422 | 0.014741648529374318 | 24 |
| AUSTRALIA | Australia Equities | 28.45 | 28.86 | 0.014411247803163496 | 25 |
| CHINA | China Equities | 52.86 | 53.56999969482422 | 0.013431700620965215 | 26 |
| COPPER | Copper | 38.81 | 39.25 | 0.011337284205101827 | 27 |
| MEXICO | Mexico Equities | 75.96 | 76.71 | 0.009873617693523018 | 28 |
| EUROPE | Europe Equities | 88.25 | 89.08999633789062 | 0.009518372100743688 | 29 |
| SP500 | S&P 500 | 744.39 | 747.41 | 0.004057013124840525 | 30 |
| US_DOLLAR | US Dollar | 28.36 | 28.45 | 0.003173483779971731 | 31 |
| TOTAL_US_MARKET | Total US Stock Market | 367.7503648176 | 368.87 | 0.0030445522003910153 | 32 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.3026630057 | 91.58 | 0.003037556465167901 | 33 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 34 |
| EURO | Euro | 105.3596263953 | 105.33 | -0.00028119305576168596 | 35 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.571295669 | 79.5199966430664 | -0.0006446926055719837 | 36 |
| TIPS | Treasury Inflation-Protected Securities | 107.8847668972 | 107.7699966430664 | -0.001063822608459164 | 37 |
| MID_CAP | US Mid-Cap Stocks | 76.07 | 75.69 | -0.004995398974628529 | 38 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.6900655313 | 93.0999984741211 | -0.0062980749755348064 | 39 |
| LARGE_GROWTH | US Large-Cap Growth | 121.76 | 120.92 | -0.006898817345597941 | 40 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.2999835031 | 97.58000183105469 | -0.007324331565351727 | 41 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.1590555836 | 47.8 | -0.007455619285903881 | 42 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.94 | 114.02 | -0.008004176091873982 | 43 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.9130835664 | 93.15 | -0.008125423395990095 | 44 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.0003458213 | 95.09 | -0.00948273481216999 | 45 |
| YEN | Japanese Yen | 56.79 | 56.23 | -0.009860891001936989 | 46 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.0322453937 | 105.88 | -0.010765404289722835 | 47 |
| GOLD | Gold | 78.8 | 77.69000244140625 | -0.014086263433930823 | 48 |
| SMALL_CAP | US Small-Cap Stocks | 298.18 | 293.79 | -0.01472265074787038 | 49 |
| MATERIALS | Materials Sector | 51.62 | 50.81999969482422 | -0.015497874954974455 | 50 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.3986846896 | 106.66999816894531 | -0.015947486130526323 | 51 |
| INDUSTRIALS | Industrials Sector | 181.8 | 178.85 | -0.016226622662266266 | 52 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 235.51 | 231.11000061035156 | -0.01868285588573071 | 53 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.39 | 70.48999786376953 | -0.026246748670126663 | 54 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.7710364509 | 83.44000244140625 | -0.027177402838406417 | 55 |
| SOUTH_AFRICA | South Africa Equities | 65.14 | 62.98 | -0.03315934909425855 | 56 |
| INDIA | India Equities | 49.92 | 48.220001220703125 | -0.03405446272629964 | 57 |
| EMERGING_MARKETS | Emerging Markets | 61.24 | 58.810001373291016 | -0.039679925321831955 | 58 |
| NASDAQ100 | Nasdaq 100 | 737.95 | 705.35 | -0.04417643471779931 | 59 |
| JAPAN | Japan Equities | 96.97 | 92.19000244140625 | -0.04929357078058938 | 60 |
| TECHNOLOGY | Technology Sector | 192.15 | 180.27 | -0.06182669789227169 | 61 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 130.04 | 119.13999938964844 | -0.08382036765880929 | 62 |
| SILVER | Silver | 58.91 | 53.92 | -0.08470548294007796 | 63 |
| TAIWAN | Taiwan Equities | 111.53 | 101.68 | -0.08831704474132518 | 64 |
| MOMENTUM | US Momentum Equities | 345.22 | 314.24 | -0.08973987602108802 | 65 |
| METALS_MINING | Metals and Mining | 115.22 | 103.5 | -0.10171845165769833 | 66 |
| BROAD_AI_TECH | Broad AI Technology | 67.0895278034 | 60.13999938964844 | -0.10358588950151137 | 67 |
| SOLAR | Solar Energy | 61.11 | 53.720001220703125 | -0.12092945146943013 | 68 |
| SEMICONDUCTORS | Semiconductors | 668.91 | 586.9099731445312 | -0.12258753323387106 | 69 |
| SOUTH_KOREA | South Korea Equities | 219.02 | 170.43 | -0.22185188567254133 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | -0.12258753323387106 | -0.03677625997016132 | Strong momentum, AI capex cycle intact, leading sector with 16% 30d return. |
| anthropic-claude-opus-4-7 | TAIWAN | 20.0 | -0.08831704474132518 | -0.017663408948265038 | Semi supply chain leverage with strong momentum and global electronics demand. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 20.0 | -0.016226622662266266 | -0.0032453245324532533 | Solid Philly Fed new orders 27.3, positive momentum, cyclical tailwind. |
| anthropic-claude-opus-4-7 | SP500 | 20.0 | 0.004057013124840525 | 0.0008114026249681051 | Benchmark anchor given mixed macro and sticky inflation risks. |
| anthropic-claude-opus-4-7 | GOLD | 10.0 | -0.014086263433930823 | -0.0014086263433930825 | Hedge after -7% drawdown; inflation risks skewed to upside per FOMC. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | -0.12258753323387106 | -0.03677625997016132 | Strong sustained momentum (+16% 30d, +86% 6m) with AI demand intact; leading group with positive 7d action while broad market wobbles. |
| anthropic-claude-opus-4-8 | SP500 | 30.0 | 0.004057013124840525 | 0.0012171039374521575 | Benchmark core anchor given sticky inflation and only modest Fed easing path; reduces active risk where edge is weak. |
| anthropic-claude-opus-4-8 | MOMENTUM | 20.0 | -0.08973987602108802 | -0.017947975204217603 | Persistent factor leadership (+13.8% 30d, +3.5% 7d) likely to continue into July absent a regime break. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 10.0 | -0.016226622662266266 | -0.0016226622662266267 | Solid breadth, positive 7d/30d trend, Philly Fed new orders strong; cyclical participation with lower volatility than tech. |
| anthropic-claude-opus-4-8 | TAIWAN | 10.0 | -0.08831704474132518 | -0.008831704474132519 | Semiconductor supply-chain leverage with strong momentum (+15% 30d, +5% 7d) and global electronics demand. |
| google-gemini-3-1-pro | SP500 | 40.0 | 0.004057013124840525 | 0.0016228052499362101 | Core broad market exposure given steady economic data and moderate inflation. |
| google-gemini-3-1-pro | TECHNOLOGY | 20.0 | -0.06182669789227169 | -0.012365339578454338 | Strong momentum and earnings resilience in the tech sector. |
| google-gemini-3-1-pro | SMALL_CAP | 15.0 | -0.01472265074787038 | -0.002208397612180557 | Potential for catch-up performance if broader market participation increases. |
| google-gemini-3-1-pro | HEALTHCARE | 15.0 | 0.062441689990670346 | 0.009366253498600551 | Defensive growth characteristics to balance tech exposure. |
| google-gemini-3-1-pro | SHORT_TREASURY | 10.0 | 0.003037556465167901 | 0.00030375564651679014 | Cash proxy for liquidity and risk management. |
| openai-gpt-5-5 | SEMICONDUCTORS | 35.0 | -0.12258753323387106 | -0.04290563663185487 | Strongest persistent price leadership across 7-day, 30-day, 6-month, and 1-year windows, with AI chip demand likely to remain a near-term catalyst despite high volatility. |
| openai-gpt-5-5 | MOMENTUM | 25.0 | -0.08973987602108802 | -0.022434969005272004 | Captures broad continuation in recent market winners while reducing single-industry concentration versus a pure semiconductor position. |
| openai-gpt-5-5 | TAIWAN | 20.0 | -0.08831704474132518 | -0.017663408948265038 | Taiwan equities have strong near-term and medium-term momentum and are leveraged to global semiconductor supply-chain strength. |
| openai-gpt-5-5 | SOUTH_KOREA | 10.0 | -0.22185188567254133 | -0.022185188567254134 | South Korea shows exceptional trend strength and offers additional AI-memory and export-cycle exposure, though with country and currency risk. |
| openai-gpt-5-5 | BIOTECH | 10.0 | 0.04284931173969242 | 0.004284931173969242 | Recent upside momentum provides a diversifying high-beta sleeve that is less directly tied to mega-cap technology and semiconductor positioning. |
| xai-grok-4-3 | SEMICONDUCTORS | 40.0 | -0.12258753323387106 | -0.049035013293548424 | Strong 30-day momentum and exposure to AI supply chain demand likely to persist through July data window. |
| xai-grok-4-3 | MOMENTUM | 25.0 | -0.08973987602108802 | -0.022434969005272004 | Factor has shown recent outperformance and benefits from continuation of growth trends into earnings season. |
| xai-grok-4-3 | SMALL_CAP | 20.0 | -0.01472265074787038 | -0.002944530149574076 | Domestic growth sensitivity and recent relative strength versus large caps ahead of employment and retail data. |
| xai-grok-4-3 | SP500 | 15.0 | 0.004057013124840525 | 0.0006085519687260788 | Benchmark exposure provides ballast against volatility around CPI and jobs releases. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | SP500 | 5 | 0.65 | 0.004057013124840525 | -0.0032809227955813433 | -0.007337935920421868 | 0.17179631901529924 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.6 | -0.12258753323387106 | -0.05828221716930459 | -0.06233923029414511 | 0.2267976133890225 |  | False | False |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.58 | -0.12258753323387106 | -0.06396149797728591 | -0.06801851110212644 | 0.2324768941970038 |  | False | False |
| xai-grok-4-3 | SEMICONDUCTORS | 4 | 0.55 | -0.12258753323387106 | -0.07380596047966842 | -0.07786297360450894 | 0.24232135669938631 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.58 | -0.12258753323387106 | -0.1009042719786768 | -0.10496128510351732 | 0.2694196681983947 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 318e3134692a3ab8402c796c9d817f944f76565c75a12f550fa5305bf973d9e6 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 15cfd72f631f247b0505ef997c6e93e6c8c27e052aad94143f8d9879a4a801b7 |
| manifest.yaml | e344939e12590c7cb290c40300be2b0e5764e182f06f0d0d9795af3ade3341e5 |
| market_data/universe_trailing_returns.csv | cd98e95caf8cf5f3b879f6922438b48ec3f7635d746869a98a823c4e128dab52 |
| market_data/universe_trailing_returns.md | 12d2ab6cfe977f390311f19cbc554861bbd823e84fe3e6c0c13713d69fcedf94 |
| market_data/universe_trailing_returns.json | b79033228f71e152d200738a4f69d2fa9bdfe5aa85befc3b67d6bc63f97405a4 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 7d8b51ca282f6ca230567d846ec207d3cb92fb9dbdaadbd7d11fed9bcfd72f13 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 61759a1657b19d22f00594f23589b9bdd8d80a2088fdcd4989ec2bb7c6fbe0b6 | yes |
| Final briefing | research/final_briefing.md | model-facing | 318e3134692a3ab8402c796c9d817f944f76565c75a12f550fa5305bf973d9e6 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
