# CapitalBench Report: CB-2026-06-25-1M / official-20260625-no-fable

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260625-no-fable
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-06-25-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-06-25
- Decision deadline: 2026-06-26T02:30:00Z
- Horizon: one month
- Entry date: 2026-06-25
- Exit date: 2026-07-24
- Entry rule: Use adjusted close prices on Thursday, June 25, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Friday, July 24, 2026 as the one-month exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SMALL_CAP | 5 | 0.65 | Focus on US small-cap, biotech, industrials, and healthcare for catalysts from manufacturing strength, Micron-like tech spillovers, and macro data releases before July 24 exit. | June CPI release on July 14 could reinforce high inflation and pressure rate-sensitive holdings; FOMC minutes on July 8 may signal tighter policy path affecting equity valuations; Employment report on July 2 could shift growth expectations and small-cap momentum; Potential reversal in biotech and small-cap outperformance if risk appetite fades |
| anthropic-claude-opus-4-8 | anthropic | portfolio | INDUSTRIALS | 5 | 0.55 | Overweight industrials, value, healthcare, and financials for catalyst-backed relative strength, with a fundamentals-driven semiconductor stake from Micron's earnings beat. | Semiconductor volatility (SMH 64% annualized vol) could reverse sharply on any AI-spending or earnings disappointment before the July 24 exit.; Hot inflation prints (CPI 4.2% YoY, PCE 4.1%) ahead of July 14 CPI and July 28-29 FOMC could pressure rate-sensitive equities and trigger broad risk-off.; Crowded cyclical/value rotation may reverse if June payrolls (July 2) or durable-goods data disappoint, hurting industrials and financials simultaneously.; Healthcare and financials gains partly reflect recent momentum that could fade; reversal risk if defensive flows unwind. |
| anthropic-claude-opus-4-7 | anthropic | portfolio | BIOTECH | 5 | 0.55 | Balance pro-cyclical breakout sectors with a defensive healthcare anchor and a semiconductor catalyst play following Micron's guidance. | Sticky 4.2% CPI/4.1% PCE could push July FOMC hawkish, hitting rate-sensitive banks and biotech; Semiconductor momentum reversal if Micron-driven enthusiasm fades or QQQ weakness persists; Biotech high volatility (34% vol) and reversal risk after sharp 30d run; Small-cap/cyclical rotation could unwind if growth data softens; Concentration in US cyclicals underperforms if defensive bond proxies lead |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.61 | I expect semiconductors, biotech, regional banks, small value, and industrials to outperform the S&P 500 over the month if economic resilience and risk appetite persist. The allocation is aggressive because the objective is relative one-month return rather than drawdown control. | Hot June CPI or PPI data could lift rate expectations, pressure high-beta equities, and reverse small-cap and biotech strength.; Semiconductor positioning may be crowded after very large 6-month and 1-year gains; any AI-demand skepticism or earnings disappointment could hit the largest allocation.; Regional banks could underperform if credit-quality, deposit-cost, or commercial real estate concerns resurface.; Recent strength in biotech, regional banks, and industrials may reverse if market leadership rotates back to defensive assets or mega-cap growth.; A broad risk-off move before the July 24 close would likely hurt the portfolio because all holdings are equity and mostly above-average volatility. |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.75 | Overweighting semiconductors and tech based on strong Micron earnings and guidance, balanced with equal-weight broad market exposure. | A hotter-than-expected CPI or PPI print in mid-July could lead to a rapid repricing of rate expectations, disproportionately hurting high-multiple technology stocks.; The semiconductor sector's strong recent momentum leaves it vulnerable to sharp reversals if any negative industry news emerges before the exit date.; Broader market volatility could increase if the upcoming employment report shows unexpected weakness, undermining the soft-landing narrative. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 109.30999755859375 | 136.69000244140625 | 0.25048033569057493 | 1 |
| ETHEREUM_ETF | Ethereum ETF | 11.739999771118164 | 14.039999961853027 | 0.19591143403538602 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 16.11 | 17.950000762939453 | 0.11421482079077916 | 3 |
| ENERGY | Energy Sector | 54.09 | 59.619998931884766 | 0.1022369926397626 | 4 |
| BITCOIN_ETF | Bitcoin ETF | 33.52000045776367 | 36.349998474121094 | 0.08442714730637646 | 5 |
| CYBERSECURITY | Cybersecurity | 83.66 | 88.4000015258789 | 0.05665791926702024 | 6 |
| FINANCIALS | Financials Sector | 53.45 | 56.310001373291016 | 0.053507977049410904 | 7 |
| CHINA | China Equities | 50.78 | 53.33000183105469 | 0.05021665677539744 | 8 |
| AGRICULTURE | Agriculture Commodities | 26.920000076293945 | 28.239999771118164 | 0.0490341638589602 | 9 |
| BRAZIL | Brazil Equities | 34.18 | 35.72999954223633 | 0.04534814342411719 | 10 |
| HEALTHCARE | Healthcare Sector | 155.63 | 162.57000732421875 | 0.04459299186672716 | 11 |
| DIVIDEND | US Dividend Equities | 31.96 | 33.290000915527344 | 0.041614546793721674 | 12 |
| SOFTWARE | Software | 84.76 | 87.9800033569336 | 0.037989657349381645 | 13 |
| COPPER | Copper | 36.97999954223633 | 38.349998474121094 | 0.037047024035790965 | 14 |
| LOW_VOL | US Low Volatility Equities | 74.7611186211 | 77.19000244140625 | 0.032488596547306736 | 15 |
| REAL_ESTATE | Real Estate Sector | 44.59 | 45.95000076293945 | 0.03050012924286727 | 16 |
| UNITED_KINGDOM | United Kingdom Equities | 45.88 | 47.22999954223633 | 0.029424575898786554 | 17 |
| AUSTRALIA | Australia Equities | 27.93 | 28.719999313354492 | 0.02828497362529503 | 18 |
| CANADA | Canada Equities | 57.62 | 59.06999969482422 | 0.025164868011527508 | 19 |
| LARGE_VALUE | US Large-Cap Value | 244.41 | 248.24000549316406 | 0.015670412393781197 | 20 |
| REGIONAL_BANKS | Regional Banks | 74.77 | 75.7300033569336 | 0.012839418977311778 | 21 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 237.38 | 240.13999938964844 | 0.011626924718377563 | 22 |
| UTILITIES | Utilities Sector | 45.85 | 46.290000915527344 | 0.009596530327750097 | 23 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 211.75 | 213.57000732421875 | 0.008595075911304706 | 24 |
| GOLD | Gold | 75.71 | 76.2300033569336 | 0.006868357640121614 | 25 |
| COMMUNICATIONS | Communication Services Sector | 105.58 | 106.30000305175781 | 0.006819502289806989 | 26 |
| EUROPE | Europe Equities | 87.83 | 88.41000366210938 | 0.006603707868716668 | 27 |
| SP500 | S&P 500 | 734.3 | 738.9299926757812 | 0.006305314824705643 | 28 |
| SMALL_VALUE | US Small-Cap Value | 220.11 | 221.4199981689453 | 0.00595156135089403 | 29 |
| TOTAL_US_MARKET | Total US Stock Market | 362.9342419845 | 364.79998779296875 | 0.005140726866296852 | 30 |
| SILVER | Silver | 52.36000061035156 | 52.59000015258789 | 0.004392657363545993 | 31 |
| US_DOLLAR | US Dollar | 28.479999542236328 | 28.579999923706055 | 0.0035112494057951693 | 32 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.3325754212 | 91.61000061035156 | 0.0030375272773395245 | 33 |
| CONSUMER_STAPLES | Consumer Staples Sector | 83.94 | 84.12999725341797 | 0.0022634888422441435 | 34 |
| EURO | Euro | 104.8703384399414 | 104.9469985961914 | 0.000730999416902911 | 35 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 36 |
| MEXICO | Mexico Equities | 75.53 | 75.44999694824219 | -0.001059222186651887 | 37 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.5115724048 | 79.2300033569336 | -0.003541233550670042 | 38 |
| LARGE_GROWTH | US Large-Cap Growth | 118.1 | 117.6500015258789 | -0.003810317308391986 | 39 |
| BIOTECH | Biotechnology | 151.59 | 150.47999572753906 | -0.007322410927244172 | 40 |
| INDUSTRIALS | Industrials Sector | 184.12 | 182.66000366210938 | -0.00792959123338377 | 41 |
| TIPS | Treasury Inflation-Protected Securities | 108.4393425303 | 107.5 | -0.00866237758715227 | 42 |
| MID_CAP | US Mid-Cap Stocks | 76.46 | 75.7699966430664 | -0.00902437034964143 | 43 |
| MATERIALS | Materials Sector | 51.84 | 51.2599983215332 | -0.011188303982770043 | 44 |
| YEN | Japanese Yen | 56.689998626708984 | 56.040000915527344 | -0.011465826899410114 | 45 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.3785499326 | 47.79999923706055 | -0.011958826718565962 | 46 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.9179089799 | 97.45999908447266 | -0.014738583846567122 | 47 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.4774607629 | 93.02999877929688 | -0.015320712177433138 | 48 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.5806885106 | 93.11000061035156 | -0.015549557984911533 | 49 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.1596824949 | 94.63999938964844 | -0.015803745039738026 | 50 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.2915482618 | 105.55000305175781 | -0.016231895599014723 | 51 |
| EMERGING_MARKETS | Emerging Markets | 58.8 | 57.79999923706055 | -0.017006815696249178 | 52 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.16 | 69.70999908447266 | -0.020376628942205488 | 53 |
| JAPAN | Japan Equities | 93.39 | 91.20999908447266 | -0.023342980142706304 | 54 |
| SMALL_CAP | US Small-Cap Stocks | 298.91 | 291.1700134277344 | -0.02589403690831904 | 55 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 109.1161608155 | 106.2300033569336 | -0.02645032080487586 | 56 |
| INDIA | India Equities | 49.43 | 48.02000045776367 | -0.028525177872472773 | 57 |
| SOUTH_AFRICA | South Africa Equities | 63.17 | 61.06999969482422 | -0.03324363313559886 | 58 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 113.35 | 109.41000366210938 | -0.034759561869348254 | 59 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 87.0263681494 | 83.25 | -0.043393378693191376 | 60 |
| NASDAQ100 | Nasdaq 100 | 716.38 | 684.22998046875 | -0.044878443746684704 | 61 |
| TECHNOLOGY | Technology Sector | 184.57 | 175.8800048828125 | -0.04708238130350273 | 62 |
| METALS_MINING | Metals and Mining | 108.74 | 101.73999786376953 | -0.06437375516121446 | 63 |
| TAIWAN | Taiwan Equities | 104.91 | 98.01000213623047 | -0.06577064020369394 | 64 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 123.84 | 114.01499938964844 | -0.07933624523862703 | 65 |
| BROAD_AI_TECH | Broad AI Technology | 64.1795482847 | 57.97999954223633 | -0.0965969519598755 | 66 |
| MOMENTUM | US Momentum Equities | 339.3 | 306.3900146484375 | -0.09699376761438994 | 67 |
| SOLAR | Solar Energy | 57.87 | 51.279998779296875 | -0.1138759498998293 | 68 |
| SEMICONDUCTORS | Semiconductors | 636.88 | 561.1900024414062 | -0.11884499051405872 | 69 |
| SOUTH_KOREA | South Korea Equities | 205.0 | 162.9600067138672 | -0.2050731379811357 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | BIOTECH | 25.0 | -0.007322410927244172 | -0.001830602731811043 | Strong recent breakout with 13.8% 30d gain at 52w high; XBI momentum supported by risk-on small/mid cap rotation and improving claims data. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 20.0 | -0.00792959123338377 | -0.001585918246676754 | Flash manufacturing PMI 55.7 (49-month high) supports cyclicals; XLI at 52w highs with broad participation. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 15.0 | 0.04459299186672716 | 0.006688948780009074 | Defensive sector breaking out (+5.25% 30d, +7.17% vs SPY) with low beta amid sticky inflation prints; offers ballast. |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 20.0 | -0.11884499051405872 | -0.023768998102811745 | Micron blowout guide ($50B revenue, 86% GM) signals HBM/AI demand re-acceleration; sector catalyst for SMH near-term. |
| anthropic-claude-opus-4-7 | REGIONAL_BANKS | 20.0 | 0.012839418977311778 | 0.0025678837954623557 | KRE at 52w high with steepening curve (10y-2y +30bps), low claims, and improving credit; benefits from small-cap rotation. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 25.0 | -0.00792959123338377 | -0.0019823978083459426 | Strong relative strength with +5.89% 30d return, manufacturing PMI at 49-month high (55.7), and durables ex-transport up 1.3%; cyclical leadership with manageable volatility. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 20.0 | 0.04459299186672716 | 0.008918598373345432 | Defensive leadership with +5.25% 30d, low beta (0.40), and rotation into the sector; biotech strength (XBI +13.79%) supports group momentum heading into resilient earnings. |
| anthropic-claude-opus-4-8 | LARGE_VALUE | 20.0 | 0.015670412393781197 | 0.0031340824787562394 | Value outperforming growth with +2.88% 30d vs broad market decline, lower beta (0.76), and tilt toward financials/cyclicals that are strengthening as Nasdaq weakens. |
| anthropic-claude-opus-4-8 | FINANCIALS | 15.0 | 0.053507977049410904 | 0.008026196557411635 | Regional banks (KRE +6.97%) and XLF +3.44% showing strength; steeper curve and solid claims data support credit; July earnings season catalyst for banks. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 20.0 | -0.11884499051405872 | -0.023768998102811745 | Micron's blowout FY Q3 (revenue $41.46B vs $23.86B prior) and guidance for ~86% margins and $50B Q4 confirm AI/HBM demand; concrete fundamental catalyst supports the group despite high volatility. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 50.0 | -0.11884499051405872 | -0.05942249525702936 | Micron's strong earnings beat, upward guidance, and high-volume HBM4 shipments provide a direct, near-term catalyst for the semiconductor sector. |
| google-gemini-3-1-pro | TECHNOLOGY | 30.0 | -0.04708238130350273 | -0.014124714391050818 | Broader technology exposure benefits from the semiconductor catalyst and a strong US Manufacturing PMI reading of 55.7. |
| google-gemini-3-1-pro | EQUAL_WEIGHT_SP500 | 20.0 | 0.008595075911304706 | 0.0017190151822609413 | Provides diversified US equity exposure to capture broader economic resilience indicated by upward GDP revisions and strong PMI data, while reducing mega-cap concentration risk. |
| openai-gpt-5-5 | SEMICONDUCTORS | 30.0 | -0.11884499051405872 | -0.03565349715421762 | Micron's exceptionally strong Q3 results and Q4 guidance point to continued AI-memory and HBM demand that could support semiconductor sentiment during the one-month window, despite high volatility and recent weekly weakness. |
| openai-gpt-5-5 | BIOTECH | 25.0 | -0.007322410927244172 | -0.001830602731811043 | Biotech has strong recent relative performance and may benefit from improving risk appetite and healthcare sector strength; independent support is limited, so the position carries reversal risk. |
| openai-gpt-5-5 | REGIONAL_BANKS | 20.0 | 0.012839418977311778 | 0.0025678837954623557 | Regional banks have been outperforming, and a positively sloped 2s/10s Treasury curve with firm employment and growth data may support bank earnings expectations and credit-risk sentiment. |
| openai-gpt-5-5 | SMALL_VALUE | 15.0 | 0.00595156135089403 | 0.0008927342026341044 | Small-cap value exposure aligns with recent market broadening, strong Russell 2000 year-to-date performance, domestic growth resilience, and less dependence on mega-cap growth leadership. |
| openai-gpt-5-5 | INDUSTRIALS | 10.0 | -0.00792959123338377 | -0.000792959123338377 | Industrials are supported by the flash manufacturing PMI at a 49-month high, positive shipments and unfilled orders data, and recent relative strength versus the S&P 500. |
| xai-grok-4-3 | SMALL_CAP | 30.0 | -0.02589403690831904 | -0.007768211072495711 | Domestic growth sensitivity aligns with strong US manufacturing PMI and Q1 GDP revision. |
| xai-grok-4-3 | BIOTECH | 25.0 | -0.007322410927244172 | -0.001830602731811043 | Recent outperformance and clinical/regulatory catalysts expected within one-month window. |
| xai-grok-4-3 | INDUSTRIALS | 20.0 | -0.00792959123338377 | -0.001585918246676754 | Flash manufacturing PMI at 55.7 supports near-term industrial activity and orders. |
| xai-grok-4-3 | HEALTHCARE | 15.0 | 0.04459299186672716 | 0.006688948780009074 | Defensive exposure with positive 30-day relative performance amid elevated inflation data. |
| xai-grok-4-3 | EQUAL_WEIGHT_SP500 | 10.0 | 0.008595075911304706 | 0.0008595075911304707 | Broad diversification with reduced mega-cap concentration to capture mid/small rotation. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SMALL_CAP | 5 | 0.65 | -0.02589403690831904 | -0.0036362756798439637 | -0.009941590504549607 | 0.2541166113704189 |  | False | False |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 5 | 0.55 | -0.00792959123338377 | -0.00567251850164438 | -0.011977833326350024 | 0.25615285419221934 |  | False | False |
| anthropic-claude-opus-4-7 | BIOTECH | 5 | 0.55 | -0.007322410927244172 | -0.01792868650582811 | -0.024234001330533755 | 0.26840902219640306 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.61 | -0.11884499051405872 | -0.03481644101127058 | -0.04112175583597622 | 0.2852967767018455 |  | False | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.75 | -0.11884499051405872 | -0.07182819446581923 | -0.07813350929052487 | 0.32230853015639416 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 833e3b256d8a101b15bbfec9218a8e488aa2043c1c3e26c4fecdfcd334c16dcb |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 7858eef0aa73ea38b28daacc4aaa57e57b110de6456378f1697ff1cd79ca213c |
| manifest.yaml | 6de8ea05648d71967718588fd1144c64702df5573f5b663a089333f89fcc2952 |
| market_data/universe_trailing_returns.csv | 588a18556cdd760fe00850402f904f0091c916028909ec54a8a91f87d3923222 |
| market_data/universe_trailing_returns.md | 6f45e81899cde555e6a0c994a0a81cc8ed5fd622e04b29c8b822ca16590655f8 |
| market_data/universe_trailing_returns.json | 78ca1f08d33196266f5984801e46bd4fdbec70164784010f15bb7816ab57ac5d |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | d3fef3527a2acece67484f58a15b279dfd41e21b2b5a8ee2044c5abb24864c37 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 070d5246b1455a7f7f46a07871bf4cad854a14f9195f6671a91d5a3a4e088b75 | yes |
| Final briefing | research/final_briefing.md | model-facing | 833e3b256d8a101b15bbfec9218a8e488aa2043c1c3e26c4fecdfcd334c16dcb | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
