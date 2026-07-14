# CapitalBench Report: CB-2026-07-07-1W / official-20260707

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260707
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-07-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-07
- Decision deadline: 2026-07-08T07:30:00Z
- Horizon: one week
- Entry date: 2026-07-07
- Exit date: 2026-07-14
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | openai | portfolio | OIL | 5 | 0.38 | A one-week overweight to oil and energy targets the clearest fresh catalyst in the briefing, while financials have scheduled earnings before the exit close. Smaller biotech and agriculture positions add return potential and diversification but acknowledge weaker near-term catalyst support. | A rapid de-escalation in Iran or Strait of Hormuz concerns could reverse crude oil and energy equity gains.; June CPI could come in hotter than expected, pressuring equities broadly and especially financials through rate and credit-quality concerns.; JPMorgan or Wells Fargo earnings could highlight deposit, loan-loss, or net-interest-margin weakness, hurting the financials allocation.; Biotech’s sharp recent run could mean crowded positioning and a near-term reversal without a fresh sector catalyst.; Commodity exposures could underperform if the US dollar strengthens or if inflation fears fade before the exit close. |
| google-gemini-3-1-pro | google | portfolio | ENERGY | 3 | 0.65 | Overweight energy and oil due to geopolitical catalysts, balanced with defensive healthcare exposure. | Geopolitical tensions could ease, leading to a drop in oil prices.; Broader market weakness could drag down all sectors, including energy and healthcare.; Upcoming CPI data could surprise to the upside, causing a market sell-off. |
| xai-grok-4-3 | xai | portfolio | LARGE_VALUE | 3 | 0.55 | Weak payrolls and elevated inflation data favor value tilt; oil supply risks support energy exposure ahead of CPI release. | CPI release on July 14 could trigger volatility if hotter than expected; FOMC minutes on July 8 may shift rate expectations; Tech sector weakness could spill over to broader market |
| anthropic-claude-fable-5 | anthropic | portfolio | FINANCIALS | 5 | 0.5 | Overweight financials into big-bank earnings, energy on Iran supply catalysts, and value/healthcare defensives against sticky-inflation CPI risk; small biotech kicker with acknowledged reversal risk. | A soft July 14 CPI could spark a growth/tech rebound, leaving this value/defensive tilt to underperform SPY; JPMorgan/Wells Fargo earnings disappoint or guide cautiously, hitting financials before the exit close; Oil retraces if Hormuz tensions ease or the cease-fire holds, dragging energy; Biotech's 30-day surge mean-reverts without fresh catalysts |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 5 | 0.55 | Defensive/value equity plus financials earnings catalyst, cushioned by short Treasuries, to seek alpha over SPY through a CPI- and Fed-minutes-heavy week. | Hot June CPI (July 14) or hawkish FOMC minutes could pressure equities broadly and lift Treasury yields; Bank earnings (JPM/WFC July 14) could disappoint on credit/NIM, hurting the financials overweight; A sharp tech/semiconductor rebound would cause underperformance versus SPY given underweight to QQQ/SMH; Defensive value/healthcare rally is recent and could mean-revert (reversal risk) with limited fresh catalyst support in the briefing |
| anthropic-claude-opus-4-7 | anthropic | portfolio | FINANCIALS | 5 | 0.55 | Barbell of catalyst-driven Financials with defensive Healthcare and Low-Vol, plus gold and T-bills as hedges against CPI and geopolitical tail risks in a soft-labor macro backdrop. | Hot CPI on July 14 hits rate-sensitive defensives and gold simultaneously; Bank earnings disappoint on NII or credit, reversing Financials' recent 7.5% run (continuation/reversal risk); Tech-led rebound (SMH/QQQ oversold bounce) causes defensive underperformance vs SPY; Oil spike from Iran/Hormuz escalation broadly pressures equities; FOMC minutes read more hawkish than expected, hurting duration-sensitive positions |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 108.92 | 120.16999816894531 | 0.10328679920074646 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 13.51 | 14.180000305175781 | 0.04959291674136068 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 16.32 | 17.08 | 0.04656862745098023 | 3 |
| ENERGY | Energy Sector | 54.64 | 56.95 | 0.04227672035139096 | 4 |
| BRAZIL | Brazil Equities | 34.64 | 36.029998779296875 | 0.04012698554552174 | 5 |
| SEMICONDUCTORS | Semiconductors | 581.45 | 600.31 | 0.032436151001805635 | 6 |
| COPPER | Copper | 37.39 | 38.540000915527344 | 0.030756911354034244 | 7 |
| CHINA | China Equities | 51.78 | 53.23 | 0.02800308999613743 | 8 |
| CYBERSECURITY | Cybersecurity | 92.21 | 94.73 | 0.02732892311029178 | 9 |
| TECHNOLOGY | Technology Sector | 179.18 | 183.62 | 0.024779551289206392 | 10 |
| MOMENTUM | US Momentum Equities | 312.44 | 319.76 | 0.023428498271668152 | 11 |
| AUSTRALIA | Australia Equities | 28.13 | 28.709999084472656 | 0.020618524154733642 | 12 |
| METALS_MINING | Metals and Mining | 102.47 | 104.42 | 0.01902995998828927 | 13 |
| LARGE_GROWTH | US Large-Cap Growth | 121.35 | 123.23 | 0.0154923774206841 | 14 |
| NASDAQ100 | Nasdaq 100 | 709.43 | 719.69 | 0.014462314816120037 | 15 |
| CANADA | Canada Equities | 58.36 | 59.18000030517578 | 0.014050724900201983 | 16 |
| BITCOIN_ETF | Bitcoin ETF | 36.15 | 36.58000183105469 | 0.011894933085883519 | 17 |
| JAPAN | Japan Equities | 93.07 | 93.89 | 0.008810572687224738 | 18 |
| SOLAR | Solar Energy | 54.81 | 55.13 | 0.005838350665936964 | 19 |
| SP500 | S&P 500 | 747.71 | 751.83 | 0.00551015768145402 | 20 |
| TOTAL_US_MARKET | Total US Stock Market | 369.61 | 371.16 | 0.004193609480263039 | 21 |
| MEXICO | Mexico Equities | 75.04 | 75.33999633789062 | 0.003997819001740677 | 22 |
| COMMUNICATIONS | Communication Services Sector | 111.02 | 111.45 | 0.0038731760043235752 | 23 |
| EMERGING_MARKETS | Emerging Markets | 58.88 | 59.08 | 0.0033967391304348116 | 24 |
| AGRICULTURE | Agriculture Commodities | 27.55 | 27.6299991607666 | 0.002903780790076249 | 25 |
| FINANCIALS | Financials Sector | 56.05 | 56.18 | 0.0023193577163247436 | 26 |
| MID_CAP | US Mid-Cap Stocks | 75.47 | 75.57 | 0.0013250298131706195 | 27 |
| EURO | Euro | 105.307 | 105.38999938964844 | 0.0007881659305499777 | 28 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.45 | 91.51 | 0.0006560962274466675 | 29 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 30 |
| TAIWAN | Taiwan Equities | 101.88 | 101.87999725341797 | -2.695899126159418e-08 | 31 |
| UTILITIES | Utilities Sector | 45.7 | 45.69 | -0.00021881838074411242 | 32 |
| US_DOLLAR | US Dollar | 28.4 | 28.389999389648438 | -0.00035213416730850433 | 33 |
| REGIONAL_BANKS | Regional Banks | 75.07 | 75.0 | -0.0009324630345010076 | 34 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.76 | 79.68 | -0.0010030090270811698 | 35 |
| YEN | Japanese Yen | 56.63 | 56.56999969482422 | -0.001059514483061741 | 36 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.02 | 47.959999084472656 | -0.00124949844913258 | 37 |
| TIPS | Treasury Inflation-Protected Securities | 108.17 | 108.01 | -0.0014791531848016293 | 38 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.7 | 93.55 | -0.0016008537886873508 | 39 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.84 | 93.66999816894531 | -0.0018116137154166045 | 40 |
| BROAD_AI_TECH | Broad AI Technology | 62.08 | 61.96 | -0.0019329896907216426 | 41 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.21 | 98.0 | -0.002138275124732636 | 42 |
| SOUTH_AFRICA | South Africa Equities | 63.59 | 63.45000076293945 | -0.002201592028000521 | 43 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.78 | 70.6 | -0.002543091268720099 | 44 |
| SMALL_VALUE | US Small-Cap Value | 220.18 | 219.6 | -0.002634208374965974 | 45 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.24 | 106.94999694824219 | -0.0027042433024786483 | 46 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.94 | 95.56999969482422 | -0.0038565802082111134 | 47 |
| SOFTWARE | Software | 94.13 | 93.63 | -0.005311802825879064 | 48 |
| LARGE_VALUE | US Large-Cap Value | 247.74 | 246.37 | -0.0055299911197222995 | 49 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.55 | 84.08 | -0.005558840922531005 | 50 |
| SMALL_CAP | US Small-Cap Stocks | 296.19 | 294.51 | -0.005672034842499785 | 51 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 214.73 | 213.45 | -0.005960974246728479 | 52 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 107.88 | 107.21 | -0.0062106043752317985 | 53 |
| EUROPE | Europe Equities | 89.04 | 88.3 | -0.008310871518418805 | 54 |
| REAL_ESTATE | Real Estate Sector | 44.89 | 44.48 | -0.009133437291156232 | 55 |
| DIVIDEND | US Dividend Equities | 32.54 | 32.2 | -0.010448678549477508 | 56 |
| INDUSTRIALS | Industrials Sector | 182.38 | 180.45 | -0.010582300690865298 | 57 |
| INDIA | India Equities | 49.33 | 48.73 | -0.012162983985404496 | 58 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.39 | 115.9 | -0.01269273362296619 | 59 |
| LOW_VOL | US Low Volatility Equities | 76.92 | 75.91 | -0.013130525221008882 | 60 |
| GOLD | Gold | 77.37 | 76.27 | -0.01421739692387236 | 61 |
| MATERIALS | Materials Sector | 51.51 | 50.64 | -0.016889924286546232 | 62 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.86 | 83.42 | -0.016969125618666037 | 63 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 124.41 | 122.28 | -0.017120810224258487 | 64 |
| UNITED_KINGDOM | United Kingdom Equities | 47.13 | 46.310001373291016 | -0.017398655351347103 | 65 |
| SILVER | Silver | 54.46 | 53.16999816894531 | -0.023687143427372215 | 66 |
| SOUTH_KOREA | South Korea Equities | 181.29 | 176.97999572753906 | -0.023774087221914764 | 67 |
| HEALTHCARE | Healthcare Sector | 164.44 | 158.29 | -0.037399659450255474 | 68 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 245.11 | 235.27000427246094 | -0.04014522348145355 | 69 |
| BIOTECH | Biotechnology | 163.87 | 155.45 | -0.051382193201928494 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | FINANCIALS | 25.0 | 0.0023193577163247436 | 0.0005798394290811859 | JPMorgan and Wells Fargo Q2 earnings land July 14 before the exit close; sector strength is supported by resilient activity data and a hold-steady Fed, not just trailing returns. |
| anthropic-claude-fable-5 | LARGE_VALUE | 20.0 | -0.0055299911197222995 | -0.00110599822394446 | Value tilt benefits from financials/energy strength, at 52-week highs with low volatility; defensive against tech weakness and sticky-inflation CPI risk. |
| anthropic-claude-fable-5 | HEALTHCARE | 20.0 | -0.037399659450255474 | -0.007479931890051095 | Defensive sector with strong recent breadth (63% up days), low beta to a potentially hot July 14 CPI, and no drawdown from highs. |
| anthropic-claude-fable-5 | ENERGY | 20.0 | 0.04227672035139096 | 0.008455344070278193 | Iranian sanction license cancellation and Hormuz uncertainty are live supply catalysts; oil up 2.6% on July 7 with sector still 12% off highs. |
| anthropic-claude-fable-5 | BIOTECH | 15.0 | -0.051382193201928494 | -0.007707328980289274 | Strong ongoing catalyst-driven rally (M&A/clinical momentum implied by 27% 30d outperformance) with high up-day share; reversal risk acknowledged as briefing support is limited. |
| anthropic-claude-opus-4-7 | FINANCIALS | 30.0 | 0.0023193577163247436 | 0.000695807314897423 | JPM and WFC report July 14 within the scoring window; sector has strong recent breadth (+7.55% 30d) with solid ISM services and steepening backdrop. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 25.0 | -0.037399659450255474 | -0.009349914862563868 | Defensive sector leadership (+7.94% 30d, +6.31% vs SPY) with low beta; positioned well if soft payrolls drive defensive rotation. |
| anthropic-claude-opus-4-7 | LOW_VOL | 20.0 | -0.013130525221008882 | -0.0026261050442017765 | Weakening labor market (57k payrolls, downward revisions) and elevated VIX favor low-vol defensive tilt into CPI print. |
| anthropic-claude-opus-4-7 | GOLD | 15.0 | -0.01421739692387236 | -0.002132609538580854 | Iran sanctions reinstated and Strait of Hormuz uncertainty; hedge against CPI upside surprise given sticky core PCE at 3.4%. |
| anthropic-claude-opus-4-7 | SHORT_TREASURY | 10.0 | 0.0006560962274466675 | 6.560962274466675e-05 | Dry powder buffer against CPI/earnings volatility with positive carry. |
| anthropic-claude-opus-4-8 | FINANCIALS | 30.0 | 0.0023193577163247436 | 0.000695807314897423 | JPMorgan and Wells Fargo Q2 earnings on July 14 are catalysts inside the window; XLF showed leadership (+4.55% 7d, +7.55% 30d) with low volatility and near 52w highs, supported by bank earnings kickoff. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 25.0 | -0.037399659450255474 | -0.009349914862563868 | Defensive sector with strong recent breadth (+3.64% 7d, +7.94% 30d, +6.31% vs SPY 30d) at 52w highs and low beta (0.35); provides ballast versus tech-led weakness. |
| anthropic-claude-opus-4-8 | LOW_VOL | 20.0 | -0.013130525221008882 | -0.0026261050442017765 | Defensive factor at 52w highs with very low beta (0.06); useful given elevated VIX, sticky core PCE, and CPI/FOMC-minutes event risk in the window. |
| anthropic-claude-opus-4-8 | LARGE_VALUE | 15.0 | -0.0055299911197222995 | -0.0008294986679583449 | Value leadership (+2.19% 7d, +3.48% vs SPY 30d), lower vol, financial/energy tilt aligns with bank earnings and firmer oil; at 52w highs. |
| anthropic-claude-opus-4-8 | SHORT_TREASURY | 10.0 | 0.0006560962274466675 | 6.560962274466675e-05 | Cash-like buffer against CPI/FOMC-minutes volatility with positive carry and near-zero drawdown. |
| google-gemini-3-1-pro | ENERGY | 40.0 | 0.04227672035139096 | 0.016910688140556386 | Energy prices are rising due to geopolitical tensions and supply constraints, as noted in the briefing. |
| google-gemini-3-1-pro | OIL | 30.0 | 0.10328679920074646 | 0.030986039760223936 | Direct exposure to crude oil, which is seeing upward pressure from canceled Iranian oil sales and Strait of Hormuz uncertainty. |
| google-gemini-3-1-pro | HEALTHCARE | 30.0 | -0.037399659450255474 | -0.011219897835076641 | A defensive sector that has shown recent strength and provides a buffer against broader market weakness. |
| openai-gpt-5-5 | OIL | 35.0 | 0.10328679920074646 | 0.03615037972026126 | Direct exposure to crude prices, where the briefing cites cancellation of a temporary license for sanctioned Iranian oil sales and renewed Strait of Hormuz traffic uncertainty; recent weakness leaves room for a sharp headline-driven rebound but volatility is high. |
| openai-gpt-5-5 | ENERGY | 25.0 | 0.04227672035139096 | 0.01056918008784774 | Energy equities should benefit if oil-price headlines persist through the week, while offering somewhat less direct futures-curve exposure than oil itself; the sector has lagged over 30 days despite strong longer-term returns. |
| openai-gpt-5-5 | FINANCIALS | 20.0 | 0.0023193577163247436 | 0.00046387154326494874 | JPMorgan and Wells Fargo report before the exit close, creating a near-window catalyst for bank and financial-sector sentiment; recent strength is supported by the scheduled earnings catalyst but could reverse on credit or margin concerns. |
| openai-gpt-5-5 | BIOTECH | 10.0 | -0.051382193201928494 | -0.00513821932019285 | Biotech has shown strong recent relative performance and healthcare has also been firm, suggesting risk appetite for the group; independent near-week catalysts are limited, so this is a smaller allocation given reversal risk. |
| openai-gpt-5-5 | AGRICULTURE | 10.0 | 0.002903780790076249 | 0.0002903780790076249 | Agriculture commodities provide diversified non-equity exposure with low S&P beta and recent positive performance, potentially helpful if inflation or commodity concerns intensify around CPI. |
| xai-grok-4-3 | LARGE_VALUE | 40.0 | -0.0055299911197222995 | -0.00221199644788892 | Recent strength in value equities aligns with stable rates and resilient ISM data supporting cyclical sectors. |
| xai-grok-4-3 | FINANCIALS | 35.0 | 0.0023193577163247436 | 0.0008117752007136603 | Financials positioned for potential stability in rates and positive sector momentum amid bank earnings window. |
| xai-grok-4-3 | ENERGY | 25.0 | 0.04227672035139096 | 0.01056918008784774 | Oil price support from Iran license cancellation and Hormuz uncertainty provides near-term catalyst. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | OIL | 5 | 0.38 | 0.10328679920074646 | 0.042335590110188726 | 0.036825432428734706 | 0.060951209090557734 |  | True | True |
| google-gemini-3-1-pro | ENERGY | 3 | 0.65 | 0.04227672035139096 | 0.036676830065703686 | 0.031166672384249666 | 0.06660996913504277 |  | True | True |
| xai-grok-4-3 | LARGE_VALUE | 3 | 0.55 | -0.0055299911197222995 | 0.009168958840672481 | 0.003658801159218461 | 0.09411784036007398 |  | True | True |
| anthropic-claude-fable-5 | FINANCIALS | 5 | 0.5 | 0.0023193577163247436 | -0.007258075594925449 | -0.012768233276379468 | 0.1105448747956719 |  | False | False |
| anthropic-claude-opus-4-8 | FINANCIALS | 5 | 0.55 | 0.0023193577163247436 | -0.0120441016370819 | -0.01755425931853592 | 0.11533090083782836 |  | False | False |
| anthropic-claude-opus-4-7 | FINANCIALS | 5 | 0.55 | 0.0023193577163247436 | -0.013347212507704409 | -0.01885737018915843 | 0.11663401170845086 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | c5384072ede9c13ed22ae6eef0ae2c0752798d06e3769a16a7f278928c7be30f |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 66320ebc013af445c33450b3005ec684487d06b5bca45c52a3ff9e8e24373e4c |
| manifest.yaml | 8d51750e5964c5c3f50ed69920bd01559783c7c1f13f5538ec05660dce2d792a |
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
| Final briefing | research/final_briefing.md | model-facing | c5384072ede9c13ed22ae6eef0ae2c0752798d06e3769a16a7f278928c7be30f | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
