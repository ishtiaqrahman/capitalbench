# CapitalBench Report: CB-2026-06-24-1M / official-20260624-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260624-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-24-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-06-24
- Decision deadline: 2026-06-25T02:30:00Z
- Horizon: one month
- Entry date: 2026-06-24
- Exit date: 2026-07-24
- Entry rule: Use adjusted close prices on Wednesday, June 24, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Friday, July 24, 2026 as the one-month exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | INDUSTRIALS | 5 | 0.55 | Favor broadening participation and concrete fundamental catalysts over concentrated mega-cap tech, which is dragging the cap-weighted index, while holding a defensive healthcare anchor. | Sticky inflation (CPI +4.2% YoY, energy surging) could force hawkish Fed repricing, hurting rate-sensitive financials and cyclicals.; Semiconductor allocation carries very high beta (2.21) and 65% volatility; a tech-led selloff or 'sell the news' on Micron could cause sharp drawdown.; Slowing housing (new-home sales -7.3%) and soft Q1 GDP (+1.6%) signal cyclical weakness that could undercut industrials and financials.; Mega-cap tech weakness spreading could pull down broad equity exposure including equal-weight and semiconductors. |
| xai-grok-4-3 | xai | portfolio | SMALL_CAP | 5 | 0.65 | Allocations prioritize areas with recent positive breadth and macro support from PMI and sales data for the one-month window. | Persistent inflation readings could pressure rate-sensitive small and mid caps.; Sharp reversal in biotech or regional bank momentum if earnings disappoint.; Oil price volatility affecting broader risk appetite before exit close. |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.65 | Overweighting semiconductors based on strong Micron earnings and guidance, balanced with small caps for market broadening and healthcare for defensive positioning. | A reversal in semiconductor momentum if AI enthusiasm wanes or broader tech weakness drags down the sector.; Small caps are sensitive to economic growth and credit conditions; a macro slowdown could disproportionately impact them.; Healthcare may underperform if the market strongly favors cyclical or high-growth sectors. |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.58 | A concentrated cyclical and thematic allocation may outperform if AI hardware earnings momentum and market broadening persist through July. The main tradeoff is elevated volatility, especially in semiconductors and biotech, after strong recent moves. | Semiconductor exposure could reverse sharply if investors sell the Micron news, question sustainability of AI/HBM margins, or de-risk high-beta technology before exit.; Biotech and regional banks rely partly on recent momentum with limited specific briefing catalysts, so factor rotation or profit-taking could hurt performance.; Hot inflation data or hawkish rate repricing could pressure small caps, banks, biotech financing conditions, and long-duration growth equities.; A renewed decline in breadth led by cyclicals, or renewed dominance of mega-cap S&P 500 constituents not held here, could cause benchmark underperformance. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Concentrated in semis (Micron catalyst), supported by strong manufacturing PMI cyclicals and mid-caps, with biotech and long Treasuries adding diversification amid falling yields. | Semi/AI sentiment reversal if mega-cap tech selling intensifies (Microsoft -2.3%, Oracle -4.6% on decision day); Sticky CPI (+4.2% YoY headline) prompts hawkish Fed repricing, hurting duration and growth; Biotech high volatility and binary clinical/regulatory risk; Industrial/mid-cap cyclicals vulnerable if Q1 GDP softness (+1.6%) extends; Concentration in high-beta semis (beta 2.21) amplifies drawdowns |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 106.29 | 136.69 | 0.2860099727161538 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 11.92 | 14.04 | 0.1778523489932886 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 15.78 | 17.95 | 0.13751584283903684 | 3 |
| ENERGY | Energy Sector | 53.57 | 59.619998931884766 | 0.11293632503051643 | 4 |
| BITCOIN_ETF | Bitcoin ETF | 33.87 | 36.35 | 0.07322113965160915 | 5 |
| AGRICULTURE | Agriculture Commodities | 26.56 | 28.24 | 0.06325301204819267 | 6 |
| HEALTHCARE | Healthcare Sector | 153.35 | 162.57000732421875 | 0.06012394733758564 | 7 |
| COPPER | Copper | 36.31 | 38.35 | 0.05618286973285591 | 8 |
| CYBERSECURITY | Cybersecurity | 83.7278415327 | 88.4 | 0.055801730723886944 | 9 |
| BRAZIL | Brazil Equities | 33.85 | 35.73 | 0.055539143279172754 | 10 |
| DIVIDEND | US Dividend Equities | 31.72 | 33.290000915527344 | 0.049495615243611235 | 11 |
| FINANCIALS | Financials Sector | 53.72 | 56.310001373291016 | 0.048212981632371976 | 12 |
| UNITED_KINGDOM | United Kingdom Equities | 45.45 | 47.23 | 0.039163916391639075 | 13 |
| CHINA | China Equities | 51.43 | 53.33 | 0.03694341823838232 | 14 |
| LOW_VOL | US Low Volatility Equities | 74.5515080082 | 77.19000244140625 | 0.03539156354712558 | 15 |
| REAL_ESTATE | Real Estate Sector | 44.51 | 45.95000076293945 | 0.03235229752728497 | 16 |
| CANADA | Canada Equities | 57.29 | 59.07 | 0.031069994763484043 | 17 |
| LARGE_VALUE | US Large-Cap Value | 241.0 | 248.24 | 0.03004149377593368 | 18 |
| AUSTRALIA | Australia Equities | 27.91 | 28.72 | 0.029021855965603693 | 19 |
| REGIONAL_BANKS | Regional Banks | 73.97 | 75.73 | 0.02379342976882537 | 20 |
| MEXICO | Mexico Equities | 73.79 | 75.45 | 0.022496273207751605 | 21 |
| SOFTWARE | Software | 86.17 | 87.98 | 0.021004990135778057 | 22 |
| EUROPE | Europe Equities | 86.95 | 88.41 | 0.016791259344450804 | 23 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 236.19 | 240.14 | 0.01672382403996786 | 24 |
| GOLD | Gold | 74.99 | 76.23 | 0.016535538071743128 | 25 |
| UTILITIES | Utilities Sector | 45.54 | 46.290000915527344 | 0.016469058311975093 | 26 |
| SILVER | Silver | 51.78 | 52.59 | 0.015643105446118133 | 27 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 210.38 | 213.57 | 0.015163038311626575 | 28 |
| INDUSTRIALS | Industrials Sector | 180.21 | 182.66000366210938 | 0.013595270307471097 | 29 |
| SMALL_VALUE | US Small-Cap Value | 218.59 | 221.4199981689453 | 0.012946604002677553 | 30 |
| SP500 | S&P 500 | 733.24 | 738.93 | 0.007760078555452354 | 31 |
| TOTAL_US_MARKET | Total US Stock Market | 362.605190114 | 364.8 | 0.006052891535584415 | 32 |
| BIOTECH | Biotechnology | 149.71 | 150.48 | 0.005143277002204183 | 33 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.3226046161 | 91.61 | 0.003147034462148257 | 34 |
| EURO | Euro | 104.7000669396 | 104.947 | 0.0023584804443577134 | 35 |
| MATERIALS | Materials Sector | 51.16 | 51.2599983215332 | 0.001954619263745183 | 36 |
| US_DOLLAR | US Dollar | 28.53 | 28.58 | 0.001752541184717682 | 37 |
| MID_CAP | US Mid-Cap Stocks | 75.76 | 75.7699966430664 | 0.00013195146602962282 | 38 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 39 |
| COMMUNICATIONS | Communication Services Sector | 106.54 | 106.30000305175781 | -0.0022526464073793218 | 40 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.4817107727 | 79.2300033569336 | -0.0031668595620221174 | 41 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.44 | 84.12999725341797 | -0.0036712783820704864 | 42 |
| TIPS | Treasury Inflation-Protected Securities | 108.2610860768 | 107.5 | -0.007030098296446852 | 43 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.28 | 69.70999908447266 | -0.008110428507788092 | 44 |
| YEN | Japanese Yen | 56.7 | 56.04 | -0.011640211640211673 | 45 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.3885269485 | 47.8 | -0.012162530781860248 | 46 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.4112962113 | 93.11 | -0.013783268141850269 | 47 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.8581097402 | 97.45999908447266 | -0.014142599523717325 | 48 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.4176585934 | 93.02999877929688 | -0.01469703691847457 | 49 |
| JAPAN | Japan Equities | 92.61 | 91.21 | -0.01511715797430091 | 50 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.171870015 | 105.55 | -0.015133355560307038 | 51 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.169641037 | 94.64 | -0.015905654014155002 | 52 |
| LARGE_GROWTH | US Large-Cap Growth | 119.67 | 117.65 | -0.016879752653129354 | 53 |
| SOUTH_AFRICA | South Africa Equities | 62.18 | 61.07 | -0.01785139916371825 | 54 |
| SMALL_CAP | US Small-Cap Stocks | 296.69 | 291.1700134277344 | -0.018605232978076813 | 55 |
| EMERGING_MARKETS | Emerging Markets | 58.97 | 57.79999923706055 | -0.01984060985144065 | 56 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.0264762997 | 106.2300033569336 | -0.025649484764409425 | 57 |
| INDIA | India Equities | 49.63 | 48.02 | -0.03244005641748937 | 58 |
| NASDAQ100 | Nasdaq 100 | 710.62 | 684.23 | -0.037136584953983864 | 59 |
| TECHNOLOGY | Technology Sector | 183.05 | 175.8800048828125 | -0.039169599110557285 | 60 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 87.0562569994 | 83.25 | -0.04372180852464447 | 61 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.07 | 109.41000366210938 | -0.04918741929165393 | 62 |
| METALS_MINING | Metals and Mining | 107.22 | 101.74 | -0.05110986756202207 | 63 |
| TAIWAN | Taiwan Equities | 104.72 | 98.01 | -0.06407563025210083 | 64 |
| MOMENTUM | US Momentum Equities | 328.41 | 306.3900146484375 | -0.0670502888205674 | 65 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 124.22 | 114.015 | -0.0821526324263403 | 66 |
| BROAD_AI_TECH | Broad AI Technology | 63.3895538449 | 57.98 | -0.0853382539674592 | 67 |
| SEMICONDUCTORS | Semiconductors | 618.92 | 561.19 | -0.09327538292509518 | 68 |
| SOLAR | Solar Energy | 58.16 | 51.28 | -0.1182943603851444 | 69 |
| SOUTH_KOREA | South Korea Equities | 197.26 | 162.96 | -0.1738821859474804 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | -0.09327538292509518 | -0.027982614877528556 | Micron's blowout Q3 results ($41B rev vs $24B prior) and Q4 guide to $50B with 86% gross margin signal extraordinary memory/HBM cycle strength benefiting the whole semi complex. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 20.0 | 0.013595270307471097 | 0.0027190540614942197 | Manufacturing PMI at 55.7 with output 57.7 shows strong industrial expansion; sector has solid momentum with moderate volatility. |
| anthropic-claude-opus-4-7 | MID_CAP | 20.0 | 0.00013195146602962282 | 2.6390293205924566e-05 | Mid-caps benefit from broadening breadth, falling 10Y yields (4.40%), and domestic growth; reasonable volatility profile. |
| anthropic-claude-opus-4-7 | BIOTECH | 15.0 | 0.005143277002204183 | 0.0007714915503306274 | Strong recent catalyst-driven momentum with falling rates supportive of biotech financing; healthcare sector also showing strength. |
| anthropic-claude-opus-4-7 | LONG_TREASURY | 15.0 | -0.04372180852464447 | -0.00655827127869667 | 10Y dropped to 4.40% from 4.50%; oil -3.9% and gold -3.4% suggest disinflation impulse that supports duration into the window. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 25.0 | 0.013595270307471097 | 0.003398817576867774 | Strong manufacturing PMI (55.7) and output index (57.7) support cyclical industrials; +6.58% benchmark-relative 30d with moderate drawdown and broad participation. |
| anthropic-claude-opus-4-8 | FINANCIALS | 20.0 | 0.048212981632371976 | 0.009642596326474396 | Steepening yield curve, resilient retail sales, and broad-market breadth favor financials; outperformed SPY by 5.2% over 30d with low drawdown. |
| anthropic-claude-opus-4-8 | EQUAL_WEIGHT_SP500 | 20.0 | 0.015163038311626575 | 0.0030326076623253154 | Breadth note shows more stocks rising while mega-cap tech weighs on cap-weighted index; equal-weight captures broad participation with lower volatility. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 15.0 | 0.06012394733758564 | 0.009018592100637846 | Defensive sector with low beta (0.40) and positive momentum amid sticky inflation; supports downside protection while sticky CPI keeps Fed on hold. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 20.0 | -0.09327538292509518 | -0.018655076585019036 | Micron's blowout Q3 ($41.5B rev, 84.6% gross margin) and Q4 guidance to $50B with HBM4 ramp is a concrete near-term catalyst for chip demand strength. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | -0.09327538292509518 | -0.03731015317003807 | Micron's strong fiscal Q3 results and Q4 guidance, along with HBM4 production updates, provide a positive catalyst for the semiconductor sector. |
| google-gemini-3-1-pro | SMALL_CAP | 30.0 | -0.018605232978076813 | -0.005581569893423044 | Small caps have shown recent relative strength and may benefit from a broadening market if mega-cap tech leadership pauses. |
| google-gemini-3-1-pro | HEALTHCARE | 30.0 | 0.06012394733758564 | 0.018037184201275692 | Healthcare offers defensive characteristics and has shown recent positive momentum, providing balance against high-beta semiconductor exposure. |
| openai-gpt-5-5 | SEMICONDUCTORS | 40.0 | -0.09327538292509518 | -0.03731015317003807 | Micron reported very strong revenue, margins, guidance, and HBM shipment facts, providing near-term fundamental support for AI semiconductor sentiment despite high volatility and reversal risk after large prior gains. |
| openai-gpt-5-5 | BIOTECH | 20.0 | 0.005143277002204183 | 0.0010286554004408366 | Biotech has strong recent breadth and relative strength, and its lower direct sensitivity to mega-cap technology concentration may help if the market broadens; independent catalyst support in the briefing is limited. |
| openai-gpt-5-5 | REGIONAL_BANKS | 15.0 | 0.02379342976882537 | 0.0035690144653238052 | Regional banks are participating in the recent broadening trade, and lower Treasury yields into the entry close may support rate-sensitive financials over the one-month window. |
| openai-gpt-5-5 | SMALL_VALUE | 15.0 | 0.012946604002677553 | 0.001941990600401633 | Small-cap value aligns with the observed market breadth improvement and Russell 2000 strength, with exposure to domestic cyclicals that could benefit from firm retail sales and manufacturing PMI. |
| openai-gpt-5-5 | INDUSTRIALS | 10.0 | 0.013595270307471097 | 0.0013595270307471099 | Industrials offer cyclical exposure supported by strong June manufacturing PMI and recent relative resilience, while being less concentrated in the large technology names that weighed on the S&P 500. |
| xai-grok-4-3 | SMALL_CAP | 30.0 | -0.018605232978076813 | -0.005581569893423044 | Positive 30d return and sensitivity to domestic growth signals in retail sales and manufacturing PMI. |
| xai-grok-4-3 | BIOTECH | 25.0 | 0.005143277002204183 | 0.0012858192505510457 | Strong 30d performance with support from broad risk appetite and sector-specific earnings momentum. |
| xai-grok-4-3 | REGIONAL_BANKS | 20.0 | 0.02379342976882537 | 0.004758685953765074 | Recent outperformance aligned with positive retail sales and stable rate environment. |
| xai-grok-4-3 | MID_CAP | 15.0 | 0.00013195146602962282 | 1.9792719904443424e-05 | Domestic cyclical exposure benefiting from Q1 GDP and PMI readings over the window. |
| xai-grok-4-3 | EQUAL_WEIGHT_SP500 | 10.0 | 0.015163038311626575 | 0.0015163038311626577 | Broad large-cap diversification with reduced mega-cap concentration risk. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 5 | 0.55 | 0.013595270307471097 | 0.006437537081286294 | -0.0013225414741660606 | 0.2795724356348675 |  | False | True |
| xai-grok-4-3 | SMALL_CAP | 5 | 0.65 | -0.018605232978076813 | 0.0019990318619601774 | -0.0057610466934921774 | 0.28401094085419365 |  | False | True |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.65 | -0.09327538292509518 | -0.024854538862185426 | -0.032614617417637784 | 0.3108645115783392 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.58 | -0.09327538292509518 | -0.029410965673124692 | -0.037171044228577046 | 0.3154209383892785 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | -0.09327538292509518 | -0.031023950251194452 | -0.0387840288066468 | 0.3170339229673483 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 0699b051cc515eb2156c7207329dedd7eaee82ba919a87c4e16d6167fabbf636 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 7858eef0aa73ea38b28daacc4aaa57e57b110de6456378f1697ff1cd79ca213c |
| manifest.yaml | 8155d3722ac720e4188babe82b9ad1331c64252be6d53c62197268b84dd45825 |
| market_data/universe_trailing_returns.csv | 8bb99f56fda6f532d2662d3f0c3c3887bdbbd5b5a41fb3a99caa9b2f47db2060 |
| market_data/universe_trailing_returns.md | 1648c81233bf787f247ad8fdc4ca44688be4feb34160b890a60b435ace1596fe |
| market_data/universe_trailing_returns.json | 0c6fae6055297130af761bbedcbdb4007e68fc4bd90bf56f5641f8af2631c938 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | fe810c6d4999e4a20e62ad16b418f69029733161f84c89ca2a555a24db923955 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 8e5b8c5ff1c00bbfb5e2c8593cd6400df7ee8dd64696e28df2f515aa2a786705 | yes |
| Final briefing | research/final_briefing.md | model-facing | 0699b051cc515eb2156c7207329dedd7eaee82ba919a87c4e16d6167fabbf636 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
