# CapitalBench Report: CB-2026-06-17-1W / official-20260617-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260617-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-17-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-06-17
- Decision deadline: 2026-06-18T02:30:00Z
- Horizon: one week
- Entry date: 2026-06-17
- Exit date: 2026-06-24
- Entry rule: Use adjusted close prices on Wednesday, June 17, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Wednesday, June 24, 2026 as the one-week exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SEMICONDUCTORS | 4 | 0.55 | Short trading week with Juneteenth holiday favors assets showing recent price strength; allocations target 100% in four high-momentum equity themes. | Post-FOMC yield rise triggers rotation out of growth themes; Low-volume holiday session amplifies any reversal in momentum names; Jobless claims surprise on June 18 shifts risk appetite before exit |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Concentrated in AI/semiconductor-led momentum that has shown the strongest recent trend, expecting continuation through the close-to-close window. | Sharp momentum/factor reversal or semiconductor profit-taking after extended run; Treasury yields rising further post-FOMC pressuring high-beta growth and EM equities; Won/Taiwan dollar or geopolitical shock hitting Korea/Taiwan exposure |
| openai-gpt-5-5 | openai | portfolio | SOUTH_KOREA | 5 | 0.58 | A concentrated high-beta momentum allocation is most likely to beat SPY over a one-week window if current trends continue. The main bet is that AI/semiconductor leadership and related country exposures remain the dominant market theme into the June 24 close. | A hawkish rates repricing after the FOMC could continue, pressuring high-valuation technology, semiconductor, and biotech exposures.; Recent extreme strength in South Korea, semiconductors, Taiwan, defense, and biotech could reverse sharply from profit-taking over the short window.; A stronger U.S. dollar could hurt non-U.S. country ETFs and emerging/export-oriented Asian equity exposures in dollar terms.; Any negative semiconductor supply-chain, AI-capex, or Taiwan/Korea geopolitical headline could disproportionately damage the largest positions.; A broad defensive rotation into value, cash-like assets, or low-volatility sectors would likely cause this high-beta portfolio to underperform SPY. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Momentum-tilted equity exposure in semis, defense, and industrials with gold hedge against rate/inflation risk during a holiday-shortened week. | Hawkish Fed repricing extends yield selloff hitting growth/semis; Profit-taking in semiconductors after large run; Gold reverses if dollar continues to strengthen; Juneteenth holiday compresses trading window and liquidity |
| google-gemini-3-1-pro | google | portfolio | SOUTH_KOREA | 3 | 0.65 | Allocating to high-momentum sectors and regions, particularly semiconductors and South Korea, to capture ongoing trends over the one-week horizon. | A sudden reversal in technology and semiconductor momentum could negatively impact the portfolio.; Geopolitical risks or currency fluctuations could affect South Korean equities.; Broader market volatility following the recent FOMC meeting could lead to a risk-off environment. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 139.2581563428 | 149.7100067138672 | 0.07505377527287349 | 1 |
| REGIONAL_BANKS | Regional Banks | 70.7405020122 | 73.97000122070312 | 0.04565276067656643 | 2 |
| UTILITIES | Utilities Sector | 44.1790255467 | 45.540000915527344 | 0.030805916427212976 | 3 |
| SMALL_CAP | US Small-Cap Stocks | 289.88 | 296.69 | 0.023492479646750386 | 4 |
| SMALL_VALUE | US Small-Cap Value | 213.69 | 218.59 | 0.022930413215405565 | 5 |
| HEALTHCARE | Healthcare Sector | 150.0537752226 | 153.35000610351562 | 0.02196699733829277 | 6 |
| REAL_ESTATE | Real Estate Sector | 43.5925530574 | 44.5099983215332 | 0.021045917244745027 | 7 |
| LOW_VOL | US Low Volatility Equities | 73.1724270453 | 74.69000244140625 | 0.020739716548786147 | 8 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.0993882751 | 84.44000244140625 | 0.016132659868303145 | 9 |
| US_DOLLAR | US Dollar | 28.18 | 28.530000686645508 | 0.012420180505518408 | 10 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 86.33 | 87.37999725341797 | 0.012162599946924146 | 11 |
| INDIA | India Equities | 49.06 | 49.630001068115234 | 0.011618448188243535 | 12 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 208.1854057668 | 210.3800048828125 | 0.010541560816567541 | 13 |
| MID_CAP | US Mid-Cap Stocks | 74.98 | 75.76 | 0.010402774073086096 | 14 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.02 | 94.7300033569336 | 0.0075516204736609804 | 15 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.19 | 94.75 | 0.00594542945110943 | 16 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.77 | 109.41000366210938 | 0.005884009029230253 | 17 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.61 | 99.19000244140625 | 0.00588178117235838 | 18 |
| INDUSTRIALS | Industrials Sector | 179.1623491514 | 180.2100067138672 | 0.005847531958748098 | 19 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.98 | 107.45999908447266 | 0.004486811408418889 | 20 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.31 | 48.5 | 0.003932933140136541 | 21 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.28 | 96.56999969482422 | 0.003012045023101484 | 22 |
| TIPS | Treasury Inflation-Protected Securities | 109.03 | 109.31999969482422 | 0.002659815599598492 | 23 |
| LARGE_VALUE | US Large-Cap Value | 240.38 | 241.0 | 0.0025792495215908318 | 24 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.73 | 79.8499984741211 | 0.0015050605057205235 | 25 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.53 | 91.59 | 0.0006555227794167173 | 26 |
| MOMENTUM | US Momentum Equities | 328.27 | 328.4100036621094 | 0.0004264893597021313 | 27 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 28 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.2561385364 | 115.06999969482422 | -0.0016150015429937659 | 29 |
| FINANCIALS | Financials Sector | 53.8623513913 | 53.720001220703125 | -0.0026428510252500814 | 30 |
| TAIWAN | Taiwan Equities | 105.11 | 104.72000122070312 | -0.0037103870164292285 | 31 |
| SOLAR | Solar Energy | 58.45 | 58.15999984741211 | -0.0049615081708792586 | 32 |
| CYBERSECURITY | Cybersecurity | 84.23 | 83.80000305175781 | -0.005105033221443511 | 33 |
| TOTAL_US_MARKET | Total US Stock Market | 365.76 | 363.65 | -0.005768810148731429 | 34 |
| DIVIDEND | US Dividend Equities | 31.93 | 31.719999313354492 | -0.006576908444895335 | 35 |
| YEN | Japanese Yen | 57.09 | 56.70000076293945 | -0.0068313056062454525 | 36 |
| BRAZIL | Brazil Equities | 34.11 | 33.849998474121094 | -0.007622442857780909 | 37 |
| SP500 | S&P 500 | 739.0760202617 | 733.24 | -0.007896373446987903 | 38 |
| SEMICONDUCTORS | Semiconductors | 623.97 | 618.9199829101562 | -0.008093365209615455 | 39 |
| UNITED_KINGDOM | United Kingdom Equities | 45.92 | 45.45000076293945 | -0.010235175023095566 | 40 |
| AGRICULTURE | Agriculture Commodities | 26.84 | 26.559999465942383 | -0.010432210657884355 | 41 |
| EURO | Euro | 106.05 | 104.7699966430664 | -0.012069810060665653 | 42 |
| EUROPE | Europe Equities | 88.0341045121 | 86.94999694824219 | -0.012314631583590474 | 43 |
| MATERIALS | Materials Sector | 51.8259858778 | 51.15999984741211 | -0.012850426655813485 | 44 |
| EMERGING_MARKETS | Emerging Markets | 59.7402031525 | 58.970001220703125 | -0.012892522809652474 | 45 |
| ENERGY | Energy Sector | 54.2835325771 | 53.56999969482422 | -0.013144555050140339 | 46 |
| TECHNOLOGY | Technology Sector | 185.5798751289 | 183.0500030517578 | -0.013632254442379588 | 47 |
| BROAD_AI_TECH | Broad AI Technology | 64.33 | 63.38999938964844 | -0.014612165558084311 | 48 |
| NASDAQ100 | Nasdaq 100 | 721.7144075433 | 710.62 | -0.015372296059690926 | 49 |
| CANADA | Canada Equities | 58.19 | 57.290000915527344 | -0.015466559279475045 | 50 |
| LARGE_GROWTH | US Large-Cap Growth | 121.6 | 119.67 | -0.015871710526315752 | 51 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.6263661277 | 70.27999877929688 | -0.01879709136720309 | 52 |
| JAPAN | Japan Equities | 94.45 | 92.61000061035156 | -0.019481200525658493 | 53 |
| COMMUNICATIONS | Communication Services Sector | 108.9108084759 | 106.54000091552734 | -0.021768340475566972 | 54 |
| AUSTRALIA | Australia Equities | 28.65 | 27.90999984741211 | -0.02582897565751796 | 55 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 242.79 | 236.19000244140625 | -0.027183976105250363 | 56 |
| CHINA | China Equities | 53.0 | 51.43000030517578 | -0.02962263575140034 | 57 |
| SOFTWARE | Software | 89.16 | 86.16999816894531 | -0.03353523812308978 | 58 |
| SOUTH_KOREA | South Korea Equities | 205.08 | 197.25999450683594 | -0.038131487678779385 | 59 |
| MEXICO | Mexico Equities | 77.31 | 73.79000091552734 | -0.04553096733246231 | 60 |
| BROAD_COMMODITIES | Broad Commodities | 16.54 | 15.779999732971191 | -0.045949230171028255 | 61 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 131.44 | 124.22000122070312 | -0.05492999679927624 | 62 |
| GOLD | Gold | 79.64 | 74.98999786376953 | -0.05838777167542031 | 63 |
| COPPER | Copper | 38.64 | 36.310001373291016 | -0.06030017149867972 | 64 |
| SOUTH_AFRICA | South Africa Equities | 66.51 | 62.18000030517578 | -0.06510298744285403 | 65 |
| BITCOIN_ETF | Bitcoin ETF | 36.36 | 33.869998931884766 | -0.06848187756092505 | 66 |
| OIL | Crude Oil | 114.23 | 106.29000091552734 | -0.06950887756694968 | 67 |
| ETHEREUM_ETF | Ethereum ETF | 13.07 | 11.920000076293945 | -0.08798775238760936 | 68 |
| METALS_MINING | Metals and Mining | 118.3076867236 | 107.22000122070312 | -0.09371906264045904 | 69 |
| SILVER | Silver | 60.61 | 51.779998779296875 | -0.14568555058081378 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 35.0 | -0.008093365209615455 | -0.0028326778233654093 | Strongest momentum, AI demand, Taiwan/Korea strength confirms chip cycle. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 20.0 | -0.027183976105250363 | -0.005436795221050073 | Strong momentum, geopolitical bid, low correlation to rate selloff. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 15.0 | 0.005847531958748098 | 0.0008771297938122147 | Broad cyclical strength with momentum tailwind. |
| anthropic-claude-opus-4-7 | GOLD | 15.0 | -0.05838777167542031 | -0.008758165751313047 | Hedge against hawkish Fed/yield spike and equity selloff risk. |
| anthropic-claude-opus-4-7 | MOMENTUM | 15.0 | 0.0004264893597021313 | 6.39734039553197e-05 | Factor momentum persisting; diversified exposure to leaders. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | -0.008093365209615455 | -0.0024280095628846365 | Strong AI-driven momentum with 9.3% 7d return; semis remain leadership amid resilient tech tape. |
| anthropic-claude-opus-4-8 | SOUTH_KOREA | 20.0 | -0.038131487678779385 | -0.007626297535755878 | Extraordinary momentum (15% 7d) driven by semiconductor export cycle; trend persistence likely near-term. |
| anthropic-claude-opus-4-8 | MOMENTUM | 20.0 | 0.0004264893597021313 | 8.529787194042627e-05 | Factor leadership with broad strong trend exposure; diversified momentum reduces single-name risk. |
| anthropic-claude-opus-4-8 | TAIWAN | 15.0 | -0.0037103870164292285 | -0.0005565580524643843 | Semiconductor supply chain strength, 7.3% 7d return; complements semis theme. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 15.0 | 0.005847531958748098 | 0.0008771297938122147 | Solid 5.9% 7d return, aerospace/defense strength, cyclical breadth diversifier. |
| google-gemini-3-1-pro | SOUTH_KOREA | 40.0 | -0.038131487678779385 | -0.015252595071511756 | South Korea equities have shown strong recent momentum, up 14.92% over the last 7 days, and are well-positioned to benefit from global semiconductor demand. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 30.0 | -0.008093365209615455 | -0.0024280095628846365 | Semiconductors continue to exhibit strong momentum, up 9.29% over the last 7 days, driven by AI and technology trends. |
| google-gemini-3-1-pro | MOMENTUM | 30.0 | 0.0004264893597021313 | 0.0001279468079106394 | The momentum factor has performed well recently, capturing the ongoing strength in technology and growth sectors. |
| openai-gpt-5-5 | SOUTH_KOREA | 35.0 | -0.038131487678779385 | -0.013346020687572784 | Strongest recent price momentum in the universe and leveraged to global semiconductor and export risk appetite. |
| openai-gpt-5-5 | SEMICONDUCTORS | 30.0 | -0.008093365209615455 | -0.0024280095628846365 | Leading short- and medium-term momentum tied to AI hardware demand, with potential to outperform broad equities if the growth trade resumes after the FOMC selloff. |
| openai-gpt-5-5 | TAIWAN | 15.0 | -0.0037103870164292285 | -0.0005565580524643843 | High recent momentum and direct exposure to semiconductor supply chains, complementing the dedicated semiconductor position. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 10.0 | -0.027183976105250363 | -0.0027183976105250363 | Strong recent momentum with a more idiosyncratic geopolitical and defense-spending catalyst profile than broad market beta. |
| openai-gpt-5-5 | BIOTECH | 10.0 | 0.07505377527287349 | 0.00750537752728735 | High recent momentum and high beta, offering upside if risk appetite rebounds over the shortened trading week. |
| xai-grok-4-3 | SEMICONDUCTORS | 30.0 | -0.008093365209615455 | -0.0024280095628846365 | Strong recent 7d momentum and semiconductor supply chain resilience likely to persist in low-news short week. |
| xai-grok-4-3 | MOMENTUM | 25.0 | 0.0004264893597021313 | 0.00010662233992553283 | Factor has shown persistence; limited catalysts reduce reversal risk over holiday-shortened window. |
| xai-grok-4-3 | AEROSPACE_DEFENSE | 25.0 | -0.027183976105250363 | -0.006795994026312591 | Defense budget stability and recent outperformance support continuation into quiet trading period. |
| xai-grok-4-3 | BIOTECH | 20.0 | 0.07505377527287349 | 0.0150107550545747 | Clinical and M&A driven sector exhibits elevated short-term volatility that can deliver positive drift. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SEMICONDUCTORS | 4 | 0.55 | -0.008093365209615455 | 0.005893373805303005 | 0.013789747252290908 | 0.06916040146757049 |  | True | True |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.55 | -0.008093365209615455 | -0.009648437485352258 | -0.0017520640383643545 | 0.08470221275822575 |  | False | False |
| openai-gpt-5-5 | SOUTH_KOREA | 5 | 0.58 | -0.038131487678779385 | -0.011543608386159494 | -0.0036472349391715904 | 0.08659738365903298 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | -0.008093365209615455 | -0.016086535597960996 | -0.008190162150973092 | 0.09114031087083449 |  | False | False |
| google-gemini-3-1-pro | SOUTH_KOREA | 3 | 0.65 | -0.038131487678779385 | -0.017552657826485754 | -0.009656284379497851 | 0.09260643309935924 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 04e0d7ac3ce6f3b67a916c35394fccc913537a534fcded2c9af7587120180f8b |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 03b5e9792d4c6bade89526a62f43cbdf51184fe03753997a0637de246e708b81 |
| manifest.yaml | 5a9cd5dac482a66cbedb9254f2f447a478cd7331ffdd3aa60f170380d56d3f0b |
| market_data/universe_trailing_returns.csv | 899f0e4b67622146d7f53cda8cb8a3868337fc9829dc0dde0899efca709c97ac |
| market_data/universe_trailing_returns.md | 91452b51c171ea470098a12a1ffbe35e131fef5599da894053747e045df5f433 |
| market_data/universe_trailing_returns.json | ea98469c1f0393f45065bd7c29c5dbd4ef5d6c94c5e3595a65f96d8076701799 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 9786a39d65e7d9d88e47397edbe747c3331126b9ff6c9d2c319718223f5e2ec6 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | b66fd001e089b7e687b7f5bf775008deb61635a9c9a2129a791d940e7c072478 | yes |
| Final briefing | research/final_briefing.md | model-facing | 04e0d7ac3ce6f3b67a916c35394fccc913537a534fcded2c9af7587120180f8b | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
