# CapitalBench Report: CB-2026-09-11-1W / official-v3-20260911-weekly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260911-weekly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-09-11-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-09-11
- Decision deadline: 2026-09-11T13:25:00Z
- Horizon: one week
- Entry date: 2026-09-11
- Exit date: 2026-09-18
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | HEALTHCARE | 3 | 0.59 | Weak breadth, hot PPI, strong oil continuation, and quality pullbacks amid upcoming CPI/FOMC create mixed one-week setup with limited cross-sectional dispersion and defensive bias. | Unknown August CPI print on entry day could reverse rate-sensitive and defensive flows; FOMC mid-window may reprice duration and growth expectations; Oil continuation fades if inventories or demand surprise; Low dispersion limits magnitude of any single-name excess |
| anthropic-claude-opus-5 | anthropic | portfolio | HEALTHCARE | 3 | 0.5633 | Hot PPI (0.4% m/m, 5.4% y/y) with 10y at 4.95% and a September 15-16 FOMC plus CPI on Sept 11 create a rate-sensitive, inflation-tilted week. Breadth is weak (RSP lagging SPY by 1.5% over 5 sessions, only 22% of assets positive), and energy/commodities are the only sustained strength. Recent one-week losers with strong prior relative trends (healthcare, biotech, dividend) are plausible mean-reversion candidates into event risk, but conviction is moderate; most of the slate has no reliable weekly edge. | Hot August CPI on Sept 11 or hawkish FOMC projections could hit rate-sensitive and biotech exposure hardest; Healthcare/biotech pullbacks may reflect policy or pipeline deterioration rather than temporary overreaction; Continued oil spike would drive energy/commodity outperformance, leaving defensive picks behind; SPY rebound in mega-cap tech would make low-beta defensives lag mechanically |
| xai-grok-4-6 | xai | portfolio | HEALTHCARE | 3 | 0.5633 | SPY is modestly lower with weak equal-weight breadth while PPI and energy prices jumped and CPI/FOMC sit inside the week; quality sectors sold off versus prior relative strength while oil/commodities already ran to highs, so the week is mixed reversal-versus-continuation rather than a clean trend. | Unknown August CPI on Sep 11 and FOMC Sep 15–16 can dominate the entire close-to-close week.; Hot PPI goods/energy and Brent at $107.63 can keep inflation-sensitive duration and defensives under pressure.; Biotech/metals/oil 80% ranges are wide given 30%+ horizon vols.; Equal-weight underperformance and 21.74% positive-asset share can persist if breadth stays negative. |
| anthropic-claude-fable-5-1 | anthropic | portfolio | HEALTHCARE | 3 | 0.56 | Risk-off tape with SPY down 1.6% over three sessions, 10-year at 4.95%, PPI hot at 0.4% m/m, Brent up 6.3% to $107.63, and ECB hiking. Breadth weak (RSP lagging SPY by 1.5% on 5 sessions, only 22% of assets positive). Week contains CPI at entry, FOMC Sept 15-16, and retail sales; oil-driven inflation is the central macro driver. Recent decliners with strong prior relative trends (healthcare, biotech, dividend) are plausible mean-reversion candidates, while oil/commodities show supported continuation from a supply-driven energy shock that is fully priced into the tape. | CPI on Sept 11 and FOMC Sept 15-16 could reprice rates sharply, hurting rate-sensitive biotech and duration proxies; Oil momentum could reverse abruptly after a 6.3% one-day Brent jump, or continue and weigh on broad equities; Healthcare weakness could reflect unreported policy or drug-pricing news rather than overreaction; Biotech vol of 33% means a single week can swing several percent relative to SPY |
| openai-gpt-6-astra | openai | portfolio | HEALTHCARE | 3 | 0.595 | Wide active-return dispersion, weak breadth and energy-led inflation favor selective defensive reversals rather than a broad rebound. Healthcare and dividend equities have stronger pullback evidence than cyclical losers. Commodity strength has independent inflation support, but oil's exceptional advance creates substantial reversal risk. CPI precedes the entry close; the FOMC, retail sales and housing releases can drive returns during the actual holding period. | September 11 CPI is unknown and occurs before entry; its repricing may eliminate the apparent pullback opportunities.; The September 15–16 FOMC and projections may lift yields further, hurting dividend valuations and biotech financing expectations.; An oil reversal could undermine commodity continuation, while another surge could worsen equity margin and inflation pressure.; Healthcare's selloff may reflect unreported sector deterioration; the supplied quality score is price-derived rather than direct fundamental evidence. |
| google-gemini-3-1-pro | google | portfolio | HEALTHCARE | 3 | 0.565 | The market is experiencing a broad pullback, with the S&P 500 down 1.6% over the past week. Energy and commodities are showing strength, while most other sectors are declining. The upcoming CPI release and FOMC meeting introduce significant uncertainty. | Upcoming CPI release could cause market volatility.; FOMC meeting could lead to unexpected interest rate changes. |
| xai-grok-4-3 | xai | portfolio | SP500 | 2 | 0.58 | Commodity strength from oil and broad indices contrasts with equity pullbacks amid rising producer prices and stable claims; one-week window favors continuation in energy while testing reversals in quality sectors. | CPI release on September 11 may shift rate expectations; ECB rate path uncertainty affecting global flows; Oil inventory and OPEC signals within window; Equity breadth deterioration continuing |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| CYBERSECURITY | Cybersecurity | 94.4 | 99.87 | 0.057944915254237284 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 43.77000045776367 | 46.02000045776367 | 0.05140507142948647 | 2 |
| ETHEREUM_ETF | Ethereum ETF | 19.15999984741211 | 19.920000076293945 | 0.039665983034153696 | 3 |
| SILVER | Silver | 58.12 | 59.93000030517578 | 0.031142469118647265 | 4 |
| SOFTWARE | Software | 101.52 | 104.35 | 0.027876280535855003 | 5 |
| COPPER | Copper | 39.18 | 40.22999954223633 | 0.02679937575896707 | 6 |
| HEALTHCARE | Healthcare Sector | 165.36 | 168.39 | 0.01832365747460063 | 7 |
| US_DOLLAR | US Dollar | 28.06999969482422 | 28.389999389648438 | 0.011400060502431142 | 8 |
| TECHNOLOGY | Technology Sector | 187.67 | 189.6 | 0.01028400916502381 | 9 |
| NASDAQ100 | Nasdaq 100 | 714.88 | 721.45 | 0.009190353625783354 | 10 |
| MOMENTUM | US Momentum Equities | 307.04 | 309.62 | 0.008402813965606937 | 11 |
| LARGE_GROWTH | US Large-Cap Growth | 122.27 | 123.25 | 0.008015048662795454 | 12 |
| SEMICONDUCTORS | Semiconductors | 568.53 | 573.0 | 0.007862381932352003 | 13 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 121.36 | 122.2 | 0.006921555702043447 | 14 |
| TAIWAN | Taiwan Equities | 110.91 | 111.64 | 0.006581913263006056 | 15 |
| GOLD | Gold | 81.71 | 82.23 | 0.0063639701382940395 | 16 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 80.87 | 81.25 | 0.0046988994682823915 | 17 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 104.32 | 104.7 | 0.0036426380368099753 | 18 |
| BIOTECH | Biotechnology | 156.2 | 156.72 | 0.0033290653008963833 | 19 |
| BROAD_AI_TECH | Broad AI Technology | 63.98 | 64.13 | 0.0023444826508283167 | 20 |
| CHINA | China Equities | 52.96 | 53.07 | 0.0020770392749245303 | 21 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.99 | 47.04999923706055 | 0.001276851182390848 | 22 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.5 | 91.55 | 0.0005464480874317612 | 23 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 93.34 | 93.37999725341797 | 0.00042851139295008167 | 24 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 25 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 95.98 | 95.96 | -0.00020837674515539195 | 26 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 78.6 | 78.53 | -0.0008905852417302462 | 27 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 91.38 | 91.29 | -0.000984898227183062 | 28 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 91.01 | 90.8 | -0.002307438742995327 | 29 |
| TOTAL_US_MARKET | Total US Stock Market | 376.31 | 375.43 | -0.002338497515346427 | 30 |
| MUNICIPAL_BONDS | Municipal Bonds | 103.17 | 102.88 | -0.002810894639914796 | 31 |
| SP500 | S&P 500 | 764.29 | 761.69 | -0.0034018500830835796 | 32 |
| TIPS | Treasury Inflation-Protected Securities | 105.84 | 105.27 | -0.005385487528344779 | 33 |
| EMERGING_MARKETS | Emerging Markets | 60.35 | 60.01 | -0.005633802816901512 | 34 |
| CANADA | Canada Equities | 60.58 | 60.22 | -0.005942555298778518 | 35 |
| BROAD_COMMODITIES | Broad Commodities | 19.79 | 19.66 | -0.0065689742294087194 | 36 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.38 | 82.8 | -0.006956104581434364 | 37 |
| OIL | Crude Oil | 154.9 | 153.82000732421875 | -0.006972192871409044 | 38 |
| EURO | Euro | 107.01000213623047 | 105.98999786376953 | -0.009531859191652114 | 39 |
| INDIA | India Equities | 48.57 | 48.02 | -0.011323862466543044 | 40 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 214.87 | 212.29 | -0.012007260203844239 | 41 |
| ENERGY | Energy Sector | 65.14 | 64.31 | -0.012741786920478892 | 42 |
| DIVIDEND | US Dividend Equities | 34.12 | 33.68 | -0.01289566236811246 | 43 |
| UNITED_KINGDOM | United Kingdom Equities | 47.94 | 47.27 | -0.013975803087192262 | 44 |
| LARGE_VALUE | US Large-Cap Value | 255.58 | 251.7 | -0.015181156585022393 | 45 |
| INDUSTRIALS | Industrials Sector | 172.37 | 169.75 | -0.015199860764634199 | 46 |
| REGIONAL_BANKS | Regional Banks | 73.9 | 72.75 | -0.01556156968876865 | 47 |
| JAPAN | Japan Equities | 98.56 | 97.0 | -0.015827922077922052 | 48 |
| COMMUNICATIONS | Communication Services Sector | 112.6 | 110.81 | -0.01589698046181165 | 49 |
| LOW_VOL | US Low Volatility Equities | 73.79 | 72.58 | -0.016397885892397435 | 50 |
| SMALL_CAP | US Small-Cap Stocks | 288.89 | 284.1 | -0.016580705458825062 | 51 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.96 | 111.03 | -0.017085694050991473 | 52 |
| BRAZIL | Brazil Equities | 38.19 | 37.52 | -0.01754385964912264 | 53 |
| AUSTRALIA | Australia Equities | 29.27 | 28.75 | -0.01776563033823031 | 54 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.69 | 71.38 | -0.01802173613977165 | 55 |
| SMALL_VALUE | US Small-Cap Value | 219.69 | 215.58 | -0.018708179707769945 | 56 |
| MATERIALS | Materials Sector | 50.95 | 49.99 | -0.018842001962708577 | 57 |
| MID_CAP | US Mid-Cap Stocks | 74.44 | 72.98 | -0.01961311123052112 | 58 |
| EUROPE | Europe Equities | 90.02 | 88.21 | -0.020106642968229282 | 59 |
| YEN | Japanese Yen | 59.68000030517578 | 58.47999954223633 | -0.02010725128691704 | 60 |
| REAL_ESTATE | Real Estate Sector | 43.42 | 42.53 | -0.02049746660525109 | 61 |
| SOUTH_AFRICA | South Africa Equities | 70.1 | 68.49 | -0.022967189728958615 | 62 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 219.01 | 213.84 | -0.02360622802611745 | 63 |
| FINANCIALS | Financials Sector | 57.25 | 55.86 | -0.024279475982532772 | 64 |
| AGRICULTURE | Agriculture Commodities | 28.93 | 28.149999618530273 | -0.026961644710325805 | 65 |
| MEXICO | Mexico Equities | 75.38 | 73.34 | -0.02706288140090196 | 66 |
| UTILITIES | Utilities Sector | 42.39 | 41.1 | -0.030431705590941216 | 67 |
| SOLAR | Solar Energy | 47.15 | 45.66 | -0.03160127253446454 | 68 |
| SOUTH_KOREA | South Korea Equities | 188.72 | 181.31 | -0.039264518863925346 | 69 |
| METALS_MINING | Metals and Mining | 113.63 | 108.68 | -0.04356243949661176 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | HEALTHCARE | 35.0 | 0.01832365747460063 | 0.00641328011611022 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | DIVIDEND | 35.0 | -0.01289566236811246 | -0.004513481828839361 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | BIOTECH | 30.0 | 0.0033290653008963833 | 0.000998719590268915 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | HEALTHCARE | 35.0 | 0.01832365747460063 | 0.00641328011611022 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | BIOTECH | 35.0 | 0.0033290653008963833 | 0.001165172855313734 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | DIVIDEND | 30.0 | -0.01289566236811246 | -0.0038686987104337377 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | HEALTHCARE | 35.0 | 0.01832365747460063 | 0.00641328011611022 | V3 selected model rank 3: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | DIVIDEND | 35.0 | -0.01289566236811246 | -0.004513481828839361 | V3 selected model rank 4: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SP500 | 30.0 | -0.0034018500830835796 | -0.0010205550249250738 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| openai-gpt-6-astra | HEALTHCARE | 35.0 | 0.01832365747460063 | 0.00641328011611022 | V3 selected model rank 1: overreaction with 59% estimated probability of beating SPY. |
| openai-gpt-6-astra | DIVIDEND | 35.0 | -0.01289566236811246 | -0.004513481828839361 | V3 selected model rank 3: overreaction with 60% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 30.0 | -0.0034018500830835796 | -0.0010205550249250738 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | DIVIDEND | 35.0 | -0.01289566236811246 | -0.004513481828839361 | V3 selected model rank 3: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 65.0 | -0.0034018500830835796 | -0.002211202554004327 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | HEALTHCARE | 35.0 | 0.01832365747460063 | 0.00641328011611022 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | BIOTECH | 35.0 | 0.0033290653008963833 | 0.001165172855313734 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | DIVIDEND | 30.0 | -0.01289566236811246 | -0.0038686987104337377 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | HEALTHCARE | 35.0 | 0.01832365747460063 | 0.00641328011611022 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | DIVIDEND | 35.0 | -0.01289566236811246 | -0.004513481828839361 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | BIOTECH | 30.0 | 0.0033290653008963833 | 0.000998719590268915 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | HEALTHCARE | 3 | 0.59 | 0.01832365747460063 | 0.003709754260990216 | 0.007111604344073796 | 0.054235160993247065 |  | True | True |
| anthropic-claude-opus-5 | HEALTHCARE | 3 | 0.5633 | 0.01832365747460063 | 0.003709754260990216 | 0.007111604344073796 | 0.054235160993247065 |  | True | True |
| xai-grok-4-6 | HEALTHCARE | 3 | 0.5633 | 0.01832365747460063 | 0.002898517877539774 | 0.006300367960623354 | 0.05504639737669751 |  | True | True |
| anthropic-claude-fable-5-1 | HEALTHCARE | 3 | 0.56 | 0.01832365747460063 | 0.002898517877539774 | 0.006300367960623354 | 0.05504639737669751 |  | True | True |
| openai-gpt-6-astra | HEALTHCARE | 3 | 0.595 | 0.01832365747460063 | 0.0008792432623457855 | 0.004281093345429365 | 0.0570656719918915 |  | True | True |
| google-gemini-3-1-pro | HEALTHCARE | 3 | 0.565 | 0.01832365747460063 | 0.0008792432623457855 | 0.004281093345429365 | 0.0570656719918915 |  | True | True |
| xai-grok-4-3 | SP500 | 2 | 0.58 | -0.0034018500830835796 | -0.006724684382843687 | -0.0033228342997601076 | 0.06466959963708097 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 20df25a39229eee4543fef405828cadce88b6c355d52b32e97f1a52864f11b6a |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | 1239cc612614e739f39131c46e3f1a8850ffadac61b4706c954b1985d0fe0903 |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 74506f90b663aafc851d9181e27f79a358459cc20722aecd013d0d335ee2b9d4 |
| market_data/universe_decision_context.md | 55126c393f4b5ffc42acc95195094af428c622226ed64165c5a84733ab20df34 |
| market_data/universe_decision_context.json | ae6feba30b867893fc1282d15936ce8a5ef0cfce30c0b70cbfcd57ab9dd3902e |
| market_data/decision_context_source_history.json | c6baf13a3ef016fc8d2bbeabe8ae6ae77c3d53e58d5d1222c126dbae15ccf572 |
| market_data/universe_quality_evidence.md | fbd5b7e2f5e7bc337db02b68d87be2be4fd3affe05de8a663138f5faece54fcb |
| market_data/universe_quality_evidence.json | b3fa07bf8a4d886ad440c139613d2431f61e4dc7cdd9f3e42282ca9ec8f786ae |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 11df89771bf0af0aed6b14ffe8fd0f387e6c66c3ea6383b7a4e42a9ee4c25ad8 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | c08950be890892bef39200cb1f61ac209eb788dc2312e86c23834cb665a97b7f | yes |
| Final briefing | research/final_briefing.md | model-facing | 20df25a39229eee4543fef405828cadce88b6c355d52b32e97f1a52864f11b6a | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
