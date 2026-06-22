# CapitalBench Report: CB-2026-06-12-1W / official-20260612-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260612-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 12 2026 One-Week Portfolio Round
- Description: One-week CapitalBench portfolio evaluation round scored from the latest available June 11, 2026 adjusted-close snapshot to the June 18, 2026 adjusted close, because June 19, 2026 was a U.S. market holiday.
- Decision date: 2026-06-12
- Decision deadline: 2026-06-12T23:30:00Z
- Horizon: one week
- Entry date: 2026-06-11
- Exit date: 2026-06-18
- Entry rule: Use adjusted close on Thursday, June 11, 2026 as the latest available pre-open June 12 entry snapshot for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Thursday, June 18, 2026 for each selected option because Friday, June 19, 2026 was a U.S. market holiday; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | anthropic | portfolio | NASDAQ100 | 5 | 0.45 | Pro-risk tilt toward growth, semis, momentum and small value into an expected benign FOMC hold, with energy as an inflation hedge. | Hawkish FOMC dots or Powell press conference on June 17 despite a hold, hitting growth and small caps; Hot May retail sales (June 17) reigniting inflation/rate fears; Oil price reversal dragging the energy hedge while not helping growth holdings; Weak 20-year auction pushing long yields higher, pressuring high-duration equities |
| openai-gpt-5-5 | openai | portfolio | REGIONAL_BANKS | 5 | 0.57 | I favor a one-week risk-on broadening trade rather than benchmark-like large-cap exposure. The allocation emphasizes domestic cyclicals and semiconductors, with consumer staples as a partial hedge against an inflation- or Fed-driven reversal. | The FOMC statement or press conference could be more hawkish than expected, pressuring small caps, banks, and semiconductors.; Retail sales, jobless claims, or industrial production could disappoint and revive growth-slowdown concerns for cyclical holdings.; Elevated headline CPI, PPI, and oil prices could push Treasury yields higher and compress equity multiples.; Regional banks could underperform if deposit, credit-quality, or commercial-real-estate concerns resurface during the week.; The recent Nasdaq and semiconductor rebound could fail, causing high-beta AI and chip exposure to lag defensive sectors. |
| google-gemini-3-1-pro | google | portfolio | TECHNOLOGY | 3 | 0.65 | Overweight growth sectors ahead of a likely neutral FOMC decision, balanced with broad market exposure. | A hawkish surprise from the FOMC meeting causing a spike in Treasury yields.; Technology sector volatility due to elevated forward valuations.; Unexpected weakness in retail sales or industrial production data impacting broad market sentiment. |
| xai-grok-4-3 | xai | portfolio | CONSUMER_STAPLES | 3 | 0.55 | Prioritizes sectors with recent outperformance and lower beta to volatility around FOMC and retail sales releases within the one-week window. | Hotter-than-expected retail sales or industrial production data could pressure defensives.; Any hawkish FOMC surprise on June 17 could lift yields and weigh on equity valuations.; Reversal in recent factor rotation away from value and low-vol toward growth. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | CONSUMER_STAPLES | 5 | 0.55 | Tilt defensive into FOMC and sticky-inflation week: staples, low-vol, healthcare, and aerospace/defense led on relative strength while tech sold off; short Treasuries provide ballast. | Dovish surprise or soft-landing tone at FOMC could spark a tech/growth rally that leaves defensives underperforming the benchmark; Hot retail sales (June 17) or hawkish Fed could pressure rate-sensitive defensives like staples and healthcare; Crowded defensive trade may mean-revert if VIX continues falling and risk appetite returns; Concentration in low-beta names caps upside if S&P 500 rebounds sharply from the prior week's -2.55% drop |
| anthropic-claude-opus-4-7 | anthropic | portfolio | CONSUMER_STAPLES | 5 | 0.5 | Defensive-momentum tilt into a catalyst-heavy week (FOMC June 17, retail sales, BOE, BOJ). Avoid mega-cap tech given recent drawdown (-3% to -9% 1w in QQQ/IGV/SMH) and stretched valuations. | Dovish FOMC surprise sparks a tech/growth squeeze that leaves defensive tilt behind SPY benchmark; Hot May retail sales print on 6/17 lifts cyclicals/discretionary disproportionately; Regional banks reverse on weaker CRE/credit headlines or curve flattening; Staples/healthcare rotation unwinds if VIX continues falling and risk-on resumes |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOUTH_KOREA | South Korea Equities | 198.94 | 219.2 | 0.10183975067859641 | 1 |
| SEMICONDUCTORS | Semiconductors | 609.45 | 659.88 | 0.08274673886290906 | 2 |
| TAIWAN | Taiwan Equities | 102.45 | 109.99 | 0.07359687652513403 | 3 |
| MOMENTUM | US Momentum Equities | 319.01 | 338.52 | 0.061157957430801435 | 4 |
| BIOTECH | Biotechnology | 132.74 | 140.72 | 0.060117522977248594 | 5 |
| TECHNOLOGY | Technology Sector | 183.21 | 191.44 | 0.04492112875934717 | 6 |
| BROAD_AI_TECH | Broad AI Technology | 63.95 | 66.8 | 0.044566067240031204 | 7 |
| JAPAN | Japan Equities | 92.18 | 96.26 | 0.04426122803211108 | 8 |
| INDIA | India Equities | 47.79 | 49.58 | 0.037455534630675746 | 9 |
| INDUSTRIALS | Industrials Sector | 175.15 | 180.91 | 0.03288609763060224 | 10 |
| NASDAQ100 | Nasdaq 100 | 717.12 | 740.62 | 0.03276996876394467 | 11 |
| EMERGING_MARKETS | Emerging Markets | 59.1 | 60.77 | 0.028257191201353615 | 12 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 130.24 | 133.17 | 0.022496928746928546 | 13 |
| FINANCIALS | Financials Sector | 52.62 | 53.57 | 0.01805397187381219 | 14 |
| SMALL_CAP | US Small-Cap Stocks | 290.41 | 295.59 | 0.017836851348093985 | 15 |
| UTILITIES | Utilities Sector | 44.05 | 44.76 | 0.01611804767309888 | 16 |
| TOTAL_US_MARKET | Total US Stock Market | 364.3 | 369.99 | 0.015618995333516406 | 17 |
| ETHEREUM_ETF | Ethereum ETF | 12.7 | 12.88 | 0.014173228346456845 | 18 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.31 | 72.31 | 0.01402327864254671 | 19 |
| LARGE_GROWTH | US Large-Cap Growth | 121.57 | 123.19 | 0.013325656000658048 | 20 |
| AGRICULTURE | Agriculture Commodities | 26.3 | 26.63 | 0.012547528517110162 | 21 |
| US_DOLLAR | US Dollar | 27.95 | 28.3 | 0.012522361359570633 | 22 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 236.04 | 238.99 | 0.012497881714963688 | 23 |
| SP500 | S&P 500 | 737.76 | 746.74 | 0.012171980047712028 | 24 |
| MATERIALS | Materials Sector | 51.22 | 51.81 | 0.011518937914877014 | 25 |
| LARGE_VALUE | US Large-Cap Value | 239.78 | 242.18 | 0.010009175077154042 | 26 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.98 | 86.75 | 0.008955571063037793 | 27 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.3 | 117.16 | 0.007394668959587181 | 28 |
| SOUTH_AFRICA | South Africa Equities | 66.28 | 66.74 | 0.006940253470126612 | 29 |
| SMALL_VALUE | US Small-Cap Value | 215.81 | 216.87 | 0.004911727908808672 | 30 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.27 | 96.73 | 0.0047782279006960415 | 31 |
| MID_CAP | US Mid-Cap Stocks | 75.5 | 75.78 | 0.0037086092715232777 | 32 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.18 | 48.35 | 0.0035284350352844385 | 33 |
| GOLD | Gold | 79.13 | 79.33 | 0.002527486414760638 | 34 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.06 | 107.33 | 0.0025219503082383188 | 35 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 209.75 | 209.96 | 0.0010011918951131626 | 36 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.48 | 91.57 | 0.0009838216003497102 | 37 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.94 | 80.01 | 0.0008756567425569628 | 38 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.34 | 94.36 | 0.0002119991520033171 | 39 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.88 | 98.9 | 0.0002022653721684975 | 40 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 41 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.08 | 109.07 | -9.167583425018222e-05 | 42 |
| MEXICO | Mexico Equities | 77.34 | 77.33 | -0.00012929919834503423 | 43 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.52 | 94.48 | -0.0004231908590773825 | 44 |
| TIPS | Treasury Inflation-Protected Securities | 109.6 | 109.39 | -0.0019160583941605358 | 45 |
| COPPER | Copper | 38.94 | 38.86 | -0.0020544427324088455 | 46 |
| REGIONAL_BANKS | Regional Banks | 72.35 | 71.72 | -0.008707671043538312 | 47 |
| YEN | Japanese Yen | 57.43 | 56.85 | -0.010099251262406406 | 48 |
| LOW_VOL | US Low Volatility Equities | 73.84 | 73.09 | -0.010157096424702083 | 49 |
| EURO | Euro | 106.88 | 105.77 | -0.010385479041916112 | 50 |
| CANADA | Canada Equities | 58.49 | 57.87 | -0.010600102581638016 | 51 |
| CYBERSECURITY | Cybersecurity | 85.47 | 84.54 | -0.010881010881010789 | 52 |
| METALS_MINING | Metals and Mining | 118.35 | 117.02 | -0.011237853823405142 | 53 |
| BITCOIN_ETF | Bitcoin ETF | 36.05 | 35.62 | -0.01192787794729544 | 54 |
| EUROPE | Europe Equities | 89.46 | 88.27 | -0.013302034428794962 | 55 |
| AUSTRALIA | Australia Equities | 28.96 | 28.56 | -0.013812154696132617 | 56 |
| SOFTWARE | Software | 90.92 | 89.09 | -0.02012758468983722 | 57 |
| DIVIDEND | US Dividend Equities | 32.53 | 31.86 | -0.020596372579157807 | 58 |
| SILVER | Silver | 60.82 | 59.51 | -0.021538967444919455 | 59 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.27 | 83.3 | -0.023103084320393985 | 60 |
| REAL_ESTATE | Real Estate Sector | 44.92 | 43.86 | -0.02359750667853966 | 61 |
| COMMUNICATIONS | Communication Services Sector | 112.12 | 109.45 | -0.023813770959686065 | 62 |
| SOLAR | Solar Energy | 62.3 | 60.58 | -0.02760834670947032 | 63 |
| CHINA | China Equities | 54.34 | 52.77 | -0.028892160471107875 | 64 |
| HEALTHCARE | Healthcare Sector | 154.09 | 149.4 | -0.03043675773898369 | 65 |
| UNITED_KINGDOM | United Kingdom Equities | 46.9 | 45.46 | -0.030703624733475432 | 66 |
| BRAZIL | Brazil Equities | 34.81 | 33.73 | -0.031025567365699613 | 67 |
| BROAD_COMMODITIES | Broad Commodities | 17.24 | 16.5 | -0.04292343387470987 | 68 |
| ENERGY | Energy Sector | 57.12 | 53.77 | -0.058648459383753404 | 69 |
| OIL | Crude Oil | 128.83 | 114.87 | -0.1083598540712567 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | NASDAQ100 | 25.0 | 0.03276996876394467 | 0.008192492190986167 | Soft core CPI plus near-certain Fed hold supports rate-sensitive mega-cap growth rebounding after a weak week. |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 20.0 | 0.08274673886290906 | 0.016549347772581813 | Strongest momentum theme; dip after pullback offers high beta to a post-FOMC relief rally. |
| anthropic-claude-fable-5 | SMALL_VALUE | 15.0 | 0.004911727908808672 | 0.0007367591863213008 | Small caps rallied 3% on cool core CPI; benefits from dovish hold and steady economy. |
| anthropic-claude-fable-5 | MOMENTUM | 20.0 | 0.061157957430801435 | 0.012231591486160287 | Persistent factor strength (5.2% 30d) in a trending market. |
| anthropic-claude-fable-5 | ENERGY | 20.0 | -0.058648459383753404 | -0.011729691876750681 | WTI ~$95 with rising headline inflation; energy hedges hawkish-FOMC or oil-spike tail risk. |
| anthropic-claude-opus-4-7 | CONSUMER_STAPLES | 30.0 | -0.023103084320393985 | -0.006930925296118195 | Defensive leader showing strong recent momentum (+3.94% 7d) amid sticky headline CPI and weak consumer sentiment (44.8); hedges against FOMC week volatility. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 25.0 | -0.03043675773898369 | -0.007609189434745922 | Defensive sector with positive momentum (+1.32% 7d, +5.65% 30d) into FOMC meeting; lagged YTD provides catch-up potential. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 20.0 | 0.012497881714963688 | 0.002499576342992738 | Strong momentum (+1.93% 7d) supported by elevated oil/geopolitical backdrop and durable goods orders surge (+7.9% MoM). |
| anthropic-claude-opus-4-7 | REGIONAL_BANKS | 15.0 | -0.008707671043538312 | -0.0013061506565307467 | Strong relative momentum (+3.39% 7d) with steepening curve and Fed hold (97% probability) reducing tail risk into FOMC. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 10.0 | 0.0009838216003497102 | 9.838216003497103e-05 | Cash-like ballast yielding ~3.6% with zero duration risk into FOMC and Treasury auctions during the scoring window. |
| anthropic-claude-opus-4-8 | CONSUMER_STAPLES | 25.0 | -0.023103084320393985 | -0.005775771080098496 | Defensive sector with strong recent relative strength (+3.94% 7d) amid market selloff; hot CPI/PPI and FOMC week favor defensives. |
| anthropic-claude-opus-4-8 | LOW_VOL | 25.0 | -0.010157096424702083 | -0.002539274106175521 | Defensive factor outperforming (+1.96% 7d) into FOMC; sticky inflation and high valuations argue for lower-beta positioning. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 20.0 | -0.03043675773898369 | -0.006087351547796738 | Defensive sector with positive momentum (+1.32% 7d, +5.65% 30d), low policy event risk in window. |
| anthropic-claude-opus-4-8 | AEROSPACE_DEFENSE | 15.0 | 0.012497881714963688 | 0.001874682257244553 | Industry showing resilience (+1.93% 7d) with steady demand backdrop, decorrelated from tech-led selloff. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 15.0 | 0.0009838216003497102 | 0.00014757324005245653 | Cash-like ballast against FOMC and hot inflation print volatility while earning short-rate yield. |
| google-gemini-3-1-pro | TECHNOLOGY | 40.0 | 0.04492112875934717 | 0.01796845150373887 | Strong earnings growth estimates and a favorable rate environment with the FOMC expected to hold rates steady. |
| google-gemini-3-1-pro | COMMUNICATIONS | 30.0 | -0.023813770959686065 | -0.007144131287905819 | Benefiting from secular growth trends and stable macroeconomic conditions. |
| google-gemini-3-1-pro | SP500 | 30.0 | 0.012171980047712028 | 0.0036515940143136082 | Core broad market exposure to balance sector-specific risks and provide baseline beta. |
| openai-gpt-5-5 | REGIONAL_BANKS | 30.0 | -0.008707671043538312 | -0.0026123013130614934 | Recent relative strength, improving domestic risk appetite, and a positively sloped 2s10s curve could support a short-window continuation trade if the FOMC hold is uneventful. |
| openai-gpt-5-5 | SMALL_VALUE | 25.0 | 0.004911727908808672 | 0.001227931977202168 | Small value has held up better than mega-cap growth over the past week and can benefit from a broadening rally, domestic cyclicals, and relief around a widely expected Fed pause. |
| openai-gpt-5-5 | SEMICONDUCTORS | 25.0 | 0.08274673886290906 | 0.020686684715727266 | Semiconductors retain very strong medium-term momentum and high beta to any post-pullback rebound in Nasdaq and AI-linked risk appetite. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 10.0 | 0.012497881714963688 | 0.001249788171496369 | Aerospace and defense has positive recent momentum and comparatively idiosyncratic demand support, offering equity upside with less direct rate sensitivity than long-duration growth. |
| openai-gpt-5-5 | CONSUMER_STAPLES | 10.0 | -0.023103084320393985 | -0.0023103084320393987 | Staples provide a defensive offset if FOMC, retail sales, or claims data trigger risk-off trading, while recent one-week relative performance is strong. |
| xai-grok-4-3 | CONSUMER_STAPLES | 40.0 | -0.023103084320393985 | -0.009241233728157595 | Recent +3.94% 7d return and defensive characteristics amid hot CPI print and FOMC decision week. |
| xai-grok-4-3 | LOW_VOL | 35.0 | -0.010157096424702083 | -0.003554983748645729 | Defensive equity factor with positive recent performance and lower sensitivity to rate and growth volatility. |
| xai-grok-4-3 | SMALL_VALUE | 25.0 | 0.004911727908808672 | 0.001227931977202168 | Positive trailing returns and potential rebound in domestic cyclicals ahead of retail sales and industrial production data. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | NASDAQ100 | 5 | 0.45 | 0.03276996876394467 | 0.025980498759298892 | 0.013808518711586865 | 0.07585925191929752 |  | True | True |
| openai-gpt-5-5 | REGIONAL_BANKS | 5 | 0.57 | -0.008707671043538312 | 0.01824179511932491 | 0.0060698150716128815 | 0.08359795555927149 |  | True | True |
| google-gemini-3-1-pro | TECHNOLOGY | 3 | 0.65 | 0.04492112875934717 | 0.01447591423014666 | 0.002303934182434632 | 0.08736383644844975 |  | True | True |
| xai-grok-4-3 | CONSUMER_STAPLES | 3 | 0.55 | -0.023103084320393985 | -0.011568285499601157 | -0.023740265547313184 | 0.11340803617819756 |  | False | False |
| anthropic-claude-opus-4-8 | CONSUMER_STAPLES | 5 | 0.55 | -0.023103084320393985 | -0.012380141236773745 | -0.02455212128448577 | 0.11421989191537016 |  | False | False |
| anthropic-claude-opus-4-7 | CONSUMER_STAPLES | 5 | 0.5 | -0.023103084320393985 | -0.013248306884367156 | -0.025420286932079185 | 0.11508805756296356 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | NASDAQ100 | 0.013808518711586865 | 0.47973 | 0.02878393828108908 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | c9091b215dd734efd6ea44e28afb072ea8634f21ec682163030c2d14b4e1720d |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 03b5e9792d4c6bade89526a62f43cbdf51184fe03753997a0637de246e708b81 |
| manifest.yaml | 305662c61b3039de756c4884bf69c5eca02a7e9ec58c23aa00ddbee0367d63e2 |
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
| Market fact report | research/market_fact_report.md | audit-only | ab6df5e1020de0cda284751f535d15cdf16e82baeac80c88565d619287a1138c | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | f93b75d5d0a60b3b959444b014d72cff200056e094d5bcbaf26a4225b32fe680 | yes |
| Final briefing | research/final_briefing.md | model-facing | c9091b215dd734efd6ea44e28afb072ea8634f21ec682163030c2d14b4e1720d | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
