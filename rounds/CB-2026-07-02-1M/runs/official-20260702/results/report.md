# CapitalBench Report: CB-2026-07-02-1M / official-20260702

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260702
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-02-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-02
- Decision deadline: 2026-07-03T07:30:00Z
- Horizon: one month
- Entry date: 2026-07-02
- Exit date: 2026-07-31
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | LARGE_VALUE | 4 | 0.65 | Value, financials, healthcare, and low-vol allocations balance earnings catalysts with macro softening signals. | Stronger-than-expected July data reversing defensive flows; Tech earnings beats driving growth rotation; Oil price spike pressuring broader risk appetite |
| google-gemini-3-1-pro | google | portfolio | SP500 | 4 | 0.7 | A balanced approach combining broad US equities, defensive sectors (healthcare), interest-rate sensitive sectors (financials), and short-term treasuries for stability. | Unexpected changes in Federal Reserve policy or interest rates could negatively impact equities and financials.; A broader market downturn could drag down the performance of the S&P 500 and sector-specific allocations.; Disappointing earnings reports from major banks could negatively affect the financials sector. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 5 | 0.6 | Overweight sectors with positive benchmark-relative momentum, catalysts, and lower drawdown while avoiding the weak, high-volatility AI/semis complex. | A mega-cap tech rebound could cause cap-weighted and growth indices to outperform this value/defensive tilt; Weak June payrolls and elevated core PCE could trigger a broad risk-off move hurting financials and cyclicals; Bank earnings July 14 could disappoint on credit or NIM, reversing the financials rally |
| anthropic-claude-opus-4-7 | anthropic | portfolio | FINANCIALS | 5 | 0.55 | Barbell of financials (earnings catalyst), healthcare/equal-weight (defensive breadth), aerospace (trend + geopolitics), and T-bills (ballast) to seek alpha vs SPY during a tech-heavy drawdown month. | Mega-cap tech rebound would cause SPY to outperform this defensive tilt; Bank earnings disappointment on NIM or credit could hit financials overweight; Sticky inflation surprise pressures all equity sectors; Healthcare policy or drug-pricing headline reversal risk after strong 30d run |
| anthropic-claude-fable-5 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Rotation portfolio tilted to value, healthcare, biotech, financials, and small-cap value on weakening labor data and near-term bank earnings catalysts, avoiding recently drawn-down tech/momentum. | Sticky core PCE at 3.4% y/y keeps the Fed hawkish at the late-July FOMC, hurting rate-sensitive biotech and small caps; Mega-cap tech earnings rebound could make SPY outrun this low-beta, value-tilted portfolio; Bank Q2 results on July 14 disappoint on credit costs or net interest income; Healthcare/biotech recent strength reverses on drug-pricing policy headlines or profit-taking after outsized 30d gains |
| openai-gpt-5-5 | openai | portfolio | HEALTHCARE | 5 | 0.58 | Soft payrolls and elevated inflation create a mixed macro backdrop, making defensive healthcare strength and earnings-driven financial exposure more attractive than broad S&P 500 beta. Biotech and regional banks increase upside potential but are balanced by larger allocations to broader healthcare and financials. | Biotech's very strong recent performance could reverse sharply because independent July catalyst support in the briefing is limited and the group is highly volatile.; Bank earnings could reveal credit deterioration, deposit pressure, or margin compression, hurting both financials and regional banks.; Elevated PCE inflation and high Treasury yields could keep rate-cut expectations subdued, pressuring rate-sensitive biotech and broader equities.; A rebound in mega-cap technology, semiconductors, or AI stocks after recent weakness could cause this underweight to underperform the S&P 500.; A broad risk-off move after weak labor or services data could overwhelm sector selection and hurt high-beta holdings such as biotech and regional banks. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 103.98 | 129.1699981689453 | 0.24225810895311883 | 1 |
| ENERGY | Energy Sector | 53.220001220703125 | 59.55 | 0.11894022236200996 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 15.87 | 17.559999465942383 | 0.10649019949227378 | 3 |
| CHINA | China Equities | 50.91 | 55.79999923706055 | 0.09605184123081023 | 4 |
| ETHEREUM_ETF | Ethereum ETF | 12.86 | 14.069999694824219 | 0.09409017844667344 | 5 |
| BRAZIL | Brazil Equities | 34.43 | 36.650001525878906 | 0.06447869665637262 | 6 |
| COPPER | Copper | 37.29 | 39.560001373291016 | 0.0608742658431487 | 7 |
| AUSTRALIA | Australia Equities | 28.09 | 29.34000015258789 | 0.04449982743281922 | 8 |
| DIVIDEND | US Dividend Equities | 32.38999938964844 | 33.47 | 0.033343644047635346 | 9 |
| AGRICULTURE | Agriculture Commodities | 26.74 | 27.510000228881836 | 0.02879582007785486 | 10 |
| CANADA | Canada Equities | 57.77 | 59.38999938964844 | 0.02804222588970795 | 11 |
| UNITED_KINGDOM | United Kingdom Equities | 47.16 | 48.40999984741211 | 0.026505509911198377 | 12 |
| FINANCIALS | Financials Sector | 55.619998931884766 | 56.94 | 0.023732489993963712 | 13 |
| BITCOIN_ETF | Bitcoin ETF | 34.87 | 35.63999938964844 | 0.022082001423815223 | 14 |
| LARGE_VALUE | US Large-Cap Value | 246.80999755859375 | 251.82 | 0.0202990255296156 | 15 |
| MEXICO | Mexico Equities | 75.5 | 76.80999755859375 | 0.017350961040976776 | 16 |
| EUROPE | Europe Equities | 89.3499984741211 | 90.59 | 0.0138780251489099 | 17 |
| REGIONAL_BANKS | Regional Banks | 75.02 | 76.05999755859375 | 0.013862937331295067 | 18 |
| CYBERSECURITY | Cybersecurity | 90.67 | 91.83000183105469 | 0.012793667487092542 | 19 |
| YEN | Japanese Yen | 56.95 | 57.65999984741211 | 0.012467073703461118 | 20 |
| SOFTWARE | Software | 93.57 | 94.58000183105469 | 0.01079407749337058 | 21 |
| EURO | Euro | 105.47 | 106.48999786376953 | 0.009670976237503792 | 22 |
| REAL_ESTATE | Real Estate Sector | 44.68000030517578 | 45.07 | 0.008728730800367623 | 23 |
| INDIA | India Equities | 49.56 | 49.79999923706055 | 0.0048425996178480535 | 24 |
| SP500 | S&P 500 | 744.780029296875 | 747.03 | 0.0030209868882347113 | 25 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.44000244140625 | 91.68 | 0.00262464514639027 | 26 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.98999786376953 | 85.05 | 0.0007059905605204531 | 27 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 214.91 | 215.00999450683594 | 0.00046528550014390824 | 28 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 29 |
| SMALL_VALUE | US Small-Cap Value | 221.3300018310547 | 221.24 | -0.00040664089960740224 | 30 |
| TOTAL_US_MARKET | Total US Stock Market | 368.760009765625 | 368.21 | -0.0014915114195126478 | 31 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.80999755859375 | 70.62 | -0.002683202445198929 | 32 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.70999908447266 | 79.48 | -0.002885448339158936 | 33 |
| LOW_VOL | US Low Volatility Equities | 76.58870697021484 | 76.23 | -0.004683549108021157 | 34 |
| EMERGING_MARKETS | Emerging Markets | 59.040000915527344 | 58.75 | -0.004911939549971711 | 35 |
| SOUTH_AFRICA | South Africa Equities | 64.0 | 63.619998931884766 | -0.005937516689300537 | 36 |
| US_DOLLAR | US Dollar | 28.34 | 28.170000076293945 | -0.005998585875301887 | 37 |
| TIPS | Treasury Inflation-Protected Securities | 108.33000183105469 | 107.63 | -0.006461754077567328 | 38 |
| HEALTHCARE | Healthcare Sector | 163.74000549316406 | 162.55 | -0.0072676527008772585 | 39 |
| JAPAN | Japan Equities | 93.13999938964844 | 92.38999938964844 | -0.008052394297989984 | 40 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.12000274658203 | 116.09 | -0.008794422151873538 | 41 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.24 | 47.77000045776367 | -0.009742942417834355 | 42 |
| MID_CAP | US Mid-Cap Stocks | 76.08999633789062 | 75.27 | -0.010776664178682505 | 43 |
| COMMUNICATIONS | Communication Services Sector | 109.5999984741211 | 108.24 | -0.012408745374592578 | 44 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.12000274658203 | 92.95 | -0.012430968045467061 | 45 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.61000061035156 | 97.37 | -0.012574795686811857 | 46 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.13 | 92.91999816894531 | -0.012854582291030314 | 47 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.2 | 94.66000366210938 | -0.01600827794065096 | 48 |
| GOLD | Gold | 77.51 | 76.16999816894531 | -0.017288115482578914 | 49 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.5 | 105.63999938964844 | -0.017302331259084314 | 50 |
| SMALL_CAP | US Small-Cap Stocks | 297.5799865722656 | 291.2 | -0.021439568721521862 | 51 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.63999938964844 | 106.25 | -0.021999258128458377 | 52 |
| INDUSTRIALS | Industrials Sector | 183.91000366210938 | 179.84 | -0.022130409336443835 | 53 |
| LARGE_GROWTH | US Large-Cap Growth | 121.16000366210938 | 118.32 | -0.023440108750983346 | 54 |
| TECHNOLOGY | Technology Sector | 180.58999633789062 | 175.35 | -0.02901598341076661 | 55 |
| MATERIALS | Materials Sector | 52.0099983215332 | 50.43 | -0.03037874202120583 | 56 |
| UTILITIES | Utilities Sector | 45.7599983215332 | 44.35 | -0.03081290151336613 | 57 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 248.19 | 239.66000366210938 | -0.0343688155763352 | 58 |
| NASDAQ100 | Nasdaq 100 | 712.5999755859375 | 687.99 | -0.034535470711603455 | 59 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.51000213623047 | 82.25 | -0.038124220030269496 | 60 |
| METALS_MINING | Metals and Mining | 105.13 | 100.6500015258789 | -0.04261389207762856 | 61 |
| BROAD_AI_TECH | Broad AI Technology | 61.85 | 58.88999938964844 | -0.04785773015928152 | 62 |
| SILVER | Silver | 55.02 | 52.36000061035156 | -0.048346044886376616 | 63 |
| MOMENTUM | US Momentum Equities | 316.5299987792969 | 299.59 | -0.05351783036244995 | 64 |
| TAIWAN | Taiwan Equities | 104.86 | 96.55000305175781 | -0.07924849273547763 | 65 |
| BIOTECH | Biotechnology | 160.46 | 147.00999450683594 | -0.08382154738354775 | 66 |
| SEMICONDUCTORS | Semiconductors | 592.29 | 540.530029296875 | -0.08738957386267698 | 67 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 127.94 | 115.06999969482422 | -0.10059403083614027 | 68 |
| SOLAR | Solar Energy | 56.32 | 49.33000183105469 | -0.12411218339746644 | 69 |
| SOUTH_KOREA | South Korea Equities | 180.14 | 157.10000610351562 | -0.12790048793429754 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | HEALTHCARE | 25.0 | -0.0072676527008772585 | -0.0018169131752193146 | Defensive sector with strong recent breadth (67% up days, at 52w high) and low beta; supported by rotation away from stretched tech amid soft June payrolls. |
| anthropic-claude-fable-5 | BIOTECH | 20.0 | -0.08382154738354775 | -0.01676430947670955 | Weak labor data (+57k payrolls, downward revisions) raises rate-cut expectations, supporting rate-sensitive biotech; strength backed by broad participation (71% up days) though continuation risk exists. |
| anthropic-claude-fable-5 | FINANCIALS | 20.0 | 0.023732489993963712 | 0.004746497998792743 | JPMorgan and Wells Fargo Q2 results July 14 as near-term catalysts; sector showing steady gains with low drawdown and modest beta. |
| anthropic-claude-fable-5 | LARGE_VALUE | 20.0 | 0.0202990255296156 | 0.00405980510592312 | Value at 52w high with positive 30d relative return, low volatility; rotation from expensive growth amid slowing labor market favors value tilt. |
| anthropic-claude-fable-5 | SMALL_VALUE | 15.0 | -0.00040664089960740224 | -6.099613494111033e-05 | Small-cap value benefits if soft jobs data pulls forward Fed easing; positive 30d relative performance with contained drawdown. |
| anthropic-claude-opus-4-7 | FINANCIALS | 25.0 | 0.023732489993963712 | 0.005933122498490928 | Big bank earnings (JPM, WFC) July 14 as key July catalyst; sector showing leadership with steep yield curve supportive. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 25.0 | -0.0072676527008772585 | -0.0018169131752193146 | Defensive leadership with strong 30d relative outperformance; low beta cushions if tech drawdown continues. |
| anthropic-claude-opus-4-7 | EQUAL_WEIGHT_SP500 | 20.0 | 0.00046528550014390824 | 9.305710002878166e-05 | Broadening participation away from mega-cap tech weakness; balanced sector exposure into earnings season. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 15.0 | -0.0343688155763352 | -0.0051553223364502795 | Sustained defense spending backdrop, strong trend with moderate volatility, geopolitical tailwinds. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 15.0 | 0.00262464514639027 | 0.00039369677195854046 | Dry powder given elevated tech volatility, sticky core PCE at 3.4%, and Fed on hold; hedges drawdown risk. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | 0.023732489993963712 | 0.005933122498490928 | Strong recent breadth (+8.5% 30d, +10.2% vs SPX) with bank earnings catalysts July 14 (JPM, WFC) and steep yield curve supporting NIM; low volatility and near 52w highs. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 20.0 | -0.0072676527008772585 | -0.0014535305401754519 | Defensive sector with the strongest 30d relative return (+14% vs SPX), low beta, and momentum into a choppy tech tape; XBI biotech strength supports the group. |
| anthropic-claude-opus-4-8 | LARGE_VALUE | 20.0 | 0.0202990255296156 | 0.00405980510592312 | Value leadership with +3.45% 30d and +5.15% vs SPX, lower volatility, and defensive rotation away from stretched mega-cap growth amid soft payrolls. |
| anthropic-claude-opus-4-8 | AEROSPACE_DEFENSE | 15.0 | -0.0343688155763352 | -0.0051553223364502795 | Steady uptrend (+8.8% 30d, +10.5% vs SPX) backed by durable defense budget demand and geopolitical tailwinds; near 52w highs with contained drawdown. |
| anthropic-claude-opus-4-8 | EQUAL_WEIGHT_SP500 | 20.0 | 0.00046528550014390824 | 9.305710002878166e-05 | Broad diversified US exposure that avoids mega-cap tech concentration, positive 30d relative return, and lower volatility as breadth broadens. |
| google-gemini-3-1-pro | SP500 | 40.0 | 0.0030209868882347113 | 0.0012083947552938845 | Broad US equity exposure provides a baseline for the portfolio, capturing general market growth while managing risk. |
| google-gemini-3-1-pro | HEALTHCARE | 20.0 | -0.0072676527008772585 | -0.0014535305401754519 | Healthcare offers defensive characteristics and has shown recent strength, providing stability in a potentially volatile market. |
| google-gemini-3-1-pro | FINANCIALS | 20.0 | 0.023732489993963712 | 0.004746497998792743 | Financials benefit from the current interest rate environment and upcoming earnings reports from major banks could provide a catalyst. |
| google-gemini-3-1-pro | SHORT_TREASURY | 20.0 | 0.00262464514639027 | 0.000524929029278054 | Short-term treasuries provide a risk-free yield and act as a buffer against potential market downturns. |
| openai-gpt-5-5 | HEALTHCARE | 30.0 | -0.0072676527008772585 | -0.0021802958102631774 | Healthcare has shown strong recent relative strength with lower S&P beta, and the softer labor data could favor defensive growth areas if broad risk appetite weakens during July. |
| openai-gpt-5-5 | BIOTECH | 25.0 | -0.08382154738354775 | -0.020955386845886936 | Biotech has the strongest recent benchmark-relative performance in the universe and may benefit from lower-rate expectations after weak payrolls; independent catalyst support is limited, so the position is sized below healthcare despite high momentum. |
| openai-gpt-5-5 | FINANCIALS | 20.0 | 0.023732489993963712 | 0.004746497998792743 | Financials have strong recent relative strength, low drawdown, and near-term large-bank earnings catalysts in mid-July that could support continuation if credit and deposit commentary are stable. |
| openai-gpt-5-5 | REGIONAL_BANKS | 15.0 | 0.013862937331295067 | 0.00207944059969426 | Regional banks add higher-beta exposure to the financials earnings catalyst and have recently outperformed, with potential upside if yield-curve, deposit, and credit concerns ease. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 10.0 | -0.0343688155763352 | -0.0034368815576335202 | Aerospace and defense has been outperforming with identifiable sector demand and geopolitical/defense-spending sensitivity, offering equity upside not tightly linked to mega-cap technology. |
| xai-grok-4-3 | LARGE_VALUE | 25.0 | 0.0202990255296156 | 0.0050747563824039 | Soft June payrolls and downward revisions favor value tilt with lower rate sensitivity over the window. |
| xai-grok-4-3 | FINANCIALS | 25.0 | 0.023732489993963712 | 0.005933122498490928 | Bank earnings season begins mid-July with stable rates supporting net interest margins. |
| xai-grok-4-3 | HEALTHCARE | 25.0 | -0.0072676527008772585 | -0.0018169131752193146 | Defensive sector positioning amid labor market cooling and upcoming PCE release. |
| xai-grok-4-3 | LOW_VOL | 25.0 | -0.004683549108021157 | -0.0011708872770052892 | Lower volatility exposure to buffer potential equity swings before July 31 close. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | LARGE_VALUE | 4 | 0.65 | 0.0202990255296156 | 0.008020078428670224 | 0.004999091540435513 | 0.2342380305244486 |  | True | True |
| google-gemini-3-1-pro | SP500 | 4 | 0.7 | 0.0030209868882347113 | 0.00502629124318923 | 0.0020053043549545183 | 0.2372318177099296 |  | True | True |
| anthropic-claude-opus-4-8 | FINANCIALS | 5 | 0.6 | 0.023732489993963712 | 0.0034771318278170983 | 0.00045614493958238706 | 0.23878097712530175 |  | True | True |
| anthropic-claude-opus-4-7 | FINANCIALS | 5 | 0.55 | 0.023732489993963712 | -0.0005523591411913437 | -0.003573346029426055 | 0.24281046809431017 |  | False | False |
| anthropic-claude-fable-5 | HEALTHCARE | 5 | 0.55 | -0.0072676527008772585 | -0.009835915682154112 | -0.012856902570388823 | 0.252094024635273 |  | False | False |
| openai-gpt-5-5 | HEALTHCARE | 5 | 0.58 | -0.0072676527008772585 | -0.01974662561529663 | -0.02276761250353134 | 0.26200473456841544 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | HEALTHCARE | -0.012856902570388823 | 0.27189 | -0.0472871476346641 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 665508a1f43a6420716b2088c4ea4c58c7093fecfab26ae08b6d31e16110c67b |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 7858eef0aa73ea38b28daacc4aaa57e57b110de6456378f1697ff1cd79ca213c |
| manifest.yaml | 277a54a48ae0a6133f19828a9049cb14e400e4244046c22cc2dcb8f89260426d |
| market_data/universe_trailing_returns.csv | f6cbad822725c4e104ad345c7ae396f0bb1d13dc98f395f843180c52b87e67b1 |
| market_data/universe_trailing_returns.md | 7a0319653ef701364c37ed807b6b1ce1fa8c5393dde17fbec300bc96b6e12ba9 |
| market_data/universe_trailing_returns.json | fd83409f0525b11a2aee4fc1914d1d9d6faae7afdcfe98884bcf524b44677fe2 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 43c8e389b97d1460a319cc06b5a85f0ce83e68ef5495d3634730ab60abc95d28 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 8490095f22998d14f4967888865c2b43616b597a34346f3f98ed92b0a37ee8e4 | yes |
| Final briefing | research/final_briefing.md | model-facing | 665508a1f43a6420716b2088c4ea4c58c7093fecfab26ae08b6d31e16110c67b | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
