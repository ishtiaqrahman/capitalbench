# CapitalBench Report: CB-2026-07-21-1M / official-v2-2-20260721-1m

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-20260721-1m
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-21-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-21
- Decision deadline: 2026-07-22T09:30:00Z
- Horizon: one month
- Entry date: 2026-07-21
- Exit date: 2026-08-21
- Entry rule: Use adjusted close prices on Tuesday, July 21, 2026 as the post-close entry snapshot, supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Friday, August 21, 2026 as the one-month exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | HEALTHCARE | 3 | 0.65 | Overweight energy and healthcare to balance cyclical upside with defensive stability. | A sudden reversal in oil prices due to geopolitical de-escalation or demand shocks.; Broader market volatility impacting equity allocations.; Underperformance of defensive sectors if risk appetite surges. |
| xai-grok-4-5 | xai | portfolio | ENERGY | 4 | 0.58 | Energy/oil leadership and commodity breadth offer the clearest one-month edge given supplied price context and oil settlement strength, while avoiding pure tech pullback names. Equal weights balance cluster caps and forecast dispersion. | Sharp oil price reversal on inventory or demand data; FOMC July 29 hawkish surprise triggering risk-off; High volatility in energy and biotech amplifying drawdowns; USD strength pressuring commodities |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SP500 | 3 | 0.55 | Overweight defensive quality sectors with positive relative momentum while anchoring to SPY ahead of FOMC and key data. | Hawkish FOMC or hot CPI triggers broad equity selloff; Defensive rotation reverses as growth/tech re-leads |
| xai-grok-4-3 | xai | portfolio | SP500 | 5 | 0.55 | Selected holdings have base forecasts above SPY while respecting cluster caps and allocation rules. | FOMC policy surprise on July 29; Oil price reversal below $85; Weaker than expected Q2 GDP |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.56 | SPY has modest positive one-month expected return but faces slowing payrolls, inflation uncertainty, a FOMC meeting, and concentrated leadership risk. Selected holdings have stronger base cases from either high quality evidence scores, positive active trends, near-term earnings/policy catalysts, or oil-linked momentum. | A broad risk-off move around July GDP, July employment, CPI/PPI, or FOMC communications could hurt all equity holdings versus SPY.; Semiconductor and biotech allocations have high volatility and could reverse sharply if earnings or guidance disappoint.; Oil and energy could fall on inventory builds, demand concerns, or geopolitical de-escalation, dragging the energy allocation.; SPY mega-cap concentration could outperform the diversified active basket, especially if technology leadership narrows again. |
| anthropic-claude-fable-5 | anthropic | portfolio | SP500 | 4 | 0.6 | Semis offer the strongest trend-plus-pullback setup into mega-cap AI earnings; energy is supported by supplied oil-price facts; healthcare offers defensive relative strength; SPY anchors the book. | Hawkish July 29 FOMC or hot Aug 12 CPI given 3.5% headline inflation; Disappointing AI capex guidance hitting semiconductors (high beta 2.3); Oil price reversal unwinding energy gains; Momentum unwind: high-vol prior winners continuing to mean-revert lower |
| openai-gpt-5-6-sol | openai | portfolio | SEMICONDUCTORS | 3 | 0.56 | Semiconductors provide the strongest expected upside, while broad commodities and dividend equities reduce dependence on a single technology outcome. The weighted one-month base forecast is 2.105%, implying 1.355 percentage points of expected alpha. | Semiconductor earnings disappoint or elevated Treasury yields compress growth-stock valuations.; Commodity prices reverse sharply if the energy shock fades or inflation data undershoot expectations.; Stronger-than-expected growth and risk appetite rotate capital away from dividend equities.; A broad equity correction overwhelms the portfolio's cross-cluster diversification. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.529999732971191 | 18.239999771118164 | 0.2553337994720202 | 1 |
| SILVER | Silver | 53.08000183105469 | 62.720001220703125 | 0.18161264237199992 | 2 |
| METALS_MINING | Metals and Mining | 101.5999984741211 | 119.33999633789062 | 0.17460628080903118 | 3 |
| SOUTH_AFRICA | South Africa Equities | 62.279998779296875 | 72.51000213623047 | 0.16425824594483207 | 4 |
| BITCOIN_ETF | Bitcoin ETF | 37.66999816894531 | 43.68000030517578 | 0.15954346770276828 | 5 |
| GOLD | Gold | 76.81999969482422 | 86.79000091552734 | 0.12978392684600415 | 6 |
| SOFTWARE | Software | 91.81999969482422 | 103.37000274658203 | 0.12578962197937016 | 7 |
| HEALTHCARE | Healthcare Sector | 160.25 | 174.6199951171875 | 0.08967235642550708 | 8 |
| ENERGY | Energy Sector | 58.5 | 63.63999938964844 | 0.08786323742988777 | 9 |
| BIOTECH | Biotechnology | 154.5 | 165.72999572753906 | 0.07268605648892601 | 10 |
| DIVIDEND | US Dividend Equities | 32.81999969482422 | 35.11000061035156 | 0.06977455627120199 | 11 |
| MATERIALS | Materials Sector | 50.099998474121094 | 53.540000915527344 | 0.0686627254726 | 12 |
| BROAD_COMMODITIES | Broad Commodities | 17.649999618530273 | 18.649999618530273 | 0.05665722502056747 | 13 |
| CANADA | Canada Equities | 59.04999923706055 | 62.36000061035156 | 0.056054215343894764 | 14 |
| AUSTRALIA | Australia Equities | 28.68000030517578 | 30.139999389648438 | 0.05090652262682083 | 15 |
| CYBERSECURITY | Cybersecurity | 90.58000183105469 | 94.8499984741211 | 0.04714061113655732 | 16 |
| UNITED_KINGDOM | United Kingdom Equities | 46.77000045776367 | 48.939998626708984 | 0.04639722359859633 | 17 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 120.0999984741211 | 125.58000183105469 | 0.045628671328538095 | 18 |
| OIL | Crude Oil | 128.85000610351562 | 134.63999938964844 | 0.04493591782588857 | 19 |
| EUROPE | Europe Equities | 88.76000213623047 | 92.72000122070312 | 0.044614679913986155 | 20 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.75999450683594 | 221.6699981689453 | 0.04187819088246458 | 21 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.47000122070312 | 73.41999816894531 | 0.04186174112588947 | 22 |
| BROAD_AI_TECH | Broad AI Technology | 61.0 | 63.43000030517578 | 0.03983607057665206 | 23 |
| LARGE_VALUE | US Large-Cap Value | 247.44000244140625 | 257.2900085449219 | 0.03980765440643785 | 24 |
| TAIWAN | Taiwan Equities | 100.58000183105469 | 104.30000305175781 | 0.03698549565500753 | 25 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 229.74000549316406 | 237.33999633789062 | 0.03308083338995438 | 26 |
| SOUTH_KOREA | South Korea Equities | 172.89999389648438 | 178.33999633789062 | 0.03146328879955429 | 27 |
| CHINA | China Equities | 54.0 | 55.65999984741211 | 0.030740737915039062 | 28 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 114.87000274658203 | 118.0199966430664 | 0.02742224968370266 | 29 |
| EMERGING_MARKETS | Emerging Markets | 58.86000061035156 | 60.45000076293945 | 0.027013254096165618 | 30 |
| YEN | Japanese Yen | 56.220001220703125 | 57.70000076293945 | 0.026325142477786168 | 31 |
| JAPAN | Japan Equities | 92.73999786376953 | 95.18000030517578 | 0.026310141229359152 | 32 |
| EURO | Euro | 105.2300033569336 | 107.80000305175781 | 0.02442268946915216 | 33 |
| FINANCIALS | Financials Sector | 56.11000061035156 | 57.47999954223633 | 0.02441630577405518 | 34 |
| TOTAL_US_MARKET | Total US Stock Market | 369.45001220703125 | 378.239990234375 | 0.02379206316663507 | 35 |
| SP500 | S&P 500 | 748.280029296875 | 765.719970703125 | 0.023306704339868034 | 36 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.05999755859375 | 85.98999786376953 | 0.022959794923030685 | 37 |
| MEXICO | Mexico Equities | 75.83999633789062 | 77.37999725341797 | 0.020305920225340834 | 38 |
| INDIA | India Equities | 48.779998779296875 | 49.63999938964844 | 0.01763018925528481 | 39 |
| TECHNOLOGY | Technology Sector | 180.77999877929688 | 183.30999755859375 | 0.013994904283551879 | 40 |
| MID_CAP | US Mid-Cap Stocks | 75.72000122070312 | 76.7699966430664 | 0.013866817293132883 | 41 |
| COMMUNICATIONS | Communication Services Sector | 110.02999877929688 | 111.4000015258789 | 0.012451174786705543 | 42 |
| COPPER | Copper | 39.529998779296875 | 39.9900016784668 | 0.011636805296610264 | 43 |
| SMALL_CAP | US Small-Cap Stocks | 296.5400085449219 | 299.9599914550781 | 0.011532956132757954 | 44 |
| INDUSTRIALS | Industrials Sector | 178.66000366210938 | 180.25 | 0.008899565125374709 | 45 |
| LARGE_GROWTH | US Large-Cap Growth | 121.33000183105469 | 122.38999938964844 | 0.008736483496223357 | 46 |
| SMALL_VALUE | US Small-Cap Value | 222.91000366210938 | 224.80999755859375 | 0.008523591876856251 | 47 |
| NASDAQ100 | Nasdaq 100 | 708.969970703125 | 713.4400024414062 | 0.006304966251036159 | 48 |
| AGRICULTURE | Agriculture Commodities | 28.149999618530273 | 28.31999969482422 | 0.006039079168656203 | 49 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.55999755859375 | 91.5999984741211 | 0.00043688200736080596 | 50 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 51 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.6500015258789 | 79.61000061035156 | -0.0005022085971253532 | 52 |
| REAL_ESTATE | Real Estate Sector | 45.20000076293945 | 45.08000183105469 | -0.0026548435809575777 | 53 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.41000366210938 | 93.12000274658203 | -0.003104602335488149 | 54 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.83000183105469 | 47.650001525878906 | -0.003763334691300635 | 55 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.73999786376953 | 97.3499984741211 | -0.003990171865892789 | 56 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.30999755859375 | 92.81999969482422 | -0.005251290071697223 | 57 |
| LOW_VOL | US Low Volatility Equities | 75.7300033569336 | 75.30999755859375 | -0.005546095070935841 | 58 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.37999725341797 | 94.72000122070312 | -0.006919648267144307 | 59 |
| TIPS | Treasury Inflation-Protected Securities | 107.87999725341797 | 107.12999725341797 | -0.006952169253751417 | 60 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.16999816894531 | 105.33999633789062 | -0.00781766831844466 | 61 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.8499984741211 | 105.91999816894531 | -0.00870379334072735 | 62 |
| REGIONAL_BANKS | Regional Banks | 75.9800033569336 | 74.86000061035156 | -0.014740756739909044 | 63 |
| BRAZIL | Brazil Equities | 35.619998931884766 | 35.060001373291016 | -0.015721436703707403 | 64 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.66000366210938 | 82.05000305175781 | -0.01924456777284067 | 65 |
| US_DOLLAR | US Dollar | 28.479999542236328 | 27.899999618530273 | -0.020365166187798045 | 66 |
| MOMENTUM | US Momentum Equities | 314.4800109863281 | 305.1700134277344 | -0.0296044175570781 | 67 |
| SEMICONDUCTORS | Semiconductors | 584.0800170898438 | 560.4199829101562 | -0.0405082069021514 | 68 |
| UTILITIES | Utilities Sector | 44.91999816894531 | 42.77000045776367 | -0.047862818317477296 | 69 |
| SOLAR | Solar Energy | 53.7400016784668 | 49.31999969482422 | -0.08224789440997804 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SP500 | 30.0 | 0.023306704339868034 | 0.00699201130196041 | Benchmark core; resilient breadth and July 21 strength support baseline equity exposure. |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 30.0 | -0.0405082069021514 | -0.01215246207064542 | Strongest prior active trend (+56% over 105s) with a deep recent pullback (-11.7% active); top quality evidence score and July 21 SOX +5.4% suggests trend resumption into AI earnings. |
| anthropic-claude-fable-5 | ENERGY | 20.0 | 0.08786323742988777 | 0.017572647485977557 | Brent at $91 up 2% on July 21, oil +12% over 21 sessions; energy sector +9.4% active with low SPY beta provides diversification and inflation-linked upside. |
| anthropic-claude-fable-5 | HEALTHCARE | 20.0 | 0.08967235642550708 | 0.01793447128510142 | Best 21-session active return among sectors (+7.5%) after a deep prior lag (-12.2%), low beta defensive that hedges FOMC/CPI risk while still beating SPY base case. |
| anthropic-claude-opus-4-8 | SP500 | 40.0 | 0.023306704339868034 | 0.009322681735947214 | Core broad exposure; benchmark anchor amid mixed macro and pre-FOMC uncertainty. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 30.0 | 0.08967235642550708 | 0.026901706927652123 | Strong relative strength (+7.53% active 21s), low drawdown, defensive tilt into event-heavy window. |
| anthropic-claude-opus-4-8 | DIVIDEND | 30.0 | 0.06977455627120199 | 0.020932366881360596 | Positive recent momentum (+3.63% active 21s), low beta, defensive quality tilt. |
| google-gemini-3-1-pro | OIL | 25.0 | 0.04493591782588857 | 0.011233979456472143 | Strong recent momentum in crude prices and positive active return trends support further upside. |
| google-gemini-3-1-pro | ENERGY | 25.0 | 0.08786323742988777 | 0.021965809357471944 | Energy sector equities are well-positioned to benefit from rising crude prices and strong recent active returns. |
| google-gemini-3-1-pro | HEALTHCARE | 50.0 | 0.08967235642550708 | 0.04483617821275354 | Healthcare offers defensive characteristics with strong recent active performance, providing balance to the portfolio. |
| openai-gpt-5-5 | SEMICONDUCTORS | 25.0 | -0.0405082069021514 | -0.01012705172553785 | High-quality evidence score and very strong prior active trend with a large recent pullback create the best one-month rebound setup among growth exposures, with sector strength at the July 21 close and near-term mega-cap and chip-related earnings as catalysts. |
| openai-gpt-5-5 | ENERGY | 20.0 | 0.08786323742988777 | 0.017572647485977557 | Energy has positive prior and recent active returns, crude was strong at the entry close, and the sector offers differentiated exposure versus SPY if oil strength persists. |
| openai-gpt-5-5 | BIOTECH | 20.0 | 0.07268605648892601 | 0.014537211297785202 | Biotech shows strong 21-day active performance with positive prior active return and a pullback-resistant healthcare exposure that could continue if risk appetite broadens beyond mega-cap growth. |
| openai-gpt-5-5 | DIVIDEND | 20.0 | 0.06977455627120199 | 0.0139549112542404 | Dividend equities combine positive recent and prior active performance with lower volatility and shallow drawdown, giving a steadier route to beat SPY if market breadth and value/dividend factors persist. |
| openai-gpt-5-5 | JAPAN | 15.0 | 0.026310141229359152 | 0.003946521184403873 | Japan has a high quality evidence score, positive prior active trend, and a recent pullback that could mean-revert around the Bank of Japan meeting and global equity risk appetite. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 50.0 | -0.0405082069021514 | -0.0202541034510757 | The highest quality-evidence score among the finalists combines a very strong prior relative trend with a deep pullback, while the July 21 semiconductor surge and upcoming technology earnings provide near-term confirmation opportunities. |
| openai-gpt-5-6-sol | BROAD_COMMODITIES | 30.0 | 0.05665722502056747 | 0.01699716750617024 | Positive prior and recent relative performance has macro support from elevated energy prices and inflation uncertainty, while low correlation to SPY diversifies the semiconductor allocation. |
| openai-gpt-5-6-sol | DIVIDEND | 20.0 | 0.06977455627120199 | 0.0139549112542404 | Dividend equities offer profitable, lower-volatility equity exposure with positive prior and recent relative trends, potentially benefiting if weakening employment encourages a defensive rotation. |
| xai-grok-4-3 | SP500 | 40.0 | 0.023306704339868034 | 0.009322681735947214 | Broad diversified US equity exposure as core holding. |
| xai-grok-4-3 | ENERGY | 20.0 | 0.08786323742988777 | 0.017572647485977557 | Strong recent oil price momentum and sector outperformance. |
| xai-grok-4-3 | SMALL_VALUE | 20.0 | 0.008523591876856251 | 0.0017047183753712504 | Positive recent relative performance in value segment. |
| xai-grok-4-3 | HEALTHCARE | 15.0 | 0.08967235642550708 | 0.013450853463826061 | Strong active returns and defensive characteristics. |
| xai-grok-4-3 | FINANCIALS | 5.0 | 0.02441630577405518 | 0.001220815288702759 | Modest positive active return in recent window. |
| xai-grok-4-5 | ENERGY | 25.0 | 0.08786323742988777 | 0.021965809357471944 | Strong recent active returns and oil price support outweigh near-term volatility for the one-month window. |
| xai-grok-4-5 | OIL | 25.0 | 0.04493591782588857 | 0.011233979456472143 | Direct crude exposure with elevated prior active trend and positive 5s/21s returns supports higher base case than SPY. |
| xai-grok-4-5 | BIOTECH | 25.0 | 0.07268605648892601 | 0.018171514122231502 | Positive 21s active return and biotech momentum provide edge over broad market base case. |
| xai-grok-4-5 | BROAD_COMMODITIES | 25.0 | 0.05665722502056747 | 0.014164306255141867 | Diversified commodity strength with solid 21s active return and energy/ag support exceeds SPY forecast. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | HEALTHCARE | 3 | 0.65 | 0.08967235642550708 | 0.07803596702669763 | 0.054729262686829594 | 0.17729783244532255 |  | True | True |
| xai-grok-4-5 | ENERGY | 4 | 0.58 | 0.08786323742988777 | 0.06553560919131746 | 0.04222890485144942 | 0.18979819028070272 |  | True | True |
| anthropic-claude-opus-4-8 | SP500 | 3 | 0.55 | 0.023306704339868034 | 0.057156755544959935 | 0.0338500512050919 | 0.19817704392706023 |  | True | True |
| xai-grok-4-3 | SP500 | 5 | 0.55 | 0.023306704339868034 | 0.04327171634982484 | 0.019965012009956803 | 0.21206208312219532 |  | True | True |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.56 | -0.0405082069021514 | 0.03988423949686919 | 0.016577535157001153 | 0.21544955997515097 |  | True | True |
| anthropic-claude-fable-5 | SP500 | 4 | 0.6 | 0.023306704339868034 | 0.030346668002393967 | 0.007039963662525933 | 0.2249871314696262 |  | True | True |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 3 | 0.56 | -0.0405082069021514 | 0.010697975309334942 | -0.012608729030533092 | 0.24463582416268523 |  | False | True |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SP500 | 0.007039963662525933 | 0.45914000000000005 | 0.015332934753072989 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | fc2dc9655a8f43dc8da3387505b3828e0c0ae6e49f64710c1f4a21f997b4ccf6 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | ef3cf65c548d3cc3229f74393dc61292363e4cb8a6e609b4a75e4c2062b6698e |
| manifest.yaml | c5b1707bf8d52c572c481c74e8b7c9df98f97fd5d6f543b82bb5d4e9756c2899 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | abac7369e7e0f6d1822ce4a9c44531e491d0e2429cc5e2b5215e057f1c344ca6 |
| market_data/universe_decision_context.md | 78ec7cf3bd1eabeb83700d44504b90d24f67945bb4f9426dba182693b46d200b |
| market_data/universe_decision_context.json | 94c99a055fa83d9042270988e91c9494d0ebd006afe07d9387f248dc9a01946e |
| market_data/decision_context_source_history.json | 46fb8b21c5a2f4706288f794e42d2c473ce783fbc58c8c3e088f8679f4394061 |
| market_data/universe_quality_evidence.md | aa0dfa1805837b0334e15bacde622a62c320f9e602f20fdf2370f3cccf75f45b |
| market_data/universe_quality_evidence.json | d0dc68ec6fbbd862f7b497210851ed980c9345a5796235e595c5159eb3ff943e |

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
