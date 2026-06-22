# CapitalBench Report: CB-2026-06-13-1W / official-20260613

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260613
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 13 2026 One-Week Portfolio Round
- Description: One-week CapitalBench portfolio evaluation round scored from the June 12, 2026 adjusted-close snapshot to the June 18, 2026 adjusted close, because June 19, 2026 was a U.S. market holiday.
- Decision date: 2026-06-13
- Decision deadline: 2026-06-13T23:30:00Z
- Horizon: one week
- Entry date: 2026-06-12
- Exit date: 2026-06-18
- Entry rule: Use adjusted close on Friday, June 12, 2026 as the post-close entry snapshot for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Thursday, June 18, 2026 for each selected option because Friday, June 19, 2026 was a U.S. market holiday; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.58 | Favor risk-on, momentum, and semiconductor-linked exposures over broad market beta. The allocation is intentionally aggressive because scoring rewards one-week realized return relative to the S&P 500 rather than risk-adjusted stability. | A hawkish FOMC statement or press conference could reverse the recent decline in yields and pressure high-multiple technology and crypto assets.; Semiconductors and Korea/Taiwan exposures are crowded after very strong trailing gains, creating risk of sharp profit-taking during the scoring week.; Weak retail sales, industrial production, or jobless claims data could trigger a broad risk-off move that hurts high-beta equities more than SPY.; Geopolitical or trade-related headlines affecting Taiwan, Korea, or chip supply chains could disproportionately hurt the portfolio.; Crypto momentum could reverse independently of equities due to ETF outflows, regulatory headlines, or liquidity-driven selling. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Lean into the strongest trending risk assets (semis, momentum, small caps) supported by disinflation and lower rates into the June FOMC. | Hawkish FOMC dot-plot or Powell tone on 6/17 could spike yields and hit growth/semis hardest; Momentum and semiconductor crowding makes the book vulnerable to a sharp factor reversal; Hot retail sales (6/17) or sticky energy CPI could reignite inflation fears; Concentration in high-beta tech and small caps amplifies any broad risk-off move |
| anthropic-claude-fable-5 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.5 | Momentum continuation in semis, Korea, and momentum factor plus small-value breadth, hedged with gold given safe-haven flows and FOMC event risk. | Hawkish FOMC dots or Powell commentary on 4.2% headline CPI could hit high-beta momentum names; Sharp reversal of crowded semiconductor/Korea trade after large recent gains; Gold spike fading if geopolitical stress de-escalates, dragging the hedge negative; Weak May retail sales (6/17) hurting small-cap value; Factor rotation away from momentum into laggards |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Disinflationary core CPI print plus dovish FOMC hold setup with falling yields supports growth, semis, small caps, and regional banks for the week. | Hawkish FOMC surprise on June 17 reversing yield decline; Semiconductor profit-taking after large run-up; Headline CPI re-acceleration via energy weighing on sentiment; Geopolitical shock to Taiwan exposure |
| xai-grok-4-3 | xai | portfolio | MOMENTUM | 3 | 0.55 | Recent inflation data and scheduled FOMC meeting favor selective equity exposure over broad benchmark; momentum and small caps show strongest near-term price action. | FOMC decision on June 17 could trigger volatility if hawkish on 4.2% CPI YoY; Hotter-than-expected retail sales on June 17 may pressure rate-sensitive small caps; BOJ meeting June 14-15 risks yen-driven global equity rotation away from US momentum |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.6 | Balanced portfolio with equity and short-duration fixed income. | Unexpected inflation data causing a spike in interest rates.; A sudden shift in market sentiment away from growth stocks.; Geopolitical events impacting global markets. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOUTH_KOREA | South Korea Equities | 197.4499969482 | 219.2 | 0.1101544866445654 | 1 |
| TAIWAN | Taiwan Equities | 102.6200027466 | 109.99 | 0.07181833030738427 | 2 |
| SEMICONDUCTORS | Semiconductors | 619.9600219727 | 659.88 | 0.06439121332416797 | 3 |
| BIOTECH | Biotechnology | 133.7899932861 | 140.72 | 0.05179764602484638 | 4 |
| BROAD_AI_TECH | Broad AI Technology | 64.0 | 66.8 | 0.043749999999999956 | 5 |
| MOMENTUM | US Momentum Equities | 324.3999938965 | 338.52 | 0.043526530114562645 | 6 |
| JAPAN | Japan Equities | 92.7099990845 | 96.26 | 0.038291456698908766 | 7 |
| TECHNOLOGY | Technology Sector | 184.8000030518 | 191.44 | 0.03593071882330423 | 8 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 129.4100036621 | 133.17 | 0.029054912537655575 | 9 |
| INDUSTRIALS | Industrials Sector | 176.1799926758 | 180.91 | 0.026847584974668326 | 10 |
| NASDAQ100 | Nasdaq 100 | 721.3400268555 | 740.62 | 0.02672799571173967 | 11 |
| INDIA | India Equities | 48.3300018311 | 49.58 | 0.02586381381214098 | 12 |
| ETHEREUM_ETF | Ethereum ETF | 12.5699996948 | 12.88 | 0.024661918275800998 | 13 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 233.7899932861 | 238.99 | 0.02224221251222036 | 14 |
| EMERGING_MARKETS | Emerging Markets | 59.5499992371 | 60.77 | 0.020486998799824185 | 15 |
| AGRICULTURE | Agriculture Commodities | 26.2399997711 | 26.63 | 0.01486281373102516 | 16 |
| LARGE_GROWTH | US Large-Cap Growth | 121.6100006104 | 123.19 | 0.012992347518045122 | 17 |
| US_DOLLAR | US Dollar | 27.9500007629 | 28.3 | 0.012522333722601475 | 18 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.7699966431 | 86.75 | 0.011425946079698601 | 19 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.5500030518 | 72.31 | 0.010621899591671369 | 20 |
| TOTAL_US_MARKET | Total US Stock Market | 366.3599853516 | 369.99 | 0.009908327310681031 | 21 |
| SMALL_CAP | US Small-Cap Stocks | 292.950012207 | 295.59 | 0.009011734708973318 | 22 |
| SP500 | S&P 500 | 741.75 | 746.74 | 0.006727334007414987 | 23 |
| UTILITIES | Utilities Sector | 44.5299987793 | 44.76 | 0.005165084819335641 | 24 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.5999984741 | 117.16 | 0.004802757574858596 | 25 |
| FINANCIALS | Financials Sector | 53.3400001526 | 53.57 | 0.0043119581316459765 | 26 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.3600006104 | 96.73 | 0.003839761179495804 | 27 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.0500030518 | 107.33 | 0.0026155716040896504 | 28 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.1800003052 | 94.36 | 0.0019112305608057767 | 29 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.2599983215 | 48.35 | 0.001864933311858552 | 30 |
| GOLD | Gold | 79.1900024414 | 79.33 | 0.001767869103219244 | 31 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.7600021362 | 98.9 | 0.0014175563059115603 | 32 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.3799972534 | 94.48 | 0.0010595756464317763 | 33 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.9400024414 | 80.01 | 0.000875626175409705 | 34 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.5100021362 | 91.57 | 0.0006556426882242672 | 35 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.0100021362 | 109.07 | 0.000550388612276409 | 36 |
| LARGE_VALUE | US Large-Cap Value | 242.1300048828 | 242.18 | 0.00020648046996152303 | 37 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 38 |
| SOUTH_AFRICA | South Africa Equities | 66.8700027466 | 66.74 | -0.0019441115785898688 | 39 |
| TIPS | Treasury Inflation-Protected Securities | 109.6100006104 | 109.39 | -0.0020071216966959238 | 40 |
| MID_CAP | US Mid-Cap Stocks | 76.0400009155 | 75.78 | -0.0034192650232728328 | 41 |
| SMALL_VALUE | US Small-Cap Value | 218.3300018311 | 216.87 | -0.006687133325036343 | 42 |
| MATERIALS | Materials Sector | 52.1800003052 | 51.81 | -0.007090845209579699 | 43 |
| YEN | Japanese Yen | 57.2599983215 | 56.85 | -0.007160292237487709 | 44 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 211.6499938965 | 209.96 | -0.007984852091828643 | 45 |
| CYBERSECURITY | Cybersecurity | 85.3300018311 | 84.54 | -0.009258195407797043 | 46 |
| EURO | Euro | 106.8300018311 | 105.77 | -0.00992232343846522 | 47 |
| BITCOIN_ETF | Bitcoin ETF | 36.0400009155 | 35.62 | -0.011653743197308608 | 48 |
| MEXICO | Mexico Equities | 78.4700012207 | 77.33 | -0.014527860366583933 | 49 |
| EUROPE | Europe Equities | 89.6200027466 | 88.27 | -0.015063632060100751 | 50 |
| CANADA | Canada Equities | 58.7599983215 | 57.87 | -0.015146329934021763 | 51 |
| COPPER | Copper | 39.5499992371 | 38.86 | -0.017446251590638395 | 52 |
| SOFTWARE | Software | 90.6999969482 | 89.09 | -0.017750793851949997 | 53 |
| LOW_VOL | US Low Volatility Equities | 74.4700012207 | 73.09 | -0.018530968149311655 | 54 |
| COMMUNICATIONS | Communication Services Sector | 111.6500015259 | 109.45 | -0.019704446895055794 | 55 |
| AUSTRALIA | Australia Equities | 29.2199993134 | 28.56 | -0.02258724602698159 | 56 |
| REGIONAL_BANKS | Regional Banks | 73.4100036621 | 71.72 | -0.023021435469189444 | 57 |
| METALS_MINING | Metals and Mining | 120.4400024414 | 117.02 | -0.028395901461925055 | 58 |
| HEALTHCARE | Healthcare Sector | 153.8099975586 | 149.4 | -0.028671722440667957 | 59 |
| SILVER | Silver | 61.2900009155 | 59.51 | -0.02904227262052217 | 60 |
| DIVIDEND | US Dividend Equities | 32.8199996948 | 31.86 | -0.02925044801118959 | 61 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.8199996948 | 83.3 | -0.029363781213724405 | 62 |
| BROAD_COMMODITIES | Broad Commodities | 17.0599994659 | 16.5 | -0.0328252921120743 | 63 |
| REAL_ESTATE | Real Estate Sector | 45.3600006104 | 43.86 | -0.03306879608057334 | 64 |
| UNITED_KINGDOM | United Kingdom Equities | 47.1599998474 | 45.46 | -0.03604749476040814 | 65 |
| CHINA | China Equities | 54.8300018311 | 52.77 | -0.03757070513048111 | 66 |
| SOLAR | Solar Energy | 63.0299987793 | 60.58 | -0.03887036057034832 | 67 |
| BRAZIL | Brazil Equities | 35.0999984741 | 33.73 | -0.039031297255209596 | 68 |
| ENERGY | Energy Sector | 57.5499992371 | 53.77 | -0.06568200325297657 | 69 |
| OIL | Crude Oil | 125.4300003052 | 114.87 | -0.08419038730371586 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 25.0 | 0.06439121332416797 | 0.016097803331041993 | Strongest momentum in the universe (+8.8% 7d, +75% 6m) with AI capex tailwinds intact; trend continuation favored into a likely benign FOMC hold. |
| anthropic-claude-fable-5 | SOUTH_KOREA | 15.0 | 0.1101544866445654 | 0.01652317299668481 | Explosive momentum (+12.7% 7d) driven by semiconductor export cycle; high-beta extension of the chip trade. |
| anthropic-claude-fable-5 | MOMENTUM | 20.0 | 0.043526530114562645 | 0.008705306022912529 | Diversified exposure to leading factor with consistent trend persistence (+5.9% 7d, +30% 6m). |
| anthropic-claude-fable-5 | SMALL_VALUE | 20.0 | -0.006687133325036343 | -0.0013374266650072687 | Cooling core CPI, falling yields, and strong domestic data support small-cap value breadth rally (+4.2% 7d). |
| anthropic-claude-fable-5 | GOLD | 20.0 | 0.001767869103219244 | 0.0003535738206438488 | Sharp +3.7% single-day spike into the close suggests geopolitical or macro hedging demand; serves as portfolio hedge against FOMC/geopolitical shocks. |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 35.0 | 0.06439121332416797 | 0.022536924663458788 | Strong momentum (+8.8% 7d), AI infrastructure demand, cooling core CPI supports growth multiples. |
| anthropic-claude-opus-4-7 | SMALL_CAP | 20.0 | 0.009011734708973318 | 0.0018023469417946638 | Yields falling sharply (2Y -8bp, 10Y -10bp), dovish FOMC hold expected, small caps benefit most from rate relief. |
| anthropic-claude-opus-4-7 | MOMENTUM | 20.0 | 0.043526530114562645 | 0.008705306022912529 | Persistent factor leadership (+5.85% 7d), benign vol regime with VIX at 17.7. |
| anthropic-claude-opus-4-7 | REGIONAL_BANKS | 15.0 | -0.023021435469189444 | -0.0034532153203784164 | Steepening curve, falling short rates, strong recent momentum into FOMC. |
| anthropic-claude-opus-4-7 | TAIWAN | 10.0 | 0.07181833030738427 | 0.007181833030738428 | Semiconductor supply chain leverage, strong trend, weaker USD supportive. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | 0.06439121332416797 | 0.01931736399725039 | Strongest momentum in the universe (+8.82% 7d, +75% 6m); cooling core CPI and falling yields support growth/tech leadership into FOMC. |
| anthropic-claude-opus-4-8 | MOMENTUM | 25.0 | 0.043526530114562645 | 0.010881632528640661 | Top broad factor with persistent trend (+5.85% 7d); benefits from soft-landing tape and declining VIX. |
| anthropic-claude-opus-4-8 | SMALL_CAP | 20.0 | 0.009011734708973318 | 0.0018023469417946638 | Rate relief (2Y down to 4.05%, 10Y to 4.45%) and risk-on breadth favor small caps; strong 7d/30d momentum. |
| anthropic-claude-opus-4-8 | TAIWAN | 15.0 | 0.07181833030738427 | 0.01077274954610764 | Semiconductor export strength and global electronics demand; strong trailing returns with constructive risk appetite. |
| anthropic-claude-opus-4-8 | NASDAQ100 | 10.0 | 0.02672799571173967 | 0.0026727995711739675 | Mega-cap growth leadership aided by falling yields and benign inflation print ahead of FOMC hold. |
| google-gemini-3-1-pro | SP500 | 40.0 | 0.006727334007414987 | 0.002690933602965995 | Broad US equity exposure to capture general market beta. |
| google-gemini-3-1-pro | NASDAQ100 | 30.0 | 0.02672799571173967 | 0.0080183987135219 | Growth and technology tilt for potential outperformance. |
| google-gemini-3-1-pro | SHORT_TREASURY | 30.0 | 0.0006556426882242672 | 0.00019669280646728016 | Cash-like proxy to reduce overall portfolio volatility. |
| openai-gpt-5-5 | SEMICONDUCTORS | 40.0 | 0.06439121332416797 | 0.025756485329667192 | Strongest broad thematic price momentum in the table, supported by falling Treasury yields and continued AI-related earnings-growth sentiment over a one-week horizon. |
| openai-gpt-5-5 | SOUTH_KOREA | 25.0 | 0.1101544866445654 | 0.02753862166114135 | Very strong recent and longer trailing performance with high semiconductor/export beta, giving leveraged exposure to the same risk-on chip leadership. |
| openai-gpt-5-5 | TAIWAN | 15.0 | 0.07181833030738427 | 0.01077274954610764 | Semiconductor supply-chain exposure with strong recent momentum and sensitivity to global AI hardware demand. |
| openai-gpt-5-5 | MOMENTUM | 10.0 | 0.043526530114562645 | 0.0043526530114562645 | Diversified exposure to stocks with persistent recent strength, which can outperform if the risk-on trend continues through the FOMC week. |
| openai-gpt-5-5 | BITCOIN_ETF | 10.0 | -0.011653743197308608 | -0.0011653743197308608 | High-beta liquidity-sensitive asset with positive short-term momentum that could benefit if the Fed hold and lower yields support risk appetite. |
| xai-grok-4-3 | MOMENTUM | 40.0 | 0.043526530114562645 | 0.017410612045825058 | Strong 7d trailing return of 5.85% and factor persistence into window with low VIX supporting trend continuation. |
| xai-grok-4-3 | SMALL_CAP | 35.0 | 0.009011734708973318 | 0.003154107148140661 | 4.01% 7d return and domestic growth sensitivity ahead of retail sales and industrial production releases. |
| xai-grok-4-3 | SEMICONDUCTORS | 25.0 | 0.06439121332416797 | 0.016097803331041993 | 8.82% 7d return and tech earnings momentum likely to hold through FOMC and BOJ events. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.58 | 0.06439121332416797 | 0.06725513522864159 | 0.0605278012212266 | 0.04289935141592381 |  | True | True |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.55 | 0.06439121332416797 | 0.04544689258496732 | 0.038719558577552333 | 0.06470759405959808 |  | True | True |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 5 | 0.5 | 0.06439121332416797 | 0.04034242950627591 | 0.03361509549886092 | 0.06981205713828949 |  | True | True |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | 0.06439121332416797 | 0.036773195338525994 | 0.030045861331111007 | 0.0733812913060394 |  | True | True |
| xai-grok-4-3 | MOMENTUM | 3 | 0.55 | 0.043526530114562645 | 0.036662522525007714 | 0.029935188517592727 | 0.07349196411955769 |  | True | True |
| google-gemini-3-1-pro | SP500 | 3 | 0.6 | 0.006727334007414987 | 0.010906025122955175 | 0.0041786911155401885 | 0.09924846152161022 |  | True | True |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 0.03361509549886092 | 0.49201 | 0.0683219761770308 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | ac761001a098386fa849139205a79dbadacdf8c8b3fc3d78290646515ebfc47d |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 03b5e9792d4c6bade89526a62f43cbdf51184fe03753997a0637de246e708b81 |
| manifest.yaml | 24ea1f9996eb7ea42099ad71e0794bd9828c83a604e8691065303afd863eeb2b |
| market_data/universe_trailing_returns.csv | 29ce3e75a78c914f42a7358bdbb62922c3d4dd51dc526ce83e318d784b7fa4b4 |
| market_data/universe_trailing_returns.md | 03b954f3e297410c2febcbbefd22ec734ca7df2f371bfd9f1f3ad28e3229f51d |
| market_data/universe_trailing_returns.json | 9e44263b0c84f6ca24eaf5073c59d4f5fae611b5d605e065fc0082e09cdb1c5c |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 5f10c1d01c285e19a09a835c94cbb520d5905b3f936519d6c97b6a71b6ffd1f1 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | ecb61fe308a702f44229537f3579b753445f234d4039dc4416ad88107bfe833c | yes |
| Final briefing | research/final_briefing.md | model-facing | ac761001a098386fa849139205a79dbadacdf8c8b3fc3d78290646515ebfc47d | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
