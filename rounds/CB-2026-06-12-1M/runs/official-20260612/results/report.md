# CapitalBench Report: CB-2026-06-12-1M / official-20260612

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260612
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 12 2026 One-Month Portfolio Round
- Description: One-month CapitalBench portfolio evaluation round scored from the latest available June 11, 2026 adjusted-close snapshot to the July 13, 2026 adjusted close.
- Decision date: 2026-06-12
- Decision deadline: 2026-06-12T23:30:00Z
- Horizon: one month
- Entry date: 2026-06-11
- Exit date: 2026-07-13
- Entry rule: Use adjusted close on Thursday, June 11, 2026 as the latest available pre-open June 12 entry snapshot for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Monday, July 13, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | ENERGY | 3 | 0.55 | High oil prices, persistent inflation above 4% YoY, and scheduled policy events favor a concentrated mix of energy, financials, and healthcare over broad equity or bond exposure for the one-month window. | FOMC decision on June 17 surprises markets with unexpected policy shift; PCE release on June 25 shows further inflation acceleration pressuring multiples; Weaker-than-expected retail sales or GDP revisions reduce growth-sensitive holdings |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Tilt toward leadership and lower-rate-sensitivity sectors while trimming concentration risk in the cap-weighted index that just sold off 2.5% in 7 days. | FOMC June 17 surprise or hawkish dots could pressure rate-sensitive equities and lift yields further.; Semiconductors are high-beta and could reverse sharply if growth/AI sentiment cools.; Defensive tilt underperforms if a broad risk-on rally lifts cyclicals and mega-cap growth.; Sticky CPI/PPI YoY (4.2%/6.5%) and weak consumer sentiment could trigger a broader equity drawdown affecting all sleeves. |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.7 | Overweighting technology and energy to capture growth and commodity price tailwinds. | A sudden drop in oil prices could negatively impact the energy allocation.; Higher than expected inflation could lead to tighter monetary policy, hurting technology valuations.; Broader market downturn could drag down the S&P 500 core holding. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Balance AI/semi momentum and defensive cyclicals against macro risks from rising headline CPI, 4.55% 10Y yields, and FOMC uncertainty. | Hawkish FOMC surprise on June 17 spikes yields and hits growth/semis; Sticky headline CPI (4.2% YoY) triggers risk-off and multiple compression; Semiconductor cycle pullback after large run, profit-taking in SMH; Healthcare policy headlines or weak biotech sentiment drag XLV |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.56 | Macro data show resilient growth and labor conditions with elevated inflation, making a Fed hold likely and supporting selective risk assets rather than duration. Recent momentum is strongest in semiconductors, cybersecurity, regional banks, aerospace-defense, and South Korea, so the allocation emphasizes those leadership pockets. | A hawkish FOMC statement or hotter-than-expected PCE data could lift yields and pressure high-valuation technology and semiconductor holdings.; Semiconductor and South Korea exposure could reverse sharply if AI/chip momentum unwinds or geopolitical risk in East Asia rises.; Regional banks could underperform if deposit stress, credit-quality concerns, or commercial real estate worries re-emerge.; The portfolio is highly concentrated in high-beta momentum areas, so a broad risk-off rotation into defensive sectors or cash-like assets would likely hurt relative performance. |
| anthropic-claude-fable-5 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.45 | Momentum-led barbell: AI/semiconductor and Korea/Taiwan momentum plus energy as an inflation/oil hedge to beat SPY over one month. | Sharp factor rotation or AI/semiconductor de-rating reverses momentum exposures simultaneously; Hawkish FOMC surprise on June 17 hits high-beta growth and EM Asia; Oil price reversal from $95 drags energy allocation; Dollar strength (broad index at 120) pressures Korea/Taiwan returns; Concentrated correlation between SMH, EWY, EWT, and MTUM amplifies drawdowns |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 132.6144463228 | 155.34 | 0.17136559633844994 | 1 |
| CYBERSECURITY | Cybersecurity | 85.3964035298 | 91.84 | 0.07545512695919854 | 2 |
| FINANCIALS | Financials Sector | 52.4373160076 | 56.07 | 0.06927669585288254 | 3 |
| AGRICULTURE | Agriculture Commodities | 26.3 | 27.719999313354492 | 0.053992369329068035 | 4 |
| ETHEREUM_ETF | Ethereum ETF | 12.7 | 13.369999885559082 | 0.052755896500715105 | 5 |
| HEALTHCARE | Healthcare Sector | 153.4190579527 | 161.41 | 0.0520857196878608 | 6 |
| UTILITIES | Utilities Sector | 43.7716166292 | 45.72 | 0.04451248367875538 | 7 |
| REGIONAL_BANKS | Regional Banks | 71.9335955106 | 75.12 | 0.044296471861057674 | 8 |
| LOW_VOL | US Low Volatility Equities | 73.7014324515 | 76.41 | 0.036750541453619556 | 9 |
| LARGE_VALUE | US Large-Cap Value | 239.0333419297 | 247.62 | 0.03592242823105973 | 10 |
| INDUSTRIALS | Industrials Sector | 174.7231929502 | 180.37 | 0.032318588931748105 | 11 |
| BRAZIL | Brazil Equities | 34.4808157136 | 35.39 | 0.02636782998267062 | 12 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 208.9424798296 | 214.23 | 0.025306104219267267 | 13 |
| SMALL_VALUE | US Small-Cap Value | 215.033148468 | 219.78 | 0.022074975722668144 | 14 |
| INDIA | India Equities | 47.79 | 48.79 | 0.0209248796819419 | 15 |
| SOFTWARE | Software | 90.9034906392 | 92.7 | 0.01976282041720956 | 16 |
| US_DOLLAR | US Dollar | 27.95 | 28.5 | 0.019677996422182487 | 17 |
| SP500 | S&P 500 | 735.8841566458 | 749.17 | 0.01805425926650961 | 18 |
| TOTAL_US_MARKET | Total US Stock Market | 363.2533225863 | 369.78 | 0.01796728896306088 | 19 |
| SMALL_CAP | US Small-Cap Stocks | 289.7264632546 | 293.48 | 0.012955450127803969 | 20 |
| JAPAN | Japan Equities | 91.6916391778 | 92.72 | 0.011215426307363607 | 21 |
| DIVIDEND | US Dividend Equities | 32.2730971929 | 32.56 | 0.008889844237295996 | 22 |
| CANADA | Canada Equities | 58.2178323746 | 58.73 | 0.008797435502312823 | 23 |
| REAL_ESTATE | Real Estate Sector | 44.5343980746 | 44.7 | 0.0037185172037714764 | 24 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.2129257591 | 91.5 | 0.003147297803583138 | 25 |
| UNITED_KINGDOM | United Kingdom Equities | 46.2334104698 | 46.36 | 0.0027380530424570004 | 26 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.7729425256 | 106.9 | 0.0011899782041648876 | 27 |
| LARGE_GROWTH | US Large-Cap Growth | 121.4657090499 | 121.59 | 0.0010232595773096431 | 28 |
| ENERGY | Energy Sector | 56.7162132943 | 56.74 | 0.00041939869251450546 | 29 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 30 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.064498327 | 116.04 | -0.00021107511214124575 | 31 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.571295669 | 79.52 | -0.0006446504178262424 | 32 |
| MID_CAP | US Mid-Cap Stocks | 75.3126469354 | 75.24 | -0.0009646047291673732 | 33 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.6783560972 | 84.59 | -0.0010434318906542561 | 34 |
| COMMUNICATIONS | Communication Services Sector | 111.8230755158 | 111.59 | -0.002084323961980994 | 35 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 235.8774690969 | 235.05 | -0.003508046360121253 | 36 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.0692624408 | 47.89 | -0.0037292529924038975 | 37 |
| EMERGING_MARKETS | Emerging Markets | 59.0310317056 | 58.79 | -0.004083135575235652 | 38 |
| EUROPE | Europe Equities | 88.2610219618 | 87.86 | -0.004543590736730496 | 39 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.870884774 | 95.38 | -0.005120269570445646 | 40 |
| TAIWAN | Taiwan Equities | 102.45 | 101.88 | -0.005563689604685229 | 41 |
| TIPS | Treasury Inflation-Protected Securities | 108.5383738933 | 107.91 | -0.005789416874051767 | 42 |
| NASDAQ100 | Nasdaq 100 | 716.3303427461 | 711.74 | -0.006408136682445442 | 43 |
| AUSTRALIA | Australia Equities | 28.5557691252 | 28.35 | -0.0072058687790136355 | 44 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.0289444917 | 93.29 | -0.007858691764483505 | 45 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.5491470018 | 97.71 | -0.008515010300238046 | 46 |
| MATERIALS | Materials Sector | 51.0289695629 | 50.58 | -0.008798327043358922 | 47 |
| TECHNOLOGY | Technology Sector | 182.992943608 | 181.28 | -0.009360708529118966 | 48 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.1821183947 | 93.26 | -0.00979080116711284 | 49 |
| MOMENTUM | US Momentum Equities | 318.6680033173 | 314.63 | -0.012671505376331549 | 50 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.6976330754 | 106.96 | -0.015985932961343097 | 51 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.9399467857 | 69.76 | -0.016633037367006498 | 52 |
| EURO | Euro | 106.808658533 | 105.01000213623047 | -0.016839986771426507 | 53 |
| YEN | Japanese Yen | 57.43 | 56.459999084472656 | -0.01689014305288772 | 54 |
| BROAD_COMMODITIES | Broad Commodities | 17.24 | 16.9 | -0.019721577726218076 | 55 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.661444001 | 83.97 | -0.019745686297096054 | 56 |
| BITCOIN_ETF | Bitcoin ETF | 36.05 | 35.220001220703125 | -0.02302354450199373 | 57 |
| COPPER | Copper | 38.94 | 37.94 | -0.0256805341551104 | 58 |
| CHINA | China Equities | 53.9849211345 | 52.53 | -0.026950509585355387 | 59 |
| MEXICO | Mexico Equities | 76.2246334446 | 74.15 | -0.027217362037009196 | 60 |
| SOUTH_AFRICA | South Africa Equities | 64.9059332499 | 62.76 | -0.033062204677618 | 61 |
| SEMICONDUCTORS | Semiconductors | 609.45 | 585.62 | -0.03910082861596531 | 62 |
| BROAD_AI_TECH | Broad AI Technology | 63.9495499035 | 61.3 | -0.04143187727666853 | 63 |
| GOLD | Gold | 79.13 | 75.25 | -0.049033236446354045 | 64 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 130.24 | 120.7 | -0.07324938574938578 | 65 |
| OIL | Crude Oil | 128.83 | 117.79000091552734 | -0.08569431874930267 | 66 |
| METALS_MINING | Metals and Mining | 118.2677145345 | 102.09 | -0.13678893346485343 | 67 |
| SILVER | Silver | 60.82 | 52.16 | -0.14238737257481093 | 68 |
| SOLAR | Solar Energy | 62.3 | 53.12 | -0.14735152487961478 | 69 |
| SOUTH_KOREA | South Korea Equities | 198.94 | 168.02 | -0.155423745853021 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 30.0 | -0.03910082861596531 | -0.011730248584789592 | Strongest momentum theme (64.8% 6m) backed by AI capex cycle and strong manufacturing PMI; recent 7d pullback offers entry. |
| anthropic-claude-fable-5 | SOUTH_KOREA | 15.0 | -0.155423745853021 | -0.023313561877953148 | Powerful momentum (11.4% 30d, 114% 6m) tied to semiconductor cycle and domestic reform rally. |
| anthropic-claude-fable-5 | TAIWAN | 10.0 | -0.005563689604685229 | -0.000556368960468523 | Semiconductor supply-chain leverage with strong 30d momentum. |
| anthropic-claude-fable-5 | MOMENTUM | 20.0 | -0.012671505376331549 | -0.0025343010752663098 | Broad momentum factor leading US factors (5.2% 30d, 25% 6m) in a trending market. |
| anthropic-claude-fable-5 | ENERGY | 25.0 | 0.00041939869251450546 | 0.00010484967312862636 | WTI at $95 with strong oil momentum and sticky headline inflation; energy equities lag spot oil's 6m run, offering catch-up and inflation hedge. |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | -0.03910082861596531 | -0.011730248584789592 | Strong momentum, AI capex tailwind, leading semis cycle continues. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 20.0 | -0.003508046360121253 | -0.0007016092720242506 | Defensive cyclical with strong momentum, geopolitical tailwinds, low drawdown risk. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 20.0 | 0.0520857196878608 | 0.01041714393757216 | Defensive sector with positive 30d momentum amid sticky inflation and softening sentiment. |
| anthropic-claude-opus-4-7 | EQUAL_WEIGHT_SP500 | 20.0 | 0.025306104219267267 | 0.005061220843853454 | Broadening rally beneficiary; less mega-cap concentration risk into FOMC. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 10.0 | 0.003147297803583138 | 0.0003147297803583138 | Yield buffer ~3.6% annualized with zero duration risk into hot CPI/FOMC. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 25.0 | 0.0520857196878608 | 0.0130214299219652 | Defensive sector with strong recent momentum (+5.65% 30d), low valuation, and resilience amid sticky inflation/elevated rates. |
| anthropic-claude-opus-4-8 | AEROSPACE_DEFENSE | 20.0 | -0.003508046360121253 | -0.0007016092720242506 | Strong trend (+4.73% 30d), geopolitical tailwinds, and low rate sensitivity; durable orders support continuation. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 20.0 | -0.03910082861596531 | -0.007820165723193063 | Leading momentum group (+8.59% 30d, +133% 1y) with AI capex tailwinds; high-beta growth engine. |
| anthropic-claude-opus-4-8 | DIVIDEND | 20.0 | 0.008889844237295996 | 0.0017779688474591994 | Quality dividend tilt provides defensive ballast with positive momentum (+2.42% 30d) into a hawkish-leaning macro window. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 15.0 | 0.003147297803583138 | 0.00047209467053747065 | Positive carry cash-like buffer given rich 21x forward P/E, hot PPI/CPI YoY, and elevated 10Y at 4.55%. |
| google-gemini-3-1-pro | TECHNOLOGY | 30.0 | -0.009360708529118966 | -0.0028082125587356897 | Strong earnings growth estimates and momentum in the tech sector. |
| google-gemini-3-1-pro | ENERGY | 30.0 | 0.00041939869251450546 | 0.00012581960775435164 | High crude oil prices provide a tailwind for energy equities. |
| google-gemini-3-1-pro | SP500 | 40.0 | 0.01805425926650961 | 0.007221703706603844 | Core broad market exposure to balance sector bets. |
| openai-gpt-5-5 | SEMICONDUCTORS | 35.0 | -0.03910082861596531 | -0.013685290015587858 | Strongest structural and price momentum in the universe, with large AI-related exposure and a sharp 6-month/1-year leadership profile despite the recent one-week pullback. |
| openai-gpt-5-5 | CYBERSECURITY | 20.0 | 0.07545512695919854 | 0.015091025391839707 | Best 30-day trailing return among thematic technology options, suggesting near-term relative strength that can persist over the one-month window. |
| openai-gpt-5-5 | REGIONAL_BANKS | 20.0 | 0.044296471861057674 | 0.008859294372211534 | Recent outperformance, improving risk appetite, and a positively sloped 10-year/2-year curve support a short-window cyclical financial rebound. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 15.0 | -0.003508046360121253 | -0.0005262069540181879 | Positive 7-day and 30-day momentum with less direct sensitivity to consumer weakness, supported by durable defense and aerospace demand themes. |
| openai-gpt-5-5 | SOUTH_KOREA | 10.0 | -0.155423745853021 | -0.0155423745853021 | Very strong 30-day and longer-term momentum, with semiconductor/export sensitivity that complements the AI and chip cycle exposure. |
| xai-grok-4-3 | ENERGY | 35.0 | 0.00041939869251450546 | 0.0001467895423800769 | WTI at $95 and Brent at $97 with upward momentum support sector returns over the window. |
| xai-grok-4-3 | FINANCIALS | 30.0 | 0.06927669585288254 | 0.020783008755864762 | Higher policy rates and stable money market assets favor bank and financial sector positioning. |
| xai-grok-4-3 | HEALTHCARE | 35.0 | 0.0520857196878608 | 0.018230001890751277 | Recent 30-day outperformance and defensive characteristics amid elevated inflation and low GDP growth. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | ENERGY | 3 | 0.55 | 0.00041939869251450546 | 0.03915980018899612 | 0.02110554092248651 | 0.13220579614945382 |  | True | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.55 | 0.0520857196878608 | 0.0067497184447445555 | -0.011304540821765054 | 0.16461587789370538 |  | False | True |
| google-gemini-3-1-pro | SP500 | 3 | 0.7 | 0.01805425926650961 | 0.004539310755622507 | -0.013514948510887102 | 0.16682628558282744 |  | False | True |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | -0.03910082861596531 | 0.0033612367049700854 | -0.014693022561539523 | 0.16800435963347987 |  | False | True |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.56 | -0.03910082861596531 | -0.005803551790856905 | -0.023857811057366514 | 0.17716914812930684 |  | False | False |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 5 | 0.45 | -0.03910082861596531 | -0.03802963082534895 | -0.05608389009185856 | 0.20939522716379888 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | -0.05608389009185856 | 0.4764 | -0.11772437046989623 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | d02a439ecb68ccb43fbcc2207dff682efb0c4d9c72048bdbd2f96a1f3d430e5b |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 0e5a222ebba001788946308d0e0b4c71b9e1bdc4f2882aad00ed1514ecaa5c5f |
| manifest.yaml | 8d88898cdf51893a95c73f66a4b90eced07fe91070fbf3c5c0ab009bf2af7306 |
| market_data/universe_trailing_returns.csv | 7605b83022b18918fba99923217333f9d36991cf866af8347e7e377cd217e82f |
| market_data/universe_trailing_returns.md | f5e961d9b96ebcd8e524ea71d7922b4d5b3c40fdad0c8a71160bf77e5386c427 |
| market_data/universe_trailing_returns.json | aa80a9d11cd86dfdcc4b7426b4687748f023280b9be19f0da21b4c6054d19f47 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 73df571f7a825d68cc8d673f51e94bf38118986838149f4e0c8b6adc9881cf7a | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 07a29d43d86d782833393b1dd5a60fbd5c30c8c8887865df8b0954e036e46b04 | yes |
| Final briefing | research/final_briefing.md | model-facing | d02a439ecb68ccb43fbcc2207dff682efb0c4d9c72048bdbd2f96a1f3d430e5b | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
