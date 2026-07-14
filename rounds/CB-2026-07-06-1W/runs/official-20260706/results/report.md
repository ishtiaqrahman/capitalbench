# CapitalBench Report: CB-2026-07-06-1W / official-20260706

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260706
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-06-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-07-06
- Decision deadline: 2026-07-07T07:30:00Z
- Horizon: one week
- Entry date: 2026-07-06
- Exit date: 2026-07-13
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | xai | portfolio | SP500 | 4 | 0.55 | Weak June payrolls and downward revisions create scope for policy easing signals in FOMC minutes, while TSMC sales and select tech deals provide discrete mid-week events; allocation balances broad beta with targeted sector exposure. | FOMC minutes could reinforce higher-for-longer stance given 4.1% core PCE; Further downside revisions or weak follow-through data could trigger growth fears; Tech names face reversal risk after recent concentration-driven moves |
| anthropic-claude-opus-4-7 | anthropic | portfolio | FINANCIALS | 5 | 0.55 | Overweight financials/industrials/defense on catalyst mix (soft payrolls, ISM services employment recovery, FOMC minutes) with healthcare and RSP as ballast against mega-cap tech reversal risk highlighted by MTUM/SMH weekly drawdowns. | FOMC minutes read hawkish, hitting rate-sensitive financials and cyclicals; Mega-cap tech rebound leaves equal-weight/value tilt lagging SPY benchmark; Weaker payroll revisions signal deeper slowdown, hurting cyclicals; Oil/commodity weakness spills into risk sentiment |
| anthropic-claude-opus-4-8 | anthropic | portfolio | FINANCIALS | 5 | 0.58 | Overweight cyclicals showing broad participation and 52w highs, with healthcare and SPY ballast for a one-week close-to-close window. | FOMC minutes on July 8 could signal hawkish stance, pressuring rate-sensitive financials and cyclicals; Recent sector strength may reverse; momentum-heavy positioning faces rotation risk into defensives; Narrow index breadth (most stocks declining while index near highs) suggests fragile leadership; Financials at 52w high have limited cushion if credit or curve dynamics disappoint |
| anthropic-claude-fable-5 | anthropic | portfolio | FINANCIALS | 5 | 0.5 | Overweight financials, biotech, aerospace-defense, and value on rate-cut-friendly labor data and strong breadth, with semis for AI catalysts including TSMC monthly sales Friday. | Hawkish FOMC minutes or hot inflation signals (ISM prices at 67-73) could reprice rate-cut expectations, hurting rate-sensitive financials and biotech.; Semiconductor volatility is very high (66% 30d vol, -4.4% 7d); a TSMC sales miss or AI sentiment reversal could sharply drag SMH.; Biotech and defense gains partly rest on recent price strength; momentum reversal or profit-taking near 52-week highs could cause underperformance.; Further labor-market deterioration could shift narrative from rate-cut optimism to growth fears, hitting cyclical financials and value. |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 4 | 0.65 | Overweighting semiconductors and AI-related technology based on strong corporate catalysts from TSMC, Tesla, Broadcom, and TeraWulf. | A sharp reversal in semiconductor and AI stocks given their high volatility and recent strong performance.; Hawkish surprises in the upcoming FOMC minutes could disproportionately hurt high-duration growth and tech equities.; Broader market weakness driven by declining ISM Services and Manufacturing PMIs could drag down sector-specific momentum. |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.58 | I overweight semiconductor-linked assets because the briefing contains concrete near-term company and supply-chain catalysts before the exit date. The remaining positions target areas with strong relative performance and plausible continuation, while acknowledging reversal risk after sharp recent gains. | TSMC monthly sales or commentary disappoints, causing semiconductor and Taiwan exposures to underperform sharply.; FOMC minutes emphasize elevated inflation and reduce rate-cut expectations, pressuring high-beta technology and biotech holdings.; Recent momentum in biotech, cybersecurity, and aerospace-defense reverses because independent one-week catalysts are limited outside semiconductors.; A broad risk-off move or profit-taking near S&P 500 highs disproportionately hurts the portfolio's high-beta and thematic exposures. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 104.3499984741211 | 117.79000091552734 | 0.1287973420022559 | 1 |
| ENERGY | Energy Sector | 53.13 | 56.7400016784668 | 0.06794657779911151 | 2 |
| BROAD_COMMODITIES | Broad Commodities | 16.1 | 16.899999618530273 | 0.04968941730001686 | 3 |
| BRAZIL | Brazil Equities | 34.91999816894531 | 35.38999938964844 | 0.013459371287169786 | 4 |
| COMMUNICATIONS | Communication Services Sector | 110.21 | 111.58999633789062 | 0.01252151654015643 | 5 |
| CANADA | Canada Equities | 58.06 | 58.72999954223633 | 0.011539778543512291 | 6 |
| DIVIDEND | US Dividend Equities | 32.24 | 32.560001373291016 | 0.00992560090853023 | 7 |
| CHINA | China Equities | 52.02 | 52.529998779296875 | 0.009803898102592745 | 8 |
| UTILITIES | Utilities Sector | 45.3 | 45.720001220703125 | 0.009271550125896866 | 9 |
| REAL_ESTATE | Real Estate Sector | 44.29 | 44.70000076293945 | 0.009257185887095343 | 10 |
| AGRICULTURE | Agriculture Commodities | 27.540000915527344 | 27.719999313354492 | 0.006535889318931121 | 11 |
| US_DOLLAR | US Dollar | 28.31999969482422 | 28.5 | 0.006355943047862356 | 12 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.1 | 84.58999633789062 | 0.005826353601553258 | 13 |
| LOW_VOL | US Low Volatility Equities | 76.17 | 76.41000366210938 | 0.00315089486818132 | 14 |
| COPPER | Copper | 37.84000015258789 | 37.939998626708984 | 0.0026426657959264244 | 15 |
| LARGE_VALUE | US Large-Cap Value | 247.24 | 247.6199951171875 | 0.0015369483788525429 | 16 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.43 | 91.5 | 0.0007656130372961645 | 17 |
| AUSTRALIA | Australia Equities | 28.33 | 28.350000381469727 | 0.0007059788729166794 | 18 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 19 |
| FINANCIALS | Financials Sector | 56.14 | 56.06999969482422 | -0.0012468882289949912 | 20 |
| YEN | Japanese Yen | 56.59000015258789 | 56.459999084472656 | -0.0022972445266778996 | 21 |
| SP500 | S&P 500 | 751.28 | 749.1699829101562 | -0.0028085628392127138 | 22 |
| HEALTHCARE | Healthcare Sector | 161.96 | 161.41000366210938 | -0.003395877611080733 | 23 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 215.0 | 214.22999572753906 | -0.0035814152207485073 | 24 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.87 | 79.5199966430664 | -0.004382162976506843 | 25 |
| TOTAL_US_MARKET | Total US Stock Market | 371.67 | 369.7799987792969 | -0.005085159471313605 | 26 |
| EURO | Euro | 105.56999969482422 | 105.01000213623047 | -0.00530451416323352 | 27 |
| TIPS | Treasury Inflation-Protected Securities | 108.49 | 107.91000366210938 | -0.005346081094023569 | 28 |
| REGIONAL_BANKS | Regional Banks | 75.56 | 75.12000274658203 | -0.0058231505216777 | 29 |
| MUNICIPAL_BONDS | Municipal Bonds | 107.56999969482422 | 106.9000015258789 | -0.00622848536623688 | 30 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 48.220001220703125 | 47.88999938964844 | -0.00684367114683937 | 31 |
| SMALL_VALUE | US Small-Cap Value | 221.74 | 219.77999877929688 | -0.008839186527929699 | 32 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 94.18 | 93.29000091552734 | -0.009449979660996588 | 33 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 98.66 | 97.70999908447266 | -0.009629038268065493 | 34 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 96.3499984741211 | 95.37999725341797 | -0.010067475205655096 | 35 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 94.27999877929688 | 93.26000213623047 | -0.010818802039382125 | 36 |
| LARGE_GROWTH | US Large-Cap Growth | 123.0 | 121.58999633789062 | -0.01146344440739333 | 37 |
| CYBERSECURITY | Cybersecurity | 92.91 | 91.83999633789062 | -0.011516560780425955 | 38 |
| TECHNOLOGY | Technology Sector | 183.57 | 181.27999877929688 | -0.012474811901199145 | 39 |
| ETHEREUM_ETF | Ethereum ETF | 13.550000190734863 | 13.369999885559082 | -0.013284155176533585 | 40 |
| NASDAQ100 | Nasdaq 100 | 722.82 | 711.739990234375 | -0.015328864400023567 | 41 |
| MID_CAP | US Mid-Cap Stocks | 76.42 | 75.23999786376953 | -0.015441011989406839 | 42 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 108.67 | 106.95999908447266 | -0.01573572205325613 | 43 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 118.01 | 116.04000091552734 | -0.016693492792752007 | 44 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 85.45 | 83.97000122070312 | -0.017320055930917233 | 45 |
| SMALL_CAP | US Small-Cap Stocks | 298.9 | 293.4800109863281 | -0.018133118145439497 | 46 |
| UNITED_KINGDOM | United Kingdom Equities | 47.22 | 46.36000061035156 | -0.018212608844736078 | 47 |
| EMERGING_MARKETS | Emerging Markets | 60.07 | 58.790000915527344 | -0.021308458206636516 | 48 |
| INDIA | India Equities | 49.88 | 48.790000915527344 | -0.021852427515490325 | 49 |
| MOMENTUM | US Momentum Equities | 321.71 | 314.6300048828125 | -0.02200738278942982 | 50 |
| SOFTWARE | Software | 94.79 | 92.69999694824219 | -0.022048771513427767 | 51 |
| EUROPE | Europe Equities | 89.97 | 87.86000061035156 | -0.02345225508112081 | 52 |
| BITCOIN_ETF | Bitcoin ETF | 36.119998931884766 | 35.220001220703125 | -0.02491688089135491 | 53 |
| JAPAN | Japan Equities | 95.27 | 92.72000122070312 | -0.026766020565727633 | 54 |
| MATERIALS | Materials Sector | 51.98 | 50.58000183105469 | -0.026933400710760114 | 55 |
| INDUSTRIALS | Industrials Sector | 185.56 | 180.3699951171875 | -0.027969416268659786 | 56 |
| SOUTH_AFRICA | South Africa Equities | 64.62999725341797 | 62.7599983215332 | -0.028933916313695462 | 57 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.89 | 69.76000213623047 | -0.029628569533586502 | 58 |
| MEXICO | Mexico Equities | 76.43000030517578 | 74.1500015258789 | -0.02983120201744227 | 59 |
| SEMICONDUCTORS | Semiconductors | 604.3 | 585.6199951171875 | -0.030911806855555946 | 60 |
| BIOTECH | Biotechnology | 160.81 | 155.33999633789062 | -0.034015320329017995 | 61 |
| METALS_MINING | Metals and Mining | 106.08 | 102.08999633789062 | -0.03761315669409293 | 62 |
| GOLD | Gold | 78.3 | 75.25 | -0.03895274584929753 | 63 |
| BROAD_AI_TECH | Broad AI Technology | 63.84 | 61.29999923706055 | -0.03978697936935238 | 64 |
| TAIWAN | Taiwan Equities | 107.2699966430664 | 101.87999725341797 | -0.050247036061567996 | 65 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 250.78 | 235.0500030517578 | -0.06272428801436392 | 66 |
| SILVER | Silver | 56.11000061035156 | 52.15999984741211 | -0.07039744644398971 | 67 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 130.11 | 120.69999694824219 | -0.07232344210097474 | 68 |
| SOLAR | Solar Energy | 57.54 | 53.119998931884766 | -0.07681614647402213 | 69 |
| SOUTH_KOREA | South Korea Equities | 189.85 | 168.02000427246094 | -0.11498549237576539 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | FINANCIALS | 25.0 | -0.0012468882289949912 | -0.0003117220572487478 | Strong breadth (67% up days, low drawdown) with soft payrolls raising rate-cut odds ahead of FOMC minutes; low volatility relative to alpha generated recently, supported by steady economy and upcoming bank earnings anticipation. |
| anthropic-claude-fable-5 | BIOTECH | 20.0 | -0.034015320329017995 | -0.0068030640658036 | Broad-based rally with 78% up days, at 52-week high, low 30d drawdown; weak jobs data supports lower rates which benefits long-duration biotech financing conditions beyond just momentum. |
| anthropic-claude-fable-5 | AEROSPACE_DEFENSE | 20.0 | -0.06272428801436392 | -0.012544857602872784 | Persistent geopolitical demand backdrop, at 52-week high with strong breadth (72% up days) and moderate volatility; defense budgets provide fundamental support independent of price trend. |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 20.0 | -0.030911806855555946 | -0.0061823613711111895 | Broadcom-Apple silicon deal, Anthropic data-center deal, TSMC strong guidance and June sales report Friday July 10 are concrete near-term catalysts; recent 7d pullback offers entry after AI-driven strength. |
| anthropic-claude-fable-5 | LARGE_VALUE | 15.0 | 0.0015369483788525429 | 0.00023054225682788142 | Rotation into value evident (+2.8% vs SPY 30d), at 52-week high with low volatility; soft labor data favoring rate-sensitive value sectors like financials embedded in IWD. |
| anthropic-claude-opus-4-7 | FINANCIALS | 30.0 | -0.0012468882289949912 | -0.0003740664686984973 | Strongest sector momentum with soft payrolls supporting rate-cut hopes; ISM services employment turned positive, benign backdrop for banks. |
| anthropic-claude-opus-4-7 | INDUSTRIALS | 20.0 | -0.027969416268659786 | -0.005593883253731957 | ISM Manufacturing still expansionary, broad sector strength, high up-day share. |
| anthropic-claude-opus-4-7 | AEROSPACE_DEFENSE | 15.0 | -0.06272428801436392 | -0.009408643202154588 | Sustained defense spending and strong recent trend with high up-day share into a quiet catalyst week. |
| anthropic-claude-opus-4-7 | HEALTHCARE | 15.0 | -0.003395877611080733 | -0.00050938164166211 | Defensive with improving 30d relative performance; low beta cushions if mega-cap tech wobbles. |
| anthropic-claude-opus-4-7 | EQUAL_WEIGHT_SP500 | 20.0 | -0.0035814152207485073 | -0.0007162830441497015 | AP noted most stocks declined despite index near ATH; equal-weight captures broadening participation. |
| anthropic-claude-opus-4-8 | FINANCIALS | 30.0 | -0.0012468882289949912 | -0.0003740664686984973 | Strong recent breadth with +4.5% 7d and +7.7% 30d, at 52w high; steepening curve context and healthy banking sector momentum with supporting sector rotation. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 25.0 | -0.027969416268659786 | -0.0069923540671649465 | At 52w high with broad participation (72% up days), solid ISM manufacturing/production, and cyclical strength; beta near 1 offers benchmark-plus without extreme volatility. |
| anthropic-claude-opus-4-8 | AEROSPACE_DEFENSE | 20.0 | -0.06272428801436392 | -0.012544857602872784 | Leading industry with +4.87% 7d, at 52w high, geopolitical tailwinds and defense budget support; positive relative strength beyond pure momentum. |
| anthropic-claude-opus-4-8 | HEALTHCARE | 15.0 | -0.003395877611080733 | -0.00050938164166211 | Defensive-cyclical mix with +6.3% 30d, at 52w high territory, low beta (0.36) cushions if market wobbles into FOMC minutes. |
| anthropic-claude-opus-4-8 | SP500 | 10.0 | -0.0028085628392127138 | -0.0002808562839212714 | Core benchmark anchor to limit tracking error against the scoring benchmark over the one-week window. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | -0.030911806855555946 | -0.012364722742222379 | Supported by strong TSMC guidance, Broadcom's new Apple agreement, and SK Hynix's capital raise plans. |
| google-gemini-3-1-pro | AUTONOMOUS_ROBOTICS | 20.0 | -0.07232344210097474 | -0.01446468842019495 | Benefits from Tesla's strong Q2 vehicle delivery and energy storage deployment numbers. |
| google-gemini-3-1-pro | BROAD_AI_TECH | 20.0 | -0.03978697936935238 | -0.007957395873870477 | Supported by ongoing AI infrastructure build-out, highlighted by TeraWulf's $19 billion data center deal with Anthropic. |
| google-gemini-3-1-pro | TECHNOLOGY | 20.0 | -0.012474811901199145 | -0.002494962380239829 | Broad technology exposure captures the positive momentum from mega-cap AI and hardware catalysts. |
| openai-gpt-5-5 | SEMICONDUCTORS | 30.0 | -0.030911806855555946 | -0.009273542056666783 | Direct exposure to the strongest near-term briefing catalysts: TSMC's July 10 monthly sales release, high Q2 guidance, AI/data-center chip demand, Broadcom's Apple silicon agreements, and reported shortages in electronic and memory components; recent weakness creates rebound potential but volatility is high. |
| openai-gpt-5-5 | TAIWAN | 25.0 | -0.050247036061567996 | -0.012561759015391999 | Taiwan equities provide concentrated semiconductor supply-chain exposure with TSMC-specific catalyst support before the exit close, while recent 30-day strength is supported by supplied chip demand and margin guidance rather than price action alone. |
| openai-gpt-5-5 | BIOTECH | 20.0 | -0.034015320329017995 | -0.0068030640658036 | Biotech has strong recent breadth and momentum near a 52-week high with moderate market beta, offering alpha potential in a risk-on week; independent catalyst support in the briefing is limited, so this is sized below the semiconductor complex. |
| openai-gpt-5-5 | AEROSPACE_DEFENSE | 15.0 | -0.06272428801436392 | -0.009408643202154588 | Aerospace and defense shows strong short-term relative strength and broad up-day participation, with industrials also near highs; sector demand and geopolitical/defense-budget priors can support continued inflows over a short horizon. |
| openai-gpt-5-5 | CYBERSECURITY | 10.0 | -0.011516560780425955 | -0.0011516560780425956 | Cybersecurity combines recent relative strength with a structural demand theme tied to enterprise technology spending, and software-related shortages in the briefing are consistent with firm IT demand, though direct catalyst support is limited. |
| xai-grok-4-3 | SP500 | 40.0 | -0.0028085628392127138 | -0.0011234251356850855 | Broad large-cap exposure to capture any risk-on response to FOMC minutes and TSMC sales data within the window. |
| xai-grok-4-3 | FINANCIALS | 20.0 | -0.0012468882289949912 | -0.00024937764579899827 | Sector positioned for potential rate policy signals and domestic growth sensitivity amid recent labor data. |
| xai-grok-4-3 | TECHNOLOGY | 20.0 | -0.012474811901199145 | -0.002494962380239829 | Exposure to semiconductor and AI supply-chain names with company-specific agreements and TSMC guidance due mid-week. |
| xai-grok-4-3 | AEROSPACE_DEFENSE | 20.0 | -0.06272428801436392 | -0.012544857602872784 | Defensive industrial exposure with stable budget visibility and limited sensitivity to the weak payroll print. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-3 | SP500 | 4 | 0.55 | -0.0028085628392127138 | -0.016412622764596697 | -0.013604059925383983 | 0.1452099647668526 |  | False | False |
| anthropic-claude-opus-4-7 | FINANCIALS | 5 | 0.55 | -0.0012468882289949912 | -0.016602257610396853 | -0.01379369477118414 | 0.14539959961265275 |  | False | False |
| anthropic-claude-opus-4-8 | FINANCIALS | 5 | 0.58 | -0.0012468882289949912 | -0.02070151606431961 | -0.017892953225106895 | 0.1494988580665755 |  | False | False |
| anthropic-claude-fable-5 | FINANCIALS | 5 | 0.5 | -0.0012468882289949912 | -0.025611462840208436 | -0.022802900000995722 | 0.15440880484246433 |  | False | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 4 | 0.65 | -0.030911806855555946 | -0.03728176941652763 | -0.03447320657731492 | 0.16607911141878354 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.58 | -0.030911806855555946 | -0.03919866441805957 | -0.036390101578846853 | 0.16799600642031548 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 614ba1d539341546f7c5934bd991865225e8cee9c8b7e4cfe2231217f69419f2 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 66320ebc013af445c33450b3005ec684487d06b5bca45c52a3ff9e8e24373e4c |
| manifest.yaml | cfa925eeb9e30a01ecb6d9abda66fc5ec3bdee16de5ce6b0b0a4817be6c1d697 |
| market_data/universe_trailing_returns.csv | 529caec62ef157d30718a21c498f976e4d5a6c0b10f6c70a992916cb93ecfdf4 |
| market_data/universe_trailing_returns.md | a1452a84ba42c5875aa782791e8f85ac371186ffe14471927800ab618337f8c6 |
| market_data/universe_trailing_returns.json | 175081d6bc6081b386e09945f6c5a038522de8adcb86ecdb5fd940dcc7135213 |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | f98201443c62b5147116460ebb6681ffde2ed5bd068a6b425c093e7d3ffc9f9a | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 530740ee6dc2fcd360a8331b3cfe4621982b9b06ead770387a90b149b9ce7a96 | yes |
| Final briefing | research/final_briefing.md | model-facing | 614ba1d539341546f7c5934bd991865225e8cee9c8b7e4cfe2231217f69419f2 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
