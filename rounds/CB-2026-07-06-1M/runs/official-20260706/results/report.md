# CapitalBench Report: CB-2026-07-06-1M / official-20260706

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260706
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-06-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-06
- Decision deadline: 2026-07-07T07:30:00Z
- Horizon: one month
- Entry date: 2026-07-06
- Exit date: 2026-08-06
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 5 | 0.55 | Overweight sectors showing durable outperformance and near-term catalysts while keeping a defensive and index anchor for stability. | Bank earnings (JPM/WFC) or CPI July 14 disappoint, reversing financials leadership; Momentum/cyclical rotation reverses given narrow market breadth near all-time highs; Sticky core PCE (3.4%) keeps Fed on hold and pressures rate-sensitive cyclicals; Healthcare policy or drug-pricing headlines undercut defensive allocation |
| anthropic-claude-opus-4-7 | anthropic | portfolio | FINANCIALS | 5 | 0.55 | Overweight financials into JPM/WFC earnings, industrials/defense with strong breadth, healthcare for defensive ballast, and equal-weight SPX to diversify away mega-cap concentration risk. | Bank earnings disappointment or CPI hotter-than-expected pressuring cyclicals; Mega-cap tech leadership resumes, causing equal-weight/value tilt to underperform SPY; Sector rotation reversal; recent industrials/financials strength could mean-revert; FOMC minutes/July 29 meeting introducing hawkish surprise hitting rate-sensitive sectors |
| xai-grok-4-3 | xai | portfolio | SMALL_CAP | 4 | 0.62 | Concentrated 25% weights in four sectors with recent strength and direct exposure to potential Fed easing and domestic growth catalysts before the August 6 close. | Further downside surprises in July CPI or FOMC minutes could delay rate-cut expectations and pressure cyclicals; Earnings disappointments from regional banks or industrial names scheduled in mid-July could trigger sector rotation; OPEC+ supply increase may keep energy prices soft, indirectly weighing on broader risk appetite |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.65 | Allocating to semiconductors and financials based on upcoming earnings catalysts, balanced with small caps for broader market exposure. | TSMC earnings could disappoint, leading to a sharp reversal in semiconductor stocks.; Bank earnings might reveal credit weakness or lower net interest income, hurting financials.; Small caps are highly sensitive to economic data and could underperform if growth slows. |
| openai-gpt-5-5 | openai | portfolio | TAIWAN | 5 | 0.58 | I favor a pro-risk, catalyst-driven allocation over the S&P 500 benchmark, emphasizing areas with scheduled July earnings or sales events and recent relative strength backed by supplied fundamentals. The main bet is that AI semiconductor leadership and cyclical earnings breadth persist through the one-month window. | A hotter-than-expected CPI or hawkish July FOMC communication could pressure high-beta semiconductor, Taiwan, and cybersecurity holdings.; TSMC, Broadcom-linked sentiment, or broader AI capital-spending expectations could disappoint after large prior gains, causing a sharp reversal in semiconductor-heavy positions.; Weak payrolls and downward revisions could shift investor focus from solid ISM activity to recession risk, hurting financials and cyclical equity exposures.; Recent momentum in cybersecurity, aerospace-defense, and Taiwan may be crowded; a rotation back into defensive or mega-cap benchmark constituents could reduce relative returns.; Geopolitical or currency stress in Taiwan or broader Asia could specifically hurt Taiwan and semiconductor supply-chain exposures. |
| anthropic-claude-fable-5 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.5 | Concentrated in AI-chip beneficiaries with confirmed near-window catalysts (TSMC earnings/sales, Broadcom-Apple deal, component shortages), balanced by financials into earnings and healthcare/industrials to manage beta. | TSMC or bank earnings disappoint versus elevated expectations, hitting SMH/EWT/XLF within the window; Hot June CPI (July 14) or hawkish FOMC on July 29 given 3.4% core PCE could compress high-beta tech multiples; Weak payrolls (+57k with negative revisions) could morph into growth-scare selloff hurting cyclicals and financials; Semiconductor and Taiwan positions are crowded after large trailing gains; reversal/positioning risk is elevated (SMH 30d vol ~66%) |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 104.35 | 118.87000274658203 | 0.13914712742292323 | 1 |
| ENERGY | Energy Sector | 53.13 | 58.15999984741211 | 0.09467343962755703 | 2 |
| COPPER | Copper | 37.84 | 40.7599983215332 | 0.07716697467053901 | 3 |
| CHINA | China Equities | 52.02 | 55.904998779296875 | 0.0746827908361567 | 4 |
| BROAD_COMMODITIES | Broad Commodities | 16.1 | 17.229999542236328 | 0.07018630697120032 | 5 |
| AUSTRALIA | Australia Equities | 28.33 | 30.15999984741211 | 0.06459582941800601 | 6 |
| ETHEREUM_ETF | Ethereum ETF | 13.55 | 14.399999618530273 | 0.06273059915352563 | 7 |
| SOFTWARE | Software | 94.79 | 99.41999816894531 | 0.04884479553692689 | 8 |
| CANADA | Canada Equities | 58.06 | 60.70000076293945 | 0.04547021637856452 | 9 |
| DIVIDEND | US Dividend Equities | 32.24 | 33.7 | 0.045285359801488845 | 10 |
| METALS_MINING | Metals and Mining | 106.08 | 110.3499984741211 | 0.04025262513311745 | 11 |
| CYBERSECURITY | Cybersecurity | 92.91 | 96.38999938964844 | 0.03745559562639578 | 12 |
| LARGE_VALUE | US Large-Cap Value | 247.24 | 256.12 | 0.03591651836272436 | 13 |
| SOUTH_AFRICA | South Africa Equities | 64.63 | 66.87999725341797 | 0.03481351158003987 | 14 |
| FINANCIALS | Financials Sector | 56.14 | 57.81 | 0.02974706091913082 | 15 |
| BRAZIL | Brazil Equities | 34.92 | 35.810001373291016 | 0.025486866359994753 | 16 |
| SP500 | S&P 500 | 751.28 | 768.56 | 0.023000745394526678 | 17 |
| YEN | Japanese Yen | 56.59 | 57.88999938964844 | 0.022972245796933022 | 18 |
| UNITED_KINGDOM | United Kingdom Equities | 47.22 | 48.29999923706055 | 0.022871648391794785 | 19 |
| EUROPE | Europe Equities | 89.97 | 91.83000183105469 | 0.02067357820445359 | 20 |
| GOLD | Gold | 78.3 | 79.87000274658203 | 0.020051120646003007 | 21 |
| TOTAL_US_MARKET | Total US Stock Market | 371.67 | 379.07 | 0.01991013533510899 | 22 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 215.0 | 218.5800018310547 | 0.01665117130723104 | 23 |
| HEALTHCARE | Healthcare Sector | 161.96 | 164.45 | 0.015374166460854433 | 24 |
| REGIONAL_BANKS | Regional Banks | 75.56 | 76.48999786376953 | 0.012308071251581953 | 25 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.1 | 85.11 | 0.012009512485136709 | 26 |
| REAL_ESTATE | Real Estate Sector | 44.29 | 44.810001373291016 | 0.011740830284285853 | 27 |
| BITCOIN_ETF | Bitcoin ETF | 36.12 | 36.4900016784668 | 0.010243678805835987 | 28 |
| TECHNOLOGY | Technology Sector | 183.57 | 185.33 | 0.009587623249986521 | 29 |
| SMALL_VALUE | US Small-Cap Value | 221.74 | 223.83 | 0.009425453233516734 | 30 |
| COMMUNICATIONS | Communication Services Sector | 110.21 | 111.18 | 0.008801379185191971 | 31 |
| EURO | Euro | 105.4877475704 | 106.30000305175781 | 0.007699998341662573 | 32 |
| INDIA | India Equities | 49.88 | 50.119998931884766 | 0.00481152630081727 | 33 |
| MID_CAP | US Mid-Cap Stocks | 76.42 | 76.75 | 0.0043182412980895535 | 34 |
| LARGE_GROWTH | US Large-Cap Growth | 123.0 | 123.5 | 0.004065040650406582 | 35 |
| MATERIALS | Materials Sector | 51.98 | 52.16999816894531 | 0.0036552167938690427 | 36 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.1578317509 | 91.45 | 0.0032050811596571194 | 37 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.89 | 72.12000274658203 | 0.003199370518598199 | 38 |
| LOW_VOL | US Low Volatility Equities | 76.0287637566 | 76.26 | 0.003041431058122823 | 39 |
| MEXICO | Mexico Equities | 76.43 | 76.62999725341797 | 0.0026167375823362704 | 40 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.01 | 118.1 | 0.0007626472332851186 | 41 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 42 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.4848637146 | 79.45999908447266 | -0.0003128222024336713 | 43 |
| JAPAN | Japan Equities | 95.27 | 95.1500015258789 | -0.0012595620249931105 | 44 |
| EMERGING_MARKETS | Emerging Markets | 60.07 | 59.959999084472656 | -0.0018312121779148205 | 45 |
| SMALL_CAP | US Small-Cap Stocks | 298.9 | 298.25 | -0.002174640347942347 | 46 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 250.78 | 249.99000549316406 | -0.003150149560714355 | 47 |
| AGRICULTURE | Agriculture Commodities | 27.54 | 27.43000030517578 | -0.0039941791875169885 | 48 |
| INDUSTRIALS | Industrials Sector | 185.56 | 184.76 | -0.004311273981461583 | 49 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.1008538632 | 47.88999938964844 | -0.004383591072026238 | 50 |
| US_DOLLAR | US Dollar | 28.32 | 28.190000534057617 | -0.004590376622259251 | 51 |
| SILVER | Silver | 56.11 | 55.849998474121094 | -0.004633782318283819 | 52 |
| TIPS | Treasury Inflation-Protected Securities | 107.6994541582 | 106.87000274658203 | -0.007701537747810572 | 53 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.3187572871 | 97.43000030517578 | -0.009039546536669163 | 54 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.8588968022 | 92.94999694824219 | -0.009683683539060128 | 55 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.9341941104 | 93.01000213623047 | -0.009838717230951421 | 56 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.9312557656 | 94.94999694824219 | -0.010228770691331657 | 57 |
| NASDAQ100 | Nasdaq 100 | 722.82 | 714.65 | -0.011302952325613624 | 58 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.2787369575 | 105.66000366210938 | -0.015089041326352581 | 59 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.203399734 | 106.36000061035156 | -0.017036425178692416 | 60 |
| BROAD_AI_TECH | Broad AI Technology | 63.84 | 61.95000076293945 | -0.02960525120708879 | 61 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.1078146032 | 82.5199966430664 | -0.03040634954849719 | 62 |
| BIOTECH | Biotechnology | 160.81 | 154.5 | -0.03923885330514276 | 63 |
| MOMENTUM | US Momentum Equities | 321.71 | 308.17 | -0.04208759441733223 | 64 |
| UTILITIES | Utilities Sector | 45.3 | 43.380001068115234 | -0.042384082381562105 | 65 |
| TAIWAN | Taiwan Equities | 107.27 | 101.9800033569336 | -0.049314781794223994 | 66 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 130.11 | 123.19999694824219 | -0.05310893130241967 | 67 |
| SEMICONDUCTORS | Semiconductors | 604.3 | 571.47998046875 | -0.054310805115422744 | 68 |
| SOLAR | Solar Energy | 57.54 | 51.25 | -0.10931525895029548 | 69 |
| SOUTH_KOREA | South Korea Equities | 189.85 | 164.1199951171875 | -0.1355280741786279 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 25.0 | -0.054310805115422744 | -0.013577701278855686 | AI capex cycle intact: Broadcom-Apple silicon deals, TSMC guiding strong Q2 with earnings July 16, SK Hynix capacity expansion, and ISM shortages in electronic/memory components signal demand exceeding supply. |
| anthropic-claude-fable-5 | FINANCIALS | 20.0 | 0.02974706091913082 | 0.005949412183826164 | Bank earnings kick off July 14 (JPM, WFC) into strong capital markets activity; recent strength supported by steady Fed policy and solid economic activity per FOMC statement. |
| anthropic-claude-fable-5 | INDUSTRIALS | 15.0 | -0.004311273981461583 | -0.0006466910972192375 | ISM manufacturing at 53.3 with New Orders 56.0 shows expanding activity; defense demand (ITA strength) and broad cyclical support. |
| anthropic-claude-fable-5 | HEALTHCARE | 15.0 | 0.015374166460854433 | 0.002306124969128165 | Defensive with catalyst momentum via biotech strength; low beta ballast against soft labor data while still participating in rotation. |
| anthropic-claude-fable-5 | TAIWAN | 25.0 | -0.049314781794223994 | -0.012328695448555999 | TSMC-heavy exposure into its July 16 earnings with guidance of 65.5-67.5% gross margin and June monthly sales July 10; direct beneficiary of AI silicon demand cited across the briefing. |
| anthropic-claude-opus-4-7 | FINANCIALS | 25.0 | 0.02974706091913082 | 0.007436765229782705 | Big bank earnings (JPM, WFC) July 14 with strong sector momentum; steep yield curve and low vol support. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 20.0 | -0.004311273981461583 | -0.0008622547962923166 | Strong breadth, ISM Manufacturing still expansionary, low drawdown, high up-day share. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 15.0 | -0.003150149560714355 | -0.0004725224341071532 | Geopolitical tailwinds and strong recent breadth; 0% distance from 52w high with sustained defense spending. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 20.0 | 0.015374166460854433 | 0.0030748332921708868 | Defensive sector with recent breakout, low beta 0.36 offering ballast against tech reversal risk. |
| anthropic-claude-opus-4-7 | EQUAL_WEIGHT_SP500 | 20.0 | 0.01665117130723104 | 0.003330234261446208 | Broad breadth participation while cap-weighted index concentration risks a mega-cap pullback. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | 0.02974706091913082 | 0.007436765229782705 | Strong broad-based momentum (+7.7% 30d, +5.6% vs SPY), major bank earnings July 14 (JPM, WFC) as near-term catalyst, low volatility and high up-day share; benefits from steady rates and solid growth backdrop. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 20.0 | -0.004311273981461583 | -0.0008622547962923166 | Broadening cyclical leadership (+6.8% 30d, +4.7% vs SPY), highest up-day share, supported by solid ISM manufacturing/services and expanding activity; independent fundamental support beyond price. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 20.0 | 0.015374166460854433 | 0.0030748332921708868 | Defensive with recent outperformance (+6.3% 30d, +4.2% vs SPY), low beta 0.36 provides ballast against a market near highs with narrow breadth. |
| anthropic-claude-opus-4-8 | SP500 | 20.0 | 0.023000745394526678 | 0.004600149078905336 | Core benchmark exposure to limit tracking error while capturing continued broad equity strength near all-time highs with supportive macro. |
| anthropic-claude-opus-4-8 | AEROSPACE_DEFENSE | 15.0 | -0.003150149560714355 | -0.0004725224341071532 | Strong momentum (+9.4% 30d, +7.3% vs SPY) at 52w high, supported by durable defense-budget and geopolitical tailwinds; adds industrial cyclical exposure. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | -0.054310805115422744 | -0.0217243220461691 | Semiconductors have strong catalysts with TSMC's upcoming earnings and Broadcom's Apple deal, despite recent volatility. |
| google-gemini-3-1-pro | FINANCIALS | 30.0 | 0.02974706091913082 | 0.008924118275739246 | Financials are supported by upcoming Q2 earnings from major banks like JPMorgan and Wells Fargo, and recent strong performance. |
| google-gemini-3-1-pro | SMALL_CAP | 30.0 | -0.002174640347942347 | -0.0006523921043827041 | Small caps show strong recent momentum and may benefit from a broadening market if large-cap tech consolidates. |
| openai-gpt-5-5 | TAIWAN | 30.0 | -0.049314781794223994 | -0.014794434538267197 | Taiwan offers concentrated semiconductor supply-chain exposure with near-term TSMC monthly sales and Q2 earnings catalysts inside the scoring window; recent strength has independent support from supplied TSMC guidance but remains reversal-prone. |
| openai-gpt-5-5 | SEMICONDUCTORS | 25.0 | -0.054310805115422744 | -0.013577701278855686 | Semiconductor exposure is supported by AI infrastructure demand datapoints, Broadcom's Apple silicon agreements, and TSMC's imminent reporting calendar, though its high beta and large prior gains increase drawdown risk. |
| openai-gpt-5-5 | FINANCIALS | 20.0 | 0.02974706091913082 | 0.005949412183826164 | Financials have near-term large-bank earnings catalysts, solid recent breadth, and lower beta than the S&P 500; they can benefit if growth remains solid while rate expectations do not deteriorate sharply. |
| openai-gpt-5-5 | CYBERSECURITY | 15.0 | 0.03745559562639578 | 0.005618339343959366 | Cybersecurity has shown recent relative strength with broader AI/software demand still relevant, and it provides technology-adjacent upside with less direct semiconductor concentration. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 10.0 | -0.003150149560714355 | -0.0003150149560714355 | Aerospace and defense is near a 52-week high with strong one-month relative performance and tends to have idiosyncratic support from defense budgets and aircraft demand, while still participating in equity risk appetite. |
| xai-grok-4-3 | SMALL_CAP | 25.0 | -0.002174640347942347 | -0.0005436600869855868 | Weak June payrolls and downward revisions increase odds of near-term Fed easing, which historically supports domestic small-cap outperformance over the next month. |
| xai-grok-4-3 | FINANCIALS | 25.0 | 0.02974706091913082 | 0.007436765229782705 | Financials posted the strongest 30-day return among major sectors and stand to benefit from any steepening yield curve or improved credit conditions following soft labor data. |
| xai-grok-4-3 | INDUSTRIALS | 25.0 | -0.004311273981461583 | -0.0010778184953653958 | Industrials showed solid 30-day gains and are positioned for domestic growth sensitivity amid potential policy support before the August 6 exit. |
| xai-grok-4-3 | AEROSPACE_DEFENSE | 25.0 | -0.003150149560714355 | -0.0007875373901785887 | Aerospace and defense delivered the second-highest 30-day sector return and offers defensive growth exposure with limited direct sensitivity to the softening labor print. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | FINANCIALS | 5 | 0.55 | 0.02974706091913082 | 0.013776970370459458 | -0.00922377502406722 | 0.12537015705246377 |  | False | True |
| anthropic-claude-opus-4-7 | FINANCIALS | 5 | 0.55 | 0.02974706091913082 | 0.012507055553000329 | -0.010493689841526349 | 0.1266400718699229 |  | False | True |
| xai-grok-4-3 | SMALL_CAP | 4 | 0.62 | -0.002174640347942347 | 0.0050277492572531335 | -0.017972996137273545 | 0.1341193781656701 |  | False | True |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.65 | -0.054310805115422744 | -0.013452595874812559 | -0.03645334126933924 | 0.1525997232977358 |  | False | False |
| openai-gpt-5-5 | TAIWAN | 5 | 0.58 | -0.049314781794223994 | -0.017119399245408787 | -0.04012014463993546 | 0.15626652666833202 |  | False | False |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 5 | 0.5 | -0.054310805115422744 | -0.018297550671676592 | -0.04129829606620327 | 0.15744467809459983 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | c627cdc562f0e4df28e30a26c4430940d99e1dec1a74aa429efe4ff198e69a43 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 7858eef0aa73ea38b28daacc4aaa57e57b110de6456378f1697ff1cd79ca213c |
| manifest.yaml | 2cf491cad746a6543f94db37230128c2b2368016a8b1bdcb1b5871662292205b |
| market_data/universe_trailing_returns.csv | 3e2e4e99f24d6a3c98a20d51457333556d5962ad6d56472a60786180de1f12e7 |
| market_data/universe_trailing_returns.md | a1452a84ba42c5875aa782791e8f85ac371186ffe14471927800ab618337f8c6 |
| market_data/universe_trailing_returns.json | 983f0f42c1747a2fef69d61fbaec872b7d05e991f458f0fabd55fa68e2e6ea9b |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | f98201443c62b5147116460ebb6681ffde2ed5bd068a6b425c093e7d3ffc9f9a | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 530740ee6dc2fcd360a8331b3cfe4621982b9b06ead770387a90b149b9ce7a96 | yes |
| Final briefing | research/final_briefing.md | model-facing | c627cdc562f0e4df28e30a26c4430940d99e1dec1a74aa429efe4ff198e69a43 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
