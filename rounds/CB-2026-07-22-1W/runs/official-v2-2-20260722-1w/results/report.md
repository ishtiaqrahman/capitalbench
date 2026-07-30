# CapitalBench Report: CB-2026-07-22-1W / official-v2-2-20260722-1w

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-20260722-1w
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-22-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-22
- Decision deadline: 2026-07-23T09:30:00Z
- Horizon: one week
- Entry date: 2026-07-22
- Exit date: 2026-07-29
- Entry rule: Use adjusted close prices on Wednesday, July 22, 2026 as the one-week entry snapshot, calculated after regular trading ends and supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Wednesday, July 29, 2026 as the one-week exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | openai | portfolio | COMMUNICATIONS | 3 | 0.61 | Alphabet's results create the strongest one-week catalyst, while Visa earnings, the FOMC decision, and elevated crude prices provide additional paths to outperformance. | Alphabet's strong reported growth may already be reflected in expectations or be overshadowed by volatile unrealized gains.; A hawkish July 29 FOMC communication could pressure equities and reverse the communications rebound.; Rising petroleum inventories and weak product supplied could trigger a sharp crude and energy reversal.; Visa results could disappoint or signal weaker payment volumes. |
| openai-gpt-5-5 | openai | portfolio | COMMUNICATIONS | 5 | 0.57 | SPY's base case is modestly positive but not the strongest active forecast. Selected holdings each clear the SPY hurdle and span technology/growth, energy, commodities, financials, and diversified U.S. equity exposure. | FOMC communication on July 29 tightens financial conditions and pressures equities before the close.; Crude oil and commodity strength reverses after inventory data showed total commercial petroleum inventories up 11.6 million barrels.; Alphabet earnings reaction fades or is offset by broader growth-stock weakness.; Recent breadth leadership reverses back toward SPY's mega-cap concentration. |
| google-gemini-3-1-pro | google | portfolio | ENERGY | 2 | 0.65 | Overweight Energy and Communications based on positive catalysts and momentum. | A sudden reversal in crude oil prices could negatively impact the Energy allocation.; A broader market selloff could drag down the Communications sector despite strong earnings.; Macroeconomic data releases could cause volatility. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 3 | 0.55 | Energy momentum plus defensive dividend leadership complement an SPY core into a rate-decision week. | Hawkish FOMC on July 29 triggers broad equity drawdown; Oil reverses sharply on inventory builds hurting energy sleeve |
| anthropic-claude-fable-5 | anthropic | portfolio | COMMUNICATIONS | 5 | 0.6 | Oil momentum and Alphabet's beat are the two strongest supplied catalysts inside the window; defensive sleeves hedge FOMC risk. | FOMC hawkish surprise on July 29 hits all risk assets; Oil price reversal on inventory builds (crude stocks rose 2.0M barrels); Alphabet sells off despite headline beat given unrealized-gain-driven net income; Commodity inflation strength pressures equity multiples |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.55 | One-week allocation favors sectors with recent earnings or commodity support while capping cluster exposure at 20%. | FOMC outcome volatility on July 29; Oil price reversal below 90; Earnings follow-through disappointment |
| xai-grok-4-5 | xai | portfolio | OIL | 5 | 0.58 | Energy complex leads on crude strength; communications benefits from Alphabet beat; financials offer FOMC optionality. Equal-weight and pure SPY lag the selected bases. | FOMC hawkish surprise triggering broad equity and commodity risk-off on July 29; Sudden crude inventory or demand disappointment reversing oil/energy gains; Post-earnings fade in Alphabet/communications names; Elevated single-cluster (energy) volatility within the 50% cap |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| HEALTHCARE | Healthcare Sector | 159.43 | 166.24000549316406 | 0.04271470547051415 | 1 |
| SOFTWARE | Software | 89.02 | 92.37000274658203 | 0.0376320236641432 | 2 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.38 | 87.36000061035156 | 0.03531643292665998 | 3 |
| DIVIDEND | US Dividend Equities | 32.9 | 33.83000183105469 | 0.028267532858805122 | 4 |
| CHINA | China Equities | 53.57 | 55.06999969482422 | 0.028000740989811757 | 5 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 231.11 | 236.25999450683594 | 0.022283737211007404 | 6 |
| REAL_ESTATE | Real Estate Sector | 45.01 | 45.959999084472656 | 0.021106400454846908 | 7 |
| INDIA | India Equities | 48.22 | 49.16999816894531 | 0.019701330753739477 | 8 |
| MATERIALS | Materials Sector | 50.82 | 51.7400016784668 | 0.018103142039881837 | 9 |
| LOW_VOL | US Low Volatility Equities | 76.2 | 77.54000091552734 | 0.017585313852064743 | 10 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.7 | 215.72999572753906 | 0.014245395992191323 | 11 |
| UNITED_KINGDOM | United Kingdom Equities | 47.24 | 47.900001525878906 | 0.013971243138842127 | 12 |
| FINANCIALS | Financials Sector | 56.05 | 56.68000030517578 | 0.011239969762279811 | 13 |
| AUSTRALIA | Australia Equities | 28.86 | 29.110000610351562 | 0.008662529811211517 | 14 |
| LARGE_VALUE | US Large-Cap Value | 247.52 | 249.52 | 0.00808015513897864 | 15 |
| REGIONAL_BANKS | Regional Banks | 75.6 | 76.18000030517578 | 0.007671961708674457 | 16 |
| EURO | Euro | 105.33 | 105.69999694824219 | 0.0035127404181352073 | 17 |
| COMMUNICATIONS | Communication Services Sector | 109.2 | 109.51000213623047 | 0.002838847401377853 | 18 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.15 | 93.2300033569336 | 0.0008588658822714645 | 19 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.1 | 93.16999816894531 | 0.0007518600316360757 | 20 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.58 | 91.64 | 0.0006551648831623069 | 21 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.8 | 47.810001373291016 | 0.00020923375085812879 | 22 |
| CANADA | Canada Equities | 59.28 | 59.290000915527344 | 0.00016870640228305867 | 23 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 24 |
| TIPS | Treasury Inflation-Protected Securities | 107.77 | 107.7699966430664 | -3.1149054335877224e-08 | 25 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.58 | 97.55000305175781 | -0.0003074087747713117 | 26 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.88 | 105.7699966430664 | -0.0010389436808990737 | 27 |
| US_DOLLAR | US Dollar | 28.45 | 28.420000076293945 | -0.0010544788648876313 | 28 |
| YEN | Japanese Yen | 56.23 | 56.130001068115234 | -0.0017783911059000568 | 29 |
| SMALL_VALUE | US Small-Cap Value | 222.05 | 221.60000610351562 | -0.0020265431050862093 | 30 |
| EUROPE | Europe Equities | 89.09 | 88.86000061035156 | -0.002581652145565605 | 31 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.52 | 79.23999786376953 | -0.00352115362462857 | 32 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.67 | 106.22000122070312 | -0.004218606724448071 | 33 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.09 | 94.55999755859375 | -0.00557369272695607 | 34 |
| CYBERSECURITY | Cybersecurity | 89.33 | 88.79000091552734 | -0.006044991430344315 | 35 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.44 | 82.8499984741211 | -0.007070967472182499 | 36 |
| ENERGY | Energy Sector | 59.2 | 58.650001525878906 | -0.009290514765559088 | 37 |
| INDUSTRIALS | Industrials Sector | 178.85 | 176.66000366210938 | -0.012244877483313488 | 38 |
| MID_CAP | US Mid-Cap Stocks | 75.69 | 74.73 | -0.01268331351565588 | 39 |
| BROAD_COMMODITIES | Broad Commodities | 17.81 | 17.56999969482422 | -0.013475592654451418 | 40 |
| SOUTH_AFRICA | South Africa Equities | 62.98 | 62.08000183105469 | -0.014290221799703184 | 41 |
| MEXICO | Mexico Equities | 76.71 | 75.56999969482422 | -0.014861169406541141 | 42 |
| SMALL_CAP | US Small-Cap Stocks | 293.79 | 288.57 | -0.017767793321760483 | 43 |
| OIL | Crude Oil | 131.68 | 129.30999755859375 | -0.017998195940205464 | 44 |
| ETHEREUM_ETF | Ethereum ETF | 14.52 | 14.239999771118164 | -0.01928376231968565 | 45 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.02 | 111.61000061035156 | -0.02113663734124216 | 46 |
| GOLD | Gold | 77.69 | 76.04000091552734 | -0.021238242817256503 | 47 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.49 | 68.94999694824219 | -0.021847113799940532 | 48 |
| UTILITIES | Utilities Sector | 45.93 | 44.90999984741211 | -0.022207710702980443 | 49 |
| TOTAL_US_MARKET | Total US Stock Market | 368.87 | 360.42 | -0.022907799495757275 | 50 |
| COPPER | Copper | 39.25 | 38.349998474121094 | -0.022929975181628204 | 51 |
| SP500 | S&P 500 | 747.41 | 729.46 | -0.02401626951739999 | 52 |
| AGRICULTURE | Agriculture Commodities | 28.23 | 27.489999771118164 | -0.026213256425144715 | 53 |
| BIOTECH | Biotechnology | 152.11 | 147.91000366210938 | -0.027611572795283923 | 54 |
| JAPAN | Japan Equities | 92.19 | 89.3499984741211 | -0.03080596079703768 | 55 |
| BRAZIL | Brazil Equities | 36.62 | 35.470001220703125 | -0.031403571253328044 | 56 |
| EMERGING_MARKETS | Emerging Markets | 58.81 | 56.91999816894531 | -0.03213742273515885 | 57 |
| BITCOIN_ETF | Bitcoin ETF | 37.34 | 36.0 | -0.03588644884841996 | 58 |
| SILVER | Silver | 53.92 | 51.77000045776367 | -0.03987387875067372 | 59 |
| LARGE_GROWTH | US Large-Cap Growth | 120.92 | 114.05 | -0.05681442275884885 | 60 |
| METALS_MINING | Metals and Mining | 103.5 | 97.58000183105469 | -0.05719804994150057 | 61 |
| NASDAQ100 | Nasdaq 100 | 705.35 | 661.73 | -0.06184163890267247 | 62 |
| BROAD_AI_TECH | Broad AI Technology | 60.14 | 55.97999954223633 | -0.06917193976993141 | 63 |
| TECHNOLOGY | Technology Sector | 180.27 | 166.57000732421875 | -0.07599707480879381 | 64 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 119.14 | 109.55999755859375 | -0.08040962264064333 | 65 |
| MOMENTUM | US Momentum Equities | 314.24 | 283.1099853515625 | -0.09906445598408065 | 66 |
| SOLAR | Solar Energy | 53.72 | 47.68000030517578 | -0.11243484167580453 | 67 |
| TAIWAN | Taiwan Equities | 101.68 | 89.41000366210938 | -0.12067266264644605 | 68 |
| SEMICONDUCTORS | Semiconductors | 586.91 | 504.2200012207031 | -0.1408904240501897 | 69 |
| SOUTH_KOREA | South Korea Equities | 170.43 | 144.2100067138672 | -0.15384611445246033 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | COMMUNICATIONS | 30.0 | 0.002838847401377853 | 0.0008516542204133559 | Alphabet beat with 24% revenue growth, Cloud +82%, margin expansion; sector pulled back last week creating entry ahead of the report's price reaction inside the window. |
| anthropic-claude-fable-5 | ENERGY | 25.0 | -0.009290514765559088 | -0.002322628691389772 | Brent +3.4% to $94 with strong recent oil momentum and 96.1% refinery utilization; energy equities lag crude's move. |
| anthropic-claude-fable-5 | BROAD_COMMODITIES | 15.0 | -0.013475592654451418 | -0.0020213388981677126 | Broad commodities show positive prior trend, strong 5-day active return, and unusual volume interest amid supply shocks and elevated inflation. |
| anthropic-claude-fable-5 | LOW_VOL | 15.0 | 0.017585313852064743 | 0.0026377970778097112 | Defensive ballast into July 29 FOMC; negative SPY beta cushions hawkish-surprise risk while retaining positive base forecast. |
| anthropic-claude-fable-5 | SP500 | 15.0 | -0.02401626951739999 | -0.0036024404276099983 | Benchmark anchor to limit tracking error around the FOMC decision. |
| anthropic-claude-opus-4-8 | ENERGY | 30.0 | -0.009290514765559088 | -0.0027871544296677263 | Strong active return with Brent up 3.4% and oil momentum; low beta diversifier ahead of tight energy inventories. |
| anthropic-claude-opus-4-8 | SP500 | 40.0 | -0.02401626951739999 | -0.009606507806959997 | Core broad exposure through FOMC week; strong Alphabet earnings support large-cap sentiment. |
| anthropic-claude-opus-4-8 | DIVIDEND | 30.0 | 0.028267532858805122 | 0.008480259857641536 | Highest recent active return (+2.71%) with very low beta and shallow drawdown; defensive tilt into FOMC. |
| google-gemini-3-1-pro | ENERGY | 50.0 | -0.009290514765559088 | -0.004645257382779544 | Strong recent momentum and positive catalyst from rising crude prices. |
| google-gemini-3-1-pro | COMMUNICATIONS | 50.0 | 0.002838847401377853 | 0.0014194237006889265 | Alphabet earnings beat provides a strong catalyst for the sector. |
| openai-gpt-5-5 | COMMUNICATIONS | 25.0 | 0.002838847401377853 | 0.0007097118503444633 | Alphabet's strong after-close revenue, margin, search, YouTube, and cloud growth provide a near-window mega-cap catalyst for communication services after a recent relative pullback. |
| openai-gpt-5-5 | ENERGY | 20.0 | -0.009290514765559088 | -0.0018581029531118177 | Energy has strong prior and recent active performance with crude prices up sharply; sector exposure is less extreme than direct oil while still benefiting from oil momentum. |
| openai-gpt-5-5 | BROAD_COMMODITIES | 20.0 | -0.013475592654451418 | -0.002695118530890284 | Broad commodities combine strong recent and prior active returns with elevated volume, offering inflation and commodity momentum exposure outside pure energy. |
| openai-gpt-5-5 | FINANCIALS | 20.0 | 0.011239969762279811 | 0.0022479939524559624 | Financials show strong prior active return and high quality evidence, with low correlation to SPY and moderate volatility supporting a one-week diversifier with upside. |
| openai-gpt-5-5 | EQUAL_WEIGHT_SP500 | 15.0 | 0.014245395992191323 | 0.0021368093988286983 | Equal-weight S&P has outperformed SPY over 5 and 21 sessions with lower volatility and shallow drawdown, supporting modest breadth exposure. |
| openai-gpt-5-6-sol | COMMUNICATIONS | 50.0 | 0.002838847401377853 | 0.0014194237006889265 | Alphabet's strong post-close revenue, cloud-growth, and margin results provide a direct near-term catalyst after the sector's recent relative pullback. |
| openai-gpt-5-6-sol | FINANCIALS | 30.0 | 0.011239969762279811 | 0.003371990928683943 | Strong prior relative performance and high cross-sectional quality are reinforced by Visa earnings before the exit close. |
| openai-gpt-5-6-sol | ENERGY | 20.0 | -0.009290514765559088 | -0.0018581029531118177 | Rising crude prices and positive prior and recent relative returns support continuation, while the smaller weight limits reversal risk. |
| xai-grok-4-3 | SP500 | 50.0 | -0.02401626951739999 | -0.012008134758699995 | Broad market exposure with neutral near-term catalyst support. |
| xai-grok-4-3 | ENERGY | 20.0 | -0.009290514765559088 | -0.0018581029531118177 | Oil inventory and Brent price strength provide base-case support. |
| xai-grok-4-3 | COMMUNICATIONS | 15.0 | 0.002838847401377853 | 0.00042582711020667797 | Alphabet revenue and cloud growth exceed expectations. |
| xai-grok-4-3 | HEALTHCARE | 15.0 | 0.04271470547051415 | 0.006407205820577122 | Defensive sector with stable relative performance. |
| xai-grok-4-5 | OIL | 30.0 | -0.017998195940205464 | -0.005399458782061639 | Strong recent oil price momentum and inventory/build data support continued energy strength into FOMC week. |
| xai-grok-4-5 | ENERGY | 20.0 | -0.009290514765559088 | -0.0018581029531118177 | Sector levered to oil strength with positive prior active returns and quality support relative to broad market. |
| xai-grok-4-5 | BROAD_COMMODITIES | 20.0 | -0.013475592654451418 | -0.002695118530890284 | Diversified commodity exposure capturing oil-linked and broader commodity momentum with elevated volume. |
| xai-grok-4-5 | COMMUNICATIONS | 15.0 | 0.002838847401377853 | 0.00042582711020667797 | Alphabet post-close beat with strong Cloud and services growth provides near-term catalyst for sector. |
| xai-grok-4-5 | FINANCIALS | 15.0 | 0.011239969762279811 | 0.0016859954643419716 | Solid prior active trend and quality score with potential rate-path clarity from FOMC. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | COMMUNICATIONS | 3 | 0.61 | 0.002838847401377853 | 0.002933311676261052 | 0.026949581193661042 | 0.03978139379425309 |  | True | True |
| openai-gpt-5-5 | COMMUNICATIONS | 5 | 0.57 | 0.002838847401377853 | 0.0005412937176270225 | 0.024557563235027013 | 0.04217341175288712 |  | True | True |
| google-gemini-3-1-pro | ENERGY | 2 | 0.65 | -0.009290514765559088 | -0.0032258336820906175 | 0.020790435835309373 | 0.045940539152604765 |  | True | False |
| anthropic-claude-opus-4-8 | SP500 | 3 | 0.55 | -0.02401626951739999 | -0.003913402378986188 | 0.020102867138413805 | 0.04662810784950033 |  | True | False |
| anthropic-claude-fable-5 | COMMUNICATIONS | 5 | 0.6 | 0.002838847401377853 | -0.004456956718944416 | 0.019559312798455575 | 0.04717166218945856 |  | True | False |
| xai-grok-4-3 | SP500 | 4 | 0.55 | -0.02401626951739999 | -0.0070332047810280135 | 0.016983064736371976 | 0.04974791025154216 |  | True | False |
| xai-grok-4-5 | OIL | 5 | 0.58 | -0.017998195940205464 | -0.00784085769151509 | 0.016175411825884903 | 0.050555563162029235 |  | True | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | COMMUNICATIONS | 0.019559312798455575 | 0.44947 | 0.043516392191816085 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | cb55d4f2bd27e6e6aa8e4b54096b80c92f156c975fa794fe4f628217de1709dc |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 1a844da9c59ab06e30e88b53a60f08b23075e0cfd4df40bd80afc8570a93c261 |
| manifest.yaml | 89ae3d497546b468a1d92aa81c1346a70edbd914bddc936187bee3c4c669e166 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 5a7927838ae172914b7dce271e42cae9992c7057133defd8cb7c3b192dd3fe2c |
| market_data/universe_decision_context.md | d415d03b13e6cf854b26170a6c59ca6b1d538cee6e9db3b846384d48f9e6b3dc |
| market_data/universe_decision_context.json | 2ac061341e3d56caa0e669e9b1129dc481052ad0833015f07ded5a0f32844425 |
| market_data/decision_context_source_history.json | 3b6297d7bb8222ff6ad473dba91c4829c4bfaa6642aecfcbc8ed3eee79ef501b |
| market_data/universe_quality_evidence.md | 41de789c95a28082504460d2466ed190b4cf293c62493c2130e60df519cf61f4 |
| market_data/universe_quality_evidence.json | 9b516cc78ec7321a8642e6505c8f17f1f438bc1c1b915fd0ab33a3ee3f8a1b7c |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 7fb9ac9a4b425eb97ea8a28ffd7ad984a86dda5523fef6d179f6bd012c1d59a2 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 75203e137c74b00b27ca12143c55a95bc5ef73c0bd302848818844031c99a196 | yes |
| Final briefing | research/final_briefing.md | model-facing | cb55d4f2bd27e6e6aa8e4b54096b80c92f156c975fa794fe4f628217de1709dc | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
