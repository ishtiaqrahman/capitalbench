# CapitalBench Report: CB-2026-05-24-1W / official-20260524-1W

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260524-1W
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench May 24 2026 One-Week Portfolio Round
- Description: One-week CapitalBench portfolio evaluation round using the frozen May 24, 2026 briefing and expanded v2.0 universe.
- Decision date: 2026-05-24
- Decision deadline: 2026-05-25T01:00:00Z
- Horizon: one week
- Entry date: 2026-05-22
- Exit date: 2026-05-29
- Entry rule: Use adjusted close from the last trading close before the decision deadline; CASH return is 0 unless explicitly priced.
- Exit rule: Use adjusted close on the exit_date for each selected option; CASH return is 0 unless explicitly priced.
- Options: 65

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | openai | portfolio | TAIWAN | 4 | 0.58 | Allocate mainly to Taiwan and semiconductors to capture persistent AI and chip-supply-chain momentum, with smaller defense and technology positions for additional near-term strength. The main macro risk is the May 28 PCE/GDP release, but current low volatility, tight credit spreads, and strong momentum argue for equity beta over duration or cash. | A hotter-than-expected May 28 PCE report could lift yields and trigger a sharp rotation out of high-valuation technology and semiconductor equities.; Taiwan and semiconductor holdings are highly concentrated in the same AI hardware supply-chain theme, so any negative chip-specific news could hurt most of the portfolio simultaneously.; Cross-strait geopolitical headlines or trade restrictions could disproportionately pressure Taiwan equities before the Friday exit.; A short holiday week could amplify profit-taking in recent winners after very strong 7-day and 30-day moves. |
| xai-grok-4-3 | xai | portfolio | TAIWAN | 5 | 0.65 | Selected assets with highest 7d returns and supportive macro facts likely to influence prices before May 29 close; avoids post-window events and underperformers. | May 28 PCE release could trigger volatility if core reading deviates from 3.2% expectation; Taiwan allocation exposed to any sudden cross-strait geopolitical headlines; Holiday-shortened trading may amplify liquidity-driven reversals in small/mid sectors |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Lean into the strongest near-term momentum (semis, Taiwan, defense) while hedging the May 28 Core PCE release and geopolitical tail risk with utilities and gold. Equity-heavy but with defensive ballast given Shiller CAPE at 41.6 and hot CPI print. | Hot Core PCE print on May 28 could spike yields and hit growth/semis disproportionately; Semiconductor profit-taking after extended 70% 6-month run could reverse the momentum trade; Taiwan geopolitical headline risk (cross-strait tensions) could trigger sudden EWT drawdown; Utility M&A regulatory pushback could pressure XLU after recent rally; Gold weakness continuing on JPM forecast cut and stronger dollar could drag the hedge sleeve |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.7 | Overweight semiconductors and Taiwan to capture AI momentum following Nvidia's earnings, balanced with utilities to capture M&A catalysts. | Profit-taking in semiconductor stocks following the recent massive run-up.; Geopolitical tensions or supply chain disruptions affecting Taiwan.; Regulatory pushback on the NextEra-Dominion merger dampening utility sector sentiment.; A broader market sell-off driven by persistent inflation and higher-for-longer interest rates. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOUTH_KOREA | South Korea Equities | 182.02999877929688 | 205.8300018310547 | 0.13074769659595642 | 1 |
| SOFTWARE | Software | 94.01000213623047 | 101.66000366210938 | 0.08137433626257384 | 2 |
| TAIWAN | Taiwan Equities | 96.83999633789062 | 102.77999877929688 | 0.061338317493121464 | 3 |
| TECHNOLOGY | Technology Sector | 180.38999938964844 | 191.02000427246094 | 0.05892790575297546 | 4 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 225.3699951171875 | 235.44000244140625 | 0.04468211182674331 | 5 |
| MOMENTUM | US Momentum Equities | 303.6000061035156 | 315.80999755859375 | 0.04021736235049689 | 6 |
| SEMICONDUCTORS | Semiconductors | 576.3200073242188 | 598.9299926757812 | 0.03923165093042291 | 7 |
| BIOTECH | Biotechnology | 131.66000366210938 | 136.69000244140625 | 0.03820445571462838 | 8 |
| SOUTH_AFRICA | South Africa Equities | 67.30999755859375 | 69.41000366210938 | 0.031199022131705778 | 9 |
| NASDAQ100 | Nasdaq 100 | 717.5399780273438 | 738.3099975585938 | 0.02894614957671182 | 10 |
| LARGE_GROWTH | US Large-Cap Growth | 125.0 | 127.8499984741211 | 0.022799987792968768 | 11 |
| SMALL_CAP | US Small-Cap Stocks | 285.1199951171875 | 290.42999267578125 | 0.01862372912994492 | 12 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.45999908447266 | 71.7699966430664 | 0.018592074590055407 | 13 |
| MATERIALS | Materials Sector | 50.290000915527344 | 51.150001525878906 | 0.017100827096744542 | 14 |
| AUSTRALIA | Australia Equities | 28.780000686645508 | 29.25 | 0.01633076101949449 | 15 |
| TOTAL_US_MARKET | Total US Stock Market | 366.7900085449219 | 372.5400085449219 | 0.015676544796873193 | 16 |
| EMERGING_MARKETS | Emerging Markets | 58.97999954223633 | 59.880001068115234 | 0.015259435959039003 | 17 |
| MID_CAP | US Mid-Cap Stocks | 73.5 | 74.5999984741211 | 0.014965965634300638 | 18 |
| JAPAN | Japan Equities | 91.61000061035156 | 92.95999908447266 | 0.014736365736565116 | 19 |
| SP500 | S&P 500 | 745.6400146484375 | 756.47998046875 | 0.014537800557046898 | 20 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 119.18000030517578 | 120.87000274658203 | 0.0141802520312031 | 21 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.76831817626953 | 96.02300262451172 | 0.013239492610900516 | 22 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.34822845458984 | 85.42400360107422 | 0.01275397440105741 | 23 |
| SMALL_VALUE | US Small-Cap Value | 211.30999755859375 | 213.8699951171875 | 0.012114890862576777 | 24 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 206.5800018310547 | 208.8300018310547 | 0.01089166414975673 | 25 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.89261627197266 | 106.88999938964844 | 0.009418816465107671 | 26 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 107.96074676513672 | 108.94700622558594 | 0.009135352338704994 | 27 |
| MEXICO | Mexico Equities | 77.76000213623047 | 78.43000030517578 | 0.008616231359813042 | 28 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.5655746459961 | 94.33300018310547 | 0.008202007415792911 | 29 |
| GOLD | Gold | 84.80999755859375 | 85.48999786376953 | 0.008017926243966578 | 30 |
| INDUSTRIALS | Industrials Sector | 171.77000427246094 | 173.1300048828125 | 0.007917567541037895 | 31 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.74949645996094 | 94.45700073242188 | 0.007546752773899934 | 32 |
| TIPS | Treasury Inflation-Protected Securities | 109.11153411865234 | 109.93199920654297 | 0.007519508313377887 | 33 |
| LARGE_VALUE | US Large-Cap Value | 236.32000732421875 | 237.9600067138672 | 0.0069397399239179425 | 34 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.11106872558594 | 98.72899627685547 | 0.006298245032860139 | 35 |
| EUROPE | Europe Equities | 88.45999908447266 | 89.01000213623047 | 0.00621753399785363 | 36 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.94663619995117 | 48.215999603271484 | 0.005617983338747523 | 37 |
| EURO | Euro | 107.03535461425781 | 107.63499450683594 | 0.005602260063874764 | 38 |
| CANADA | Canada Equities | 58.5099983215332 | 58.810001373291016 | 0.005127380966739814 | 39 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.50304412841797 | 79.9010009765625 | 0.00500555485022347 | 40 |
| INDIA | India Equities | 48.38999938964844 | 48.560001373291016 | 0.0035131635831131547 | 41 |
| REGIONAL_BANKS | Regional Banks | 69.37000274658203 | 69.61000061035156 | 0.0034596778761315505 | 42 |
| COMMUNICATIONS | Communication Services Sector | 115.45999908447266 | 115.69000244140625 | 0.001992060962735076 | 43 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.32120513916016 | 91.39100646972656 | 0.000764349643218587 | 44 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 45 |
| SILVER | Silver | 68.36000061035156 | 68.33000183105469 | -0.00043883526958798935 | 46 |
| YEN | Japanese Yen | 57.70000076293945 | 57.619998931884766 | -0.0013865135181432287 | 47 |
| COPPER | Copper | 38.91999816894531 | 38.86000061035156 | -0.0015415611874726176 | 48 |
| HEALTHCARE | Healthcare Sector | 149.88999938964844 | 149.47000122070312 | -0.002802042635636437 | 49 |
| UNITED_KINGDOM | United Kingdom Equities | 47.09000015258789 | 46.93000030517578 | -0.003397745739937452 | 50 |
| US_DOLLAR | US Dollar | 27.770000457763672 | 27.65999984741211 | -0.0039611310240655895 | 51 |
| FINANCIALS | Financials Sector | 51.939998626708984 | 51.58000183105469 | -0.006931012806557502 | 52 |
| CHINA | China Equities | 55.540000915527344 | 55.099998474121094 | -0.007922262048131068 | 53 |
| DIVIDEND | US Dividend Equities | 32.83000183105469 | 32.5 | -0.010051837119988583 | 54 |
| AGRICULTURE | Agriculture Commodities | 27.559999465942383 | 27.25 | -0.01124816661645689 | 55 |
| BRAZIL | Brazil Equities | 36.369998931884766 | 35.90999984741211 | -0.012647761836181548 | 56 |
| REAL_ESTATE | Real Estate Sector | 44.560001373291016 | 43.9900016784668 | -0.012791734229296359 | 57 |
| UTILITIES | Utilities Sector | 45.349998474121094 | 44.41999816894531 | -0.02050717390225454 | 58 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.80000305175781 | 82.91000366210938 | -0.02228772784943034 | 59 |
| ETHEREUM_ETF | Ethereum ETF | 15.569999694824219 | 15.199999809265137 | -0.023763641156786752 | 60 |
| LOW_VOL | US Low Volatility Equities | 74.08999633789062 | 72.20999908447266 | -0.025374508656258565 | 61 |
| BITCOIN_ETF | Bitcoin ETF | 42.959999084472656 | 41.630001068115234 | -0.030958986142952005 | 62 |
| BROAD_COMMODITIES | Broad Commodities | 18.200000762939453 | 17.6200008392334 | -0.031868126340252934 | 63 |
| ENERGY | Energy Sector | 59.4900016784668 | 56.290000915527344 | -0.053790564341129166 | 64 |
| OIL | Crude Oil | 140.9199981689453 | 129.08999633789062 | -0.08394835356775987 | 65 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | 0.03923165093042291 | 0.011769495279126874 | Strong momentum (+3.59% 7d, +13.80% 30d), Nvidia data center revenue +85% YoY, Taiwan +6.09% confirms AI supply chain strength heading into PCE release. |
| anthropic-claude-opus-4-7 | TAIWAN | 20.0 | 0.061338317493121464 | 0.012267663498624293 | Best 7d performer (+6.09%) with Q1 GDP +13.7% and exports +35.3% YoY; semis supply chain tailwind likely to persist through short trading week. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 20.0 | 0.04468211182674331 | 0.008936422365348662 | Strong 7d momentum (+3.73%); $1.5T FY27 defense budget proposal and Iran/Hormuz geopolitical risk provide near-term tailwind. |
| anthropic-claude-opus-4-7 | UTILITIES | 15.0 | -0.02050717390225454 | -0.0030760760853381806 | Defensive carry with +3.37% 7d momentum; NextEra/Dominion $67B M&A catalyst and weak consumer sentiment (44.8) favor defensives during holiday-shortened week with PCE risk. |
| anthropic-claude-opus-4-7 | GOLD | 15.0 | 0.008017926243966578 | 0.0012026889365949866 | Hedge against PCE upside surprise (Core PCE consensus 3.2% with CPI accelerating to 3.8%) and geopolitical Hormuz risk; recent -0.82% pullback offers entry. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | 0.03923165093042291 | 0.015692660372169164 | Nvidia's massive Q1 revenue beat (+85% YoY) provides a strong near-term catalyst for the semiconductor sector. |
| google-gemini-3-1-pro | TAIWAN | 30.0 | 0.061338317493121464 | 0.01840149524793644 | Taiwan's 13.7% Q1 GDP expansion and strong semiconductor supply chain links position it well to benefit from AI hardware demand. |
| google-gemini-3-1-pro | UTILITIES | 30.0 | -0.02050717390225454 | -0.006152152170676361 | The announced $67 billion NextEra and Dominion merger provides a significant near-term catalyst for the utilities sector. |
| openai-gpt-5-5 | TAIWAN | 40.0 | 0.061338317493121464 | 0.024535326997248585 | Strongest 7-day performance in the universe, high 30-day momentum, and reported Q1 growth/export strength tied to the semiconductor cycle. |
| openai-gpt-5-5 | SEMICONDUCTORS | 35.0 | 0.03923165093042291 | 0.013731077825648018 | Very strong 7-day, 30-day, 6-month, and 1-year momentum, with Nvidia's reported data-center revenue growth supporting near-term AI-chip sentiment. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 15.0 | 0.04468211182674331 | 0.006702316774011496 | Top-tier recent weekly momentum and a favorable policy backdrop from the proposed larger FY2027 defense budget. |
| openai-gpt-5-5 | TECHNOLOGY | 10.0 | 0.05892790575297546 | 0.005892790575297547 | Captures broader large-cap technology momentum while diversifying beyond pure semiconductor and Taiwan exposure. |
| xai-grok-4-3 | TAIWAN | 30.0 | 0.061338317493121464 | 0.01840149524793644 | Strongest 7d return at 6.09% with Q1 GDP expansion of 13.7% and export growth supporting near-term momentum into holiday-shortened week. |
| xai-grok-4-3 | AEROSPACE_DEFENSE | 25.0 | 0.04468211182674331 | 0.011170527956685827 | 3.73% 7d return and proposed $1.5T defense budget provide sector tailwinds likely to persist over five trading days. |
| xai-grok-4-3 | SEMICONDUCTORS | 20.0 | 0.03923165093042291 | 0.007846330186084582 | 3.59% 7d return and Nvidia revenue strength indicate continued AI-related flows before exit close. |
| xai-grok-4-3 | REGIONAL_BANKS | 15.0 | 0.0034596778761315505 | 0.0005189516814197325 | 3.58% 7d return and 8.45% YTD performance suggest domestic rate and credit sensitivity benefits in short window. |
| xai-grok-4-3 | DIVIDEND | 10.0 | -0.010051837119988583 | -0.0010051837119988583 | 3.50% 7d return offers defensive equity exposure with dividend tilt amid mixed consumer sentiment data. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | TAIWAN | 4 | 0.58 | 0.061338317493121464 | 0.05086151217220564 | 0.036323711615158745 | 0.07988618442375078 |  | True | True |
| xai-grok-4-3 | TAIWAN | 5 | 0.65 | 0.061338317493121464 | 0.036932121360127725 | 0.022394320803080826 | 0.0938155752358287 |  | True | True |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | 0.03923165093042291 | 0.03110019399435663 | 0.016562393437309732 | 0.0996475026015998 |  | True | True |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.7 | 0.03923165093042291 | 0.027942003449429244 | 0.013404202892382346 | 0.10280569314652718 |  | True | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 3b942e49549af897fa853fcdd9a5a85102f640bab95289f725dee250e84e65ca |
| options.yaml | 8e07e0a1d09976c253d8b385fffa546b2e406bbad7499c7fc9f3fe35f15afcb1 |
| prompt.md | 587de2c8abad41c62cc7bfa6f7affc98a9550099c9647b232e09f6982e3c8dbd |
| manifest.yaml | e61ab7aac689d4e8d76b5e06c224ae4558821e27410ac4c24f60cb99cca5c26b |
| market_data/universe_trailing_returns.csv | d245d622914ee6a513e8c78e6349288b6038cf91b84bb0547953a8d6f4a45634 |
| market_data/universe_trailing_returns.md | 26c17ed88d4c7c23ee5a9e6340f1dc8a8a2484e6580adb3f992328308cf5613d |
| market_data/universe_trailing_returns.json | 001eb44a6c57f131b78681f8bd0ff0a26d7b48900b110fffa6d86bf53123d7d5 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | 384117ddc373437b7f4372f3b841a801fa16043120f6345de026628e459b4456 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 810b580092b4c01dfcfd1d34bbeb37b438b4b54a8e415283484cacfcffb0397b | yes |
| Final briefing | research/final_briefing.md | model-facing | 3b942e49549af897fa853fcdd9a5a85102f640bab95289f725dee250e84e65ca | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
