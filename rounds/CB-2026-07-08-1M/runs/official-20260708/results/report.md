# CapitalBench Report: CB-2026-07-08-1M / official-20260708

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260708
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-08-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-08
- Decision deadline: 2026-07-09T07:30:00Z
- Horizon: one month
- Entry date: 2026-07-08
- Exit date: 2026-08-07
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | LARGE_VALUE | 5 | 0.55 | Weak jobs data and elevated inflation point to value and defensive sectors outperforming into FOMC and CPI releases. | Hotter-than-expected CPI on July 14 could pressure rate-sensitive holdings.; FOMC July 29 statement may signal persistent hawkishness.; Geopolitical de-escalation in Middle East could reverse oil gains. |
| google-gemini-3-1-pro | google | portfolio | ENERGY | 4 | 0.65 | Allocating to energy and oil to capitalize on geopolitical catalysts, while using healthcare and short treasuries for defensive stability. | A sudden resolution to geopolitical tensions could cause a sharp reversal in oil and energy prices.; Higher-than-expected inflation data could lead to a broader market sell-off, impacting the healthcare allocation.; A stronger US dollar could weigh on commodity prices, including oil. |
| anthropic-claude-fable-5 | anthropic | portfolio | HEALTHCARE | 5 | 0.5 | Value/defensive/energy tilt versus SPY given hawkish Fed minutes, rising oil, and yields near 4.6%, with financials earnings catalysts and biotech momentum. | Iran truce holds and oil retraces sharply, hurting the energy allocation; Cool July 14 CPI sparks a growth/mega-cap tech rally that this value-tilted portfolio underperforms; Bank earnings disappoint on credit costs or guidance, hitting financials and value; Biotech momentum reverses after a 27% 30-day run; Fed turns more hawkish at July 29 meeting, pressuring all equity holdings |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.6 | Barbell of defensives (healthcare, low-vol, utilities) with financials for earnings catalyst and cybersecurity as resilient tech exposure. | Tech mega-cap rally resumes on Q2 earnings (TSMC, Tesla) pushing SPY higher via QQQ leadership; Hot CPI July 14 could hurt low-beta/defensives via rate spike; Bank earnings disappoint on credit or NII guidance; FOMC July 29 more hawkish than expected pressures rate-sensitive utilities/healthcare |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 5 | 0.6 | Overweight financials, healthcare, low-vol, utilities, and defense for resilient alpha in a choppy, late-cycle macro backdrop. | A tech/semiconductor rally (TSMC July 16, Fed pause optimism) could drive SPX outperformance led by names underweighted here.; Hot July 14 CPI could pressure rate-sensitive utilities and low-vol, and derail defensive leadership.; Bank earnings July 14 disappoint on credit/NIM, reversing financials momentum.; Easing Iran tensions could unwind the aerospace/defense geopolitical premium. |
| xai-grok-4-5 | xai | portfolio | BIOTECH | 5 | 0.42 | Prioritize momentum and sector strength with near-term catalysts over broad beta or bonds; biotech leads for upside capture, balanced by healthcare/value and energy/financials exposure. | Biotech sharp mean-reversion after extreme 30d gains; Oil/energy pullback if Iran truce stabilizes or demand softens; Hawkish FOMC (July 29) or hot CPI (July 14) pressuring equities; Soft payrolls/revisions signaling growth scare that hits cyclicals and financials |
| openai-gpt-5-5 | openai | portfolio | BIOTECH | 5 | 0.56 | I favor a concentrated pro-catalyst allocation with biotech and semiconductors as the main alpha engines, balanced by healthcare and financials, plus a small oil position for geopolitical upside. The mix seeks to outperform if sector rotation and event-driven momentum continue through August 7. | A hot CPI print or hawkish July FOMC communication could lift yields and trigger a broad high-beta equity selloff, hurting biotech and semiconductors.; Biotech's 27% 30-day rally could reverse sharply if momentum fades or investors take profits near 52-week highs.; TSMC results or AI supply-chain commentary could disappoint, pressuring semiconductors after their large 6-month and 1-year gains.; Bank earnings could reveal weaker credit quality, deposit pressure, or loan demand, causing financials to underperform.; A durable Iran truce or oil demand concerns could unwind the recent crude spike and drag down the oil allocation. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| METALS_MINING | Metals and Mining | 101.94 | 115.74 | 0.13537374926427304 | 1 |
| SOUTH_AFRICA | South Africa Equities | 62.69 | 69.65 | 0.11102249162545874 | 2 |
| SOFTWARE | Software | 92.48 | 102.69 | 0.11040224913494812 | 3 |
| ETHEREUM_ETF | Ethereum ETF | 13.11 | 14.47 | 0.10373760488176975 | 4 |
| SILVER | Silver | 52.83 | 57.5 | 0.08839674427408672 | 5 |
| AUSTRALIA | Australia Equities | 28.12 | 30.41 | 0.08143669985775248 | 6 |
| COPPER | Copper | 37.07 | 39.9 | 0.07634205557054208 | 7 |
| CHINA | China Equities | 52.85 | 56.57 | 0.07038789025544001 | 8 |
| CYBERSECURITY | Cybersecurity | 91.66 | 97.85 | 0.06753218415884787 | 9 |
| GOLD | Gold | 76.74 | 81.68 | 0.064373208235601 | 10 |
| CANADA | Canada Equities | 57.97 | 61.3 | 0.05744350526134201 | 11 |
| MATERIALS | Materials Sector | 50.16 | 52.86 | 0.053827751196172224 | 12 |
| OIL | Crude Oil | 112.21 | 117.98 | 0.05142144193922116 | 13 |
| LARGE_VALUE | US Large-Cap Value | 245.2 | 257.56 | 0.05040783034257745 | 14 |
| EUROPE | Europe Equities | 88.18 | 92.6 | 0.050124744840099655 | 15 |
| DIVIDEND | US Dividend Equities | 32.34 | 33.9 | 0.04823747680890533 | 16 |
| FINANCIALS | Financials Sector | 54.97 | 57.6 | 0.04784427869747132 | 17 |
| JAPAN | Japan Equities | 92.54 | 96.9 | 0.04711476118435276 | 18 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 239.63 | 250.75 | 0.04640487418102901 | 19 |
| UNITED_KINGDOM | United Kingdom Equities | 46.49 | 48.64 | 0.04624650462465052 | 20 |
| BITCOIN_ETF | Bitcoin ETF | 35.23 | 36.8 | 0.04456429179676413 | 21 |
| MID_CAP | US Mid-Cap Stocks | 74.73 | 77.79 | 0.04094741067844243 | 22 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.3 | 119.86 | 0.03954900260190808 | 23 |
| REGIONAL_BANKS | Regional Banks | 73.34 | 76.21 | 0.03913280610853542 | 24 |
| BROAD_COMMODITIES | Broad Commodities | 16.62 | 17.25 | 0.037906137184115396 | 25 |
| MEXICO | Mexico Equities | 74.71 | 77.52 | 0.0376121001204659 | 26 |
| SP500 | S&P 500 | 745.4 | 773.26 | 0.037375905554065 | 27 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.2 | 220.09 | 0.03718190386427911 | 28 |
| TOTAL_US_MARKET | Total US Stock Market | 368.25 | 381.78 | 0.03674134419551933 | 29 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.34 | 72.89 | 0.03625248791583724 | 30 |
| TECHNOLOGY | Technology Sector | 181.4 | 187.97 | 0.03621830209481813 | 31 |
| SMALL_VALUE | US Small-Cap Value | 217.68 | 225.52 | 0.03601617052554218 | 32 |
| INDIA | India Equities | 48.65 | 50.365 | 0.035251798561151126 | 33 |
| ENERGY | Energy Sector | 55.6 | 57.5 | 0.03417266187050361 | 34 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 123.81 | 127.85 | 0.032630643728293274 | 35 |
| YEN | Japanese Yen | 56.46 | 58.24 | 0.031526744597945466 | 36 |
| SMALL_CAP | US Small-Cap Stocks | 293.48 | 301.56 | 0.027531688701103896 | 37 |
| BRAZIL | Brazil Equities | 34.41 | 35.34 | 0.027027027027027195 | 38 |
| INDUSTRIALS | Industrials Sector | 180.42 | 185.18 | 0.026382884380889093 | 39 |
| LARGE_GROWTH | US Large-Cap Growth | 121.8 | 124.6 | 0.02298850574712641 | 40 |
| EMERGING_MARKETS | Emerging Markets | 59.17 | 60.47 | 0.021970593206016575 | 41 |
| HEALTHCARE | Healthcare Sector | 162.3 | 165.68 | 0.02082563154651873 | 42 |
| REAL_ESTATE | Real Estate Sector | 44.15 | 44.98 | 0.018799546998867545 | 43 |
| COMMUNICATIONS | Communication Services Sector | 109.46 | 111.25 | 0.01635300566416964 | 44 |
| NASDAQ100 | Nasdaq 100 | 711.44 | 723.03 | 0.016290902957382114 | 45 |
| BROAD_AI_TECH | Broad AI Technology | 62.57 | 63.35 | 0.012466038037398208 | 46 |
| EURO | Euro | 105.3678410656 | 106.68 | 0.012453125366620021 | 47 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.39 | 85.12 | 0.008650314018248562 | 48 |
| LOW_VOL | US Low Volatility Equities | 75.7193385661 | 76.21 | 0.006480001584689754 | 49 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.7118175089 | 47.95 | 0.0049921068518417044 | 50 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.2758763429 | 79.61 | 0.0042146952202051224 | 51 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.177772215 | 91.48 | 0.003314709031136953 | 52 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 53 |
| AGRICULTURE | Agriculture Commodities | 27.62 | 27.62 | 0.0 | 53 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.1911811422 | 93.17 | -0.00022728698081064813 | 55 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.3463581481 | 93.27 | -0.0008180088609225367 | 56 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.7009017274 | 97.6 | -0.0010327614752372316 | 57 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.3736895671 | 95.24 | -0.001401744733865562 | 58 |
| TIPS | Treasury Inflation-Protected Securities | 107.2626603539 | 107.08 | -0.0017029258205729647 | 59 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 107.2076934698 | 106.55 | -0.006134760001951567 | 60 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.6205240134 | 105.94 | -0.006382673689677931 | 61 |
| TAIWAN | Taiwan Equities | 103.9 | 103.09 | -0.007795957651588137 | 62 |
| US_DOLLAR | US Dollar | 28.36 | 28.07 | -0.010225669957686812 | 63 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.0221795193 | 82.76 | -0.015021980226186171 | 64 |
| SEMICONDUCTORS | Semiconductors | 593.0 | 582.7 | -0.01736930860033714 | 65 |
| MOMENTUM | US Momentum Equities | 314.85 | 309.32 | -0.01756391932666357 | 66 |
| SOLAR | Solar Energy | 54.14 | 52.75 | -0.02567417805688954 | 67 |
| BIOTECH | Biotechnology | 162.97 | 157.37 | -0.034362152543412905 | 68 |
| UTILITIES | Utilities Sector | 45.36 | 43.61 | -0.038580246913580196 | 69 |
| SOUTH_KOREA | South Korea Equities | 182.72 | 166.09 | -0.0910135726795096 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | HEALTHCARE | 25.0 | 0.02082563154651873 | 0.005206407886629683 | Defensive sector with strong recent breadth and positive relative momentum amid elevated inflation and rate risk. |
| anthropic-claude-fable-5 | LARGE_VALUE | 20.0 | 0.05040783034257745 | 0.010081566068515492 | Value leadership with lower beta into bank earnings and a hawkish Fed backdrop; strong 30d relative return. |
| anthropic-claude-fable-5 | FINANCIALS | 20.0 | 0.04784427869747132 | 0.009568855739494266 | JPM/WFC earnings catalysts July 14, benefits from higher yields and steady economy. |
| anthropic-claude-fable-5 | BIOTECH | 15.0 | -0.034362152543412905 | -0.005154322881511936 | Strong momentum (75% up days, near 52w high) driven by M&A/risk appetite; catalyst-rich industry. |
| anthropic-claude-fable-5 | ENERGY | 20.0 | 0.03417266187050361 | 0.006834532374100722 | Brent above $78 on Iran truce doubts; sector lagged oil's move and hedges geopolitical/inflation risk. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 30.0 | 0.02082563154651873 | 0.0062476894639556186 | Strong momentum (+6.8% 30d, +5.7% vs SPY), defensive with low beta 0.36, benefits from risk-off tone amid weak jobs and geopolitical stress. |
| anthropic-claude-opus-4-7 | FINANCIALS | 25.0 | 0.04784427869747132 | 0.01196106967436783 | JPM/WFC earnings July 14 catalyst, steeper curve with 10Y at 4.57%, strong 30d relative performance (+5% vs SPY). |
| anthropic-claude-opus-4-7 | LOW_VOL | 20.0 | 0.006480001584689754 | 0.001296000316937951 | Defensive tilt given VIX rising, weak payrolls (57k), hawkish Fed minutes, and geopolitical oil spike; low beta 0.06 with strong recent alpha. |
| anthropic-claude-opus-4-7 | UTILITIES | 15.0 | -0.038580246913580196 | -0.005787037037037029 | Defensive with AI power demand tailwind, +4.9% 30d, low beta 0.17 hedges against equity drawdown. |
| anthropic-claude-opus-4-7 | CYBERSECURITY | 10.0 | 0.06753218415884787 | 0.006753218415884788 | Best-performing tech sub-theme (+6.5% 30d), resilient budgets, near 52w highs with strong relative strength. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | 0.04784427869747132 | 0.01196106967436783 | Strong recent momentum (+6.1% 30d, +5.05% vs SPX), positive earnings catalysts July 14 (JPM/WFC), steady yield curve, defensive beta 0.66. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 25.0 | 0.02082563154651873 | 0.005206407886629683 | Defensive leadership with +6.8% 30d and +5.7% vs SPX, low beta 0.36, benefits if inflation stays elevated and growth softens. |
| anthropic-claude-opus-4-8 | LOW_VOL | 20.0 | 0.006480001584689754 | 0.001296000316937951 | Defensive factor with strong recent outperformance (+4.9% 30d) amid weakening payrolls and hawkish Fed minutes; low drawdown, high up-day share. |
| anthropic-claude-opus-4-8 | UTILITIES | 15.0 | -0.038580246913580196 | -0.005787037037037029 | Defensive, near-zero beta, +4.9% 30d, AI-driven electricity demand tailwind, resilient in choppy risk backdrop. |
| anthropic-claude-opus-4-8 | AEROSPACE_DEFENSE | 15.0 | 0.04640487418102901 | 0.006960731127154352 | Geopolitical tailwind from renewed Iran tensions, +5.5% 30d and +4.4% vs SPX, steady defense budgets. |
| google-gemini-3-1-pro | ENERGY | 30.0 | 0.03417266187050361 | 0.010251798561151082 | Oil prices are climbing due to geopolitical tensions, and the energy sector has shown strong recent momentum. |
| google-gemini-3-1-pro | OIL | 20.0 | 0.05142144193922116 | 0.010284288387844231 | Direct exposure to crude oil, which is rallying on renewed doubts about the Iran truce. |
| google-gemini-3-1-pro | HEALTHCARE | 25.0 | 0.02082563154651873 | 0.005206407886629683 | A defensive sector that has shown solid recent performance and can provide stability if inflation or geopolitical risks weigh on broader markets. |
| google-gemini-3-1-pro | SHORT_TREASURY | 25.0 | 0.003314709031136953 | 0.0008286772577842383 | Provides a safe haven and yield while mitigating downside risk from potential market volatility related to inflation and geopolitical events. |
| openai-gpt-5-5 | BIOTECH | 35.0 | -0.034362152543412905 | -0.012026753390194517 | Strongest near-term price momentum in the universe, near a 52-week high with broad up-day participation and healthcare-sector strength; potential continuation can outperform over a one-month window despite high volatility. |
| openai-gpt-5-5 | SEMICONDUCTORS | 25.0 | -0.01736930860033714 | -0.004342327150084285 | AI-related capacity demand and reported component shortages support semiconductor fundamentals, while TSMC sales and earnings arrive early in the scoring window and could catalyze a rebound after recent weakness. |
| openai-gpt-5-5 | HEALTHCARE | 15.0 | 0.02082563154651873 | 0.0031238447319778093 | Healthcare has strong recent relative performance with lower beta than the S&P 500, offering a defensive growth tilt if weak labor data or inflation uncertainty pressures broad equities. |
| openai-gpt-5-5 | FINANCIALS | 15.0 | 0.04784427869747132 | 0.007176641804620697 | Financials have shown strong recent relative performance, and major bank earnings on July 14 provide a near-term catalyst; higher long yields may support net interest income expectations. |
| openai-gpt-5-5 | OIL | 10.0 | 0.05142144193922116 | 0.005142144193922116 | Renewed Middle East truce doubts and a sharp Brent move above $78 create a short-window upside catalyst for crude after a deep 30-day drawdown. |
| xai-grok-4-3 | LARGE_VALUE | 30.0 | 0.05040783034257745 | 0.015122349102773235 | Recent outperformance and sensitivity to higher yields amid elevated inflation data. |
| xai-grok-4-3 | HEALTHCARE | 25.0 | 0.02082563154651873 | 0.005206407886629683 | Strong 30-day returns and defensive characteristics ahead of CPI and FOMC. |
| xai-grok-4-3 | FINANCIALS | 20.0 | 0.04784427869747132 | 0.009568855739494266 | Positive 30-day momentum and exposure to rate environment. |
| xai-grok-4-3 | INDUSTRIALS | 15.0 | 0.026382884380889093 | 0.003957432657133364 | Manufacturing PMI expansion supports sector over one-month window. |
| xai-grok-4-3 | ENERGY | 10.0 | 0.03417266187050361 | 0.003417266187050361 | Oil price strength from geopolitical factors likely to persist near term. |
| xai-grok-4-5 | BIOTECH | 35.0 | -0.034362152543412905 | -0.012026753390194517 | Extreme 30d momentum (+27%) near 52w highs with high up-day share; healthcare strength and risk appetite can extend into the window before any mean-reversion. |
| xai-grok-4-5 | HEALTHCARE | 20.0 | 0.02082563154651873 | 0.004165126309303747 | Strong 30d outperformance vs SPX with lower beta; defensive characteristics amid sticky inflation and soft labor data. |
| xai-grok-4-5 | FINANCIALS | 20.0 | 0.04784427869747132 | 0.009568855739494266 | Recent relative strength, higher yields supportive, and bank earnings catalysts (JPM/WFC July 14) within the scoring window. |
| xai-grok-4-5 | ENERGY | 15.0 | 0.03417266187050361 | 0.005125899280575541 | Oil spike on Iran truce doubts and geo risk; potential short-term catch-up after 30d underperformance. |
| xai-grok-4-5 | LARGE_VALUE | 10.0 | 0.05040783034257745 | 0.005040783034257746 | Value tilt with lower beta and positive 30d relative return; benefits from rates/inflation backdrop vs pure growth. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | LARGE_VALUE | 5 | 0.55 | 0.05040783034257745 | 0.03727231157308091 | -0.00010359398098409162 | 0.09810143769119212 |  | False | True |
| google-gemini-3-1-pro | ENERGY | 4 | 0.65 | 0.03417266187050361 | 0.026571172093409236 | -0.010804733460655767 | 0.1088025771708638 |  | False | True |
| anthropic-claude-fable-5 | HEALTHCARE | 5 | 0.5 | 0.02082563154651873 | 0.026537039187228224 | -0.010838866366836779 | 0.10883671007704482 |  | False | True |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.6 | 0.02082563154651873 | 0.020470940834109157 | -0.016904964719955846 | 0.11490280843016387 |  | False | True |
| anthropic-claude-opus-4-8 | FINANCIALS | 5 | 0.6 | 0.04784427869747132 | 0.019637171968052786 | -0.017738733586012218 | 0.11573657729622025 |  | False | True |
| xai-grok-4-5 | BIOTECH | 5 | 0.42 | -0.034362152543412905 | 0.011873910973436784 | -0.02550199458062822 | 0.12349983829083624 |  | False | True |
| openai-gpt-5-5 | BIOTECH | 5 | 0.56 | -0.034362152543412905 | -0.00092644980975818 | -0.03830235536382318 | 0.1363001990740312 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 0adb480c33866f5ccd57126b52c5cace9cd2f4960e4fb7c2846812993649b3bb |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 0e5a222ebba001788946308d0e0b4c71b9e1bdc4f2882aad00ed1514ecaa5c5f |
| manifest.yaml | 4eb33b174d0e09d93e2b28bfa80311cc5cd576621bc9738413d20a3928084130 |
| market_data/universe_trailing_returns.csv | abd122f011ccebe049bcfd9ca64fd746f017a27758135aa649f457d6ad116ed1 |
| market_data/universe_trailing_returns.md | 74765a42d67967459eaa2ebe43e18bb98ef3504031393e19e404961760a3f4f5 |
| market_data/universe_trailing_returns.json | 10d43adea0db4016787331de7d8e1b99253fd310637666657c4202f70ea15724 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 4e31081d10525d7c7e7137ce4bdc21597427a98d5e19bc3da2f23bc1763bbc1f | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | f038f1d0d8943fc5d3ba539209faa3a0cc556ac6f24f33744301c1237f27bfbd | yes |
| Final briefing | research/final_briefing.md | model-facing | 0adb480c33866f5ccd57126b52c5cace9cd2f4960e4fb7c2846812993649b3bb | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
