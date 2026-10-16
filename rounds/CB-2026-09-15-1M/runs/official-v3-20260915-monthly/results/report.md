# CapitalBench Report: CB-2026-09-15-1M / official-v3-20260915-monthly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260915-monthly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-15-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-09-15
- Decision deadline: 2026-09-15T13:25:00Z
- Horizon: one month
- Entry date: 2026-09-15
- Exit date: 2026-10-15
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Mixed signals with energy supply shock supporting oil continuation while equity sectors show reversal pressure from recent pullbacks and upcoming FOMC data risk. | FOMC outcome uncertainty; Oil supply disruption duration unknown; Equity volatility from scheduled data releases |
| anthropic-claude-opus-5 | anthropic | portfolio | SEMICONDUCTORS | 3 | 0.5667 | Broad de-risking with only ~16% of assets positive over 5 sessions; a sharp semiconductor/AI drawdown (SOX -5.9% on Sep 14) against an oil spike from a Saudi pipeline disruption and firm long yields (30y 5.34%). FOMC on Sep 16 is the dominant near-term catalyst. Dispersion is high and the pattern mixed: AI-complex weakness looks like a positioning shakeout with intact prior trend, while commodity and crypto strength is stretched and unsupported by fundamentals in the window. | FOMC decision on September 16 could repricehigh-beta growth sharply against high-beta semiconductor and Taiwan exposure; Semiconductor selloff may reflect a real AI capex or earnings deterioration not visible in the frozen briefing, turning reversal into continuation; Oil near $106 with an unresolved Saudi pipeline outage could shock inflation expectations and long yields, pressuring cyclicals and small caps; High realized volatility (SMH 47.8%, EWT 38.1%) makes one-month excess returns wide in both directions; Small-cap outperformance depends on credit conditions; HYG already negative over both windows |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.58 | The market is facing uncertainty ahead of the FOMC decision, with recent broad equity declines and a sharp drop in semiconductors. Oil is surging due to a supply disruption, while crypto assets show mixed momentum. | The upcoming FOMC decision could introduce significant volatility across all asset classes.; The drone attack on Saudi Arabia's pipeline could lead to sustained higher energy prices, impacting broader economic growth and inflation expectations. |
| xai-grok-4-5 | xai | portfolio | SMALL_CAP | 3 | 0.57 | Imminent FOMC, oil spike on Saudi pipeline disruption, and sharp semiconductor/tech pullback create mixed cross-section; quality pullbacks in small/mid caps and high-quality semis after oversold sessions offer selective reversal edges versus broad SPY while continuations in oil/crypto carry elevated event risk into the one-month window. | FOMC decision and press conference on Sep 16 with unknown outcome can reverse rate-sensitive and growth factors within days; Unresolved duration of Saudi East-West pipeline shutdown may extend oil volatility and spill into equities; High cross-sectional dispersion and low positive-asset share raise risk that pullback reversals fail if risk-off continues; Semiconductor and small-cap betas remain elevated, amplifying any post-FOMC downside |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SMALL_CAP | 3 | 0.56 | Broad risk-off week with only 16% of assets positive over 5 sessions and 20% over 21 sessions; oil spiked on a Saudi pipeline attack with Brent near $106, yields are high (10y 4.97%, 30y 5.34%), semis fell 5.9% in one session while non-AI stocks rose, and the FOMC decision on Sept 16 is the dominant near-term catalyst. Dispersion is high given oil and crypto up 25-37% active while semis, defense, and solar are down 6-11% active. Mixed pattern: energy/commodity continuation coexists with sharp shock pullbacks in high-quality domestic equity and semis. | Hawkish FOMC outcome on Sept 16 with 10y at 4.97% could extend pressure on small caps and long-duration growth; Prolonged Saudi pipeline outage pushes Brent past $110, hurting equities broadly while benefiting oil, which is ranked low here; Semiconductor selloff may be the start of an AI-capex repricing rather than a one-day shock, given beta 2.39 and 48% volatility; Small-cap and mid-cap picks are highly correlated with SPY (0.82/0.81), limiting the excess return upside |
| openai-gpt-6-astra | openai | portfolio | SMALL_VALUE | 3 | 0.56 | Large differences between energy, technology and broader equities indicate high dispersion, although the explicit dispersion statistic is missing. The unresolved pipeline disruption supports oil independently of its recent gains, but also threatens inflation and financing conditions. Selective reversal is more credible in relatively stable small-company exposures than in deeply damaged thematic funds. The September 16 FOMC decision creates substantial two-sided risk; no policy outcome is assumed. | A hawkish FOMC outcome or persistent oil inflation could raise financing costs and invalidate both small-company reversal theses.; A rapid pipeline restart could unwind oil's supply premium; prolonged disruption could instead damage broader equity earnings.; Small-cap and small-value exposures overlap substantially, so their apparent separate edges may fail together.; Weak equal-weight breadth and low positive-asset shares may indicate sustained risk reduction rather than temporary overshooting.; The supplied quality scores are constructed from price history, not profitability, leverage or valuation, and cannot establish fundamental resilience. |
| xai-grok-4-6 | xai | portfolio | SMALL_VALUE | 3 | 0.5633 | SPY is modestly lower into FOMC with very few assets positive over 5 sessions, oil and crypto showing short continuation while semis/industrials/small-caps show shock or quality pullbacks; one-month edge is mixed and event-dominated rather than a clean trend. | Unknown FOMC outcome on Sep 16 can reverse both duration-sensitive small caps and cyclicals within the scoring window.; Unresolved Saudi pipeline disruption and Brent near $105 can keep oil volatility elevated and pressure risk appetite.; Semiconductor/Taiwan beta remains high after the Sep 14 SOX drop, so a growth-led rebound or further washout can dominate cross-section.; Positive-asset share of 15.94% over 5 sessions implies crowded downside that can persist if data (retail sales, claims, industrial production) disappoint. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 18.2 | 55.40999984741211 | 2.0445054861215444 | 1 |
| BRAZIL | Brazil Equities | 37.78 | 41.58000183105469 | 0.10058236715337965 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 43.11 | 46.59000015258789 | 0.08072373353254214 | 3 |
| HEALTHCARE | Healthcare Sector | 167.66 | 177.19 | 0.05684122629130384 | 4 |
| SOFTWARE | Software | 105.55 | 109.6 | 0.03837044054950267 | 5 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.73 | 86.68 | 0.035232294279230914 | 6 |
| NASDAQ100 | Nasdaq 100 | 704.54 | 728.0 | 0.03329832230959218 | 7 |
| LARGE_GROWTH | US Large-Cap Growth | 120.45 | 124.24 | 0.03146533831465326 | 8 |
| SEMICONDUCTORS | Semiconductors | 542.11 | 558.84 | 0.03086089539023451 | 9 |
| TECHNOLOGY | Technology Sector | 183.74 | 189.19 | 0.029661478175682987 | 10 |
| US_DOLLAR | US Dollar | 28.22 | 29.0 | 0.027639971651311157 | 11 |
| CYBERSECURITY | Cybersecurity | 101.0 | 103.53 | 0.025049504950495072 | 12 |
| TAIWAN | Taiwan Equities | 106.67 | 109.13999938964844 | 0.02315552066793325 | 13 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 110.88 | 113.41 | 0.022817460317460236 | 14 |
| COPPER | Copper | 38.67 | 39.45000076293945 | 0.020170694671307166 | 15 |
| SP500 | S&P 500 | 757.39 | 771.79 | 0.01901266190469908 | 16 |
| BROAD_AI_TECH | Broad AI Technology | 62.96 | 64.09 | 0.0179479034307497 | 17 |
| TOTAL_US_MARKET | Total US Stock Market | 372.84 | 378.42 | 0.014966205342774597 | 18 |
| LARGE_VALUE | US Large-Cap Value | 253.49 | 256.12 | 0.010375162728312626 | 19 |
| ENERGY | Energy Sector | 65.93 | 66.56 | 0.009555589261337705 | 20 |
| UTILITIES | Utilities Sector | 41.32 | 41.65 | 0.007986447241045358 | 21 |
| INDIA | India Equities | 47.59 | 47.95 | 0.007564614414792947 | 22 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.87 | 47.209999084472656 | 0.007254087571424428 | 23 |
| MOMENTUM | US Momentum Equities | 299.51 | 301.54 | 0.006777736970384973 | 24 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.96 | 215.0 | 0.004860721630211229 | 25 |
| LOW_VOL | US Low Volatility Equities | 73.42 | 73.71 | 0.003949877417597225 | 26 |
| CANADA | Canada Equities | 60.29 | 60.33 | 0.0006634599436059485 | 27 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.51 | 91.54 | 0.0003278330237133087 | 28 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 29 |
| UNITED_KINGDOM | United Kingdom Equities | 47.8 | 47.76 | -0.0008368200836820217 | 30 |
| MEXICO | Mexico Equities | 74.03 | 73.87999725341797 | -0.0020262426932599054 | 31 |
| MID_CAP | US Mid-Cap Stocks | 73.23 | 73.03 | -0.0027311211252218914 | 32 |
| AUSTRALIA | Australia Equities | 28.89 | 28.809999465942383 | -0.0027691427503502286 | 33 |
| MATERIALS | Materials Sector | 50.73 | 50.56 | -0.0033510743150009237 | 34 |
| MUNICIPAL_BONDS | Municipal Bonds | 102.87 | 102.4800033569336 | -0.0037911601347955237 | 35 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 95.85 | 95.41 | -0.004590505998956718 | 36 |
| TIPS | Treasury Inflation-Protected Securities | 105.79 | 105.29 | -0.004726344645051506 | 37 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 90.82 | 90.35 | -0.005175071570138745 | 38 |
| INDUSTRIALS | Industrials Sector | 168.85 | 167.89 | -0.0056855196920343465 | 39 |
| DIVIDEND | US Dividend Equities | 34.33 | 34.1 | -0.00669967958054174 | 40 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 91.24 | 90.58999633789062 | -0.007124108528160589 | 41 |
| EMERGING_MARKETS | Emerging Markets | 59.22 | 58.79 | -0.007261060452549817 | 42 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 104.28 | 103.5 | -0.007479861910241636 | 43 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 80.71 | 79.97 | -0.009168628422748015 | 44 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 92.99 | 91.81999969482422 | -0.012582001346120864 | 45 |
| BROAD_COMMODITIES | Broad Commodities | 20.1 | 19.83 | -0.013432835820895717 | 46 |
| COMMUNICATIONS | Communication Services Sector | 114.03 | 112.44 | -0.013943699026571998 | 47 |
| JAPAN | Japan Equities | 96.92 | 95.43 | -0.015373503920759313 | 48 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.38 | 77.13 | -0.015947945904567495 | 49 |
| EUROPE | Europe Equities | 88.96 | 87.21 | -0.019671762589928088 | 50 |
| YEN | Japanese Yen | 59.13 | 57.93000030517578 | -0.020294261708510453 | 51 |
| AGRICULTURE | Agriculture Commodities | 28.88 | 28.280000686645508 | -0.02077559949288399 | 52 |
| CHINA | China Equities | 52.91 | 51.69 | -0.02305802305802307 | 53 |
| REAL_ESTATE | Real Estate Sector | 43.07 | 41.99 | -0.02507545855583926 | 54 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.53 | 69.66 | -0.026142877114497476 | 55 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 118.95 | 115.68 | -0.027490542244640537 | 56 |
| BIOTECH | Biotechnology | 154.03 | 149.78 | -0.0275920275271051 | 57 |
| FINANCIALS | Financials Sector | 56.85 | 55.27 | -0.02779243623570793 | 58 |
| OIL | Crude Oil | 161.86 | 157.30999755859375 | -0.028110728045262934 | 59 |
| EURO | Euro | 106.49 | 103.4800033569336 | -0.028265533318305947 | 60 |
| GOLD | Gold | 80.78 | 78.47 | -0.02859618717504331 | 61 |
| SMALL_VALUE | US Small-Cap Value | 217.68 | 210.54 | -0.03280044101433299 | 62 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 214.0 | 206.92 | -0.033084112149532774 | 63 |
| SMALL_CAP | US Small-Cap Stocks | 285.14 | 275.08 | -0.0352809146384232 | 64 |
| SOLAR | Solar Energy | 45.09 | 42.75 | -0.05189620758483038 | 65 |
| SOUTH_AFRICA | South Africa Equities | 68.92 | 65.01000213623047 | -0.05673241241685334 | 66 |
| REGIONAL_BANKS | Regional Banks | 74.05 | 69.75 | -0.05806887238352465 | 67 |
| METALS_MINING | Metals and Mining | 109.44 | 101.34 | -0.07401315789473684 | 68 |
| SILVER | Silver | 57.53 | 51.91999816894531 | -0.09751437217199177 | 69 |
| SOUTH_KOREA | South Korea Equities | 176.49 | 156.22000122070312 | -0.11485069283980331 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | SMALL_CAP | 35.0 | -0.0352809146384232 | -0.01234832012344812 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SMALL_VALUE | 35.0 | -0.03280044101433299 | -0.011480154355016547 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SEMICONDUCTORS | 30.0 | 0.03086089539023451 | 0.009258268617070353 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SEMICONDUCTORS | 35.0 | 0.03086089539023451 | 0.010801313386582079 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SMALL_CAP | 35.0 | -0.0352809146384232 | -0.01234832012344812 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | TAIWAN | 30.0 | 0.02315552066793325 | 0.006946656200379975 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 35.0 | 0.03086089539023451 | 0.010801313386582079 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SMALL_CAP | 35.0 | -0.0352809146384232 | -0.01234832012344812 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SMALL_VALUE | 30.0 | -0.03280044101433299 | -0.009840132304299897 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | SMALL_VALUE | 35.0 | -0.03280044101433299 | -0.011480154355016547 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-6-astra | SMALL_CAP | 35.0 | -0.0352809146384232 | -0.01234832012344812 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 30.0 | 0.01901266190469908 | 0.005703798571409724 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | SP500 | 100.0 | 0.01901266190469908 | 0.01901266190469908 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | SMALL_CAP | 35.0 | -0.0352809146384232 | -0.01234832012344812 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | SEMICONDUCTORS | 35.0 | 0.03086089539023451 | 0.010801313386582079 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-5 | SMALL_VALUE | 30.0 | -0.03280044101433299 | -0.009840132304299897 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | SMALL_VALUE | 35.0 | -0.03280044101433299 | -0.011480154355016547 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | SMALL_CAP | 35.0 | -0.0352809146384232 | -0.01234832012344812 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | INDUSTRIALS | 30.0 | -0.0056855196920343465 | -0.001705655907610304 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SP500 | 1 | 0.5 | 0.01901266190469908 | 0.01901266190469908 | 0.0 | 2.0254928242168453 |  | False | True |
| anthropic-claude-opus-5 | SEMICONDUCTORS | 3 | 0.5667 | 0.03086089539023451 | 0.005399649463513934 | -0.013613012441185145 | 2.0391058366580306 |  | False | True |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.58 | 0.03086089539023451 | -0.011387139041165938 | -0.030399800945865016 | 2.05589262516271 |  | False | False |
| xai-grok-4-5 | SMALL_CAP | 3 | 0.57 | -0.0352809146384232 | -0.011387139041165938 | -0.030399800945865016 | 2.05589262516271 |  | False | False |
| anthropic-claude-fable-5-1 | SMALL_CAP | 3 | 0.56 | -0.0352809146384232 | -0.014570205861394313 | -0.03358286776609339 | 2.0590756919829385 |  | False | False |
| openai-gpt-6-astra | SMALL_VALUE | 3 | 0.56 | -0.03280044101433299 | -0.01812467590705494 | -0.03713733781175402 | 2.0626301620285994 |  | False | False |
| xai-grok-4-6 | SMALL_VALUE | 3 | 0.5633 | -0.03280044101433299 | -0.02553413038607497 | -0.044546792290774045 | 2.070039616507619 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | c1c7548c0f9112f28aa9d443589af76d1b1ebaed1e3a888d75613a1f44b4a493 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | 4726bc140393c8c01b6738af220ec32091b56860de5cbdec7c6b5a8751a46508 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | a946b92460deeee6a7cb073f671c81c3651229f9c6428778789dfab570b4e57b |
| market_data/universe_decision_context.md | 34aebb66e665b5b84b23ded289928333c7f0aa65fc5025b84f2cae75b5823744 |
| market_data/universe_decision_context.json | 9d3ec753c6889f30125dacd49618f9afdeec47425fb49000eb56a0f8c8b384e6 |
| market_data/decision_context_source_history.json | 58132e2a1774caf891c926c4376c9d53b2db8e7ce0a3435c272b6ea8e74dd671 |
| market_data/universe_quality_evidence.md | 60629bbc02498d5cebe849baa1ac75d5feb67ad1504e2727339393bf3ad7da86 |
| market_data/universe_quality_evidence.json | a59261db041c7a520efab81dd24843092929c342fb9a267f25387a3b8d4f7fcc |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | a4e8208ba51f7c117beac0ca95bb60d9f736d4c6823de16063aef1ff5aeee26c | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | c595c5eb1264cdf104cf396280f12b30dc27a95bc430da49d282eba687055ea5 | yes |
| Final briefing | research/final_briefing.md | model-facing | c1c7548c0f9112f28aa9d443589af76d1b1ebaed1e3a888d75613a1f44b4a493 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
