# CapitalBench Report: CB-2026-07-10-1M / official-20260710

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-20260710
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-07-10-1M
- Description: One-month market allocation evaluation round.
- Decision date: 2026-07-10
- Decision deadline: 2026-07-11T07:30:00Z
- Horizon: one month
- Entry date: 2026-07-10
- Exit date: 2026-08-10
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Tilt toward semiconductors and financials with earnings catalysts inside the window, supplemented by industrials breadth and cybersecurity momentum. | Hot June CPI on July 14 could lift yields and pressure high-beta semiconductor/tech holdings; Bank earnings disappointment or weak guidance July 14 hits Financials allocation; Strait of Hormuz escalation spikes oil and inflation, hurting cyclicals and growth; High-beta concentration (SMH beta 2.26, EWT 1.69) amplifies any broad-market drawdown |
| anthropic-claude-opus-4-7 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Tilt into near-term earnings catalysts (semis via TSMC, big banks) and strongest momentum sectors (biotech, cybersecurity) while avoiding oil/geopolitical volatility. | Hot June CPI (July 14) could spike yields and hit high-beta tech/biotech; Strait of Hormuz escalation spikes oil, pressures risk assets; Semiconductor high beta (2.26) amplifies any AI-trade unwind; Bank earnings disappoint on NIM or credit quality; Hawkish July 29 FOMC surprise |
| openai-gpt-5-5 | openai | portfolio | SEMICONDUCTORS | 5 | 0.58 | I favor high-beta but catalyst-supported equity themes over bonds, cash, and defensive sectors for this one-month window. Semiconductor supply-chain momentum is the core bet, complemented by earnings-sensitive financials and strong healthcare/technology subsector momentum. | A hot CPI, hawkish FOMC communication, or higher Treasury yields could trigger a growth-stock and semiconductor multiple contraction before the exit date.; TSMC, Nvidia-linked sentiment, or broader AI hardware commentary could disappoint after very strong trailing semiconductor performance.; Bank earnings could reveal weaker credit quality, deposit pressure, or lower capital-markets activity, hurting the financials allocation.; Biotech's sharp recent rally could reverse if risk appetite fades or financing conditions tighten.; Any de-escalation or escalation in Middle East tensions that lifts inflation expectations or disrupts global risk sentiment could pressure high-beta equities. |
| openai-gpt-5-6-sol | openai | portfolio | SEMICONDUCTORS | 5 | 0.61 | AI infrastructure demand, imminent semiconductor and bank earnings, and persistent leadership in cybersecurity and biotech offer the strongest one-month alpha setup. Position sizes limit, but do not eliminate, the substantial reversal risk in high-beta winners. | A hot CPI report or hawkish July FOMC communication could lift yields and compress high-growth valuations.; TSMC or other semiconductor earnings and guidance could disappoint after exceptionally strong sector gains.; Momentum reversal or profit-taking could disproportionately hurt semiconductors, cybersecurity, and biotech.; Weak bank earnings, rising credit costs, or soft loan demand could undermine financials.; Taiwan Strait tensions could sharply reduce both Taiwan and semiconductor exposure. |
| xai-grok-4-3 | xai | portfolio | SEMICONDUCTORS | 3 | 0.65 | AI-related facts dominate positive signals; overweight semiconductors and tech for expected outperformance versus S&P 500 over the one-month scoring period. | FOMC July 28-29 outcome or July 14 CPI release could shift rate expectations and pressure growth stocks; Geopolitical developments in Strait of Hormuz may elevate energy prices and inflation uncertainty; Potential earnings misses from TSMC or other tech names on July 16 |
| anthropic-claude-fable-5 | anthropic | portfolio | SEMICONDUCTORS | 5 | 0.55 | Concentrated AI/semis tilt supported by briefing facts (TSMC revenue, SK Hynix demand, Nvidia strength), diversified with bank earnings catalysts and industrial momentum. | Hot June CPI (Jul 14) or hawkish FOMC (Jul 29) could hit high-beta tech hardest given elevated PCE inflation readings; TSMC Q2 guidance disappointment would hurt SMH, EWT, and QQQ simultaneously; Iran/Strait of Hormuz escalation could spike oil and compress risk assets while portfolio holds no energy hedge; Semiconductor positioning is crowded after +57% 6m SMH run, raising sharp reversal risk |
| xai-grok-4-5 | xai | portfolio | SEMICONDUCTORS | 4 | 0.62 | Prioritize semiconductor and Taiwan exposure for AI demand and TSMC earnings catalyst, supplemented by broader tech/Nasdaq for liquidity and momentum continuation over the July-August window. | TSMC or related semiconductor earnings disappointment could reverse recent gains sharply given elevated valuations and volatility; Sticky inflation print (CPI July 14) or hawkish FOMC (July 28-29) could pressure high-beta growth/tech; Middle East/Hormuz escalation raising oil and risk-off sentiment; Mean-reversion after strong 30d/1y runs in SMH/EWT/QQQ |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.7 | Allocating to semiconductors, South Korea, and Taiwan based on strong AI demand and positive catalysts from key industry players. | A broader market sell-off or rotation out of technology stocks could negatively impact the portfolio.; Disappointing Q2 results or guidance from TSMC could lead to a sharp reversal in semiconductor and Taiwanese equities.; Geopolitical tensions in Asia or the Middle East could increase volatility and negatively affect emerging market equities. |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| OIL | Crude Oil | 108.69999694824219 | 125.92 | 0.15841769581610166 | 1 |
| SOFTWARE | Software | 92.41 | 105.01 | 0.13634887999134304 | 2 |
| METALS_MINING | Metals and Mining | 103.69 | 117.54 | 0.13357122191146686 | 3 |
| SILVER | Silver | 53.95 | 59.41 | 0.10120481927710823 | 4 |
| CYBERSECURITY | Cybersecurity | 91.88 | 100.6 | 0.09490639965171965 | 5 |
| SOUTH_AFRICA | South Africa Equities | 63.82 | 69.73 | 0.09260419931056108 | 6 |
| ENERGY | Energy Sector | 55.08 | 60.18 | 0.09259259259259256 | 7 |
| BROAD_COMMODITIES | Broad Commodities | 16.44 | 17.83 | 0.08454987834549854 | 8 |
| CHINA | China Equities | 53.13 | 56.93 | 0.07152268021833241 | 9 |
| GOLD | Gold | 77.26 | 82.51 | 0.06795236862542064 | 10 |
| COPPER | Copper | 37.99 | 40.18 | 0.05764674914451162 | 11 |
| AUSTRALIA | Australia Equities | 28.45 | 30.05 | 0.05623901581722324 | 12 |
| DIVIDEND | US Dividend Equities | 32.4 | 34.19 | 0.055246913580246915 | 13 |
| AEROSPACE_DEFENSE | Aerospace and Defense | 239.06 | 251.13 | 0.05048941688279096 | 14 |
| CANADA | Canada Equities | 58.65 | 61.5 | 0.04859335038363177 | 15 |
| HEALTHCARE | Healthcare Sector | 160.84 | 168.44 | 0.04725192738124839 | 16 |
| LARGE_VALUE | US Large-Cap Value | 246.84 | 258.30999755859375 | 0.046467337378843565 | 17 |
| ETHEREUM_ETF | Ethereum ETF | 13.529999732971191 | 14.140000343322754 | 0.045085042305289535 | 18 |
| MATERIALS | Materials Sector | 50.89 | 53.18 | 0.044999017488701165 | 19 |
| EUROPE | Europe Equities | 88.57 | 92.26 | 0.04166196228971453 | 20 |
| UNITED_KINGDOM | United Kingdom Equities | 46.6 | 48.49 | 0.04055793991416312 | 21 |
| FINANCIALS | Financials Sector | 55.71 | 57.81 | 0.03769520732364029 | 22 |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 123.99 | 127.89 | 0.0314541495281877 | 23 |
| MEXICO | Mexico Equities | 74.86 | 76.93 | 0.027651616350521158 | 24 |
| EQUAL_WEIGHT_SP500 | Equal-Weight S&P 500 | 214.3 | 220.22 | 0.027624825011665743 | 25 |
| MID_CAP | US Mid-Cap Stocks | 75.67 | 77.54000091552734 | 0.024712579827241177 | 26 |
| TOTAL_US_MARKET | Total US Stock Market | 372.69 | 381.6300048828125 | 0.023987777731660387 | 27 |
| SP500 | S&P 500 | 754.95 | 773.030029296875 | 0.02394864467431601 | 28 |
| DEVELOPED_EX_US | Developed Markets ex-US | 70.99 | 72.5 | 0.021270601493168062 | 29 |
| CONSUMER_DISCRETIONARY | Consumer Discretionary Sector | 117.24 | 119.67 | 0.020726714431934523 | 30 |
| SMALL_VALUE | US Small-Cap Value | 219.97 | 224.29 | 0.019639041687502745 | 31 |
| INDIA | India Equities | 49.3 | 50.14 | 0.017038539553752674 | 32 |
| JAPAN | Japan Equities | 94.55 | 96.05 | 0.015864621893178166 | 33 |
| YEN | Japanese Yen | 56.7400016784668 | 57.62 | 0.015509310812501509 | 34 |
| INDUSTRIALS | Industrials Sector | 181.92 | 184.6 | 0.014731750219876938 | 35 |
| SMALL_CAP | US Small-Cap Stocks | 295.99 | 299.9800109863281 | 0.013480222258617225 | 36 |
| REGIONAL_BANKS | Regional Banks | 75.02 | 76.03 | 0.013463076512929995 | 37 |
| EURO | Euro | 105.21793365478516 | 106.51 | 0.012279906099031068 | 38 |
| CONSUMER_STAPLES | Consumer Staples Sector | 84.12 | 84.95 | 0.00986685687113642 | 39 |
| EMERGING_MARKETS | Emerging Markets | 59.89 | 60.33 | 0.0073468024711971225 | 40 |
| TECHNOLOGY | Technology Sector | 185.78 | 186.32 | 0.002906663795887665 | 41 |
| SHORT_TREASURY | Short-Term Treasury Bills | 91.2276233753 | 91.4800033569336 | 0.002766486424789605 | 42 |
| HIGH_YIELD_CREDIT | High Yield Corporate Bonds | 79.3256352409 | 79.48 | 0.0019459631004683509 | 43 |
| AGRICULTURE | Agriculture Commodities | 27.770000457763672 | 27.82 | 0.0018004876273722825 | 44 |
| LARGE_GROWTH | US Large-Cap Growth | 123.95 | 124.16999816894531 | 0.0017748944650690657 | 45 |
| COMMUNICATIONS | Communication Services Sector | 111.64 | 111.83 | 0.001701898960945858 | 46 |
| BROAD_AI_TECH | Broad AI Technology | 63.44 | 63.51 | 0.0011034047919293855 | 47 |
| LOW_VOL | US Low Volatility Equities | 75.6993756506 | 75.7 | 8.247748341849714e-06 | 48 |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 | 49 |
| BITCOIN_ETF | Bitcoin ETF | 36.22999954223633 | 36.22999954223633 | 0.0 | 49 |
| REAL_ESTATE | Real Estate Sector | 44.45 | 44.4 | -0.0011248593925760053 | 51 |
| INTERNATIONAL_BONDS | International Aggregate Bonds | 47.9611997873 | 47.79 | -0.003569547635573045 | 52 |
| TIPS | Treasury Inflation-Protected Securities | 107.3420774093 | 106.86 | -0.004491038565071048 | 53 |
| MORTGAGE_BACKED_BONDS | Agency Mortgage-Backed Bonds | 93.3762481123 | 92.92 | -0.00488612598517868 | 54 |
| AGGREGATE_BONDS | US Aggregate Bond Market | 97.7407633764 | 97.24 | -0.0051233831116251904 | 55 |
| INTERMEDIATE_TREASURY | Intermediate-Term US Treasury Bonds | 93.3107720067 | 92.76 | -0.005902555459089465 | 56 |
| BIOTECH | Biotechnology | 159.03 | 158.03 | -0.006288121738036834 | 57 |
| NASDAQ100 | Nasdaq 100 | 725.51 | 720.8699951171875 | -0.006395507825960323 | 58 |
| EMERGING_MARKET_BONDS | Emerging Market USD Bonds | 95.5728203523 | 94.84 | -0.007667664819335451 | 59 |
| MUNICIPAL_BONDS | Municipal Bonds | 106.7202532474 | 105.85 | -0.008154527570156445 | 60 |
| US_DOLLAR | US Dollar | 28.389999389648438 | 28.14 | -0.008805896267105706 | 61 |
| INVESTMENT_GRADE_CREDIT | Investment Grade Corporate Bonds | 106.9985951543 | 105.96 | -0.009706624211301862 | 62 |
| BRAZIL | Brazil Equities | 35.93 | 35.19 | -0.020595602560534387 | 63 |
| LONG_TREASURY | Long-Term US Treasury Bonds | 84.1317390232 | 82.06 | -0.024624939972163196 | 64 |
| TAIWAN | Taiwan Equities | 106.19 | 102.18 | -0.0377625011771352 | 65 |
| MOMENTUM | US Momentum Equities | 321.77 | 307.32 | -0.04490785343568382 | 66 |
| UTILITIES | Utilities Sector | 45.41 | 43.13 | -0.05020920502092041 | 67 |
| SOLAR | Solar Energy | 54.96 | 51.86 | -0.05640465793304228 | 68 |
| SEMICONDUCTORS | Semiconductors | 611.03 | 569.41 | -0.06811449519663515 | 69 |
| SOUTH_KOREA | South Korea Equities | 183.52 | 163.12 | -0.11115954664341765 | 70 |

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 35.0 | -0.06811449519663515 | -0.0238400733188223 | AI memory/chip demand outpacing supply, TSMC +30% YoY revenue with Q2 results July 16, blowout SK Hynix ADR debut and Nvidia strength signal continued momentum. |
| anthropic-claude-fable-5 | TAIWAN | 15.0 | -0.0377625011771352 | -0.005664375176570279 | TSMC-heavy exposure into July 16 earnings with strong monthly revenue already disclosed. |
| anthropic-claude-fable-5 | NASDAQ100 | 20.0 | -0.006395507825960323 | -0.0012791015651920645 | Mega-cap tech earnings season within window; diversified AI-cycle exposure with lower single-theme risk than SMH. |
| anthropic-claude-fable-5 | FINANCIALS | 15.0 | 0.03769520732364029 | 0.0056542810985460434 | Big-bank Q2 earnings July 14 with favorable positioning; higher yields supportive; recent relative strength. |
| anthropic-claude-fable-5 | INDUSTRIALS | 15.0 | 0.014731750219876938 | 0.0022097625329815405 | Broadening cyclical strength (+3.15% vs SPY over 30d), diversifier against tech concentration with moderate beta. |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 30.0 | -0.06811449519663515 | -0.020434348558990543 | AI-driven memory/chip demand outpacing supply, Nvidia leadership, TSMC July 16 earnings catalyst with 30% YoY revenue growth. |
| anthropic-claude-opus-4-7 | FINANCIALS | 20.0 | 0.03769520732364029 | 0.007539041464728058 | Big bank earnings July 14 (JPM, WFC, BAC, C, GS) with strong momentum (+7% 30d) and steep yield curve support. |
| anthropic-claude-opus-4-7 | BIOTECH | 15.0 | -0.006288121738036834 | -0.000943218260705525 | Powerful momentum (+23.5% 30d) with high up-day share (75%) suggesting sustained sector rotation. |
| anthropic-claude-opus-4-7 | CYBERSECURITY | 15.0 | 0.09490639965171965 | 0.014235959947757948 | Strong momentum (+10.5% 30d, +6.1% vs SPY) with defensive tech characteristics and AI security tailwind. |
| anthropic-claude-opus-4-7 | TAIWAN | 20.0 | -0.0377625011771352 | -0.00755250023542704 | TSMC Q2 earnings July 16 catalyst, semiconductor supply chain leverage, strong benchmark-relative momentum. |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 30.0 | -0.06811449519663515 | -0.020434348558990543 | AI-driven memory/chip demand outpacing supply, TSMC +30% YTD revenue, Nvidia leadership, SK Hynix strong debut; TSMC Q2 earnings July 16 catalyst within window. |
| anthropic-claude-opus-4-8 | FINANCIALS | 25.0 | 0.03769520732364029 | 0.009423801830910072 | Big-bank Q2 earnings July 14 (JPM, WFC, BAC, C, GS) key catalyst; steepening curve, strong up-day share, positive relative momentum. |
| anthropic-claude-opus-4-8 | INDUSTRIALS | 20.0 | 0.014731750219876938 | 0.002946350043975388 | Strongest recent breadth (70% up-day share, +3.15% relative 30d), cyclical strength with resilient labor and low claims. |
| anthropic-claude-opus-4-8 | TAIWAN | 15.0 | -0.0377625011771352 | -0.005664375176570279 | Semiconductor supply-chain leverage with TSMC earnings catalyst; strong positive relative return and durable AI demand. |
| anthropic-claude-opus-4-8 | CYBERSECURITY | 10.0 | 0.09490639965171965 | 0.009490639965171965 | Best-in-class relative momentum (+6.12% 30d), lower drawdown than broad tech, durable enterprise spend theme. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 40.0 | -0.06811449519663515 | -0.02724579807865406 | Strong AI-related demand and positive catalysts from SK Hynix and TSMC suggest continued momentum in semiconductors. |
| google-gemini-3-1-pro | SOUTH_KOREA | 30.0 | -0.11115954664341765 | -0.03334786399302529 | SK Hynix's successful ADR offering and strong memory-chip pricing provide a positive catalyst for South Korean equities. |
| google-gemini-3-1-pro | TAIWAN | 30.0 | -0.0377625011771352 | -0.011328750353140559 | TSMC's strong monthly revenue growth and upcoming Q2 results provide a positive catalyst for Taiwanese equities. |
| openai-gpt-5-5 | SEMICONDUCTORS | 35.0 | -0.06811449519663515 | -0.0238400733188223 | AI-linked chip demand remains the clearest near-term earnings and sentiment catalyst, with Nvidia strength, memory-price support, and TSMC results due before the exit date. |
| openai-gpt-5-5 | TAIWAN | 20.0 | -0.0377625011771352 | -0.00755250023542704 | Taiwan equities provide concentrated exposure to the semiconductor supply chain and TSMC's upcoming Q2 report, with strong recent relative performance but somewhat less single-theme concentration than SMH. |
| openai-gpt-5-5 | CYBERSECURITY | 20.0 | 0.09490639965171965 | 0.01898127993034393 | Cybersecurity has strong recent benchmark-relative momentum and participates in resilient enterprise technology spending with lower beta than the most aggressive AI hardware exposures. |
| openai-gpt-5-5 | FINANCIALS | 15.0 | 0.03769520732364029 | 0.0056542810985460434 | Major bank earnings arrive early in the window, and a still-high rate environment can support net interest income and capital-markets optimism if credit quality does not deteriorate. |
| openai-gpt-5-5 | BIOTECH | 10.0 | -0.006288121738036834 | -0.0006288121738036834 | Biotech has very strong recent momentum, manageable beta versus other high-upside themes, and can benefit from risk appetite and sector-specific deal or data catalysts. |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 40.0 | -0.06811449519663515 | -0.02724579807865406 | AI-driven memory and foundry demand remains strong, with TSMC results providing a near-term catalyst and sector momentum exceeding the benchmark. |
| openai-gpt-5-6-sol | CYBERSECURITY | 20.0 | 0.09490639965171965 | 0.01898127993034393 | Strong benchmark-relative momentum and comparatively moderate thematic volatility support continued leadership through the earnings window. |
| openai-gpt-5-6-sol | BIOTECH | 20.0 | -0.006288121738036834 | -0.0012576243476073669 | Broad, persistent participation and strong recent relative strength offer diversification from technology while retaining high upside. |
| openai-gpt-5-6-sol | FINANCIALS | 10.0 | 0.03769520732364029 | 0.003769520732364029 | Major-bank earnings are an immediate catalyst, while elevated yields and recent sector breadth may support further outperformance. |
| openai-gpt-5-6-sol | TAIWAN | 10.0 | -0.0377625011771352 | -0.00377625011771352 | Strong semiconductor exposure and TSMC's 30% January-May revenue growth provide a focused earnings catalyst. |
| xai-grok-4-3 | SEMICONDUCTORS | 50.0 | -0.06811449519663515 | -0.034057247598317575 | Strong AI demand evidenced by Nvidia 4% gain, SK Hynix 12.8% surge on memory pricing, and TSMC 30% revenue growth; TSMC Q2 earnings on July 16 provide near-term catalyst. |
| xai-grok-4-3 | TECHNOLOGY | 30.0 | 0.002906663795887665 | 0.0008719991387662995 | Broad tech exposure benefits from same AI supply-chain momentum and recent large-cap tech outperformance lifting the S&P 500. |
| xai-grok-4-3 | CYBERSECURITY | 20.0 | 0.09490639965171965 | 0.01898127993034393 | Recent 10.46% 30-day outperformance and thematic alignment with technology spending trends. |
| xai-grok-4-5 | SEMICONDUCTORS | 40.0 | -0.06811449519663515 | -0.02724579807865406 | AI memory and foundry demand evidenced by SK Hynix pricing/ADR surge and TSMC revenue growth; TSMC Q2 results July 16 as near-term catalyst; high beta and recent relative strength support outperformance vs SPY. |
| xai-grok-4-5 | TAIWAN | 25.0 | -0.0377625011771352 | -0.0094406252942838 | Concentrated semiconductor exposure via TSMC and supply chain; benefits from same AI demand and July 16 earnings catalyst with strong 30d relative return. |
| xai-grok-4-5 | TECHNOLOGY | 20.0 | 0.002906663795887665 | 0.0005813327591775331 | Captures Nvidia-led S&P contribution and broader tech momentum; aligns with AI infrastructure theme while providing liquid large-cap exposure. |
| xai-grok-4-5 | NASDAQ100 | 15.0 | -0.006395507825960323 | -0.0009593261738940484 | Growth/tech heavy index for diversified participation in the same AI and mega-cap drivers lifting markets into the scoring window. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-opus-4-8 | SEMICONDUCTORS | 5 | 0.55 | -0.06811449519663515 | -0.0042379318955033975 | -0.02818657656981941 | 0.16265562771160505 |  | False | False |
| anthropic-claude-opus-4-7 | SEMICONDUCTORS | 5 | 0.55 | -0.06811449519663515 | -0.007155065642637103 | -0.031103710316953113 | 0.16557276145873875 |  | False | False |
| openai-gpt-5-5 | SEMICONDUCTORS | 5 | 0.58 | -0.06811449519663515 | -0.00738582469916305 | -0.031334469373479064 | 0.1658035205152647 |  | False | False |
| openai-gpt-5-6-sol | SEMICONDUCTORS | 5 | 0.61 | -0.06811449519663515 | -0.009528871881266988 | -0.033477516555582995 | 0.16794656769736865 |  | False | False |
| xai-grok-4-3 | SEMICONDUCTORS | 3 | 0.65 | -0.06811449519663515 | -0.014203968529207342 | -0.03815261320352335 | 0.172621664345309 |  | False | False |
| anthropic-claude-fable-5 | SEMICONDUCTORS | 5 | 0.55 | -0.06811449519663515 | -0.02291950642905706 | -0.04686815110337307 | 0.1813372022451587 |  | False | False |
| xai-grok-4-5 | SEMICONDUCTORS | 4 | 0.62 | -0.06811449519663515 | -0.037064416787654375 | -0.061013061461970386 | 0.19548211260375603 |  | False | False |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.7 | -0.06811449519663515 | -0.0719224124248199 | -0.09587105709913592 | 0.23034010824092155 |  | False | False |

