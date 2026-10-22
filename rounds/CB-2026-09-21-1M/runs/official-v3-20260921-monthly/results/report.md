# CapitalBench Report: CB-2026-09-21-1M / official-v3-20260921-monthly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260921-monthly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-21-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-09-21
- Decision deadline: 2026-09-21T13:25:00Z
- Horizon: one month
- Entry date: 2026-09-21
- Exit date: 2026-10-21
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Broad equity weakness with isolated strength in cybersecurity and crypto; macro data stable but no clear continuation catalyst across slate. | Macro data revisions could pressure equities; Crypto volatility exceeds slate norms; Low dispersion limits relative outperformance |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SP500 | 2 | 0.57 | Narrow market: SPY roughly flat over one month while equal-weight lagged by 3.7 points and only ~32% of assets beat SPY. 10-year yield at 5% and Brent above $100 pressure rate-sensitive, small-cap and cyclical exposures, while mega-cap tech, crypto and oil carried returns. Breadth deterioration and a heavy macro calendar (GDP, JOLTS, ADP, durable goods) argue for a mixed regime with limited high-conviction reversal setups and elevated risk of trend breaks in crowded winners. | 10-year yield sustained above 5% could extend pressure on small caps, biotech financing and duration assets; Reversal in concentrated mega-cap tech leadership would hurt SPY while not necessarily helping the selected candidates; Oil above $100 and weak manufacturing data (Q3 GDP, durable goods) could trigger a growth scare hitting high-beta candidates; Biotech-specific clinical or regulatory headlines add idiosyncratic risk beyond the factor thesis |
| xai-grok-4-6 | xai | portfolio | SP500 | 2 | 0.56 | SPY is near a 52-week high with a roughly flat week while equal-weight and most assets lagged, 10-year yields are at 5%, industrial production is unchanged, and leadership is concentrated in a few high-beta growth and crypto names versus cyclicals that sold off. One-month edge versus SPY is limited and mixed rather than a clean continuation or reversal regime. | 10-year yield at 5% can keep duration-sensitive and small-cap multiples under pressure into October data.; Scheduled labor, GDP, and sentiment releases from September 24–30 can reverse any mean-reversion in cyclicals.; High-beta semiconductors, Taiwan, crypto, and solar can dominate one-month dispersion if risk appetite flips. |
| openai-gpt-6-astra | openai | portfolio | SP500 | 2 | 0.55 | Cross-sectional return spreads are wide despite a nearly flat SPY, although the aggregate dispersion statistic is missing. Weak breadth, a 5.00% Treasury yield, expensive oil and declining manufacturing constrain broad reversal bets. Biotech offers a tentative relative-overreaction opportunity; other quality pullbacks face meaningful financing and growth headwinds. Recent technology and crypto leadership lacks independent fundamental confirmation in the briefing. | Treasury yields could rise further, extending financing pressure on biotech and smaller companies.; Elevated oil prices and weak manufacturing could produce further cyclical deterioration rather than mean reversion.; Late-September labor, spending and growth releases could alter market leadership before the exit close.; No biotech-specific catalyst is supplied, so its relative pullback may persist beyond the one-month window.; The entry close follows the frozen snapshot; intervening price changes could absorb the estimated reversal opportunity. |
| anthropic-claude-opus-5 | anthropic | portfolio | BIOTECH | 3 | 0.565 | Narrow mega-cap leadership with breadth deterioration (RSP -3.7% vs SPY over 21 sessions, only ~32% of assets positive) against a 5.00% 10-year yield and flat industrial production. Rate pressure is the dominant macro constraint, penalizing small caps, rate-sensitive defensives and long-duration equity. Dispersion is high: crypto and commodities far outperformed while defense and solar collapsed. I treat the rate-driven broad pullback in high-quality small caps and biotech as partly an overreaction, but I do not extrapolate crypto or semiconductor strength without independent in-window support. | A further rise in the 10-year yield above 5% would extend the small-cap and biotech underperformance rather than reverse it.; Breadth deterioration could persist, keeping mega-cap-weighted SPY ahead of every equal-weight-like candidate.; Biotech's 29% volatility means the 80% excess-return band is wide and the median edge is small.; Scheduled GDP, JOLTS and payroll-adjacent releases in late September could trigger a growth scare that hits high-beta pullback names hardest. |
| xai-grok-4-5 | xai | portfolio | SMALL_CAP | 3 | 0.57 | SPY near flat with low positive-asset share, 10y at 5%, industrial production unchanged, and equal-weight lagging; short-term crypto/tech strength contrasts with pullbacks in small-caps, industrials, defense and biotech, favoring selective mean-reversion over pure momentum continuation into the one-month window. | 10-year yield holding at or above 5% could extend pressure on equities and duration-sensitive names; Low positive-asset share and RSP underperformance signal fragile breadth that may reverse quality-pullback thesis; High-vol crypto and semiconductor beta could spill over into risk-off if momentum fades; Upcoming labor, claims, and sentiment data (Sept 24-30) may shift growth expectations abruptly |
| google-gemini-3-1-pro | google | portfolio | AEROSPACE_DEFENSE | 3 | 0.58 | The market is showing mixed signals with recent slight declines in major indices except Nasdaq, while industrial production is flat and the 10-year yield is at 5%. | Interest rates remaining high could pressure equities.; Industrial production stagnation could signal broader economic weakness. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 20.85 | 56.43000030517578 | 1.7064748347806127 | 1 |
| BRAZIL | Brazil Equities | 38.07 | 42.5099983215332 | 0.11662722147447346 | 2 |
| ENERGY | Energy Sector | 62.46 | 68.16 | 0.09125840537944274 | 3 |
| OIL | Crude Oil | 148.16 | 159.8000030517578 | 0.07856373550052531 | 4 |
| CONSUMER_STAPLES | Consumer Staples Sector | 81.92 | 87.11 | 0.0633544921875 | 5 |
| HEALTHCARE | Healthcare Sector | 169.01 | 178.94 | 0.05875391988639733 | 6 |
| UTILITIES | Utilities Sector | 40.66 | 42.0 | 0.03295622233152984 | 7 |
| LOW_VOL | US Low Volatility Equities | 72.18 | 74.54 | 0.03269603768356877 | 8 |
| MATERIALS | Materials Sector | 49.71 | 51.32 | 0.03238784952725804 | 9 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.23 | 115.53 | 0.029403902699812967 | 10 |
| DIVIDEND | US Dividend Equities | 33.72 | 34.66 | 0.02787663107947802 | 11 |
| BROAD_COMMODITIES | Broad Commodities | 19.44 | 19.98 | 0.02777777777777768 | 12 |
| MEXICO | Mexico Equities | 73.7 | 75.55000305175781 | 0.025101805315574044 | 13 |
| LARGE_VALUE | US Large-Cap Value | 253.45 | 258.29 | 0.01909646873150539 | 14 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.68 | 216.64 | 0.01861952228700381 | 15 |
| SOFTWARE | Software | 107.13 | 108.82 | 0.015775226360496664 | 16 |
| US_DOLLAR | US Dollar | 28.48 | 28.920000076293945 | 0.015449440881107668 | 17 |
| CANADA | Canada Equities | 60.43 | 61.32 | 0.01472778421313925 | 18 |
| AUSTRALIA | Australia Equities | 29.04 | 29.229999542236328 | 0.006542683961306084 | 19 |
| FINANCIALS | Financials Sector | 55.9 | 56.04 | 0.002504472271914082 | 20 |
| MID_CAP | US Mid-Cap Stocks | 73.25 | 73.39 | 0.0019112627986348496 | 21 |
| CYBERSECURITY | Cybersecurity | 103.09 | 103.13 | 0.0003880104762827852 | 22 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.57 | 91.6 | 0.0003276182155727003 | 23 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 24 |
| UNITED_KINGDOM | United Kingdom Equities | 47.69 | 47.69 | 0.0 | 24 |
| SP500 | S&P 500 | 773.5 | 773.09 | -0.0005300581771169321 | 26 |
| TIPS | Treasury Inflation-Protected Securities | 105.68 | 105.55 | -0.0012301286903861897 | 27 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.21 | 47.09000015258789 | -0.002541831125018268 | 28 |
| MUNICIPAL_BONDS | Municipal Bonds | 102.86 | 102.44999694824219 | -0.00398603005792153 | 29 |
| TOTAL_US_MARKET | Total US Stock Market | 381.1 | 379.15 | -0.0051167672526897245 | 30 |
| YEN | Japanese Yen | 58.2 | 57.900001525878906 | -0.005154612957407156 | 31 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 96.21 | 95.3 | -0.009458476249870063 | 32 |
| INDUSTRIALS | Industrials Sector | 169.98 | 168.31 | -0.009824685257089016 | 33 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 91.15 | 90.23 | -0.010093252879868397 | 34 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 91.59 | 90.54000091552734 | -0.011464123643112334 | 35 |
| REAL_ESTATE | Real Estate Sector | 42.59 | 42.06 | -0.012444235736088327 | 36 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.09 | 103.21 | -0.01788942810923977 | 37 |
| EUROPE | Europe Equities | 89.24 | 87.58 | -0.018601523980277812 | 38 |
| REGIONAL_BANKS | Regional Banks | 71.99 | 70.62 | -0.01903042089179041 | 39 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 81.8 | 80.24 | -0.019070904645476783 | 40 |
| AGRICULTURE | Agriculture Commodities | 28.68 | 28.1200008392334 | -0.019525772690606735 | 41 |
| EURO | Euro | 105.8 | 103.70999908447266 | -0.019754261961506092 | 42 |
| LARGE_GROWTH | US Large-Cap Growth | 126.25 | 123.54 | -0.021465346534653373 | 43 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.68 | 76.98 | -0.021606507371631944 | 44 |
| NASDAQ100 | Nasdaq 100 | 741.47 | 725.2 | -0.02194289721768916 | 45 |
| SMALL_VALUE | US Small-Cap Value | 215.95 | 211.02 | -0.022829358647835085 | 46 |
| JAPAN | Japan Equities | 97.96 | 95.72 | -0.022866476112698986 | 47 |
| BITCOIN_ETF | Bitcoin ETF | 49.01 | 47.84000015258789 | -0.023872675931689624 | 48 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 93.78 | 91.44000244140625 | -0.024951989321750356 | 49 |
| INDIA | India Equities | 48.5 | 47.27 | -0.025360824742267973 | 50 |
| COPPER | Copper | 40.67 | 39.540000915527344 | -0.02778458530790895 | 51 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.3 | 70.12 | -0.030152143845089796 | 52 |
| SMALL_CAP | US Small-Cap Stocks | 285.58 | 276.48 | -0.031864976538973244 | 53 |
| TECHNOLOGY | Technology Sector | 194.85 | 188.54 | -0.032383885039774185 | 54 |
| BIOTECH | Biotechnology | 158.23 | 152.78 | -0.03444353156797064 | 55 |
| BROAD_AI_TECH | Broad AI Technology | 66.31 | 64.0 | -0.034836374604132136 | 56 |
| SOUTH_AFRICA | South Africa Equities | 68.23 | 65.31999969482422 | -0.042649865237810114 | 57 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 216.14 | 205.79 | -0.04788562968446375 | 58 |
| EMERGING_MARKETS | Emerging Markets | 61.14 | 58.18 | -0.04841347726529277 | 59 |
| GOLD | Gold | 81.67 | 77.71 | -0.04848781682380321 | 60 |
| COMMUNICATIONS | Communication Services Sector | 114.75 | 108.97 | -0.0503703703703704 | 61 |
| MOMENTUM | US Momentum Equities | 316.25 | 299.56 | -0.052774703557312286 | 62 |
| TAIWAN | Taiwan Equities | 115.64 | 108.98999786376953 | -0.057506071741875386 | 63 |
| SEMICONDUCTORS | Semiconductors | 596.03 | 556.7 | -0.0659866114121771 | 64 |
| METALS_MINING | Metals and Mining | 109.0 | 101.29 | -0.07073394495412844 | 65 |
| CHINA | China Equities | 54.0 | 50.05 | -0.07314814814814818 | 66 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 125.49 | 115.85 | -0.0768188700294844 | 67 |
| SOLAR | Solar Energy | 46.71 | 42.56 | -0.08884607150503099 | 68 |
| SILVER | Silver | 59.63 | 52.2599983215332 | -0.12359553376600363 | 69 |
| SOUTH_KOREA | South Korea Equities | 189.16 | 156.8800048828125 | -0.17064916006125763 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | BIOTECH | 35.0 | -0.03444353156797064 | -0.012055236048789724 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 65.0 | -0.0005300581771169321 | -0.00034453781512600593 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5 | BIOTECH | 35.0 | -0.03444353156797064 | -0.012055236048789724 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SMALL_VALUE | 35.0 | -0.022829358647835085 | -0.00799027552674228 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SP500 | 30.0 | -0.0005300581771169321 | -0.00015901745313507963 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 35.0 | -0.04788562968446375 | -0.016759970389562312 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | METALS_MINING | 35.0 | -0.07073394495412844 | -0.024756880733944952 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | INDUSTRIALS | 30.0 | -0.009824685257089016 | -0.0029474055771267047 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | BIOTECH | 35.0 | -0.03444353156797064 | -0.012055236048789724 | V3 selected model rank 1: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 65.0 | -0.0005300581771169321 | -0.00034453781512600593 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | SP500 | 100.0 | -0.0005300581771169321 | -0.0005300581771169321 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | SMALL_CAP | 35.0 | -0.031864976538973244 | -0.011152741788640634 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | BIOTECH | 35.0 | -0.03444353156797064 | -0.012055236048789724 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-5 | SMALL_VALUE | 30.0 | -0.022829358647835085 | -0.0068488075943505256 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | BIOTECH | 35.0 | -0.03444353156797064 | -0.012055236048789724 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 65.0 | -0.0005300581771169321 | -0.00034453781512600593 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SP500 | 1 | 0.5 | -0.0005300581771169321 | -0.0005300581771169321 | 0.0 | 1.7070048929577295 |  | False | False |
| anthropic-claude-fable-5-1 | SP500 | 2 | 0.57 | -0.0005300581771169321 | -0.01239977386391573 | -0.011869715686798798 | 1.7188746086445283 |  | False | False |
| xai-grok-4-6 | SP500 | 2 | 0.56 | -0.0005300581771169321 | -0.01239977386391573 | -0.011869715686798798 | 1.7188746086445283 |  | False | False |
| openai-gpt-6-astra | SP500 | 2 | 0.55 | -0.0005300581771169321 | -0.01239977386391573 | -0.011869715686798798 | 1.7188746086445283 |  | False | False |
| anthropic-claude-opus-5 | BIOTECH | 3 | 0.565 | -0.03444353156797064 | -0.020204529028667085 | -0.019674470851550153 | 1.7266793638092797 |  | False | False |
| xai-grok-4-5 | SMALL_CAP | 3 | 0.57 | -0.031864976538973244 | -0.030056785431780884 | -0.029526727254663952 | 1.7365316202123935 |  | False | False |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 3 | 0.58 | -0.04788562968446375 | -0.044464256700633975 | -0.04393419852351704 | 1.7509390914812466 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | bcac8abf61756435c887a5b327e6bc1a09e79e9331e882b0cfc7b1c42343b082 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | 012fd8e6cb72b1b0eec11fc9498b649050f096d84498dedcac419ef76d15d84f |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 5f327e9ff72616cdb7ca74ba2565105155c388e9edc3ebda6b2c50cdd408d25b |
| market_data/universe_decision_context.md | 8175b2522ec0a828749f39462caf43662869c0ff7aab036553675cd23ff52e59 |
| market_data/universe_decision_context.json | d95af54276155d89d3348b551e0546a79a22f8a1d57383f9b10f956cc900c5d0 |
| market_data/decision_context_source_history.json | 2179505c8d417c388c83368a0d421c74e0affe059a9a23922e26727cd31c1c42 |
| market_data/universe_quality_evidence.md | 9aa4a9b470d022186d41ff8029ede366e5ab323683ec197861ab89bf882d7cfe |
| market_data/universe_quality_evidence.json | 00c56ffbdf30336296fbc637476407fafba71882264e4fa4763dfdbe281b67bb |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 333a7ae0ad4f4e078fa8e2a38840c0ec8797586a19945e5bc76cd2cb490459cd | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 0617f6d5f4b705b6ad49f52ef1cb8592306531f4d442ea5bfd68f03d04502068 | yes |
| Final briefing | research/final_briefing.md | model-facing | bcac8abf61756435c887a5b327e6bc1a09e79e9331e882b0cfc7b1c42343b082 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
