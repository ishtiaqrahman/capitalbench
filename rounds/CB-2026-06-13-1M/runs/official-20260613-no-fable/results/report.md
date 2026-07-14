# CapitalBench Report: CB-2026-06-13-1M / official-20260613-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260613-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 13 2026 One-Month Portfolio Round
- Description: One-month CapitalBench portfolio evaluation round scored from the June 12, 2026 adjusted-close snapshot to the July 13, 2026 adjusted close.
- Decision date: 2026-06-13
- Decision deadline: 2026-06-13T23:30:00Z
- Horizon: one month
- Entry date: 2026-06-12
- Exit date: 2026-07-13
- Entry rule: Use adjusted close on Friday, June 12, 2026 as the post-close entry snapshot for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Monday, July 13, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.7 | This portfolio balances potential equity upside with a defensive cash-like allocation. | A sudden market downturn could negatively impact the equity portion.; Interest rate changes could affect the short-term treasury allocation.; Technology sector underperformance could drag down the Nasdaq 100 allocation. |
| xai-grok-4-3 | xai | portfolio | SMALL_VALUE | 4 | 0.65 | Allocation prioritizes factors with recent positive price action and alignment with scheduled data releases on growth and inflation that could support cyclical and tech exposure before July 13 exit. | Sticky inflation readings prompting unexpected hawkish FOMC signals on June 17; Weaker-than-expected retail sales or employment data triggering broad equity rotation; Oil price volatility from scheduled EIA reports pressuring energy-sensitive sectors; Sharp reversal in momentum or semiconductor leadership due to valuation compression |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.57 | Overweight the strongest-momentum, rate-sensitive-favorable equity exposures to beat SPY over the one-month window as financial conditions ease. | Hawkish surprise or hawkish dot-plot at the June 17 FOMC could hit high-beta semis, momentum, and regional banks hardest.; Semiconductor and momentum crowding leaves the book vulnerable to a sharp factor unwind or AI-trade pullback.; Headline YoY CPI re-accelerating (4.2%) and elevated PPI could revive inflation fears and lift yields, pressuring rate-sensitive positions.; Concentration in cyclical/high-beta names amplifies drawdown if equity breadth reverses or VIX spikes. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Tilt toward AI/semis and momentum with small-cap breadth play, hedged with intermediate duration as inflation softens into the FOMC. | Hawkish FOMC surprise on 6/17 pushing yields higher and hitting growth/small caps; Semiconductor pullback after strong rally (SMH +75% 6m); Headline CPI re-acceleration from energy disrupting rate-cut narrative; Taiwan geopolitical shock; Crowded momentum factor reversal |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.62 | Risk appetite remains supported by stable labor data, improving surveys, and a highly probable Fed hold, while the strongest realized leadership is in semiconductors and momentum. The allocation deliberately takes high-beta exposure to outperform the S&P 500 over a short scoring window. | A sharp reversal in AI or semiconductor sentiment could disproportionately hurt the largest allocations.; Hot PCE, employment, or ISM prices data could push yields higher and compress growth-stock valuations.; South Korea and Taiwan exposures carry currency, export-cycle, and geopolitical risks that could overwhelm sector momentum.; The FOMC statement or minutes could be more hawkish than expected despite the high implied probability of a hold.; Regional banks could underperform if credit-quality or commercial-real-estate concerns re-emerge. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 133.65878295898438 | 155.34 | 0.16221318615230018 | 1 |
| CYBERSECURITY | Cybersecurity | 85.25668334960938 | 91.84 | 0.07721760208985184 | 2 |
| ETHEREUM_ETF | Ethereum ETF | 12.569999694824219 | 13.37 | 0.0636436216864178 | 3 |
| AGRICULTURE | Agriculture Commodities | 26.239999771118164 | 27.72 | 0.05640244823899887 | 4 |
| FINANCIALS | Financials Sector | 53.153804779052734 | 56.06999969482422 | 0.054863333450792195 | 5 |
| HEALTHCARE | Healthcare Sector | 153.13462829589844 | 161.41000366210938 | 0.0540398697427249 | 6 |
| UTILITIES | Utilities Sector | 44.24745559692383 | 45.720001220703125 | 0.03327978081256422 | 7 |
| REGIONAL_BANKS | Regional Banks | 72.9831771850586 | 75.12 | 0.029278292578619913 | 8 |
| LOW_VOL | US Low Volatility Equities | 74.32939147949219 | 76.41000366210938 | 0.02799178280897463 | 9 |
| INDUSTRIALS | Industrials Sector | 175.7476043701172 | 180.3699951171875 | 0.02630130159461941 | 10 |
| LARGE_VALUE | US Large-Cap Value | 241.36900329589844 | 247.6199951171875 | 0.025898071980791526 | 11 |
| SOFTWARE | Software | 90.68299102783203 | 92.7 | 0.022242417782061485 | 12 |
| US_DOLLAR | US Dollar | 27.950000762939453 | 28.5 | 0.019677968588459605 | 13 |
| BRAZIL | Brazil Equities | 34.76900100708008 | 35.39 | 0.01786070853152988 | 14 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 210.83348083496094 | 214.23 | 0.016109961053566435 | 15 |
| SP500 | S&P 500 | 739.843994140625 | 749.1699829101562 | 0.012605344969197185 | 16 |
| TOTAL_US_MARKET | Total US Stock Market | 365.30914306640625 | 369.7799987792969 | 0.012238554106153154 | 17 |
| SMALL_VALUE | US Small-Cap Value | 217.5449981689453 | 219.77999877929688 | 0.010273739360423528 | 18 |
| INDIA | India Equities | 48.33000183105469 | 48.79 | 0.0095178595389529 | 19 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 233.62599182128906 | 235.05 | 0.006095247226602485 | 20 |
| JAPAN | Japan Equities | 92.20899963378906 | 92.72 | 0.005541762390226523 | 21 |
| SMALL_CAP | US Small-Cap Stocks | 292.2550048828125 | 293.4800109863281 | 0.004191565869015035 | 22 |
| CANADA | Canada Equities | 58.48500061035156 | 58.73 | 0.0041890978386187605 | 23 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.24237823486328 | 91.5 | 0.0028234880558855036 | 24 |
| COMMUNICATIONS | Communication Services Sector | 111.36029815673828 | 111.58999633789062 | 0.002062657742071039 | 25 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.76253509521484 | 106.9 | 0.0012875762519366507 | 26 |
| LARGE_GROWTH | US Large-Cap Growth | 121.50299835205078 | 121.58999633789062 | 0.0007160151355916078 | 27 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 28 |
| DIVIDEND | US Dividend Equities | 32.5606803894043 | 32.560001373291016 | -2.085386746097928e-05 | 29 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.5711441040039 | 79.52 | -0.0006427468723719798 | 30 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.36811828613281 | 116.04000091552734 | -0.002819650050529088 | 31 |
| UNITED_KINGDOM | United Kingdom Equities | 46.49399948120117 | 46.36 | -0.002882081186742269 | 32 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.14938735961914 | 47.89 | -0.005387137279272536 | 33 |
| TIPS | Treasury Inflation-Protected Securities | 108.55026245117188 | 107.91 | -0.005898304036435431 | 34 |
| REAL_ESTATE | Real Estate Sector | 44.96596908569336 | 44.70000076293945 | -0.005914880256378763 | 35 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.96033477783203 | 95.38 | -0.0060476527012502945 | 36 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.87028503417969 | 93.29 | -0.006181775563676939 | 37 |
| EUROPE | Europe Equities | 88.41575622558594 | 87.86 | -0.006285714778799911 | 38 |
| ENERGY | Energy Sector | 57.137935638427734 | 56.7400016784668 | -0.006964444121311808 | 39 |
| TAIWAN | Taiwan Equities | 102.62000274658203 | 101.88 | -0.007211096538454198 | 40 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.42973327636719 | 97.71 | -0.007312153070113014 | 41 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.22863006591797 | 84.58999633789062 | -0.007493183071620502 | 42 |
| MID_CAP | US Mid-Cap Stocks | 75.85100555419922 | 75.23999786376953 | -0.00805536704444998 | 43 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.04349517822266 | 93.26 | -0.008331200119028326 | 44 |
| BROAD_COMMODITIES | Broad Commodities | 17.059999465942383 | 16.9 | -0.009378632529373654 | 45 |
| EMERGING_MARKETS | Emerging Markets | 59.47930908203125 | 58.79 | -0.011589056642883788 | 46 |
| NASDAQ100 | Nasdaq 100 | 720.5481567382812 | 711.739990234375 | -0.012224257909115077 | 47 |
| YEN | Japanese Yen | 57.2599983215332 | 56.46 | -0.013971329811100497 | 48 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.62821197509766 | 106.96 | -0.015357078467609253 | 49 |
| AUSTRALIA | Australia Equities | 28.815000534057617 | 28.35 | -0.01613744665761896 | 50 |
| EURO | Euro | 106.75907897949219 | 105.01 | -0.01638342140276583 | 51 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.45439147949219 | 83.97 | -0.01737056988871566 | 52 |
| TECHNOLOGY | Technology Sector | 184.5799102783203 | 181.27999877929688 | -0.017877955916478894 | 53 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.17536163330078 | 69.76 | -0.019885555911788644 | 54 |
| BITCOIN_ETF | Bitcoin ETF | 36.040000915527344 | 35.22 | -0.02275252205041034 | 55 |
| MATERIALS | Materials Sector | 51.98562240600586 | 50.58000183105469 | -0.027038640875996944 | 56 |
| MOMENTUM | US Momentum Equities | 324.0419921875 | 314.6300048828125 | -0.029045579065695493 | 57 |
| CHINA | China Equities | 54.46900177001953 | 52.53 | -0.03559826152508605 | 58 |
| COPPER | Copper | 39.54999923706055 | 37.94 | -0.04070794609654227 | 59 |
| SOUTH_AFRICA | South Africa Equities | 65.43600463867188 | 62.76 | -0.040894988217089145 | 60 |
| MEXICO | Mexico Equities | 77.33200073242188 | 74.15 | -0.04114727024109954 | 61 |
| BROAD_AI_TECH | Broad AI Technology | 64.0 | 61.3 | -0.042187500000000044 | 62 |
| GOLD | Gold | 79.19000244140625 | 75.25 | -0.049753786083306495 | 63 |
| SEMICONDUCTORS | Semiconductors | 619.9600219726562 | 585.62 | -0.05539070384472444 | 64 |
| OIL | Crude Oil | 125.43000030517578 | 117.79 | -0.06091047027495311 | 65 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 129.41000366210938 | 120.7 | -0.06730548965017624 | 66 |
| SILVER | Silver | 61.290000915527344 | 52.16 | -0.14896395462794543 | 67 |
| SOUTH_KOREA | South Korea Equities | 197.4499969482422 | 168.02 | -0.14905037935228072 | 68 |
| METALS_MINING | Metals and Mining | 120.35765838623047 | 102.09 | -0.1517781139244927 | 69 |
| SOLAR | Solar Energy | 63.029998779296875 | 53.12 | -0.15722670111413617 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | -0.05539070384472444 | -0.01661721115341733 | Strong momentum, AI capex tailwind, leading sector with broadening rally. |
| anthropic-claude-opus-4-7 | MOMENTUM | 25.0 | -0.029045579065695493 | -0.007261394766423873 | Strong factor momentum with cooling core CPI supporting risk-on into FOMC. |
| anthropic-claude-opus-4-7 | SMALL_CAP | 15.0 | 0.004191565869015035 | 0.0006287348803522552 | Yields falling, ISM improving, breadth broadening favors small caps. |
| anthropic-claude-opus-4-7 | TAIWAN | 15.0 | -0.007211096538454198 | -0.0010816644807681297 | Semiconductor cycle leadership and strong trailing momentum. |
| anthropic-claude-opus-4-7 | INTERMEDIATE_TREASURY | 15.0 | -0.006181775563676939 | -0.0009272663345515408 | Hedge: cooling core inflation and dovish-leaning FOMC could push yields lower. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | -0.05539070384472444 | -0.01661721115341733 | Strongest momentum (+8.3% 30d, +75% 6m) with declining VIX and AI capex tailwinds; semis leadership intact heading into earnings season. |
| anthropic-claude-opus-4-8 | MOMENTUM | 25.0 | -0.029045579065695493 | -0.007261394766423873 | Best risk-adjusted factor trend (+6.2% 30d) capturing broad winners; benefits from risk-on conditions as VIX falls to 17.7. |
| anthropic-claude-opus-4-8 | REGIONAL_BANKS | 15.0 | 0.029278292578619913 | 0.004391743886792987 | Steepening curve, easing inflation (core CPI 0.2% MoM), and strong 30d momentum (+9.3%); benefits from Fed-on-hold stable-rate backdrop. |
| anthropic-claude-opus-4-8 | MID_CAP | 15.0 | -0.00805536704444998 | -0.0012083050566674969 | Solid breadth participation (+4.0% 30d) with cheaper valuation than mega-caps; benefits from improving ISM and falling yields. |
| anthropic-claude-opus-4-8 | TECHNOLOGY | 15.0 | -0.017877955916478894 | -0.002681693387471834 | Broad tech sector strength (+4.5% 30d) with cooling rates and resilient earnings growth supporting continued large-cap tech leadership. |
| google-gemini-3-1-pro | SP500 | 40.0 | 0.012605344969197185 | 0.005042137987678875 | Broad US equity exposure to capture general market upside. |
| google-gemini-3-1-pro | NASDAQ100 | 30.0 | -0.012224257909115077 | -0.003667277372734523 | Growth and technology tilt for potential outperformance. |
| google-gemini-3-1-pro | SHORT_TREASURY | 30.0 | 0.0028234880558855036 | 0.000847046416765651 | Cash-like proxy to reduce overall portfolio volatility. |
| openai-gpt-5-5 | SEMICONDUCTORS | 40.0 | -0.05539070384472444 | -0.022156281537889778 | Strongest AI-linked price leadership in the universe with 8.3% 30-day and 75.6% 6-month trailing returns; likely to benefit if growth and technology momentum persists over the month. |
| openai-gpt-5-5 | SOUTH_KOREA | 20.0 | -0.14905037935228072 | -0.029810075870456143 | Very strong recent and medium-term performance, with heavy sensitivity to semiconductors and exports, offering high beta to the same leadership theme. |
| openai-gpt-5-5 | TAIWAN | 15.0 | -0.007211096538454198 | -0.0010816644807681297 | Semiconductor supply-chain exposure with strong 30-day and 6-month trailing returns, complementing direct US semiconductor exposure. |
| openai-gpt-5-5 | MOMENTUM | 15.0 | -0.029045579065695493 | -0.004356836859854323 | Broad US momentum factor has strong 7-day, 30-day, and 6-month returns and may capture continued trend persistence beyond a single sector. |
| openai-gpt-5-5 | REGIONAL_BANKS | 10.0 | 0.029278292578619913 | 0.0029278292578619916 | Recent leadership, positive 10-year/2-year curve, and lower Treasury yields support a tactical cyclical financial exposure if risk appetite broadens. |
| xai-grok-4-3 | SMALL_VALUE | 30.0 | 0.010273739360423528 | 0.0030821218081270585 | Recent 30d outperformance and sensitivity to domestic growth catalysts within scoring window |
| xai-grok-4-3 | MOMENTUM | 30.0 | -0.029045579065695493 | -0.008713673719708647 | Strong trailing momentum factor performance likely to persist over one-month horizon |
| xai-grok-4-3 | SEMICONDUCTORS | 25.0 | -0.05539070384472444 | -0.01384767596118111 | Elevated recent returns and exposure to earnings growth estimates in tech supply chain |
| xai-grok-4-3 | TECHNOLOGY | 15.0 | -0.017877955916478894 | -0.002681693387471834 | Complements semiconductor tilt with broad sector exposure amid positive breadth signals |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | SP500 | 3 | 0.7 | 0.012605344969197185 | 0.002221907031710003 | -0.010383437937487182 | 0.1599912791205902 |  | False | True |
| xai-grok-4-3 | SMALL_VALUE | 4 | 0.65 | 0.010273739360423528 | -0.022160921260234532 | -0.034766266229431714 | 0.1843741074125347 |  | False | False |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.57 | -0.05539070384472444 | -0.02337686047718755 | -0.03598220544638474 | 0.18559004662948772 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | -0.05539070384472444 | -0.02525880185480862 | -0.03786414682400581 | 0.1874719880071088 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.62 | -0.05539070384472444 | -0.05447702949110638 | -0.06708237446030357 | 0.21669021564340657 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 107eddb7c4004e3184ae0af7ae84206fd78eb41eec22590857cccc1ff17ef597 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 0e5a222ebba001788946308d0e0b4c71b9e1bdc4f2882aad00ed1514ecaa5c5f |
| manifest.yaml | 14cd5f142470173d66812a934271317189206f59d3667bab89b3f695252906f8 |
| market_data/universe_trailing_returns.csv | 29ce3e75a78c914f42a7358bdbb62922c3d4dd51dc526ce83e318d784b7fa4b4 |
| market_data/universe_trailing_returns.md | 03b954f3e297410c2febcbbefd22ec734ca7df2f371bfd9f1f3ad28e3229f51d |
| market_data/universe_trailing_returns.json | 9e44263b0c84f6ca24eaf5073c59d4f5fae611b5d605e065fc0082e09cdb1c5c |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 58999fe6aac9921ea9ae442b639a0517274f9b8cdbd75fe76b8682efedf94502 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 6dff766f1ff037be2ed9cc6eb418361e84d904df5cbf5816c03f2998e72c36c7 | yes |
| Final briefing | research/final_briefing.md | model-facing | 107eddb7c4004e3184ae0af7ae84206fd78eb41eec22590857cccc1ff17ef597 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