## Cost-Adjusted Leaderboard

| model_id | selected_option_id | alpha_vs_sp500 | cost_usd | alpha_per_dollar |
| --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | SEMICONDUCTORS | -0.04686815110337307 | 0.26888 | -0.17430880356803433 |

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | ac62b316a99c218c884c9d791b5a0abd08263141e4887174e9a9d9694d9ddcb8 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | 0e5a222ebba001788946308d0e0b4c71b9e1bdc4f2882aad00ed1514ecaa5c5f |
| manifest.yaml | a82877a1acb064ab2eb5cffcb0a667a1d927418ca2df2cb1e8307ac2286c40bc |
| market_data/universe_trailing_returns.csv | f8f8d04d014410e796c788294b80648e9755eedf519a32cf83f50f9cef39bd71 |
| market_data/universe_trailing_returns.md | f7aa89b335f7950c5dcd6f501a1c519e5837a9dfee44877dad36e6f46f22b1ae |
| market_data/universe_trailing_returns.json | 365e2da3c1184edc48c68b0360a576f1c7aa2d4316d674c95dbf351c124954cb |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | eae9f440179c46fed5ddab1f93cfbd93eef197e61492b7b746b9d49088667a4e | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | e678226937d5a762a5734f20003ca9b9ff70f3df2ec773c6dd6af2276c0255cf | yes |
| Final briefing | research/final_briefing.md | model-facing | ac62b316a99c218c884c9d791b5a0abd08263141e4887174e9a9d9694d9ddcb8 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
