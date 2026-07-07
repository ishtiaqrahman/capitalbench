# CapitalBench Report: CB-2026-06-30-1W / official-20260630-no-fable-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260630-no-fable-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-30-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-06-30
- Decision deadline: 2026-07-01T07:30:00Z
- Horizon: one week
- Entry date: 2026-06-30
- Exit date: 2026-07-07
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Balanced pro-risk tilt combining semi leadership, cyclical breadth via industrials/mid-caps, and healthcare/biotech momentum with defensive traits. | Weak July 2 jobs report could trigger reversal in cyclicals and semis given extended YTD gains; Semiconductor reversal risk after SMH +82% YTD; high beta 2.24 amplifies drawdowns; Biotech/momentum crowding risk into holiday-thin liquidity; Rising yields (10Y 4.4%) pressuring growth multiples |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Overweight momentum-leading cyclicals and tech with diversified broad-market ballast to capture continued risk-on breadth while limiting concentration risk. | Semiconductor and Nasdaq high-beta positions could reverse sharply if Thursday's jobs report or ISM data disappoints; Sticky core PCE at 3.4% could push yields higher and pressure growth/tech multiples; Holiday-shortened week with thin liquidity may amplify volatility around economic releases; Crowded semiconductor trade after huge YTD gains carries elevated reversal/positioning risk |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.56 | Favor recent leadership with some macro or sector support rather than defensive assets, because the benchmark is equities and the scoring window is short. Semiconductors and biotech are the main alpha engines, with industrials and regional banks adding cyclical exposure if incoming data remain firm. | A hot employment or ISM inflation signal could push Treasury yields higher and trigger a high-beta growth and semiconductor reversal.; Semiconductor positioning appears crowded after very large quarter-to-date and year-to-date gains, increasing the risk of profit-taking during a holiday-shortened week.; A weak jobs or services report could hurt industrials, regional banks, and broader cyclical risk appetite relative to the S&P 500.; Biotech's recent strength may reverse without a specific scheduled catalyst, especially if speculative equity flows fade.; Taiwan exposure could underperform because of semiconductor supply-chain volatility, currency moves, or regional geopolitical risk. |
| xai-grok-4-3 | xai | portfolio | SEMICONDUCTORS | 3 | 0.55 | Concentrated in semiconductors, small caps, and biotech based on briefing-noted performance and sector momentum into the one-week window. | Weaker-than-expected June employment report on July 2 could pressure risk assets; Follow-through from May PCE at 4.1% y/y may sustain rate sensitivity; Holiday-shortened trading week increases liquidity and gap risk around July 3-6 |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.65 | Allocating to high-momentum sectors (Semiconductors, Nasdaq 100) and strong-performing small caps to maximize short-term returns. | A sudden reversal in semiconductor momentum given the extreme recent run-up.; Higher Treasury yields pressuring growth and small-cap valuations.; Holiday-shortened trading week leading to lower liquidity and potential volatility spikes. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 11.89 | 13.510000228881836 | 0.13624896794632768 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 33.29 | 36.150001525878906 | 0.08591173102670191 | 2 |
| FINANCIALS | Financials Sector | 53.61 | 56.05 | 0.04551389666107064 | 3 |
| SOFTWARE | Software | 90.6 | 94.12999725341797 | 0.038962442090706206 | 4 |
| HEALTHCARE | Healthcare Sector | 158.66 | 164.44 | 0.036430102105130535 | 5 |
| COMMUNICATIONS | Communication Services Sector | 107.13 | 111.02 | 0.03631102398954544 | 6 |
| BIOTECH | Biotechnology | 158.25 | 163.8699951171875 | 0.03551339726500791 | 7 |
| AGRICULTURE | Agriculture Commodities | 26.67 | 27.549999237060547 | 0.03299584690890689 | 8 |
| ENERGY | Energy Sector | 53.11 | 54.64 | 0.028808134061382162 | 9 |
| BROAD_COMMODITIES | Broad Commodities | 15.88 | 16.31999969482422 | 0.027707789346613332 | 10 |
| LOW_VOL | US Low Volatility Equities | 74.9 | 76.92 | 0.026969292389853017 | 11 |
| CYBERSECURITY | Cybersecurity | 89.85 | 92.20999908447266 | 0.02626598869752539 | 12 |
| DIVIDEND | US Dividend Equities | 31.71 | 32.54 | 0.02617470829391344 | 13 |
| GOLD | Gold | 75.51 | 77.37000274658203 | 0.024632535380506138 | 14 |
| OIL | Crude Oil | 106.44 | 108.91999816894531 | 0.02329949425916311 | 15 |
| LARGE_VALUE | US Large-Cap Value | 242.43 | 247.74 | 0.0219032297982924 | 16 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.07 | 84.86 | 0.021548091970627237 | 17 |
| UNITED_KINGDOM | United Kingdom Equities | 46.14 | 47.130001068115234 | 0.021456460080520934 | 18 |
| REAL_ESTATE | Real Estate Sector | 44.03 | 44.89 | 0.019532137179195885 | 19 |
| SILVER | Silver | 53.47 | 54.459999084472656 | 0.01851503804886212 | 20 |
| CHINA | China Equities | 51.025 | 51.779998779296875 | 0.014796644376224855 | 21 |
| MATERIALS | Materials Sector | 50.83 | 51.51 | 0.013377926421404673 | 22 |
| CANADA | Canada Equities | 57.64 | 58.36000061035156 | 0.012491336057452562 | 23 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 242.42 | 245.11000061035156 | 0.011096446705517682 | 24 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.77 | 214.72999572753906 | 0.009211804895140618 | 25 |
| UTILITIES | Utilities Sector | 45.34 | 45.7 | 0.007940008822232114 | 26 |
| SOUTH_AFRICA | South Africa Equities | 63.19 | 63.59000015258789 | 0.006330117939355784 | 27 |
| EUROPE | Europe Equities | 88.54 | 89.04000091552734 | 0.0056471754633762306 | 28 |
| BRAZIL | Brazil Equities | 34.5 | 34.63999938964844 | 0.004057953323143071 | 29 |
| YEN | Japanese Yen | 56.44 | 56.630001068115234 | 0.003366425728476896 | 30 |
| REGIONAL_BANKS | Regional Banks | 74.85 | 75.06999969482422 | 0.002939207679682365 | 31 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.6011573011 | 79.76 | 0.0019954822804795214 | 32 |
| SP500 | S&P 500 | 746.77 | 747.71 | 0.0012587543688151737 | 33 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.28 | 117.39 | 0.0009379263301501073 | 34 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.3724586419 | 91.45 | 0.0008486294366216729 | 35 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 36 |
| US_DOLLAR | US Dollar | 28.41 | 28.399999618530273 | -0.0003520021636651549 | 37 |
| EURO | Euro | 105.3696197204 | 105.30699920654297 | -0.0005942938203933323 | 38 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.3314410107 | 107.23999786376953 | -0.0008519698055796665 | 39 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.0401799897 | 95.94000244140625 | -0.0010430795559159822 | 40 |
| AUSTRALIA | Australia Equities | 28.16 | 28.1299991607666 | -0.001065370711413327 | 41 |
| TOTAL_US_MARKET | Total US Stock Market | 370.04 | 369.61 | -0.0011620365365906382 | 42 |
| INDIA | India Equities | 49.39 | 49.33000183105469 | -0.001214783740540848 | 43 |
| TIPS | Treasury Inflation-Protected Securities | 108.3700205761 | 108.17 | -0.0018457187240223938 | 44 |
| JAPAN | Japan Equities | 93.27 | 93.06999969482422 | -0.0021443154838187706 | 45 |
| MEXICO | Mexico Equities | 75.27 | 75.04000091552734 | -0.0030556541048578634 | 46 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.1821183947 | 93.83999633789062 | -0.0036325585221560486 | 47 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.6488124013 | 98.21 | -0.0044482279169761885 | 48 |
| SMALL_VALUE | US Small-Cap Value | 221.2 | 220.18 | -0.004611211573236851 | 49 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.2581861414 | 93.7 | -0.005921885029302909 | 50 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.3186878374 | 48.02000045776367 | -0.006181611980885293 | 51 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.25 | 70.77999877929688 | -0.0065965083607456565 | 52 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.6876681292 | 107.88 | -0.007431092626257407 | 53 |
| COPPER | Copper | 37.73 | 37.38999938964844 | -0.009011412943322528 | 54 |
| EMERGING_MARKETS | Emerging Markets | 59.69 | 58.880001068115234 | -0.013570094352232553 | 55 |
| SMALL_CAP | US Small-Cap Stocks | 300.45 | 296.19 | -0.014178731902146802 | 56 |
| INDUSTRIALS | Industrials Sector | 185.23 | 182.38 | -0.01538627652108182 | 57 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 86.0998138005 | 84.55 | -0.01800019921170848 | 58 |
| MID_CAP | US Mid-Cap Stocks | 77.11 | 75.47 | -0.021268317987290897 | 59 |
| LARGE_GROWTH | US Large-Cap Growth | 124.17 | 121.35 | -0.022710799710074947 | 60 |
| NASDAQ100 | Nasdaq 100 | 736.4 | 709.43 | -0.03662411732753945 | 61 |
| METALS_MINING | Metals and Mining | 106.93 | 102.47000122070312 | -0.041709518182894256 | 62 |
| BROAD_AI_TECH | Broad AI Technology | 65.61 | 62.08000183105469 | -0.05380274605921831 | 63 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 132.22 | 124.41000366210938 | -0.05906819193685242 | 64 |
| TECHNOLOGY | Technology Sector | 190.52 | 179.18 | -0.05952131009867734 | 65 |
| TAIWAN | Taiwan Equities | 108.61 | 101.87999725341797 | -0.061964853573170386 | 66 |
| SOLAR | Solar Energy | 59.15 | 54.810001373291016 | -0.07337275784799635 | 67 |
| MOMENTUM | US Momentum Equities | 342.83 | 312.44 | -0.0886445176909838 | 68 |
| SOUTH_KOREA | South Korea Equities | 201.9 | 181.2899932861328 | -0.10208027099488459 | 69 |
| SEMICONDUCTORS | Semiconductors | 655.89 | 581.4500122070312 | -0.1134946222582578 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | -0.1134946222582578 | -0.03404838667747734 | Strong semi momentum with June 30 broad chip rally; TSMC monthly sales July 10 catalyst within window. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 20.0 | -0.01538627652108182 | -0.0030772553042163644 | Broad strength, low drawdown, positive breadth; benefits from ISM Manufacturing and jobs data. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 20.0 | 0.036430102105130535 | 0.007286020421026107 | Defensive with strong recent momentum (+6.6% 30d) and low beta; resilient into holiday-shortened week. |
| anthropic-claude-opus-4-7 | BIOTECH | 15.0 | 0.03551339726500791 | 0.005327009589751186 | Strongest 30d momentum (+15.9%) with 70% up-day share; continuation potential. |
| anthropic-claude-opus-4-7 | MID_CAP | 15.0 | -0.021268317987290897 | -0.0031902476980936343 | Broad participation theme with small/mid outperformance; reasonable volatility profile. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 25.0 | -0.1134946222582578 | -0.02837365556456445 | Strong semiconductor momentum with broad chip strength on June 30 (NVDA, AMD, Intel up); leadership group heading into a light-catalyst holiday week. Momentum supported by sector-wide breadth, though very high beta and reversal risk noted. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 20.0 | -0.01538627652108182 | -0.0030772553042163644 | Cyclical strength with strong 30d relative outperformance and high up-day share; benefits from constructive ISM Manufacturing readings and firm domestic demand data. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 15.0 | 0.036430102105130535 | 0.00546451531576958 | Defensive-leaning sector with strong recent breadth and low drawdown; biotech strength spillover provides fundamental support ahead of jobs data. |
| anthropic-claude-opus-4-8 | NASDAQ100 | 20.0 | -0.03662411732753945 | -0.00732482346550789 | Broad large-cap tech/growth exposure participating in the Nasdaq's 1.5% June 30 rally; diversified way to hold leadership with lower single-sector concentration. |
| anthropic-claude-opus-4-8 | EQUAL_WEIGHT_SP500 | 20.0 | 0.009211804895140618 | 0.0018423609790281237 | Broad participation with reduced mega-cap concentration; steady positive breadth and low volatility provide ballast against a tech reversal. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | -0.1134946222582578 | -0.04539784890330312 | Semiconductors have shown massive recent strength, with SMH up 82% YTD and strong momentum heading into the new quarter. |
| google-gemini-3-1-pro | NASDAQ100 | 30.0 | -0.03662411732753945 | -0.010987235198261835 | Broad tech exposure captures the ongoing AI and growth rally while providing some diversification away from pure semis. |
| google-gemini-3-1-pro | SMALL_CAP | 30.0 | -0.014178731902146802 | -0.00425361957064404 | The Russell 2000 had its best first half since 1991, indicating strong breadth and potential for continued catch-up performance. |
| openai-gpt-5-5 | SEMICONDUCTORS | 35.0 | -0.1134946222582578 | -0.03972311779039023 | Semiconductor shares showed strong broad participation into the entry close, with reported June 30 gains across Nvidia, AMD, Intel and semiconductor ETFs; this is a short-window momentum allocation, tempered by extreme recent gains and reversal risk. |
| openai-gpt-5-5 | BIOTECH | 25.0 | 0.03551339726500791 | 0.008878349316251977 | Biotech had strong 7-day and 30-day relative performance, was near its 52-week high, and has only moderate benchmark beta versus other high-return themes, offering a continuation candidate with less direct exposure to the week's macro data than cyclicals. |
| openai-gpt-5-5 | INDUSTRIALS | 20.0 | -0.01538627652108182 | -0.0030772553042163644 | Industrials were at a 52-week high with positive 7-day and 30-day relative performance, supported by still-positive GDP, income, consumption, and corporate-profit data ahead of the short scoring window. |
| openai-gpt-5-5 | REGIONAL_BANKS | 10.0 | 0.002939207679682365 | 0.00029392076796823656 | Regional banks had strong recent relative performance and could benefit if the employment and services data support domestic growth and higher yields, though credit and rate sensitivity make this a smaller position. |
| openai-gpt-5-5 | TAIWAN | 10.0 | -0.061964853573170386 | -0.006196485357317039 | Taiwan equities provide additional semiconductor supply-chain exposure with positive 30-day relative performance, but position size is limited because currency and geopolitical risks can dominate over a one-week window. |
| xai-grok-4-3 | SEMICONDUCTORS | 40.0 | -0.1134946222582578 | -0.04539784890330312 | June 30 reports highlighted strong semiconductor gains including Nvidia +2.6%, AMD +7.7%, and SMH +3%+, with SMH up 82% YTD. |
| xai-grok-4-3 | SMALL_CAP | 35.0 | -0.014178731902146802 | -0.00496255616575138 | Russell 2000 posted its strongest first-half gain since 1991 at nearly 22%, with positive June 30 equity breadth. |
| xai-grok-4-3 | BIOTECH | 25.0 | 0.03551339726500791 | 0.008878349316251977 | Biotech showed 7.63% 7-day return into the window alongside healthcare sector strength of 4.26%. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | -0.1134946222582578 | -0.02770285966901004 | -0.028961614037825215 | 0.16395182761533772 |  | False | False |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.55 | -0.1134946222582578 | -0.031468858039490996 | -0.03272761240830617 | 0.1677178259858187 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.56 | -0.1134946222582578 | -0.03982458836770342 | -0.04108334273651859 | 0.1760735563140311 |  | False | False |
| xai-grok-4-3 | SEMICONDUCTORS | 3 | 0.55 | -0.1134946222582578 | -0.04148205575280252 | -0.04274081012161769 | 0.1777310236991302 |  | False | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.65 | -0.1134946222582578 | -0.06063870367220899 | -0.061897458041024166 | 0.19688767161853668 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 79dc6a4c9142c8fe89c2547bbfe2042c35174fcfa460a2e126bf8fec73901ceb |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 66320ebc013af445c33450b3005ec684487d06b5bca45c52a3ff9e8e24373e4c |
| manifest.yaml | cca97c9edfbcb2b01aa1dbe407c20723803007f1ead9e4a8d0a2c60f4e7c78cb |
| market_data/universe_trailing_returns.csv | fc2f3371dafcaf4e49ff93b69f7a41822e4becdacc75969daea9838e0e921c64 |
| market_data/universe_trailing_returns.md | 9cbf32fa070454b52319ddff31d3f8c2b6bba8eb69f128c10fd9180a6c0ae02d |
| market_data/universe_trailing_returns.json | 8e0909ff87daf3d2b4b0f7b7d6d9011d043fab10bbe4f88134871cc84a9793dc |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | f9bbe864c38dc274e367cb9eaf2781955396b5b67e366b43e6520abe31437762 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | c3abdf5eb6e643972d7e7f1238aaa5432ce8cdcd71ba986819b0b91b23776bc3 | yes |
| Final briefing | research/final_briefing.md | model-facing | 79dc6a4c9142c8fe89c2547bbfe2042c35174fcfa460a2e126bf8fec73901ceb | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
