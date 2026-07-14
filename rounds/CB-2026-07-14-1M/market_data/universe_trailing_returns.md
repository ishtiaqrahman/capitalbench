# Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-07-14
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-07-14 | 0.00% | 0.00% | 0.00% | 0.00% | -1.62% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-07-14 | 0.07% | 0.29% | 1.76% | 3.82% | -1.33% | 0.26% | -0.01% | 73.68% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-07-14 | 0.55% | 1.62% | 9.48% | 21.66% | 0.00% | 12.85% | -3.17% | 42.11% | -0.76% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-07-14 | 0.42% | 1.60% | 9.50% | 22.02% | -0.02% | 12.12% | -2.49% | 42.11% | -0.57% | 1.01 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-07-14 | 1.45% | -0.12% | 16.44% | 30.01% | -1.74% | 26.92% | -4.93% | 47.37% | -3.44% | 1.38 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-07-14 | 1.55% | 1.42% | 5.03% | 15.35% | -0.20% | 22.00% | -5.03% | 47.37% | -4.22% | 1.25 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-07-14 | -0.55% | 2.07% | 13.63% | 27.35% | 0.45% | 11.34% | -1.39% | 57.89% | -0.55% | 0.73 | pass |
| MID_CAP | IJH | us_size_factor | 2026-07-14 | 0.13% | -0.37% | 9.37% | 20.30% | -1.99% | 12.89% | -3.09% | 47.37% | -2.00% | 1.01 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-07-14 | -0.57% | 0.77% | 12.37% | 33.33% | -0.85% | 13.53% | -2.32% | 47.37% | -1.98% | 1.26 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-07-14 | -0.26% | 0.94% | 14.09% | 34.98% | -0.68% | 10.45% | -1.83% | 47.37% | -0.97% | 1.03 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-07-14 | -1.04% | -1.11% | 12.71% | 22.24% | -2.73% | 12.65% | -2.36% | 47.37% | -1.14% | 0.29 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-07-14 | -1.31% | 2.13% | 5.32% | 6.49% | 0.51% | 14.98% | -1.89% | 57.89% | -1.31% | 0.05 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-07-14 | 2.34% | -1.32% | 25.29% | 34.62% | -2.94% | 43.32% | -9.50% | 57.89% | -7.38% | 1.51 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-07-14 | 2.48% | -0.52% | 27.21% | 44.41% | -2.14% | 35.07% | -6.75% | 52.63% | -7.25% | 1.68 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-07-14 | 0.39% | 0.08% | -3.90% | 5.42% | -1.54% | 19.73% | -5.76% | 52.63% | -6.65% | 0.69 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-07-14 | -1.27% | -0.40% | -4.81% | 5.11% | -2.02% | 20.65% | -4.21% | 47.37% | -6.55% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-07-14 | -1.70% | -2.12% | 2.73% | 6.00% | -3.74% | 18.83% | -3.32% | 47.37% | -6.15% | -0.05 | pass |
| HEALTHCARE | XLV | us_sector | 2026-07-14 | -3.74% | 3.37% | 1.13% | 19.27% | 1.75% | 22.29% | -3.74% | 57.89% | -3.74% | 0.34 | pass |
| FINANCIALS | XLF | us_sector | 2026-07-14 | 0.23% | 5.69% | 4.65% | 8.57% | 4.07% | 15.04% | -2.08% | 63.16% | 0.00% | 0.66 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-07-14 | -1.06% | 2.68% | 10.43% | 21.04% | 1.06% | 18.20% | -2.80% | 63.16% | -2.75% | 0.97 | pass |
| ENERGY | XLE | us_sector | 2026-07-14 | 4.23% | -0.33% | 20.13% | 33.24% | -1.95% | 21.91% | -4.25% | 47.37% | -8.31% | -0.19 | pass |
| MATERIALS | XLB | us_sector | 2026-07-14 | -1.69% | -2.59% | 4.73% | 13.31% | -4.21% | 17.96% | -4.50% | 52.63% | -4.78% | 0.77 | pass |
| UTILITIES | XLU | us_sector | 2026-07-14 | -0.02% | 3.26% | 7.26% | 13.47% | 1.64% | 15.71% | -3.10% | 57.89% | -2.99% | 0.16 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-07-14 | -0.91% | -1.08% | 9.14% | 9.95% | -2.70% | 18.39% | -2.75% | 57.89% | -1.68% | 0.30 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-07-14 | -0.16% | -0.34% | -1.16% | 3.10% | -1.96% | 5.31% | -1.54% | 57.89% | -2.98% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-07-14 | -0.56% | -1.61% | -2.65% | 2.69% | -3.23% | 9.41% | -3.62% | 47.37% | -5.68% | 0.13 | pass |
| TIPS | TIP | bonds_and_rates | 2026-07-14 | -0.15% | -0.50% | 0.44% | 3.12% | -2.12% | 4.36% | -0.85% | 52.63% | -0.96% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-07-14 | -0.62% | -1.31% | -1.25% | 3.78% | -2.93% | 4.93% | -2.16% | 52.63% | -2.22% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-07-14 | -0.10% | 0.14% | 1.28% | 5.49% | -1.48% | 2.77% | -0.44% | 36.84% | -0.24% | 0.23 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-07-14 | -0.21% | -0.44% | -0.39% | 3.99% | -2.06% | 4.17% | -1.34% | 57.89% | -1.74% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-07-14 | -0.25% | -0.81% | 9.59% | 27.58% | -2.43% | 18.75% | -3.63% | 57.89% | -2.47% | 1.08 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-07-14 | 0.34% | -0.67% | 5.47% | 22.11% | -2.29% | 20.13% | -4.34% | 47.37% | -3.53% | 1.08 | pass |
| EUROPE | VGK | international_equity | 2026-07-14 | -0.83% | -0.13% | 4.41% | 17.05% | -1.75% | 13.50% | -2.35% | 52.63% | -1.86% | 0.93 | pass |
| JAPAN | EWJ | international_equity | 2026-07-14 | 0.88% | 1.82% | 11.01% | 35.25% | 0.20% | 24.60% | -4.57% | 63.16% | -3.18% | 1.17 | pass |
| CHINA | MCHI | international_equity | 2026-07-14 | 2.80% | -2.27% | -15.68% | -2.36% | -3.89% | 19.93% | -8.10% | 42.11% | -19.04% | 0.92 | pass |
| INDIA | INDA | international_equity | 2026-07-14 | -1.22% | 0.83% | -8.49% | -11.27% | -0.79% | 13.75% | -2.54% | 52.63% | -11.86% | 0.62 | pass |
| GOLD | IAU | commodities | 2026-07-14 | -1.42% | -3.69% | -12.56% | 20.97% | -5.31% | 23.03% | -7.99% | 42.11% | -24.91% | 0.66 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-07-14 | 4.66% | 0.12% | 23.05% | 33.21% | -1.50% | 22.29% | -6.57% | 47.37% | -9.68% | -0.18 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-07-14 | 3.24% | -3.17% | 54.58% | 111.05% | -4.79% | 60.20% | -13.07% | 57.89% | -10.26% | 2.28 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-07-14 | -0.53% | 3.25% | -7.34% | -14.12% | 1.63% | 28.31% | -8.55% | 52.63% | -20.50% | 1.18 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-07-14 | -0.19% | -3.19% | 18.52% | 42.53% | -4.81% | 40.37% | -8.63% | 52.63% | -11.66% | 1.86 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-07-14 | -1.71% | -5.51% | -7.38% | 31.40% | -7.13% | 33.16% | -10.39% | 31.58% | -14.98% | 2.16 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-07-14 | 2.73% | 11.11% | 31.15% | 30.09% | 9.49% | 27.42% | -3.12% | 47.37% | 0.00% | 1.10 | pass |
| SOLAR | TAN | clean_energy | 2026-07-14 | 0.58% | -12.53% | 7.07% | 43.94% | -14.15% | 42.41% | -15.28% | 42.11% | -25.43% | 1.77 | pass |
| METALS_MINING | XME | commodities | 2026-07-14 | 1.90% | -13.24% | -14.97% | 44.37% | -14.86% | 27.21% | -15.44% | 36.84% | -21.33% | 1.69 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-07-14 | -0.60% | 1.24% | 8.31% | 17.54% | -0.38% | 10.89% | -1.83% | 52.63% | -0.72% | 0.73 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-07-14 | -5.14% | 16.30% | 22.70% | 76.91% | 14.68% | 28.48% | -5.44% | 68.42% | -5.37% | 1.02 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-07-14 | -0.09% | 2.76% | 13.28% | 20.79% | 1.14% | 18.66% | -3.73% | 68.42% | -1.55% | 0.83 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-07-14 | -4.01% | 0.70% | -1.49% | 22.12% | -0.92% | 19.81% | -6.27% | 57.89% | -6.18% | 1.02 | pass |
| CANADA | EWC | country_equity | 2026-07-14 | 1.41% | 1.19% | 7.75% | 29.17% | -0.43% | 9.53% | -3.08% | 68.42% | -0.00% | 0.77 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-07-14 | -1.74% | -0.40% | 3.74% | 19.61% | -2.02% | 14.36% | -2.28% | 36.84% | -3.51% | 0.72 | pass |
| AUSTRALIA | EWA | country_equity | 2026-07-14 | 2.06% | -0.36% | 9.70% | 12.21% | -1.98% | 14.26% | -4.42% | 52.63% | -3.79% | 0.93 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-07-14 | -2.38% | -10.37% | 61.42% | 147.21% | -11.99% | 80.19% | -23.35% | 47.37% | -19.26% | 2.65 | pass |
| TAIWAN | EWT | country_equity | 2026-07-14 | 0.00% | -0.72% | 53.18% | 84.33% | -2.34% | 44.76% | -8.65% | 52.63% | -8.65% | 1.71 | pass |
| BRAZIL | EWZ | country_equity | 2026-07-14 | 4.01% | 3.63% | 9.69% | 37.85% | 2.01% | 19.96% | -2.63% | 42.11% | -12.84% | 1.01 | pass |
| MEXICO | EWW | country_equity | 2026-07-14 | 0.40% | -2.58% | 4.18% | 30.71% | -4.20% | 18.78% | -5.37% | 42.11% | -5.89% | 0.92 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-07-14 | -0.22% | -3.04% | -11.65% | 29.06% | -4.66% | 23.32% | -8.61% | 47.37% | -20.54% | 1.58 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-07-14 | -0.18% | -0.40% | -0.18% | 5.42% | -2.02% | 4.88% | -1.45% | 57.89% | -1.63% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-07-14 | -0.27% | 0.18% | 0.83% | 6.35% | -1.44% | 2.48% | -0.62% | 57.89% | -0.58% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-07-14 | -0.39% | -0.41% | 1.79% | 9.59% | -2.03% | 4.69% | -1.08% | 42.11% | -0.88% | 0.29 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-07-14 | -0.12% | -0.39% | 0.02% | 2.09% | -2.01% | 3.53% | -1.20% | 47.37% | -1.40% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-07-14 | -2.37% | -13.25% | -37.12% | 53.54% | -14.87% | 45.15% | -18.42% | 42.11% | -49.65% | 1.69 | pass |
| COPPER | CPER | commodities | 2026-07-14 | 3.08% | -2.55% | 2.77% | 12.43% | -4.17% | 25.41% | -8.42% | 47.37% | -5.07% | 1.23 | pass |
| AGRICULTURE | DBA | commodities | 2026-07-14 | 0.29% | 5.30% | 8.31% | 10.61% | 3.68% | 14.33% | -1.52% | 57.89% | -3.83% | 0.07 | pass |
| OIL | USO | commodities | 2026-07-14 | 10.33% | -4.19% | 65.50% | 58.91% | -5.81% | 51.85% | -14.80% | 47.37% | -21.44% | -1.03 | pass |
| US_DOLLAR | UUP | currencies | 2026-07-14 | -0.04% | 1.57% | 3.88% | 7.58% | -0.05% | 5.34% | -0.74% | 52.63% | -0.49% | -0.13 | pass |
| EURO | FXE | currencies | 2026-07-14 | 0.08% | -1.28% | -1.54% | -1.42% | -2.90% | 5.56% | -2.19% | 42.11% | -4.78% | 0.13 | pass |
| YEN | FXY | currencies | 2026-07-14 | -0.11% | -1.21% | -2.43% | -9.23% | -2.83% | 5.53% | -1.42% | 36.84% | -9.99% | 0.07 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-07-14 | 1.19% | 1.50% | -34.02% | -46.35% | -0.12% | 39.45% | -11.79% | 52.63% | -48.69% | 1.81 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-07-14 | 4.96% | 12.81% | -44.59% | -37.67% | 11.19% | 52.65% | -14.68% | 47.37% | -61.25% | 2.96 | pass |
