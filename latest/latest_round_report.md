# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-08-26-1W
- Decision deadline: 2026-08-27T13:25:00Z
- Horizon: one week
- Official run ID: official-v3-20260827-weekly
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 1 | 0.5 | Mixed signals with equity weakness offset by crypto volume strength and commodity pullbacks; one-week window favors selective reversal and continuation candidates over broad benchmark. | crypto volatility exceeding 50%; NVIDIA guidance execution risk; FOMC September meeting uncertainty; oil inventory and demand weakness |
| xai-grok-4-6 | xai | portfolio | SP500 | 1 | 0.5 | SPY is near a 52-week high with low 5-session dispersion (~3%) after a quiet close; Jackson Hole and mixed inflation/labor prints dominate a one-week window more than single-theme continuation. Crypto volume spikes and metals prior strength coexist with oil/defense shocks, so edges versus SPY are modest. | Jackson Hole remarks on August 28 can reprice rates and growth beta across the entire slate.; Oil’s drop from ~$94 to ~$87 can keep dragging ENERGY/OIL even if equities stabilize.; Crypto and Korea vol (38–67%) can dominate weekly excess if risk appetite fades.; NVIDIA’s after-close print can spill into robotics/tech high-beta names without a one-week mean reversion. |
| xai-grok-4-5 | xai | portfolio | ENERGY | 3 | 0.5633 | SPY near flat with low single-week vol; mixed cross-asset signals from oil weakness, crypto volume spikes, quality pullbacks in energy/tech themes, and modest international strength amid sticky PCE and soft labor data. One-week edge limited outside selective mean-reversion. | Jackson Hole Fed speech and sticky 3.7% PCE could reprice rates and growth equities; oil/energy inventory and demand data may extend commodity weakness; crypto volume spikes can reverse sharply on risk-off or liquidity shifts; soft labor/housing prints raise recession-sensitivity for cyclicals |
| anthropic-claude-opus-5 | anthropic | portfolio | AUTONOMOUS_ROBOTICS | 3 | 0.5633 | Flat tape into Jackson Hole with sticky 3.7% headline PCE, soft payrolls and a hawkish-leaning FOMC split. NVIDIA's large beat and $108B guide is a concrete in-window catalyst for AI/semis-linked exposure. Dispersion (3.07% 5s active) is normal; breadth improved short-term (RSP > SPY). Crypto's huge 5-day active surge on 2+ volume z is a stretched move, not a reversal setup. | Jackson Hole remarks from Chair Warsh could trigger a hawkish rate shock hitting high-beta tech; NVIDIA sell-the-news reaction could reverse AI-linked names rather than lift them; Crude weakness may extend and drag energy equities despite favorable product inventories; Sticky 3.7% PCE with a split FOMC raises September hike risk premium |
| anthropic-claude-fable-5 | anthropic | portfolio | SEMICONDUCTORS | 3 | 0.58 | SPY flat into Jackson Hole with a strong NVIDIA beat and raise after the close ($108B guide vs $96.2B reported), which should support AI/tech pullback names into the window. Gold/silver retain strong medium trends; oil weakness looks supply-driven. Dispersion at 3.07% is normal; edge favors quality pullbacks in AI-linked exposures. | NVIDIA guidance already priced or sell-the-news reaction in semis/AI names; Hawkish Warsh remarks at Jackson Hole on Aug 28 pressuring high-beta and precious metals; Dollar strength (UUP +0.50% 5s) capping silver; High-vol picks (SMH 42.8% vol, ARKQ 36.7%) can swing sharply against SPY in one week |
| openai-gpt-5-6-sol | openai | portfolio | SEMICONDUCTORS | 3 | 0.5667 | High cross-sectional dispersion and conflicting macro signals favor selective reversals rather than broad beta. NVIDIA's strong report supports a near-term technology rebound, while elevated inflation, 4.65% Treasury yields, weak payrolls, and softer petroleum demand limit risk appetite. | NVIDIA's strong results may already be priced in, producing a sell-the-news technology reversal; Jackson Hole remarks could push yields higher and pressure high-beta growth exposures; Elevated inflation and weak labor data could trigger a broad risk-off move; The selected technology exposures are correlated and may decline together |
| google-gemini-3-1-pro | google | portfolio | AUTONOMOUS_ROBOTICS | 3 | 0.6033 | The market is relatively flat with mixed signals. Inflation data is steady, and GDP growth is moderate. The upcoming Jackson Hole symposium and payroll data could introduce volatility. | Volatility from upcoming economic data releases, particularly the Jackson Hole symposium and payroll data.; Potential for continued downward momentum in the selected sectors if the recent pullbacks are indicative of broader fundamental deterioration rather than temporary overreactions. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 130.00999450683594 | 142.09 | 0.09291597572161181 | 1 |
| BRAZIL | Brazil Equities | 35.7599983215332 | 38.13 | 0.06627521783298529 | 2 |
| ENERGY | Energy Sector | 62.290000915527344 | 64.62 | 0.0374056678475958 | 3 |
| BROAD_COMMODITIES | Broad Commodities | 18.420000076293945 | 19.09 | 0.036373502764982524 | 4 |
| YEN | Japanese Yen | 57.5 | 58.87 | 0.023826086956521664 | 5 |
| BITCOIN_ETF | Bitcoin ETF | 45.290000915527344 | 46.35 | 0.023404704416979616 | 6 |
| JAPAN | Japan Equities | 95.83999633789062 | 97.9 | 0.02149419596017821 | 7 |
| COMMUNICATIONS | Communication Services Sector | 111.41000366210938 | 113.38 | 0.01768240080006933 | 8 |
| TAIWAN | Taiwan Equities | 108.62999725341797 | 110.13 | 0.01380836587045775 | 9 |
| FINANCIALS | Financials Sector | 57.880001068115234 | 58.56 | 0.011748426387976796 | 10 |
| HEALTHCARE | Healthcare Sector | 171.5800018310547 | 173.26 | 0.009791340197090603 | 11 |
| AGRICULTURE | Agriculture Commodities | 28.81999969482422 | 29.09 | 0.009368504789549759 | 12 |
| AUSTRALIA | Australia Equities | 30.110000610351562 | 30.37 | 0.008634984535970114 | 13 |
| ETHEREUM_ETF | Ethereum ETF | 18.8700008392334 | 19.02 | 0.007949080768175243 | 14 |
| INDIA | India Equities | 49.529998779296875 | 49.92 | 0.007874040587825482 | 15 |
| DIVIDEND | US Dividend Equities | 34.83000183105469 | 35.08 | 0.00717766740748238 | 16 |
| REGIONAL_BANKS | Regional Banks | 74.3499984741211 | 74.87 | 0.00699396821184739 | 17 |
| LARGE_VALUE | US Large-Cap Value | 257.5799865722656 | 259.38 | 0.006988172690308714 | 18 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 115.87999725341797 | 116.46 | 0.005005201590690511 | 19 |
| SOUTH_AFRICA | South Africa Equities | 71.55999755859375 | 71.82 | 0.003633348941821213 | 20 |
| CANADA | Canada Equities | 62.2599983215332 | 62.47 | 0.0033729791861263347 | 21 |
| SP500 | S&P 500 | 771.0999755859375 | 773.17 | 0.0026845084679059106 | 22 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.08000183105469 | 85.26 | 0.0021156342862185262 | 23 |
| LOW_VOL | US Low Volatility Equities | 75.12000274658203 | 75.24 | 0.0015974074684579342 | 24 |
| UNITED_KINGDOM | United Kingdom Equities | 48.630001068115234 | 48.68 | 0.00102814992363931 | 25 |
| TOTAL_US_MARKET | Total US Stock Market | 380.6300048828125 | 380.93 | 0.0007881541479628495 | 26 |
| DEVELOPED_EX_US | Developed Markets ex-US | 73.41999816894531 | 73.44 | 0.0002724302853924776 | 27 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 28 |
| EMERGING_MARKETS | Emerging Markets | 61.0099983215332 | 60.99 | -0.0003277876099554433 | 29 |
| US_DOLLAR | US Dollar | 28.020000457763672 | 28.01 | -0.0003569042683901902 | 30 |
| COPPER | Copper | 39.97999954223633 | 39.91 | -0.0017508640079493265 | 31 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.62999725341797 | 91.42 | -0.0022917959152305434 | 32 |
| EURO | Euro | 107.54000091552734 | 107.28 | -0.0024177135327678734 | 33 |
| MEXICO | Mexico Equities | 77.16000366210938 | 76.97 | -0.002462463103830581 | 34 |
| UTILITIES | Utilities Sector | 43.18000030517578 | 43.03 | -0.0034738375200474847 | 35 |
| LARGE_GROWTH | US Large-Cap Growth | 123.88999938964844 | 123.43 | -0.0037129662758467186 | 36 |
| BROAD_AI_TECH | Broad AI Technology | 64.54000091552734 | 64.3 | -0.003718638241754446 | 37 |
| TIPS | Treasury Inflation-Protected Securities | 107.44000244140625 | 107.0 | -0.004095331640058486 | 38 |
| SMALL_VALUE | US Small-Cap Value | 224.74000549316406 | 223.72 | -0.004538602243627232 | 39 |
| NASDAQ100 | Nasdaq 100 | 721.1099853515625 | 717.67 | -0.004770403158244174 | 40 |
| EUROPE | Europe Equities | 92.27999877929688 | 91.74 | -0.005851742375814095 | 41 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.70000076293945 | 47.4 | -0.006289324070043678 | 42 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 221.4499969482422 | 220.05 | -0.0063219551480481195 | 43 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.12999725341797 | 94.45 | -0.007148084442875735 | 44 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.87000274658203 | 79.21 | -0.008263462174605718 | 45 |
| SOUTH_KOREA | South Korea Equities | 182.13999938964844 | 180.56 | -0.008674642554864498 | 46 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.83000183105469 | 96.95 | -0.008995214296064091 | 47 |
| REAL_ESTATE | Real Estate Sector | 44.65999984741211 | 44.25 | -0.00918047131242583 | 48 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.5199966430664 | 92.66 | -0.009195858361166542 | 49 |
| CHINA | China Equities | 54.900001525878906 | 54.37 | -0.00965394373676065 | 50 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.2300033569336 | 92.28 | -0.010189888691695903 | 51 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 124.16000366210938 | 122.81 | -0.010873096184688347 | 52 |
| MATERIALS | Materials Sector | 53.22999954223633 | 52.62 | -0.011459694673720877 | 53 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.7300033569336 | 105.5 | -0.011524438473220489 | 54 |
| MID_CAP | US Mid-Cap Stocks | 76.6500015258789 | 75.75 | -0.011741702647912411 | 55 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.12999725341797 | 82.07 | -0.012751080096714329 | 56 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.38999938964844 | 104.0 | -0.013189101410934878 | 57 |
| TECHNOLOGY | Technology Sector | 188.61000061035156 | 185.97 | -0.013997140140015851 | 58 |
| SMALL_CAP | US Small-Cap Stocks | 299.80999755859375 | 295.19 | -0.015409751496665236 | 59 |
| MOMENTUM | US Momentum Equities | 304.2300109863281 | 299.42 | -0.015810442141239833 | 60 |
| BIOTECH | Biotechnology | 168.22999572753906 | 164.38 | -0.022885310737179254 | 61 |
| INDUSTRIALS | Industrials Sector | 178.8000030517578 | 174.56 | -0.02371366319569046 | 62 |
| GOLD | Gold | 86.62000274658203 | 84.1 | -0.029092619102710326 | 63 |
| SOFTWARE | Software | 110.31999969482422 | 106.95 | -0.03054749550531699 | 64 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 234.25999450683594 | 225.98 | -0.03534532016133185 | 65 |
| SILVER | Silver | 62.77000045776367 | 60.55 | -0.03536722067187903 | 66 |
| SEMICONDUCTORS | Semiconductors | 573.0 | 552.6 | -0.03560209424083771 | 67 |
| METALS_MINING | Metals and Mining | 123.0 | 118.38 | -0.03756097560975613 | 68 |
| SOLAR | Solar Energy | 49.7400016784668 | 47.72 | -0.040611210500647976 | 69 |
| CYBERSECURITY | Cybersecurity | 100.79000091552734 | 95.32 | -0.054271265659693646 | 70 |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | portfolio | SP500 | 1 | 0.5 | 0.0026845084679059106 | 0.0026845084679059106 | 0.0 | 0.0902314672537059 |  | False | True |
| xai-grok-4-6 | portfolio | SP500 | 1 | 0.5 | 0.0026845084679059106 | 0.0026845084679059106 | 0.0 | 0.0902314672537059 |  | False | True |
| xai-grok-4-5 | portfolio | ENERGY | 3 | 0.5633 | 0.0374056678475958 | 0.0018201961332392868 | -0.0008643123346666237 | 0.09109577958837252 |  | False | True |
| anthropic-claude-opus-5 | portfolio | AUTONOMOUS_ROBOTICS | 3 | 0.5633 | -0.010873096184688347 | -0.011578826291254953 | -0.014263334759160863 | 0.10449480201286676 |  | False | False |
| anthropic-claude-fable-5 | portfolio | SEMICONDUCTORS | 3 | 0.58 | -0.03560209424083771 | -0.026876482850497825 | -0.029560991318403736 | 0.11979245857210963 |  | False | False |
| openai-gpt-5-6-sol | portfolio | SEMICONDUCTORS | 3 | 0.5667 | -0.03560209424083771 | -0.03254769634684221 | -0.03523220481474812 | 0.12546367206845402 |  | False | False |
| google-gemini-3-1-pro | portfolio | AUTONOMOUS_ROBOTICS | 3 | 0.6033 | -0.010873096184688347 | -0.034300887037775805 | -0.036985395505681716 | 0.12721686275938762 |  | False | False |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1W has no scored official run.
- Round CB-2026-08-27-1W has no scored official run.
- Round CB-2026-08-30-1W has no scored official run.
- Round CB-2026-09-01-1W has no scored official run.
- Round CB-2026-09-02-1W has no scored official run.
- Round CB-2026-09-03-1W has no scored official run.
