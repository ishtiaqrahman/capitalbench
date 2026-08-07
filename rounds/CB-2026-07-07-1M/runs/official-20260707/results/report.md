# CapitalBench Report: CB-2026-07-07-1M / official-20260707

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260707
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-07-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-07
- Decision deadline: 2026-07-08T07:30:00Z
- Horizon: one month
- Entry date: 2026-07-07
- Exit date: 2026-08-07
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | openai | portfolio | OIL | 5 | 0.42 | Allocation is tilted toward assets with identifiable July catalysts and/or reversal potential after recent weakness, while retaining exposure to financials and biotech where recent leadership could persist. The main thesis is that geopolitical oil risk and sector earnings events can drive returns before the August 7 close. | A durable Iran cease-fire or normalization of Strait of Hormuz traffic could remove the oil risk premium and hurt both OIL and ENERGY.; The July CPI or FOMC communication could reinforce higher-for-longer rates, pressuring biotech, semiconductors, and broader risk appetite.; TSMC results or guidance could disappoint after a large prior semiconductor run, extending the recent drawdown in high-beta chip equities.; Bank earnings could reveal weaker credit quality, deposit pressure, or net-interest-margin compression, causing FINANCIALS to lag.; Biotech's recent 30-day surge may reverse sharply because the briefing provides limited fundamental catalyst support for continued near-term gains. |
| google-gemini-3-1-pro | google | portfolio | SP500 | 4 | 0.65 | Allocates to SP500 for core exposure, Energy for geopolitical catalysts, Financials for upcoming earnings, and Healthcare for defense. | Geopolitical escalation in the Middle East could disrupt energy markets and broader risk appetite.; Upcoming CPI data and FOMC meetings could signal higher-for-longer rates, negatively impacting equities.; Disappointing bank earnings could weigh on the financials sector.; Continued weakness in the technology sector could drag down broader market indices. |
| xai-grok-4-3 | xai | portfolio | LARGE_VALUE | 5 | 0.55 | Value and financials positioned for rate-cut expectations after weak employment report; healthcare provides stability; energy hedges supply shocks before August 7 close. | Hotter-than-expected June CPI on July 14 reversing rate-cut bets; Disappointing bank or Tesla earnings mid-July pressuring sectors; FOMC July 29 statement signaling persistent inflation hawkishness; Escalation in Strait of Hormuz disrupting oil flows beyond expectations |
| anthropic-claude-opus-4-7 | anthropic | portfolio | FINANCIALS | 5 | 0.55 | Rotate toward value, financials (earnings catalyst), healthcare, defense (geopolitics), and low-vol to navigate CPI/FOMC event risk while avoiding stretched tech. | Dovish CPI/FOMC surprise sparks tech-led rally, leaving defensive tilt behind; Bank earnings disappoint on NIM/credit, hurting Financials overweight; Iran de-escalation reduces defense premium; Sticky core PCE (3.4%) prompts hawkish Fed, pressuring all equities |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 5 | 0.58 | Overweight defensive/value equity leadership (financials, healthcare, value, industrials) with a T-bill buffer, avoiding stretched high-beta tech/semis showing recent sharp weakness. | Mega-cap tech rebound could lift SPY benchmark and cause value/defensive tilt to lag, generating negative alpha; Hot July 14 CPI or hawkish July 29 FOMC could pressure rate-sensitive financials and broad equities; Bank earnings (JPM/WFC July 14) disappointment could reverse recent financials strength; Healthcare and low-beta names may underperform if a strong risk-on rally develops before the exit close |
| anthropic-claude-fable-5 | anthropic | portfolio | FINANCIALS | 5 | 0.5 | Rotation portfolio favoring value, financials into earnings, healthcare/biotech strength, and energy on Iranian sanctions risk, avoiding expensive tech ahead of a hawkish-risk July FOMC. | Mega-cap tech rebounds on strong TSMC/Tesla results, causing value/defensive tilt to lag the SPY benchmark; Oil retraces if Hormuz tensions ease, hurting energy and value exposure; Biotech's 27% 30-day run reverses sharply given limited fundamental support in the briefing; Hot July CPI or hawkish FOMC on July 29 pressures rate-sensitive financials and healthcare; Bank earnings disappoint on credit costs, dragging financials and large value |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| METALS_MINING | Metals and Mining | 102.47 | 115.74 | 0.12950131745876847 | 1 |
| SOUTH_AFRICA | South Africa Equities | 63.59 | 69.65 | 0.09529800283063383 | 2 |
| CHINA | China Equities | 51.78 | 56.57 | 0.09250675936655073 | 3 |
| SOFTWARE | Software | 94.13 | 102.69 | 0.09093806437905028 | 4 |
| OIL | Crude Oil | 108.92 | 117.98 | 0.08318031582813079 | 5 |
| AUSTRALIA | Australia Equities | 28.13 | 30.41 | 0.08105225737646649 | 6 |
| ETHEREUM_ETF | Ethereum ETF | 13.51 | 14.47 | 0.07105847520355302 | 7 |
| COPPER | Copper | 37.39 | 39.9 | 0.06713024872960682 | 8 |
| CYBERSECURITY | Cybersecurity | 92.21 | 97.85 | 0.06116473267541478 | 9 |
| BROAD_COMMODITIES | Broad Commodities | 16.32 | 17.25 | 0.05698529411764697 | 10 |
| SILVER | Silver | 54.46 | 57.5 | 0.05582078589790673 | 11 |
| GOLD | Gold | 77.37 | 81.68 | 0.055706346128990614 | 12 |
| ENERGY | Energy Sector | 54.64 | 57.5 | 0.05234260614934105 | 13 |
| CANADA | Canada Equities | 58.36 | 61.3 | 0.0503769705277588 | 14 |
| TECHNOLOGY | Technology Sector | 179.18 | 187.97 | 0.049056814376604585 | 15 |
| DIVIDEND | US Dividend Equities | 32.54 | 33.9 | 0.041794714197910254 | 16 |
| JAPAN | Japan Equities | 93.07 | 96.9 | 0.04115182120984229 | 17 |
| EUROPE | Europe Equities | 89.04 | 92.6 | 0.03998203054806804 | 18 |
| LARGE_VALUE | US Large-Cap Value | 247.74 | 257.56 | 0.03963833050779031 | 19 |
| SP500 | S&P 500 | 747.71 | 773.26 | 0.03417100212649293 | 20 |
| MEXICO | Mexico Equities | 75.04 | 77.52 | 0.03304904051172697 | 21 |
| TOTAL_US_MARKET | Total US Stock Market | 369.61 | 381.78 | 0.03292659830632272 | 22 |
| UNITED_KINGDOM | United Kingdom Equities | 47.13 | 48.64 | 0.0320390409505622 | 23 |
| MID_CAP | US Mid-Cap Stocks | 75.47 | 77.79 | 0.03074069166556259 | 24 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.78 | 72.89 | 0.029810680983328508 | 25 |
| YEN | Japanese Yen | 56.63 | 58.24 | 0.028430160692212603 | 26 |
| FINANCIALS | Financials Sector | 56.05 | 57.6 | 0.027653880463871516 | 27 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 124.41 | 127.85 | 0.027650510409131135 | 28 |
| EMERGING_MARKETS | Emerging Markets | 58.88 | 60.47 | 0.02700407608695654 | 29 |
| LARGE_GROWTH | US Large-Cap Growth | 121.35 | 124.6 | 0.02678203543469304 | 30 |
| MATERIALS | Materials Sector | 51.51 | 52.86 | 0.026208503203261513 | 31 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 214.73 | 220.09 | 0.02496157965817547 | 32 |
| SMALL_VALUE | US Small-Cap Value | 220.18 | 225.52 | 0.024252884003996833 | 33 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 245.11 | 250.75 | 0.023010077108237104 | 34 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.39 | 119.86 | 0.021040974529346723 | 35 |
| INDIA | India Equities | 49.33 | 50.365 | 0.020981147374822706 | 36 |
| BROAD_AI_TECH | Broad AI Technology | 62.08 | 63.35 | 0.020457474226804218 | 37 |
| BRAZIL | Brazil Equities | 34.64 | 35.34 | 0.020207852193995457 | 38 |
| NASDAQ100 | Nasdaq 100 | 709.43 | 723.03 | 0.01917031983423323 | 39 |
| SMALL_CAP | US Small-Cap Stocks | 296.19 | 301.56 | 0.018130254228704512 | 40 |
| BITCOIN_ETF | Bitcoin ETF | 36.15 | 36.8 | 0.017980636237897585 | 41 |
| INDUSTRIALS | Industrials Sector | 182.38 | 185.18 | 0.015352560587783781 | 42 |
| REGIONAL_BANKS | Regional Banks | 75.07 | 76.21 | 0.015185826561875615 | 43 |
| EURO | Euro | 105.2249524808 | 106.68 | 0.013827970314032711 | 44 |
| TAIWAN | Taiwan Equities | 101.88 | 103.09 | 0.01187671770710641 | 45 |
| HEALTHCARE | Healthcare Sector | 164.44 | 165.68 | 0.007540744344441741 | 46 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.177772215 | 91.48 | 0.003314709031136953 | 47 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.86 | 85.12 | 0.0030638699033702643 | 48 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.375394139 | 79.61 | 0.0029556497141818294 | 49 |
| AGRICULTURE | Agriculture Commodities | 27.55 | 27.62 | 0.002540834845734974 | 50 |
| SEMICONDUCTORS | Semiconductors | 581.45 | 582.7 | 0.0021497979189957217 | 51 |
| COMMUNICATIONS | Communication Services Sector | 111.02 | 111.25 | 0.0020716987930102793 | 52 |
| REAL_ESTATE | Real Estate Sector | 44.89 | 44.98 | 0.002004900868790349 | 53 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.9013480405 | 47.95 | 0.001015669944379738 | 54 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 55 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.3805333443 | 93.17 | -0.0022545742325518203 | 56 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.4958079691 | 93.27 | -0.0024151667759759743 | 57 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.8703137357 | 97.6 | -0.0027619584057938518 | 58 |
| TIPS | Treasury Inflation-Protected Securities | 107.3817859369 | 107.08 | -0.0028104015431196228 | 59 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.523037656 | 95.24 | -0.002963030311277204 | 60 |
| LOW_VOL | US Low Volatility Equities | 76.7773730886 | 76.21 | -0.007389847630567714 | 61 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 107.4167917852 | 106.55 | -0.00806942537376576 | 62 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.9496304855 | 105.94 | -0.009440242859341863 | 63 |
| MOMENTUM | US Momentum Equities | 312.44 | 309.32 | -0.009985917296120861 | 64 |
| US_DOLLAR | US Dollar | 28.4 | 28.07 | -0.011619718309859084 | 65 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.2114186623 | 82.76 | -0.017235413977769398 | 66 |
| SOLAR | Solar Energy | 54.81 | 52.75 | -0.03758438241196871 | 67 |
| BIOTECH | Biotechnology | 163.87 | 157.37 | -0.03966558857631053 | 68 |
| UTILITIES | Utilities Sector | 45.7 | 43.61 | -0.045733041575492406 | 69 |
| SOUTH_KOREA | South Korea Equities | 181.29 | 166.09 | -0.08384356555794581 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | FINANCIALS | 25.0 | 0.027653880463871516 | 0.006913470115967879 | JPMorgan and Wells Fargo Q2 earnings July 14 as near-term catalysts; solid economy with Fed on hold supports net interest margins; low drawdown and beta cushion versus tech volatility. |
| anthropic-claude-fable-5 | HEALTHCARE | 20.0 | 0.007540744344441741 | 0.0015081488688883484 | Defensive sector with improving relative strength backed by broad rotation from stretched tech; earnings season catalyst and low beta help in a cooling-labor-market, elevated-inflation environment. |
| anthropic-claude-fable-5 | LARGE_VALUE | 20.0 | 0.03963833050779031 | 0.007927666101558062 | Value tilt benefits from rotation out of expensive mega-cap growth after tech drawdown; higher oil and elevated inflation support energy/financial-heavy value; at 52-week high with low volatility. |
| anthropic-claude-fable-5 | ENERGY | 15.0 | 0.05234260614934105 | 0.007851390922401157 | Cancellation of Iranian oil sales license and Strait of Hormuz uncertainty create supply-risk upside; sector lagged 30d despite rising oil, offering catch-up potential; negative beta hedges equity risk. |
| anthropic-claude-fable-5 | BIOTECH | 20.0 | -0.03966558857631053 | -0.007933117715262106 | Strong 30d outperformance supported by broad risk appetite in healthcare and M&A-friendly conditions; briefing support beyond price trend is limited, so sized moderately with reversal risk noted. |
| anthropic-claude-opus-4-7 | FINANCIALS | 25.0 | 0.027653880463871516 | 0.006913470115967879 | Bank earnings catalyst July 14 (JPM, WFC); sector leadership with strong breadth and low drawdown. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 20.0 | 0.007540744344441741 | 0.0015081488688883484 | Defensive sector leading recently at new highs; low beta cushion vs tech weakness. |
| anthropic-claude-opus-4-7 | LARGE_VALUE | 20.0 | 0.03963833050779031 | 0.007927666101558062 | Value outperforming amid tech rotation; solid breadth, low vol, at 52w highs. |
| anthropic-claude-opus-4-7 | LOW_VOL | 15.0 | -0.007389847630567714 | -0.001108477144585157 | Elevated policy/CPI/FOMC event risk over window; defensive posture with near-zero beta. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 20.0 | 0.023010077108237104 | 0.004602015421647421 | Iran/Hormuz geopolitical tension and sanctions news support defense; strong recent breadth. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | 0.027653880463871516 | 0.006913470115967879 | Broad financials strength with JPM/WFC earnings July 14 as catalysts; steady 30d outperformance and low volatility relative to growth sectors amid rotation to value. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 25.0 | 0.007540744344441741 | 0.0018851860861104353 | Defensive sector leading recent 30d returns (+7.94%), low beta, at 52w highs with fundamental durability; benefits if tech weakness/rotation continues before exit close. |
| anthropic-claude-opus-4-8 | LARGE_VALUE | 20.0 | 0.03963833050779031 | 0.007927666101558062 | Value leadership over growth into elevated inflation/rate-hold environment; lower volatility, dividend/cyclical tilt, positive benchmark-relative momentum with catalyst support from bank earnings. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 15.0 | 0.015352560587783781 | 0.0023028840881675673 | Solid ISM manufacturing/services expansion and defense demand; broad-based 30d gains with moderate beta and reasonable drawdown profile. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 15.0 | 0.003314709031136953 | 0.000497206354670543 | Cash-like ballast against CPI/FOMC event risk (July 14 CPI, July 29 FOMC) and elevated VIX; preserves capital while tech-heavy indices show weakness. |
| google-gemini-3-1-pro | SP500 | 40.0 | 0.03417100212649293 | 0.013668400850597173 | Provides broad US equity exposure amid solid economic expansion and steady payroll growth, balancing technology weakness with broader market resilience. |
| google-gemini-3-1-pro | ENERGY | 20.0 | 0.05234260614934105 | 0.010468521229868211 | Supported by rising oil prices, canceled Iranian oil sales licenses, and renewed uncertainty around the Strait of Hormuz. |
| google-gemini-3-1-pro | FINANCIALS | 20.0 | 0.027653880463871516 | 0.005530776092774303 | Positioned to benefit from upcoming Q2 earnings reports from major banks like JPMorgan Chase and Wells Fargo, alongside solid economic data. |
| google-gemini-3-1-pro | HEALTHCARE | 20.0 | 0.007540744344441741 | 0.0015081488688883484 | Offers defensive characteristics and has shown recent relative strength, providing a buffer against potential volatility from inflation and geopolitical concerns. |
| openai-gpt-5-5 | OIL | 25.0 | 0.08318031582813079 | 0.020795078957032698 | Crude oil has a near-term geopolitical catalyst from the canceled Iranian oil-sales license and renewed Strait of Hormuz uncertainty, while recent 30-day weakness leaves room for a sharp reversal if supply-risk premia rebuild. |
| openai-gpt-5-5 | ENERGY | 20.0 | 0.05234260614934105 | 0.010468521229868211 | Energy equities provide equity-linked exposure to the same oil supply-risk catalyst, with potential support from firm crude prices and sector sensitivity to inflationary energy shocks. |
| openai-gpt-5-5 | SEMICONDUCTORS | 20.0 | 0.0021497979189957217 | 0.0004299595837991444 | Semiconductors have near-term catalysts from TSMC monthly sales and Q2 results, while ISM comments noted AI-related capacity consumption and shortages in semiconductors and memory components; recent weakness raises rebound potential but also volatility risk. |
| openai-gpt-5-5 | FINANCIALS | 20.0 | 0.027653880463871516 | 0.005530776092774303 | Major bank earnings on July 14 create an immediate sector catalyst, and financials have shown broad participation with relatively moderate volatility versus high-beta technology segments. |
| openai-gpt-5-5 | BIOTECH | 15.0 | -0.03966558857631053 | -0.005949838286446579 | Biotech has strong recent breadth and price strength, likely helped by risk appetite and financing sensitivity if weak payroll data increases rate-cut expectations; independent briefing support is limited, so the position is sized below the main catalyst exposures. |
| xai-grok-4-3 | LARGE_VALUE | 30.0 | 0.03963833050779031 | 0.011891499152337092 | Recent outperformance and positioning for potential policy support amid soft labor data. |
| xai-grok-4-3 | FINANCIALS | 25.0 | 0.027653880463871516 | 0.006913470115967879 | Strong recent returns and sensitivity to rate expectations following weak payrolls. |
| xai-grok-4-3 | HEALTHCARE | 20.0 | 0.007540744344441741 | 0.0015081488688883484 | Defensive characteristics with solid recent performance in uncertain macro environment. |
| xai-grok-4-3 | SMALL_VALUE | 15.0 | 0.024252884003996833 | 0.003637932600599525 | Domestic growth exposure benefiting from potential easing signals. |
| xai-grok-4-3 | ENERGY | 10.0 | 0.05234260614934105 | 0.0052342606149341055 | Geopolitical oil supply risks from Iran-related developments. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | OIL | 5 | 0.42 | 0.08318031582813079 | 0.03127449757702777 | -0.002896504549465162 | 0.0982268198817407 |  | False | True |
| google-gemini-3-1-pro | SP500 | 4 | 0.65 | 0.03417100212649293 | 0.031175847042128033 | -0.0029951550843649 | 0.09832547041664044 |  | False | True |
| xai-grok-4-3 | LARGE_VALUE | 5 | 0.55 | 0.03963833050779031 | 0.02918531135272695 | -0.004985690773765983 | 0.10031600610604152 |  | False | True |
| anthropic-claude-opus-4-7 | FINANCIALS | 5 | 0.55 | 0.027653880463871516 | 0.019842823363476557 | -0.014328178763016376 | 0.10965849409529191 |  | False | True |
| anthropic-claude-opus-4-8 | FINANCIALS | 5 | 0.58 | 0.027653880463871516 | 0.019526412746474486 | -0.014644589380018447 | 0.10997490471229399 |  | False | True |
| anthropic-claude-fable-5 | FINANCIALS | 5 | 0.5 | 0.027653880463871516 | 0.01626755829355334 | -0.017903443832939594 | 0.11323375916521514 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 2e94ad1667629689bb2f5fdbe239e2cefb0f3f5850e42376f32e89862339bd44 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 7858eef0aa73ea38b28daacc4aaa57e57b110de6456378f1697ff1cd79ca213c |
| manifest.yaml | aec77ea90ae75a36c2f767e573aed0d150c088bee528677cf0b65952fbcd7307 |
| market_data/universe_trailing_returns.csv | b78baf02c9a6c05956be9d81dbf41bed9eaa2877f3133f029ebc1632fb8c318f |
| market_data/universe_trailing_returns.md | 34cca079f4788d41e79044d96827cc3e801f490691e2d3910b59fa16e5012825 |
| market_data/universe_trailing_returns.json | 9eb6aca0bc09815330a254bbac9a42f0d2a4a102906315d6f25853d91c4b1769 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | ccd149f34c709af9657f72fa6f448cbf5d0c23b23e21bcbec716a9290317d883 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | c3b656ea8db800a5b13af4f8390c882dcb8030847758aa9663bc17012c35d2b6 | yes |
| Final briefing | research/final_briefing.md | model-facing | 2e94ad1667629689bb2f5fdbe239e2cefb0f3f5850e42376f32e89862339bd44 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
