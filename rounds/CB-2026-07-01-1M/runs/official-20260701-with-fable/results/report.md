# CapitalBench Report: CB-2026-07-01-1M / official-20260701-with-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260701-with-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-01-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-01
- Decision deadline: 2026-07-02T07:30:00Z
- Horizon: one month
- Entry date: 2026-07-01
- Exit date: 2026-07-31
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | SP500 | 4 | 0.65 | A balanced approach favoring broad US equities, defensive sectors like healthcare, and financials, with a cash-like buffer. | A broader market downturn could negatively impact the equity allocations.; Unexpected changes in interest rates or inflation could affect the performance of financials and the broader market.; Sector-specific risks in healthcare or financials could lead to underperformance relative to the benchmark. |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 5 | 0.6 | Overweight financials, industrials, healthcare, and equal-weight to capture broadening leadership and bank earnings while diversifying away from tech concentration risk. | Sticky core PCE at 3.4% YoY could push hawkish FOMC minutes (July 8) and July decision, pressuring rate-sensitive financials and regional banks; Bank Q2 earnings (JPM, WFC) could disappoint on credit or NII, reversing the recent financials/regional-bank rally that relies partly on momentum; Weak June jobs report (July 2) could trigger risk-off, hurting cyclical industrials and small-cap-heavy regional banks; Tech/AI rebound could cause equal-weight and defensive sectors to lag the cap-weighted S&P 500 benchmark |
| xai-grok-4-3 | xai | portfolio | SMALL_VALUE | 4 | 0.55 | Allocations emphasize areas with recent benchmark outperformance and near-term data or earnings sensitivity over the July horizon. | Surprise in June employment report leading to rate volatility; Sticky inflation data pressuring valuations; Reversal in recent small-cap and value momentum |
| anthropic-claude-opus-4-7 | anthropic | portfolio | HEALTHCARE | 5 | 0.55 | Overweight healthcare, financials, and broad-breadth cyclicals to capture July rotation and bank earnings catalysts while avoiding concentrated mega-cap tech drawdown risk. | Soft June payrolls (July 2) could trigger growth scare hitting cyclicals and financials; Bank Q2 earnings disappointment on NII or credit could reverse KRE/XLF strength; Mega-cap tech rebound would cause SPY benchmark to outrun defensive tilt; Sticky core PCE (3.4%) prompts hawkish July 29 FOMC, pressuring rate-sensitive sectors; Biotech reversal risk after +17% monthly run-up |
| anthropic-claude-fable-5 | anthropic | portfolio | HEALTHCARE | 5 | 0.5 | Overweight broadening-market beneficiaries (value, small caps, equal-weight, financials, healthcare/biotech) given firm macro data, lagging mega-cap tech, and mid-July bank earnings catalysts. | Mega-cap tech re-acceleration (e.g., strong TSMC results) reverses the rotation and lifts cap-weighted SPY above this portfolio; Hot June payrolls or sticky core PCE pushes yields higher, hurting small caps, regional-bank-heavy value, and biotech; Momentum reversal in healthcare/biotech after strong 30-day runs with limited fundamental support in the briefing; Weak Q2 bank earnings or credit deterioration hits the financials overweight |
| openai-gpt-5-5 | openai | portfolio | REGIONAL_BANKS | 5 | 0.57 | I expect a one-month continuation of rotation into banks, small value, industrials, and healthcare/biotech to outperform the cap-weighted S&P 500, especially if earnings and macro releases confirm solid nominal growth. The portfolio accepts elevated factor and industry risk to target benchmark-relative upside over the short scoring window. | A weak July payrolls report, softer services data, or poor Q2 GDP signal could hurt regional banks, small value, and industrial cyclicals before month-end.; Bank earnings could reveal credit deterioration, deposit pressure, margin compression, or commercial real estate losses, reversing recent financials and regional-bank momentum.; Biotech's recent surge may be overextended; clinical, regulatory, funding, or risk-appetite shocks could cause a sharp one-month reversal.; A renewed mega-cap AI and technology rally could lift the S&P 500 while this underweight to technology and semiconductors lags.; Hot PCE inflation or a hawkish July FOMC decision could pressure small caps, banks, and other rate-sensitive equities. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 103.27 | 129.1699981689453 | 0.2507988590001484 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 12.19 | 14.069999694824219 | 0.1542247493703215 | 2 |
| ENERGY | Energy Sector | 52.81 | 59.55 | 0.12762734330619185 | 3 |
| BROAD_COMMODITIES | Broad Commodities | 15.78 | 17.559999465942383 | 0.11280098009774298 | 4 |
| CHINA | China Equities | 51.525 | 55.79999923706055 | 0.08296941750724018 | 5 |
| BRAZIL | Brazil Equities | 34.18 | 36.650001525878906 | 0.07226452679575512 | 6 |
| COPPER | Copper | 37.21 | 39.560001373291016 | 0.06315510274901959 | 7 |
| AUSTRALIA | Australia Equities | 27.7 | 29.34000015258789 | 0.059205781681873404 | 8 |
| UNITED_KINGDOM | United Kingdom Equities | 45.94 | 48.40999984741211 | 0.05376577813261019 | 9 |
| DIVIDEND | US Dividend Equities | 31.85 | 33.47 | 0.0508634222919937 | 10 |
| BITCOIN_ETF | Bitcoin ETF | 34.0 | 35.63999938964844 | 0.048235276166130436 | 11 |
| FINANCIALS | Financials Sector | 54.78 | 56.94 | 0.03943044906900317 | 12 |
| LARGE_VALUE | US Large-Cap Value | 243.88 | 251.82 | 0.03255699524356248 | 13 |
| EUROPE | Europe Equities | 87.77 | 90.58999633789062 | 0.032129387465997805 | 14 |
| CANADA | Canada Equities | 57.67 | 59.38999938964844 | 0.029824855031185038 | 15 |
| AGRICULTURE | Agriculture Commodities | 26.86 | 27.510000228881836 | 0.024199561760306576 | 16 |
| YEN | Japanese Yen | 56.43 | 57.65999984741211 | 0.021796913829737807 | 17 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.3 | 85.05 | 0.021008403361344463 | 18 |
| MEXICO | Mexico Equities | 75.27 | 76.80999755859375 | 0.020459646055450476 | 19 |
| REAL_ESTATE | Real Estate Sector | 44.18 | 45.06999969482422 | 0.02014485502091934 | 20 |
| HEALTHCARE | Healthcare Sector | 159.54 | 162.55 | 0.018866741882913596 | 21 |
| LOW_VOL | US Low Volatility Equities | 75.100488185 | 76.23 | 0.015040006294201547 | 22 |
| EURO | Euro | 104.95 | 106.48999786376953 | 0.014673633766265182 | 23 |
| SOUTH_AFRICA | South Africa Equities | 62.73 | 63.619998931884766 | 0.014187771909529134 | 24 |
| SOFTWARE | Software | 93.34 | 94.58000183105469 | 0.013284784990943654 | 25 |
| INDIA | India Equities | 49.21 | 49.79999923706055 | 0.011989417538316394 | 26 |
| CYBERSECURITY | Cybersecurity | 91.11 | 91.83000183105469 | 0.007902555493960017 | 27 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 213.41 | 215.00999450683594 | 0.007497279915823718 | 28 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.36 | 70.62000274658203 | 0.0036953204460208333 | 29 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.4 | 91.68 | 0.0030634573304157975 | 30 |
| GOLD | Gold | 75.96 | 76.16999816894531 | 0.0027645888486744763 | 31 |
| SP500 | S&P 500 | 745.76 | 747.03 | 0.0017029607380389944 | 32 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 33 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.59 | 79.4800033569336 | -0.001382040998447187 | 34 |
| REGIONAL_BANKS | Regional Banks | 76.18 | 76.05999755859375 | -0.0015752486401451327 | 35 |
| SMALL_VALUE | US Small-Cap Value | 221.71 | 221.24 | -0.0021198863380090804 | 36 |
| TOTAL_US_MARKET | Total US Stock Market | 369.27 | 368.21 | -0.0028705283396972536 | 37 |
| TIPS | Treasury Inflation-Protected Securities | 108.17 | 107.62999725341797 | -0.004992167390053037 | 38 |
| JAPAN | Japan Equities | 93.05 | 92.38999938964844 | -0.007092967333170996 | 39 |
| EMERGING_MARKETS | Emerging Markets | 59.22 | 58.75 | -0.007936507936507908 | 40 |
| UTILITIES | Utilities Sector | 44.77 | 44.349998474121094 | -0.009381316191175104 | 41 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.27 | 47.77000045776367 | -0.010358391179538629 | 42 |
| US_DOLLAR | US Dollar | 28.49 | 28.170000076293945 | -0.01123200855409101 | 43 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.5 | 97.37000274658203 | -0.011472053334192545 | 44 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.03 | 92.94999694824219 | -0.01148572850960139 | 45 |
| MATERIALS | Materials Sector | 51.02 | 50.43 | -0.011564092512740154 | 46 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.02 | 92.91999816894531 | -0.011699657849975398 | 47 |
| COMMUNICATIONS | Communication Services Sector | 109.74 | 108.24 | -0.013668671405139388 | 48 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.02 | 94.66000366210938 | -0.014163677753495363 | 49 |
| MID_CAP | US Mid-Cap Stocks | 76.44 | 75.27 | -0.015306122448979664 | 50 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.34 | 105.63999938964844 | -0.015837531305678887 | 51 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.09 | 116.09 | -0.016936235074942796 | 52 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 243.86 | 239.66000366210938 | -0.017222981784182023 | 53 |
| INDUSTRIALS | Industrials Sector | 183.36 | 179.84 | -0.01919720767888311 | 54 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.46 | 106.25 | -0.02037617554858928 | 55 |
| SILVER | Silver | 53.58 | 52.36000061035156 | -0.022769678791497494 | 56 |
| SMALL_CAP | US Small-Cap Stocks | 299.32 | 291.2 | -0.027128157156220745 | 57 |
| METALS_MINING | Metals and Mining | 104.36 | 100.6500015258789 | -0.0355500045431304 | 58 |
| LARGE_GROWTH | US Large-Cap Growth | 123.02 | 118.32 | -0.0382051698910747 | 59 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.52 | 82.25 | -0.038236669784845634 | 60 |
| NASDAQ100 | Nasdaq 100 | 725.17 | 687.99 | -0.051270736516954574 | 61 |
| TECHNOLOGY | Technology Sector | 185.62 | 175.35 | -0.05532808964551239 | 62 |
| BIOTECH | Biotechnology | 156.55 | 147.00999450683594 | -0.06093903221439845 | 63 |
| BROAD_AI_TECH | Broad AI Technology | 63.63 | 58.88999938964844 | -0.07449317319427262 | 64 |
| TAIWAN | Taiwan Equities | 105.69 | 96.55000305175781 | -0.08647929745711214 | 65 |
| MOMENTUM | US Momentum Equities | 328.1 | 299.59 | -0.08689423956110953 | 66 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 130.44 | 115.06999969482422 | -0.11783195572811855 | 67 |
| SEMICONDUCTORS | Semiconductors | 620.46 | 540.530029296875 | -0.12882372869020575 | 68 |
| SOLAR | Solar Energy | 57.8 | 49.33000183105469 | -0.14653976070839636 | 69 |
| SOUTH_KOREA | South Korea Equities | 185.5 | 157.10000610351562 | -0.15309969755517183 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | HEALTHCARE | 25.0 | 0.018866741882913596 | 0.004716685470728399 | Broad healthcare showing renewed strength with low beta; defensive earnings and sector rotation support continuation with limited drawdown risk. |
| anthropic-claude-fable-5 | SMALL_VALUE | 20.0 | -0.0021198863380090804 | -0.0004239772676018161 | Rotation into small-cap value is supported by solid labor data, resilient GDP, and steady Fed policy; at 52-week high with moderate volatility. |
| anthropic-claude-fable-5 | FINANCIALS | 20.0 | 0.03943044906900317 | 0.007886089813800635 | Q2 bank earnings (JPM, WFC July 14) are a near-term catalyst; sector momentum backed by firm economy and stable rates. |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 20.0 | 0.007497279915823718 | 0.0014994559831647436 | Market breadth is improving while mega-cap tech lags; equal-weight at 52-week high with lower volatility than cap-weighted SPY. |
| anthropic-claude-fable-5 | BIOTECH | 15.0 | -0.06093903221439845 | -0.009140854832159767 | Strong recent breadth (66% up days, small drawdown) alongside healthcare strength; M&A and rate-plateau environment supportive, though momentum reliance is a risk. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 30.0 | 0.018866741882913596 | 0.005660022564874079 | Strong recent leadership with defensive characteristics; low beta (0.37) offers downside protection amid tech weakness while momentum is positive. |
| anthropic-claude-opus-4-7 | FINANCIALS | 25.0 | 0.03943044906900317 | 0.009857612267250793 | Big bank Q2 earnings (JPM, WFC on July 14) as key July catalyst; sector showing strong breadth with +6.88% 30d return and low drawdown. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 15.0 | -0.01919720767888311 | -0.0028795811518324663 | ISM Manufacturing PMI at 53.3 with new orders 56.0 supports cyclical strength; broad rotation into non-tech cyclicals evident. |
| anthropic-claude-opus-4-7 | EQUAL_WEIGHT_SP500 | 15.0 | 0.007497279915823718 | 0.0011245919873735576 | Captures market breadth rotation away from mega-cap tech; lower concentration risk with beta 0.74. |
| anthropic-claude-opus-4-7 | BIOTECH | 15.0 | -0.06093903221439845 | -0.009140854832159767 | Strongest 30d momentum (+17.27%) with healthcare sector tailwind; catalyst-rich July with clinical data flow. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | 0.03943044906900317 | 0.009857612267250793 | Strong 30d relative outperformance (+8.3% vs SPY), Q2 bank earnings (JPM, WFC July 14) as catalyst, low volatility, high up-day share; sticky rates at 3.50-3.75% support net interest margins. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 20.0 | -0.01919720767888311 | -0.003839441535776622 | ISM manufacturing still expansionary at 53.3, new orders robust at 56.0; strong benchmark-relative performance (+8.05% 30d) with moderate volatility supports continuation. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 20.0 | 0.018866741882913596 | 0.003773348376582719 | Defensive sector leading recently (+9.8% vs SPY 30d), low beta 0.37 provides downside protection against tech-led index weakness while offering positive momentum. |
| anthropic-claude-opus-4-8 | REGIONAL_BANKS | 15.0 | -0.0015752486401451327 | -0.00023628729602176988 | Best up-day share (80.95%), strong 30d relative return (+13.6%), benefits from bank earnings season and stable rate environment; limited fundamental support beyond macro, higher volatility noted. |
| anthropic-claude-opus-4-8 | EQUAL_WEIGHT_SP500 | 20.0 | 0.007497279915823718 | 0.0014994559831647436 | Broad diversified US large-cap exposure that reduces mega-cap tech concentration risk, positive 30d relative return, lower beta 0.74; hedges against AI/tech reversal dragging cap-weighted index. |
| google-gemini-3-1-pro | SP500 | 40.0 | 0.0017029607380389944 | 0.0006811842952155978 | Broad US equity exposure provides a baseline for market returns, balancing growth and value. |
| google-gemini-3-1-pro | HEALTHCARE | 20.0 | 0.018866741882913596 | 0.003773348376582719 | Healthcare offers defensive characteristics and has shown recent relative strength, providing a buffer against potential volatility. |
| google-gemini-3-1-pro | FINANCIALS | 20.0 | 0.03943044906900317 | 0.007886089813800635 | Financials may benefit from stable interest rates and upcoming earnings reports from major banks. |
| google-gemini-3-1-pro | SHORT_TREASURY | 20.0 | 0.0030634573304157975 | 0.0006126914660831595 | A cash-like allocation reduces overall portfolio risk and provides liquidity amid uncertain market conditions. |
| openai-gpt-5-5 | REGIONAL_BANKS | 30.0 | -0.0015752486401451327 | -0.00047257459204353976 | Regional banks have shown strong recent relative strength with broad up-day participation, and July bank earnings plus firm domestic growth data could keep attention on improving credit and net-interest-income expectations; support is catalyst-linked but vulnerable to reversal if earnings or credit signals disappoint. |
| openai-gpt-5-5 | BIOTECH | 25.0 | -0.06093903221439845 | -0.015234758053599612 | Biotech has the strongest 30-day relative performance in the universe and remains near its 52-week high, with healthcare also participating; the independent support is limited to sector risk appetite and healthcare strength, so the position is sized below banks despite high upside. |
| openai-gpt-5-5 | SMALL_VALUE | 20.0 | -0.0021198863380090804 | -0.0004239772676018161 | Small-cap value combines favorable recent breadth with domestic cyclicality, and the briefing's GDP, consumption, manufacturing, and income data suggest enough near-term growth support for continued rotation away from mega-cap technology concentration. |
| openai-gpt-5-5 | FINANCIALS | 15.0 | 0.03943044906900317 | 0.005914567360350475 | Large financials provide a broader, less volatile complement to regional banks, with JPMorgan and Wells Fargo earnings scheduled mid-month and recent outperformance supported by firm nominal activity and rates. |
| openai-gpt-5-5 | INDUSTRIALS | 10.0 | -0.01919720767888311 | -0.001919720767888311 | Industrials offer cyclical exposure with recent outperformance and independent support from expansionary manufacturing new orders, while diversifying away from financial-sector-specific risks. |
| xai-grok-4-3 | SMALL_VALUE | 30.0 | -0.0021198863380090804 | -0.0006359659014027241 | Recent outperformance and sensitivity to domestic growth and potential rate stability. |
| xai-grok-4-3 | FINANCIALS | 25.0 | 0.03943044906900317 | 0.009857612267250793 | Upcoming bank earnings and resilient consumer income data support sector positioning. |
| xai-grok-4-3 | HEALTHCARE | 25.0 | 0.018866741882913596 | 0.004716685470728399 | Strong recent relative returns and defensive characteristics amid mixed macro data. |
| xai-grok-4-3 | INDUSTRIALS | 20.0 | -0.01919720767888311 | -0.003839441535776622 | Positive 30-day relative performance and exposure to domestic demand trends. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | SP500 | 4 | 0.65 | 0.0017029607380389944 | 0.012953313951682113 | 0.011250353213643118 | 0.2378455450484663 |  | True | True |
| anthropic-claude-opus-4-8 | FINANCIALS | 5 | 0.6 | 0.03943044906900317 | 0.011054687795199865 | 0.00935172705716087 | 0.23974417120494856 |  | True | True |
| xai-grok-4-3 | SMALL_VALUE | 4 | 0.55 | -0.0021198863380090804 | 0.010098890300799846 | 0.008395929562760852 | 0.24069996869934857 |  | True | True |
| anthropic-claude-opus-4-7 | HEALTHCARE | 5 | 0.55 | 0.018866741882913596 | 0.004621790835506196 | 0.0029188300974672017 | 0.24617706816464222 |  | True | True |
| anthropic-claude-fable-5 | HEALTHCARE | 5 | 0.5 | 0.018866741882913596 | 0.004537399167932195 | 0.002834438429893201 | 0.24626145983221623 |  | True | True |
| openai-gpt-5-5 | REGIONAL_BANKS | 5 | 0.57 | -0.0015752486401451327 | -0.012136463320782803 | -0.013839424058821798 | 0.2629353223209312 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | HEALTHCARE | 0.002834438429893201 | 0.27101 | 0.010458796464681012 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 3738d4f6be5fc14989131b7bd65d5822ada04471f07d71b8ceef5d9a56553477 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 7858eef0aa73ea38b28daacc4aaa57e57b110de6456378f1697ff1cd79ca213c |
| manifest.yaml | b8b3a13a49f58c6eb1879788779251f362700f45a5956ef276fd1ff029bfa9dd |
| market_data/universe_trailing_returns.csv | fb5dc17daf1e0f939405696981e26a2673dbc70b63fb830608f857a9f5566763 |
| market_data/universe_trailing_returns.md | a18f671af37c4e4d52095bdc6102c07e11bff2764f37450504d357722aebe9a9 |
| market_data/universe_trailing_returns.json | 3ba5033579de0dc0c723f050ac717d42f50508fcccb52ebe37a0a0bd879243f2 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 3199804d98151c4131093adf80706680a72376b94ef7269cc4aa32f6f5f95a06 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 8709ac7c84a704dbb0f1c7472daf09c478fd3e410b70eb23fc66ce5c2356d605 | yes |
| Final briefing | research/final_briefing.md | model-facing | 3738d4f6be5fc14989131b7bd65d5822ada04471f07d71b8ceef5d9a56553477 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
