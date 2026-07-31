# CapitalBench Report: CB-2026-07-23-1W / official-v2-2-20260723-1w-r2

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-20260723-1w-r2
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-23-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-23
- Decision deadline: 2026-07-24T09:30:00Z
- Horizon: one week
- Entry date: 2026-07-23
- Exit date: 2026-07-30
- Entry rule: Use adjusted close prices on Thursday, July 23, 2026 as the one-week entry snapshot, calculated after regular trading ends and supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Thursday, July 30, 2026 as the one-week exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | ENERGY | 4 | 0.62 | Selected holdings exceed SPY base forecast; energy cluster at 40% drives alpha in one-week window. | FOMC outcome surprises rates higher; Oil reversal on inventory build; Broader equity selloff extends |
| openai-gpt-5-5 | openai | portfolio | ENERGY | 5 | 0.56 | SPY faces near-term earnings and policy-event risk after a broad down day. Selected holdings have base forecasts above SPY, supported by supplied relative strength, quality evidence, commodity shock data, or defensive rotation potential. | Oil and commodity prices could reverse sharply after the large July move and inventory builds.; The FOMC statement or GDP/personal income data could trigger a broad risk-off move that hurts equities and cyclicals.; Mega-cap technology could rebound after earnings-related declines, causing SPY to outperform equal-weight and defensive tilts.; Energy-price inflation could pressure margins and consumer demand, weakening non-energy equity holdings. |
| openai-gpt-5-6-sol | openai | portfolio | ENERGY | 4 | 0.6 | Energy, aerospace and defense, healthcare, and the dollar each have base forecasts above SPY's. The allocation respects the 50% cluster cap and targets resilience through a catalyst-heavy week. | A rapid de-escalation could reverse crude oil, energy, and defense risk premiums.; A dovish FOMC outcome could weaken the dollar and trigger a growth-led rebound that leaves defensive holdings behind.; The July 30 GDP and inflation-related releases could produce an abrupt rates and factor rotation.; Energy inventories rose and the demand proxy was down year over year, increasing oil reversal risk. |
| xai-grok-4-5 | xai | portfolio | ENERGY | 4 | 0.58 | SPY base is modest after the July 23 selloff; selected sleeves show stronger base forecasts from oil momentum, defense earnings and factor quality. Horizon catalysts are FOMC, GDP and residual commodity momentum. | FOMC hawkish surprise drives rates higher and equities lower; Oil mean-reversion after 7% single-day jump; Growth data (GDP/durables) disappoints cyclical sleeves; Mega-cap earnings (MSFT) dominate and leave cyclicals behind |
| anthropic-claude-fable-5 | anthropic | portfolio | ENERGY | 5 | 0.62 | Overweight energy and inflation-shock beneficiaries with defensive equity ballast; underweight rate-sensitive mega-cap growth that just sold off on Tesla and Alphabet results. | Rapid conflict de-escalation collapses oil, commodities, and gold simultaneously; Dovish FOMC surprise sparks a growth/tech rally that leaves defensive tilts behind; High-volatility oil positioning (USO vol 50.7%) can reverse violently within the week; Strong Microsoft results July 29 lift SPY via mega-cap concentration |
| anthropic-claude-opus-4-8 | anthropic | portfolio | HEALTHCARE | 4 | 0.55 | Overweight defensives and energy given deteriorating breadth and an oil supply shock, while retaining SPY exposure ahead of FOMC. | FOMC surprise triggering risk-on rally hurting defensives; Crude oil reversing sharply, undercutting energy; Mega-cap earnings (MSFT) driving broad rebound above defensives |
| google-gemini-3-1-pro | google | portfolio | OIL | 4 | 0.65 | Overweight energy and gold to capture momentum and hedge against volatility, balanced with core equity exposure. | A hawkish surprise from the FOMC could negatively impact equities and gold.; A sudden reversal in crude oil prices would hurt the energy overweight.; Disappointing mega-cap tech earnings could drag down the broader market. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOFTWARE | Software | 87.1 | 93.31 | 0.07129735935706094 | 1 |
| SOUTH_AFRICA | South Africa Equities | 60.43 | 64.11 | 0.06089690551050797 | 2 |
| AUSTRALIA | Australia Equities | 28.49 | 29.82 | 0.04668304668304679 | 3 |
| INDIA | India Equities | 47.63 | 49.7 | 0.043460004199034286 | 4 |
| UNITED_KINGDOM | United Kingdom Equities | 46.7 | 48.68 | 0.042398286937901375 | 5 |
| CHINA | China Equities | 53.35 | 55.5 | 0.0402999062792877 | 6 |
| EUROPE | Europe Equities | 87.83 | 90.99 | 0.03597859501309353 | 7 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 108.76000213623047 | 112.39 | 0.03337622096791315 | 8 |
| COPPER | Copper | 38.24 | 39.34 | 0.028765690376569175 | 9 |
| ETHEREUM_ETF | Ethereum ETF | 14.11 | 14.51 | 0.028348688873139682 | 10 |
| MEXICO | Mexico Equities | 75.0 | 77.11 | 0.028133333333333344 | 11 |
| YEN | Japanese Yen | 56.01 | 57.58 | 0.02803070880199976 | 12 |
| SILVER | Silver | 52.06 | 53.5 | 0.027660391855551136 | 13 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.20999908447266 | 85.47 | 0.027160208393140817 | 14 |
| MATERIALS | Materials Sector | 50.290000915527344 | 51.64 | 0.026844284348697123 | 15 |
| CYBERSECURITY | Cybersecurity | 87.72 | 90.02 | 0.026219790241678087 | 16 |
| JAPAN | Japan Equities | 91.1 | 93.29 | 0.024039517014270206 | 17 |
| FINANCIALS | Financials Sector | 55.83000183105469 | 57.0 | 0.020956441529158543 | 18 |
| DEVELOPED_EX_US | Developed Markets ex-US | 69.78 | 71.09 | 0.01877328747492113 | 19 |
| DIVIDEND | US Dividend Equities | 32.79999923706055 | 33.41 | 0.01859758466854511 | 20 |
| LARGE_VALUE | US Large-Cap Value | 246.17999267578125 | 250.71 | 0.018401200174641197 | 21 |
| CANADA | Canada Equities | 58.82 | 59.79 | 0.016490989459367444 | 22 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 211.92 | 215.38 | 0.016326915817289622 | 23 |
| GOLD | Gold | 76.15 | 77.3 | 0.0151017728168088 | 24 |
| EURO | Euro | 105.03 | 106.47 | 0.01371036846615259 | 25 |
| HEALTHCARE | Healthcare Sector | 161.44000244140625 | 163.52 | 0.012884028290006233 | 26 |
| COMMUNICATIONS | Communication Services Sector | 105.37999725341797 | 106.58 | 0.0113873863907612 | 27 |
| REGIONAL_BANKS | Regional Banks | 75.15 | 75.9 | 0.009980039920159722 | 28 |
| BRAZIL | Brazil Equities | 36.17 | 36.53 | 0.0099529997235277 | 29 |
| REAL_ESTATE | Real Estate Sector | 44.95000076293945 | 45.3 | 0.007786412260733844 | 30 |
| SMALL_VALUE | US Small-Cap Value | 220.5800018310547 | 221.79 | 0.005485529780129728 | 31 |
| SP500 | S&P 500 | 738.1799926757812 | 741.69 | 0.004754947789218145 | 32 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.26 | 105.76 | 0.004750142504275079 | 33 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 92.88 | 93.29 | 0.004414298018949214 | 34 |
| TOTAL_US_MARKET | Total US Stock Market | 364.69000244140625 | 366.27 | 0.004332440012110306 | 35 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 92.8499984741211 | 93.21 | 0.003877237822241142 | 36 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.71 | 47.88 | 0.003563194298889183 | 37 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.2300033569336 | 79.47 | 0.003029113125051941 | 38 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.33999633789062 | 97.62 | 0.002876553037226559 | 39 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.53 | 94.79 | 0.0027504495927219708 | 40 |
| TIPS | Treasury Inflation-Protected Securities | 107.48999786376953 | 107.74 | 0.002325817668610508 | 41 |
| SMALL_CAP | US Small-Cap Stocks | 292.0899963378906 | 292.59 | 0.0017118137162457359 | 42 |
| EMERGING_MARKETS | Emerging Markets | 58.1 | 58.19 | 0.001549053356282304 | 43 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.26000213623047 | 106.41 | 0.0014116117142293216 | 44 |
| BITCOIN_ETF | Bitcoin ETF | 36.65 | 36.7 | 0.0013642564802183177 | 45 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.58000183105469 | 91.65 | 0.0007643390210283485 | 46 |
| LOW_VOL | US Low Volatility Equities | 76.36000061035156 | 76.38 | 0.00026190923898083973 | 47 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 48 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 238.23 | 238.13 | -0.00041976241447339024 | 49 |
| MID_CAP | US Mid-Cap Stocks | 75.44999694824219 | 75.35 | -0.001325340653238083 | 50 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.16999816894531 | 82.8 | -0.004448697572335236 | 51 |
| BIOTECH | Biotechnology | 152.23 | 151.46 | -0.005058135715693246 | 52 |
| ENERGY | Energy Sector | 59.380001068115234 | 58.96 | -0.007073106442578969 | 53 |
| LARGE_GROWTH | US Large-Cap Growth | 118.58999633789062 | 117.43 | -0.009781569893851039 | 54 |
| BROAD_AI_TECH | Broad AI Technology | 59.33 | 58.69 | -0.010787122872071508 | 55 |
| NASDAQ100 | Nasdaq 100 | 691.9600219726562 | 683.55 | -0.012153913095558355 | 56 |
| METALS_MINING | Metals and Mining | 103.17 | 101.86 | -0.012697489580304366 | 57 |
| US_DOLLAR | US Dollar | 28.56 | 28.14 | -0.014705882352941124 | 58 |
| TECHNOLOGY | Technology Sector | 178.4499969482422 | 175.73 | -0.015242347967263425 | 59 |
| INDUSTRIALS | Industrials Sector | 181.94000244140625 | 178.39 | -0.01951194016582225 | 60 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 116.85 | 113.98 | -0.024561403508771895 | 61 |
| AGRICULTURE | Agriculture Commodities | 28.24 | 27.48 | -0.026912181303116123 | 62 |
| BROAD_COMMODITIES | Broad Commodities | 18.06 | 17.5 | -0.03100775193798444 | 63 |
| UTILITIES | Utilities Sector | 46.189998626708984 | 44.66 | -0.033124024078759695 | 64 |
| MOMENTUM | US Momentum Equities | 313.9800109863281 | 298.77 | -0.048442609255754276 | 65 |
| SOLAR | Solar Energy | 52.85 | 49.84 | -0.05695364238410594 | 66 |
| TAIWAN | Taiwan Equities | 99.84 | 94.0 | -0.05849358974358976 | 67 |
| SEMICONDUCTORS | Semiconductors | 580.17 | 538.9 | -0.07113432269851938 | 68 |
| SOUTH_KOREA | South Korea Equities | 173.86 | 161.21 | -0.0727596917059703 | 69 |
| OIL | Crude Oil | 139.49 | 127.48 | -0.08609936196143098 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 30.0 | -0.007073106442578969 | -0.002121931932773691 | Brent at $100.69 amid war-driven supply shock; XLE +5.81% active over 5 sessions with negative SPY beta gives hedge plus carry. |
| anthropic-claude-fable-5 | BROAD_COMMODITIES | 20.0 | -0.03100775193798444 | -0.006201550387596889 | Broad commodity strength (+8.16% active 5s, volume z-score 3.75) benefits from energy shock spillover into the complex; negative equity correlation. |
| anthropic-claude-fable-5 | LOW_VOL | 20.0 | 0.00026190923898083973 | 5.238184779616795e-05 | Defensive equity with +1.10% recent active return and negative SPY beta; likely to outperform in risk-off, oil-shock tape into FOMC. |
| anthropic-claude-fable-5 | LARGE_VALUE | 15.0 | 0.018401200174641197 | 0.0027601800261961794 | Value tilt with energy/financials weight, top quality-evidence rank (0.792), shallow drawdown, and positive prior active trend. |
| anthropic-claude-fable-5 | GOLD | 15.0 | 0.0151017728168088 | 0.00226526592252132 | Safe-haven demand during war and equity risk-off; IAU +3.48% active over 5 sessions. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.012884028290006233 | 0.0038652084870018696 | Defensive sector with strong prior rank, low beta to SPY (-0.18), and shallow drawdown; benefits during equity pullback. |
| anthropic-claude-opus-4-8 | ENERGY | 25.0 | -0.007073106442578969 | -0.0017682766106447423 | Brent surged 7% to $100 with strong active return; energy sector negative-beta and momentum supported by oil supply shock. |
| anthropic-claude-opus-4-8 | UTILITIES | 25.0 | -0.033124024078759695 | -0.008281006019689924 | Defensive, low correlation to SPY, strong 3-session return of 2.78% and shallow drawdown amid risk-off. |
| anthropic-claude-opus-4-8 | SP500 | 20.0 | 0.004754947789218145 | 0.000950989557843629 | Core benchmark exposure to limit tracking error. |
| google-gemini-3-1-pro | OIL | 25.0 | -0.08609936196143098 | -0.021524840490357744 | Strong recent momentum and tight inventories support continued strength in crude oil. |
| google-gemini-3-1-pro | ENERGY | 25.0 | -0.007073106442578969 | -0.0017682766106447423 | Energy equities should benefit from the underlying strength in crude oil prices. |
| google-gemini-3-1-pro | GOLD | 25.0 | 0.0151017728168088 | 0.0037754432042022 | Gold offers a hedge against volatility and potential dovish signals from the Fed. |
| google-gemini-3-1-pro | SP500 | 25.0 | 0.004754947789218145 | 0.0011887369473045362 | Maintains diversified equity exposure while tilting toward specific sectors. |
| openai-gpt-5-5 | ENERGY | 30.0 | -0.007073106442578969 | -0.002121931932773691 | Energy equities have direct support from the sharp crude move and positive recent relative strength, while avoiding the full volatility of crude oil itself. |
| openai-gpt-5-5 | BROAD_COMMODITIES | 20.0 | -0.03100775193798444 | -0.006201550387596889 | Commodity exposure is supported by the large energy shock and very strong short-term relative performance, with diversification beyond single-sector equities. |
| openai-gpt-5-5 | HEALTHCARE | 20.0 | 0.012884028290006233 | 0.002576805658001247 | Healthcare combines strong prior active return and high quality evidence with defensive characteristics during a weak equity tape. |
| openai-gpt-5-5 | FINANCIALS | 15.0 | 0.020956441529158543 | 0.0031434662293737814 | Financials have one of the highest quality evidence scores and a strong prior active trend, with potential support if firm labor data and rates sustain bank earnings expectations. |
| openai-gpt-5-5 | EQUAL_WEIGHT_SP500 | 15.0 | 0.016326915817289622 | 0.0024490373725934433 | Equal-weight S&P offers broad US equity exposure with better recent breadth than cap-weighted SPY and less dependence on the mega-cap names that led the July 23 decline. |
| openai-gpt-5-6-sol | ENERGY | 30.0 | -0.007073106442578969 | -0.002121931932773691 | Energy has positive prior and recent active returns, while crude near $100 provides fundamental support despite reversal risk after the sharp surge. |
| openai-gpt-5-6-sol | AEROSPACE_DEFENSE | 30.0 | -0.00041976241447339024 | -0.00012592872434201706 | Strong RTX results and geopolitical demand support provide independent backing for recent aerospace and defense strength. |
| openai-gpt-5-6-sol | HEALTHCARE | 25.0 | 0.012884028290006233 | 0.0032210070725015583 | Healthcare combines strong prior relative performance with defensive characteristics during weak market breadth and event risk. |
| openai-gpt-5-6-sol | US_DOLLAR | 15.0 | -0.014705882352941124 | -0.0022058823529411686 | Recent dollar strength, high Treasury yields, and major policy and economic releases provide a lower-beta source of prospective alpha. |
| xai-grok-4-3 | ENERGY | 40.0 | -0.007073106442578969 | -0.002829242577031588 | Brent crude surge and inventory data support near-term strength |
| xai-grok-4-3 | FINANCIALS | 20.0 | 0.020956441529158543 | 0.0041912883058317085 | Strong prior active rank and low drawdown support outperformance |
| xai-grok-4-3 | HEALTHCARE | 20.0 | 0.012884028290006233 | 0.002576805658001247 | High prior active rank with positive recent relative performance |
| xai-grok-4-3 | AEROSPACE_DEFENSE | 20.0 | -0.00041976241447339024 | -8.395248289467806e-05 | RTX earnings beat and defense segment strength |
| xai-grok-4-5 | ENERGY | 30.0 | -0.007073106442578969 | -0.002121931932773691 | Oil price spike and energy sector momentum supported by elevated Brent and product demand proxies into FOMC week. |
| xai-grok-4-5 | AEROSPACE_DEFENSE | 25.0 | -0.00041976241447339024 | -0.00010494060361834756 | RTX beat on sales/EPS/cash flow provides near-term fundamental support for defense names into month-end. |
| xai-grok-4-5 | FINANCIALS | 25.0 | 0.020956441529158543 | 0.005239110382289636 | High quality evidence score, positive prior active trend, and rate backdrop favor banks/insurers vs mega-cap growth. |
| xai-grok-4-5 | BROAD_COMMODITIES | 20.0 | -0.03100775193798444 | -0.006201550387596889 | Strong recent active return and volume confirmation alongside energy complex strength. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | ENERGY | 4 | 0.62 | -0.007073106442578969 | 0.003854898903906689 | -0.0009000488853114557 | 0.06744246045315425 |  | False | True |
| openai-gpt-5-5 | ENERGY | 5 | 0.56 | -0.007073106442578969 | -0.00015417306040210743 | -0.004909120849620252 | 0.07145153241746305 |  | False | False |
| openai-gpt-5-6-sol | ENERGY | 4 | 0.6 | -0.007073106442578969 | -0.001232735937555318 | -0.005987683726773463 | 0.07253009529461626 |  | False | False |
| xai-grok-4-5 | ENERGY | 4 | 0.58 | -0.007073106442578969 | -0.0031893125416992915 | -0.007944260330917436 | 0.07448667189876024 |  | False | False |
| anthropic-claude-fable-5 | ENERGY | 5 | 0.62 | -0.007073106442578969 | -0.003245654523856912 | -0.008000602313075056 | 0.07454301388091786 |  | False | False |
| anthropic-claude-opus-4-8 | HEALTHCARE | 4 | 0.55 | 0.012884028290006233 | -0.005233084585489167 | -0.009988032374707311 | 0.07653044394255011 |  | False | False |
| google-gemini-3-1-pro | OIL | 4 | 0.65 | -0.08609936196143098 | -0.01832893694949575 | -0.023083884738713895 | 0.08962629630655669 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | -0.008000602313075056 | 0.47625000000000006 | -0.016799164961837386 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 35719b1e1aed21a35150d8f2f577abb191a027721c728526b6a206f5634efe48 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 1a844da9c59ab06e30e88b53a60f08b23075e0cfd4df40bd80afc8570a93c261 |
| manifest.yaml | 435f674a1d39cbef04290f2ec666adea07ce9b1c3ac215a45371a1adcbb6db0b |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 0a5a27ee6caa4513e6c30ebf0629b0622dc1bf8021833965c829f492d446cb9c |
| market_data/universe_decision_context.md | 99b4d13457e4d64372f24c599347c369392a0bdee03178a78f69edd13194a9ad |
| market_data/universe_decision_context.json | b23ddc77c3a01a5a78c7d94db5fafc83adcc431c09f8ee63f1ffc60ef5797b15 |
| market_data/decision_context_source_history.json | 335b896989b7fa7ffc368da09a75944b6c2f167dc687e70f2b71bdc4afb19895 |
| market_data/universe_quality_evidence.md | 9105b736586b042c68d975a21554837d8121cf9c26898daaf7f4930a109d8629 |
| market_data/universe_quality_evidence.json | be880356a4b19b318f2350a7252dcd93ce3f81235666c4825d45c32dc18bf772 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 27d0418fae50529e59d35ed261eabed009bc5862e1baaf622e230bb5fc925c45 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | c3734f1f0a8a4f49e610c11199ec52d8c72a482fdac355c53365889bb75c68a4 | yes |
| Final briefing | research/final_briefing.md | model-facing | 35719b1e1aed21a35150d8f2f577abb191a027721c728526b6a206f5634efe48 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
