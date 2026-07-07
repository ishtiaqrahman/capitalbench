# CapitalBench Report: CB-2026-06-05-1M / official-20260605-r3

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260605-r3
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 5 2026 One-Month Portfolio Round
- Description: One-month CapitalBench portfolio evaluation round scored from the June 5, 2026 adjusted close to the July 6, 2026 adjusted close.
- Decision date: 2026-06-05
- Decision deadline: 2026-06-05T20:35:00Z
- Horizon: one month
- Entry date: 2026-06-05
- Exit date: 2026-07-06
- Entry rule: Use adjusted close on Friday, June 5, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Monday, July 6, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | ENERGY | 4 | 0.55 | Energy and financials benefit from commodity and rate backdrop; healthcare and industrials add defensive growth exposure ahead of June data. | Weaker-than-expected CPI or employment data triggering broad equity selloff; FOMC June decision surprises on hawkish side pressuring financials; Oil price reversal if inventories surprise higher |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Defensive barbell: healthcare + dividend quality + energy/defense cyclicals with catalyst support, plus T-bill ballast against elevated volatility and stretched large-cap growth valuations. | Dovish surprise at June 17 FOMC could rally growth/tech and underperform defensives; Oil price reversal on OPEC+ supply increase would hit ENERGY allocation; Healthcare drug-pricing headlines from CMS negotiations could pressure XLV; Reacceleration in mega-cap tech momentum leaves portfolio behind SPY benchmark |
| google-gemini-3-1-pro | google | portfolio | SP500 | 5 | 0.75 | A balanced approach combining growth-oriented equities with defensive assets like healthcare, Treasuries, and gold to navigate market uncertainties. | Higher-than-expected inflation could lead to tighter monetary policy, negatively impacting both equities and bonds.; A slowdown in economic growth could reduce corporate earnings, particularly in cyclical sectors.; Geopolitical tensions could increase market volatility and negatively affect global supply chains. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Favor inflation-resilient and defensive sectors with positive momentum over richly valued mega-cap growth, with a cash buffer for volatility around June CPI/PCE and the June 17 FOMC. | A dovish FOMC surprise or soft CPI could spark a tech/growth rally that my defensive tilt underperforms versus SPY; Oil reversal lower would hurt the energy overweight; Healthcare drug-pricing policy headlines (CMS negotiated prices) could pressure the sector; Short-Treasury allocation drags relative return if equities rally broadly |
| openai-gpt-5-5 | openai | portfolio | ENERGY | 5 | 0.58 | A concentrated pro-inflation, pro-AI, and defense allocation offers higher expected one-month upside than the broad S&P 500 while diversifying across commodities and selected equity themes. The main bet is that oil strength and AI/security capex momentum persist through early July. | A softer CPI/PPI or dovish rates move could rotate leadership away from energy and commodity-linked exposures toward long-duration growth or broad equities.; Crude oil could fall on weaker demand data, OPEC supply changes, inventory builds, or easing geopolitical risk, hurting both OIL and ENERGY holdings.; Semiconductor and cybersecurity momentum could reverse if high valuations, profit-taking, or AI spending skepticism pressure technology shares.; A broad risk-off move around the FOMC, employment report, or inflation releases could hurt the equity holdings despite their thematic catalysts. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 128.5482959798 | 160.81 | 0.25096951907685794 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 11.869999885559082 | 13.55 | 0.14153328817507305 | 2 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 229.2920067967 | 250.78 | 0.09371453241434691 | 3 |
| TAIWAN | Taiwan Equities | 98.08000183105469 | 107.27 | 0.09369900078892046 | 4 |
| SOUTH_KOREA | South Korea Equities | 175.19000244140625 | 189.85 | 0.08368056027339166 | 5 |
| REGIONAL_BANKS | Regional Banks | 69.7661423218 | 75.56 | 0.08304684027784592 | 6 |
| FINANCIALS | Financials Sector | 52.1184269707 | 56.14 | 0.07716221043203886 | 7 |
| CYBERSECURITY | Cybersecurity | 86.625344402 | 92.91 | 0.07254984833116462 | 8 |
| INDUSTRIALS | Industrials Sector | 173.7555566547 | 185.56 | 0.06793706959690882 | 9 |
| SMALL_CAP | US Small-Cap Stocks | 280.9870816282 | 298.9 | 0.0637499712371199 | 10 |
| HEALTHCARE | Healthcare Sector | 152.3437605123 | 161.96 | 0.06312197792257868 | 11 |
| SMALL_VALUE | US Small-Cap Value | 208.6860785651 | 221.74 | 0.06255290973244199 | 12 |
| SEMICONDUCTORS | Semiconductors | 569.69 | 604.3 | 0.060752338991381105 | 13 |
| BITCOIN_ETF | Bitcoin ETF | 34.13999938964844 | 36.12 | 0.057996503976268876 | 14 |
| JAPAN | Japan Equities | 90.2393741181 | 95.27 | 0.055747570626057286 | 15 |
| INDIA | India Equities | 47.34 | 49.88 | 0.05365441487114486 | 16 |
| MOMENTUM | US Momentum Equities | 306.1414469034 | 321.71 | 0.05085411744824109 | 17 |
| LARGE_VALUE | US Large-Cap Value | 235.6838047336 | 247.24000549316406 | 0.04903264682368125 | 18 |
| EUROPE | Europe Equities | 85.9622495364 | 89.97 | 0.046622214811897766 | 19 |
| DEVELOPED_EX_US | Developed Markets ex-US | 68.8110520147 | 71.89 | 0.04474496312950205 | 20 |
| AGRICULTURE | Agriculture Commodities | 26.399999618530273 | 27.54 | 0.04318183325538971 | 21 |
| LOW_VOL | US Low Volatility Equities | 73.3321267906 | 76.17 | 0.03869890774480811 | 22 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 207.029871671 | 215.0 | 0.03849747992727193 | 23 |
| BRAZIL | Brazil Equities | 33.68927764892578 | 34.92 | 0.036531574345390005 | 24 |
| EMERGING_MARKETS | Emerging Markets | 57.9622803701 | 60.07 | 0.03636364229360578 | 25 |
| MID_CAP | US Mid-Cap Stocks | 73.7664932566 | 76.42 | 0.035971707834472566 | 26 |
| UNITED_KINGDOM | United Kingdom Equities | 45.7208012279 | 47.22 | 0.032790299641231035 | 27 |
| MEXICO | Mexico Equities | 74.01087188720703 | 76.43 | 0.03268611828380763 | 28 |
| MATERIALS | Materials Sector | 50.4411700306 | 51.98 | 0.030507420197954715 | 29 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.6274142548 | 118.01 | 0.029509395873495103 | 30 |
| UTILITIES | Utilities Sector | 44.0697207152 | 45.3 | 0.02791665717036551 | 31 |
| NASDAQ100 | Nasdaq 100 | 704.2836226246 | 722.8200073242188 | 0.026319488490362364 | 32 |
| SOUTH_AFRICA | South Africa Equities | 62.9896125793457 | 64.63 | 0.02604218939413161 | 33 |
| TOTAL_US_MARKET | Total US Stock Market | 362.3359658562 | 371.6700134277344 | 0.025760753695753147 | 34 |
| AUSTRALIA | Australia Equities | 27.671077728271484 | 28.33 | 0.02381267105672924 | 35 |
| SP500 | S&P 500 | 735.674690596 | 751.280029296875 | 0.021212281597226657 | 36 |
| BROAD_AI_TECH | Broad AI Technology | 62.5195599682 | 63.84 | 0.021120430669563817 | 37 |
| TECHNOLOGY | Technology Sector | 180.0863912042 | 183.57 | 0.01934409797712 | 38 |
| CONSUMER_STAPLES | Consumer Staples Sector | 82.8610535095 | 84.1 | 0.014952096769539125 | 39 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.00431823730469 | 96.35 | 0.01416442734038692 | 40 |
| US_DOLLAR | US Dollar | 28.020000457763672 | 28.32 | 0.010706621603683963 | 41 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.0636479233 | 79.87 | 0.010198771469313694 | 42 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.40577697753906 | 94.28 | 0.009359410635502385 | 43 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.3113184579 | 94.18 | 0.0093094981022257 | 44 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.8415226655 | 98.66 | 0.008365337253572802 | 45 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.744852602 | 85.45 | 0.008320828656245283 | 46 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.68274688720703 | 107.57 | 0.008316744166055656 | 47 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 107.7908229718 | 108.67 | 0.008156325408425591 | 48 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.899959564208984 | 48.22 | 0.006681434362423744 | 49 |
| DIVIDEND | US Dividend Equities | 32.0449135976 | 32.24 | 0.006087905395838256 | 50 |
| CANADA | Canada Equities | 57.759972862 | 58.06 | 0.005194378098425156 | 51 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 129.6 | 130.11 | 0.00393518518518543 | 52 |
| LARGE_GROWTH | US Large-Cap Growth | 122.5847482384 | 123.0 | 0.0033874667735371844 | 53 |
| TIPS | Treasury Inflation-Protected Securities | 108.1917641227 | 108.49 | 0.0027565487975755865 | 54 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.1830133436 | 91.43000030517578 | 0.002708694882072704 | 55 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 56 |
| REAL_ESTATE | Real Estate Sector | 44.3162865969 | 44.29 | -0.0005931588343378591 | 57 |
| EURO | Euro | 106.21943664550781 | 105.57 | -0.006114103652001268 | 58 |
| COPPER | Copper | 38.08000183105469 | 37.84 | -0.0063025687897672045 | 59 |
| COMMUNICATIONS | Communication Services Sector | 111.3742672391 | 110.21 | -0.010453646681244155 | 60 |
| SOFTWARE | Software | 95.832595444 | 94.79 | -0.01087934057477602 | 61 |
| YEN | Japanese Yen | 57.310001373291016 | 56.59 | -0.012563276147931957 | 62 |
| GOLD | Gold | 81.22 | 78.3 | -0.035951736025609526 | 63 |
| CHINA | China Equities | 54.0842676953 | 52.02 | -0.03816761848250716 | 64 |
| ENERGY | Energy Sector | 57.2623252921 | 53.13 | -0.07216481815959541 | 65 |
| BROAD_COMMODITIES | Broad Commodities | 17.46 | 16.1 | -0.07789232531500567 | 66 |
| SILVER | Silver | 61.56999969482422 | 56.11 | -0.08867954721271831 | 67 |
| SOLAR | Solar Energy | 64.05 | 57.54 | -0.10163934426229504 | 68 |
| METALS_MINING | Metals and Mining | 118.5175407164 | 106.08 | -0.1049426155927563 | 69 |
| OIL | Crude Oil | 133.02000427246094 | 104.35 | -0.21553152421899657 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 25.0 | 0.06312197792257868 | 0.01578049448064467 | Defensive sector with positive momentum (+5.2% 30d), low beta, attractive after consolidation amid sticky inflation and elevated VIX. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 20.0 | 0.09371453241434691 | 0.018742906482869384 | $1.5T FY27 defense budget tailwind, strong order flow, geopolitical risk premium. |
| anthropic-claude-opus-4-7 | ENERGY | 20.0 | -0.07216481815959541 | -0.014432963631919083 | WTI $90, EIA forecasts global inventory draws of 2.6mb/d, strong relative momentum, inflation hedge. |
| anthropic-claude-opus-4-7 | DIVIDEND | 20.0 | 0.006087905395838256 | 0.0012175810791676513 | Value/quality tilt outperforming amid stretched 25.9x forward P/E, sticky inflation, hawkish hold scenario at June FOMC. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 15.0 | 0.002708694882072704 | 0.0004063042323109056 | 3.6%+ yield with zero duration risk; hedge against equity drawdown given elevated VIX 21.5 and weak sentiment. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.06312197792257868 | 0.018936593376773603 | Defensive sector with positive recent momentum (+5.2% 30d, +2.4% 7d) while broad market sold off; low valuation and stable earnings provide downside cushion amid reaccelerating inflation. |
| anthropic-claude-opus-4-8 | ENERGY | 25.0 | -0.07216481815959541 | -0.018041204539898853 | Oil near $90, EIA forecasting large inventory draws in 2026; energy showing positive relative strength (+2.45% 7d) and inflation hedge with reaccelerating CPI/PPI. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 20.0 | 0.002708694882072704 | 0.0005417389764145409 | Cash-like buffer yielding ~4% with VIX at 21.5, sticky inflation (CPI 3.8% YoY, PPI 6% YoY) and elevated equity valuations (forward P/E 25.9) raising correction risk. |
| anthropic-claude-opus-4-8 | AEROSPACE_DEFENSE | 15.0 | 0.09371453241434691 | 0.014057179862152035 | FY2027 $1.5T defense budget tailwind; positive 30d momentum and lower beta to tech-led drawdown. |
| anthropic-claude-opus-4-8 | DIVIDEND | 10.0 | 0.006087905395838256 | 0.0006087905395838256 | Quality dividend tilt with best recent stability (+2.0% 30d) provides defensive equity ballast against rate and inflation pressure. |
| google-gemini-3-1-pro | SP500 | 40.0 | 0.021212281597226657 | 0.008484912638890663 | Broad US equity exposure provides a baseline for market returns, balancing growth and value. |
| google-gemini-3-1-pro | TECHNOLOGY | 20.0 | 0.01934409797712 | 0.0038688195954240004 | Technology sector offers strong growth potential, supported by AI and software trends. |
| google-gemini-3-1-pro | HEALTHCARE | 15.0 | 0.06312197792257868 | 0.009468296688386802 | Healthcare provides defensive characteristics and steady growth, mitigating broader market volatility. |
| google-gemini-3-1-pro | INTERMEDIATE_TREASURY | 15.0 | 0.0093094981022257 | 0.001396424715333855 | Intermediate Treasuries offer yield and downside protection against equity market corrections. |
| google-gemini-3-1-pro | GOLD | 10.0 | -0.035951736025609526 | -0.0035951736025609526 | Gold serves as a hedge against inflation and geopolitical risks, adding diversification. |
| openai-gpt-5-5 | ENERGY | 30.0 | -0.07216481815959541 | -0.021649445447878623 | Energy equities have supportive near-term oil fundamentals, with WTI near $90 and EIA forecasting a sizable 2026 global inventory draw, while inflation pressure favors real-asset-linked sectors. |
| openai-gpt-5-5 | OIL | 20.0 | -0.21553152421899657 | -0.04310630484379932 | Direct crude exposure targets the strongest immediate commodity catalyst from tight inventories and elevated inflation, with potential to outperform equities if oil prices continue rising. |
| openai-gpt-5-5 | SEMICONDUCTORS | 20.0 | 0.060752338991381105 | 0.012150467798276221 | Semiconductors retain strong AI-linked earnings momentum, supported by reported Q1 global semiconductor sales growth and continued large AI infrastructure capex expectations. |
| openai-gpt-5-5 | CYBERSECURITY | 15.0 | 0.07254984833116462 | 0.010882477249674694 | Cybersecurity has strong recent momentum and a secular spending tailwind from AI-related security demand, with less direct commodity and rate exposure than broad growth indexes. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 15.0 | 0.09371453241434691 | 0.014057179862152035 | Aerospace and defense offers policy-supported demand from a large FY2027 U.S. defense budget request and can provide relative resilience if broader equity volatility remains elevated. |
| xai-grok-4-3 | ENERGY | 30.0 | -0.07216481815959541 | -0.021649445447878623 | Oil at $90+ and EIA inventory draw forecasts support energy sector outperformance amid sticky inflation data releases. |
| xai-grok-4-3 | HEALTHCARE | 25.0 | 0.06312197792257868 | 0.01578049448064467 | Recent 30-day outperformance and defensive characteristics position it well ahead of CPI and FOMC events. |
| xai-grok-4-3 | FINANCIALS | 25.0 | 0.07716221043203886 | 0.019290552608009714 | Fed policy stability and 4.3% unemployment support bank profitability over the one-month window. |
| xai-grok-4-3 | INDUSTRIALS | 20.0 | 0.06793706959690882 | 0.013587413919381765 | ISM manufacturing at 54.0 and durable goods orders surge indicate near-term industrial strength. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | ENERGY | 4 | 0.55 | -0.07216481815959541 | 0.027009015560157525 | 0.005796733962930869 | 0.2239605035167004 |  | True | True |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.55 | 0.06312197792257868 | 0.02171432264307353 | 0.0005020410458468731 | 0.22925519643378442 |  | True | True |
| google-gemini-3-1-pro | SP500 | 5 | 0.75 | 0.021212281597226657 | 0.019623280035474366 | -0.0015890015617522901 | 0.23134623904138357 |  | False | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.55 | 0.06312197792257868 | 0.016103098215025154 | -0.005109183382201503 | 0.2348664208618328 |  | False | True |
| openai-gpt-5-5 | ENERGY | 5 | 0.58 | -0.07216481815959541 | -0.027665625381575 | -0.048877906978801657 | 0.27863514445843296 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 368c7a09f53eafa68f69caf3becee2e69e3830587ce13551c7212acaf69b14f1 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 0e5a222ebba001788946308d0e0b4c71b9e1bdc4f2882aad00ed1514ecaa5c5f |
| manifest.yaml | c65b51d312cd39845a084b20745b8725f0b966e7e44bd311d5900edacc90ff14 |
| market_data/universe_trailing_returns.csv | 30efc20118b973b5a836953a08852bad01096fd828eed623d3d196aa04324b6a |
| market_data/universe_trailing_returns.md | f3580ea3bf260aa7c674328c329f4602535148cf7de1f0acfb51de3ee610e8c9 |
| market_data/universe_trailing_returns.json | e308b733de0aa6e291b26f72cdd2ffd14a6f4552d59deb8dafb6c3e678751f4b |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 65e3f43ed481095a97c980cd66aaec36213b1c5253b635ac96e2144be5f33b1b | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 8f37051fc829b27408e9bfb954d4f87eb7180c7301daae7ab3a2230596e74218 | yes |
| Final briefing | research/final_briefing.md | model-facing | 368c7a09f53eafa68f69caf3becee2e69e3830587ce13551c7212acaf69b14f1 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
