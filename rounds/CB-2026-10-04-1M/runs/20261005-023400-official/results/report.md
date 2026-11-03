# CapitalBench Report: CB-2026-10-04-1M / 20261005-023400-official

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: 20261005-023400-official
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-10-04-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-10-04
- Decision deadline: 2026-10-05T13:25:00Z
- Horizon: one month
- Entry date: 2026-10-02
- Exit date: 2026-11-02
- Entry rule: Use the October 2, 2026 official adjusted close supplied in prices/entry_prices.csv; CASH is fixed at 1.0.
- Exit rule: Use the November 2, 2026 official adjusted close supplied in prices/exit_prices.csv; CASH is fixed at 1.0.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | FINANCIALS | 3 | 0.58 | The macro environment shows mixed signals with downward payroll revisions and cautious manufacturing commentary, offset by positive real consumption growth and ongoing manufacturing expansion. The Fed's recent 25 bps hike and long-term Treasury yields above 5% suggest a restrictive policy stance, creating a challenging environment for equities and favoring defensive or high-quality assets. | Further downward revisions in employment data could signal a sharper economic slowdown, negatively impacting cyclical sectors like Financials and Small-Cap Value.; Persistent inflation and high input prices could force the Fed to maintain or increase restrictive policy, pressuring equity valuations across the board. |
| xai-grok-4-5 | xai | portfolio | FINANCIALS | 3 | 0.5633 | Soft payrolls with downward revisions, sticky PCE inflation near 3.4%, Fed funds at 3.75-4.00% and long yields >5%, manufacturing still expanding but input prices elevated; recent breadth weak with growth/tech outperforming value/cyclicals and bonds under pressure, producing mixed continuation vs pullback signals over the one-month window. | Sticky inflation and further Fed hawkishness could extend value/financial underperformance; High-vol continuation names (SMH/EWY) may reverse sharply on any growth scare; Upcoming CPI/PPI/FOMC before exit can reprice rates and cyclicals abruptly; Narrow market breadth leaves equal-weight and small-value vulnerable if mega-cap leadership persists |
| xai-grok-4-6 | xai | portfolio | FINANCIALS | 3 | 0.56 | SPY is near a 52-week high while equal-weight and most cyclicals lag, Fed just hiked into still-elevated PCE, and long yields remain above 5%. Strength is concentrated in high-beta tech/Asia continuation names; quality cyclicals show pullbacks without a clear one-month catalyst to beat SPY. | October CPI/PPI and FOMC could reprice the 5%+ Treasury curve and hit both cyclicals and duration.; Mega-cap/tech leadership can persist, leaving quality pullbacks lagging SPY.; Manufacturing input-price spike and USD strength can extend metals, EM, and materials underperformance.; High-beta continuation names (SMH, EWY, EWT) can reverse sharply if growth data disappoint. |
| openai-gpt-6-astra | openai | portfolio | FINANCIALS | 3 | 0.565 | Cross-sectional spreads are large despite the missing aggregate dispersion statistic: semiconductor 21-session active return is +13.72%, versus -12.26% for mining. Narrow equity breadth, falling credit prices, rising dollar strength and restrictive policy argue against indiscriminate dip buying. Manufacturing and consumption remain firm enough to support selective reversals, but weak employment and elevated inflation leave substantial two-sided risk around October releases and the FOMC. Recent technology leadership lacks independent sector-specific fundamental confirmation in the briefing. | October inflation releases or the October 27-28 FOMC could produce further tightening and prevent reversal in rate-sensitive equities.; Weak payroll growth could develop into a credit deterioration cycle, disproportionately hurting financials and smaller companies.; Technology leadership could persist despite absent sector-specific confirmation, causing dividend and value exposures to lag SPY.; A stronger dollar and trade-policy disruption could overwhelm manufacturing expansion and deepen commodity-linked losses. |
| xai-grok-4-3 | xai | portfolio | FINANCIALS | 3 | 0.5833 | Weak payroll revisions and manufacturing price pressure favor reversal in quality cyclicals over continuation in high-valuation tech amid elevated long-term yields. | September payroll revisions signal growth slowdown; Elevated manufacturing input prices at 77.9; FOMC and CPI releases within horizon |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SP500 | 2 | 0.56 | Narrow mega-cap tech leadership (SPY +0.8% vs RSP -3.7% over 21 sessions, only 32% of assets positive) alongside a hiking Fed, 10y above 5.25%, hot ISM prices and weak payrolls. Bonds, gold, defensives and most cyclicals are in drawdown. Into an FOMC (Oct 27-28), CPI (Oct 14) and Q3 earnings season, concentration risk and rate pressure argue for modest expectations of any broad-based reversal; only a few pullbacks look like temporary overreactions with intact medium-term trends. | FOMC on Oct 27-28 or hot CPI on Oct 14 pushes yields higher, hurting financials via credit concerns and all rate-sensitive assets; Continued mega-cap tech leadership keeps SPY ahead of value, equal-weight and financials; Weak labor data (29k payrolls, negative revisions) tips into growth scare, widening credit spreads and hitting bank stocks; Q3 bank earnings disappoint on credit costs or deposit pricing |
| anthropic-claude-opus-5-5 | anthropic | portfolio | SP500 | 2 | 0.55 | Narrow cap-weighted, tech-led market: RSP lagged SPY by 4.5pts over 21 sessions and only 32% of assets were positive. Rising yields (10y 5.28%), a Fed hike, a strong dollar, and widening HY weakness point to tightening conditions. CPI, the FOMC on Oct 27-28, and GDP/PCE all fall inside the window, so broad reversal of the laggards is not strongly supported. | A hot CPI or a hawkish FOMC on Oct 27-28 drives yields higher and hits equities broadly; Credit stress (HYG -2.78%) spreads to financials; A narrow tech leadership reversal causes large active swings; A weak labor trend leads to a growth scare |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 20.110000610351562 | 50.7400016784668 | 1.5231228313513094 | 1 |
| CONSUMER_STAPLES | Consumer Staples Sector | 80.53 | 90.83 | 0.12790264497702708 | 2 |
| HEALTHCARE | Healthcare Sector | 166.18 | 184.6 | 0.11084366349741237 | 3 |
| MATERIALS | Materials Sector | 48.86 | 53.67 | 0.09844453540728626 | 4 |
| DIVIDEND | US Dividend Equities | 32.72 | 35.9 | 0.09718826405867964 | 5 |
| UTILITIES | Utilities Sector | 39.83 | 43.67 | 0.09640974140095415 | 6 |
| LOW_VOL | US Low Volatility Equities | 70.89 | 77.45 | 0.09253773451826786 | 7 |
| FINANCIALS | Financials Sector | 53.49 | 57.56 | 0.07608898859599922 | 8 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 110.04 | 118.16 | 0.07379134860050884 | 9 |
| ENERGY | Energy Sector | 62.82 | 67.25 | 0.07051894301177963 | 10 |
| REAL_ESTATE | Real Estate Sector | 40.81 | 43.64 | 0.0693457485910316 | 11 |
| MEXICO | Mexico Equities | 71.08999633789062 | 75.87999725341797 | 0.0673793946023078 | 12 |
| OIL | Crude Oil | 147.3699951171875 | 156.8699951171875 | 0.06446359716878369 | 13 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 77.48 | 81.73 | 0.054852865255549776 | 14 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 209.73 | 219.98 | 0.04887235970056736 | 15 |
| REGIONAL_BANKS | Regional Banks | 70.78 | 73.73 | 0.04167844023735512 | 16 |
| INDIA | India Equities | 46.52 | 48.45 | 0.0414875322441961 | 17 |
| UNITED_KINGDOM | United Kingdom Equities | 46.18 | 48.03 | 0.040060632308358546 | 18 |
| LARGE_VALUE | US Large-Cap Value | 249.38 | 259.36 | 0.04001924773438126 | 19 |
| AUSTRALIA | Australia Equities | 28.31999969482422 | 29.43000030517578 | 0.039194937228563154 | 20 |
| CANADA | Canada Equities | 58.72 | 60.83 | 0.03593324250681196 | 21 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 207.79 | 214.68 | 0.03315847730882138 | 22 |
| MUNICIPAL_BONDS | Municipal Bonds | 100.95999908447266 | 103.9000015258789 | 0.029120468186081938 | 23 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 89.22000122070312 | 91.7300033569336 | 0.028132729229867204 | 24 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 89.05 | 91.5 | 0.027512633352049454 | 25 |
| TIPS | Treasury Inflation-Protected Securities | 104.11 | 106.4 | 0.021995965805398088 | 26 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 94.25 | 96.16 | 0.020265251989389776 | 27 |
| EUROPE | Europe Equities | 86.38 | 88.06 | 0.01944894651539708 | 28 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 101.83 | 103.71 | 0.01846214278699798 | 29 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 90.13999938964844 | 91.77999877929688 | 0.018193913920047988 | 30 |
| SMALL_VALUE | US Small-Cap Value | 212.34 | 215.91 | 0.016812658943204273 | 31 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.86000061035156 | 47.349998474121094 | 0.010456633747061739 | 32 |
| MID_CAP | US Mid-Cap Stocks | 73.39 | 73.92 | 0.007221692328655216 | 33 |
| US_DOLLAR | US Dollar | 28.889999389648438 | 28.959999084472656 | 0.0024229732192138087 | 34 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 35 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.43 | 91.41 | -0.00021874658208476117 | 36 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 76.91 | 76.89 | -0.00026004420751524204 | 37 |
| YEN | Japanese Yen | 58.06999969482422 | 58.04999923706055 | -0.00034441980142552175 | 38 |
| INDUSTRIALS | Industrials Sector | 169.95 | 169.71 | -0.0014121800529566242 | 39 |
| COPPER | Copper | 39.52000045776367 | 39.369998931884766 | -0.003795585125036083 | 40 |
| SOUTH_AFRICA | South Africa Equities | 63.189998626708984 | 62.93000030517578 | -0.004114548618193936 | 41 |
| BROAD_COMMODITIES | Broad Commodities | 19.44 | 19.36 | -0.004115226337448652 | 42 |
| EURO | Euro | 103.81999969482422 | 103.25 | -0.005490268700632961 | 43 |
| SMALL_CAP | US Small-Cap Stocks | 281.52 | 279.14 | -0.008454106280193274 | 44 |
| BIOTECH | Biotechnology | 154.43 | 152.05 | -0.015411513306999858 | 45 |
| TOTAL_US_MARKET | Total US Stock Market | 377.99 | 370.0 | -0.021138125347231473 | 46 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.13 | 69.61 | -0.02136932377337264 | 47 |
| SP500 | S&P 500 | 769.64 | 752.1 | -0.022789875786081715 | 48 |
| CHINA | China Equities | 51.24 | 49.59 | -0.032201405152224805 | 49 |
| SOLAR | Solar Energy | 44.05 | 42.07 | -0.04494892167990916 | 50 |
| GOLD | Gold | 77.95 | 74.15 | -0.04874919820397683 | 51 |
| AGRICULTURE | Agriculture Commodities | 28.209999084472656 | 26.799999237060547 | -0.04998227200185201 | 52 |
| SOFTWARE | Software | 108.43 | 101.9 | -0.06022318546527716 | 53 |
| JAPAN | Japan Equities | 98.92 | 92.84 | -0.06146380913869787 | 54 |
| EMERGING_MARKETS | Emerging Markets | 59.56 | 55.7 | -0.06480859637340497 | 55 |
| CYBERSECURITY | Cybersecurity | 104.7 | 96.75 | -0.07593123209169061 | 56 |
| METALS_MINING | Metals and Mining | 105.74 | 97.66 | -0.07641384528087758 | 57 |
| LARGE_GROWTH | US Large-Cap Growth | 127.07 | 116.22 | -0.08538600771228455 | 58 |
| COMMUNICATIONS | Communication Services Sector | 110.32 | 100.26 | -0.09118926758520662 | 59 |
| NASDAQ100 | Nasdaq 100 | 749.58 | 681.09 | -0.09137116785399824 | 60 |
| BITCOIN_ETF | Bitcoin ETF | 47.72999954223633 | 43.349998474121094 | -0.09176620804782043 | 61 |
| BROAD_AI_TECH | Broad AI Technology | 66.23 | 59.135 | -0.1071266797523781 | 62 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 124.48 | 109.85 | -0.11752892030848339 | 63 |
| TECHNOLOGY | Technology Sector | 199.81 | 174.22 | -0.1280716680846805 | 64 |
| TAIWAN | Taiwan Equities | 116.33000183105469 | 100.66000366210938 | -0.13470298222553756 | 65 |
| MOMENTUM | US Momentum Equities | 322.88 | 275.14 | -0.14785678889990095 | 66 |
| BRAZIL | Brazil Equities | 38.189998626708984 | 32.15999984741211 | -0.15789471055596394 | 67 |
| SILVER | Silver | 54.7400016784668 | 45.56999969482422 | -0.1675192126866486 | 68 |
| SEMICONDUCTORS | Semiconductors | 630.6 | 508.31 | -0.1939264192832224 | 69 |
| SOUTH_KOREA | South Korea Equities | 191.8800048828125 | 151.6199951171875 | -0.20981868220304212 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | FINANCIALS | 35.0 | 0.07608898859599922 | 0.026631146008599726 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 65.0 | -0.022789875786081715 | -0.014813419260953115 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5-5 | FINANCIALS | 35.0 | 0.07608898859599922 | 0.026631146008599726 | V3 selected model rank 1: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | SP500 | 65.0 | -0.022789875786081715 | -0.014813419260953115 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | FINANCIALS | 35.0 | 0.07608898859599922 | 0.026631146008599726 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | DIVIDEND | 35.0 | 0.09718826405867964 | 0.034015892420537874 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SMALL_VALUE | 30.0 | 0.016812658943204273 | 0.005043797682961281 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | FINANCIALS | 35.0 | 0.07608898859599922 | 0.026631146008599726 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-6-astra | DIVIDEND | 35.0 | 0.09718826405867964 | 0.034015892420537874 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 30.0 | -0.022789875786081715 | -0.006836962735824514 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | FINANCIALS | 35.0 | 0.07608898859599922 | 0.026631146008599726 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | MATERIALS | 35.0 | 0.09844453540728626 | 0.03445558739255019 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | METALS_MINING | 30.0 | -0.07641384528087758 | -0.022924153584263272 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-5 | FINANCIALS | 35.0 | 0.07608898859599922 | 0.026631146008599726 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | DIVIDEND | 35.0 | 0.09718826405867964 | 0.034015892420537874 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-5 | SMALL_VALUE | 30.0 | 0.016812658943204273 | 0.005043797682961281 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | FINANCIALS | 35.0 | 0.07608898859599922 | 0.026631146008599726 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | MATERIALS | 35.0 | 0.09844453540728626 | 0.03445558739255019 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 30.0 | -0.022789875786081715 | -0.006836962735824514 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | FINANCIALS | 3 | 0.58 | 0.07608898859599922 | 0.06569083611209889 | 0.0884807118981806 | 1.4574319952392105 |  | True | True |
| xai-grok-4-5 | FINANCIALS | 3 | 0.5633 | 0.07608898859599922 | 0.06569083611209889 | 0.0884807118981806 | 1.4574319952392105 |  | True | True |
| xai-grok-4-6 | FINANCIALS | 3 | 0.56 | 0.07608898859599922 | 0.0542497706653254 | 0.07703964645140712 | 1.468873060685984 |  | True | True |
| openai-gpt-6-astra | FINANCIALS | 3 | 0.565 | 0.07608898859599922 | 0.053810075693313086 | 0.0765999514793948 | 1.4693127556579963 |  | True | True |
| xai-grok-4-3 | FINANCIALS | 3 | 0.5833 | 0.07608898859599922 | 0.038162579816886644 | 0.06095245560296836 | 1.4849602515344227 |  | True | True |
| anthropic-claude-fable-5-1 | SP500 | 2 | 0.56 | -0.022789875786081715 | 0.011817726747646612 | 0.03460760253372833 | 1.5113051046036627 |  | True | True |
| anthropic-claude-opus-5-5 | SP500 | 2 | 0.55 | -0.022789875786081715 | 0.011817726747646612 | 0.03460760253372833 | 1.5113051046036627 |  | True | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 2be55e79cbacdf50251358420f8851ed8ebd9700ede2c515652ef8f68466e8c5 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | b32fba77ffbeec03eb907721f8317bee7e1dbc23dd8e1233d5b2f18b88ccd7e7 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | f2c1a4745a41b62f233a013c92058352e1cde0146e1c6ca24b5a3aafe7584610 |
| market_data/universe_decision_context.md | e935d48af1a7b0b7ea25b2df6268731e1715877c751997cb0f14ce514f3b0bd4 |
| market_data/universe_decision_context.json | 6545dc997337cee2a629337e5fe7d81942e55e0877ac0fb0c88799cce77562c5 |
| market_data/decision_context_source_history.json | 9369d8898572f98afb2f668a9d1c3a13f724554a3e781c15217ec3fb06f6f503 |
| market_data/universe_quality_evidence.md | f6581ef92ef368c2f8a5a7d07ab340d5319bec08190101e8050e8d50591e215d |
| market_data/universe_quality_evidence.json | 55164fc068ab5c6dbf49c732e69a6b303c285f1842bd80dcb36e45b193343e5a |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 909160d5d547fd1eed9d1b8c91c2165f665c76315399da1b1c9e3a6ef1d98f85 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | ca1df3e34fb65c139c4d56c1790794b673de5173335602e2e5998b8fabb76f85 | yes |
| Final briefing | research/final_briefing.md | model-facing | 2be55e79cbacdf50251358420f8851ed8ebd9700ede2c515652ef8f68466e8c5 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
