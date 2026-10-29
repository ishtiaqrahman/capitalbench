# CapitalBench Report: CB-2026-09-28-1M / official-v3-20260928-1M-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260928-1M-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-28-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-09-28
- Decision deadline: 2026-09-28T13:25:00Z
- Horizon: one month
- Entry date: 2026-09-28
- Exit date: 2026-10-28
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | BIOTECH | 3 | 0.5867 | Post-hike rates elevated with sticky CPI/PPI; mega-cap/tech leadership and weak breadth (RSP lagging SPY); mixed growth signals and scheduled data/FOMC create two-way risk over one-month window. | Further Fed hawkishness or higher yields after data/FOMC minutes pressuring duration and rate-sensitive names; Continued mega-cap concentration leaving small-cap/biotech reversals incomplete; High-vol Asia/semis drawdown risk if growth data disappoints; Oil/commodity volatility spilling into risk appetite |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SP500 | 2 | 0.56 | Narrow mega-cap-led tape: SPY up 1.27% on the week while equal-weight, small caps and 65% of the universe fell over 21 sessions. The Fed hiked to 3.75-4.00% on Sept 16 with 10y at 5.17% and CPI 3.4%/PPI 5.4%, so duration, rate-sensitive defensives and credit are under pressure; the Oct 27-28 FOMC sits inside the window. Cross-sectional dispersion is wide and the pattern is mixed: semis/Taiwan/cyber continuation coexists with broad rate-driven selloffs in bonds, utilities, small caps and financials. Most of these pullbacks look fundamentally rate-driven rather than pure overreaction, so I hold a modest number of eligible reversal candidates and otherwise lean toward SPY. | Oct 27-28 FOMC and Oct 14 CPI could trigger another hawkish repricing that hits high-beta and rate-sensitive candidates; Biotech carries 29% vol and financing sensitivity; its pullback may extend if yields rise further; Narrow mega-cap leadership could persist, making SPY hard to beat for broad or small-cap tilts; Semis/Taiwan/Korea rallies on light volume are vulnerable to sharp reversals given 23-29% drawdowns |
| anthropic-claude-opus-5-5 | anthropic | portfolio | SP500 | 1 | 0.5 | The market is narrow and cap-weighted. SPY rose 0.94% over 21 sessions while RSP fell 4.6%, and only 35% of assets were positive. The Fed hiked to 3.75-4.00%, 10y yields are 5.17%, and inflation is sticky, which pressures duration and rate-sensitive assets. A dense data calendar and an FOMC meeting on Oct 27-28 create two-way risk, and concentrated mega-cap tech leadership could either persist or mean-revert. | A hawkish FOMC on Oct 27-28 or a hot CPI on Oct 14 moves yields sharply; Mega-cap tech concentration unwinds, which hurts SPY relative to broad breadth; A sharp broadening rally in which small caps and financials outperform; An oil supply shock |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Breadth weak with equal-weight and small-caps lagging SPY; tech and select international showing relative strength amid rising rates and mixed macro data. | Rising Treasury yields pressuring rate-sensitive sectors; Weak breadth and equal-weight underperformance; Upcoming labor and inflation data releases |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | SPY is near a 52-week high after a 1.2% up week while equal-weight and small/mid indexes lagged, rates remain elevated after a 25bp hike to 3.75–4.00%, and only ~43% of assets were positive over 5 sessions. Mega-cap/tech strength coexists with rate-sensitive and cyclical drawdowns, so one-month outcomes look mixed rather than a clean continuation or reversal regime. | October 14 CPI and October 27–28 FOMC can reprice duration and growth stocks inside the scoring window.; Continued mega-cap concentration if equal-weight and small-cap lag persists.; High-vol Asia/tech beta (Korea 61% vol, semis 43% vol) can reverse sharply on any growth scare.; Oil’s 5-session drop after a large 21-session gain can spill into energy-linked cyclicals. |
| openai-gpt-6-astra | openai | portfolio | FINANCIALS | 3 | 0.56 | Large relative-return gaps and weak breadth indicate high dispersion, although the supplied dispersion statistic is blank. The rate hike and persistent inflation provide fundamental reasons for some laggards to remain weak. Selective reversal looks more attractive than indiscriminate dip buying or extrapolating technology leadership. Expansionary activity readings support a modest cyclical rebound, but the October inflation releases and exit-day FOMC decision limit conviction. | October inflation releases or the October 28 FOMC decision could raise yields further and extend financing-sensitive underperformance.; Weak breadth may reflect durable concentration in large-cap growth rather than a temporary relative-price overshoot.; PMI expansion may fail to translate into financial-sector credit resilience or metals demand as GDP growth remains modest.; Biotech and mining lack supplied company-level catalysts; their high volatility could overwhelm the small estimated reversal edge. |
| google-gemini-3-1-pro | google | portfolio | METALS_MINING | 3 | 0.58 | The market is showing mixed signals with recent rate hikes and moderate economic growth. | Continued rate hikes could pressure equities.; Economic slowdown could impact cyclical sectors. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 20.31 | 53.599998474121094 | 1.6390939672142344 | 1 |
| OIL | Crude Oil | 148.33 | 166.57000732421875 | 0.1229691048622581 | 2 |
| ENERGY | Energy Sector | 62.04 | 68.45 | 0.10332043842682137 | 3 |
| UTILITIES | Utilities Sector | 39.51 | 42.49 | 0.0754239433054924 | 4 |
| CYBERSECURITY | Cybersecurity | 100.95 | 107.92 | 0.06904408122833083 | 5 |
| CONSUMER_STAPLES | Consumer Staples Sector | 82.06 | 86.84 | 0.05825006093102614 | 6 |
| DIVIDEND | US Dividend Equities | 33.21 | 35.09 | 0.056609454983438834 | 7 |
| SOFTWARE | Software | 106.01 | 111.91 | 0.0556551268748231 | 8 |
| LOW_VOL | US Low Volatility Equities | 71.3 | 75.07 | 0.05287517531556807 | 9 |
| HEALTHCARE | Healthcare Sector | 170.7 | 179.72 | 0.05284124194493267 | 10 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 110.56 | 115.33 | 0.043143994211287895 | 11 |
| MATERIALS | Materials Sector | 49.8 | 51.86 | 0.04136546184738954 | 12 |
| AUSTRALIA | Australia Equities | 28.43 | 29.59000015258789 | 0.04080197511740735 | 13 |
| BROAD_COMMODITIES | Broad Commodities | 19.5 | 20.14 | 0.03282051282051279 | 14 |
| CANADA | Canada Equities | 59.59 | 61.51 | 0.03222017116965925 | 15 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 211.11 | 217.43 | 0.02993699966841934 | 16 |
| LARGE_VALUE | US Large-Cap Value | 251.93 | 258.72 | 0.026951931091970138 | 17 |
| MUNICIPAL_BONDS | Municipal Bonds | 101.17 | 103.76000213623047 | 0.025600495564203518 | 18 |
| FINANCIALS | Financials Sector | 54.84 | 56.13 | 0.023522975929978207 | 19 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 79.32 | 80.99 | 0.02105395864851234 | 20 |
| MEXICO | Mexico Equities | 73.34 | 74.62999725341797 | 0.017589272612734685 | 21 |
| TIPS | Treasury Inflation-Protected Securities | 104.54 | 106.26 | 0.016453032332121698 | 22 |
| BIOTECH | Biotechnology | 155.03 | 157.51 | 0.015996903825066022 | 23 |
| US_DOLLAR | US Dollar | 28.62 | 29.059999465942383 | 0.015373845770173977 | 24 |
| REAL_ESTATE | Real Estate Sector | 41.56 | 42.13 | 0.013715110683349296 | 25 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 90.34 | 91.41000366210938 | 0.011844184880555275 | 26 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 90.0 | 90.85 | 0.009444444444444366 | 27 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 103.21 | 104.07 | 0.00833252591803113 | 28 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 95.12 | 95.89 | 0.00809503784693022 | 29 |
| REGIONAL_BANKS | Regional Banks | 71.55 | 72.11 | 0.007826694619147423 | 30 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.94 | 47.279998779296875 | 0.00724326329989089 | 31 |
| SMALL_VALUE | US Small-Cap Value | 213.49 | 214.81 | 0.006182959389198439 | 32 |
| MID_CAP | US Mid-Cap Stocks | 72.99 | 73.35 | 0.004932182490752224 | 33 |
| SP500 | S&P 500 | 771.35 | 772.31 | 0.0012445712063264835 | 34 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.62 | 91.66 | 0.00043658589827533234 | 35 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 36 |
| UNITED_KINGDOM | United Kingdom Equities | 47.32 | 47.29 | -0.000633981403212247 | 37 |
| TOTAL_US_MARKET | Total US Stock Market | 379.77 | 379.17 | -0.0015799036258787869 | 38 |
| SMALL_CAP | US Small-Cap Stocks | 281.97 | 281.29 | -0.0024116040713551 | 39 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 77.86 | 77.59 | -0.0034677626509118653 | 40 |
| YEN | Japanese Yen | 58.3 | 58.08000183105469 | -0.003773553498204296 | 41 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 92.18 | 91.79000091552734 | -0.004230842747588004 | 42 |
| COPPER | Copper | 40.61 | 40.33000183105469 | -0.006894808395599861 | 43 |
| INDUSTRIALS | Industrials Sector | 170.43 | 168.49 | -0.011382972481370657 | 44 |
| EUROPE | Europe Equities | 88.63 | 87.31 | -0.014893376960397053 | 45 |
| EURO | Euro | 105.15 | 103.02999877929688 | -0.020161685408493835 | 46 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.84 | 70.34 | -0.020879732739420898 | 47 |
| INDIA | India Equities | 47.86 | 46.79 | -0.022356874216464706 | 48 |
| BROAD_AI_TECH | Broad AI Technology | 65.97 | 64.4 | -0.02379869637714105 | 49 |
| NASDAQ100 | Nasdaq 100 | 744.5 | 725.61 | -0.025372733378106083 | 50 |
| LARGE_GROWTH | US Large-Cap Growth | 126.25 | 123.01 | -0.025663366336633575 | 51 |
| TECHNOLOGY | Technology Sector | 196.27 | 191.0 | -0.026850766800835646 | 52 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 213.81 | 207.74 | -0.028389691782423565 | 53 |
| JAPAN | Japan Equities | 97.93 | 94.99 | -0.030021443888491928 | 54 |
| BITCOIN_ETF | Bitcoin ETF | 47.57 | 46.13999938964844 | -0.030060975622273722 | 55 |
| SOUTH_AFRICA | South Africa Equities | 66.48 | 64.36000061035156 | -0.03188928083105358 | 56 |
| MOMENTUM | US Momentum Equities | 318.5 | 303.5 | -0.04709576138147564 | 57 |
| AGRICULTURE | Agriculture Commodities | 28.54 | 27.110000610351562 | -0.05010509424136078 | 58 |
| GOLD | Gold | 80.66 | 76.57 | -0.050706669972725105 | 59 |
| TAIWAN | Taiwan Equities | 114.78 | 108.94000244140625 | -0.050879922970846425 | 60 |
| EMERGING_MARKETS | Emerging Markets | 60.16 | 57.02 | -0.05219414893617014 | 61 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 124.42 | 116.66 | -0.062369393988104815 | 62 |
| SEMICONDUCTORS | Semiconductors | 606.56 | 567.67 | -0.0641156686890002 | 63 |
| METALS_MINING | Metals and Mining | 108.33 | 101.31 | -0.06480199390750485 | 64 |
| CHINA | China Equities | 52.62 | 49.04 | -0.06803496769289241 | 65 |
| SOLAR | Solar Energy | 44.06 | 40.98 | -0.06990467544257839 | 66 |
| BRAZIL | Brazil Equities | 36.82 | 33.619998931884766 | -0.08690931743930563 | 67 |
| COMMUNICATIONS | Communication Services Sector | 112.96 | 103.14 | -0.0869334277620396 | 68 |
| SOUTH_KOREA | South Korea Equities | 187.18 | 165.91000366210938 | -0.11363391568485215 | 69 |
| SILVER | Silver | 58.14 | 49.060001373291016 | -0.15617472698157864 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | BIOTECH | 35.0 | 0.015996903825066022 | 0.0055989163387731074 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 65.0 | 0.0012445712063264835 | 0.0008089712841122143 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5-5 | SP500 | 100.0 | 0.0012445712063264835 | 0.0012445712063264835 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | METALS_MINING | 35.0 | -0.06480199390750485 | -0.022680697867626696 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SOLAR | 35.0 | -0.06990467544257839 | -0.024466636404902434 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 30.0 | -0.028389691782423565 | -0.008516907534727069 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | FINANCIALS | 35.0 | 0.023522975929978207 | 0.008233041575492372 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-6-astra | BIOTECH | 35.0 | 0.015996903825066022 | 0.0055989163387731074 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | METALS_MINING | 30.0 | -0.06480199390750485 | -0.019440598172251456 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 100.0 | 0.0012445712063264835 | 0.0012445712063264835 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | BIOTECH | 35.0 | 0.015996903825066022 | 0.0055989163387731074 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | SMALL_CAP | 35.0 | -0.0024116040713551 | -0.000844061424974285 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | FINANCIALS | 30.0 | 0.023522975929978207 | 0.007056892778993462 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 100.0 | 0.0012445712063264835 | 0.0012445712063264835 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | BIOTECH | 3 | 0.5867 | 0.015996903825066022 | 0.011811747692792285 | 0.010567176486465801 | 1.627282219521442 |  | True | True |
| anthropic-claude-fable-5-1 | SP500 | 2 | 0.56 | 0.0012445712063264835 | 0.006407887622885322 | 0.005163316416558838 | 1.6326860795913491 |  | True | True |
| anthropic-claude-opus-5-5 | SP500 | 1 | 0.5 | 0.0012445712063264835 | 0.0012445712063264835 | 0.0 | 1.637849396007908 |  | False | True |
| xai-grok-4-3 | SP500 | 1 | 0.5 | 0.0012445712063264835 | 0.0012445712063264835 | 0.0 | 1.637849396007908 |  | False | True |
| xai-grok-4-6 | SP500 | 1 | 0.5 | 0.0012445712063264835 | 0.0012445712063264835 | 0.0 | 1.637849396007908 |  | False | True |
| openai-gpt-6-astra | FINANCIALS | 3 | 0.56 | 0.023522975929978207 | -0.005608640257985976 | -0.00685321146431246 | 1.6447026074722204 |  | False | False |
| google-gemini-3-1-pro | METALS_MINING | 3 | 0.58 | -0.06480199390750485 | -0.055664241807256196 | -0.05690881301358268 | 1.6947582090214905 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 4f254576c0177b39155a4d033dfdb4ca1efece2edd37157adf1c0b0bc0464b0e |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | 206060a050294b67445c196e19be7f8aeccc0efdbc8584c468ebf636d792b11d |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 7a82cc37589c521dd43ff3e6e070a13337cb0324e076409dc06d60211b4401e1 |
| market_data/universe_decision_context.md | 67f5959a228a3e157dacf78f3d68f384dc0522dbb20843172567cd7ba5120a61 |
| market_data/universe_decision_context.json | b778f2f2bebe80877e9ed952b41fb8640da62d8d2ba6ab7897637bd760efaba9 |
| market_data/decision_context_source_history.json | 6c65083ea80e2aa06edd9178418f6908ccef900edd8198da0d80fcbd8f243f6c |
| market_data/universe_quality_evidence.md | dcf8db928652e67e1838ae68a911815a45a8ed86ecdffa12ab8af89e5df75d14 |
| market_data/universe_quality_evidence.json | d6d58d4809be82e2be571c74e319213306628e0418a2c95e0fd1c5762ba24c0a |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | a062a138f864d51f12aae7c0d557abed209d85a3ef7e3839cc97896d7f227c5c | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 9c015ff6bde06649164e5bb8ce53ef7a50f0fe07a4ac3c394dc152d7a019a162 | yes |
| Final briefing | research/final_briefing.md | model-facing | 4f254576c0177b39155a4d033dfdb4ca1efece2edd37157adf1c0b0bc0464b0e | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
