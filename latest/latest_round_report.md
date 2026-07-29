# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-07-21-1W
- Decision deadline: 2026-07-22T09:30:00Z
- Horizon: one week
- Official run ID: official-v2-2-20260721-1w-r2
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | openai | portfolio | CYBERSECURITY | 4 | 0.58 | Each active holding has a base forecast above SPY's 0.18% forecast. The weighted one-week base return is 0.61%, implying expected alpha of 0.43 percentage point. | Alphabet or Tesla results trigger a broad growth-stock selloff that overwhelms the cybersecurity rebound case.; The recent agriculture advance reverses without a supplied fundamental or scheduled catalyst.; A sharp decline in Treasury yields pressures financials and signals weaker growth expectations.; A broad risk-off move overwhelms the portfolio's cross-cluster diversification. |
| anthropic-claude-fable-5 | anthropic | portfolio | ENERGY | 4 | 0.58 | Tilt toward energy/commodity momentum with confirmed macro support and low-beta sectors with strong prior trends; avoid extended tech into earnings and FOMC risk. | Oil reverses sharply on inventory build or supply news; Strong Alphabet/Tesla earnings drive tech-led SPY rally that our low-beta portfolio lags; Yields fall on soft data, hurting financials; Healthcare-specific policy headlines |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 3 | 0.55 | Overweight energy (oil momentum) and financials (top quality score) versus SPY, with a substantial SPY core for stability. | Oil reverses after sharp run-up (USO up 7.7% active 5d); Financials sensitive to FOMC rate signals; Mega-cap earnings surprises move SPY broadly |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.52 | SPY base forecast set at 0.75%; all other candidates at or below this level; 100% SP500 satisfies rules with no cluster violations. | FOMC statement risk after exit close; Weak June payrolls and downward revisions; Housing market contraction signals |
| openai-gpt-5-5 | openai | portfolio | OIL | 5 | 0.58 | SPY has modest positive base-case return, but several supplied cross-sectional signals show stronger one-week setups. The highest-conviction active views are oil/energy continuation, broad commodity follow-through, cybersecurity rebound after pullback, and financials trend persistence. | Oil and broad commodities reverse after bearish EIA inventory data or geopolitical risk premium fades.; Large-cap technology earnings disappoint and pressure cybersecurity and growth-adjacent sentiment.; A broad risk-off move around the upcoming FOMC meeting start lifts defensive assets and hurts equities and commodities.; The recent commodity and energy strength proves overextended over a one-week horizon. |
| xai-grok-4-5 | xai | portfolio | OIL | 5 | 0.58 | SPY base is modest given mixed macro prints and recent flat-to-negative short-term returns. Higher-conviction active holdings in oil/energy, cybersecurity, Brazil, and biotech offer superior one-week expected returns backed by supplied price context and scheduled data/earnings. | Sharp reversal in crude oil prices after the large recent run-up; Tech earnings disappointment from Alphabet/Tesla spilling into growth and cybersecurity; Risk-off move ahead of FOMC week reducing appetite for EM and biotech; Higher yields or dollar strength pressuring international and commodity exposures |
| google-gemini-3-1-pro | google | portfolio | OIL | 2 | 0.65 | Equal allocation to oil and gold for momentum and hedging. | A sudden reversal in commodity prices.; Unexpectedly strong economic data leading to higher interest rates.; A stronger US dollar negatively impacting commodity prices. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| AEROSPACE_DEFENSE | Aerospace and Defense | 229.74 | 244.98 | 0.06633585792635155 | 1 |
| MATERIALS | Materials Sector | 50.1 | 52.34 | 0.04471057884231544 | 2 |
| HEALTHCARE | Healthcare Sector | 160.25 | 167.25999450683594 | 0.04374411548727575 | 3 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.06 | 87.05999755859375 | 0.03568876467515758 | 4 |
| DIVIDEND | US Dividend Equities | 32.82 | 33.88999938964844 | 0.032602053310433865 | 5 |
| LOW_VOL | US Low Volatility Equities | 75.73 | 77.97000122070312 | 0.02957878279021675 | 6 |
| FINANCIALS | Financials Sector | 56.11 | 57.6 | 0.02655498128675826 | 7 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.76 | 217.69 | 0.023171648806166623 | 8 |
| UNITED_KINGDOM | United Kingdom Equities | 46.77 | 47.82 | 0.022450288646568284 | 9 |
| AUSTRALIA | Australia Equities | 28.68 | 29.32 | 0.02231520223152028 | 10 |
| INDUSTRIALS | Industrials Sector | 178.66 | 182.49 | 0.021437367065935353 | 11 |
| LARGE_VALUE | US Large-Cap Value | 247.44 | 252.0399932861328 | 0.018590338207779 | 12 |
| REAL_ESTATE | Real Estate Sector | 45.2 | 46.01 | 0.01792035398230074 | 13 |
| CANADA | Canada Equities | 59.05 | 59.84 | 0.01337849280270964 | 14 |
| UTILITIES | Utilities Sector | 44.92 | 45.52 | 0.01335707925200369 | 15 |
| MEXICO | Mexico Equities | 75.83999633789062 | 76.78 | 0.012394563653739699 | 16 |
| INDIA | India Equities | 48.78 | 49.38 | 0.012300123001230068 | 17 |
| BRAZIL | Brazil Equities | 35.619998931884766 | 36.05 | 0.012071900084486664 | 18 |
| REGIONAL_BANKS | Regional Banks | 75.98 | 76.79 | 0.010660700184259131 | 19 |
| CHINA | China Equities | 54.0 | 54.41 | 0.007592592592592595 | 20 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.66 | 84.24 | 0.006932823332536531 | 21 |
| SMALL_VALUE | US Small-Cap Value | 222.91 | 224.11000061035156 | 0.005383341305242428 | 22 |
| EUROPE | Europe Equities | 88.76 | 89.23 | 0.005295178008111856 | 23 |
| MID_CAP | US Mid-Cap Stocks | 75.72 | 76.02999877929688 | 0.004094014517919575 | 24 |
| US_DOLLAR | US Dollar | 28.479999542236328 | 28.58 | 0.003511252084655636 | 25 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.83000183105469 | 47.99 | 0.0033451424382222594 | 26 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.41000366210938 | 93.67 | 0.0027833885847077244 | 27 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.31 | 93.56 | 0.0026792412388811915 | 28 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.74 | 97.92 | 0.0018416206261511192 | 29 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.56 | 91.62999725341797 | 0.0007644959962642695 | 30 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 31 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.85 | 106.83 | -0.0001871782873186234 | 32 |
| SOFTWARE | Software | 91.82 | 91.78 | -0.0004356349379219804 | 33 |
| EURO | Euro | 105.2300033569336 | 105.11 | -0.0011403910776905946 | 34 |
| METALS_MINING | Metals and Mining | 101.6 | 101.44 | -0.0015748031496062298 | 35 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.16999816894531 | 106.0 | -0.0016011883948118255 | 36 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.37999725341797 | 95.19 | -0.0019920031336670974 | 37 |
| TIPS | Treasury Inflation-Protected Securities | 107.88 | 107.66 | -0.002039302929180531 | 38 |
| ETHEREUM_ETF | Ethereum ETF | 14.529999732971191 | 14.49 | -0.00275290665562955 | 39 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.65 | 79.42 | -0.0028876333961079803 | 40 |
| COMMUNICATIONS | Communication Services Sector | 110.03 | 109.66999816894531 | -0.003271851595516573 | 41 |
| YEN | Japanese Yen | 56.220001220703125 | 56.0 | -0.003913219778125976 | 42 |
| SOUTH_AFRICA | South Africa Equities | 62.279998779296875 | 61.98 | -0.004816936178178022 | 43 |
| TOTAL_US_MARKET | Total US Stock Market | 369.45 | 365.989990234375 | -0.009365299135539296 | 44 |
| SP500 | S&P 500 | 748.28 | 740.8599853515625 | -0.009916093772969314 | 45 |
| SMALL_CAP | US Small-Cap Stocks | 296.54 | 293.3699951171875 | -0.010689973975897105 | 46 |
| AGRICULTURE | Agriculture Commodities | 28.149999618530273 | 27.84 | -0.01101241999045044 | 47 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.47 | 69.6 | -0.012345679012345734 | 48 |
| CYBERSECURITY | Cybersecurity | 90.58 | 89.28 | -0.014351954073746898 | 49 |
| GOLD | Gold | 76.82 | 75.7 | -0.014579536579015784 | 50 |
| ENERGY | Energy Sector | 58.5 | 57.57 | -0.015897435897435863 | 51 |
| EMERGING_MARKETS | Emerging Markets | 58.86 | 57.74 | -0.01902820251444104 | 52 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.87 | 112.4800033569336 | -0.020806099443426596 | 53 |
| SILVER | Silver | 53.08000183105469 | 51.7 | -0.025998526440278114 | 54 |
| COPPER | Copper | 39.529998779296875 | 38.33 | -0.03035666117767133 | 55 |
| BIOTECH | Biotechnology | 154.5 | 149.78 | -0.03055016181229775 | 56 |
| JAPAN | Japan Equities | 92.74 | 89.83 | -0.031378046150528305 | 57 |
| BROAD_COMMODITIES | Broad Commodities | 17.65 | 17.06 | -0.033427762039660025 | 58 |
| LARGE_GROWTH | US Large-Cap Growth | 121.33 | 116.4800033569336 | -0.0399735979812611 | 59 |
| BITCOIN_ETF | Bitcoin ETF | 37.66999816894531 | 36.14 | -0.04061582806782893 | 60 |
| NASDAQ100 | Nasdaq 100 | 708.97 | 675.489990234375 | -0.04722345059117461 | 61 |
| TECHNOLOGY | Technology Sector | 180.78 | 171.08999633789062 | -0.05360108232165828 | 62 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 120.1 | 113.59 | -0.05420482930890913 | 63 |
| BROAD_AI_TECH | Broad AI Technology | 61.0 | 57.24 | -0.061639344262295004 | 64 |
| OIL | Crude Oil | 128.85000610351562 | 120.49 | -0.06488168961978447 | 65 |
| TAIWAN | Taiwan Equities | 100.58000183105469 | 93.95 | -0.06591769447559936 | 66 |
| MOMENTUM | US Momentum Equities | 314.48 | 292.32000732421875 | -0.07046550710945454 | 67 |
| SOLAR | Solar Energy | 53.74 | 49.1 | -0.08634164495720131 | 68 |
| SEMICONDUCTORS | Semiconductors | 584.08 | 529.6 | -0.09327489385015753 | 69 |
| SOUTH_KOREA | South Korea Equities | 172.9 | 151.45 | -0.12406015037593998 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | portfolio | CYBERSECURITY | 4 | 0.58 | -0.014351954073746898 | 0.00918833390943391 | 0.019104427682403224 | 0.05714752401691764 |  | True | True |
| anthropic-claude-fable-5 | portfolio | ENERGY | 4 | 0.58 | -0.015897435897435863 | 0.006119991016345739 | 0.016036084789315053 | 0.060215866910005814 |  | True | True |
| anthropic-claude-opus-4-8 | portfolio | SP500 | 3 | 0.55 | -0.009916093772969314 | -0.0007691738923910063 | 0.009146919880578308 | 0.06710503181874256 |  | True | False |
| xai-grok-4-3 | portfolio | SP500 | 1 | 0.52 | -0.009916093772969314 | -0.009916093772969314 | 0.0 | 0.07625195169932086 |  | False | False |
| openai-gpt-5-5 | portfolio | OIL | 5 | 0.58 | -0.06488168961978447 | -0.024972605614100935 | -0.01505651184113162 | 0.09130846354045248 |  | False | False |
| xai-grok-4-5 | portfolio | OIL | 5 | 0.58 | -0.06488168961978447 | -0.025836911453226124 | -0.01592081768025681 | 0.09217276937957768 |  | False | False |
| google-gemini-3-1-pro | portfolio | OIL | 2 | 0.65 | -0.06488168961978447 | -0.039730613099400125 | -0.02981451932643081 | 0.10606647102575167 |  | False | False |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1W has no scored official run.
- Round CB-2026-07-22-1W has no scored official run.
- Round CB-2026-07-23-1W has no scored official run.
- Round CB-2026-07-24-1W has no scored official run.
- Round CB-2026-07-27-1W has no scored official run.
