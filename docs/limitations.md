# Limitations

CapitalBench is intentionally narrow in this version.

- It is not financial advice.
- It calls live model APIs only when explicitly allowed by the operator.
- It fetches Tiingo EOD data only when the operator explicitly runs a price or performance command.
- It depends on operator-supplied price files.
- Universe validation depends on Tiingo EOD availability for each non-cash ticker.
- Tiingo validation confirms data availability, not investment suitability.
- It supports one selected option, not portfolios.
- It does not model taxes, transaction costs, slippage, liquidity, or dividends.
- It does not verify that a manually entered submission truly came from a named model.
- It measures one prompt and one option set at a time.
- It allows models to use internal learned knowledge and general market priors, so rationales may include model-internal associations that were not explicitly stated in the briefing.
- It relies on the operator to keep audit-only research material out of the final model-facing briefing.
- The import command catches obvious recommendation, ranking, and subjective-analysis language but cannot prove a briefing is fully neutral.
- Full-universe trailing returns are historical price facts, not forecasts. They may still influence model behavior through momentum or reversal patterns.
- A one-month result can be dominated by noise.
- Newer models may have fewer resolved rounds in cumulative leaderboards.
- Old rounds are not rerun for new models because outcomes may already be knowable.
- The official one-shot result can differ from a model's repeated-call behavior.
- A round where many models choose the same asset may be fair but low-discrimination as a ranking event.
- Multi-run stability analysis measures consistency, not a separate investment skill score.
- Stability results must not be combined with the official leaderboard into one headline number.
- Providers expose different reasoning or thinking controls, and some models require hidden reasoning tokens. CapitalBench records reported token usage where available but does not treat hidden reasoning tokens as directly comparable.
- A format retry can be necessary when a provider returns malformed or truncated structured output. Such retries must be disclosed and must not be used to change an otherwise valid asset choice.
- The v1.5 universe is a fixed ETF universe and does not cover every investable asset.

The framework is useful for reproducible comparisons, but it should not be read
as proof that a model has durable investing skill.
