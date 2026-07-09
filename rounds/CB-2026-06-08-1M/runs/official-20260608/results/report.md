# CapitalBench Report: CB-2026-06-08-1M / official-20260608

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260608
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench June 8 2026 One-Month Portfolio Round
- Description: One-month CapitalBench portfolio evaluation round scored from the June 8, 2026 adjusted close to the July 8, 2026 adjusted close.
- Decision date: 2026-06-08
- Decision deadline: 2026-06-08T20:35:00Z
- Horizon: one month
- Entry date: 2026-06-08
- Exit date: 2026-07-08
- Entry rule: Use adjusted close on Monday, June 8, 2026 for each option; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on Wednesday, July 8, 2026 for each selected option; CASH return is 0 unless explicitly priced.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Tilt toward defensives with strong relative momentum and secular catalysts (AI semis, defense budget, capex cycle) while sidestepping duration and stretched mega-cap growth into hot inflation prints and June FOMC. | Hot June 10 CPI/June 11 PPI prints could spike yields and hurt all equity sectors; Hawkish June 17 FOMC surprise despite 98.7% hold probability; Semiconductor pullback if AI capex guidance disappoints; Healthcare drug-pricing CMS headline risk; Defense budget reconciliation delays |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Overweight defensive and real-asset cyclical sectors showing relative strength while holding a short-Treasury buffer for the CPI/PPI/FOMC catalyst cluster. | A soft CPI/PPI print or dovish FOMC surprise sparks a growth/tech rally that leaves defensives lagging the S&P 500.; Oil reverses lower on demand weakness or OPEC supply news, hurting the energy overweight.; Healthcare drug-pricing headlines from CMS negotiated-price file pressure the sector.; Broad risk-off escalation drags all equity sectors down faster than the short-Treasury buffer offsets. |
| xai-grok-4-3 | xai | portfolio | ENERGY | 3 | 0.55 | Energy benefits from elevated crude, healthcare provides stability, and industrials capture manufacturing rebound signals. | Hotter-than-expected CPI on June 10 could pressure rate-sensitive cyclicals; FOMC June 16-17 decision may trigger volatility if hawkish signals emerge; Weakening consumer sentiment could weigh on discretionary spending and related sectors |
| google-gemini-3-1-pro | google | portfolio | SP500 | 5 | 0.75 | A balanced approach combining broad US equities, growth sectors, and defensive assets to navigate market uncertainties. | Higher-than-expected inflation could lead to tighter monetary policy, negatively impacting equities.; A slowdown in economic growth could reduce corporate earnings and weigh on market performance.; Geopolitical tensions could increase market volatility and negatively affect risk assets. |
| openai-gpt-5-5 | openai | portfolio | ENERGY | 5 | 0.61 | Overweight energy/oil and semiconductors versus the benchmark, with small defensive hedges. The portfolio is positioned for persistent inflation, commodity tightness, and continued AI-led equity leadership during a macro-event-heavy window. | A softer-than-expected CPI/PPI/PCE sequence could reduce inflation-hedge demand and pull down oil, energy equities, and the dollar.; Crude oil could fall on a surprise inventory build, OPEC supply shift, weaker demand data, or geopolitical de-escalation.; Semiconductors could underperform if high valuations face renewed rate pressure or AI capex sentiment reverses.; A broad risk-off equity selloff could overwhelm sector selection and hurt energy, oil-linked equities, and semiconductors simultaneously. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| BIOTECH | Biotechnology | 128.3085229866 | 162.97 | 0.2701416570512616 | 1 |
| HEALTHCARE | Healthcare Sector | 151.9853280322 | 162.3 | 0.06786623486192522 | 2 |
| CYBERSECURITY | Cybersecurity | 86.0558352173 | 91.66 | 0.06512242625440678 | 3 |
| FINANCIALS | Financials Sector | 51.7895726514 | 54.97 | 0.06141057332153954 | 4 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 227.1035147728 | 239.63 | 0.0551576017646922 | 5 |
| AGRICULTURE | Agriculture Commodities | 26.33 | 27.62 | 0.04899354348651741 | 6 |
| UTILITIES | Utilities Sector | 43.2449660772 | 45.36 | 0.04890821093544817 | 7 |
| LOW_VOL | US Low Volatility Equities | 72.3340033825 | 75.86000061035156 | 0.048746053902287034 | 8 |
| REGIONAL_BANKS | Regional Banks | 69.9550487924 | 73.34 | 0.048387518356898696 | 9 |
| INDUSTRIALS | Industrials Sector | 173.2068968995 | 180.42 | 0.04164443350477698 | 10 |
| LARGE_VALUE | US Large-Cap Value | 236.5311578933 | 245.1999969482422 | 0.036649882121884136 | 11 |
| SMALL_CAP | US Small-Cap Stocks | 283.441291537 | 293.4800109863281 | 0.03541727951806806 | 12 |
| TAIWAN | Taiwan Equities | 100.43 | 103.9 | 0.03455142885591944 | 13 |
| SMALL_VALUE | US Small-Cap Value | 210.4895631058 | 217.67999267578125 | 0.03416050403585613 | 14 |
| BRAZIL | Brazil Equities | 33.3714071069 | 34.41 | 0.031122238561084092 | 15 |
| ETHEREUM_ETF | Ethereum ETF | 12.720000267028809 | 13.11 | 0.030660355722011978 | 16 |
| INDIA | India Equities | 47.21 | 48.65 | 0.03050201228553262 | 17 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 206.8107186528 | 212.2 | 0.026059004012493503 | 18 |
| CONSUMER_STAPLES | Consumer Staples Sector | 82.4936207458 | 84.39 | 0.022988192748183423 | 19 |
| EUROPE | Europe Equities | 86.3470226033 | 88.18 | 0.021228032437449196 | 20 |
| AUSTRALIA | Australia Equities | 27.6781919663 | 28.12 | 0.01596231553845473 | 21 |
| UNITED_KINGDOM | United Kingdom Equities | 45.7700905781 | 46.49 | 0.015728817942179507 | 22 |
| EMERGING_MARKETS | Emerging Markets | 58.2619302773 | 59.17 | 0.015585987597355633 | 23 |
| TOTAL_US_MARKET | Total US Stock Market | 363.422834156 | 368.25 | 0.013282505638949171 | 24 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.4974713567 | 70.34 | 0.01212315537317421 | 25 |
| MEXICO | Mexico Equities | 73.819822149 | 74.71 | 0.012058791596696539 | 26 |
| JAPAN | Japan Equities | 91.4628576958 | 92.54 | 0.011776827570624482 | 27 |
| US_DOLLAR | US Dollar | 28.03 | 28.36 | 0.011773100249732327 | 28 |
| REAL_ESTATE | Real Estate Sector | 43.6520380059 | 44.15 | 0.011407531397106707 | 29 |
| SP500 | S&P 500 | 737.3404444205 | 745.4000244140625 | 0.010930608858567004 | 30 |
| MID_CAP | US Mid-Cap Stocks | 73.926096217 | 74.7300033569336 | 0.01087447033012312 | 31 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.8849891064 | 95.79 | 0.009537977525456265 | 32 |
| DIVIDEND | US Dividend Equities | 32.0349925717 | 32.34000015258789 | 0.00952107543665659 | 33 |
| MATERIALS | Materials Sector | 49.7736688669 | 50.16 | 0.007761757208074815 | 34 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.1731405744 | 79.66 | 0.006149300407535252 | 35 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.365049657 | 93.69 | 0.0034804281065965448 | 36 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.2116481754 | 93.51 | 0.0032007997974521363 | 37 |
| CANADA | Canada Equities | 57.789833265 | 57.97 | 0.0031176199137628036 | 38 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.1929841488 | 91.44999694824219 | 0.0028183396106746805 | 39 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.6532642788 | 106.91 | 0.0024071998446186793 | 40 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.8415226655 | 98.04 | 0.002028559338539404 | 41 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.1563410314 | 115.30000305175781 | 0.0012475389463670883 | 42 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.3064828026 | 84.36 | 0.0006347933826786889 | 43 |
| MOMENTUM | US Momentum Equities | 314.7422164986 | 314.8500061035156 | 0.0003424694853926269 | 44 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 45 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 107.6812085637 | 107.67 | -0.00010409024795965394 | 46 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.8397910759 | 47.83 | -0.00020466385157225098 | 47 |
| TIPS | Treasury Inflation-Protected Securities | 108.072926487 | 108.05 | -0.00021213904115724436 | 48 |
| NASDAQ100 | Nasdaq 100 | 715.2814989544 | 711.4400024414062 | -0.005370607961493912 | 49 |
| EURO | Euro | 106.34934997558594 | 105.45 | -0.008456562976571047 | 50 |
| SEMICONDUCTORS | Semiconductors | 598.16 | 593.0 | -0.008626454460345045 | 51 |
| LARGE_GROWTH | US Large-Cap Growth | 122.8744994568 | 121.80000305175781 | -0.008744665571719823 | 52 |
| COMMUNICATIONS | Communication Services Sector | 110.795803238 | 109.45999908447266 | -0.0120564508265526 | 53 |
| SOUTH_AFRICA | South Africa Equities | 63.4859935515 | 62.69 | -0.012538097097815615 | 54 |
| CHINA | China Equities | 53.5776002353 | 52.85 | -0.0135803065479706 | 55 |
| TECHNOLOGY | Technology Sector | 183.9617944093 | 181.39999389648438 | -0.013925720397768293 | 56 |
| YEN | Japanese Yen | 57.279998779296875 | 56.46 | -0.01431562145202514 | 57 |
| SOUTH_KOREA | South Korea Equities | 185.64 | 182.72 | -0.015729368670545085 | 58 |
| BITCOIN_ETF | Bitcoin ETF | 35.88999938964844 | 35.23 | -0.018389506850724602 | 59 |
| BROAD_AI_TECH | Broad AI Technology | 64.4395464548 | 62.57 | -0.029012408647403398 | 60 |
| SOFTWARE | Software | 95.6326317603 | 92.48 | -0.0329660671495684 | 61 |
| COPPER | Copper | 38.55 | 37.07 | -0.03839169909208817 | 62 |
| ENERGY | Energy Sector | 57.9176596894 | 55.6 | -0.04001645960539679 | 63 |
| BROAD_COMMODITIES | Broad Commodities | 17.62 | 16.62 | -0.05675368898978428 | 64 |
| GOLD | Gold | 81.38 | 76.74 | -0.05701646596215282 | 65 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 131.68 | 123.81 | -0.05976609963547996 | 66 |
| METALS_MINING | Metals and Mining | 118.5075476692 | 101.94 | -0.13980162441169042 | 67 |
| SILVER | Silver | 61.58 | 52.83 | -0.14209158817797984 | 68 |
| SOLAR | Solar Energy | 63.58 | 54.14 | -0.14847436300723493 | 69 |
| OIL | Crude Oil | 135.15 | 112.21 | -0.16973732889382176 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 25.0 | 0.06786623486192522 | 0.016966558715481306 | Defensive sector with strong recent momentum (+6.4% 30d), reasonable valuation amid sticky inflation and weakening sentiment. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 20.0 | 0.0551576017646922 | 0.01103152035293844 | FY27 $1.5T defense budget tailwind; resilient in geopolitical risk environment. |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 20.0 | -0.008626454460345045 | -0.0017252908920690091 | AI capex acceleration, Q1 global semi sales +25% QoQ, strongest secular momentum into earnings season. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 20.0 | 0.04164443350477698 | 0.008328886700955397 | ISM Manufacturing 54.0 with new orders 56.8 rising; durable goods +8% MoM signals capex cycle. |
| anthropic-claude-opus-4-7 | DIVIDEND | 15.0 | 0.00952107543665659 | 0.0014281613154984885 | Defensive quality tilt with positive recent momentum amid sticky inflation, hot PPI, weak sentiment. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.06786623486192522 | 0.020359870458577567 | Defensive sector with strong recent momentum (+6.4% 30d, +3.25% 7d), low valuation, and resilience during the recent broad-market pullback ahead of FOMC and CPI. |
| anthropic-claude-opus-4-8 | ENERGY | 25.0 | -0.04001645960539679 | -0.010004114901349198 | WTI at $91, EIA forecasting large global inventory draws, strong relative strength (+4.7% 30d, +1.8% 7d) and sticky inflation favoring real-asset cyclicals. |
| anthropic-claude-opus-4-8 | AEROSPACE_DEFENSE | 20.0 | 0.0551576017646922 | 0.01103152035293844 | FY2027 $1.5T defense budget tailwind, steady momentum, lower beta than tech amid elevated geopolitical risk. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 15.0 | 0.04164443350477698 | 0.006246665025716546 | ISM Manufacturing back above 54 with new orders 56.8 and durable goods +8% MoM signal cyclical reacceleration; relative outperformer in the recent selloff. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 10.0 | 0.0028183396106746805 | 0.00028183396106746806 | Cash-like buffer yielding ~4% to dampen volatility into the June FOMC and CPI/PPI prints while preserving optionality. |
| google-gemini-3-1-pro | SP500 | 40.0 | 0.010930608858567004 | 0.0043722435434268014 | Broad US equity exposure provides a baseline for market returns, balancing growth and value. |
| google-gemini-3-1-pro | TECHNOLOGY | 20.0 | -0.013925720397768293 | -0.0027851440795536586 | Technology sector exposure captures ongoing growth in AI and software, despite recent volatility. |
| google-gemini-3-1-pro | HEALTHCARE | 15.0 | 0.06786623486192522 | 0.010179935229288783 | Healthcare offers defensive characteristics and potential upside from policy developments and innovation. |
| google-gemini-3-1-pro | SHORT_TREASURY | 15.0 | 0.0028183396106746805 | 0.00042275094160120207 | Short-term Treasuries provide a cash-like buffer against market volatility while earning a yield. |
| google-gemini-3-1-pro | GOLD | 10.0 | -0.05701646596215282 | -0.005701646596215282 | Gold serves as a hedge against inflation and geopolitical risks, adding diversification. |
| openai-gpt-5-5 | ENERGY | 35.0 | -0.04001645960539679 | -0.014005760861888877 | Energy equities have strong recent relative momentum, high oil sensitivity, and support from elevated WTI plus EIA's forecast for a large 2026 global inventory draw. |
| openai-gpt-5-5 | OIL | 25.0 | -0.16973732889382176 | -0.04243433222345544 | Direct crude exposure targets the near-term commodity catalyst from WTI above $90 and tightening inventory expectations, with weekly EIA reports inside the scoring window. |
| openai-gpt-5-5 | SEMICONDUCTORS | 25.0 | -0.008626454460345045 | -0.0021566136150862614 | Semiconductors retain powerful AI-linked earnings and demand momentum, with Q1 global semiconductor sales up sharply and AI infrastructure capex forecasts still supportive. |
| openai-gpt-5-5 | HEALTHCARE | 10.0 | 0.06786623486192522 | 0.006786623486192522 | Healthcare has positive short-term momentum and offers a defensive ballast if hot inflation or rate volatility pressures broad equities. |
| openai-gpt-5-5 | US_DOLLAR | 5.0 | 0.011773100249732327 | 0.0005886550124866163 | The dollar can hedge hot U.S. inflation surprises, higher-rate repricing, and risk-off moves during the CPI, PPI, PCE, and FOMC-heavy month. |
| xai-grok-4-3 | ENERGY | 40.0 | -0.04001645960539679 | -0.01600658384215872 | High oil prices at $91+ and EIA inventory draw forecasts support sector outperformance over the next month. |
| xai-grok-4-3 | HEALTHCARE | 30.0 | 0.06786623486192522 | 0.020359870458577567 | Strong recent 30-day returns and defensive characteristics amid sticky inflation and upcoming data releases. |
| xai-grok-4-3 | INDUSTRIALS | 30.0 | 0.04164443350477698 | 0.012493330051433093 | ISM manufacturing expansion at 54.0 signals improving factory activity likely to lift the sector before July close. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.55 | 0.06786623486192522 | 0.036029836192804615 | 0.02509922733423761 | 0.23411182085845697 |  | True | True |
| anthropic-claude-opus-4-8 | HEALTHCARE | 5 | 0.55 | 0.06786623486192522 | 0.02791577489695082 | 0.016985166038383816 | 0.24222588215431076 |  | True | True |
| xai-grok-4-3 | ENERGY | 3 | 0.55 | -0.04001645960539679 | 0.016846616667851942 | 0.005916007809284939 | 0.25329504038340966 |  | True | True |
| google-gemini-3-1-pro | SP500 | 5 | 0.75 | 0.010930608858567004 | 0.006488139038547847 | -0.004442469820019157 | 0.26365351801271375 |  | False | True |
| openai-gpt-5-5 | ENERGY | 5 | 0.61 | -0.04001645960539679 | -0.05122142820175144 | -0.062152037060318445 | 0.32136308525301305 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | a177176683a423d0f8c9816abb4b7ba6972bfb56c9bd8a768c2c71ea224b3d45 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 5dada80c93b91910364d1a36d9af22e4444797245fc3790bfce7579f2dc17e54 |
| manifest.yaml | b059ed255060c06ad6792e96ab136c4fde93a350b7446452e0f34b68dac91c62 |
| market_data/universe_trailing_returns.csv | a3fa1ed2b2573c3f609afc99e5e6af35d394cdc7cbc7411c4c1b1ee2c03995e0 |
| market_data/universe_trailing_returns.md | 42e92ab117d34e1be7af0cfc861ab4bd3ef1c3228e1a4b7c784b82490ddb83ab |
| market_data/universe_trailing_returns.json | a54fc5f6c27fea2eafb744e212b452df1b0dc5601e8ab84416d5b8611ee6527d |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 91f379decdaadd80a88a25f872686815a85c1677bd55aa87dd5e520f07e7c2a7 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 11ae6b16c975be615951553a1d7032a45b42b84a1658d51359e751d92d487ebf | yes |
| Final briefing | research/final_briefing.md | model-facing | a177176683a423d0f8c9816abb4b7ba6972bfb56c9bd8a768c2c71ea224b3d45 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
