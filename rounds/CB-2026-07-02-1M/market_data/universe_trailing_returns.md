# Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-07-02
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-07-02 | 0.00% | 0.00% | 0.00% | 0.00% | 1.69% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-07-02 | 0.12% | 0.35% | 1.77% | 3.87% | 2.04% | 0.24% | 0.00% | 76.19% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-07-02 | 1.43% | -1.69% | 9.60% | 21.37% | 0.00% | 17.82% | -4.49% | 42.86% | -1.69% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-07-02 | 1.60% | -1.21% | 10.31% | 22.11% | 0.48% | 17.54% | -4.36% | 42.86% | -1.21% | 1.02 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-07-02 | -0.53% | -4.39% | 16.50% | 30.00% | -2.70% | 33.84% | -7.03% | 38.10% | -4.39% | 1.36 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-07-02 | 2.59% | -5.47% | 2.91% | 14.86% | -3.78% | 24.18% | -7.86% | 42.86% | -5.83% | 1.24 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-07-02 | 0.98% | 3.45% | 17.12% | 27.73% | 5.15% | 15.30% | -2.40% | 57.14% | 0.00% | 0.74 | pass |
| MID_CAP | IJH | us_size_factor | 2026-07-02 | -0.48% | 1.41% | 14.27% | 21.55% | 3.10% | 16.24% | -2.40% | 57.14% | -1.32% | 1.01 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-07-02 | -0.44% | 2.27% | 20.11% | 36.03% | 3.97% | 21.65% | -3.55% | 57.14% | -0.96% | 1.27 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-07-02 | 0.55% | 3.32% | 21.80% | 37.44% | 5.01% | 17.05% | -2.60% | 52.38% | -0.17% | 1.04 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-07-02 | 1.35% | 0.86% | 18.73% | 22.96% | 2.55% | 12.08% | -2.93% | 47.62% | -0.55% | 0.31 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-07-02 | 2.44% | 7.31% | 8.95% | 7.76% | 9.00% | 14.92% | -1.89% | 66.67% | -0.19% | 0.07 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-07-02 | -6.71% | -2.81% | 25.50% | 34.56% | -1.11% | 49.66% | -8.31% | 52.38% | -8.31% | 1.49 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-07-02 | -2.16% | -8.78% | 25.45% | 43.16% | -7.09% | 43.91% | -10.89% | 42.86% | -8.78% | 1.66 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-07-02 | 3.81% | -3.24% | -5.70% | 3.28% | -1.55% | 19.01% | -6.79% | 47.62% | -8.20% | 0.69 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-07-02 | 3.33% | -0.20% | -0.64% | 7.30% | 1.49% | 23.07% | -4.21% | 57.14% | -5.57% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-07-02 | 1.25% | 4.58% | 10.78% | 6.24% | 6.28% | 17.75% | -3.58% | 52.38% | -4.39% | -0.03 | pass |
| HEALTHCARE | XLV | us_sector | 2026-07-02 | 5.21% | 12.34% | 6.19% | 23.08% | 14.03% | 20.78% | -3.34% | 66.67% | 0.00% | 0.37 | pass |
| FINANCIALS | XLF | us_sector | 2026-07-02 | 4.06% | 8.46% | 2.13% | 7.34% | 10.16% | 15.99% | -1.44% | 61.90% | -0.53% | 0.66 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-07-02 | -0.11% | 5.84% | 17.03% | 25.73% | 7.53% | 23.69% | -3.69% | 61.90% | -0.71% | 0.97 | pass |
| ENERGY | XLE | us_sector | 2026-07-02 | -1.61% | -7.52% | 18.19% | 26.26% | -5.82% | 21.63% | -9.46% | 42.86% | -14.32% | -0.15 | pass |
| MATERIALS | XLB | us_sector | 2026-07-02 | 0.33% | 1.33% | 13.70% | 15.84% | 3.02% | 22.93% | -3.93% | 57.14% | -2.21% | 0.77 | pass |
| UTILITIES | XLU | us_sector | 2026-07-02 | -0.20% | 4.90% | 7.40% | 15.81% | 6.60% | 16.20% | -3.10% | 71.43% | -2.84% | 0.18 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-07-02 | 0.20% | 3.64% | 12.37% | 10.63% | 5.33% | 19.58% | -3.31% | 61.90% | -1.24% | 0.31 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-07-02 | -0.38% | 0.20% | -0.12% | 2.85% | 1.90% | 5.55% | -0.76% | 57.14% | -2.38% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-07-02 | -1.74% | 0.21% | 0.48% | 2.09% | 1.90% | 9.91% | -1.86% | 47.62% | -4.08% | 0.13 | pass |
| TIPS | TIP | bonds_and_rates | 2026-07-02 | -0.10% | -0.53% | 1.24% | 3.28% | 1.16% | 4.57% | -0.97% | 52.38% | -0.66% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-07-02 | -0.44% | 0.09% | 0.86% | 3.94% | 1.79% | 5.43% | -0.79% | 47.62% | -0.92% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-07-02 | 0.25% | 0.22% | 1.78% | 5.23% | 1.92% | 3.81% | -0.59% | 42.86% | 0.00% | 0.23 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-07-02 | -0.31% | 0.23% | 0.73% | 3.97% | 1.93% | 4.31% | -0.55% | 57.14% | -1.13% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-07-02 | -0.49% | -1.57% | 12.82% | 27.48% | 0.12% | 24.53% | -4.85% | 57.14% | -2.18% | 1.07 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-07-02 | 0.41% | -3.40% | 7.61% | 21.66% | -1.70% | 24.17% | -5.67% | 42.86% | -3.59% | 1.07 | pass |
| EUROPE | VGK | international_equity | 2026-07-02 | 1.73% | 1.81% | 7.60% | 18.39% | 3.50% | 18.95% | -2.55% | 57.14% | 0.00% | 0.93 | pass |
| JAPAN | EWJ | international_equity | 2026-07-02 | -0.27% | 0.07% | 15.14% | 30.47% | 1.77% | 27.31% | -5.14% | 66.67% | -3.95% | 1.15 | pass |
| CHINA | MCHI | international_equity | 2026-07-02 | 0.26% | -10.39% | -17.66% | -5.68% | -8.70% | 17.31% | -11.15% | 38.10% | -22.56% | 0.91 | pass |
| INDIA | INDA | international_equity | 2026-07-02 | 0.26% | 3.19% | -9.16% | -10.86% | 4.88% | 15.99% | -1.71% | 57.14% | -11.17% | 0.60 | pass |
| GOLD | IAU | commodities | 2026-07-02 | 2.38% | -8.19% | -4.97% | 22.43% | -6.49% | 30.59% | -11.17% | 47.62% | -23.69% | 0.63 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-07-02 | -1.49% | -11.74% | 19.50% | 23.77% | -10.04% | 16.94% | -12.58% | 28.57% | -16.08% | -0.16 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-07-02 | -7.00% | -6.31% | 58.66% | 111.25% | -4.62% | 71.13% | -11.45% | 52.38% | -11.45% | 2.25 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-07-02 | 10.39% | -10.64% | -8.80% | -13.99% | -8.94% | 34.19% | -19.05% | 33.33% | -20.55% | 1.18 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-07-02 | -3.63% | -11.82% | 20.26% | 42.34% | -10.12% | 50.56% | -12.52% | 47.62% | -11.82% | 1.84 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-07-02 | 3.31% | -9.81% | 8.02% | 46.16% | -8.11% | 45.09% | -12.87% | 33.33% | -11.04% | 2.14 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-07-02 | 8.38% | -3.79% | 28.62% | 22.33% | -2.09% | 29.69% | -11.74% | 38.10% | -3.79% | 1.09 | pass |
| SOLAR | TAN | clean_energy | 2026-07-02 | -2.68% | -22.07% | 9.15% | 52.05% | -20.38% | 50.12% | -22.07% | 33.33% | -23.82% | 1.75 | pass |
| METALS_MINING | XME | commodities | 2026-07-02 | -3.32% | -20.80% | -2.10% | 50.56% | -19.11% | 41.07% | -21.38% | 33.33% | -20.80% | 1.67 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-07-02 | 1.49% | 2.71% | 12.34% | 18.55% | 4.41% | 13.57% | -2.04% | 57.14% | 0.00% | 0.74 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-07-02 | 5.85% | 25.72% | 32.17% | 90.11% | 27.41% | 29.03% | -3.74% | 71.43% | 0.00% | 1.05 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-07-02 | 0.33% | 8.51% | 16.34% | 22.93% | 10.21% | 21.26% | -3.08% | 76.19% | -1.52% | 0.83 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-07-02 | 4.55% | 8.77% | 11.94% | 35.04% | 10.47% | 27.32% | -3.00% | 61.90% | -0.82% | 1.00 | pass |
| CANADA | EWC | country_equity | 2026-07-02 | 0.26% | -2.39% | 7.11% | 26.39% | -0.69% | 14.21% | -3.20% | 57.14% | -2.39% | 0.78 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-07-02 | 2.79% | 1.93% | 7.59% | 23.10% | 3.62% | 17.01% | -2.39% | 42.86% | -1.73% | 0.73 | pass |
| AUSTRALIA | EWA | country_equity | 2026-07-02 | 0.57% | -3.34% | 7.61% | 9.16% | -1.65% | 20.23% | -4.78% | 47.62% | -5.87% | 0.94 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-07-02 | -12.13% | -16.03% | 76.23% | 155.99% | -14.34% | 97.68% | -18.34% | 38.10% | -17.82% | 2.59 | pass |
| TAIWAN | EWT | country_equity | 2026-07-02 | -0.05% | -2.10% | 61.90% | 86.69% | -0.41% | 49.16% | -8.51% | 52.38% | -5.98% | 1.69 | pass |
| BRAZIL | EWZ | country_equity | 2026-07-02 | 0.73% | -2.86% | 7.94% | 24.44% | -1.16% | 21.58% | -5.84% | 38.10% | -16.71% | 0.99 | pass |
| MEXICO | EWW | country_equity | 2026-07-02 | -0.04% | -3.12% | 9.98% | 26.78% | -1.43% | 23.81% | -5.91% | 38.10% | -5.69% | 0.91 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-07-02 | 1.31% | -4.59% | -5.76% | 27.01% | -2.90% | 36.51% | -8.61% | 52.38% | -19.85% | 1.58 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-07-02 | -0.48% | 0.15% | 1.04% | 5.13% | 1.84% | 4.77% | -0.67% | 61.90% | -1.15% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-07-02 | 0.19% | 0.64% | 1.85% | 6.35% | 2.34% | 2.25% | -0.35% | 52.38% | 0.00% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-07-02 | 0.04% | 0.35% | 2.52% | 9.64% | 2.05% | 6.12% | -1.02% | 42.86% | -0.23% | 0.30 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-07-02 | -0.29% | 0.31% | 1.23% | 2.31% | 2.01% | 3.17% | -0.62% | 52.38% | -0.83% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-07-02 | 5.08% | -19.08% | -16.32% | 65.52% | -17.38% | 54.84% | -23.84% | 47.62% | -47.90% | 1.64 | pass |
| COPPER | CPER | commodities | 2026-07-02 | 0.84% | -8.15% | 6.60% | 15.66% | -6.46% | 31.51% | -10.57% | 52.38% | -8.15% | 1.22 | pass |
| AGRICULTURE | DBA | commodities | 2026-07-02 | -0.67% | -1.40% | 4.62% | 7.09% | 0.29% | 10.91% | -3.24% | 38.10% | -6.93% | 0.06 | pass |
| OIL | USO | commodities | 2026-07-02 | -4.88% | -24.25% | 50.78% | 37.56% | -22.56% | 38.93% | -26.69% | 33.33% | -32.02% | -0.98 | pass |
| US_DOLLAR | UUP | currencies | 2026-07-02 | -0.49% | 2.09% | 4.54% | 9.15% | 3.78% | 5.32% | -0.67% | 57.14% | -0.67% | -0.13 | pass |
| EURO | FXE | currencies | 2026-07-02 | 0.57% | -1.60% | -2.06% | -2.45% | 0.09% | 5.90% | -2.32% | 52.38% | -4.71% | 0.12 | pass |
| YEN | FXY | currencies | 2026-07-02 | 0.46% | -0.84% | -2.80% | -11.20% | 0.86% | 4.46% | -1.74% | 23.81% | -11.20% | 0.07 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-07-02 | 4.03% | -8.36% | -31.55% | -44.14% | -6.66% | 45.58% | -12.51% | 38.10% | -51.09% | 1.77 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-07-02 | 9.54% | -10.57% | -45.46% | -34.89% | -8.88% | 73.93% | -18.36% | 38.10% | -64.85% | 2.91 | pass |
