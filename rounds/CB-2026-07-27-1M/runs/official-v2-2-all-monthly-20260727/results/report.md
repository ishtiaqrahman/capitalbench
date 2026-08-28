# CapitalBench Report: CB-2026-07-27-1M / official-v2-2-all-monthly-20260727

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v2-2-all-monthly-20260727
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-27-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-27
- Decision deadline: 2026-07-28T12:30:00Z
- Horizon: one month
- Entry date: 2026-07-27
- Exit date: 2026-08-27
- Entry rule: Use adjusted close prices on Monday, July 27, 2026 as the one-month entry snapshot, calculated after regular trading ends and supplied in prices/entry_prices.csv.
- Exit rule: Use adjusted close prices on Thursday, August 27, 2026 as the one-month exit snapshot, calculated after regular trading ends and supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | google | portfolio | GOLD | 3 | 0.65 | A balanced approach favoring healthcare, industrials, and gold for defensive growth and inflation protection. | Unexpected hawkishness from the Federal Reserve.; A sudden deterioration in macroeconomic data.; Geopolitical shocks affecting commodity prices. |
| openai-gpt-5-6-sol | openai | portfolio | EQUAL_WEIGHT_SP500 | 3 | 0.58 | Breadth and factor rotation support equal-weight U.S. equities, while healthcare and Japan diversify the catalyst set. The weighted one-month base forecast is 1.48%, implying 0.68 percentage point of expected alpha. | Mega-cap earnings trigger renewed cap-weighted technology leadership and reverse market broadening.; A hawkish FOMC outcome or upside inflation surprise raises yields and pressures equities broadly.; BOJ communication or an abrupt yen move harms Japanese exporters.; Recent healthcare strength mean-reverts as investors rotate back into higher-beta sectors. |
| anthropic-claude-opus-5 | anthropic | portfolio | EQUAL_WEIGHT_SP500 | 5 | 0.55 | Tilt toward broadening breadth and low-drawdown defensives/value rather than concentrated mega-cap tech, plus a small energy hedge, targeting modest alpha over SPY. | A hawkish July 29 FOMC hike surprise pressures all equity exposures; Mega-cap earnings (MSFT/META/AAPL/AMZN) and Nvidia Aug 26 re-ignite cap-weighted leadership, causing SPY to outrun equal-weight and defensives; Oil collapse on a US-Iran deal hurts the energy sleeve; Hot Aug 12 CPI lifts yields and hits dividend/defensive rate-sensitive holdings; Healthcare and financials give back recent relative strength via mean reversion |
| xai-grok-4-5 | xai | portfolio | FINANCIALS | 4 | 0.58 | SPY base case is modest given mixed breadth and pending FOMC/data. Selected holdings clear the active hurdle on recent relative strength, lower concentration risk, and scheduled macro/earnings events before August 27. | FOMC hawkish surprise lifting yields and pressuring equities; Tech mega-cap rebound reversing equal-weight and sector rotation; Oil price collapse on geopolitics resolution; Weaker-than-expected August employment or CPI data |
| xai-grok-4-3 | xai | portfolio | DIVIDEND | 3 | 0.55 | Value and defensive equity tilt for one-month window based on recent active returns and macro data. | FOMC policy surprise on July 29; August CPI deviation from 3.5% YoY; Sector rotation away from financials and healthcare |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 4 | 0.55 | Overweight relatively strong, lower-volatility financials, healthcare, and dividend equity with an SPY anchor to seek modest alpha with downside protection into the FOMC and earnings. | Hawkish FOMC surprise (38% priced hike) hitting rate-sensitive and equity broadly; Mega-cap earnings disappointment dragging the index; Defensive rotation reverses if strong growth data revives risk-on tech leadership |
| anthropic-claude-fable-5 | anthropic | portfolio | EQUAL_WEIGHT_SP500 | 4 | 0.58 | Rotation from concentrated tech into breadth: equal-weight, value, financials, and healthcare all show positive recent relative strength, shallow drawdowns, and resilience to the elevated-rate scenario. | Mega-cap earnings (MSFT, META, AAPL, AMZN) and Nvidia Aug 26 could reignite narrow tech leadership, hurting breadth trades; A hawkish 25bp hike on July 29 could pressure all equities including value sectors; Soft July payrolls (Aug 7) or CPI surprise could trigger broad risk-off; Financials exposed to credit-quality surprises in the Aug 3 loan officer survey |
| openai-gpt-5-5 | openai | portfolio | DIVIDEND | 5 | 0.57 | SPY is forecast to rise modestly, but selected active holdings have stronger one-month base cases from positive breadth, shallow drawdowns, and near-term macro/earnings catalysts. Diversification across five clusters reduces dependence on a single theme. | Mega-cap technology leadership resumes, causing SPY to outperform diversified value and defensive sector tilts.; FOMC, CPI, payrolls, or GDP/PCE data surprise hawkishly or recessionarily, pressuring equities broadly.; Financials could underperform if loan survey, credit, or yield-curve signals worsen.; Recent sector and factor rotation could reverse because volume was below its 20-session average and signals are short-horizon. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| ETHEREUM_ETF | Ethereum ETF | 14.71 | 18.8700008392334 | 0.28280087282348054 | 1 |
| BITCOIN_ETF | Bitcoin ETF | 36.77 | 45.290000915527344 | 0.23171065856750994 | 2 |
| SOFTWARE | Software | 90.91 | 110.31999969482422 | 0.21350786156445078 | 3 |
| METALS_MINING | Metals and Mining | 103.11 | 123.0 | 0.19290078556881007 | 4 |
| SILVER | Silver | 52.93 | 62.77000045776367 | 0.1859059221190944 | 5 |
| SOUTH_AFRICA | South Africa Equities | 61.94 | 71.55999755859375 | 0.1553115524474291 | 6 |
| CYBERSECURITY | Cybersecurity | 89.1 | 100.79000091552734 | 0.13120090814284335 | 7 |
| SOUTH_KOREA | South Korea Equities | 161.2 | 182.13999938964844 | 0.12990074063057344 | 8 |
| GOLD | Gold | 76.78 | 86.62000274658203 | 0.12815841034881514 | 9 |
| BIOTECH | Biotechnology | 150.59 | 168.22999572753906 | 0.11713922390290898 | 10 |
| TAIWAN | Taiwan Equities | 97.81 | 108.62999725341797 | 0.11062260764152909 | 11 |
| BROAD_AI_TECH | Broad AI Technology | 58.3 | 64.54000091552734 | 0.10703260575518603 | 12 |
| TECHNOLOGY | Technology Sector | 174.3 | 188.61000061035156 | 0.08209983138469057 | 13 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 114.87 | 124.16000366210938 | 0.08087406339435343 | 14 |
| ENERGY | Energy Sector | 58.36 | 62.290000915527344 | 0.06734065996448502 | 15 |
| BROAD_COMMODITIES | Broad Commodities | 17.34 | 18.420000076293945 | 0.06228374142410287 | 16 |
| LARGE_GROWTH | US Large-Cap Growth | 117.13 | 123.88999938964844 | 0.05771364628744502 | 17 |
| NASDAQ100 | Nasdaq 100 | 682.12 | 721.1099853515625 | 0.05716000901829954 | 18 |
| HEALTHCARE | Healthcare Sector | 163.4 | 171.5800018310547 | 0.05006121071636893 | 19 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.0 | 73.41999816894531 | 0.04885711669921866 | 20 |
| CANADA | Canada Equities | 59.39 | 62.2599983215332 | 0.04832460551495532 | 21 |
| EMERGING_MARKETS | Emerging Markets | 58.23 | 61.0099983215332 | 0.047741685068404704 | 22 |
| JAPAN | Japan Equities | 91.51 | 95.83999633789062 | 0.04731719307060023 | 23 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 110.84 | 115.87999725341797 | 0.04547092433614197 | 24 |
| SEMICONDUCTORS | Semiconductors | 548.55 | 573.0 | 0.0445720535958436 | 25 |
| AGRICULTURE | Agriculture Commodities | 27.62 | 28.81999969482422 | 0.04344676664823388 | 26 |
| SP500 | S&P 500 | 739.09 | 771.0999755859375 | 0.04330998333888636 | 27 |
| AUSTRALIA | Australia Equities | 28.88 | 30.110000610351562 | 0.04259004883488804 | 28 |
| TOTAL_US_MARKET | Total US Stock Market | 365.18 | 380.6300048828125 | 0.042307916322943395 | 29 |
| OIL | Crude Oil | 124.76 | 130.00999450683594 | 0.04208075109679332 | 30 |
| DIVIDEND | US Dividend Equities | 33.43 | 34.83000183105469 | 0.04187860697142343 | 31 |
| EUROPE | Europe Equities | 88.84 | 92.27999877929688 | 0.03872128297272481 | 32 |
| MATERIALS | Materials Sector | 51.39 | 53.22999954223633 | 0.035804622343575065 | 33 |
| COMMUNICATIONS | Communication Services Sector | 107.66 | 111.41000366210938 | 0.034831912150375066 | 34 |
| LARGE_VALUE | US Large-Cap Value | 249.74 | 257.5799865722656 | 0.031392594587433376 | 35 |
| COPPER | Copper | 38.77 | 39.97999954223633 | 0.03120968641311128 | 36 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 215.18 | 221.4499969482422 | 0.029138381579339123 | 37 |
| YEN | Japanese Yen | 56.01 | 57.5 | 0.02660239242992324 | 38 |
| UNITED_KINGDOM | United Kingdom Equities | 47.37 | 48.630001068115234 | 0.02659913591123564 | 39 |
| EURO | Euro | 104.95 | 107.54000091552734 | 0.024678427017887916 | 40 |
| SMALL_CAP | US Small-Cap Stocks | 292.91 | 299.80999755859375 | 0.02355671557336292 | 41 |
| FINANCIALS | Financials Sector | 56.88 | 57.880001068115234 | 0.017580890789648862 | 42 |
| INDIA | India Equities | 48.89 | 49.529998779296875 | 0.01309058660864948 | 43 |
| CHINA | China Equities | 54.26 | 54.900001525878906 | 0.011795088939898779 | 44 |
| SMALL_VALUE | US Small-Cap Value | 222.16 | 224.74000549316406 | 0.011613276436640563 | 45 |
| MID_CAP | US Mid-Cap Stocks | 76.0 | 76.6500015258789 | 0.00855265165630148 | 46 |
| MEXICO | Mexico Equities | 76.54 | 77.16000366210938 | 0.008100387537357756 | 47 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.27 | 79.87000274658203 | 0.007569102391598692 | 48 |
| MOMENTUM | US Momentum Equities | 302.33 | 304.2300109863281 | 0.006284559872748785 | 49 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.51 | 106.7300033569336 | 0.0020655652702430416 | 50 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 94.96 | 95.12999725341797 | 0.0017901985406274523 | 51 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.37 | 93.5199966430664 | 0.0016064757745142266 | 52 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.69 | 97.83000183105469 | 0.0014331234625313272 | 53 |
| TIPS | Treasury Inflation-Protected Securities | 107.39 | 107.44000244140625 | 0.0004656154335249685 | 54 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.62 | 91.62999725341797 | 0.0001091164965942859 | 55 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 56 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.28 | 93.2300033569336 | -0.0005359845954803211 | 57 |
| BRAZIL | Brazil Equities | 35.87 | 35.7599983215332 | -0.0030666762884525856 | 58 |
| CONSUMER_STAPLES | Consumer Staples Sector | 85.36 | 85.08000183105469 | -0.0032802034787408063 | 59 |
| MUNICIPAL_BONDS | Municipal Bonds | 105.8 | 105.38999938964844 | -0.003875242063814399 | 60 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.92 | 47.70000076293945 | -0.004590969053851146 | 61 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 83.75 | 83.12999725341797 | -0.007403017869636153 | 62 |
| REGIONAL_BANKS | Regional Banks | 75.52 | 74.3499984741211 | -0.015492604950727018 | 63 |
| US_DOLLAR | US Dollar | 28.6 | 28.020000457763672 | -0.0202797042739975 | 64 |
| INDUSTRIALS | Industrials Sector | 183.2 | 178.8000030517578 | -0.024017450590841594 | 65 |
| REAL_ESTATE | Real Estate Sector | 45.76 | 44.65999984741211 | -0.02403846487298711 | 66 |
| LOW_VOL | US Low Volatility Equities | 77.22 | 75.12000274658203 | -0.027194991626754317 | 67 |
| SOLAR | Solar Energy | 51.56 | 49.7400016784668 | -0.03529864859451526 | 68 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 243.91 | 234.25999450683594 | -0.039563796044295274 | 69 |
| UTILITIES | Utilities Sector | 45.68 | 43.18000030517578 | -0.05472853972907654 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 25.0 | 0.029138381579339123 | 0.007284595394834781 | Breadth rotation: RSP beat SPY by 1.7% over 5 sessions with low volatility and zero drawdown from highs; hedges mega-cap earnings concentration risk. |
| anthropic-claude-fable-5 | LARGE_VALUE | 25.0 | 0.031392594587433376 | 0.007848148646858344 | At 52-week high, low 11.9% vol, positive prior and recent active returns; value benefits if the 38%-priced hike materializes and rates stay elevated. |
| anthropic-claude-fable-5 | FINANCIALS | 25.0 | 0.017580890789648862 | 0.0043952226974122155 | +5.76% active over 21 sessions, at 52-week high, shallow 2.4% drawdown; benefits from elevated rate environment (10y at 4.65%, possible Fed hike). |
| anthropic-claude-fable-5 | HEALTHCARE | 25.0 | 0.05006121071636893 | 0.012515302679092233 | +4.34% active over 21 sessions after a prior lag, near 52-week high, low beta 0.32 provides defense into a hike-risk FOMC and stretched tech valuations. |
| anthropic-claude-opus-4-8 | FINANCIALS | 30.0 | 0.017580890789648862 | 0.005274267236894658 | Strong recent relative strength (+5.76% active 21d), low drawdown, low volatility, and breadth favoring value/cyclicals. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 25.0 | 0.05006121071636893 | 0.012515302679092233 | Defensive leadership with +4.34% active 21d, low drawdown, positive recent breadth, low beta cushions downside. |
| anthropic-claude-opus-4-8 | DIVIDEND | 25.0 | 0.04187860697142343 | 0.010469651742855857 | Low-beta dividend equity with +3.95% active 21d and shallow drawdown; strong defensive carry. |
| anthropic-claude-opus-4-8 | SP500 | 20.0 | 0.04330998333888636 | 0.008661996667777273 | Core broad market anchor for the horizon. |
| anthropic-claude-opus-5 | EQUAL_WEIGHT_SP500 | 30.0 | 0.029138381579339123 | 0.008741514473801736 | Broadening breadth (adv/dec 1.9:1, RSP-SPY +0.97% over 21 sessions) with lowest volatility and zero drawdown from highs. |
| anthropic-claude-opus-5 | HEALTHCARE | 20.0 | 0.05006121071636893 | 0.010012242143273786 | Defensive sector with strong recent relative strength (+4.34% active 21s), low beta 0.315, shallow 3.7% drawdown, near 52w high. |
| anthropic-claude-opus-5 | FINANCIALS | 20.0 | 0.017580890789648862 | 0.0035161781579297726 | At 52-week high, +5.76% active 21s, low volatility 13%, benefits from steeper curve if Fed holds/hikes. |
| anthropic-claude-opus-5 | DIVIDEND | 15.0 | 0.04187860697142343 | 0.006281791045713514 | Quality income tilt at 52-week high with 0.27 beta and +3.95% active 21s; ballast if mega-cap tech corrects. |
| anthropic-claude-opus-5 | ENERGY | 15.0 | 0.06734065996448502 | 0.010101098994672751 | Strong 21-session active return +7.24%, negative SPY correlation offers hedge against oil re-spike from unresolved US-Iran situation. |
| google-gemini-3-1-pro | HEALTHCARE | 30.0 | 0.05006121071636893 | 0.01501836321491068 | Healthcare offers defensive growth characteristics and has shown recent relative strength. |
| google-gemini-3-1-pro | INDUSTRIALS | 30.0 | -0.024017450590841594 | -0.007205235177252477 | Industrials benefit from steady economic data and infrastructure spending. |
| google-gemini-3-1-pro | GOLD | 40.0 | 0.12815841034881514 | 0.05126336413952606 | Gold provides a hedge against inflation and geopolitical uncertainty. |
| openai-gpt-5-5 | DIVIDEND | 30.0 | 0.04187860697142343 | 0.012563582091427028 | Dividend equities combine positive 5-day and 21-day active performance with low volatility, shallow drawdown, and a new-high entry, offering defensive participation if breadth continues. |
| openai-gpt-5-5 | FINANCIALS | 20.0 | 0.017580890789648862 | 0.0035161781579297726 | Financials have the strongest recent active return among selected U.S. sectors, shallow drawdown, and a new-high entry, with near-term catalysts from FOMC communication and loan survey data. |
| openai-gpt-5-5 | HEALTHCARE | 20.0 | 0.05006121071636893 | 0.010012242143273786 | Healthcare shows strong 5-day and 21-day active returns, a relatively shallow drawdown, and lower market beta than SPY, making it a plausible one-month defensive rotation candidate. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 15.0 | -0.039563796044295274 | -0.005934569406644291 | Aerospace and defense has strong immediate price momentum and positive 21-day active performance, supported by geopolitical uncertainty as a plausible near-term demand/risk catalyst. |
| openai-gpt-5-5 | LARGE_VALUE | 15.0 | 0.031392594587433376 | 0.004708889188115006 | Large value has positive prior and recent active returns, lower volatility than SPY, a shallow drawdown, and a 52-week-high entry, fitting the current breadth and rotation backdrop. |
| openai-gpt-5-6-sol | EQUAL_WEIGHT_SP500 | 50.0 | 0.029138381579339123 | 0.014569190789669562 | Broadening breadth, a positive 21-session active return, lower volatility, and a shallow drawdown support continued leadership beyond mega-caps. |
| openai-gpt-5-6-sol | HEALTHCARE | 25.0 | 0.05006121071636893 | 0.012515302679092233 | Recent relative strength and near-high positioning provide a defensive source of potential alpha amid substantial macro-event risk. |
| openai-gpt-5-6-sol | JAPAN | 25.0 | 0.04731719307060023 | 0.011829298267650057 | Strong prior relative trend and deep recent pullback create a supported rebound setup, with near-term BOJ communication as a catalyst. |
| xai-grok-4-3 | DIVIDEND | 40.0 | 0.04187860697142343 | 0.01675144278856937 | Positive active returns and defensive tilt support modest outperformance. |
| xai-grok-4-3 | HEALTHCARE | 30.0 | 0.05006121071636893 | 0.01501836321491068 | Recent outperformance and low drawdown support relative strength. |
| xai-grok-4-3 | FINANCIALS | 30.0 | 0.017580890789648862 | 0.005274267236894658 | Strong recent active returns and sector breadth support base case. |
| xai-grok-4-5 | FINANCIALS | 35.0 | 0.017580890789648862 | 0.006153311776377101 | Strong recent active returns and defensive positioning into FOMC and data releases support outperformance versus cap-weighted benchmark. |
| xai-grok-4-5 | HEALTHCARE | 30.0 | 0.05006121071636893 | 0.01501836321491068 | Positive 21-session active return, shallow drawdown, and defensive characteristics favor relative strength in uncertain macro window. |
| xai-grok-4-5 | EQUAL_WEIGHT_SP500 | 20.0 | 0.029138381579339123 | 0.005827676315867825 | Breadth improvement and RSP outperformance versus SPY indicate equal-weight catch-up potential over the month. |
| xai-grok-4-5 | ENERGY | 15.0 | 0.06734065996448502 | 0.010101098994672751 | Elevated prior active trend and oil price context support continued sector contribution despite recent pullback. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| google-gemini-3-1-pro | GOLD | 3 | 0.65 | 0.12815841034881514 | 0.05907649217718426 | 0.015766508838297902 | 0.2237243806462963 |  | True | True |
| openai-gpt-5-6-sol | EQUAL_WEIGHT_SP500 | 3 | 0.58 | 0.029138381579339123 | 0.03891379173641185 | -0.0043961916024745085 | 0.2438870810870687 |  | False | True |
| anthropic-claude-opus-5 | EQUAL_WEIGHT_SP500 | 5 | 0.55 | 0.029138381579339123 | 0.03865282481539156 | -0.004657158523494798 | 0.24414804800808898 |  | False | True |
| xai-grok-4-5 | FINANCIALS | 4 | 0.58 | 0.017580890789648862 | 0.03710045030182836 | -0.006209533037057999 | 0.2457004225216522 |  | False | True |
| xai-grok-4-3 | DIVIDEND | 3 | 0.55 | 0.04187860697142343 | 0.0370440732403747 | -0.006265910098511657 | 0.24575679958310584 |  | False | True |
| anthropic-claude-opus-4-8 | FINANCIALS | 4 | 0.55 | 0.017580890789648862 | 0.03692121832662002 | -0.006388765012266338 | 0.24587965449686053 |  | False | True |
| anthropic-claude-fable-5 | EQUAL_WEIGHT_SP500 | 4 | 0.58 | 0.029138381579339123 | 0.03204326941819757 | -0.011266713920688787 | 0.25075760340528297 |  | False | True |
| openai-gpt-5-5 | DIVIDEND | 5 | 0.57 | 0.04187860697142343 | 0.024866322174101303 | -0.018443661164785057 | 0.25793455064937926 |  | False | True |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 76e4f491cb9be2449b6ac3404b95dbc4f886c7952f7cef36ce859ea550103fa4 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | ef3cf65c548d3cc3229f74393dc61292363e4cb8a6e609b4a75e4c2062b6698e |
| manifest.yaml | bf16033e25de00ed65b3449a13c7b71cfc5b8aa60e39b162e3e2eeb376c06730 |
| submission_schema.json | 722025ee45d276e3f4d132a6be281de790a0c5478dc0051f23ade0524ff79571 |
| market_data/universe_decision_context.csv | f5f72a5ada66f0072dfb804216c6bcbc19cd229317f647bd13f568d393fbe87c |
| market_data/universe_decision_context.md | a7ec6d0d96778f031ce73f1a68334929a99a9dfe5a1381eb669964e7a973f678 |
| market_data/universe_decision_context.json | 283553a9ac5588474d83a1bce2ea0e386df88d881e348172cf6bd4eecb9ee13f |
| market_data/decision_context_source_history.json | 1be80a25dcdd31ab5344ee3928e62a67b284e69cde051a5acb3f819bca6c9c56 |
| market_data/universe_quality_evidence.md | f1f6540bb68b8a7bb7620f1f52e45a467e795da928d7a7e52006f7691ab66133 |
| market_data/universe_quality_evidence.json | 69ad1aab5f28590b2466ab316b8dd6b80962b973812e5af210554be22439ee3f |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | ee7cae6ff30b609be0cecc7ed3bba0e8c99653ef43124598fd5144b456b31665 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | e64875c961a660b81c28e8cfeddbe736ce2db3c2ef963597abec369f4e4d0508 | yes |
| Final briefing | research/final_briefing.md | model-facing | 76e4f491cb9be2449b6ac3404b95dbc4f886c7952f7cef36ce859ea550103fa4 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
