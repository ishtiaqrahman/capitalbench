# October 19, 2026 production rounds

Fresh research was prepared by direct public-source browsing, not participant
model APIs. Source ledger, factual briefing, audit, and research hashes are
published in each round's research directory. Research cutoff: 05:33:04 UTC
(01:33:04 America/Toronto), October 19.

| Round | Accepted run | Valid | Call window UTC | Exit close |
| --- | --- | --- | --- | --- |
| CB-2026-10-19-1W | official-20261019-1W | 6/6 | 05:34:30–05:38:31 | October 26 |
| CB-2026-10-19-1M | official-20261019-1M | 6/6 | 05:34:31–05:38:48 | November 19 |

All twelve first-attempt decisions were valid. No technical, formatting, or
outcome-based retries were performed. The frozen six-model roster comprises
GPT-6 Astra, Opus 5.5, Fable 5.1, Gemini 4 Argon, Grok 4.5, and Grok 4.6.
This is Argon's first official roster; no historical backfill was performed.
Retired Gemini 3.1 and Grok 4.3 remain in historical data.

Both rounds use production V3, one tool-free decision per participant, lowest
configured reasoning, and deterministic 35/35/30 allocation with SPY fallback.
Their complete 70-option mechanical profiles use October 16 histories, with
100% Q1 coverage and no failed options. Tiingo returned HTTP 429 during fresh
validation; the unchanged ticker universe retains cached prior Tiingo validation.
Fresh full histories and volume came from the existing Yahoo mechanical-data
pipeline. This limitation is disclosed in both audit reports and in
`universe_validation_cached_evidence.json`.

Entry is the prospective October 19 close, not the previously observed Friday
close. At acceptance neither entry nor exit prices are yet available. The
full-round audit therefore reports missing entry/exit price files; every input,
hash, guardrail, submission, and private raw-response-preservation check passes.
Do not interpret these pending rounds as scored results. Entry/day-zero data is
populated by the normal post-close pipeline, and final resolution is scheduled
for October 26 and November 19 at 23:30 UTC, respectively.

Both accepted pending rounds and resolution jobs were synced using local
production credentials. Exact raw provider text remains private on disk;
normalized judgments, parsed portfolios, sanitized logs, and response hashes
are public. Public research contains no credentials.
