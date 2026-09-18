# CapitalBench Report: CB-2026-09-10-1W / official-v3-20260910-weekly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260910-weekly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-10-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-09-10
- Decision deadline: 2026-09-10T13:25:00Z
- Horizon: one week
- Entry date: 2026-09-10
- Exit date: 2026-09-17
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | SOFTWARE | 3 | 0.58 | The market is experiencing a mixed environment with recent pullbacks in equities and strength in commodities like oil. Inflation data and upcoming central bank meetings are key drivers. | Inflation data surprises could negatively impact equity valuations.; Upcoming central bank meetings may introduce volatility if policy expectations shift. |
| openai-gpt-6-astra | openai | portfolio | HEALTHCARE | 3 | 0.57 | Cross-sectional dispersion of 2.30%, weak equal-weight breadth, and sharp sector divergences favor selective judgments rather than broad momentum extrapolation. Slowing real consumption supports defensive exposures, while elevated inflation, rising Treasury yields, and the September 15–16 FOMC create substantial two-sided event risk. Selected defensive pullbacks have modest reversal potential; oil has independent supply support but considerable reversal risk. PPI and the ECB decision precede the entry close and are not assumed to generate post-entry gains. | A benign CPI release or dovish FOMC could lift growth equities and weaken the dollar, hurting all three leading relative-return judgments.; A hawkish rate shock could pressure dividend valuations and healthcare alongside the broader equity market.; Healthcare weakness may reflect sector-specific information absent from the briefing; low selling volume is not proof of temporary overreaction.; Changes in Middle East export flows could sharply reverse oil and inflation expectations before the exit.; PPI and ECB outcomes occur before the entry close and may materially change the starting prices and opportunity set. |
| xai-grok-4-6 | xai | portfolio | HEALTHCARE | 3 | 0.5633 | SPY is modestly weaker with 4.1-to-1 declining breadth into a CPI and FOMC week; oil and Korea show continuation while several quality defensives and software show short-horizon pullbacks. One-week edge versus SPY is limited by event risk and only moderate 5-session active-return dispersion. | August CPI on September 11 and FOMC September 15-16 can dominate the entire close-to-close week.; Oil at $96-$101 WTI/Brent can reverse if EIA-style supply-normalization views reassert.; Software and biotech remain high-vol with betas that can underperform if rates stay elevated at a 4.84% 10-year. |
| anthropic-claude-fable-5-1 | anthropic | portfolio | HEALTHCARE | 3 | 0.5567 | Late-cycle stagflation tone: 10y at 4.84% and rising, Brent above $100, headline CPI 3.4% with a hawkish-leaning Fed into the Sept 15-16 FOMC and Aug CPI on Sept 11. SPY is flat over 5 sessions but breadth is poor (4.1:1 decliners, RSP lagging). Cross-sectional dispersion at 2.3% is ordinary. Defensive and healthcare pullbacks from strong prior relative trends look like mild overreaction candidates; energy-linked continuation is supported by the oil shock but stretched. Crypto and Korea are extended with very high vol into an event-heavy week. | A soft August CPI on Sept 11 or dovish FOMC on Sept 16 could spark a growth/beta rally that leaves low-beta defensives lagging SPY; Continued rise in 10y yields above 4.84% pressures dividend and staples multiples relative to mega-cap tech; Healthcare pullback could reflect unreported sector-specific policy news not in briefing, extending underperformance; Oil reversal on improving Middle East export flows would hit energy-linked candidates sharply |
| xai-grok-4-5 | xai | portfolio | HEALTHCARE | 3 | 0.5933 | Weak breadth and mild SPY pullback with upcoming CPI/FOMC create mixed setup; quality pullbacks in defensives offer selective reversal potential while oil/Korea show short-term strength but elevated risk. | August CPI and FOMC projections mid-window can reverse rate-sensitive and defensive flows; Oil continuation fails if Middle East supply assumptions shift; Elevated single-name/sector vol in software biotech Korea crypto amplifies gap risk; Weak equity breadth persists into retail sales data |
| anthropic-claude-opus-5 | anthropic | portfolio | HEALTHCARE | 3 | 0.5733 | Breadth is weak (4.1:1 decliners, RSP -1.4% vs SPY 5-session), inflation is re-accelerating (headline CPI 3.4% y/y, PCE 3.7%, Brent above $100), and the 10-year sits near 4.84% into a September 15-16 FOMC with projections plus August CPI on September 11. That combination argues against duration and against aggressive beta chasing. Defensive equity clusters (healthcare, staples, dividend) sold off sharply in the latest window despite strong prior relative trends, which is the clearest overreaction signature in the slate; energy-linked and Korea strength are already extended into a high-event week. | A dovish FOMC or soft August CPI could spark a beta-led rally that leaves low-beta defensives behind; Healthcare and staples pullbacks may reflect sector-specific fundamental news not visible in this briefing; Continued oil strength above $100 could push inflation expectations higher and pressure rate-sensitive defensive equities; Concentration in a single defensive theme means all three positions can move together against SPY; One-week horizon leaves little time for mean reversion to complete |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Commodity strength and equity sector pullbacks amid stable macro data and upcoming policy events create mixed one-week signals. | Upcoming FOMC and CPI releases; Oil price volatility from geopolitical factors; Equity breadth deterioration |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| CYBERSECURITY | Cybersecurity | 94.16 | 101.66 | 0.07965165675446051 | 1 |
| SOFTWARE | Software | 101.2 | 105.78 | 0.0452569169960475 | 2 |
| SILVER | Silver | 57.5 | 58.97 | 0.02556521739130435 | 3 |
| BROAD_AI_TECH | Broad AI Technology | 63.08 | 64.37 | 0.020450221940393254 | 4 |
| HEALTHCARE | Healthcare Sector | 165.66 | 168.81 | 0.019014849692140512 | 5 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 120.49 | 122.52 | 0.016847871192630093 | 6 |
| COPPER | Copper | 39.04 | 39.66 | 0.015881147540983465 | 7 |
| TAIWAN | Taiwan Equities | 108.92 | 110.64 | 0.015791406536907804 | 8 |
| TECHNOLOGY | Technology Sector | 185.22 | 188.06 | 0.015333117373933725 | 9 |
| JAPAN | Japan Equities | 96.44 | 97.91 | 0.015242637909581136 | 10 |
| US_DOLLAR | US Dollar | 28.03 | 28.38 | 0.012486621476988757 | 11 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 80.78 | 81.78 | 0.012379301807378118 | 12 |
| NASDAQ100 | Nasdaq 100 | 708.69 | 716.92 | 0.01161297605441014 | 13 |
| LARGE_GROWTH | US Large-Cap Growth | 121.32 | 122.53 | 0.00997362347510733 | 14 |
| MOMENTUM | US Momentum Equities | 303.15 | 306.12 | 0.009797130133597287 | 15 |
| BIOTECH | Biotechnology | 156.82 | 158.25 | 0.009118734855248167 | 16 |
| UNITED_KINGDOM | United Kingdom Equities | 47.53 | 47.95 | 0.008836524300441795 | 17 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 104.36 | 105.16 | 0.007665772326561848 | 18 |
| COMMUNICATIONS | Communication Services Sector | 111.5 | 112.35 | 0.007623318385650224 | 19 |
| SP500 | S&P 500 | 757.83 | 762.6 | 0.006294287637069074 | 20 |
| TOTAL_US_MARKET | Total US Stock Market | 373.24 | 375.34 | 0.005626406601650258 | 21 |
| GOLD | Gold | 81.27 | 81.69 | 0.0051679586563306845 | 22 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.09 | 83.49 | 0.0048140570465760035 | 23 |
| MUNICIPAL_BONDS | Municipal Bonds | 102.72 | 103.16 | 0.004283489096573279 | 24 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 91.48 | 91.81 | 0.0036073458679493076 | 25 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.92 | 72.15 | 0.0031979977753060496 | 26 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.965 | 47.11 | 0.0030874055147449564 | 27 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 96.05 | 96.33 | 0.002915148360228992 | 28 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 93.41 | 93.66 | 0.002676372979338426 | 29 |
| CANADA | Canada Equities | 60.29 | 60.41 | 0.0019903798308176235 | 30 |
| AUSTRALIA | Australia Equities | 29.08 | 29.13 | 0.0017193947730398396 | 31 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.62 | 78.72 | 0.0012719409819383909 | 32 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 91.18 | 91.25 | 0.0007677122175915319 | 33 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.17 | 213.31 | 0.0006567528263827782 | 34 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.47 | 91.53 | 0.0006559527714005142 | 35 |
| SEMICONDUCTORS | Semiconductors | 560.28 | 560.61 | 0.0005889912186765045 | 36 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 37 |
| EMERGING_MARKETS | Emerging Markets | 59.94 | 59.91 | -0.0005005005005005447 | 38 |
| EUROPE | Europe Equities | 89.42 | 89.37 | -0.0005591590248266165 | 39 |
| MATERIALS | Materials Sector | 50.76 | 50.71 | -0.0009850275807722353 | 40 |
| LARGE_VALUE | US Large-Cap Value | 253.33 | 252.82 | -0.0020131843840051067 | 41 |
| INDIA | India Equities | 48.11 | 48.01 | -0.002078569943878672 | 42 |
| SOUTH_KOREA | South Korea Equities | 182.78 | 182.39 | -0.002133712660028486 | 43 |
| CHINA | China Equities | 52.8 | 52.67 | -0.0024621212121210823 | 44 |
| REAL_ESTATE | Real Estate Sector | 43.05 | 42.94 | -0.002555168408826969 | 45 |
| DIVIDEND | US Dividend Equities | 33.99 | 33.89 | -0.0029420417769933094 | 46 |
| ETHEREUM_ETF | Ethereum ETF | 18.56 | 18.47 | -0.004849137931034475 | 47 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 111.96 | 111.39 | -0.005091103965702004 | 48 |
| TIPS | Treasury Inflation-Protected Securities | 106.33 | 105.71 | -0.005830903790087549 | 49 |
| ENERGY | Energy Sector | 64.93 | 64.48 | -0.0069305405821654675 | 50 |
| SMALL_CAP | US Small-Cap Stocks | 287.7 | 285.43 | -0.007890163364615899 | 51 |
| LOW_VOL | US Low Volatility Equities | 73.67 | 73.06 | -0.008280168318175685 | 52 |
| BITCOIN_ETF | Bitcoin ETF | 43.68 | 43.3 | -0.00869963369963378 | 53 |
| MID_CAP | US Mid-Cap Stocks | 73.86 | 73.21 | -0.008800433252098672 | 54 |
| INDUSTRIALS | Industrials Sector | 170.55 | 169.01 | -0.009029610085019124 | 55 |
| SMALL_VALUE | US Small-Cap Value | 218.97 | 216.73 | -0.010229711832671184 | 56 |
| YEN | Japanese Yen | 59.4 | 58.76 | -0.01077441077441077 | 57 |
| EURO | Euro | 107.13 | 105.91 | -0.011388033230654293 | 58 |
| SOUTH_AFRICA | South Africa Equities | 69.54 | 68.69 | -0.012223180903077502 | 59 |
| MEXICO | Mexico Equities | 75.25 | 74.29 | -0.012757475083056358 | 60 |
| SOLAR | Solar Energy | 47.04 | 46.36 | -0.014455782312925214 | 61 |
| REGIONAL_BANKS | Regional Banks | 73.81 | 72.74 | -0.01449668066657639 | 62 |
| BROAD_COMMODITIES | Broad Commodities | 20.05 | 19.71 | -0.01695760598503737 | 63 |
| FINANCIALS | Financials Sector | 56.87 | 55.88 | -0.01740812379110246 | 64 |
| OIL | Crude Oil | 158.38 | 155.31 | -0.019383760575830244 | 65 |
| UTILITIES | Utilities Sector | 42.52 | 41.69 | -0.01952022577610546 | 66 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 218.32 | 213.88 | -0.02033711982411135 | 67 |
| BRAZIL | Brazil Equities | 38.56 | 37.74 | -0.02126556016597514 | 68 |
| METALS_MINING | Metals and Mining | 114.77 | 111.32 | -0.030060120240480992 | 69 |
| AGRICULTURE | Agriculture Commodities | 29.32 | 28.42 | -0.03069577080491126 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | HEALTHCARE | 35.0 | 0.019014849692140512 | 0.006655197392249179 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | CONSUMER_STAPLES | 35.0 | 0.0048140570465760035 | 0.0016849199663016012 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | DIVIDEND | 30.0 | -0.0029420417769933094 | -0.0008826125330979928 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | HEALTHCARE | 35.0 | 0.019014849692140512 | 0.006655197392249179 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | DIVIDEND | 35.0 | -0.0029420417769933094 | -0.0010297146219476582 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | CONSUMER_STAPLES | 30.0 | 0.0048140570465760035 | 0.001444217113972801 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SOFTWARE | 35.0 | 0.0452569169960475 | 0.015839920948616627 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | HEALTHCARE | 35.0 | 0.019014849692140512 | 0.006655197392249179 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | CONSUMER_STAPLES | 30.0 | 0.0048140570465760035 | 0.001444217113972801 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | HEALTHCARE | 35.0 | 0.019014849692140512 | 0.006655197392249179 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| openai-gpt-6-astra | DIVIDEND | 35.0 | -0.0029420417769933094 | -0.0010297146219476582 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-6-astra | US_DOLLAR | 30.0 | 0.012486621476988757 | 0.003745986443096627 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 100.0 | 0.006294287637069074 | 0.006294287637069074 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | HEALTHCARE | 35.0 | 0.019014849692140512 | 0.006655197392249179 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | DIVIDEND | 35.0 | -0.0029420417769933094 | -0.0010297146219476582 | V3 selected model rank 2: overreaction with 59% estimated probability of beating SPY. |
| xai-grok-4-5 | CONSUMER_STAPLES | 30.0 | 0.0048140570465760035 | 0.001444217113972801 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | HEALTHCARE | 35.0 | 0.019014849692140512 | 0.006655197392249179 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | CONSUMER_STAPLES | 35.0 | 0.0048140570465760035 | 0.0016849199663016012 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | DIVIDEND | 30.0 | -0.0029420417769933094 | -0.0008826125330979928 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | SOFTWARE | 3 | 0.58 | 0.0452569169960475 | 0.023939335454838607 | 0.017645047817769533 | 0.055712321299621906 |  | True | True |
| openai-gpt-6-astra | HEALTHCARE | 3 | 0.57 | 0.019014849692140512 | 0.009371469213398147 | 0.003077181576329073 | 0.07028018754106236 |  | True | True |
| xai-grok-4-6 | HEALTHCARE | 3 | 0.5633 | 0.019014849692140512 | 0.007457504825452788 | 0.0011632171883837143 | 0.07219415192900772 |  | True | True |
| anthropic-claude-fable-5-1 | HEALTHCARE | 3 | 0.5567 | 0.019014849692140512 | 0.007457504825452788 | 0.0011632171883837143 | 0.07219415192900772 |  | True | True |
| xai-grok-4-5 | HEALTHCARE | 3 | 0.5933 | 0.019014849692140512 | 0.007069699884274322 | 0.0007754122472052481 | 0.07258195687018619 |  | True | True |
| anthropic-claude-opus-5 | HEALTHCARE | 3 | 0.5733 | 0.019014849692140512 | 0.007069699884274322 | 0.0007754122472052481 | 0.07258195687018619 |  | True | True |
| xai-grok-4-3 | SP500 | 1 | 0.5 | 0.006294287637069074 | 0.006294287637069074 | 0.0 | 0.07335736911739144 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 079784000fb1b960af27b6e652974ce160817d7d39eb462cb65e11bae7571314 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | 2ecf2009b864fa26820d6cff2cef761b04ef4f5f6ab3b4cd9500a3ea5ba062f5 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | e62a60d82db773118d4dccf32738f3a90f99923c712c21f0a841c3e92f93379e |
| market_data/universe_decision_context.md | d5de835750c632d153f26eab8553cd7ad4a30c2ab41f077fc3ceaf2900417491 |
| market_data/universe_decision_context.json | 7b51ca649fd3ec621e6016bdd4ac583251f83e3188eecc5f1af2da8a2c0ce638 |
| market_data/decision_context_source_history.json | 356c991c0e12bba98eb2ffea5af433da908b8547e47ce153d4699a6c906fda5c |
| market_data/universe_quality_evidence.md | c092e97bf81fd7164c2143924cf52ca0ed33e45257f38487522d51b3f80643f7 |
| market_data/universe_quality_evidence.json | 979a626bce6abfb69c1671b5c1df4fc22e35d659174209b2c5ebc8f6bb97ecdf |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 748b096d64af872eb18e0e80415a9d2f52c992dba0060cfef1eb4f226e2f874b | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | bd783b69aa8b5371780092fd9b3ffa20f70aea56f23c21e6fa64e31d0708f5ec | yes |
| Final briefing | research/final_briefing.md | model-facing | 079784000fb1b960af27b6e652974ce160817d7d39eb462cb65e11bae7571314 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
