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
| SOUTH_KOREA | South Korea Equities | 182.03 | 205.83 | 0.13074767895401873 | 1 |
| SOFTWARE | Software | 94.01 | 101.66 | 0.08137432188065086 | 2 |
| TAIWAN | Taiwan Equities | 96.84 | 102.78 | 0.0613382899628252 | 3 |
| TECHNOLOGY | Technology Sector | 180.39 | 191.02 | 0.05892787848550385 | 4 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 225.37 | 235.44 | 0.04468207836003013 | 5 |
| MOMENTUM | US Momentum Equities | 303.6 | 315.81 | 0.04021739130434776 | 6 |
| SEMICONDUCTORS | Semiconductors | 576.32 | 598.93 | 0.03923167684619644 | 7 |
| BIOTECH | Biotechnology | 131.66 | 136.69 | 0.03820446604891381 | 8 |
| SOUTH_AFRICA | South Africa Equities | 67.31 | 69.41 | 0.031198930322388962 | 9 |
| NASDAQ100 | Nasdaq 100 | 717.54 | 738.31 | 0.028946121470579955 | 10 |
| LARGE_GROWTH | US Large-Cap Growth | 125.0 | 127.85 | 0.02279999999999993 | 11 |
| SMALL_CAP | US Small-Cap Stocks | 285.12 | 290.43 | 0.01862373737373746 | 12 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.46 | 71.77 | 0.018592108998013 | 13 |
| MATERIALS | Materials Sector | 50.29 | 51.15 | 0.017100815271425818 | 14 |
| AUSTRALIA | Australia Equities | 28.78 | 29.25 | 0.016330785267546943 | 15 |
| TOTAL_US_MARKET | Total US Stock Market | 366.79 | 372.54 | 0.015676545162081945 | 16 |
| EMERGING_MARKETS | Emerging Markets | 58.98 | 59.88 | 0.015259409969481386 | 17 |
| MID_CAP | US Mid-Cap Stocks | 73.5 | 74.6 | 0.014965986394557707 | 18 |
| JAPAN | Japan Equities | 91.61 | 92.96 | 0.014736382490994293 | 19 |
| SP500 | S&P 500 | 745.64 | 756.48 | 0.014537846682044941 | 20 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 119.18 | 120.87 | 0.014180231582480163 | 21 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.17 | 96.43 | 0.013239466218346152 | 22 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.68 | 85.76 | 0.012753897024090577 | 23 |
| SMALL_VALUE | US Small-Cap Value | 211.31 | 213.87 | 0.01211490227627654 | 24 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 206.58 | 208.83 | 0.01089166424629684 | 25 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.17 | 107.17 | 0.009418856550814647 | 26 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.37 | 109.36 | 0.009135369567223384 | 27 |
| MEXICO | Mexico Equities | 77.76 | 78.43 | 0.00861625514403297 | 28 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.88 | 94.65 | 0.008201959948870963 | 29 |
| GOLD | Gold | 84.81 | 85.49 | 0.008017922414809586 | 30 |
| INDUSTRIALS | Industrials Sector | 171.77 | 173.13 | 0.007917564184665382 | 31 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.08 | 94.79 | 0.007546768707483054 | 32 |
| TIPS | Treasury Inflation-Protected Securities | 110.38 | 111.21 | 0.007519478166334359 | 33 |
| LARGE_VALUE | US Large-Cap Value | 236.32 | 237.96 | 0.006939742721733255 | 34 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.44 | 99.06 | 0.006298252742787502 | 35 |
| EUROPE | Europe Equities | 88.46 | 89.01 | 0.006217499434773011 | 36 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.06 | 48.33 | 0.00561797752808979 | 37 |
| EURO | Euro | 107.1 | 107.7 | 0.0056022408963585235 | 38 |
| CANADA | Canada Equities | 58.51 | 58.81 | 0.005127328661767239 | 39 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.91 | 80.31 | 0.005005631335252225 | 40 |
| INDIA | India Equities | 48.39 | 48.56 | 0.0035131225459805737 | 41 |
| REGIONAL_BANKS | Regional Banks | 69.37 | 69.61 | 0.0034597088078418547 | 42 |
| COMMUNICATIONS | Communication Services Sector | 115.46 | 115.69 | 0.0019920318725099584 | 43 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.59 | 91.66 | 0.0007642755759360575 | 44 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 45 |
| SILVER | Silver | 68.36 | 68.33 | -0.0004388531304856391 | 46 |
| YEN | Japanese Yen | 57.7 | 57.62 | -0.001386481802426398 | 47 |
| COPPER | Copper | 38.92 | 38.86 | -0.0015416238437822027 | 48 |
| HEALTHCARE | Healthcare Sector | 149.89 | 149.47 | -0.002802054840216117 | 49 |
| UNITED_KINGDOM | United Kingdom Equities | 47.09 | 46.93 | -0.0033977489912933034 | 50 |
| US_DOLLAR | US Dollar | 27.77 | 27.66 | -0.00396110911055092 | 51 |
| FINANCIALS | Financials Sector | 51.94 | 51.58 | -0.00693107431651907 | 52 |
| CHINA | China Equities | 55.54 | 55.1 | -0.00792221822110184 | 53 |
| DIVIDEND | US Dividend Equities | 32.83 | 32.5 | -0.010051781906792567 | 54 |
| AGRICULTURE | Agriculture Commodities | 27.56 | 27.25 | -0.011248185776487563 | 55 |
| BRAZIL | Brazil Equities | 36.37 | 35.91 | -0.012647786637338454 | 56 |
| REAL_ESTATE | Real Estate Sector | 44.56 | 43.99 | -0.012791741472172324 | 57 |
| UTILITIES | Utilities Sector | 45.35 | 44.42 | -0.020507166482910733 | 58 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.8 | 82.91 | -0.022287735849056634 | 59 |
| ETHEREUM_ETF | Ethereum ETF | 15.57 | 15.2 | -0.023763648041104757 | 60 |
| LOW_VOL | US Low Volatility Equities | 74.09 | 72.21 | -0.02537454447293841 | 61 |
| BITCOIN_ETF | Bitcoin ETF | 42.96 | 41.63 | -0.030959031657355585 | 62 |
| BROAD_COMMODITIES | Broad Commodities | 18.2 | 17.62 | -0.031868131868131755 | 63 |
| ENERGY | Energy Sector | 59.49 | 56.29 | -0.05379055303412339 | 64 |
| OIL | Crude Oil | 140.92 | 129.09 | -0.08394833948339475 | 65 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | 0.03923167684619644 | 0.011769503053858932 | Strong momentum (+3.59% 7d, +13.80% 30d), Nvidia data center revenue +85% YoY, Taiwan +6.09% confirms AI supply chain strength heading into PCE release. |
| anthropic-claude-opus-4-7 | TAIWAN | 20.0 | 0.0613382899628252 | 0.01226765799256504 | Best 7d performer (+6.09%) with Q1 GDP +13.7% and exports +35.3% YoY; semis supply chain tailwind likely to persist through short trading week. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 20.0 | 0.04468207836003013 | 0.008936415672006027 | Strong 7d momentum (+3.73%); $1.5T FY27 defense budget proposal and Iran/Hormuz geopolitical risk provide near-term tailwind. |
| anthropic-claude-opus-4-7 | UTILITIES | 15.0 | -0.020507166482910733 | -0.00307607497243661 | Defensive carry with +3.37% 7d momentum; NextEra/Dominion $67B M&A catalyst and weak consumer sentiment (44.8) favor defensives during holiday-shortened week with PCE risk. |
| anthropic-claude-opus-4-7 | GOLD | 15.0 | 0.008017922414809586 | 0.0012026883622214379 | Hedge against PCE upside surprise (Core PCE consensus 3.2% with CPI accelerating to 3.8%) and geopolitical Hormuz risk; recent -0.82% pullback offers entry. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | 0.03923167684619644 | 0.015692670738478576 | Nvidia's massive Q1 revenue beat (+85% YoY) provides a strong near-term catalyst for the semiconductor sector. |
| google-gemini-3-1-pro | TAIWAN | 30.0 | 0.0613382899628252 | 0.018401486988847558 | Taiwan's 13.7% Q1 GDP expansion and strong semiconductor supply chain links position it well to benefit from AI hardware demand. |
| google-gemini-3-1-pro | UTILITIES | 30.0 | -0.020507166482910733 | -0.00615214994487322 | The announced $67 billion NextEra and Dominion merger provides a significant near-term catalyst for the utilities sector. |
| openai-gpt-5-5 | TAIWAN | 40.0 | 0.0613382899628252 | 0.02453531598513008 | Strongest 7-day performance in the universe, high 30-day momentum, and reported Q1 growth/export strength tied to the semiconductor cycle. |
| openai-gpt-5-5 | SEMICONDUCTORS | 35.0 | 0.03923167684619644 | 0.013731086896168752 | Very strong 7-day, 30-day, 6-month, and 1-year momentum, with Nvidia's reported data-center revenue growth supporting near-term AI-chip sentiment. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 15.0 | 0.04468207836003013 | 0.006702311754004519 | Top-tier recent weekly momentum and a favorable policy backdrop from the proposed larger FY2027 defense budget. |
| openai-gpt-5-5 | TECHNOLOGY | 10.0 | 0.05892787848550385 | 0.005892787848550385 | Captures broader large-cap technology momentum while diversifying beyond pure semiconductor and Taiwan exposure. |
| xai-grok-4-3 | TAIWAN | 30.0 | 0.0613382899628252 | 0.018401486988847558 | Strongest 7d return at 6.09% with Q1 GDP expansion of 13.7% and export growth supporting near-term momentum into holiday-shortened week. |
| xai-grok-4-3 | AEROSPACE_DEFENSE | 25.0 | 0.04468207836003013 | 0.011170519590007533 | 3.73% 7d return and proposed $1.5T defense budget provide sector tailwinds likely to persist over five trading days. |
| xai-grok-4-3 | SEMICONDUCTORS | 20.0 | 0.03923167684619644 | 0.007846335369239288 | 3.59% 7d return and Nvidia revenue strength indicate continued AI-related flows before exit close. |
| xai-grok-4-3 | REGIONAL_BANKS | 15.0 | 0.0034597088078418547 | 0.0005189563211762782 | 3.58% 7d return and 8.45% YTD performance suggest domestic rate and credit sensitivity benefits in short window. |
| xai-grok-4-3 | DIVIDEND | 10.0 | -0.010051781906792567 | -0.0010051781906792567 | 3.50% 7d return offers defensive equity exposure with dividend tilt amid mixed consumer sentiment data. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| openai-gpt-5-5 | TAIWAN | 4 | 0.58 | 0.0613382899628252 | 0.05086150248385374 | 0.036323655801808796 | 0.079886176470165 |  | True | True |
| xai-grok-4-3 | TAIWAN | 5 | 0.65 | 0.0613382899628252 | 0.036932120078591396 | 0.022394273396546455 | 0.09381555887542734 |  | True | True |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | 0.03923167684619644 | 0.03110019010821483 | 0.016562343426169888 | 0.0996474888458039 |  | True | True |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.7 | 0.03923167684619644 | 0.02794200778245291 | 0.013404161100407968 | 0.10280567117156582 |  | True | True |

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
