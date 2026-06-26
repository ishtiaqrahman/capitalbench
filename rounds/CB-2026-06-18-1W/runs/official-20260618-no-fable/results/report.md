# CapitalBench Report: CB-2026-06-18-1W / official-20260618-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260618-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-18-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-06-18
- Decision deadline: 2026-06-19T02:30:00Z
- Horizon: one week
- Entry date: 2026-06-18
- Exit date: 2026-06-25
- Entry rule: Use adjusted close prices on Thursday, June 18, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Thursday, June 25, 2026 as the one-week exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 4 | 0.55 | Risk-on continuation in dominant US tech/large-cap leadership, partially hedged with cash-like BIL. | Semiconductor and Nasdaq momentum reverses after extended run, dragging the high-beta sleeve; Hawkish FOMC dots and sticky 4.2% CPI lift yields, pressuring growth multiples; Holiday-shortened liquidity amplifies an adverse intraday move into the June 25 exit close |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.65 | Overweighting high-momentum tech and semiconductors while maintaining a core S&P 500 position. | A sudden reversal in technology and semiconductor momentum.; Geopolitical tensions affecting semiconductor supply chains, particularly in Taiwan.; Unexpected hawkish shifts in interest rate expectations impacting growth stock valuations. |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.58 | Recent market action shows risk appetite and leadership concentrated in technology, semiconductors, and select high-beta equity areas. Over a one-week window, trend persistence appears more compelling than defensive or mean-reversion positioning despite elevated macro uncertainty. | A sharp reversal in crowded semiconductor and AI-related momentum trades could cause large underperformance versus the S&P 500.; Hot or poorly received Personal Income and Outlays data on the exit date could lift yields and pressure high-growth equities before the close.; South Korea and Taiwan exposures add currency, geopolitical, and export-cycle risks that may not affect broad U.S. equities as much.; A rotation from high-beta growth into value, defensives, or the equal-weight market would hurt the concentrated continuation positioning. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.6 | Ride the semiconductor and AI-tech momentum leadership into PCE print while keeping benchmark exposure. | Sharp mean-reversion in extended semis after parabolic run; Hot PCE on 6/25 lifts yields and hits growth/tech multiples; Taiwan geopolitical headline risk; Momentum factor crash if leadership rotates to defensives |
| xai-grok-4-3 | xai | portfolio | SEMICONDUCTORS | 3 | 0.55 | Allocates to recent outperformers SEMICONDUCTORS, MOMENTUM, and SOUTH_KOREA based on 7d returns to maximize expected close-to-close performance. | Holiday-reduced trading volume may mute price moves; Mean reversion after sharp recent gains in semis and Korea; No major catalysts scheduled before June 25 exit |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 140.5868983468 | 151.59 | 0.07826548407133593 | 1 |
| REGIONAL_BANKS | Regional Banks | 71.3072214239 | 74.77 | 0.048561401032790386 | 2 |
| HEALTHCARE | Healthcare Sector | 148.7494792532 | 155.63 | 0.0462557635922074 | 3 |
| UTILITIES | Utilities Sector | 44.4771296327 | 45.85 | 0.03086688324173359 | 4 |
| LOW_VOL | US Low Volatility Equities | 72.9528398955 | 74.9 | 0.02669066903069406 | 5 |
| REAL_ESTATE | Real Estate Sector | 43.4834973186 | 44.59 | 0.0254464969386603 | 6 |
| INDUSTRIALS | Industrials Sector | 180.4691569319 | 184.12 | 0.020229734156056667 | 7 |
| SMALL_VALUE | US Small-Cap Value | 216.87 | 220.11 | 0.014939825702033449 | 8 |
| CONSUMER_STAPLES | Consumer Staples Sector | 82.7220248962 | 83.94 | 0.014723709983264 | 9 |
| BRAZIL | Brazil Equities | 33.73 | 34.18 | 0.013341239252890658 | 10 |
| ENERGY | Energy Sector | 53.3898947625 | 54.09 | 0.013113066444771171 | 11 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 209.151671347 | 211.75 | 0.012423179008161922 | 12 |
| SMALL_CAP | US Small-Cap Stocks | 295.59 | 298.91 | 0.011231773740654427 | 13 |
| DIVIDEND | US Dividend Equities | 31.6078941607 | 31.96 | 0.01113980695802863 | 14 |
| AGRICULTURE | Agriculture Commodities | 26.63 | 26.92 | 0.010889973713856582 | 15 |
| UNITED_KINGDOM | United Kingdom Equities | 45.46 | 45.88 | 0.009238891333040122 | 16 |
| LARGE_VALUE | US Large-Cap Value | 242.18 | 244.41 | 0.009208027087290294 | 17 |
| MID_CAP | US Mid-Cap Stocks | 75.78 | 76.46 | 0.00897334389020843 | 18 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 86.75 | 87.35 | 0.006916426512968199 | 19 |
| US_DOLLAR | US Dollar | 28.3 | 28.48 | 0.006360424028268641 | 20 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.48 | 94.92 | 0.004657070279424191 | 21 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.36 | 94.79 | 0.004557015684612198 | 22 |
| MATERIALS | Materials Sector | 51.6167690951 | 51.84 | 0.0043247748515355955 | 23 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.07 | 109.5 | 0.003942422297606996 | 24 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.9 | 99.25 | 0.003538928210313319 | 25 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.35 | 48.49 | 0.002895553257497463 | 26 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.33 | 107.58 | 0.0023292648840025354 | 27 |
| MOMENTUM | US Momentum Equities | 338.52 | 339.3 | 0.0023041474654379446 | 28 |
| FINANCIALS | Financials Sector | 53.384017836 | 53.45 | 0.0012359909702321925 | 29 |
| TIPS | Treasury Inflation-Protected Securities | 109.39 | 109.5 | 0.0010055763780967286 | 30 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.57 | 91.6 | 0.0003276182155727003 | 31 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 32 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 80.01 | 79.88 | -0.0016247969003875262 | 33 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.73 | 96.56 | -0.0017574692442882123 | 34 |
| YEN | Japanese Yen | 56.85 | 56.69 | -0.0028144239226034484 | 35 |
| INDIA | India Equities | 49.58 | 49.43 | -0.003025413473174643 | 36 |
| CANADA | Canada Equities | 57.87 | 57.62 | -0.004320027648176961 | 37 |
| EUROPE | Europe Equities | 88.27 | 87.83 | -0.004984706015633833 | 38 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 238.99 | 237.38 | -0.006736683543244526 | 39 |
| EURO | Euro | 105.77 | 104.94 | -0.007847215656613393 | 40 |
| CYBERSECURITY | Cybersecurity | 84.4672043338 | 83.66 | -0.009556422994776326 | 41 |
| DEVELOPED_EX_US | Developed Markets ex-US | 72.31 | 71.16 | -0.0159037477527314 | 42 |
| TOTAL_US_MARKET | Total US Stock Market | 369.99 | 363.98 | -0.016243682261682713 | 43 |
| SP500 | S&P 500 | 746.74 | 734.3 | -0.016659078126255555 | 44 |
| AUSTRALIA | Australia Equities | 28.56 | 27.93 | -0.022058823529411686 | 45 |
| MEXICO | Mexico Equities | 77.33 | 75.53 | -0.023276865382128475 | 46 |
| BROAD_COMMODITIES | Broad Commodities | 16.5 | 16.11 | -0.023636363636363678 | 47 |
| JAPAN | Japan Equities | 96.26 | 93.39 | -0.029815084147101656 | 48 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 116.92275687 | 113.35 | -0.030556556872605722 | 49 |
| NASDAQ100 | Nasdaq 100 | 739.8044657025 | 716.38 | -0.031663049884751215 | 50 |
| EMERGING_MARKETS | Emerging Markets | 60.77 | 58.8 | -0.0324173111732764 | 51 |
| COMMUNICATIONS | Communication Services Sector | 109.1601464074 | 105.58 | -0.0327971931627723 | 52 |
| TECHNOLOGY | Technology Sector | 191.2131931899 | 184.57 | -0.03474233696470119 | 53 |
| SEMICONDUCTORS | Semiconductors | 659.88 | 636.88 | -0.03485482208886459 | 54 |
| CHINA | China Equities | 52.77 | 50.78 | -0.03771082054197461 | 55 |
| BROAD_AI_TECH | Broad AI Technology | 66.8 | 64.18 | -0.039221556886227416 | 56 |
| LARGE_GROWTH | US Large-Cap Growth | 123.19 | 118.1 | -0.04131828882214472 | 57 |
| SOLAR | Solar Energy | 60.58 | 57.87 | -0.04473423572136015 | 58 |
| GOLD | Gold | 79.33 | 75.71 | -0.04563216941888315 | 59 |
| TAIWAN | Taiwan Equities | 109.99 | 104.91 | -0.04618601691062818 | 60 |
| COPPER | Copper | 38.86 | 36.98 | -0.04837879567678849 | 61 |
| OIL | Crude Oil | 114.87 | 109.31 | -0.04840254200400451 | 62 |
| SOFTWARE | Software | 89.09 | 84.76 | -0.04860253676057913 | 63 |
| SOUTH_AFRICA | South Africa Equities | 66.74 | 63.17 | -0.05349115972430318 | 64 |
| BITCOIN_ETF | Bitcoin ETF | 35.62 | 33.52 | -0.05895564289724853 | 65 |
| SOUTH_KOREA | South Korea Equities | 219.2 | 205.0 | -0.06478102189781021 | 66 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 133.17 | 123.84 | -0.07006082451002471 | 67 |
| METALS_MINING | Metals and Mining | 116.9386392465 | 108.74 | -0.07011060928473556 | 68 |
| ETHEREUM_ETF | Ethereum ETF | 12.88 | 11.74 | -0.08850931677018636 | 69 |
| SILVER | Silver | 59.51 | 52.36 | -0.12014787430683915 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 35.0 | -0.03485482208886459 | -0.012199187731102606 | Strong momentum, AI capex cycle, leading sector with 8.3% weekly gain showing trend persistence. |
| anthropic-claude-opus-4-7 | NASDAQ100 | 25.0 | -0.031663049884751215 | -0.007915762471187804 | Tech-led rally with Nasdaq +2.4% WTD, dovish-leaning Fed dots, growth tailwind. |
| anthropic-claude-opus-4-7 | TAIWAN | 15.0 | -0.04618601691062818 | -0.006927902536594227 | Semi supply chain beneficiary riding chip strength, strong momentum. |
| anthropic-claude-opus-4-7 | MOMENTUM | 15.0 | 0.0023041474654379446 | 0.0003456221198156917 | Factor showing clear trend persistence with low drawdown risk over 1w. |
| anthropic-claude-opus-4-7 | SP500 | 10.0 | -0.016659078126255555 | -0.0016659078126255557 | Benchmark anchor to limit tracking error given holiday-shortened week. |
| anthropic-claude-opus-4-8 | SP500 | 40.0 | -0.016659078126255555 | -0.006663631250502223 | Broad large-cap core with strong momentum into the window; balanced risk-on exposure. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 25.0 | -0.03485482208886459 | -0.008713705522216147 | Strongest tech momentum (+8.3% 7d) on durable AI demand; leadership likely to continue near-term. |
| anthropic-claude-opus-4-8 | NASDAQ100 | 20.0 | -0.031663049884751215 | -0.006332609976950243 | Mega-cap growth leadership with Nasdaq up 1.9% on entry day; continuation tilt. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 15.0 | 0.0003276182155727003 | 4.9142732335905044e-05 | Cash-like ballast given sticky inflation (CPI 4.2%, hawkish dots) and short holiday-shortened week. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 30.0 | -0.03485482208886459 | -0.010456446626659377 | Strong recent momentum and structural AI tailwinds support continued outperformance over a short horizon. |
| google-gemini-3-1-pro | NASDAQ100 | 30.0 | -0.031663049884751215 | -0.009498914965425364 | Provides broad exposure to large-cap tech and growth, which are currently leading the market. |
| google-gemini-3-1-pro | SP500 | 40.0 | -0.016659078126255555 | -0.006663631250502223 | Core benchmark holding to manage active risk while maintaining exposure to the broader US equity market. |
| openai-gpt-5-5 | SEMICONDUCTORS | 35.0 | -0.03485482208886459 | -0.012199187731102606 | Strongest U.S. thematic momentum with large 7-day, 30-day, and longer-term gains, aligned with current risk-on leadership in technology and AI-linked equities. |
| openai-gpt-5-5 | SOUTH_KOREA | 25.0 | -0.06478102189781021 | -0.016195255474452552 | Exceptional recent and longer-term momentum, with sensitivity to global semiconductor and export strength that could continue over a short risk-on window. |
| openai-gpt-5-5 | TAIWAN | 15.0 | -0.04618601691062818 | -0.006927902536594227 | High semiconductor supply-chain exposure and strong trailing momentum provide a focused continuation opportunity over the one-week horizon. |
| openai-gpt-5-5 | MOMENTUM | 15.0 | 0.0023041474654379446 | 0.0003456221198156917 | Broad U.S. momentum exposure diversifies the continuation thesis beyond a single sector while retaining strong recent trend characteristics. |
| openai-gpt-5-5 | BIOTECH | 10.0 | 0.07826548407133593 | 0.007826548407133593 | Recent strength and high beta to improving risk appetite offer additional upside potential with less direct overlap to mega-cap technology. |
| xai-grok-4-3 | SEMICONDUCTORS | 40.0 | -0.03485482208886459 | -0.013941928835545837 | Strongest recent 7d return at +8.27% with semiconductor supply chain momentum likely to extend over the abbreviated trading week. |
| xai-grok-4-3 | MOMENTUM | 30.0 | 0.0023041474654379446 | 0.0006912442396313834 | Recent +6.23% 7d performance indicates trend continuation into the short scoring window. |
| xai-grok-4-3 | SOUTH_KOREA | 30.0 | -0.06478102189781021 | -0.01943430656934306 | Leading 7d return of +10.18% driven by semiconductor exposure, positioned for continuation before exit close. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | SP500 | 4 | 0.55 | -0.016659078126255555 | -0.021660804017332707 | -0.005001725891077152 | 0.09992628808866864 |  | False | False |
| google-gemini-3-1-pro | SP500 | 3 | 0.65 | -0.016659078126255555 | -0.026618992842586963 | -0.009959914716331408 | 0.1048844769139229 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.58 | -0.03485482208886459 | -0.027150175215200106 | -0.010491097088944551 | 0.10541565928653604 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.6 | -0.03485482208886459 | -0.0283631384316945 | -0.011704060305438944 | 0.10662862250303043 |  | False | False |
| xai-grok-4-3 | SEMICONDUCTORS | 3 | 0.55 | -0.03485482208886459 | -0.03268499116525751 | -0.016025913039001957 | 0.11095047523659345 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | dda2ee5ee69295c60efc89f291aad2182afd5b498ee8c5f305989ec7f746d61a |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 68a143201b250285b114b2001bcdfdd6269a744b9b3595e63fe6b846177dc887 |
| manifest.yaml | e38ef9831d19140bcc968ab48c4dbe95f213b7cd3b7b5c60f4ad999d82c23bd4 |
| market_data/universe_trailing_returns.csv | fb88877ba6d0c6634f00dafe37ccd2085bdd8328a9eedc00a0f168d773b6b6df |
| market_data/universe_trailing_returns.md | a86a3bf5eaa7f64e8c8b534f433a1c510755ac647c99d5f88509a3b3e1222f26 |
| market_data/universe_trailing_returns.json | dbff0e67a33a2a3027578f257447beaaa61e4a01a4186a91dcad8434e9e853d5 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 71603cb8967d7bb6a1b16b28da99e3416b68a7669a41048290d29e00fcdd3a65 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 225b5b2a98fde058aef40e21ac16e7a994e4280be103e567b6fdf204f6c61aa7 | yes |
| Final briefing | research/final_briefing.md | model-facing | dda2ee5ee69295c60efc89f291aad2182afd5b498ee8c5f305989ec7f746d61a | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
