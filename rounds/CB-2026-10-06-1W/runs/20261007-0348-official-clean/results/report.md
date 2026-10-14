# CapitalBench Report: CB-2026-10-06-1W / 20261007-0348-official-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: 20261007-0348-official-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-10-06-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-10-06
- Decision deadline: 2026-10-07T03:45:00Z
- Horizon: one week
- Entry date: 2026-10-06
- Exit date: 2026-10-13
- Entry rule: Use the October 6, 2026 official adjusted close supplied in prices/entry_prices.csv; CASH is fixed at 1.0.
- Exit rule: Use the October 13, 2026 official adjusted close supplied in prices/exit_prices.csv; CASH is fixed at 1.0.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-6-astra | openai | portfolio | OIL | 3 | 0.57 | Dispersion is high, although Ethereum's extreme reported move distorts the aggregate. Narrow equity leadership, weak payroll revisions, elevated survey prices and recent policy tightening favor selective rather than broad reversal bets. Oil has a specific supply catalyst, while healthcare offers the strongest relative-pullback setup among the slate's equities. Fed minutes and petroleum data fall inside the window; CPI and the next FOMC decision do not. | Petroleum inventories could build again or production shut-ins could ease, reversing the oil supply thesis.; Fed minutes could reinforce tightening expectations, damaging both equities and duration-sensitive exposures.; Healthcare has no supplied sector-specific catalyst; concentrated growth leadership could persist through the exit.; Ethereum's extreme reported discontinuity and inconsistent return-window summaries reduce confidence in mechanical dispersion and volatility comparisons. |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SP500 | 2 | 0.56 | SPY near its 52-week high with narrow leadership (RSP lagging SPY by 4.1% over 21 sessions), a hawkish Fed hiking into 3.4% PCE inflation, 10-year yields above 5%, weak payrolls with negative revisions, and an elevated oil forecast. Cross-sectional active dispersion of 24% is dominated by ETHA's anomalous print; ex-crypto, the tape is a mega-cap growth continuation with broad weakness in rates, small caps, and defensives. One-week window has limited catalysts (FOMC minutes, petroleum data) so mean reversion in oversold low-beta sectors and persistence in leaders are both plausible; edge versus SPY is modest. | FOMC minutes on Oct 7 read hawkish, lifting yields further and hitting duration-sensitive and rate-sensitive sectors; Mega-cap growth leadership reverses sharply, producing a broad drawdown where low-beta healthcare still underperforms if rotation goes to cyclicals; Healthcare-specific policy or drug-pricing headlines extend the sector's recent underperformance rather than reverse it; Oil-driven inflation surprise from weekly petroleum data increases cross-asset volatility |
| anthropic-claude-opus-5-5 | anthropic | portfolio | SP500 | 2 | 0.55 | SPY up ~2% on the week, led by mega-cap tech, while breadth lagged (RSP -4.09% vs SPY over 21 sessions). Long yields are above 5%, and services and manufacturing price indexes are hot after a Fed hike. Payrolls were weak, with downward revisions. Dispersion is inflated by an anomalous ETHA print, which looks like a likely data artifact. Few catalysts fall inside the window: FOMC minutes, petroleum data and a federal holiday. | FOMC minutes read hawkish and lift yields, hitting duration-sensitive sectors; Mega-cap tech rally continues, leaving defensive healthcare behind; An oil spike on Middle East supply disrupts the equity tape; The healthcare pullback reflects undisclosed policy or drug-pricing news |
| google-gemini-3-1-pro | google | portfolio | BIOTECH | 3 | 0.5767 | The market is showing mixed signals with positive economic data (services and manufacturing PMIs above 50, positive GDP growth) but also signs of caution (downward employment revisions, elevated inflation, and cautious survey commentary). The divergence between large and small caps suggests a potential rotation or uncertainty. | Continued divergence between large and small caps could negatively impact selected assets.; Elevated inflation and cautious survey commentary may lead to broader market weakness. |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Mixed macro signals with services expansion but weak payrolls and elevated inflation readings support selective continuation in high-volume assets while reversal candidates show limited independent support. | elevated services prices index at 74.0; downward payroll revisions of 60k; high volume dislocation in BRAZIL; oil price forecast volatility |
| xai-grok-4-6 | xai | portfolio | HEALTHCARE | 3 | 0.5633 | Five-session active-return dispersion is elevated while SPY sits at a 52-week high after a 1.98% 3-session gain; sticky survey prices, a fresh 25bp hike, and long yields above 5% argue against duration and against mechanically chasing extreme winners, while several shock-reversal names show deep relative pullbacks versus a still-expanding services/manufacturing backdrop. | Sticky ISM prices and a just-completed hike can keep mega-cap SPY leadership intact, leaving low-beta healthcare/Europe lagging.; Oct 7 petroleum data and FOMC minutes can reprice energy and rates before the Oct 13 close.; Biotech 27% vol can extend the -5.72% active draw rather than reverse.; Brazil/ETH-style extremes show how high dispersion can produce violent fades if risk appetite flips. |
| xai-grok-4-5 | xai | portfolio | HEALTHCARE | 3 | 0.5633 | Elevated cross-sectional dispersion with sticky services/manufacturing expansion, soft payrolls, high survey prices, Fed hike to 3.75-4%, long yields >5%, and oil forecast lift; large-cap strength vs small-cap weakness and mixed international/rate moves favor selective reversal over pure momentum continuation into the one-week window. | Sticky high services/manufacturing price indexes and oil forecast raise could reprice rates higher and pressure duration and defensives; Soft payrolls plus downward revisions risk growth scare that hits high-beta semis/cyber/Brazil harder than expected; Extreme volume dislocations in UTILITIES and BRAZIL can reverse sharply inside one week; Ethereum outlier move and crypto beta create tail risk if risk appetite fades after Oct 6 large-cap strength |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 144.91000366210938 | 153.09 | 0.05644880361030258 | 1 |
| ENERGY | Energy Sector | 63.75 | 67.2 | 0.054117647058823604 | 2 |
| CONSUMER_STAPLES | Consumer Staples Sector | 81.8 | 84.19 | 0.029217603911980472 | 3 |
| BROAD_COMMODITIES | Broad Commodities | 19.46 | 19.98 | 0.02672147995888996 | 4 |
| REAL_ESTATE | Real Estate Sector | 41.1 | 41.83 | 0.017761557177615517 | 5 |
| LOW_VOL | US Low Volatility Equities | 71.73 | 72.98 | 0.01742646033737638 | 6 |
| UTILITIES | Utilities Sector | 41.16 | 41.87 | 0.01724975704567533 | 7 |
| DIVIDEND | US Dividend Equities | 32.85 | 33.37 | 0.015829528158295192 | 8 |
| HEALTHCARE | Healthcare Sector | 167.09 | 169.66 | 0.01538093243162364 | 9 |
| FINANCIALS | Financials Sector | 54.01 | 54.82 | 0.014997222736530258 | 10 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 77.28 | 78.37 | 0.01410455486542439 | 11 |
| CANADA | Canada Equities | 59.18 | 59.91 | 0.012335248394727882 | 12 |
| LARGE_VALUE | US Large-Cap Value | 251.74 | 254.53 | 0.011082863271629328 | 13 |
| INDIA | India Equities | 46.73 | 47.24 | 0.010913759897282382 | 14 |
| COPPER | Copper | 40.029998779296875 | 40.45 | 0.010492161716486148 | 15 |
| SOUTH_AFRICA | South Africa Equities | 63.65999984741211 | 64.32 | 0.010367580178602731 | 16 |
| UNITED_KINGDOM | United Kingdom Equities | 46.37 | 46.82 | 0.009704550355833508 | 17 |
| AUSTRALIA | Australia Equities | 28.549999237060547 | 28.77 | 0.007705806263345494 | 18 |
| MEXICO | Mexico Equities | 72.69000244140625 | 73.24 | 0.007566343927929875 | 19 |
| MUNICIPAL_BONDS | Municipal Bonds | 101.0199966430664 | 101.77 | 0.007424305898401151 | 20 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 89.36000061035156 | 89.97 | 0.006826313624462621 | 21 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 111.72 | 112.36 | 0.005728607232366567 | 22 |
| COMMUNICATIONS | Communication Services Sector | 111.65 | 112.28 | 0.005642633228840177 | 23 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 89.125 | 89.54 | 0.00465638148667602 | 24 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.33 | 213.3 | 0.00456836057080956 | 25 |
| US_DOLLAR | US Dollar | 28.899999618530273 | 29.02 | 0.004152262389401029 | 26 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 102.14 | 102.55 | 0.004014098296455826 | 27 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 94.36 | 94.71 | 0.0037091988130564246 | 28 |
| TIPS | Treasury Inflation-Protected Securities | 104.18 | 104.56 | 0.003647533115761048 | 29 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.849998474121094 | 47.01 | 0.0034151874298840035 | 30 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 90.94999694824219 | 91.26 | 0.003408499858820635 | 31 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.45 | 91.52 | 0.0007654455986876307 | 32 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 33 |
| MATERIALS | Materials Sector | 49.73 | 49.72 | -0.00020108586366374137 | 34 |
| SOLAR | Solar Energy | 44.4 | 44.38 | -0.00045045045045033483 | 35 |
| YEN | Japanese Yen | 57.93000030517578 | 57.89 | -0.0006904937850001902 | 36 |
| SP500 | S&P 500 | 779.09 | 778.01 | -0.0013862326560475369 | 37 |
| GOLD | Gold | 78.37 | 78.25 | -0.0015311981625623083 | 38 |
| SOFTWARE | Software | 111.16 | 110.98 | -0.0016192875134940499 | 39 |
| CHINA | China Equities | 52.22 | 52.135 | -0.001627728839525111 | 40 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 77.27 | 77.09 | -0.0023294939821404403 | 41 |
| BRAZIL | Brazil Equities | 43.0 | 42.87 | -0.0030232558139535737 | 42 |
| EUROPE | Europe Equities | 86.58 | 86.31 | -0.0031185031185030354 | 43 |
| TOTAL_US_MARKET | Total US Stock Market | 382.54 | 381.32 | -0.0031892089716109018 | 44 |
| CYBERSECURITY | Cybersecurity | 108.13 | 107.47 | -0.006103763987792443 | 45 |
| SMALL_VALUE | US Small-Cap Value | 212.37 | 210.99 | -0.006498092950981804 | 46 |
| EURO | Euro | 103.91999816894531 | 102.98999786376953 | -0.008949194780237146 | 47 |
| MID_CAP | US Mid-Cap Stocks | 74.0 | 73.26 | -0.009999999999999898 | 48 |
| REGIONAL_BANKS | Regional Banks | 70.07 | 69.06 | -0.014414157271300021 | 49 |
| AGRICULTURE | Agriculture Commodities | 28.850000381469727 | 28.43 | -0.014558071955503071 | 50 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.11 | 70.06 | -0.01476585571649558 | 51 |
| EMERGING_MARKETS | Emerging Markets | 60.62 | 59.68 | -0.015506433520290241 | 52 |
| LARGE_GROWTH | US Large-Cap Growth | 129.19 | 127.12 | -0.016022911990092092 | 53 |
| SMALL_CAP | US Small-Cap Stocks | 281.34 | 276.7 | -0.01649250017772086 | 54 |
| INDUSTRIALS | Industrials Sector | 171.58 | 168.67 | -0.016960018650192477 | 55 |
| BROAD_AI_TECH | Broad AI Technology | 67.05 | 65.85 | -0.017897091722595126 | 56 |
| JAPAN | Japan Equities | 99.32 | 97.32 | -0.020136931131695568 | 57 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 208.26 | 204.0 | -0.020455200230481085 | 58 |
| NASDAQ100 | Nasdaq 100 | 759.66 | 743.57 | -0.021180528131005905 | 59 |
| BIOTECH | Biotechnology | 150.9 | 146.8 | -0.02717031146454607 | 60 |
| BITCOIN_ETF | Bitcoin ETF | 48.4900016784668 | 47.13 | -0.028047053647983988 | 61 |
| TECHNOLOGY | Technology Sector | 202.0 | 196.28 | -0.028316831683168342 | 62 |
| MOMENTUM | US Momentum Equities | 324.45 | 313.11 | -0.03495145631067953 | 63 |
| TAIWAN | Taiwan Equities | 117.61000061035156 | 113.46 | -0.03528612013276622 | 64 |
| SILVER | Silver | 55.45000076293945 | 53.49 | -0.0353471728759549 | 65 |
| METALS_MINING | Metals and Mining | 108.24 | 103.76 | -0.04138950480413883 | 66 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 127.2 | 120.11 | -0.0557389937106918 | 67 |
| ETHEREUM_ETF | Ethereum ETF | 60.88999938964844 | 56.68 | -0.06914106473721127 | 68 |
| SEMICONDUCTORS | Semiconductors | 632.5 | 588.12 | -0.07016600790513838 | 69 |
| SOUTH_KOREA | South Korea Equities | 186.39999389648438 | 166.56 | -0.10643773898137754 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | HEALTHCARE | 35.0 | 0.01538093243162364 | 0.005383326351068273 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 65.0 | -0.0013862326560475369 | -0.000901051226430899 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5-5 | HEALTHCARE | 35.0 | 0.01538093243162364 | 0.005383326351068273 | V3 selected model rank 1: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | SP500 | 65.0 | -0.0013862326560475369 | -0.000901051226430899 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | BIOTECH | 35.0 | -0.02717031146454607 | -0.009509609012591125 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | HEALTHCARE | 35.0 | 0.01538093243162364 | 0.005383326351068273 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SOUTH_AFRICA | 30.0 | 0.010367580178602731 | 0.003110274053580819 | V3 selected model rank 3: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-6-astra | OIL | 35.0 | 0.05644880361030258 | 0.0197570812636059 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-6-astra | HEALTHCARE | 35.0 | 0.01538093243162364 | 0.005383326351068273 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 30.0 | -0.0013862326560475369 | -0.00041586979681426103 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | SP500 | 100.0 | -0.0013862326560475369 | -0.0013862326560475369 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | HEALTHCARE | 35.0 | 0.01538093243162364 | 0.005383326351068273 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | BIOTECH | 35.0 | -0.02717031146454607 | -0.009509609012591125 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-5 | EUROPE | 30.0 | -0.0031185031185030354 | -0.0009355509355509106 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | HEALTHCARE | 35.0 | 0.01538093243162364 | 0.005383326351068273 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | EUROPE | 35.0 | -0.0031185031185030354 | -0.0010914760914760623 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | BIOTECH | 30.0 | -0.02717031146454607 | -0.008151093439363821 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-6-astra | OIL | 3 | 0.57 | 0.05644880361030258 | 0.024724537817859913 | 0.02611077047390745 | 0.03172426579244267 |  | True | True |
| anthropic-claude-fable-5-1 | SP500 | 2 | 0.56 | -0.0013862326560475369 | 0.004482275124637374 | 0.005868507780684911 | 0.0519665284856652 |  | True | True |
| anthropic-claude-opus-5-5 | SP500 | 2 | 0.55 | -0.0013862326560475369 | 0.004482275124637374 | 0.005868507780684911 | 0.0519665284856652 |  | True | True |
| google-gemini-3-1-pro | BIOTECH | 3 | 0.5767 | -0.02717031146454607 | -0.0010160086079420323 | 0.00037022404810550455 | 0.05746481221824461 |  | True | False |
| xai-grok-4-3 | SP500 | 1 | 0.5 | -0.0013862326560475369 | -0.0013862326560475369 | 0.0 | 0.057835036266350115 |  | False | False |
| xai-grok-4-6 | HEALTHCARE | 3 | 0.5633 | 0.01538093243162364 | -0.00385924317977161 | -0.002473010523724073 | 0.06030804679007419 |  | False | False |
| xai-grok-4-5 | HEALTHCARE | 3 | 0.5633 | 0.01538093243162364 | -0.005061833597073762 | -0.003675600941026225 | 0.06151063720737634 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | c46ba581646ffee06167a6d20b89e0712e78f2bbccaacf2eb132e125756b2559 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | 49ea594f51cdba011b168ab97fa41525a7368a0666aba1fb082c811818b35c32 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 96f53c7a31f73fce0823f470e5f1933b94244c4051b94ee5053ed7e2561803bc |
| market_data/universe_decision_context.md | 62c28f74d7a5c3fff684bdeaaab4cb8f4a303e4ef5e8a66a707483883c93d906 |
| market_data/universe_decision_context.json | c287ae1740fae5749f4305a3e6a92f1641bc12026b938f379d80695324148c49 |
| market_data/decision_context_source_history.json | d6d921ecb3c1c6dd6b9e5faa90d027eb0d619a56f1344b7964a6497cf612e0c0 |
| market_data/universe_quality_evidence.md | 50f8d837492e3243ad7eb0125d87ea5f1717aed7bbd5b50a3637ea707d8b4d68 |
| market_data/universe_quality_evidence.json | 3b35bb6f96efff798ec202f1deeb0ab27745512c73c47793933e50c611e44f84 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | e6b8d5b26758cf6c0d83b6f6f98e65cbed3925a54a63edf6163f3c235dfba304 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | bb98b57c663be677f5886ed0ab8bd51ef6f7855ef68f223d535dc3f43b52aa5a | yes |
| Final briefing | research/final_briefing.md | model-facing | c46ba581646ffee06167a6d20b89e0712e78f2bbccaacf2eb132e125756b2559 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
