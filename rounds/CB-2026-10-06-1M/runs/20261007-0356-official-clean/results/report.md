# CapitalBench Report: CB-2026-10-06-1M / 20261007-0356-official-clean

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: 20261007-0356-official-clean
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-10-06-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-10-06
- Decision deadline: 2026-10-07T03:45:00Z
- Horizon: one month
- Entry date: 2026-10-06
- Exit date: 2026-11-06
- Entry rule: Use the October 6, 2026 official adjusted close supplied in prices/entry_prices.csv; CASH is fixed at 1.0.
- Exit rule: Use the November 6, 2026 official adjusted close supplied in prices/exit_prices.csv; CASH is fixed at 1.0.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | xai | portfolio | FINANCIALS | 3 | 0.59 | Elevated inflation readings, Fed hike to 3.75-4%, long yields >5%, soft payrolls with revisions, and oil forecast hike create mixed one-month setup; large-cap strength vs small-cap/equal-weight lag and high cross-sectional dispersion favor selective quality pullbacks over pure continuation or extreme crypto. | Further Fed hawkishness or higher-than-expected CPI/PPI could extend rate pressure and delay financials/small-value rebound; Oil price spike persistence from Middle East shut-ins may raise input costs and volatility without helping pure equity pullbacks; High dispersion and soft payrolls raise recession-scare risk that hits beta>1 names harder than SPY; Biotech clinical/financing sensitivity could convert pullback into continued deterioration if risk appetite fades |
| xai-grok-4-3 | xai | portfolio | BIOTECH | 3 | 0.5833 | Services and manufacturing diffusion above 50 with positive real GDP and consumption growth offset by weak payrolls, downward revisions, elevated price indexes, and divergent large-small cap closes. | payroll revisions and weak employment data; elevated services and manufacturing price indexes; divergent large-small cap performance; scheduled CPI PPI and FOMC events within horizon |
| google-gemini-3-1-pro | google | portfolio | BIOTECH | 3 | 0.58 | The market shows mixed signals with positive GDP and consumption growth but cautious manufacturing and downward payroll revisions. Long Treasury yields are elevated, and there is a divergence between large and small caps. | Continued divergence between large and small caps could hurt SMALL_VALUE.; Elevated long Treasury yields could pressure equity valuations, particularly in growth-sensitive sectors like BIOTECH. |
| xai-grok-4-6 | xai | portfolio | FINANCIALS | 3 | 0.57 | SPY is at a 52-week high with large-cap outperformance versus equal-weight and small caps, while inflation prints, survey prices, and a September hike keep duration and high-beta risk elevated into a dense data/FOMC calendar. Quality pullbacks in financials, biotech, and small value look more like temporary relative overshoots than confirmed deterioration; many shock names remain high-vol with weak quality. | September CPI, PCE, and the Oct 27-28 FOMC can extend large-cap leadership if inflation stays sticky; Payrolls of +29k with downward revisions can hit small-value and financials if growth fears dominate rates; High-vol EM, mining, solar, and crypto tails can reverse independently of the quality-pullback thesis |
| openai-gpt-6-astra | openai | portfolio | FINANCIALS | 3 | 0.555 | Cross-sectional divergence is large, although the aggregate dispersion statistic is missing and Ethereum is an extreme outlier. Expanding activity and positive real spending argue against indiscriminate recession positioning, while elevated prices, a recent Fed hike and weak employment constrain broad risk taking. Selective pullback reversals are more credible than buying every laggard; energy has independent supply support. The October inflation releases, FOMC meeting and November 6 employment report can materially change leadership before the exit. | October inflation releases or the October 27-28 FOMC meeting could reinforce tightening expectations and extend biotechnology and financial-sector losses.; The November 6 employment report arrives before the exit close; renewed labor deterioration could overwhelm financials' reversal case.; Middle East supply restoration or demand weakness could reverse the oil-price support behind the top-ranked energy judgment.; Quality scores are constructed from price history, not business fundamentals; unreported sector deterioration could make apparent overreactions persistent.; Ethereum's extreme reported return and volatility, plus the missing dispersion statistic, reduce confidence in cross-sectional tail calibration. |
| anthropic-claude-fable-5-1 | anthropic | portfolio | ENERGY | 3 | 0.56 | Macro is late-cycle hawkish: Fed hiking to 3.75-4.00%, 10y at 5.27%, 30y at 5.64%, services prices index at post-2022 high, manufacturing prices up 6.8 points, Brent forecast raised to $105, yet payrolls were only +29k with -60k revisions. Breadth is narrow (RSP minus SPY -4.09% over 21 sessions, only 32% of assets positive) with leadership concentrated in semis, cyber, Taiwan and an extreme crypto outlier. Rate pressure argues against duration and small caps; energy-linked and inflation-resilient equity and high-quality cyclicals that sold off on positioning rather than fundamentals have the best reversal odds, but the FOMC on Oct 27-28, CPI on Oct 14 and the Nov 6 jobs print inside the window keep the bar for beating SPY high. | Oct 14 CPI or Oct 27-28 FOMC hawkish surprise could hit high-beta cyclicals like XME harder than SPY; Oil forecast inputs were completed Oct 1 and a de-escalation of Middle East shut-ins could reverse energy quickly; Narrow mega-cap tech leadership may persist, leaving SPY ahead of sector reversal candidates; Nov 6 payroll report prints before exit close and could reprice financials and small caps in either direction |
| anthropic-claude-opus-5-5 | anthropic | portfolio | SP500 | 1 | 0.5 | Narrow cap-weighted leadership. RSP lags SPY by 4.09% over 21 sessions and only 31.88% of assets were positive over 21 sessions. Long yields sit above 5%, the Fed is hiking with inflation elevated, and payrolls are weakening. That macro backdrop supports large-cap quality over rate-sensitive and cyclical pullbacks, so reversal edges are weak. | Hot CPI on Oct 14 or a hawkish FOMC on Oct 27-28 drives a broad selloff in which beta matters more than selection; A sharp rally in small caps and breadth catches up with the cap-weighted index; An oil spike toward the $105 Brent forecast rotates leadership toward energy; A soft October jobs report on Nov 6 moves markets just before the exit close |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| HEALTHCARE | Healthcare Sector | 167.09 | 184.8 | 0.10599078341013835 | 1 |
| CONSUMER_STAPLES | Consumer Staples Sector | 81.8 | 90.08 | 0.10122249388753057 | 2 |
| INDIA | India Equities | 46.73 | 50.89 | 0.08902204151508686 | 3 |
| LOW_VOL | US Low Volatility Equities | 71.73 | 76.87 | 0.07165760490729123 | 4 |
| DIVIDEND | US Dividend Equities | 32.85 | 35.17 | 0.0706240487062404 | 5 |
| REAL_ESTATE | Real Estate Sector | 41.1 | 44.0 | 0.07055961070559613 | 6 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 77.28 | 81.92 | 0.0600414078674949 | 7 |
| FINANCIALS | Financials Sector | 54.01 | 57.16 | 0.05832253286428446 | 8 |
| MEXICO | Mexico Equities | 72.69000244140625 | 76.73999786376953 | 0.05571598963183266 | 9 |
| SOUTH_AFRICA | South Africa Equities | 63.65999984741211 | 67.05999755859375 | 0.05340869807306259 | 10 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 111.72 | 117.58 | 0.052452559971357005 | 11 |
| UTILITIES | Utilities Sector | 41.16 | 43.13 | 0.04786200194363466 | 12 |
| MATERIALS | Materials Sector | 49.73 | 51.95 | 0.044641061733360354 | 13 |
| MUNICIPAL_BONDS | Municipal Bonds | 101.0199966430664 | 104.91000366210938 | 0.03850729705315192 | 14 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 89.125 | 91.86 | 0.030687237026647995 | 15 |
| REGIONAL_BANKS | Regional Banks | 70.07 | 72.2 | 0.03039817325531624 | 16 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 89.36000061035156 | 92.06999969482422 | 0.030326757676395255 | 17 |
| SOLAR | Solar Energy | 44.4 | 45.58 | 0.026576576576576638 | 18 |
| OIL | Crude Oil | 144.91000366210938 | 148.41000366210938 | 0.0241529218932397 | 19 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 102.14 | 104.53 | 0.023399255923242546 | 20 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 94.36 | 96.55 | 0.023208986858838543 | 21 |
| LARGE_VALUE | US Large-Cap Value | 251.74 | 257.45 | 0.022682132358782692 | 22 |
| AUSTRALIA | Australia Equities | 28.549999237060547 | 29.170000076293945 | 0.021716317190950463 | 23 |
| TIPS | Treasury Inflation-Protected Securities | 104.18 | 106.27 | 0.02006143213668632 | 24 |
| UNITED_KINGDOM | United Kingdom Equities | 46.37 | 47.22 | 0.0183308173387966 | 25 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 212.33 | 216.05 | 0.01751989827155831 | 26 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 46.849998474121094 | 47.59000015258789 | 0.015795127055885816 | 27 |
| CANADA | Canada Equities | 59.18 | 59.94 | 0.012842176410949646 | 28 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 90.94999694824219 | 91.95999908447266 | 0.011105026609349311 | 29 |
| BIOTECH | Biotechnology | 150.9 | 152.21 | 0.008681245858184194 | 30 |
| EUROPE | Europe Equities | 86.58 | 87.31 | 0.008431508431508528 | 31 |
| US_DOLLAR | US Dollar | 28.899999618530273 | 29.1299991607666 | 0.007958461774125958 | 32 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.45 | 91.46 | 0.00010934937124096322 | 33 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 34 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 77.27 | 77.23 | -0.0005176653293644806 | 35 |
| YEN | Japanese Yen | 57.93000030517578 | 57.790000915527344 | -0.002416699273449341 | 36 |
| CHINA | China Equities | 52.22 | 51.89 | -0.006319417847567954 | 37 |
| SMALL_VALUE | US Small-Cap Value | 212.37 | 210.7 | -0.007863634223289617 | 38 |
| EURO | Euro | 103.91999816894531 | 102.7699966430664 | -0.011066219651094666 | 39 |
| GOLD | Gold | 78.37 | 76.38 | -0.02539236952915669 | 40 |
| MID_CAP | US Mid-Cap Stocks | 74.0 | 72.11 | -0.025540540540540557 | 41 |
| SMALL_CAP | US Small-Cap Stocks | 281.34 | 273.67 | -0.027262387147223843 | 42 |
| ENERGY | Energy Sector | 63.75 | 61.62 | -0.03341176470588236 | 43 |
| BROAD_COMMODITIES | Broad Commodities | 19.46 | 18.77 | -0.035457348406988776 | 44 |
| DEVELOPED_EX_US | Developed Markets ex-US | 71.11 | 67.9 | -0.04514133033328638 | 45 |
| INDUSTRIALS | Industrials Sector | 171.58 | 162.67 | -0.051929129269145724 | 46 |
| TOTAL_US_MARKET | Total US Stock Market | 382.54 | 361.93 | -0.05387671877450728 | 47 |
| SP500 | S&P 500 | 779.09 | 735.29 | -0.05621943549525732 | 48 |
| COPPER | Copper | 40.029998779296875 | 37.66999816894531 | -0.05895580020782143 | 49 |
| COMMUNICATIONS | Communication Services Sector | 111.65 | 104.79 | -0.06144200626959251 | 50 |
| EMERGING_MARKETS | Emerging Markets | 60.62 | 55.29 | -0.08792477730122072 | 51 |
| AGRICULTURE | Agriculture Commodities | 28.850000381469727 | 26.110000610351562 | -0.09497399427689635 | 52 |
| SOFTWARE | Software | 111.16 | 98.88 | -0.11047139258726157 | 53 |
| JAPAN | Japan Equities | 99.32 | 88.26 | -0.11135722915827617 | 54 |
| BITCOIN_ETF | Bitcoin ETF | 48.4900016784668 | 42.880001068115234 | -0.11569396609946547 | 55 |
| LARGE_GROWTH | US Large-Cap Growth | 129.19 | 111.75 | -0.1349949686508244 | 56 |
| NASDAQ100 | Nasdaq 100 | 759.66 | 656.1 | -0.13632414501224221 | 57 |
| METALS_MINING | Metals and Mining | 108.24 | 93.45 | -0.13664079822616404 | 58 |
| BROAD_AI_TECH | Broad AI Technology | 67.05 | 56.89 | -0.15152870991797163 | 59 |
| SILVER | Silver | 55.45000076293945 | 46.869998931884766 | -0.15473402548245252 | 60 |
| CYBERSECURITY | Cybersecurity | 108.13 | 91.04 | -0.15805049477480804 | 61 |
| ETHEREUM_ETF | Ethereum ETF | 60.88999938964844 | 50.33000183105469 | -0.1734274538421 | 62 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 127.2 | 104.8 | -0.17610062893081768 | 63 |
| TECHNOLOGY | Technology Sector | 202.0 | 164.74 | -0.1844554455445544 | 64 |
| TAIWAN | Taiwan Equities | 117.61000061035156 | 89.23999786376953 | -0.24122100671160962 | 65 |
| BRAZIL | Brazil Equities | 43.0 | 31.979999542236328 | -0.25627908041310865 | 66 |
| SOUTH_KOREA | South Korea Equities | 186.39999389648438 | 137.00999450683594 | -0.2649678165605346 | 67 |
| SEMICONDUCTORS | Semiconductors | 632.5 | 463.96 | -0.2664664031620554 | 68 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 208.26 | 68.98 | -0.668779410352444 | 69 |
| MOMENTUM | US Momentum Equities | 324.45 | 63.76 | -0.8034828170750501 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5-1 | ENERGY | 35.0 | -0.03341176470588236 | -0.011694117647058827 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | METALS_MINING | 35.0 | -0.13664079822616404 | -0.04782427937915741 | V3 selected model rank 2: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-fable-5-1 | FINANCIALS | 30.0 | 0.05832253286428446 | 0.017496759859285338 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| anthropic-claude-opus-5-5 | SP500 | 100.0 | -0.05621943549525732 | -0.05621943549525732 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| google-gemini-3-1-pro | BIOTECH | 35.0 | 0.008681245858184194 | 0.003038436050364468 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| google-gemini-3-1-pro | FINANCIALS | 35.0 | 0.05832253286428446 | 0.02041288650249956 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SMALL_VALUE | 30.0 | -0.007863634223289617 | -0.002359090266986885 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | FINANCIALS | 35.0 | 0.05832253286428446 | 0.02041288650249956 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| openai-gpt-6-astra | BIOTECH | 35.0 | 0.008681245858184194 | 0.003038436050364468 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-6-astra | SP500 | 30.0 | -0.05621943549525732 | -0.016865830648577194 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-3 | BIOTECH | 35.0 | 0.008681245858184194 | 0.003038436050364468 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | FINANCIALS | 35.0 | 0.05832253286428446 | 0.02041288650249956 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | SMALL_VALUE | 30.0 | -0.007863634223289617 | -0.002359090266986885 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| xai-grok-4-5 | FINANCIALS | 35.0 | 0.05832253286428446 | 0.02041288650249956 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | BIOTECH | 35.0 | 0.008681245858184194 | 0.003038436050364468 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-5 | SMALL_VALUE | 30.0 | -0.007863634223289617 | -0.002359090266986885 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | FINANCIALS | 35.0 | 0.05832253286428446 | 0.02041288650249956 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-6 | BIOTECH | 35.0 | 0.008681245858184194 | 0.003038436050364468 | V3 selected model rank 2: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | SMALL_VALUE | 30.0 | -0.007863634223289617 | -0.002359090266986885 | V3 selected model rank 3: overreaction with 56% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xai-grok-4-5 | FINANCIALS | 3 | 0.59 | 0.05832253286428446 | 0.021092232285877144 | 0.07731166778113446 | 0.0848985511242612 |  | True | True |
| xai-grok-4-3 | BIOTECH | 3 | 0.5833 | 0.008681245858184194 | 0.021092232285877144 | 0.07731166778113446 | 0.0848985511242612 |  | True | True |
| google-gemini-3-1-pro | BIOTECH | 3 | 0.58 | 0.008681245858184194 | 0.021092232285877144 | 0.07731166778113446 | 0.0848985511242612 |  | True | True |
| xai-grok-4-6 | FINANCIALS | 3 | 0.57 | 0.05832253286428446 | 0.021092232285877144 | 0.07731166778113446 | 0.0848985511242612 |  | True | True |
| openai-gpt-6-astra | FINANCIALS | 3 | 0.555 | 0.05832253286428446 | 0.006585491904286835 | 0.06280492739954416 | 0.0994052915058515 |  | True | True |
| anthropic-claude-fable-5-1 | ENERGY | 3 | 0.56 | -0.03341176470588236 | -0.0420216371669309 | 0.01419779832832642 | 0.14801242057706926 |  | True | False |
| anthropic-claude-opus-5-5 | SP500 | 1 | 0.5 | -0.05621943549525732 | -0.05621943549525732 | 0.0 | 0.16221021890539566 |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | c46ba581646ffee06167a6d20b89e0712e78f2bbccaacf2eb132e125756b2559 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | b0cf9b835591ce66e32f658ea0a409637a6f58535c6e08290b08283733e9174a |
| manifest.yaml | 1ccf5d76040a10f24ce4d9e81aca49007714361f28c8532ae85c921e651ba98f |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | a8338432597963fe2480c153ff8111f36e2c01389aa7875bd5c4c457d786f55a |
| market_data/universe_decision_context.md | 97c05820bfb788d6a7704c8e8ac0e9fd2e0ab6b24f7f7b0ef4303c5a25f493b1 |
| market_data/universe_decision_context.json | 33223afe413bdc5c79a2002c5c83482b8f608e4a31a3e075db1c19e89397472f |
| market_data/decision_context_source_history.json | d6d921ecb3c1c6dd6b9e5faa90d027eb0d619a56f1344b7964a6497cf612e0c0 |
| market_data/universe_quality_evidence.md | bbc2281ae7c9090834e5fd9da2e26bb300afdf1491151709d129b2612b0d18c2 |
| market_data/universe_quality_evidence.json | 87da9eb32beed941ee8ced519539d1446cd6917ec12f3e08e546875230ff796a |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | e6b8d5b26758cf6c0d83b6f6f98e65cbed3925a54a63edf6163f3c235dfba304 | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | bb98b57c663be677f5886ed0ab8bd51ef6f7855ef68f223d535dc3f43b52aa5a | yes |
| Final briefing | research/final_briefing.md | model-facing | c46ba581646ffee06167a6d20b89e0712e78f2bbccaacf2eb132e125756b2559 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
