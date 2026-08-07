# CapitalBench Report: CB-2026-07-30-1W / official-v2-2-all-weekly-20260730

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-weekly-20260730
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-30-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-30
- Decision deadline: 2026-07-31T12:30:00Z
- Horizon: one week
- Entry date: 2026-07-30
- Exit date: 2026-08-06
- Entry rule: Use the Thursday, July 30, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Thursday, August 6, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | SP500 | 3 | 0.65 | A balanced approach favoring technology and financials based on strong earnings and solid economic indicators. | A sudden reversal in tech stock sentiment.; Unexpectedly weak economic data.; A shift in Federal Reserve policy expectations. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 3 | 0.55 | Balanced allocation anchored on SPY with modest overweights to leading, lower-volatility clusters (Europe, Financials) that clear the SPY base hurdle. | Post-earnings tech reversal could drag broad indices lower; Hot ECI or inflation prints could push yields up and pressure rate-sensitive and equity names; Rally exhaustion after a 1.7% S&P day may mean mean-reversion week |
| anthropic-claude-opus-5 | anthropic | portfolio | SP500 | 5 | 0.5 | SPY base +0.4%; tilt toward broad-based leadership outside crowded semis while keeping 40% benchmark to limit tracking error. | Mega-cap tech momentum continues and SPY outruns the diversified tilts; Hot ECI or flash inflation lifts yields and hits gold and financials; Europe reverses from 52-week highs on dollar rebound; Weak JOLTS/claims triggers broad risk-off |
| xai-grok-4-3 | xai | portfolio | SP500 | 5 | 0.62 | Selected holdings exceed SP500 base forecast; allocations respect 50% cluster cap and 5% increments. | Inflation reacceleration from PCE and CPI prints; FOMC policy surprise on August 3 survey; Weak August 6 claims data triggering risk-off rotation |
| xai-grok-4-5 | xai | portfolio | SOFTWARE | 5 | 0.58 | Selected SOFTWARE, ENERGY, EUROPE, FINANCIALS and AGRICULTURE for higher base-case weekly returns than SPY after FOMC hold and mixed earnings; equal-ish weights keep cluster exposures balanced while targeting positive alpha. | Elevated inflation readings or hawkish Fed speak could pressure risk assets broadly; Sharp USD rebound would reverse international and commodity holdings; Post-earnings profit-taking in software and tech-related names; Oil price volatility spilling into energy sector underperformance |
| anthropic-claude-fable-5 | anthropic | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.58 | Overweight breadth (RSP), value, financials, Europe and gold versus SPY, expecting continued rotation away from concentrated mega-cap tech in a higher-for-longer rate regime with a softening dollar. | Mega-cap tech leadership resumes after strong Microsoft/Apple/Amazon results, dragging SPY above the breadth-tilted portfolio; Dollar rebound reverses Europe and gold tailwinds; Hot ECI or euro-area inflation prints push yields higher and hit all risk assets; SLOOS reveals credit tightening hurting financials |
| openai-gpt-5-5 | openai | portfolio | LARGE_VALUE | 5 | 0.57 | Base case is that one-week breadth and cyclical/value continuation modestly outpace SPY, while high-yield credit dampens volatility. The strongest near-term catalysts are SLOOS, JOLTS/orders, claims, and euro-area inflation. | The July 30 mega-cap technology rebound continues and SPY outperforms diversified value, financials, and international exposures.; Scheduled labor or credit data weaken risk appetite and pressure financials, high yield, and cyclical international equities.; Euro-area inflation or currency moves reverse the recent Europe and Australia strength.; A broad equity pullback after the S&P 500's 1.7% entry-day gain overwhelms relative-factor signals. |
| openai-gpt-5-6-sol | openai | portfolio | FINANCIALS | 4 | 0.59 | Financials, China, agriculture, and yen offer stronger one-week base cases than SPY based on relative trend, pullback quality, and identifiable macro transmission channels. Cluster diversification limits concentration to 30%. | Hot U.S. cost or labor data could lift yields and pressure risk assets.; The recent broad equity rally could reverse after the July 30 surge.; China or emerging-market sentiment could weaken despite recent relative strength.; Agriculture's pullback could continue without a near-term asset-specific catalyst.; Post-BOJ yen strength could reverse if rate differentials widen. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| TAIWAN | Taiwan Equities | 94.0 | 101.9800033569336 | 0.08489365273333616 | 1 |
| METALS_MINING | Metals and Mining | 101.86 | 110.3499984741211 | 0.0833496806805527 | 2 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 113.98 | 123.19999694824219 | 0.08089135767891009 | 3 |
| CYBERSECURITY | Cybersecurity | 90.02 | 96.38999938964844 | 0.07076204609696113 | 4 |
| SOFTWARE | Software | 93.31 | 99.41999816894531 | 0.0654806362549063 | 5 |
| SEMICONDUCTORS | Semiconductors | 538.9 | 571.47998046875 | 0.060456449190480654 | 6 |
| BROAD_AI_TECH | Broad AI Technology | 58.69 | 61.95000076293945 | 0.0555461026229247 | 7 |
| TECHNOLOGY | Technology Sector | 175.73 | 185.3300018310547 | 0.05462927121751937 | 8 |
| LARGE_GROWTH | US Large-Cap Growth | 117.43 | 123.5 | 0.05169036873030741 | 9 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 112.39 | 118.0999984741211 | 0.05080521820554407 | 10 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 238.13 | 249.99000549316406 | 0.049804751577558815 | 11 |
| NASDAQ100 | Nasdaq 100 | 683.55 | 714.6500244140625 | 0.045497804716644774 | 12 |
| SILVER | Silver | 53.5 | 55.849998474121094 | 0.04392520512375886 | 13 |
| SOUTH_AFRICA | South Africa Equities | 64.11 | 66.87999725341797 | 0.043206945147683085 | 14 |
| COMMUNICATIONS | Communication Services Sector | 106.58 | 111.18000030517578 | 0.04316007041823777 | 15 |
| SP500 | S&P 500 | 741.6900024414062 | 768.5599975585938 | 0.03622806702091186 | 16 |
| COPPER | Copper | 39.34 | 40.7599983215332 | 0.03609553435519053 | 17 |
| INDUSTRIALS | Industrials Sector | 178.39 | 184.75999450683594 | 0.03570824881908141 | 18 |
| TOTAL_US_MARKET | Total US Stock Market | 366.2699890136719 | 379.07000732421875 | 0.03494694813794608 | 19 |
| GOLD | Gold | 77.3 | 79.87000274658203 | 0.033247124794075544 | 20 |
| MOMENTUM | US Momentum Equities | 298.77 | 308.1700134277344 | 0.03146237382513095 | 21 |
| EMERGING_MARKETS | Emerging Markets | 58.19 | 59.959999084472656 | 0.030417581791934323 | 22 |
| SOLAR | Solar Energy | 49.84 | 51.25 | 0.02829052969502399 | 23 |
| LARGE_VALUE | US Large-Cap Value | 250.71 | 256.1199951171875 | 0.021578696969356992 | 24 |
| BIOTECH | Biotechnology | 151.46 | 154.5 | 0.020071305955367658 | 25 |
| JAPAN | Japan Equities | 93.29 | 95.1500015258789 | 0.019937844633711066 | 26 |
| SMALL_CAP | US Small-Cap Stocks | 292.59 | 298.25 | 0.019344475204210676 | 27 |
| MID_CAP | US Mid-Cap Stocks | 75.35 | 76.75 | 0.01857996018579966 | 28 |
| SOUTH_KOREA | South Korea Equities | 161.21 | 164.1199951171875 | 0.018050959104196407 | 29 |
| CANADA | Canada Equities | 59.79 | 60.70000076293945 | 0.015219949204540173 | 30 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 215.38 | 218.5800018310547 | 0.01485746973281965 | 31 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.09 | 72.12000274658203 | 0.014488714961063742 | 32 |
| FINANCIALS | Financials Sector | 57.0 | 57.810001373291016 | 0.014210550408614298 | 33 |
| AUSTRALIA | Australia Equities | 29.82 | 30.15999984741211 | 0.01140173867914518 | 34 |
| MATERIALS | Materials Sector | 51.64 | 52.16999816894531 | 0.01026332627701998 | 35 |
| EUROPE | Europe Equities | 90.99 | 91.83000183105469 | 0.00923180383618738 | 36 |
| SMALL_VALUE | US Small-Cap Value | 221.79 | 223.8300018310547 | 0.009197898151651174 | 37 |
| DIVIDEND | US Dividend Equities | 33.41 | 33.70000076293945 | 0.008680058753051778 | 38 |
| INDIA | India Equities | 49.7 | 50.119998931884766 | 0.008450682734099768 | 39 |
| REGIONAL_BANKS | Regional Banks | 75.9 | 76.48999786376953 | 0.007773357888926524 | 40 |
| CHINA | China Equities | 55.5 | 55.904998779296875 | 0.007297275302646344 | 41 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.3780356411 | 94.94999694824219 | 0.006060322227061876 | 42 |
| HEALTHCARE | Healthcare Sector | 163.52 | 164.4499969482422 | 0.005687359027899852 | 43 |
| YEN | Japanese Yen | 57.58000183105469 | 57.88999938964844 | 0.005383771252792213 | 44 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.0867925304 | 79.45999908447266 | 0.004718949171306885 | 45 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 105.9531035768 | 106.36000061035156 | 0.0038403503041948284 | 46 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.7616939646 | 47.88999938964844 | 0.0026863667177201567 | 47 |
| US_DOLLAR | US Dollar | 28.14 | 28.190000534057617 | 0.001776849113632517 | 48 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.473637823 | 105.66000366210938 | 0.001766942365466928 | 49 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.2823544128 | 97.43000030517578 | 0.0015177047601999671 | 50 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.37709045410156 | 91.44999694824219 | 0.0007978640354853184 | 51 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.9478252923 | 93.01000213623047 | 0.0006689435038951252 | 52 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.4684265552 | 82.5199966430664 | 0.0006253312936908006 | 53 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.892203981 | 92.94999694824219 | 0.0006221508885073668 | 54 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 55 |
| TIPS | Treasury Inflation-Protected Securities | 106.9549192645 | 106.87000274658203 | -0.0007939468189207544 | 56 |
| EURO | Euro | 106.38701629638672 | 106.30000305175781 | -0.0008178934578491059 | 57 |
| LOW_VOL | US Low Volatility Equities | 76.38 | 76.26000213623047 | -0.0015710639404232785 | 58 |
| AGRICULTURE | Agriculture Commodities | 27.48 | 27.43000030517578 | -0.0018194939892365314 | 59 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.47 | 85.11000061035156 | -0.004211997070883822 | 60 |
| BITCOIN_ETF | Bitcoin ETF | 36.70000076293945 | 36.4900016784668 | -0.005722045779484541 | 61 |
| MEXICO | Mexico Equities | 77.11 | 76.62999725341797 | -0.006224909176268056 | 62 |
| ETHEREUM_ETF | Ethereum ETF | 14.510000228881836 | 14.399999618530273 | -0.00758102058004162 | 63 |
| UNITED_KINGDOM | United Kingdom Equities | 48.68 | 48.29999923706055 | -0.007806096198427537 | 64 |
| REAL_ESTATE | Real Estate Sector | 45.3 | 44.810001373291016 | -0.010816746726467596 | 65 |
| ENERGY | Energy Sector | 58.96 | 58.15999984741211 | -0.013568523619197581 | 66 |
| BROAD_COMMODITIES | Broad Commodities | 17.5 | 17.229999542236328 | -0.015428597586495507 | 67 |
| BRAZIL | Brazil Equities | 36.53 | 35.810001373291016 | -0.019709789945496436 | 68 |
| UTILITIES | Utilities Sector | 44.66 | 43.380001068115234 | -0.028660970261638163 | 69 |
| OIL | Crude Oil | 127.48 | 118.87000274658203 | -0.06753998473029477 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 25.0 | 0.01485746973281965 | 0.0037143674332049126 | Breadth is broadening: RSP beat SPY by 1.16% over 5 sessions and 1.91% over 21, with lower volatility and shallow drawdown. |
| anthropic-claude-fable-5 | LARGE_VALUE | 25.0 | 0.021578696969356992 | 0.005394674242339248 | Value leading with +1.36% 5-day active return, +2.70% prior active trend, only -0.53% from 52-week high and low 9.97% volatility. |
| anthropic-claude-fable-5 | FINANCIALS | 20.0 | 0.014210550408614298 | 0.0028421100817228595 | Strong prior trend (+5.29% prior active) plus +1.62% recent active, near 52-week high; benefits from elevated rates and solid activity per FOMC. |
| anthropic-claude-fable-5 | EUROPE | 20.0 | 0.00923180383618738 | 0.001846360767237476 | Europe at 52-week high with +3.12% 5-day active return; CAC 40 up 0.9%, dollar weakening (-1.47% 5-day) boosts USD-denominated returns. |
| anthropic-claude-fable-5 | GOLD | 10.0 | 0.033247124794075544 | 0.0033247124794075545 | Diversifier with positive momentum: +1.51% 5-day, +2.37% 21-day, supported by weakening dollar and sticky elevated inflation. |
| anthropic-claude-opus-4-8 | SP500 | 50.0 | 0.03622806702091186 | 0.01811403351045593 | Broad large-cap exposure after strong tech-led rally; solid GDP final sales and megacap earnings beats support continuation. |
| anthropic-claude-opus-4-8 | EUROPE | 25.0 | 0.00923180383618738 | 0.002307950959046845 | Europe showing strong recent active return (+3.12% 5s) with low drawdown and improving momentum; ECB steady. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | 0.014210550408614298 | 0.0035526376021535744 | Strong prior active return (+5.29%), high quality-evidence rank, low volatility and drawdown, steady rates backdrop. |
| anthropic-claude-opus-5 | SP500 | 40.0 | 0.03622806702091186 | 0.014491226808364744 | Core benchmark exposure given strong mega-cap earnings from Microsoft, Apple, Amazon. |
| anthropic-claude-opus-5 | FINANCIALS | 20.0 | 0.014210550408614298 | 0.0028421100817228595 | Steady leadership with low volatility, positive prior active return, minimal drawdown; steep curve with 30y at 5.22%. |
| anthropic-claude-opus-5 | EUROPE | 20.0 | 0.00923180383618738 | 0.001846360767237476 | At 52-week high with positive breadth, weaker dollar tailwind, ECB on hold, contained 2.8% euro-area inflation. |
| anthropic-claude-opus-5 | HEALTHCARE | 10.0 | 0.005687359027899852 | 0.0005687359027899852 | Defensive diversifier with positive prior active return, negative SPY beta, shallow drawdown. |
| anthropic-claude-opus-5 | GOLD | 10.0 | 0.033247124794075544 | 0.0033247124794075545 | Hedge against elevated core inflation (3.3-3.4%) and hawkish FOMC dissents; weaker dollar supportive. |
| google-gemini-3-1-pro | SP500 | 50.0 | 0.03622806702091186 | 0.01811403351045593 | Core holding to capture broad market recovery and solid GDP growth. |
| google-gemini-3-1-pro | TECHNOLOGY | 25.0 | 0.05462927121751937 | 0.013657317804379843 | Strong earnings from major tech companies support continued outperformance. |
| google-gemini-3-1-pro | FINANCIALS | 25.0 | 0.014210550408614298 | 0.0035526376021535744 | Solid economic growth and stable rates provide a favorable environment for financials. |
| openai-gpt-5-5 | LARGE_VALUE | 25.0 | 0.021578696969356992 | 0.005394674242339248 | Large-cap value has positive relative trend, low recent drawdown, and less dependence on mega-cap growth continuation after the July 30 rally. |
| openai-gpt-5-5 | FINANCIALS | 20.0 | 0.014210550408614298 | 0.0028421100817228595 | Financials combine the strongest prior active trend among major US sectors considered, positive near-term active return, and a macro setup where loan and labor data can matter within the week. |
| openai-gpt-5-5 | EUROPE | 20.0 | 0.00923180383618738 | 0.001846360767237476 | Europe has strong recent active return, is at a 52-week high, and has ECB policy already held steady with euro-area flash inflation due immediately after cutoff. |
| openai-gpt-5-5 | AUSTRALIA | 15.0 | 0.01140173867914518 | 0.0017102608018717768 | Australia shows strong short-term and prior relative performance with shallow drawdown, while maintaining a non-US cyclical exposure distinct from US mega-cap concentration. |
| openai-gpt-5-5 | HIGH_YIELD_CREDIT | 20.0 | 0.004718949171306885 | 0.0009437898342613771 | High yield has low volatility, shallow drawdown, and a modest positive prior active trend, offering a lower-beta way to benefit if risk appetite remains stable. |
| openai-gpt-5-6-sol | FINANCIALS | 30.0 | 0.014210550408614298 | 0.004263165122584289 | Strong prior and recent benchmark-relative performance, supported by solid domestic demand and an upcoming lending-conditions survey. |
| openai-gpt-5-6-sol | AGRICULTURE | 25.0 | -0.0018194939892365314 | -0.00045487349730913285 | Highest quality score in the universe combines strong prior trend with a recent pullback, offering a diversified mean-reversion setup. |
| openai-gpt-5-6-sol | CHINA | 25.0 | 0.007297275302646344 | 0.001824318825661586 | Positive prior and recent active returns align with reported 4.3% year-over-year Chinese GDP growth. |
| openai-gpt-5-6-sol | YEN | 20.0 | 0.005383771252792213 | 0.0010767542505584428 | Recent strength, elevated volume, and the BOJ's inflation outlook support continued adjustment in rate differentials. |
| xai-grok-4-3 | SP500 | 40.0 | 0.03622806702091186 | 0.014491226808364744 | Broad market exposure with solid recent recovery and limited near-term catalysts. |
| xai-grok-4-3 | LARGE_VALUE | 20.0 | 0.021578696969356992 | 0.004315739393871399 | Value tilt shows positive active return and lower volatility than growth. |
| xai-grok-4-3 | FINANCIALS | 20.0 | 0.014210550408614298 | 0.0028421100817228595 | Sector exhibits strong prior active rank and positive recent momentum. |
| xai-grok-4-3 | EUROPE | 15.0 | 0.00923180383618738 | 0.0013847705754281069 | International equity with highest 5s active return among peers. |
| xai-grok-4-3 | ENERGY | 5.0 | -0.013568523619197581 | -0.0006784261809598791 | Commodity exposure with top quality evidence score and prior strength. |
| xai-grok-4-5 | SOFTWARE | 25.0 | 0.0654806362549063 | 0.016370159063726575 | Recent relative strength and mega-cap software earnings support short-horizon continuation above broad market. |
| xai-grok-4-5 | ENERGY | 20.0 | -0.013568523619197581 | -0.0027137047238395165 | High quality evidence score and strong prior active trend support base case above SPY despite oil volatility. |
| xai-grok-4-5 | EUROPE | 20.0 | 0.00923180383618738 | 0.001846360767237476 | At 52-week high with positive active returns and ECB policy stability favoring continuation. |
| xai-grok-4-5 | FINANCIALS | 20.0 | 0.014210550408614298 | 0.0028421100817228595 | Solid prior active return and quality rank with stable rates backdrop after FOMC hold. |
| xai-grok-4-5 | AGRICULTURE | 15.0 | -0.0018194939892365314 | -0.0002729240983854797 | Highest quality evidence score and constructive prior active trend for diversified commodity exposure. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | SP500 | 3 | 0.65 | 0.03622806702091186 | 0.035323988916989346 | -0.0009040781039225121 | 0.04956966381634681 |  | False | True |
| anthropic-claude-opus-4-8 | SP500 | 3 | 0.55 | 0.03622806702091186 | 0.02397462207165635 | -0.01225344494925551 | 0.06091903066167981 |  | False | True |
| anthropic-claude-opus-5 | SP500 | 5 | 0.5 | 0.03622806702091186 | 0.023073146039522624 | -0.013154920981389234 | 0.06182050669381353 |  | False | True |
| xai-grok-4-3 | SP500 | 5 | 0.62 | 0.03622806702091186 | 0.022355420678427232 | -0.013872646342484626 | 0.06253823205490892 |  | False | True |
| xai-grok-4-5 | SOFTWARE | 5 | 0.58 | 0.0654806362549063 | 0.018072001090461913 | -0.018156065930449945 | 0.06682165164287424 |  | False | True |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 5 | 0.58 | 0.01485746973281965 | 0.017122225003912053 | -0.019105842016999806 | 0.0677714277294241 |  | False | True |
| openai-gpt-5-5 | LARGE_VALUE | 5 | 0.57 | 0.021578696969356992 | 0.012737195727432739 | -0.02349087129347912 | 0.07215645700590342 |  | False | True |
| openai-gpt-5-6-sol | FINANCIALS | 4 | 0.59 | 0.014210550408614298 | 0.0067093647014951855 | -0.029518702319416674 | 0.07818428803184096 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | f7ad652a48296d549882fef2a721ed1767578d1146dfc7c950b8f544e6de2b6e |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 1a844da9c59ab06e30e88b53a60f08b23075e0cfd4df40bd80afc8570a93c261 |
| manifest.yaml | 04045275aa8a69ce129c5bb757e985071021c68f11e9aa8e6c252f48b0d365df |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 91d25a6330eb03b611413a9980768efe6545601d469b4c6610eeb33bfdf520ad |
| market_data/universe_decision_context.md | d978c80553aff05cc644c1c526a5897f7c606c85751e09b2d81dbb08780c18da |
| market_data/universe_decision_context.json | 6a84368376629a9fe6ee691d8764ee090c7e1acc8955ba319d85d81ffbcc9825 |
| market_data/decision_context_source_history.json | 3f4866a9cdb0ae8273873b5d8875b5562688dc82cf6e0e84a9d11231cc8a248e |
| market_data/universe_quality_evidence.md | 9435c6a12a9cd9492f986ec400773f221246abe0dbebdfa5ce1ae0da859ab86f |
| market_data/universe_quality_evidence.json | 454ebb1052dd363cf2c9c12d6fe006f141dc43cc8fee7e75ca7f34191e2555c1 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | a15a0a36c3925c4f53cd8baad0484ebded55acf929ac80f0d98276e30b2e7359 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 66ef4880c3fe0193e9ac0823c981069cabe80024ff0832c4fa329507a1dc317f | yes |
| Final briefing | research/final_briefing.md | model-facing | f7ad652a48296d549882fef2a721ed1767578d1146dfc7c950b8f544e6de2b6e | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
