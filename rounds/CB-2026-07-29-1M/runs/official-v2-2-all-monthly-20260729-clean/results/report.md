# CapitalBench Report: CB-2026-07-29-1M / official-v2-2-all-monthly-20260729-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-monthly-20260729-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-29-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-29
- Decision deadline: 2026-07-30T12:30:00Z
- Horizon: one month
- Entry date: 2026-07-29
- Exit date: 2026-08-28
- Entry rule: Use the Wednesday, July 29, 2026 adjusted close supplied in prices/entry_prices.csv.
- Exit rule: Use the Friday, August 28, 2026 adjusted close supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | anthropic | portfolio | LARGE_VALUE | 5 | 0.6 | Overweight value, breadth, healthcare, and energy versus concentrated growth during an ongoing tech correction with elevated rates and geopolitical oil risk. | Rapid tech rebound (e.g., strong Apple/Amazon or Nvidia results) reverses breadth rotation and value/defensive leadership; Middle East de-escalation cuts oil prices, hurting the energy sleeve; Hotter CPI/PPI in mid-August triggers rate-hike fears and a broad equity selloff; Weak payrolls could hit cyclical value and energy demand expectations |
| xai-grok-4-5 | xai | portfolio | HEALTHCARE | 4 | 0.58 | SPY base is modest given the late-July decline and mixed macro prints; selected holdings show stronger recent active returns, shallower relative drawdowns in several cases, and catalysts that can sustain rotation. Equal-weight and value capture breadth, healthcare adds defense, energy retains geopolitical support. | Sharp reversal back into mega-cap tech/growth if Nvidia or AI-related earnings surprise positively; Escalation or de-escalation in Middle East conflict causing oil volatility that hurts energy allocation; Hotter-than-expected inflation or labor data prompting rate-hike fears and broad equity pressure; Failure of equal-weight/value leadership if market breadth collapses again |
| anthropic-claude-opus-4-8 | anthropic | portfolio | DIVIDEND | 4 | 0.6 | Defensive equity tilt favoring dividends, financials, and healthcare over vulnerable mega-cap tech during a breadth-narrowing selloff. | Sharp tech-led rebound leaving defensives behind and lagging SPY; August CPI/PPI surprise triggering rate-hike repricing that hurts financials and rate-sensitives; Middle East conflict escalation spiking oil and broad risk-off |
| google-gemini-3-1-pro | google | portfolio | DIVIDEND | 2 | 0.65 | Defensive positioning with a focus on dividend equities and healthcare. | A sudden shift in market sentiment favoring high-growth technology stocks.; Unexpectedly strong economic data leading to higher interest rates.; Sector-specific risks in healthcare, such as regulatory changes or negative clinical trial results. |
| openai-gpt-5-5 | openai | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.58 | Base case is a one-month continuation of rotation away from cap-weighted growth into equal-weight, dividend, defensive healthcare, financials, and geopolitically supported oil. Main expected alpha source is SPY’s recent weakness and Nasdaq drawdown versus stronger breadth in non-mega-cap and defensive/value areas. | Mega-cap technology rebounds sharply after Apple, Amazon, or Nvidia results, causing SPY to outperform the active portfolio.; Inflation or GDP data reprice rates higher and pressure dividend, healthcare, and financial exposures simultaneously.; Oil reverses if Middle East tensions ease or demand concerns dominate, hurting the energy allocation.; Weak payrolls or loan survey deterioration could damage financials and broader cyclical risk appetite. |
| anthropic-claude-opus-5 | anthropic | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.55 | Tilt away from cap-weighted tech concentration into equal-weight, financials, healthcare and dividend equity, plus a geopolitical oil hedge. | Sharp V-shaped rebound in semis/mega-cap tech would leave defensives lagging SPY; Hot July CPI (August 12) with three FOMC hawks dissenting could pressure financials and rate-sensitive defensives; Middle East de-escalation would sink oil sleeve quickly; Weak payrolls August 7 could hit cyclical financials harder than mega-caps; Concentration in defensive factors underperforms in a broad risk-on melt-up |
| xai-grok-4-3 | xai | portfolio | DIVIDEND | 4 | 0.58 | Four holdings in defensive and diversified equity clusters with base returns above SPY forecast; 100% allocation in 25% increments. | Inflation reacceleration from energy prices; Stronger than expected GDP boosting growth stocks; FOMC signaling further rate hikes |
| openai-gpt-5-6-sol | openai | portfolio | EQUAL_WEIGHT_SP500 | 4 | 0.61 | SPY faces concentrated growth weakness and elevated policy uncertainty. Equal weight, healthcare, real estate, and the dollar offer stronger one-month base cases supported by relative strength, defensiveness, or event-driven rate sensitivity. | A sharp mega-cap technology rebound could restore SPY leadership and hurt equal-weight alpha.; Hot July inflation or hawkish Federal Reserve minutes could pressure real estate and equities.; A rapid de-escalation in the Middle East or dovish U.S. data could weaken the dollar.; Recent defensive-sector strength could reverse if risk appetite broadens into high-beta growth. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.24 | 18.37 | 0.2900280898876404 | 1 |
| SOUTH_KOREA | South Korea Equities | 144.21 | 180.2 | 0.24956660425767963 | 2 |
| BITCOIN_ETF | Bitcoin ETF | 36.0 | 43.9 | 0.21944444444444433 | 3 |
| METALS_MINING | Metals and Mining | 97.58 | 118.74 | 0.21684771469563424 | 4 |
| TAIWAN | Taiwan Equities | 89.41 | 107.9 | 0.20680013421317534 | 5 |
| SOFTWARE | Software | 92.37 | 109.5 | 0.18544982137057486 | 6 |
| SILVER | Silver | 51.77 | 60.02 | 0.15935870195093682 | 7 |
| BROAD_AI_TECH | Broad AI Technology | 55.98 | 64.22 | 0.14719542693819232 | 8 |
| SOUTH_AFRICA | South Africa Equities | 62.08 | 70.72 | 0.1391752577319587 | 9 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 109.56 | 122.32 | 0.11646586345381515 | 10 |
| TECHNOLOGY | Technology Sector | 166.57 | 185.69 | 0.11478657621420418 | 11 |
| CYBERSECURITY | Cybersecurity | 88.79 | 98.56 | 0.11003491384164876 | 12 |
| GOLD | Gold | 76.04 | 83.82 | 0.10231457127827448 | 13 |
| BIOTECH | Biotechnology | 147.91 | 162.38 | 0.09782976134135613 | 14 |
| SEMICONDUCTORS | Semiconductors | 504.22 | 553.11 | 0.09696164372694449 | 15 |
| NASDAQ100 | Nasdaq 100 | 661.73 | 716.43 | 0.08266211294636783 | 16 |
| LARGE_GROWTH | US Large-Cap Growth | 114.05 | 122.75 | 0.07628233231039028 | 17 |
| JAPAN | Japan Equities | 89.35 | 95.87 | 0.07297146054840531 | 18 |
| ENERGY | Energy Sector | 58.65 | 62.68 | 0.06871270247229333 | 19 |
| EMERGING_MARKETS | Emerging Markets | 56.92 | 60.79 | 0.06799016163035843 | 20 |
| AGRICULTURE | Agriculture Commodities | 27.49 | 29.19 | 0.06184066933430343 | 21 |
| DEVELOPED_EX_US | Developed Markets ex-US | 68.95 | 73.06 | 0.05960841189267585 | 22 |
| MOMENTUM | US Momentum Equities | 283.11 | 299.71 | 0.05863445303945447 | 23 |
| SP500 | S&P 500 | 729.46 | 769.35 | 0.054684287006826926 | 24 |
| TOTAL_US_MARKET | Total US Stock Market | 360.42 | 379.36 | 0.05254980300760215 | 25 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 111.61 | 117.21 | 0.050174715527282476 | 26 |
| BROAD_COMMODITIES | Broad Commodities | 17.57 | 18.39 | 0.04667046101309058 | 27 |
| CANADA | Canada Equities | 59.29 | 61.73 | 0.041153651543262004 | 28 |
| LARGE_VALUE | US Large-Cap Value | 249.52 | 258.33 | 0.03530779095864056 | 29 |
| EUROPE | Europe Equities | 88.86 | 91.98 | 0.035111411208642807 | 30 |
| COPPER | Copper | 38.35 | 39.67 | 0.034419817470664915 | 31 |
| COMMUNICATIONS | Communication Services Sector | 109.51 | 112.99 | 0.031777919824673484 | 32 |
| DIVIDEND | US Dividend Equities | 33.83 | 34.9 | 0.03162873189476789 | 33 |
| AUSTRALIA | Australia Equities | 29.11 | 30.0 | 0.030573686018550372 | 34 |
| HEALTHCARE | Healthcare Sector | 166.24 | 171.16 | 0.029595765158806575 | 35 |
| MATERIALS | Materials Sector | 51.74 | 53.18 | 0.02783146501739453 | 36 |
| FINANCIALS | Financials Sector | 56.68 | 58.1 | 0.025052928722653522 | 37 |
| SMALL_CAP | US Small-Cap Stocks | 288.57 | 295.75 | 0.024881311293620367 | 38 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 215.73 | 220.69 | 0.02299170259120209 | 39 |
| SOLAR | Solar Energy | 47.68 | 48.65 | 0.02034395973154357 | 40 |
| YEN | Japanese Yen | 56.13 | 57.25 | 0.01995367895955802 | 41 |
| MID_CAP | US Mid-Cap Stocks | 74.73 | 75.76 | 0.0137829519603907 | 42 |
| UNITED_KINGDOM | United Kingdom Equities | 47.9 | 48.55 | 0.013569937369519725 | 43 |
| EURO | Euro | 105.7 | 106.978 | 0.012090823084200508 | 44 |
| MEXICO | Mexico Equities | 75.57 | 76.48 | 0.01204181553526551 | 45 |
| INDIA | India Equities | 49.17 | 49.56 | 0.007931665649786535 | 46 |
| SMALL_VALUE | US Small-Cap Value | 221.6 | 223.14 | 0.006949458483754389 | 47 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.24 | 79.74 | 0.00630994447248856 | 48 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.56 | 94.89 | 0.0034898477157361274 | 49 |
| OIL | Crude Oil | 129.31 | 129.7 | 0.0030160080426879787 | 50 |
| CHINA | China Equities | 55.07 | 55.23 | 0.0029053931360085716 | 51 |
| INDUSTRIALS | Industrials Sector | 176.66 | 177.14 | 0.002717083663534403 | 52 |
| BRAZIL | Brazil Equities | 35.47 | 35.55 | 0.0022554271215111665 | 53 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.22 | 106.35 | 0.0012238749764639234 | 54 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 82.85 | 82.88 | 0.00036210018105009567 | 55 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.64 | 91.65 | 0.00010912265386298081 | 56 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 57 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.55 | 97.49 | -0.0006150691952845344 | 58 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.23 | 93.17 | -0.0006435696664164325 | 59 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.17 | 92.85 | -0.0034345819469787653 | 60 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.81 | 47.6 | -0.004392386530014614 | 61 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.77 | 105.22 | -0.005199962182093176 | 62 |
| TIPS | Treasury Inflation-Protected Securities | 107.77 | 106.94 | -0.0077015867124431425 | 63 |
| US_DOLLAR | US Dollar | 28.42 | 28.18 | -0.008444757213230236 | 64 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 236.26 | 232.82 | -0.014560230254804019 | 65 |
| CONSUMER_STAPLES | Consumer Staples Sector | 87.36 | 85.45 | -0.021863553113553036 | 66 |
| REGIONAL_BANKS | Regional Banks | 76.18 | 74.3 | -0.02467839327907595 | 67 |
| LOW_VOL | US Low Volatility Equities | 77.54 | 75.08 | -0.03172556100077395 | 68 |
| REAL_ESTATE | Real Estate Sector | 45.96 | 44.48 | -0.03220191470844225 | 69 |
| UTILITIES | Utilities Sector | 44.91 | 42.73 | -0.04854152749944329 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | LARGE_VALUE | 25.0 | 0.03530779095864056 | 0.00882694773966014 | Value showing positive 5-day return (+0.81%) and +4.35% active return while growth corrects; low drawdown and shallow distance to 52w high suggest defensive leadership in a risk-off tape. |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 25.0 | 0.02299170259120209 | 0.0057479256478005225 | Breadth rotation is strong: RSP beat SPY by 3.83% over 5 days and 2.82% over 21 days as mega-cap tech corrects; low volatility (11.2%) and shallow drawdown (-2.0%). |
| anthropic-claude-fable-5 | HEALTHCARE | 20.0 | 0.029595765158806575 | 0.005919153031761316 | Best 5-day sector return (+4.27%), low beta (0.32), near 52-week high, defensive characteristics suited to elevated policy uncertainty and weakening labor data. |
| anthropic-claude-fable-5 | ENERGY | 15.0 | 0.06871270247229333 | 0.010306905370844 | Brent up 7.3% to $88.09 with unresolved Strait of Hormuz risk; XLE +11.02% active over 21 days with negative SPY beta provides geopolitical hedge. |
| anthropic-claude-fable-5 | SP500 | 15.0 | 0.054684287006826926 | 0.008202643051024038 | Benchmark ballast maintaining core beta while tilts play out. |
| anthropic-claude-opus-4-8 | DIVIDEND | 30.0 | 0.03162873189476789 | 0.009488619568430367 | Strong defensive equity, low beta (0.27), positive recent returns while market sold off, near 52w high. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | 0.025052928722653522 | 0.006263232180663381 | Best breadth-leading sector with +7% active 21s, minimal drawdown, low volatility, near highs. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 25.0 | 0.029595765158806575 | 0.007398941289701644 | Defensive sector with best recent 5s return (+4.27%), low beta, shallow drawdown. |
| anthropic-claude-opus-4-8 | SP500 | 20.0 | 0.054684287006826926 | 0.010936857401365387 | Core benchmark exposure to limit tracking error. |
| anthropic-claude-opus-5 | EQUAL_WEIGHT_SP500 | 30.0 | 0.02299170259120209 | 0.006897510777360627 | Broad large-cap with far lower concentration in the de-rating mega-cap tech complex; lowest volatility and drawdown in equity set. |
| anthropic-claude-opus-5 | FINANCIALS | 20.0 | 0.025052928722653522 | 0.005010585744530705 | Steeper curve (10y up to 4.68%, 2y down), low drawdown, strong recent relative return with defensive volatility profile. |
| anthropic-claude-opus-5 | HEALTHCARE | 20.0 | 0.029595765158806575 | 0.005919153031761316 | Defensive leadership with shallow 63-day drawdown and near 52-week high; low beta to tech unwind. |
| anthropic-claude-opus-5 | DIVIDEND | 15.0 | 0.03162873189476789 | 0.004744309784215184 | Low correlation to SPY (0.31), strong 21-day active return, minimal drawdown; ballast if mega-cap unwind continues. |
| anthropic-claude-opus-5 | OIL | 15.0 | 0.0030160080426879787 | 0.0004524012064031968 | Brent settled $88.09 up 7.3% with Strait of Hormuz access unresolved; supply-risk premium can persist through the window. |
| google-gemini-3-1-pro | DIVIDEND | 50.0 | 0.03162873189476789 | 0.015814365947383946 | Dividend equities offer defensive characteristics and have shown recent relative strength. |
| google-gemini-3-1-pro | HEALTHCARE | 50.0 | 0.029595765158806575 | 0.014797882579403288 | Healthcare provides defensive exposure with positive recent momentum. |
| openai-gpt-5-5 | EQUAL_WEIGHT_SP500 | 25.0 | 0.02299170259120209 | 0.0057479256478005225 | Equal-weight exposure benefits from recent breadth improvement versus cap-weighted SPY while keeping lower 63-day volatility and shallower drawdown than SPY. |
| openai-gpt-5-5 | DIVIDEND | 25.0 | 0.03162873189476789 | 0.007907182973691973 | Dividend equities show strong recent active performance, low volatility, and near-high price positioning, fitting a defensive/value rotation if growth leadership remains under pressure. |
| openai-gpt-5-5 | HEALTHCARE | 20.0 | 0.029595765158806575 | 0.005919153031761316 | Healthcare has defensive characteristics, positive recent active return, and shallow drawdown while broad equity breadth has weakened. |
| openai-gpt-5-5 | FINANCIALS | 15.0 | 0.025052928722653522 | 0.003757939308398028 | Financials have strong recent active return and low drawdown, with potential support from solid activity and a higher ten-year yield despite credit and labor risks. |
| openai-gpt-5-5 | OIL | 15.0 | 0.0030160080426879787 | 0.0004524012064031968 | Oil has the strongest direct near-term geopolitical catalyst, with Brent up and Strait of Hormuz access unresolved, but position size is limited because volatility and drawdown are very high. |
| openai-gpt-5-6-sol | EQUAL_WEIGHT_SP500 | 35.0 | 0.02299170259120209 | 0.008047095906920732 | Broadening leadership, positive relative performance, and lower volatility favor equal weight over concentrated SPY. |
| openai-gpt-5-6-sol | HEALTHCARE | 25.0 | 0.029595765158806575 | 0.007398941289701644 | Recent defensive strength and shallow drawdown offer favorable one-month asymmetry amid macro uncertainty. |
| openai-gpt-5-6-sol | REAL_ESTATE | 20.0 | -0.03220191470844225 | -0.00644038294168845 | Positive relative trend and near-high positioning provide upside if upcoming inflation data eases rate pressure. |
| openai-gpt-5-6-sol | US_DOLLAR | 20.0 | -0.008444757213230236 | -0.0016889514426460474 | Low volatility, shallow drawdown, and restrictive relative U.S. policy provide diversification against equity and geopolitical shocks. |
| xai-grok-4-3 | DIVIDEND | 25.0 | 0.03162873189476789 | 0.007907182973691973 | Defensive equity with recent outperformance and lower volatility. |
| xai-grok-4-3 | HEALTHCARE | 25.0 | 0.029595765158806575 | 0.007398941289701644 | Defensive sector with positive recent returns and low drawdown. |
| xai-grok-4-3 | CONSUMER_STAPLES | 25.0 | -0.021863553113553036 | -0.005465888278388259 | Defensive equity benefiting from weak consumer confidence. |
| xai-grok-4-3 | EQUAL_WEIGHT_SP500 | 25.0 | 0.02299170259120209 | 0.0057479256478005225 | Broad equity exposure with recent relative strength versus SPY. |
| xai-grok-4-5 | HEALTHCARE | 30.0 | 0.029595765158806575 | 0.008878729547641972 | Recent relative strength and defensive characteristics amid elevated uncertainty and mixed growth data support outperformance vs cap-weighted SPY over the one-month window. |
| xai-grok-4-5 | LARGE_VALUE | 25.0 | 0.03530779095864056 | 0.00882694773966014 | Value leadership and lower drawdown profile versus growth/tech after the late-July selloff provide a higher base-case path than SPY. |
| xai-grok-4-5 | EQUAL_WEIGHT_SP500 | 25.0 | 0.02299170259120209 | 0.0057479256478005225 | Equal-weight breadth advantage and positive active returns versus SPY in recent windows favor continued rotation away from mega-cap concentration. |
| xai-grok-4-5 | ENERGY | 20.0 | 0.06871270247229333 | 0.013742540494458666 | Geopolitical premium from unresolved Middle East/Hormuz issues and prior active strength support elevated base return versus SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | LARGE_VALUE | 5 | 0.6 | 0.03530779095864056 | 0.039003574841090016 | -0.01568071216573691 | 0.2510245150465504 |  | False | True |
| xai-grok-4-5 | HEALTHCARE | 4 | 0.58 | 0.029595765158806575 | 0.037196143429561304 | -0.017488143577265622 | 0.2528319464580791 |  | False | True |
| anthropic-claude-opus-4-8 | DIVIDEND | 4 | 0.6 | 0.03162873189476789 | 0.03408765044016078 | -0.020596636566666146 | 0.25594043944747963 |  | False | True |
| google-gemini-3-1-pro | DIVIDEND | 2 | 0.65 | 0.03162873189476789 | 0.030612248526787234 | -0.024072038480039692 | 0.25941584136085316 |  | False | True |
| openai-gpt-5-5 | EQUAL_WEIGHT_SP500 | 5 | 0.58 | 0.02299170259120209 | 0.023784602168055037 | -0.03089968483877189 | 0.26624348771958534 |  | False | True |
| anthropic-claude-opus-5 | EQUAL_WEIGHT_SP500 | 5 | 0.55 | 0.02299170259120209 | 0.02302396054427103 | -0.0316603264625559 | 0.26700412934336937 |  | False | True |
| xai-grok-4-3 | DIVIDEND | 4 | 0.58 | 0.03162873189476789 | 0.01558816163280588 | -0.039096125374021046 | 0.27443992825483454 |  | False | True |
| openai-gpt-5-6-sol | EQUAL_WEIGHT_SP500 | 4 | 0.61 | 0.02299170259120209 | 0.007316702812287879 | -0.04736758419453905 | 0.28271138707535254 |  | False | True |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | LARGE_VALUE | -0.01568071216573691 | 0.47775 | -0.0328220034866288 |
| anthropic-claude-opus-5 | EQUAL_WEIGHT_SP500 | -0.0316603264625559 | 0.2217 | -0.14280706568586332 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | f4a01f6bcc5e7f8056754cca44b755e4937d0a71956aa4e42476c8c6acd01220 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | ef3cf65c548d3cc3229f74393dc61292363e4cb8a6e609b4a75e4c2062b6698e |
| manifest.yaml | 5cbd93a3334fc4404ad716e45756cae929028eca454b48ba38339ca28e28219d |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | fdf06c138c06bf8543f82d96377e0ba0f703d9958f3a71d40a13aa2663f97b2e |
| market_data/universe_decision_context.md | ac01c0937644d70398f5c77e86bb8a11661555acf1d1c1aa1bf2ace876528ea0 |
| market_data/universe_decision_context.json | 1aab17ea48c3cedaa7b6ebd10c1357c35922af6cf12ac04b2c99ecb981dd2a14 |
| market_data/decision_context_source_history.json | 732511e3d9864990a3aee1a8834300c3be6b0002a008be2c1d6861b885e772c4 |
| market_data/universe_quality_evidence.md | 4d77b56a7cc9c7e108896504d8798f20733d811dee15c6494298514ed7ff93ad |
| market_data/universe_quality_evidence.json | 668b4b41dea481d997c6cf5cfa3b4eab9f735326a89468c01c0bd6f5d65f8727 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 75695a3599f66831d0ed1070b57ca3ba14dc912210c94a19c53321e58304e9ea | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | b7393df29eef1c3751c47694aa160227d8ad332331b122f50db0a1471ade578a | yes |
| Final briefing | research/final_briefing.md | model-facing | f4a01f6bcc5e7f8056754cca44b755e4937d0a71956aa4e42476c8c6acd01220 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
