# CapitalBench Report: CB-2026-06-16-1W / official-20260616-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260616-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-16-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-06-16
- Decision deadline: 2026-06-17T02:30:00Z
- Horizon: one week
- Entry date: 2026-06-16
- Exit date: 2026-06-23
- Entry rule: Use adjusted close prices on Tuesday, June 16, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Tuesday, June 23, 2026 as the one-week exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | NASDAQ100 | 3 | 0.55 | Allocates to Nasdaq-100, semiconductors, and momentum for expected outperformance versus broad market amid policy event and recent factor strength. | Hawkish FOMC surprise raises yields and pressures growth stocks; Hotter-than-expected retail sales data reinforces inflation concerns; Oil price rebound reverses recent commodity weakness and rotates flows |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Momentum-led equity exposure concentrated in semis and global momentum proxies with a small gold hedge for FOMC risk in a holiday-shortened week. | Hawkish FOMC surprise on June 17 hitting growth/semis; Profit-taking in extended Korea/semi trade; Oil collapse signaling demand weakness spreading to cyclicals |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Momentum-led growth/semiconductor allocation captures persistent leadership over a short holiday-shortened window. | Hawkish FOMC statement/press conference on June 17 could trigger growth and semi drawdown.; South Korea's outsized recent run is vulnerable to sharp mean reversion.; Juneteenth holiday compresses trading days, amplifying single-catalyst gap risk.; Crowded momentum/AI positioning raises risk of a factor unwind. |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.65 | Overweighting tech and semiconductor momentum ahead of the FOMC meeting, anticipating that a neutral Fed will allow the current growth trend to persist. | A hawkish surprise from the FOMC meeting could disproportionately hit high-valuation growth and tech stocks.; Extreme recent outperformance in semiconductors and South Korea leaves them vulnerable to sharp mean-reversion or profit-taking.; Concentration risk is very high, as all three positions are heavily exposed to the global technology and semiconductor cycle. |
| openai-gpt-5-5 | openai | portfolio | SOUTH_KOREA | 5 | 0.58 | I expect high-momentum, semiconductor-linked and precious-metal exposures to have the best chance of beating the S&P 500 over the June 16 to June 23 window. The allocation intentionally accepts high volatility to maximize expected relative return. | A hawkish FOMC statement or press conference could lift yields and trigger a reversal in high-beta technology, semiconductor, and momentum trades.; South Korean equities and semiconductor stocks are highly extended after very large trailing gains and could mean-revert sharply during the scoring week.; Silver could reverse if real yields or the US dollar rise after the Fed meeting, reducing precious-metals demand.; A broad risk-off move around retail sales, jobless claims, or post-FOMC positioning could make the concentrated high-volatility portfolio underperform SPY. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 135.2119870825 | 147.03 | 0.08740358878306553 | 1 |
| US_DOLLAR | US Dollar | 27.93 | 28.45 | 0.018617973505191454 | 2 |
| REGIONAL_BANKS | Regional Banks | 72.0727897521 | 73.12 | 0.014529897503648304 | 3 |
| TAIWAN | Taiwan Equities | 103.79 | 105.24 | 0.013970517390885284 | 4 |
| MOMENTUM | US Momentum Equities | 326.05 | 329.76 | 0.011378622910596548 | 5 |
| SMALL_CAP | US Small-Cap Stocks | 292.08 | 295.32 | 0.011092851273623694 | 6 |
| SEMICONDUCTORS | Semiconductors | 616.0 | 622.05 | 0.009821428571428426 | 7 |
| UTILITIES | Utilities Sector | 44.7752337187 | 45.07 | 0.00658324383412201 | 8 |
| SMALL_VALUE | US Small-Cap Value | 216.2 | 217.55 | 0.006244218316373784 | 9 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.33 | 48.38 | 0.001034554107179897 | 10 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.17 | 107.26 | 0.000839787253895663 | 11 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.52 | 91.58 | 0.000655594405594373 | 12 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 86.19 | 86.2 | 0.00011602274045707794 | 13 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 14 |
| HEALTHCARE | Healthcare Sector | 152.2740653078 | 152.18 | -0.00061773689176714 | 15 |
| REAL_ESTATE | Real Estate Sector | 44.7128529199 | 44.64 | -0.0016293507379301353 | 16 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.12 | 108.91 | -0.0019244868035190876 | 17 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 80.03 | 79.87 | -0.00199925028114456 | 18 |
| LOW_VOL | US Low Volatility Equities | 74.3601939009 | 74.21 | -0.002019815885635934 | 19 |
| AGRICULTURE | Agriculture Commodities | 26.66 | 26.6 | -0.0022505626406601476 | 20 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.97 | 98.71 | -0.0026270587046580696 | 21 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.695 | 94.34 | -0.003748877976661791 | 22 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.52 | 94.12 | -0.00423190859077438 | 23 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.67 | 96.26 | -0.0042412330609289395 | 24 |
| FINANCIALS | Financials Sector | 54.1613098634 | 53.88 | -0.0051939265152465275 | 25 |
| YEN | Japanese Yen | 57.19 | 56.8 | -0.006819374016436397 | 26 |
| INDIA | India Equities | 49.41 | 49.07 | -0.006881198138028677 | 27 |
| INDUSTRIALS | Industrials Sector | 179.4117399492 | 178.15 | -0.007032649867602103 | 28 |
| BRAZIL | Brazil Equities | 34.41 | 34.15 | -0.007555943039813995 | 29 |
| TIPS | Treasury Inflation-Protected Securities | 109.76 | 108.9 | -0.007835276967930072 | 30 |
| LARGE_VALUE | US Large-Cap Value | 242.96 | 240.95 | -0.008272966743496979 | 31 |
| MID_CAP | US Mid-Cap Stocks | 75.93 | 75.3 | -0.00829711576452008 | 32 |
| ENERGY | Energy Sector | 54.9686549015 | 54.46 | -0.009253544632144894 | 33 |
| CYBERSECURITY | Cybersecurity | 85.08 | 84.21 | -0.010225669957686923 | 34 |
| TECHNOLOGY | Technology Sector | 186.2191168947 | 184.19 | -0.01089639414328969 | 35 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 211.3531630296 | 208.89 | -0.011654252031492285 | 36 |
| EMERGING_MARKETS | Emerging Markets | 60.0897947108 | 59.36 | -0.0121450691304964 | 37 |
| JAPAN | Japan Equities | 94.12 | 92.75 | -0.014555886102847526 | 38 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 239.52 | 235.93 | -0.014988309953239853 | 39 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.9961357847 | 83.72 | -0.015014044731780807 | 40 |
| DIVIDEND | US Dividend Equities | 32.53 | 32.02 | -0.01567783584383642 | 41 |
| TOTAL_US_MARKET | Total US Stock Market | 370.37 | 363.7 | -0.018009018009017996 | 42 |
| EUROPE | Europe Equities | 88.8036506459 | 87.16 | -0.018508818431958174 | 43 |
| EURO | Euro | 107.12 | 105.03 | -0.019510828976848416 | 44 |
| SP500 | S&P 500 | 748.422195912 | 733.58 | -0.01983131445468933 | 45 |
| BROAD_AI_TECH | Broad AI Technology | 64.64 | 63.35 | -0.01995668316831678 | 46 |
| UNITED_KINGDOM | United Kingdom Equities | 46.51 | 45.57 | -0.020210707374758052 | 47 |
| NASDAQ100 | Nasdaq 100 | 729.056314085 | 713.65 | -0.021131857426316514 | 48 |
| CANADA | Canada Equities | 59.11 | 57.67 | -0.024361360175943148 | 49 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.9447055327 | 70.17 | -0.02466763217056145 | 50 |
| LARGE_GROWTH | US Large-Cap Growth | 123.35 | 119.81 | -0.028698824483177843 | 51 |
| BROAD_COMMODITIES | Broad Commodities | 16.67 | 16.18 | -0.02939412117576501 | 52 |
| MATERIALS | Materials Sector | 52.5233751533 | 50.87 | -0.031478844390222416 | 53 |
| AUSTRALIA | Australia Equities | 28.98 | 28.02 | -0.0331262939958592 | 54 |
| SOLAR | Solar Energy | 60.58 | 58.56 | -0.03334433806536807 | 55 |
| OIL | Crude Oil | 115.47 | 111.26 | -0.036459686498657606 | 56 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.2201244352 | 113.76 | -0.03772728591268515 | 57 |
| MEXICO | Mexico Equities | 77.98 | 74.73 | -0.04167735316747889 | 58 |
| COMMUNICATIONS | Communication Services Sector | 112.022545861 | 107.27 | -0.042424904955267295 | 59 |
| CHINA | China Equities | 54.13 | 51.81 | -0.042859782006281155 | 60 |
| SOFTWARE | Software | 91.37 | 87.32 | -0.0443252708766555 | 61 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 132.35 | 126.36 | -0.04525878352852286 | 62 |
| BITCOIN_ETF | Bitcoin ETF | 37.17 | 35.31 | -0.050040355125100855 | 63 |
| GOLD | Gold | 81.5 | 77.33 | -0.05116564417177916 | 64 |
| COPPER | Copper | 39.55 | 37.32 | -0.05638432364096069 | 65 |
| SOUTH_AFRICA | South Africa Equities | 68.04 | 63.93 | -0.060405643738977166 | 66 |
| SOUTH_KOREA | South Korea Equities | 205.91 | 192.2 | -0.06658248749453644 | 67 |
| METALS_MINING | Metals and Mining | 119.2470331677 | 110.9 | -0.06999782674644284 | 68 |
| ETHEREUM_ETF | Ethereum ETF | 13.54 | 12.52 | -0.07533234859675031 | 69 |
| SILVER | Silver | 63.39 | 55.73 | -0.12083924909291688 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 35.0 | 0.009821428571428426 | 0.003437499999999949 | Strong momentum, AI demand, leading sector heading into FOMC with potential dovish surprise. |
| anthropic-claude-opus-4-7 | MOMENTUM | 25.0 | 0.011378622910596548 | 0.002844655727649137 | Persistent momentum factor leadership with broad participation. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 15.0 | -0.014988309953239853 | -0.0022482464929859777 | Strong trend, geopolitical tailwinds, defensive growth into holiday-shortened week. |
| anthropic-claude-opus-4-7 | SOUTH_KOREA | 15.0 | -0.06658248749453644 | -0.009987373124180465 | Extreme momentum tied to semis cycle; continuation likely short-term. |
| anthropic-claude-opus-4-7 | GOLD | 10.0 | -0.05116564417177916 | -0.005116564417177916 | Hedge against FOMC surprise and dollar weakness; soft CPI core supports. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | 0.009821428571428426 | 0.0029464285714285274 | Strongest momentum group with 4.23% 7d and 10.72% 30d; AI-led leadership likely persists into exit close. |
| anthropic-claude-opus-4-8 | SOUTH_KOREA | 20.0 | -0.06658248749453644 | -0.013316497498907287 | Powerful semiconductor-linked momentum (11.88% 7d); export/chip tailwinds drive continued outperformance. |
| anthropic-claude-opus-4-8 | MOMENTUM | 20.0 | 0.011378622910596548 | 0.0022757245821193096 | Top US factor with 4.74% 7d; broad trend persistence with lower single-name risk than thematics. |
| anthropic-claude-opus-4-8 | NASDAQ100 | 15.0 | -0.021131857426316514 | -0.003169778613947477 | Mega-cap growth leadership intact; benefits if dovish FOMC tone supports rate-sensitive growth. |
| anthropic-claude-opus-4-8 | FINANCIALS | 15.0 | -0.0051939265152465275 | -0.0007790889772869791 | Strong 7d/30d momentum, benefits from steep curve and resilient credit conditions. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | 0.009821428571428426 | 0.003928571428571371 | Strong momentum and trend persistence in semiconductors, supported by AI demand and recent extreme outperformance. |
| google-gemini-3-1-pro | SOUTH_KOREA | 30.0 | -0.06658248749453644 | -0.01997474624836093 | High exposure to global semiconductor and electronics supply chains, showing significant recent price momentum. |
| google-gemini-3-1-pro | NASDAQ100 | 30.0 | -0.021131857426316514 | -0.006339557227894954 | Broad growth and tech exposure to capture upside if the upcoming FOMC meeting is perceived as dovish. |
| openai-gpt-5-5 | SOUTH_KOREA | 30.0 | -0.06658248749453644 | -0.01997474624836093 | Strongest short-term and medium-term momentum in the universe, with semiconductor/export leverage that could keep attracting performance-chasing flows over the one-week window. |
| openai-gpt-5-5 | SEMICONDUCTORS | 25.0 | 0.009821428571428426 | 0.0024553571428571064 | Leading AI/technology subsector with very strong 7-day, 30-day, and 6-month trend; positioned to outperform if risk appetite and AI-chip leadership persist. |
| openai-gpt-5-5 | MOMENTUM | 20.0 | 0.011378622910596548 | 0.0022757245821193096 | Broad US momentum exposure captures current winners while diversifying single-theme risk; recent performance suggests trend persistence into the shortened trading week. |
| openai-gpt-5-5 | SILVER | 15.0 | -0.12083924909291688 | -0.01812588736393753 | Strongest precious-metals momentum with sensitivity to inflation concerns and potential dollar weakness, offering differentiated upside versus equities. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 10.0 | -0.014988309953239853 | -0.0014988309953239854 | Solid recent momentum with less direct dependence on consumer data and a potential support from geopolitical and defense-spending themes. |
| xai-grok-4-3 | NASDAQ100 | 40.0 | -0.021131857426316514 | -0.008452742970526606 | Growth tilt benefits from potential policy clarity and recent momentum in tech. |
| xai-grok-4-3 | SEMICONDUCTORS | 35.0 | 0.009821428571428426 | 0.003437499999999949 | Strong recent performance and sensitivity to positive risk appetite post-FOMC. |
| xai-grok-4-3 | MOMENTUM | 25.0 | 0.011378622910596548 | 0.002844655727649137 | Factor exposure to capture short-term trend continuation into exit date. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | NASDAQ100 | 3 | 0.55 | -0.021131857426316514 | -0.00217058724287752 | 0.017660727211811812 | 0.08957417602594306 |  | True | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | 0.009821428571428426 | -0.011070028306695272 | 0.008761286147994058 | 0.09847361708976081 |  | True | False |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.55 | 0.009821428571428426 | -0.012043211936593906 | 0.007788102518095424 | 0.09944680071965945 |  | True | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.65 | 0.009821428571428426 | -0.022385732047684515 | -0.002554417592995184 | 0.10978932083075005 |  | False | False |
| openai-gpt-5-5 | SOUTH_KOREA | 5 | 0.58 | -0.06658248749453644 | -0.03486838288264603 | -0.015037068427956699 | 0.12227197166571156 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 72d6c03ef8c005ec2f76ba6634b90d88f3f3dc44950d2166e588a13e100b1fcc |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 03b5e9792d4c6bade89526a62f43cbdf51184fe03753997a0637de246e708b81 |
| manifest.yaml | 09692e1894c099fdb74a19ae474d3bb56bd470cfed728ada3e62bf62e89b1500 |
| market_data/universe_trailing_returns.csv | 16bc494a75b84d92ae46d22af32635d0fdf971c6a180a7e66af662f61ae629bb |
| market_data/universe_trailing_returns.md | 3d88959b88dfb7a5a84279b7432fe392eaab70ef4a324f4d2e8efbb113de392b |
| market_data/universe_trailing_returns.json | d5301071d940e891606b26fc563b881db024cec206cf91695331aee082cbc2da |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | f5e89f195d1c85b6e102b873449ae7d6bfc3ea49c2dd78a9fb14e658256a48e1 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 1b6868d216aa6785c406ee597853c1b6f6763c574484a288b4cdbba3c97fdd27 | yes |
| Final briefing | research/final_briefing.md | model-facing | 72d6c03ef8c005ec2f76ba6634b90d88f3f3dc44950d2166e588a13e100b1fcc | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
