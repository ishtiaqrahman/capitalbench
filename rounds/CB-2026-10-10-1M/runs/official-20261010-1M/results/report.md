# CapitalBench Report: CB-2026-10-10-1M / official-20261010-1M

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20261010-1M
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-10-10-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-10-10
- Decision deadline: 2026-10-12T13:25:00Z
- Horizon: one month
- Entry date: 2026-10-09
- Exit date: 2026-11-09
- Entry rule: Use the October 9, 2026 official adjusted close supplied in prices/entry_prices.csv; CASH is fixed at 1.0.
- Exit rule: Use the November 9, 2026 official adjusted close supplied in prices/exit_prices.csv; CASH is fixed at 1.0.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-6 | xai | portfolio | FINANCIALS | 3 | 0.555 | SPY is near a 52-week high after a modest 5-session gain while 21-session breadth is weak (37.7% positive). Fed minutes show a September hike to 3.75%-4.00% and most participants expecting another increase by year-end amid 3.4% PCE and an ISM services prices index of 74.0. That mix favors the benchmark over stretched high-beta winners and over high-vol shock names unless a pullback is clearly transitory. | September CPI/PPI (Oct 14-15) and the Oct 27-28 FOMC can reprice rates and compress any financials/small-value bounce.; ISM services prices at 74.0 and PCE at 3.4% keep real-rate pressure on duration, EM, and high-beta growth.; Oil and mining reversals can fail if EIA supply/demand revisions reverse or if the dollar's 21-session +3.53% trend persists.; ETHA's extreme 5-session move implies path-dependent mean reversion that can dominate a one-month window. |
| google-gemini-3-1-pro | google | portfolio | OIL | 3 | 0.58 | The market is showing mixed signals with solid activity but elevated inflation, leading to expectations of further rate hikes. This environment favors defensive and quality assets while punishing highly volatile or rate-sensitive sectors. | Further interest rate hikes could negatively impact equity valuations.; Energy prices may not reach EIA forecasts if global demand weakens. |
| anthropic-claude-opus-5-5 | anthropic | portfolio | SP500 | 2 | 0.56 | Hawkish Fed (hike to 3.75-4.00%, more likely), 10y at 5.24%, ISM prices 74, oil supply shocks and a weak payroll print. Breadth is narrow over 21 sessions (RSP -2.68% vs SPY) but improved over the last week. Rates pressure duration and rate-sensitive assets. The ETHA +178% print looks anomalous and gives no edge. | A hot CPI on October 14 or a hawkish October 28 FOMC could hit cyclicals; Credit stress showing in HYG/KRE weakness could hurt Financials; Oil supply shock driving inflation and growth fears; Weak labor data turning into recession fears |
| anthropic-claude-fable-5-1 | anthropic | portfolio | SP500 | 2 | 0.55 | Hawkish Fed (hiked to 3.75-4.00%, another hike likely by year end), 10y at 5.24% and rising, ISM prices at highest since 2022, weak payrolls (29k) and oil shock from Middle East shut-ins. SPY near its 52-week high with narrow leadership (RSP lagging SPY by 2.7% over 21 sessions, only 38% of assets positive). Rate-sensitive and small/regional names have sold off on fundamentals (rates), not noise, so most 'pullbacks' are rate-driven and continuation of pressure is plausible through the Oct 27-28 FOMC. Energy-linked and quality large-cap value look better supported; speculative crypto/AI winners offer no independent edge. | Sept CPI (Oct 14) and Oct 27-28 FOMC could push yields further above 5.24% at 10y, hurting financials, small caps and all duration; Oil could reverse sharply if Middle East shut-ins recover faster than EIA's 4.8 mb/d estimate, with 49% vol; Narrow mega-cap leadership may persist, leaving equal-weight, value and cyclical candidates lagging SPY; Weak payrolls (29k) plus downward revisions raise recession-scare risk that would hit beta and credit-sensitive names |
| xai-grok-4-5 | xai | portfolio | OIL | 3 | 0.59 | Elevated cross-asset dispersion with soft payrolls, sticky PCE/ISM prices, unanimous Fed hike to 3.75-4.00% and likely further tightening, rising Treasury yields, and mixed equity breadth; shock-laggards show deep active drawdowns while select growth/crypto momentum remains extreme, favoring selective reversal over pure continuation into the one-month window. | Further Fed tightening or hotter CPI/PPI could extend rate pressure on banks and cyclicals; Oil supply recovery or demand miss could invalidate the EIA-supported reversal; High dispersion and crypto/tech extremes raise gap-risk and correlation breakdown into the Nov 9 exit; Soft payrolls and trade deficit widening may signal broader growth slowdown hurting metals and EM |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Mixed equity signals with recent strength in select growth and cybersecurity offset by broad quality pullbacks, rate sensitivity, and slowing macro data including weak payrolls and elevated PCE. | Further payroll revisions and CPI surprises; Fed policy tightening impact on rates; Elevated energy costs pressuring households |
| openai-gpt-6-astra | openai | portfolio | SP500 | 2 | 0.61 | Cross-sectional outcomes are widely dispersed, although the supplied aggregate dispersion statistic is missing and Ethereum is an extreme outlier. Weak payrolls coexist with solid spending, strong services orders, elevated prices and a tightening Fed. This favors selective rather than broad reversal exposure. Oil has independent supply evidence supporting a rebound; technology leadership lacks comparable briefing support. The October inflation releases, FOMC meeting and November employment report can materially change relative returns before exit. | Middle East production restoration could accelerate; shut-ins already declined from August to September, undermining the oil reversal.; CPI, PCE or the October FOMC meeting could intensify tightening expectations and depress both equities and commodity demand.; Weak payrolls and downward revisions could precede a sharper demand slowdown despite currently resilient spending and services orders.; Oil futures-curve effects can make USO returns differ materially from the briefing's Brent forecast.; Extreme Ethereum statistics and the missing aggregate dispersion measure reduce confidence in cross-sectional tail calibration. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| INDIA | India Equities | 46.03 | 51.41 | 0.11688029545948275 | 1 |
| HEALTHCARE | Healthcare Sector | 170.81 | 188.33 | 0.10257010713658454 | 2 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.43 | 90.89 | 0.0894162771185425 | 3 |
| SOUTH_AFRICA | South Africa Equities | 63.79999923706055 | 69.19000244140625 | 0.08448280985581458 | 4 |
| DIVIDEND | US Dividend Equities | 33.04 | 35.65 | 0.07899515738498786 | 5 |
| LOW_VOL | US Low Volatility Equities | 72.14 | 77.83 | 0.07887441086775704 | 6 |
| MEXICO | Mexico Equities | 71.94999694824219 | 77.55999755859375 | 0.07797082485475526 | 7 |
| REAL_ESTATE | Real Estate Sector | 41.61 | 44.64 | 0.07281903388608502 | 8 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.85 | 121.01 | 0.07230837394771839 | 9 |
| MATERIALS | Materials Sector | 49.43 | 52.94 | 0.07100950839571096 | 10 |
| REGIONAL_BANKS | Regional Banks | 69.01 | 73.45 | 0.06433850166642507 | 11 |
| FINANCIALS | Financials Sector | 54.73 | 57.99 | 0.05956513794993623 | 12 |
| UTILITIES | Utilities Sector | 41.41 | 43.79 | 0.057474040086935574 | 13 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 77.98 | 81.96 | 0.05103872787894326 | 14 |
| EUROPE | Europe Equities | 86.03 | 89.99 | 0.04603045449261889 | 15 |
| UNITED_KINGDOM | United Kingdom Equities | 46.52 | 48.32 | 0.038693035253654307 | 16 |
| MUNICIPAL_BONDS | Municipal Bonds | 101.08000183105469 | 104.9800033569336 | 0.03858331475297527 | 17 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.04 | 220.95 | 0.037129177619226406 | 18 |
| AUSTRALIA | Australia Equities | 28.6200008392334 | 29.670000076293945 | 0.036687603293888316 | 19 |
| LARGE_VALUE | US Large-Cap Value | 253.54 | 262.61 | 0.03577344797665072 | 20 |
| CANADA | Canada Equities | 59.03 | 60.98 | 0.03303405048280528 | 21 |
| SOLAR | Solar Energy | 43.75 | 45.18 | 0.03268571428571421 | 22 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 89.4 | 91.8 | 0.02684563758389258 | 23 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 89.79000091552734 | 92.08000183105469 | 0.025503963605944646 | 24 |
| SMALL_VALUE | US Small-Cap Value | 210.87 | 215.91 | 0.023900981647460462 | 25 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 102.41 | 104.67 | 0.022068157406503364 | 26 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 94.59 | 96.58 | 0.021038164710857288 | 27 |
| BIOTECH | Biotechnology | 153.77 | 156.9 | 0.020355075762502395 | 28 |
| TIPS | Treasury Inflation-Protected Securities | 104.42 | 106.03 | 0.01541850220264318 | 29 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 91.16999816894531 | 92.54000091552734 | 0.015026903302589822 | 30 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.97999954223633 | 47.63999938964844 | 0.014048528178863595 | 31 |
| MID_CAP | US Mid-Cap Stocks | 73.43 | 74.39 | 0.013073675609423852 | 32 |
| SMALL_CAP | US Small-Cap Stocks | 278.94 | 282.51 | 0.012798451279845136 | 33 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 77.23 | 77.51 | 0.003625534118865792 | 34 |
| YEN | Japanese Yen | 57.900001525878906 | 58.040000915527344 | 0.0024179513982545142 | 35 |
| EURO | Euro | 103.37000274658203 | 103.55000305175781 | 0.0017413205029805923 | 36 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 37 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.51 | 91.48 | -0.0003278330237133087 | 38 |
| US_DOLLAR | US Dollar | 29.020000457763672 | 28.969999313354492 | -0.0017229890978792683 | 39 |
| INDUSTRIALS | Industrials Sector | 169.25 | 168.89 | -0.002127031019202419 | 40 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.35 | 69.89 | -0.0065387348969437875 | 41 |
| GOLD | Gold | 78.87 | 77.78 | -0.013820210472930139 | 42 |
| CHINA | China Equities | 52.55 | 51.52 | -0.0196003805899142 | 43 |
| COMMUNICATIONS | Communication Services Sector | 110.38 | 107.36 | -0.027360028990759178 | 44 |
| TOTAL_US_MARKET | Total US Stock Market | 381.94 | 370.9 | -0.028905063622558624 | 45 |
| SP500 | S&P 500 | 778.57 | 752.69 | -0.03324042796408799 | 46 |
| OIL | Crude Oil | 148.1999969482422 | 142.66000366210938 | -0.037381871796310584 | 47 |
| COPPER | Copper | 40.310001373291016 | 38.43000030517578 | -0.04663857613661371 | 48 |
| ENERGY | Energy Sector | 65.08 | 61.94 | -0.04824830977258765 | 49 |
| EMERGING_MARKETS | Emerging Markets | 59.76 | 56.61 | -0.052710843373493965 | 50 |
| BROAD_COMMODITIES | Broad Commodities | 19.66 | 18.47 | -0.06052899287894209 | 51 |
| JAPAN | Japan Equities | 97.86 | 91.48 | -0.06519517678315956 | 52 |
| METALS_MINING | Metals and Mining | 106.35 | 98.58 | -0.07306064880112828 | 53 |
| AGRICULTURE | Agriculture Commodities | 28.329999923706055 | 26.100000381469727 | -0.07871512701171257 | 54 |
| BITCOIN_ETF | Bitcoin ETF | 46.54999923706055 | 42.31999969482422 | -0.09087002387893994 | 55 |
| NASDAQ100 | Nasdaq 100 | 751.27 | 679.35 | -0.09573122845315263 | 56 |
| SOFTWARE | Software | 112.67 | 101.46 | -0.0994940978077572 | 57 |
| LARGE_GROWTH | US Large-Cap Growth | 127.91 | 115.01 | -0.1008521616761785 | 58 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 123.51 | 110.53 | -0.10509270504412604 | 59 |
| BROAD_AI_TECH | Broad AI Technology | 66.6 | 58.77 | -0.11756756756756748 | 60 |
| SILVER | Silver | 54.779998779296875 | 48.13999938964844 | -0.1212121127713115 | 61 |
| CYBERSECURITY | Cybersecurity | 110.0 | 94.68 | -0.13927272727272721 | 62 |
| TECHNOLOGY | Technology Sector | 198.78 | 170.88 | -0.14035617265318445 | 63 |
| ETHEREUM_ETF | Ethereum ETF | 55.9900016784668 | 48.060001373291016 | -0.14163243556796645 | 64 |
| TAIWAN | Taiwan Equities | 114.30999755859375 | 95.6500015258789 | -0.16324028021389803 | 65 |
| SEMICONDUCTORS | Semiconductors | 603.33 | 487.41 | -0.19213365819700667 | 66 |
| SOUTH_KOREA | South Korea Equities | 177.24000549316406 | 142.10000610351562 | -0.19826223369759344 | 67 |
| BRAZIL | Brazil Equities | 43.540000915527344 | 32.61000061035156 | -0.25103353411455487 | 68 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 206.65 | 71.67 | -0.6531817082022744 | 69 |
| MOMENTUM | US Momentum Equities | 320.0 | 66.87 | -0.79103125 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | FINANCIALS | 35.0 | 0.05956513794993623 | 0.02084779828247768 | V3 selected model rank 1: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | SP500 | 65.0 | -0.03324042796408799 | -0.021606278176657195 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| anthropic-claude-opus-5-5 | FINANCIALS | 35.0 | 0.05956513794993623 | 0.02084779828247768 | V3 selected model rank 1: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | SP500 | 65.0 | -0.03324042796408799 | -0.021606278176657195 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | OIL | 35.0 | -0.037381871796310584 | -0.013083655128708703 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | FINANCIALS | 35.0 | 0.05956513794993623 | 0.02084779828247768 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SMALL_VALUE | 30.0 | 0.023900981647460462 | 0.007170294494238138 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | OIL | 35.0 | -0.037381871796310584 | -0.013083655128708703 | V3 selected model rank 1: overreaction with 61% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 65.0 | -0.03324042796408799 | -0.021606278176657195 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | SP500 | 100.0 | -0.03324042796408799 | -0.03324042796408799 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | OIL | 35.0 | -0.037381871796310584 | -0.013083655128708703 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | REGIONAL_BANKS | 35.0 | 0.06433850166642507 | 0.022518475583248775 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | METALS_MINING | 30.0 | -0.07306064880112828 | -0.021918194640338482 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | FINANCIALS | 35.0 | 0.05956513794993623 | 0.02084779828247768 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | SMALL_VALUE | 35.0 | 0.023900981647460462 | 0.00836534357661116 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-6 | SP500 | 30.0 | -0.03324042796408799 | -0.009972128389226398 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-6 | FINANCIALS | 3 | 0.555 | 0.05956513794993623 | 0.019241013469862442 | 0.052481441433950435 | 0.09763928198962031 |  | True | True |
| google-gemini-3-1-pro | OIL | 3 | 0.58 | -0.037381871796310584 | 0.014934437648007115 | 0.04817486561209511 | 0.10194585781147564 |  | True | True |
| anthropic-claude-opus-5-5 | SP500 | 2 | 0.56 | -0.03324042796408799 | -0.0007584798941795146 | 0.03248194806990848 | 0.11763877535366227 |  | True | False |
| anthropic-claude-fable-5-1 | SP500 | 2 | 0.55 | -0.03324042796408799 | -0.0007584798941795146 | 0.03248194806990848 | 0.11763877535366227 |  | True | False |
| xai-grok-4-5 | OIL | 3 | 0.59 | -0.037381871796310584 | -0.01248337418579841 | 0.020757053778289583 | 0.12936366964528118 |  | True | False |
| xai-grok-4-3 | SP500 | 1 | 0.5 | -0.03324042796408799 | -0.03324042796408799 | 0.0 | 0.15012072342357075 |  | False | False |
| openai-gpt-6-astra | SP500 | 2 | 0.61 | -0.03324042796408799 | -0.0346899333053659 | -0.0014495053412779055 | 0.15157022876484866 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | c7d350de5e478b4e1efd2d95e15133a760ce884b19aebc152620389b6ff778f6 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | 502d9939f34aa16b7180ba54e5f8da073aca1a1e61612538a48170ccef9ed0b9 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | ceb6e5e3f8efe1cf6568b1b876ff3baefd57dc8ea424bd78eb49db6495c15acb |
| market_data/universe_decision_context.md | ebf380d16f126717d35e8e2619b62695652932b0d4628eb29eccdff1544f9124 |
| market_data/universe_decision_context.json | 18ba2e3fe721deaeb1ae59bdf2cfa063edab8079c18139b8e1d971ce8c14dbe9 |
| market_data/decision_context_source_history.json | f95dccd5f5077775cd13e2975fdfc59b80f1964d29df3c20a102ebafdb47e242 |
| market_data/universe_quality_evidence.md | c5c80314d260d9aabde3cd6feff42a0d868ce78888227c0ed5b818a6ffaa3a5c |
| market_data/universe_quality_evidence.json | ae97aaa24ae4ab1eaff2eaae5b457778edd3b5ed184d49934cdea3166a14c8e4 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 601ddfccc59a4c23ce77d0c8411a833bb9e3b5f0cdb93ea2d1d5d990b7eeb41c | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 7437509eb1218cf7419a162168e53ae145ab4c1c0c558073a052c9426eb211a0 | yes |
| Final briefing | research/final_briefing.md | model-facing | c7d350de5e478b4e1efd2d95e15133a760ce884b19aebc152620389b6ff778f6 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
