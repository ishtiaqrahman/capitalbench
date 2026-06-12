# CapitalBench Report: CB-2026-06-03-1W / official-20260603

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260603
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 3 2026 One-Week Portfolio Round
- Description: One-week CapitalBench portfolio evaluation round scored from the June 2, 2026 adjusted close to the June 9, 2026 adjusted close.
- Decision date: 2026-06-03
- Decision deadline: 2026-06-02T20:35:43Z
- Horizon: one week
- Entry date: 2026-06-02
- Exit date: 2026-06-09
- Entry rule: Use adjusted close on Tuesday, June 2, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Tuesday, June 9, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Concentrate in leading semiconductor and AI-technology momentum with an SP500 anchor to capture continued trend into the one-week exit close. | A hot or cold May jobs report on June 5 could trigger a sharp rates/growth repricing that disproportionately hits high-beta tech and semis.; Momentum reversal or factor rotation out of crowded AI/semiconductor trades after extended 30-day runs (SMH +24%, TECH +22%).; Concentration in one correlated theme amplifies drawdown if mega-cap tech sentiment cracks within the week.; Sticky inflation prints (CPI 3.8% YoY, PPI 6% YoY) and elevated forward P/E of 25.9 leave little valuation cushion for growth names. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Concentrated in leading momentum themes (semis, cybersecurity, tech, momentum factor) with a gold hedge against sticky inflation risk ahead of May payrolls Friday. | Hot May payrolls June 5 could spike yields and hit high-multiple tech; Crowded momentum trade vulnerable to factor reversal; Oil at $93+ and PPI 6% YoY signal inflation reacceleration pressuring growth multiples; Consumer sentiment collapse (44.8) could trigger broader risk-off |
| xai-grok-4-3 | xai | portfolio | TECHNOLOGY | 5 | 0.65 | Focus on sectors with recent strength and supportive macro prints to maximize expected close-to-close return versus SP500. | Weaker-than-expected May employment report on June 5 could trigger broad risk-off rotation; Hotter ISM Services PMI on June 3 may reinforce inflation concerns and pressure valuations; Profit-taking after strong trailing tech returns could lead to short-term reversal |
| google-gemini-3-1-pro | google | portfolio | CYBERSECURITY | 5 | 0.75 | Overweighting high-momentum tech and AI-adjacent themes to maximize short-term relative returns against the S&P 500. | A sudden reversal in technology and AI momentum could lead to significant underperformance relative to the broader market.; Higher-than-expected inflation or interest rate fears could disproportionately impact high-valuation growth stocks.; Geopolitical tensions in Asia could negatively impact South Korean equities and semiconductor supply chains. |
| openai-gpt-5-5 | openai | portfolio | CYBERSECURITY | 5 | 0.62 | I favor recent leaders with strong thematic and macro support over broad S&P 500 exposure. The allocation is high-beta and momentum-oriented to maximize one-week upside versus SPY. | A hotter-than-expected jobs or services release could push yields higher and trigger a sharp reversal in growth and technology stocks.; Recent extreme gains in cybersecurity, software, AI, and semiconductors could invite profit-taking during the one-week window.; A risk-off move or volatility spike would likely hurt this concentrated high-beta portfolio more than the S&P 500.; Metals and mining could underperform if the dollar strengthens, commodity prices reverse, or industrial-demand expectations weaken. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| HEALTHCARE | Healthcare Sector | 146.4 | 154.57 | 0.05580601092896176 | 1 |
| REAL_ESTATE | Real Estate Sector | 43.49 | 44.97 | 0.034030811680846096 | 2 |
| BIOTECH | Biotechnology | 127.76 | 131.38 | 0.02833437695679386 | 3 |
| LOW_VOL | US Low Volatility Equities | 71.64 | 73.64 | 0.027917364600781758 | 4 |
| CONSUMER_STAPLES | Consumer Staples Sector | 81.83 | 84.1 | 0.027740437492362213 | 5 |
| REGIONAL_BANKS | Regional Banks | 69.54 | 71.24 | 0.02444636180615456 | 6 |
| FINANCIALS | Financials Sector | 51.46 | 52.46 | 0.019432568985619847 | 7 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 228.33 | 230.45 | 0.009284807077475588 | 8 |
| US_DOLLAR | US Dollar | 27.76 | 28.01 | 0.009005763688760826 | 9 |
| INDUSTRIALS | Industrials Sector | 174.19 | 175.6 | 0.008094609334634573 | 10 |
| UTILITIES | Utilities Sector | 43.9 | 43.98 | 0.0018223234624146212 | 11 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.39 | 91.46 | 0.0007659481343691432 | 12 |
| DIVIDEND | US Dividend Equities | 32.37 | 32.39 | 0.0006178560395428967 | 13 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 14 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.1 | 107.04 | -0.0005602240896357413 | 15 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.71 | 98.37 | -0.0034444331881267054 | 16 |
| YEN | Japanese Yen | 57.43 | 57.23 | -0.0034825004353126188 | 17 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.9 | 79.62 | -0.0035043804755945374 | 18 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 210.04 | 209.19 | -0.004046848219386723 | 19 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.2 | 47.99 | -0.00435684647302903 | 20 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.33 | 93.89 | -0.0046644757765291756 | 21 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.92 | 108.41 | -0.00468233565919951 | 22 |
| LARGE_VALUE | US Large-Cap Value | 239.32 | 238.17 | -0.004805281631288683 | 23 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.24 | 93.78 | -0.0048811544991510525 | 24 |
| TIPS | Treasury Inflation-Protected Securities | 109.97 | 109.32 | -0.005910702918977995 | 25 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.26 | 95.67 | -0.00612923332640769 | 26 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.65 | 85.12 | -0.0061879743140689225 | 27 |
| MID_CAP | US Mid-Cap Stocks | 75.22 | 74.73 | -0.006514224940175395 | 28 |
| EURO | Euro | 107.26 | 106.53 | -0.006805892224501231 | 29 |
| ENERGY | Energy Sector | 57.96 | 57.39 | -0.009834368530020732 | 30 |
| INDIA | India Equities | 48.03 | 47.54 | -0.010201957110139492 | 31 |
| EUROPE | Europe Equities | 88.96 | 87.88 | -0.012140287769784153 | 32 |
| SMALL_VALUE | US Small-Cap Value | 215.0 | 212.17 | -0.013162790697674454 | 33 |
| UNITED_KINGDOM | United Kingdom Equities | 46.93 | 46.28 | -0.013850415512465353 | 34 |
| MATERIALS | Materials Sector | 51.52 | 50.77 | -0.014557453416149113 | 35 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.59 | 115.87 | -0.014627094140658214 | 36 |
| COMMUNICATIONS | Communication Services Sector | 113.57 | 111.48 | -0.018402747204367298 | 37 |
| SMALL_CAP | US Small-Cap Stocks | 291.66 | 285.02 | -0.022766234656792284 | 38 |
| CANADA | Canada Equities | 59.46 | 58.03 | -0.024049781365623968 | 39 |
| JAPAN | Japan Equities | 93.58 | 90.95 | -0.02810429578969864 | 40 |
| TOTAL_US_MARKET | Total US Stock Market | 374.36 | 363.67 | -0.02855540121807887 | 41 |
| SP500 | S&P 500 | 759.57 | 737.05 | -0.029648353673789263 | 42 |
| AGRICULTURE | Agriculture Commodities | 27.12 | 26.28 | -0.030973451327433676 | 43 |
| BROAD_COMMODITIES | Broad Commodities | 17.98 | 17.38 | -0.033370411568409475 | 44 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.32 | 69.84 | -0.03429203539823 | 45 |
| AUSTRALIA | Australia Equities | 29.47 | 28.25 | -0.04139803189684421 | 46 |
| OIL | Crude Oil | 137.27 | 131.3 | -0.043490930283383133 | 47 |
| MOMENTUM | US Momentum Equities | 326.03 | 311.63 | -0.04416771462748825 | 48 |
| EMERGING_MARKETS | Emerging Markets | 61.19 | 58.45 | -0.0447785585880045 | 49 |
| LARGE_GROWTH | US Large-Cap Growth | 128.29 | 122.02 | -0.04887364564658192 | 50 |
| COPPER | Copper | 40.6 | 38.6 | -0.049261083743842415 | 51 |
| SOUTH_AFRICA | South Africa Equities | 68.55 | 65.09 | -0.05047410649161188 | 52 |
| CHINA | China Equities | 57.19 | 54.3 | -0.05053331001923411 | 53 |
| NASDAQ100 | Nasdaq 100 | 746.16 | 707.83 | -0.05136967942532422 | 54 |
| GOLD | Gold | 84.42 | 80.07 | -0.051528073916133676 | 55 |
| BRAZIL | Brazil Equities | 35.78 | 33.92 | -0.05198434879821123 | 56 |
| MEXICO | Mexico Equities | 79.08 | 74.76 | -0.054628224582701 | 57 |
| TAIWAN | Taiwan Equities | 107.11 | 100.8 | -0.05891139949584545 | 58 |
| SEMICONDUCTORS | Semiconductors | 632.21 | 591.01 | -0.06516821942076212 | 59 |
| BITCOIN_ETF | Bitcoin ETF | 38.05 | 35.14 | -0.07647831800262805 | 60 |
| TECHNOLOGY | Technology Sector | 198.21 | 180.77 | -0.08798748801775891 | 61 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 141.85 | 128.87 | -0.09150511103278103 | 62 |
| BROAD_AI_TECH | Broad AI Technology | 70.14 | 63.16 | -0.09951525520387805 | 63 |
| CYBERSECURITY | Cybersecurity | 94.32 | 84.34 | -0.10581000848176414 | 64 |
| SOFTWARE | Software | 104.73 | 92.95 | -0.11247970972978139 | 65 |
| METALS_MINING | Metals and Mining | 132.83 | 116.1 | -0.12595046299781687 | 66 |
| SILVER | Silver | 67.99 | 59.01 | -0.1320782468010001 | 67 |
| ETHEREUM_ETF | Ethereum ETF | 14.38 | 12.48 | -0.13212795549374134 | 68 |
| SOUTH_KOREA | South Korea Equities | 214.53 | 184.05 | -0.14207803104460914 | 69 |
| SOLAR | Solar Energy | 72.27 | 61.83 | -0.14445828144458284 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 35.0 | -0.06516821942076212 | -0.02280887679726674 | Strong momentum, AI capex acceleration, SIA Q1 sales +25% QoQ, Taiwan/Korea strength corroborates. |
| anthropic-claude-opus-4-7 | CYBERSECURITY | 25.0 | -0.10581000848176414 | -0.026452502120441035 | Best trailing momentum (+11.65% 7d, +37% 30d) with strong secular AI security spend tailwind. |
| anthropic-claude-opus-4-7 | TECHNOLOGY | 20.0 | -0.08798748801775891 | -0.01759749760355178 | Broad tech leadership intact; ISM new orders strong, AI spending forecast +47% YoY. |
| anthropic-claude-opus-4-7 | MOMENTUM | 15.0 | -0.04416771462748825 | -0.006625157194123238 | Factor riding tech/semis leadership; low VIX 16 supports trend persistence. |
| anthropic-claude-opus-4-7 | GOLD | 5.0 | -0.051528073916133676 | -0.002576403695806684 | Hedge against sticky inflation (CPI 3.8%, PPI 6.0%) and weak dollar. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | -0.06516821942076212 | -0.019550465826228634 | Strongest momentum group with SIA Q1 sales +25% QoQ and AI capex surge; semis leading market with persistent trend into the scoring week. |
| anthropic-claude-opus-4-8 | TECHNOLOGY | 25.0 | -0.08798748801775891 | -0.021996872004439727 | Tech sector showed dominant 7% weekly momentum backed by AI spending forecasts; mega-cap leadership likely to persist short-term. |
| anthropic-claude-opus-4-8 | BROAD_AI_TECH | 20.0 | -0.09951525520387805 | -0.01990305104077561 | Broad AI exposure with strong trend persistence and Gartner $2.59T 2026 AI spend tailwind diversifies single-name semi risk. |
| anthropic-claude-opus-4-8 | SP500 | 15.0 | -0.029648353673789263 | -0.004447253051068389 | Benchmark-anchoring core position to limit tracking error against SPY while still capturing broad equity drift in a low-VIX regime. |
| anthropic-claude-opus-4-8 | TAIWAN | 10.0 | -0.05891139949584545 | -0.005891139949584546 | Semiconductor supply-chain leverage with strong momentum; reinforces the AI/chip theme via export-driven country exposure. |
| google-gemini-3-1-pro | CYBERSECURITY | 25.0 | -0.10581000848176414 | -0.026452502120441035 | Cybersecurity shows exceptional short-term momentum with an 11.65% 7-day return and strong AI-driven spending forecasts. |
| google-gemini-3-1-pro | SOFTWARE | 25.0 | -0.11247970972978139 | -0.028119927432445346 | Software exhibits strong momentum with an 11.36% 7-day return, supported by robust PCE software spending data. |
| google-gemini-3-1-pro | BROAD_AI_TECH | 20.0 | -0.09951525520387805 | -0.01990305104077561 | Broad AI tech captures the ongoing AI infrastructure build-out, supported by strong 7-day returns and massive projected AI spending. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 20.0 | -0.06516821942076212 | -0.013033643884152424 | Semiconductors continue to benefit from AI demand, with global sales up 25% QoQ and strong recent price momentum. |
| google-gemini-3-1-pro | SOUTH_KOREA | 10.0 | -0.14207803104460914 | -0.014207803104460915 | South Korean equities are highly correlated with global semiconductor demand and show strong recent outperformance. |
| openai-gpt-5-5 | CYBERSECURITY | 25.0 | -0.10581000848176414 | -0.026452502120441035 | Strongest near-term price momentum in the universe, supported by rising AI-related cybersecurity spending forecasts and continued technology risk appetite. |
| openai-gpt-5-5 | SOFTWARE | 25.0 | -0.11247970972978139 | -0.028119927432445346 | Very strong 7-day and 30-day momentum, with briefing evidence of unusually strong software-price/spending dynamics that may sustain short-horizon flows. |
| openai-gpt-5-5 | BROAD_AI_TECH | 20.0 | -0.09951525520387805 | -0.01990305104077561 | Broad AI exposure benefits from large 2026 AI spending forecasts and recent leadership in growth technology over the scoring-relevant window. |
| openai-gpt-5-5 | SEMICONDUCTORS | 15.0 | -0.06516821942076212 | -0.009775232913114317 | Semiconductor sales showed major sequential growth, and the group remains central to AI infrastructure momentum. |
| openai-gpt-5-5 | METALS_MINING | 15.0 | -0.12595046299781687 | -0.01889256944967253 | Strong recent performance, high commodity inflation backdrop, and supportive base-metals price forecasts provide diversification away from pure software/AI exposure. |
| xai-grok-4-3 | TECHNOLOGY | 30.0 | -0.08798748801775891 | -0.026396246405327672 | Strong recent momentum and positive manufacturing PMI/ durable goods data support continued tech outperformance over one week. |
| xai-grok-4-3 | SEMICONDUCTORS | 25.0 | -0.06516821942076212 | -0.01629205485519053 | Semiconductor sales growth and AI infrastructure forecasts provide near-term catalyst support ahead of employment data. |
| xai-grok-4-3 | SOFTWARE | 20.0 | -0.11247970972978139 | -0.022495941945956277 | Elevated software spending trends and trailing outperformance position for continuation in short window. |
| xai-grok-4-3 | MOMENTUM | 15.0 | -0.04416771462748825 | -0.006625157194123238 | Factor has shown resilience and aligns with growth-oriented rotation observed in recent returns. |
| xai-grok-4-3 | BROAD_AI_TECH | 10.0 | -0.09951525520387805 | -0.009951525520387805 | AI spending projections and sector breadth add targeted exposure without over-concentration. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.55 | -0.06516821942076212 | -0.07178878187209689 | -0.04214042819830763 | 0.12759479280105865 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | -0.06516821942076212 | -0.07606043741118948 | -0.04641208373740022 | 0.13186644834015124 |  | False | False |
| xai-grok-4-3 | TECHNOLOGY | 5 | 0.65 | -0.08798748801775891 | -0.08176092592098552 | -0.05211257224719626 | 0.13756693684994728 |  | False | False |
| google-gemini-3-1-pro | CYBERSECURITY | 5 | 0.75 | -0.10581000848176414 | -0.10171692758227534 | -0.07206857390848607 | 0.1575229385112371 |  | False | False |
| openai-gpt-5-5 | CYBERSECURITY | 5 | 0.62 | -0.10581000848176414 | -0.10314328295644884 | -0.07349492928265958 | 0.1589492938854106 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 553004f2adbf82c643f012ee1c732df75a5ed71ac25cfa4cd0a148f374dee88c |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 29bcc94b677b8d749c2f807b79033b2524c83629237985ad667cb31fa57d6b22 |
| manifest.yaml | e3daa07082df8c094d2dca8349419070693c0c2eb7f8c6a4c54caafe46452656 |
| market_data/universe_trailing_returns.csv | a7180a919bd853daed2339277216dc47363db315f5f605db6249f579cadac231 |
| market_data/universe_trailing_returns.md | 3dc1d1e61569822680f7bae786dcd2b823da69bcefd1c33f51e3fb4ca1f0064e |
| market_data/universe_trailing_returns.json | 864ff8570161f17c431dea63710145879d06e0306604eb1f2d977a4e144b356d |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 7842a0b151480a3f5ab4503e428fe4bc948ac207b38e6ce9d80edfba88f7b6e2 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 1d3ca6688d7346d4ef12120216b621f969749a6dface07091a92a7cb738f52a5 | yes |
| Final briefing | research/final_briefing.md | model-facing | 553004f2adbf82c643f012ee1c732df75a5ed71ac25cfa4cd0a148f374dee88c | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
