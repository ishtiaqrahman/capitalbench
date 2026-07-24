# CapitalBench Report: CB-2026-06-23-1M / official-20260623-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260623-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-23-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-06-23
- Decision deadline: 2026-06-24T02:30:00Z
- Horizon: one month
- Entry date: 2026-06-23
- Exit date: 2026-07-23
- Entry rule: Use adjusted close prices on Tuesday, June 23, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Thursday, July 23, 2026 as the one-month exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | SP500 | 5 | 0.65 | A balanced approach combining broad market equity with defensive sectors and safe-haven assets to navigate potential short-term volatility. | A sudden acceleration in economic growth could cause defensive assets to underperform.; Unexpected shifts in Federal Reserve policy could negatively impact both equities and fixed income.; A sharp decline in the US dollar could reduce the effectiveness of the currency hedge. |
| xai-grok-4-3 | xai | portfolio | SMALL_CAP | 5 | 0.65 | Recent data show tech/semiconductor pullback with positive breadth elsewhere; selected factors exhibit strongest trailing one-month performance and domestic sensitivity ahead of July data releases and holiday. | Further escalation in CPI or energy prices delaying rate relief; Disappointing Q2 GDP or retail sales data on July 30; Renewed semiconductor supply-chain or Korea-related volatility spilling into small caps |
| openai-gpt-5-5 | openai | portfolio | BIOTECH | 5 | 0.58 | Recent price action shows the S&P 500 pressured by large technology weights while broader participation and several high-beta segments remain firm. A concentrated allocation to momentum, biotech, regional banks, small caps, and Taiwan offers better upside potential than benchmark-like exposure over the one-month scoring window. | A sharp rebound in mega-cap technology could make the S&P 500 outperform this broader high-beta allocation.; Biotech momentum could reverse abruptly due to trial, regulatory, financing, or risk-appetite shocks.; Regional banks could underperform if credit-quality, deposit, or commercial real estate concerns re-emerge.; Taiwan and semiconductor-linked exposure could be hurt by further chip-sector weakness or geopolitical stress.; Hot inflation or rising yields could pressure small caps, banks, and long-duration growth-oriented holdings. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SMALL_CAP | 5 | 0.55 | Rotate away from mega-cap tech weakness into broadening leadership (small caps, momentum, biotech, industrials), with long Treasuries as hedge. | Mega-cap tech rebound would leave SPY benchmark hard to beat; Sticky inflation (CPI +4.2% YoY) could push yields higher, hurting TLT and small caps; Biotech momentum reversal after sharp run; Credit/risk-off event hitting small caps and high-beta biotech disproportionately |
| anthropic-claude-opus-4-8 | anthropic | portfolio | MOMENTUM | 5 | 0.55 | Capture rotation away from concentrated mega-cap tech weakness into breadth leaders (small caps, industrials, momentum, biotech) plus quality semiconductor exposure via Taiwan. | Continued mega-cap tech selloff could spill into broad risk-off, hurting small caps and cyclicals despite breadth; Biotech and Taiwan are high-volatility positions vulnerable to reversal of recent sharp gains; Higher long-end yields (10y 4.51%, sticky 4.2% CPI) could pressure rate-sensitive small caps and growth-momentum names; Semiconductor weakness (Micron -13%, Samsung) could broaden into Taiwan chip supply chain |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 111.26 | 139.49 | 0.2537300017975912 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 12.52 | 14.11 | 0.1269968051118211 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 16.18 | 18.059999465942383 | 0.1161927976478605 | 3 |
| ENERGY | Energy Sector | 54.46 | 59.380001068115234 | 0.09034155468445149 | 4 |
| AGRICULTURE | Agriculture Commodities | 26.6 | 28.24 | 0.06165413533834574 | 5 |
| HEALTHCARE | Healthcare Sector | 152.18 | 161.44000244140625 | 0.06084901065452919 | 6 |
| BRAZIL | Brazil Equities | 34.15 | 36.17 | 0.059150805270864026 | 7 |
| CYBERSECURITY | Cybersecurity | 84.1374884901 | 87.72000122070312 | 0.042579268705229545 | 8 |
| BITCOIN_ETF | Bitcoin ETF | 35.31 | 36.65 | 0.03794958935145831 | 9 |
| FINANCIALS | Financials Sector | 53.88 | 55.83000183105469 | 0.03619157073226953 | 10 |
| BIOTECH | Biotechnology | 147.03 | 152.23 | 0.03536693191865603 | 11 |
| DIVIDEND | US Dividend Equities | 31.7671248729 | 32.79999923706055 | 0.032513939120807134 | 12 |
| LOW_VOL | US Low Volatility Equities | 74.0723980357 | 76.36000061035156 | 0.030883333540099756 | 13 |
| CHINA | China Equities | 51.81 | 53.349998474121094 | 0.029723962055994813 | 14 |
| REGIONAL_BANKS | Regional Banks | 73.12 | 75.15 | 0.02776258205689275 | 15 |
| UTILITIES | Utilities Sector | 45.07 | 46.189998626708984 | 0.024850202500753982 | 16 |
| UNITED_KINGDOM | United Kingdom Equities | 45.57 | 46.7 | 0.024797015580425796 | 17 |
| COPPER | Copper | 37.32 | 38.24 | 0.024651661307609984 | 18 |
| LARGE_VALUE | US Large-Cap Value | 240.95 | 246.18 | 0.02170574808051473 | 19 |
| INDUSTRIALS | Industrials Sector | 178.15 | 181.94000244140625 | 0.02127422083304098 | 20 |
| CANADA | Canada Equities | 57.67 | 58.82 | 0.019941043870296493 | 21 |
| AUSTRALIA | Australia Equities | 28.02 | 28.49 | 0.016773733047823036 | 22 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 208.89 | 211.9199981689453 | 0.0145052332277531 | 23 |
| SMALL_VALUE | US Small-Cap Value | 217.55 | 220.5800018310547 | 0.013927841098849258 | 24 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 235.93 | 238.23 | 0.009748654261857226 | 25 |
| EUROPE | Europe Equities | 87.16 | 87.83000183105469 | 0.0076870333989753625 | 26 |
| REAL_ESTATE | Real Estate Sector | 44.64 | 44.95000076293945 | 0.006944461535381974 | 27 |
| SP500 | S&P 500 | 733.58 | 738.18 | 0.006270618064832645 | 28 |
| TOTAL_US_MARKET | Total US Stock Market | 362.655046458 | 364.69 | 0.005611264924823445 | 29 |
| US_DOLLAR | US Dollar | 28.45 | 28.56 | 0.0038664323374340004 | 30 |
| MEXICO | Mexico Equities | 74.73 | 75.0 | 0.0036130068245683322 | 31 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.3126338109 | 91.58 | 0.002928030634333556 | 32 |
| MID_CAP | US Mid-Cap Stocks | 75.3 | 75.45 | 0.0019920318725099584 | 33 |
| EURO | Euro | 104.9598933918 | 105.03 | 0.000667937113258299 | 34 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 35 |
| SOFTWARE | Software | 87.32 | 87.0999984741211 | -0.0025194860957271636 | 36 |
| TIPS | Treasury Inflation-Protected Securities | 107.845154352 | 107.48999786376953 | -0.003293207658373376 | 37 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.5016185275 | 79.2300033569336 | -0.003416473470567838 | 38 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.17 | 69.77999877929688 | -0.005557948136000079 | 39 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.72 | 83.20999908447266 | -0.006091745288190897 | 40 |
| LARGE_GROWTH | US Large-Cap Growth | 119.81 | 118.59 | -0.010182789416576243 | 41 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.8096698703 | 92.8499984741211 | -0.010229983726685488 | 42 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.3797158227 | 97.33999633789062 | -0.010568433503946761 | 43 |
| SMALL_CAP | US Small-Cap Stocks | 295.32 | 292.0899963378906 | -0.010937300765641922 | 44 |
| MATERIALS | Materials Sector | 50.87 | 50.290000915527344 | -0.011401593954642353 | 45 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.2688027581 | 47.71 | -0.011576892861843935 | 46 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.0027618425 | 92.88 | -0.011943923992160599 | 47 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.8609262319 | 94.53 | -0.013883928355546193 | 48 |
| YEN | Japanese Yen | 56.8 | 56.01 | -0.013908450704225306 | 49 |
| GOLD | Gold | 77.33 | 76.1500015258789 | -0.015259258685129895 | 50 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.9724062703 | 105.26 | -0.016007925127654477 | 51 |
| COMMUNICATIONS | Communication Services Sector | 107.27 | 105.37999725341797 | -0.017619117615195523 | 52 |
| JAPAN | Japan Equities | 92.75 | 91.0999984741211 | -0.017789773863923553 | 53 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.5282289901 | 106.26000213623047 | -0.02089987899900625 | 54 |
| EMERGING_MARKETS | Emerging Markets | 59.36 | 58.099998474121094 | -0.021226440799846813 | 55 |
| INDIA | India Equities | 49.07 | 47.630001068115234 | -0.029345810717032128 | 56 |
| NASDAQ100 | Nasdaq 100 | 713.65 | 691.96 | -0.03039304981433466 | 57 |
| TECHNOLOGY | Technology Sector | 184.19 | 178.4499969482422 | -0.03116348906975308 | 58 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.8806289007 | 83.16999816894531 | -0.03156277226251891 | 59 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 113.76 | 108.76000213623047 | -0.043952161249732224 | 60 |
| MOMENTUM | US Momentum Equities | 329.76 | 313.9800109863281 | -0.04785295067222184 | 61 |
| TAIWAN | Taiwan Equities | 105.24 | 99.84 | -0.05131128848346633 | 62 |
| SOUTH_AFRICA | South Africa Equities | 63.93 | 60.43 | -0.05474737994681678 | 63 |
| BROAD_AI_TECH | Broad AI Technology | 63.3495541265 | 59.33000183105469 | -0.06345036442433116 | 64 |
| SILVER | Silver | 55.73 | 52.06 | -0.06585322088641654 | 65 |
| SEMICONDUCTORS | Semiconductors | 622.05 | 580.1699829101562 | -0.06732580514402975 | 66 |
| METALS_MINING | Metals and Mining | 110.9 | 103.16999816894531 | -0.06970245113665186 | 67 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 126.36 | 116.8499984741211 | -0.07526117067014015 | 68 |
| SOUTH_KOREA | South Korea Equities | 192.2 | 173.86 | -0.0954214360041622 | 69 |
| SOLAR | Solar Energy | 58.56 | 52.849998474121094 | -0.09750685665776826 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SMALL_CAP | 25.0 | -0.010937300765641922 | -0.0027343251914104805 | Small caps showing relative strength amid tech selloff, positive momentum with +3.82% 30d. |
| anthropic-claude-opus-4-7 | MOMENTUM | 20.0 | -0.04785295067222184 | -0.00957059013444437 | Strong momentum factor (+8.73% 30d) likely to continue as leadership broadens. |
| anthropic-claude-opus-4-7 | BIOTECH | 20.0 | 0.03536693191865603 | 0.007073386383731207 | XBI breaking out +11.78% 30d, +8.74% 7d signals sector rotation and risk appetite return. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 15.0 | 0.02127422083304098 | 0.003191133124956147 | Solid breadth participation, defensive cyclical with steady gains. |
| anthropic-claude-opus-4-7 | LONG_TREASURY | 20.0 | -0.03156277226251891 | -0.0063125544525037824 | Hedge for equity drawdown; TLT positive 30d as rates likely peak with Fed at 3.50-3.75%. |
| anthropic-claude-opus-4-8 | MOMENTUM | 25.0 | -0.04785295067222184 | -0.01196323766805546 | Strong relative momentum (+8.7% 30d) and positive 7d return amid mega-cap tech weakness; broad factor exposure with persistence. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 20.0 | 0.02127422083304098 | 0.004254844166608196 | Solid breadth-driven cyclical with +4% 30d, defense/aerospace tailwinds and domestic resilience. |
| anthropic-claude-opus-4-8 | SMALL_CAP | 20.0 | -0.010937300765641922 | -0.0021874601531283846 | Best 7d/30d breadth participation (+1.1%/+3.8%); benefits from broadening rally away from concentrated mega-cap tech. |
| anthropic-claude-opus-4-8 | BIOTECH | 15.0 | 0.03536693191865603 | 0.005305039787798405 | Sharp positive momentum (+8.7% 7d, +11.8% 30d) suggesting M&A/data catalysts and idiosyncratic strength uncorrelated to tech selloff. |
| anthropic-claude-opus-4-8 | TAIWAN | 20.0 | -0.05131128848346633 | -0.010262257696693268 | Semiconductor supply chain strength with positive 7d (+1.4%) and strong 30d (+8.7%) despite Korea/Micron weakness; quality chip exposure. |
| google-gemini-3-1-pro | SP500 | 40.0 | 0.006270618064832645 | 0.002508247225933058 | Core broad market exposure to capture potential upside while maintaining diversification. |
| google-gemini-3-1-pro | SHORT_TREASURY | 20.0 | 0.002928030634333556 | 0.0005856061268667113 | Provides a cash-like buffer with yield to mitigate downside risk in a volatile environment. |
| google-gemini-3-1-pro | HEALTHCARE | 20.0 | 0.06084901065452919 | 0.012169802130905839 | Defensive sector exposure that can perform well during periods of economic uncertainty. |
| google-gemini-3-1-pro | GOLD | 10.0 | -0.015259258685129895 | -0.0015259258685129896 | Safe-haven asset to hedge against inflation and geopolitical risks. |
| google-gemini-3-1-pro | US_DOLLAR | 10.0 | 0.0038664323374340004 | 0.00038664323374340006 | Hedge against potential currency fluctuations and global market stress. |
| openai-gpt-5-5 | BIOTECH | 30.0 | 0.03536693191865603 | 0.01061007957559681 | Strongest recent 7-day and 30-day mechanical momentum in the universe, with potential for continued risk-on flows and idiosyncratic catalysts over the one-month window. |
| openai-gpt-5-5 | MOMENTUM | 25.0 | -0.04785295067222184 | -0.01196323766805546 | Broad exposure to stocks with persistent relative strength, which has outperformed over 30 days, 6 months, and 1 year and may continue if trend-following flows persist. |
| openai-gpt-5-5 | REGIONAL_BANKS | 20.0 | 0.02776258205689275 | 0.00555251641137855 | Recent positive momentum, strong domestic retail data, and higher long-end yields can support bank earnings sentiment if credit fears stay contained. |
| openai-gpt-5-5 | SMALL_CAP | 15.0 | -0.010937300765641922 | -0.0016405951148462882 | Small caps have shown relative strength versus the S&P 500, supported by domestic growth sensitivity and improving market breadth beyond mega-cap technology. |
| openai-gpt-5-5 | TAIWAN | 10.0 | -0.05131128848346633 | -0.005131128848346634 | Maintains selective semiconductor-linked international exposure with strong trailing momentum while limiting concentration after recent chip-sector volatility. |
| xai-grok-4-3 | SMALL_CAP | 30.0 | -0.010937300765641922 | -0.0032811902296925764 | Positive 30d return of 3.82% and breadth favoring non-mega caps after tech-led decline. |
| xai-grok-4-3 | BIOTECH | 25.0 | 0.03536693191865603 | 0.008841732979664008 | Strong recent momentum with 11.78% 30d return amid favorable risk appetite signals. |
| xai-grok-4-3 | MOMENTUM | 20.0 | -0.04785295067222184 | -0.00957059013444437 | Leading 30d return of 8.73% indicating persistence in recent winners over one-month window. |
| xai-grok-4-3 | SMALL_VALUE | 15.0 | 0.013927841098849258 | 0.0020891761648273886 | 3.32% 30d return and domestic growth sensitivity in post-selloff environment. |
| xai-grok-4-3 | REGIONAL_BANKS | 10.0 | 0.02776258205689275 | 0.002776258205689275 | 6.02% 30d return with potential yield-curve and credit improvement tailwinds. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | SP500 | 5 | 0.65 | 0.006270618064832645 | 0.014124372848936018 | 0.007853754784103373 | 0.23960562894865517 |  | True | True |
| xai-grok-4-3 | SMALL_CAP | 5 | 0.65 | -0.010937300765641922 | 0.0008553869860437255 | -0.005415231078788919 | 0.2528746148115475 |  | False | True |
| openai-gpt-5-5 | BIOTECH | 5 | 0.58 | 0.03536693191865603 | -0.0025723656442730226 | -0.008842983709105667 | 0.25630236744186424 |  | False | False |
| anthropic-claude-opus-4-7 | SMALL_CAP | 5 | 0.55 | -0.010937300765641922 | -0.008352950269671278 | -0.014623568334503923 | 0.26208295206726245 |  | False | False |
| anthropic-claude-opus-4-8 | MOMENTUM | 5 | 0.55 | -0.04785295067222184 | -0.014853071563470512 | -0.021123689628303157 | 0.2685830733610617 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 2218976e7d767f6963091d4a175346e7c2dea00a579bff2e03372b14806c8827 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 0e5a222ebba001788946308d0e0b4c71b9e1bdc4f2882aad00ed1514ecaa5c5f |
| manifest.yaml | 6f290901006ce5354f948ab2681ca2ecf171b0a212abb566a42fd2928a39e998 |
| market_data/universe_trailing_returns.csv | 48ac9b3cff9bf0458bdbff994bc3d106780f9a050279bc1a57b5549e16624493 |
| market_data/universe_trailing_returns.md | 084f6c13c8d304543ebbfba78c4684ef0d221555120a2655044d984436323ce4 |
| market_data/universe_trailing_returns.json | a4ccb1046396a7bd296806faf056e992b2dd8486a8eed5b637704928b1183421 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 4a7bfbda9cd8d27396df783c7c3939d08fe2489f225921ff7cc13bbd82ba2b12 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | e9947e280d4eea4a5a90adc9b1211dbb963be8ee9a78953e80e9410928e2a6ea | yes |
| Final briefing | research/final_briefing.md | model-facing | 2218976e7d767f6963091d4a175346e7c2dea00a579bff2e03372b14806c8827 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
