# CapitalBench Report: CB-2026-07-21-1W / official-v2-2-20260721-1w-r2

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-20260721-1w-r2
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-21-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-21
- Decision deadline: 2026-07-22T09:30:00Z
- Horizon: one week
- Entry date: 2026-07-21
- Exit date: 2026-07-28
- Entry rule: Use adjusted close prices on Tuesday, July 21, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Tuesday, July 28, 2026 as the one-week exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

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

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 30.0 | -0.015897435897435863 | -0.004769230769230759 | Oil rallying hard (Brent $91, USO +7.7% active 5d), energy shows strong prior 16d active return (+6.0%) and negative SPY beta gives diversification. |
| anthropic-claude-fable-5 | BROAD_COMMODITIES | 20.0 | -0.033427762039660025 | -0.006685552407932005 | Broad commodities +3.8% active with huge volume z-score 3.77; inflation prints (PPI +5.5% y/y) support commodity complex. |
| anthropic-claude-fable-5 | HEALTHCARE | 25.0 | 0.04374411548727575 | 0.010936028871818937 | Defensive sector with strong prior trend (+5.7% prior 16d active), low SPY correlation, cushions FOMC-eve risk. |
| anthropic-claude-fable-5 | FINANCIALS | 25.0 | 0.02655498128675826 | 0.006638745321689565 | Financials show +4.6% prior 16d active trend, rising 10y yield (4.63%) supportive, low beta to SPY drawdown. |
| anthropic-claude-opus-4-8 | ENERGY | 30.0 | -0.015897435897435863 | -0.004769230769230759 | Strong prior active trend, Brent up 2% to $91, oil momentum positive, low beta to SPY diversifies. |
| anthropic-claude-opus-4-8 | FINANCIALS | 30.0 | 0.02655498128675826 | 0.007966494386027478 | Highest quality evidence in cluster (0.698), strong prior active return, low volatility, defensive to rates. |
| anthropic-claude-opus-4-8 | SP500 | 40.0 | -0.009916093772969314 | -0.003966437509187726 | Core broad exposure; index rose 0.9% with broad participation. |
| google-gemini-3-1-pro | OIL | 50.0 | -0.06488168961978447 | -0.03244084480989223 | Strong recent momentum and tight supply dynamics support continued outperformance. |
| google-gemini-3-1-pro | GOLD | 50.0 | -0.014579536579015784 | -0.007289768289507892 | Safe-haven demand and potential for a weaker dollar support gold. |
| openai-gpt-5-5 | OIL | 25.0 | -0.06488168961978447 | -0.016220422404946117 | Crude has the clearest near-window catalyst and strongest supplied short-term price impulse, while position size is capped for volatility. |
| openai-gpt-5-5 | ENERGY | 20.0 | -0.015897435897435863 | -0.003179487179487173 | Energy equities offer oil-linked upside with somewhat less direct commodity-ETP volatility and strong prior relative trend evidence. |
| openai-gpt-5-5 | BROAD_COMMODITIES | 20.0 | -0.033427762039660025 | -0.006685552407932005 | Broad commodities diversify the energy overweight and show strong recent active performance, high volume confirmation, and positive prior trend evidence. |
| openai-gpt-5-5 | CYBERSECURITY | 20.0 | -0.014351954073746898 | -0.0028703908147493795 | Cybersecurity has the highest quality evidence score and the strongest prior active rank, with recent pullback creating a rebound setup into tech earnings week. |
| openai-gpt-5-5 | FINANCIALS | 15.0 | 0.02655498128675826 | 0.003983247193013739 | Financials provide a non-commodity equity diversifier with strong prior active trend, moderate volatility, and support from higher Treasury yields. |
| openai-gpt-5-6-sol | CYBERSECURITY | 30.0 | -0.014351954073746898 | -0.004305586222124069 | Highest quality evidence score, combining the strongest prior active rank with the deepest recent relative pullback, supports a one-week rebound position. |
| openai-gpt-5-6-sol | HEALTHCARE | 25.0 | 0.04374411548727575 | 0.010936028871818937 | Strong prior and recent benchmark-relative performance provide a comparatively defensive continuation opportunity. |
| openai-gpt-5-6-sol | AGRICULTURE | 25.0 | -0.01101241999045044 | -0.00275310499761261 | Positive recent and prior performance with near-zero SPY correlation offers independently sourced return potential, though briefing support is limited. |
| openai-gpt-5-6-sol | FINANCIALS | 20.0 | 0.02655498128675826 | 0.005310996257351652 | Strong prior active return and a high quality score support continued relative strength, with elevated Treasury yields providing a possible tailwind. |
| xai-grok-4-3 | SP500 | 100.0 | -0.009916093772969314 | -0.009916093772969314 | No active option clears the base-forecast hurdle above SPY; broad US equity exposure matches the benchmark. |
| xai-grok-4-5 | OIL | 25.0 | -0.06488168961978447 | -0.016220422404946117 | Strong recent price action and elevated crude levels support continued upside into inventory data and energy-sensitive flows over the one-week window. |
| xai-grok-4-5 | ENERGY | 25.0 | -0.015897435897435863 | -0.003974358974358966 | Sector benefits from oil strength, positive prior active returns, and defensive positioning amid sticky inflation readings. |
| xai-grok-4-5 | CYBERSECURITY | 20.0 | -0.014351954073746898 | -0.0028703908147493795 | Highest quality evidence score with strong prior active trend and recent pullback creates favorable risk-reward into tech earnings. |
| xai-grok-4-5 | BRAZIL | 15.0 | 0.012071900084486664 | 0.0018107850126729995 | Elevated quality score and solid prior active return support continuation in EM commodity-linked equities. |
| xai-grok-4-5 | BIOTECH | 15.0 | -0.03055016181229775 | -0.004582524271844662 | Strong prior active performance and quality ranking favor relative strength in healthcare risk assets. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-6-sol | CYBERSECURITY | 4 | 0.58 | -0.014351954073746898 | 0.00918833390943391 | 0.019104427682403224 | 0.05714752401691764 |  | True | True |
| anthropic-claude-fable-5 | ENERGY | 4 | 0.58 | -0.015897435897435863 | 0.006119991016345739 | 0.016036084789315053 | 0.060215866910005814 |  | True | True |
| anthropic-claude-opus-4-8 | SP500 | 3 | 0.55 | -0.009916093772969314 | -0.0007691738923910063 | 0.009146919880578308 | 0.06710503181874256 |  | True | False |
| xai-grok-4-3 | SP500 | 1 | 0.52 | -0.009916093772969314 | -0.009916093772969314 | 0.0 | 0.07625195169932086 |  | False | False |
| openai-gpt-5-5 | OIL | 5 | 0.58 | -0.06488168961978447 | -0.024972605614100935 | -0.01505651184113162 | 0.09130846354045248 |  | False | False |
| xai-grok-4-5 | OIL | 5 | 0.58 | -0.06488168961978447 | -0.025836911453226124 | -0.01592081768025681 | 0.09217276937957768 |  | False | False |
| google-gemini-3-1-pro | OIL | 2 | 0.65 | -0.06488168961978447 | -0.039730613099400125 | -0.02981451932643081 | 0.10606647102575167 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | ENERGY | 0.016036084789315053 | 0.43624999999999997 | 0.03675893361447577 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | fc2dc9655a8f43dc8da3387505b3828e0c0ae6e49f64710c1f4a21f997b4ccf6 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 1a844da9c59ab06e30e88b53a60f08b23075e0cfd4df40bd80afc8570a93c261 |
| manifest.yaml | fa0f9e24dc7ec42c0fef700b00ceb0a622ab44d640abfac94f0ee2bffcd92130 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | 2e45d037441cd230a0a31f14a93301ad78b3265225dfba6e6e28d01cf22360b1 |
| market_data/universe_decision_context.md | ac0e9ebf2dfeb0f90366bd3a172d6c980c712e02e0041b6f1a3ab386b26d51d6 |
| market_data/universe_decision_context.json | 6520a0039fb5cbfac86ec5669aec50a0b7700fcb47ac845175bc7935db7bfb05 |
| market_data/decision_context_source_history.json | 24231ddb874b42bc944bb41c85c1f5e4c0c57358214241e9eecba1fd2d073291 |
| market_data/universe_quality_evidence.md | 837b1ad2c0e258ce9b0e35af2fa61a008fbc191ebc9d018ca7ff3f958a42ba8f |
| market_data/universe_quality_evidence.json | 5d8772cd67401ebe6b21805e4dc81e8b95f85f5c1eac4af5a41ef90e5235f025 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | c0289177d43870b9cf3a688be39261150d06660f1549b83ca613c45e445763dd | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | b9e8ccbe67113574a2c2693f17c9224d26b554159f1bb615c45010f7508223b7 | yes |
| Final briefing | research/final_briefing.md | model-facing | fc2dc9655a8f43dc8da3387505b3828e0c0ae6e49f64710c1f4a21f997b4ccf6 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
