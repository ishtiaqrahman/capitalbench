# CapitalBench Report: CB-2026-06-30-1M / official-20260630-no-fable-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260630-no-fable-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-30-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-06-30
- Decision deadline: 2026-07-01T07:30:00Z
- Horizon: one month
- Entry date: 2026-06-30
- Exit date: 2026-07-30
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | INDUSTRIALS | 5 | 0.55 | Overweight sectors with confirmed breadth and near-term earnings/macro catalysts while limiting exposure to overheated semis and volatile commodities/crypto. | Regional banks and financials sensitive to disappointing Q2 earnings or credit deterioration before exit close; Sticky core PCE (3.4% y/y) or hawkish July 29 FOMC minutes/decision could pressure cyclicals; Sharp semiconductor rally could cause this portfolio to underperform a tech-heavy benchmark; Weak July jobs report (July 2) could dent cyclical industrials and small/mid-cap sentiment |
| xai-grok-4-3 | xai | portfolio | SMALL_CAP | 5 | 0.65 | Small-cap and factor exposures positioned for domestic growth and earnings momentum before July 30 exit close. | July 2 employment report could trigger volatility in small caps and cyclicals; FOMC minutes on July 8 may shift rate expectations affecting growth sectors; Q2 GDP release on July 30 coincides with exit and could cause reversal in recent leaders |
| anthropic-claude-opus-4-7 | anthropic | portfolio | INDUSTRIALS | 5 | 0.55 | Balanced pro-risk US equity mix capturing rally broadening, biotech strength, and semi catalysts while including defensive healthcare ballast. | Semiconductor reversal after extreme QTD gains could drag SMH and broader tape; Hot June jobs/CPI or hawkish FOMC minutes push yields higher, hurting mid-caps and biotech; Momentum crowding in industrials/biotech unwinds on positioning shock; Oil/geopolitical shock from Iran ceasefire breakdown hits risk assets |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.65 | Overweight semiconductors and small caps for momentum and catalysts, balanced with defensive healthcare. | A disappointment in TSMC's July earnings could trigger a sharp reversal in the highly extended semiconductor sector.; Small caps are vulnerable to any re-acceleration in inflation or higher-for-longer interest rates.; Weakening consumer data, such as the rise in 'jobs hard to get', could negatively impact broader equity market sentiment. |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.38 | I favor a pro-risk, leadership-continuation portfolio over the S&P 500 for the July window, with semiconductors as the central overweight due to scheduled industry-relevant catalysts. The mix balances AI-chip exposure with biotech, factor momentum, and industrial cyclicality. | A semiconductor momentum reversal or disappointing TSMC sales/results could sharply hurt the largest allocation.; Hot June inflation or a hawkish July FOMC outcome could pressure high-beta growth, biotech, and momentum exposures.; Recent winners such as semiconductors, biotech, and momentum may suffer factor rotation or profit-taking after strong trailing gains.; Weak labor, PMI, or GDP data could undermine cyclical risk appetite and industrials while favoring defensive or bond exposures.; Taiwan exposure carries geopolitical and currency risks that could overwhelm company-specific semiconductor catalysts. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 11.89 | 14.51 | 0.22035323801513873 | 1 |
| OIL | Crude Oil | 106.44 | 127.48 | 0.19767004885381434 | 2 |
| ENERGY | Energy Sector | 53.11 | 58.96 | 0.11014874788175488 | 3 |
| BITCOIN_ETF | Bitcoin ETF | 33.29 | 36.7 | 0.10243316311204587 | 4 |
| BROAD_COMMODITIES | Broad Commodities | 15.88 | 17.5 | 0.10201511335012592 | 5 |
| CHINA | China Equities | 51.025 | 55.5 | 0.08770210681038715 | 6 |
| FINANCIALS | Financials Sector | 53.61 | 57.0 | 0.06323447118074976 | 7 |
| AUSTRALIA | Australia Equities | 28.16 | 29.82 | 0.058948863636363535 | 8 |
| BRAZIL | Brazil Equities | 34.5 | 36.53 | 0.058840579710145 | 9 |
| UNITED_KINGDOM | United Kingdom Equities | 46.14 | 48.68 | 0.05504984828781967 | 10 |
| DIVIDEND | US Dividend Equities | 31.71 | 33.41 | 0.053610848312835024 | 11 |
| COPPER | Copper | 37.73 | 39.34 | 0.04267161410018572 | 12 |
| CANADA | Canada Equities | 57.64 | 59.79 | 0.03730048577376821 | 13 |
| LARGE_VALUE | US Large-Cap Value | 242.43 | 250.71 | 0.03415418883801502 | 14 |
| HEALTHCARE | Healthcare Sector | 158.66 | 163.52 | 0.030631539140300035 | 15 |
| AGRICULTURE | Agriculture Commodities | 26.67 | 27.48 | 0.030371203599550034 | 16 |
| SOFTWARE | Software | 90.6 | 93.31 | 0.029911699779249457 | 17 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.07 | 85.47 | 0.02889129649693034 | 18 |
| REAL_ESTATE | Real Estate Sector | 44.03 | 45.3 | 0.02884397002044059 | 19 |
| EUROPE | Europe Equities | 88.54 | 90.99 | 0.027671109103230007 | 20 |
| MEXICO | Mexico Equities | 75.27 | 77.11 | 0.024445330144811983 | 21 |
| GOLD | Gold | 75.51 | 77.3 | 0.02370546947424179 | 22 |
| LOW_VOL | US Low Volatility Equities | 74.7611186211 | 76.38 | 0.0216540550590838 | 23 |
| YEN | Japanese Yen | 56.44 | 57.58 | 0.020198440822112085 | 24 |
| MATERIALS | Materials Sector | 50.83 | 51.64 | 0.015935471178438076 | 25 |
| SOUTH_AFRICA | South Africa Equities | 63.19 | 64.11 | 0.014559265706599156 | 26 |
| REGIONAL_BANKS | Regional Banks | 74.85 | 75.9 | 0.014028056112224574 | 27 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.77 | 215.38 | 0.012266766931428252 | 28 |
| EURO | Euro | 105.3696197204 | 106.47 | 0.010443050686904654 | 29 |
| INDIA | India Equities | 49.39 | 49.7 | 0.006276574205304808 | 30 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.3724586419 | 91.65 | 0.003037472803350205 | 31 |
| SMALL_VALUE | US Small-Cap Value | 221.2 | 221.79 | 0.002667269439421416 | 32 |
| CYBERSECURITY | Cybersecurity | 89.85 | 90.02 | 0.0018920422927100056 | 33 |
| SILVER | Silver | 53.47 | 53.5 | 0.0005610622779128605 | 34 |
| JAPAN | Japan Equities | 93.27 | 93.29 | 0.00021443122118580682 | 35 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 36 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.6011573011 | 79.47 | -0.0016476808321251868 | 37 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.25 | 71.09 | -0.0022456140350877174 | 38 |
| COMMUNICATIONS | Communication Services Sector | 107.13 | 106.58 | -0.005133949407262195 | 39 |
| TIPS | Treasury Inflation-Protected Securities | 108.3700205761 | 107.74 | -0.005813605762468144 | 40 |
| SP500 | S&P 500 | 746.77 | 741.69 | -0.006802629993170495 | 41 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.3186878374 | 47.88 | -0.009079051129787463 | 42 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.1821183947 | 93.29 | -0.00947226936392842 | 43 |
| US_DOLLAR | US Dollar | 28.41 | 28.14 | -0.009503695881731722 | 44 |
| TOTAL_US_MARKET | Total US Stock Market | 370.04 | 366.27 | -0.010188087774294807 | 45 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.6488124013 | 97.62 | -0.010429039906885373 | 46 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.2581861414 | 93.21 | -0.011120372503536036 | 47 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.0401799897 | 94.79 | -0.013017259961758398 | 48 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.3314410107 | 105.76 | -0.01464101288403774 | 49 |
| UTILITIES | Utilities Sector | 45.34 | 44.66 | -0.014997794441994006 | 50 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 242.42 | 238.13 | -0.017696559689794555 | 51 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.6876681292 | 106.41 | -0.02095608608046018 | 52 |
| MID_CAP | US Mid-Cap Stocks | 77.11 | 75.35 | -0.022824536376604865 | 53 |
| EMERGING_MARKETS | Emerging Markets | 59.69 | 58.19 | -0.025129837493717555 | 54 |
| SMALL_CAP | US Small-Cap Stocks | 300.45 | 292.59 | -0.026160758861707434 | 55 |
| INDUSTRIALS | Industrials Sector | 185.23 | 178.39 | -0.036927063650596614 | 56 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 86.0998138005 | 82.8 | -0.03832544641903557 | 57 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.28 | 112.39 | -0.041695088676671266 | 58 |
| BIOTECH | Biotechnology | 158.25 | 151.46 | -0.042906793048973046 | 59 |
| METALS_MINING | Metals and Mining | 106.93 | 101.86 | -0.04741419620312359 | 60 |
| LARGE_GROWTH | US Large-Cap Growth | 124.17 | 117.43 | -0.05428042200209382 | 61 |
| NASDAQ100 | Nasdaq 100 | 736.4 | 683.55 | -0.07176806083650189 | 62 |
| TECHNOLOGY | Technology Sector | 190.52 | 175.73 | -0.07762964518160831 | 63 |
| BROAD_AI_TECH | Broad AI Technology | 65.61 | 58.69 | -0.10547172687090389 | 64 |
| MOMENTUM | US Momentum Equities | 342.83 | 298.77 | -0.12851850771519413 | 65 |
| TAIWAN | Taiwan Equities | 108.61 | 94.0 | -0.13451800018414506 | 66 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 132.22 | 113.98 | -0.13795189835123278 | 67 |
| SOLAR | Solar Energy | 59.15 | 49.84 | -0.1573964497041419 | 68 |
| SEMICONDUCTORS | Semiconductors | 655.89 | 538.9 | -0.17836832395676105 | 69 |
| SOUTH_KOREA | South Korea Equities | 201.9 | 161.21 | -0.20153541357107474 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 25.0 | -0.036927063650596614 | -0.009231765912649154 | Strong breadth leadership with 7.25% 30d return, low drawdown, supported by broadening rally and capex cycle. |
| anthropic-claude-opus-4-7 | BIOTECH | 20.0 | -0.042906793048973046 | -0.00858135860979461 | Sector momentum with 15.88% 30d gain, near 52w high, healthcare catalysts and improving risk appetite. |
| anthropic-claude-opus-4-7 | MID_CAP | 20.0 | -0.022824536376604865 | -0.0045649072753209735 | Broadening rally beyond mega-caps; mid-caps at 52w highs with solid risk-adjusted profile. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 15.0 | 0.030631539140300035 | 0.004594730871045005 | Defensive with positive momentum (+6.61% 30d), low beta, supportive if growth cools. |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 20.0 | -0.17836832395676105 | -0.035673664791352214 | TSMC July sales/earnings catalysts within window; strong trend, though high volatility warrants sized exposure. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 25.0 | -0.036927063650596614 | -0.009231765912649154 | Strong broad-based momentum with +8.3% 30d alpha and 65% up-day share; cyclical strength supported by resilient consumer income/spending data, less concentrated risk than semis. |
| anthropic-claude-opus-4-8 | FINANCIALS | 20.0 | 0.06323447118074976 | 0.012646894236149953 | Positive rate backdrop with steady yields and Q2 bank earnings (JPM, WFC July 14) as near-term catalysts; solid 30d alpha with low volatility and drawdown. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 20.0 | 0.030631539140300035 | 0.006126307828060007 | Defensive sector with strong recent breadth (+7.6% 30d alpha), low beta 0.37, and improving momentum; hedges equity drawdown risk while participating in upside. |
| anthropic-claude-opus-4-8 | EQUAL_WEIGHT_SP500 | 20.0 | 0.012266766931428252 | 0.0024533533862856507 | Broad diversified US large-cap exposure with lower mega-cap concentration; positive 30d alpha, modest volatility, near 52w high without the semis crowding risk. |
| anthropic-claude-opus-4-8 | REGIONAL_BANKS | 15.0 | 0.014028056112224574 | 0.002104208416833686 | High up-day share (80%) and strong 30d alpha; benefits from stable rate environment and bank earnings catalysts, though higher-risk cyclical tilt. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | -0.17836832395676105 | -0.07134732958270443 | Strong momentum in the semiconductor sector, supported by upcoming TSMC sales and earnings catalysts in July. |
| google-gemini-3-1-pro | SMALL_CAP | 30.0 | -0.026160758861707434 | -0.00784822765851223 | Historic first-half strength in small caps suggests potential continuation, balancing mega-cap tech exposure. |
| google-gemini-3-1-pro | HEALTHCARE | 30.0 | 0.030631539140300035 | 0.00918946174209001 | Provides defensive growth and diversification, showing recent positive momentum amidst mixed consumer data. |
| openai-gpt-5-5 | SEMICONDUCTORS | 35.0 | -0.17836832395676105 | -0.062428913384866364 | Semiconductor shares showed exceptional recent strength with independent near-term catalysts from TSMC June sales and Q2 results before the exit date; allocation accepts very high volatility and reversal risk. |
| openai-gpt-5-5 | BIOTECH | 20.0 | -0.042906793048973046 | -0.00858135860979461 | Biotech had strong recent relative performance and can benefit from risk appetite and stable-to-lower rate expectations; briefing support beyond price action is limited, so position size is moderate. |
| openai-gpt-5-5 | TAIWAN | 15.0 | -0.13451800018414506 | -0.02017770002762176 | Taiwan provides semiconductor supply-chain exposure with near-term TSMC catalysts and strong recent relative performance, while diversifying away from pure U.S. sector exposure. |
| openai-gpt-5-5 | MOMENTUM | 15.0 | -0.12851850771519413 | -0.01927777615727912 | Momentum factor exposure targets continuation in recent market leadership, supported by broad first-half equity strength but vulnerable to factor rotation after large gains. |
| openai-gpt-5-5 | INDUSTRIALS | 15.0 | -0.036927063650596614 | -0.005539059547589492 | Industrials showed broadening market leadership, positive recent relative performance, and less extreme beta than semiconductor-heavy positions, adding cyclical participation. |
| xai-grok-4-3 | SMALL_CAP | 30.0 | -0.026160758861707434 | -0.00784822765851223 | Strong first-half Russell 2000 performance and positive 30d returns amid domestic growth data. |
| xai-grok-4-3 | BIOTECH | 25.0 | -0.042906793048973046 | -0.010726698262243262 | Leading 30d return with upcoming earnings and clinical catalysts before exit. |
| xai-grok-4-3 | INDUSTRIALS | 20.0 | -0.036927063650596614 | -0.0073854127301193236 | Solid 30d gains and exposure to domestic demand ahead of July data releases. |
| xai-grok-4-3 | HEALTHCARE | 15.0 | 0.030631539140300035 | 0.004594730871045005 | Positive 30d performance and defensive characteristics through PCE and employment prints. |
| xai-grok-4-3 | MOMENTUM | 10.0 | -0.12851850771519413 | -0.012851850771519414 | Highest 30d factor return with trend persistence likely into early July. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 5 | 0.55 | -0.036927063650596614 | 0.014098997954680142 | 0.020901627947850637 | 0.2062542400604586 |  | True | True |
| xai-grok-4-3 | SMALL_CAP | 5 | 0.65 | -0.026160758861707434 | -0.03421745855134922 | -0.027414828558178728 | 0.25457069656648795 |  | False | False |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 5 | 0.55 | -0.036927063650596614 | -0.053456965718071944 | -0.04665433572490145 | 0.2738102037332107 |  | False | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.65 | -0.17836832395676105 | -0.07000609549912665 | -0.06320346550595615 | 0.29035933351426535 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.38 | -0.17836832395676105 | -0.11600480772715134 | -0.10920217773398085 | 0.33635804574229006 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 79dc6a4c9142c8fe89c2547bbfe2042c35174fcfa460a2e126bf8fec73901ceb |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 7858eef0aa73ea38b28daacc4aaa57e57b110de6456378f1697ff1cd79ca213c |
| manifest.yaml | 386e29132b93a375444b7242fa0f48c21988fb5aab8d772a51f262592ecf0aef |
| market_data/universe_trailing_returns.csv | fc2f3371dafcaf4e49ff93b69f7a41822e4becdacc75969daea9838e0e921c64 |
| market_data/universe_trailing_returns.md | 9cbf32fa070454b52319ddff31d3f8c2b6bba8eb69f128c10fd9180a6c0ae02d |
| market_data/universe_trailing_returns.json | 8e0909ff87daf3d2b4b0f7b7d6d9011d043fab10bbe4f88134871cc84a9793dc |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | f9bbe864c38dc274e367cb9eaf2781955396b5b67e366b43e6520abe31437762 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | c3abdf5eb6e643972d7e7f1238aaa5432ce8cdcd71ba986819b0b91b23776bc3 | yes |
| Final briefing | research/final_briefing.md | model-facing | 79dc6a4c9142c8fe89c2547bbfe2042c35174fcfa460a2e126bf8fec73901ceb | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
