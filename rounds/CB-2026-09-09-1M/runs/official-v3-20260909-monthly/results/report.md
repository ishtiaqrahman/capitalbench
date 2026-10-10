# CapitalBench Report: CB-2026-09-09-1M / official-v3-20260909-monthly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260909-monthly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-09-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-09-09
- Decision deadline: 2026-09-09T13:25:00Z
- Horizon: one month
- Entry date: 2026-09-09
- Exit date: 2026-10-09
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 2 | 0.58 | Macro is stagflationary at the margin: core PCE 3.3% y/y, headline 3.7%, 10-year near 4.8%, Fed on hold at 3.50-3.75% with hawkish dissents, and oil spiking on Houthi attacks on Saudi facilities (Brent ~$99). Breadth is negative (positive asset share 37.7% over 21 sessions, RSP lagging SPY), so leadership is narrow and commodity/energy-driven. Within the one-month window CPI (Sep 11), the FOMC (Sep 15-16) and the Oct 2 jobs report are live catalysts that can whipsaw high-beta growth. I favor a small number of quality pullbacks with strong prior trends (CYBERSECURITY after a -6.1% idiosyncratic drop with high prior relative strength) over chasing the oil/crypto momentum extremes, which have extreme volatility and mean-reversion risk. | September 11 CPI or the September 15-16 FOMC delivering a hawkish surprise that hits high-beta tech, including cybersecurity; Cybersecurity's -6.13% drop reflecting a genuine sector demand or guidance problem rather than a temporary dislocation; Rapid unwind or further escalation of the Saudi-facility oil premium, whipsawing energy-linked and cyclical exposures; Narrow breadth persisting so cap-weighted SPY outperforms nearly all diversified alternatives; Elevated 3.3% core PCE keeping real yields high and compressing long-duration growth multiples |
| anthropic-claude-fable-5-1 | anthropic | portfolio | CYBERSECURITY | 3 | 0.565 | Stagflationary backdrop: Q2 GDP 1.5%, CPI 3.4% and PCE 3.7% with energy up 14.7% y/y, ISM prices indexes above 70, ten-year yield near 4.8%, Fed on hold with three hawkish dissents, and Brent near $99 after Houthi attacks on Saudi facilities. Breadth is weak (positive asset share 21s 37.7%, RSP lagging SPY) and SPY is near its 52-week high, so the index is exposed to the September 11 CPI and September 15-16 FOMC. Cross-sectional dispersion is wide, dominated by energy/commodity strength versus rate- and consumer-sensitive weakness; prior strong trends (semis, cyber, Taiwan) are pausing rather than clearly reversing. | Hot August CPI on September 11 or a hawkish FOMC on September 16 could lift yields further and hit high-beta cybersecurity harder than SPY; Rapid resolution of the Saudi disruption could drop oil, reversing energy-linked value outperformance; Renewed mega-cap tech leadership would leave value and equal-weight-style tilts lagging a cap-weighted SPY; Software/cyber sector-specific earnings or AI-disruption fears could extend the pullback rather than reverse it |
| openai-gpt-6-astra | openai | portfolio | INDUSTRIALS | 3 | 0.565 | Wide monthly relative-return spreads coexist with weak breadth, expanding business activity and an inflationary oil shock. Selective reversals are more credible than a broad rebound, while oil has independent supply-side support but substantial unwind risk. High yields and the September FOMC constrain speculative growth exposures. The dispersion judgment uses observed cross-sectional spreads because the aggregate dispersion field is blank; five-session returns are distinguished from monthly active returns. | Hot CPI or PCE data and a hawkish September FOMC could lift yields and overwhelm both selected reversal cases.; Persistent energy disruption could compress industrial margins; rapid normalization could instead reverse oil's relative strength.; Cybersecurity's decline may reflect company-specific deterioration absent from the briefing; its quality score is price-derived, not accounting evidence.; Weak exchange breadth and repeated prior industrial underperformance may signal a durable rotation rather than temporary overselling. |
| google-gemini-3-1-pro | google | portfolio | CYBERSECURITY | 3 | 0.58 | The market is experiencing mixed signals with moderate growth, elevated inflation, and uncertainty regarding the upcoming FOMC meeting. | Uncertainty surrounding the upcoming FOMC meeting could lead to increased volatility.; Elevated inflation readings may prompt a more hawkish stance from the Federal Reserve. |
| xai-grok-4-6 | xai | portfolio | CYBERSECURITY | 3 | 0.5633 | SPY is near highs with negative 5s/21s returns, mixed breadth, and a dense data/FOMC calendar inside the month. Oil shows a sharp short-horizon spike while several quality names show pullbacks; high-beta tech and crypto remain volatile versus a still-elevated 10y yield near 4.8%. | September 11 CPI and September 15–16 FOMC can reprice duration and growth beta across the window.; Oil geopolitical spike may reverse if disruption duration is short, or extend if inventories keep falling.; High-beta semiconductors/Taiwan/crypto can dominate dispersion if risk-off breadth persists.; China PMI still sub-50 limits a clean EM/China reversal.; Services employment ISM 47.8 versus headline 55.4 leaves labor-demand uncertainty into October payrolls. |
| xai-grok-4-5 | xai | portfolio | CYBERSECURITY | 3 | 0.5867 | Mixed macro with sticky inflation near 3.4% CPI/3.7% PCE, solid but slowing GDP, ISM still expansionary yet services employment soft; oil spiked on geopolitical reports while breadth negative and rates near 4.8% 10y create selective reversal opportunities in quality pullbacks amid continuation in energy/tech leaders. | FOMC Sept 15-16 and CPI/PPI could reprice rates higher given sticky 3+% inflation; Oil geopolitical spike reverses if Saudi disruption proves temporary; High-beta tech/semi drawdowns resume if growth data softens; China PMI bounce fails and EM contagion hits risk assets |
| xai-grok-4-3 | xai | portfolio | SP500 | 2 | 0.62 | Mixed macro data with stable but soft growth, persistent inflation, and sector-specific price dislocations favor selective reversals over broad continuation. | Inflation reacceleration from scheduled CPI and PPI releases; Geopolitical supply shocks in energy; FOMC policy surprise on September 16-17 |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 18.58 | 55.9900016784668 | 2.013455418647298 | 1 |
| CYBERSECURITY | Cybersecurity | 94.48 | 110.0 | 0.16426756985605406 | 2 |
| BRAZIL | Brazil Equities | 38.07 | 43.540000915527344 | 0.14368271383050546 | 3 |
| SOFTWARE | Software | 101.83 | 112.67 | 0.10645192968673278 | 4 |
| TECHNOLOGY | Technology Sector | 187.87 | 198.78 | 0.05807207111300361 | 5 |
| BITCOIN_ETF | Bitcoin ETF | 44.29 | 46.54999923706055 | 0.051027302710782374 | 6 |
| SEMICONDUCTORS | Semiconductors | 574.29 | 603.33 | 0.05056678681502391 | 7 |
| NASDAQ100 | Nasdaq 100 | 716.31 | 751.27 | 0.04880568468958968 | 8 |
| LARGE_GROWTH | US Large-Cap Growth | 122.46 | 127.91 | 0.04450432794381842 | 9 |
| BROAD_AI_TECH | Broad AI Technology | 64.11 | 66.6 | 0.038839494618624126 | 10 |
| US_DOLLAR | US Dollar | 27.98 | 29.020000457763672 | 0.037169423079473685 | 11 |
| MOMENTUM | US Momentum Equities | 309.29 | 320.0 | 0.03462769569012902 | 12 |
| HEALTHCARE | Healthcare Sector | 166.58 | 170.81 | 0.025393204466322317 | 13 |
| TAIWAN | Taiwan Equities | 111.76 | 114.30999755859375 | 0.022816728333873826 | 14 |
| SP500 | S&P 500 | 762.4 | 778.57 | 0.021209338929695898 | 15 |
| TOTAL_US_MARKET | Total US Stock Market | 375.56 | 381.94 | 0.01698796463947172 | 16 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 122.03 | 123.51 | 0.012128165205277375 | 17 |
| JAPAN | Japan Equities | 97.0 | 97.86 | 0.0088659793814434 | 18 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.05 | 83.43 | 0.004575556893437804 | 19 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.46 | 112.85 | 0.0034678996976702514 | 20 |
| BROAD_COMMODITIES | Broad Commodities | 19.6 | 19.66 | 0.003061224489795844 | 21 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.46 | 91.51 | 0.0005466870763175535 | 22 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 23 |
| LARGE_VALUE | US Large-Cap Value | 254.06 | 253.54 | -0.002046760607730458 | 24 |
| ENERGY | Energy Sector | 65.31 | 65.08 | -0.0035216659010871565 | 25 |
| COMMUNICATIONS | Communication Services Sector | 110.83 | 110.38 | -0.00406027248939822 | 26 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.23 | 46.97999954223633 | -0.005293255510558259 | 27 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 214.64 | 213.04 | -0.007454342154304849 | 28 |
| OIL | Crude Oil | 149.97 | 148.1999969482422 | -0.011802380821216318 | 29 |
| INDUSTRIALS | Industrials Sector | 171.79 | 169.25 | -0.014785493916991577 | 30 |
| CHINA | China Equities | 53.34 | 52.55 | -0.01481064866891646 | 31 |
| MID_CAP | US Mid-Cap Stocks | 74.56 | 73.43 | -0.015155579399141583 | 32 |
| COPPER | Copper | 41.05 | 40.310001373291016 | -0.018026763135419732 | 33 |
| EMERGING_MARKETS | Emerging Markets | 60.87 | 59.76 | -0.018235584031542573 | 34 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 96.68 | 94.59 | -0.021617707902358285 | 35 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.98 | 77.23 | -0.022157508229931677 | 36 |
| TIPS | Treasury Inflation-Protected Securities | 106.8 | 104.42 | -0.02228464419475651 | 37 |
| AGRICULTURE | Agriculture Commodities | 29.0 | 28.329999923706055 | -0.02310345090668775 | 38 |
| MUNICIPAL_BONDS | Municipal Bonds | 103.48 | 101.08000183105469 | -0.02319286981972668 | 39 |
| LOW_VOL | US Low Volatility Equities | 74.02 | 72.14 | -0.025398540934882363 | 40 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.22 | 89.79000091552734 | -0.026350022603260248 | 41 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 91.895 | 89.4 | -0.027150552260732264 | 42 |
| UNITED_KINGDOM | United Kingdom Equities | 47.83 | 46.52 | -0.02738866819987451 | 43 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.31 | 102.41 | -0.027537745703162142 | 44 |
| YEN | Japanese Yen | 59.7 | 57.900001525878906 | -0.030150728209733635 | 45 |
| DIVIDEND | US Dividend Equities | 34.09 | 33.04 | -0.030800821355236208 | 46 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.17 | 91.16999816894531 | -0.03185729883248045 | 47 |
| CANADA | Canada Equities | 60.99 | 59.03 | -0.03213641580586979 | 48 |
| AUSTRALIA | Australia Equities | 29.62 | 28.6200008392334 | -0.03376094398266716 | 49 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.82 | 70.35 | -0.033919252952485546 | 50 |
| BIOTECH | Biotechnology | 159.38 | 153.77 | -0.0351988957209185 | 51 |
| UTILITIES | Utilities Sector | 42.94 | 41.41 | -0.03563111318118306 | 52 |
| EURO | Euro | 107.325 | 103.37000274658203 | -0.03685066157389216 | 53 |
| MATERIALS | Materials Sector | 51.39 | 49.43 | -0.038139715898034665 | 54 |
| SMALL_CAP | US Small-Cap Stocks | 290.64 | 278.94 | -0.04025598678777864 | 55 |
| FINANCIALS | Financials Sector | 57.06 | 54.73 | -0.04083420960392581 | 56 |
| REAL_ESTATE | Real Estate Sector | 43.41 | 41.61 | -0.04146510020732541 | 57 |
| SMALL_VALUE | US Small-Cap Value | 220.48 | 210.87 | -0.043586719883889624 | 58 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 81.73 | 77.98 | -0.045882784779150865 | 59 |
| GOLD | Gold | 82.69 | 78.87 | -0.046196638045712834 | 60 |
| EUROPE | Europe Equities | 90.21 | 86.03 | -0.04633632634962859 | 61 |
| INDIA | India Equities | 48.67 | 46.03 | -0.05424286007807688 | 62 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 219.45 | 206.65 | -0.05832763727500567 | 63 |
| MEXICO | Mexico Equities | 76.5 | 71.94999694824219 | -0.05947716407526549 | 64 |
| REGIONAL_BANKS | Regional Banks | 73.45 | 69.01 | -0.06044928522804627 | 65 |
| SOUTH_KOREA | South Korea Equities | 190.78 | 177.24000549316406 | -0.0709717711858473 | 66 |
| SOLAR | Solar Energy | 47.74 | 43.75 | -0.08357771260997071 | 67 |
| SILVER | Silver | 60.72 | 54.779998779296875 | -0.09782610706032813 | 68 |
| SOUTH_AFRICA | South Africa Equities | 71.31 | 63.79999923706055 | -0.1053148333044377 | 69 |
| METALS_MINING | Metals and Mining | 119.19 | 106.35 | -0.10772715831865087 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | CYBERSECURITY | 35.0 | 0.16426756985605406 | 0.05749364944961892 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | LARGE_VALUE | 35.0 | -0.002046760607730458 | -0.0007163662127056602 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 30.0 | 0.021209338929695898 | 0.006362801678908769 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5 | CYBERSECURITY | 35.0 | 0.16426756985605406 | 0.05749364944961892 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SP500 | 65.0 | 0.021209338929695898 | 0.013786070304302334 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | CYBERSECURITY | 35.0 | 0.16426756985605406 | 0.05749364944961892 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SMALL_CAP | 35.0 | -0.04025598678777864 | -0.014089595375722524 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | LARGE_VALUE | 30.0 | -0.002046760607730458 | -0.0006140281823191373 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | INDUSTRIALS | 35.0 | -0.014785493916991577 | -0.005174922870947052 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-6-astra | CYBERSECURITY | 35.0 | 0.16426756985605406 | 0.05749364944961892 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 30.0 | 0.021209338929695898 | 0.006362801678908769 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | OIL | 35.0 | -0.011802380821216318 | -0.004130833287425711 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 65.0 | 0.021209338929695898 | 0.013786070304302334 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | CYBERSECURITY | 35.0 | 0.16426756985605406 | 0.05749364944961892 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | AEROSPACE_DEFENSE | 35.0 | -0.05832763727500567 | -0.020414673046251983 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | SMALL_CAP | 30.0 | -0.04025598678777864 | -0.012076796036333591 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | CYBERSECURITY | 35.0 | 0.16426756985605406 | 0.05749364944961892 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | AEROSPACE_DEFENSE | 35.0 | -0.05832763727500567 | -0.020414673046251983 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | CONSUMER_DISCRETIONARY | 30.0 | 0.0034678996976702514 | 0.0010403699093010754 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-5 | SP500 | 2 | 0.58 | 0.021209338929695898 | 0.07127971975392125 | 0.05007038082422535 | 1.942175698893377 |  | True | True |
| anthropic-claude-fable-5-1 | CYBERSECURITY | 3 | 0.565 | 0.16426756985605406 | 0.06314008491582203 | 0.04193074598612613 | 1.950315333731476 |  | True | True |
| openai-gpt-6-astra | INDUSTRIALS | 3 | 0.565 | -0.014785493916991577 | 0.05868152825758064 | 0.03747218932788474 | 1.9547738903897176 |  | True | True |
| google-gemini-3-1-pro | CYBERSECURITY | 3 | 0.58 | 0.16426756985605406 | 0.04279002589157726 | 0.02158068696188136 | 1.970665392755721 |  | True | True |
| xai-grok-4-6 | CYBERSECURITY | 3 | 0.5633 | 0.16426756985605406 | 0.038119346312668015 | 0.016910007382972117 | 1.97533607233463 |  | True | True |
| xai-grok-4-5 | CYBERSECURITY | 3 | 0.5867 | 0.16426756985605406 | 0.025002180367033347 | 0.003792841437337449 | 1.9884532382802649 |  | True | True |
| xai-grok-4-3 | SP500 | 2 | 0.62 | 0.021209338929695898 | 0.009655237016876622 | -0.011554101912819276 | 2.0038001816304214 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | c72d246b0a4e68e599fe4a58518c6d685202b9928ec6a609bcbd5f2f2dbc90b7 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | ab8482b9883cb3ea1e06c573cfd1ebb8d6d64d5e897c999a442c667dff765634 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | f896cbda19d32a59814664b6878a326712228f812d0e36e196cb13cc25405b2a |
| market_data/universe_decision_context.md | a77382344b35a012836e2211f852873d55b861b03842995f3e8787d5fae92989 |
| market_data/universe_decision_context.json | b25715ff0db9aa6f6c587c19b15deb611870ed17f65db1dc35df008c024159c9 |
| market_data/decision_context_source_history.json | 7d16d46e1ce0dff2ed3600d3d5205718cc395b42eca6be9274dbe3ea9b509b12 |
| market_data/universe_quality_evidence.md | 338ecbf0e9e203fd878d9f0626a4dd55250c89a62fe2ccf027fa39768f812b05 |
| market_data/universe_quality_evidence.json | b98361cbc8ca428d5a82391de7e2b947e7d2908c3051ef4bdefd6c9849416704 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | a44caac9f8cddef0d867bce9fdde979444f92d12921e064b7d53d587479eeef8 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 16dc74e53a3e9aca7ae7d3c0cf164128011537430ec8f4b1efa1fe2f7fc8ee98 | yes |
| Final briefing | research/final_briefing.md | model-facing | c72d246b0a4e68e599fe4a58518c6d685202b9928ec6a609bcbd5f2f2dbc90b7 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
