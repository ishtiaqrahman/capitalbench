# Gemini 4 Argon roster replacement

Operator-directed, forward-only replacement effective 2026-10-14T20:38:28Z.
Gemini 3.1 Pro remains enabled for historical frozen-roster use, with retirement
metadata and successor `google-gemini-4-argon`. The active roster remains seven.
No historical rounds, accepted runs, results, or comparison sets were rewritten.
Argon's first accepted frozen roster starts a new fair comparison origin.

Official API ID: `gemini-4-argon`. Public release: October 13, 2026.
Sources reviewed October 14:

- https://ai.google.dev/gemini-api/docs/models/gemini-4-argon
- https://ai.google.dev/gemini-api/docs/generate-content/latest-model
- https://deepmind.google/models/model-cards/gemini-4-argon/

Use low thinking, the lowest supported level. Omit deprecated temperature.
Retain the benchmark's 6,000-token and 180-second limits despite Google's
general-purpose recommendation to raise limits. Do not introduce long decode,
automatic continuation, tools, search, or an agent loop. This preserves the
benchmark's one-shot contract; API compatibility is not proof that a complete
V3 portfolio decision will succeed within these limits.

A minimal live adapter compatibility check on October 14 returned valid
structured JSON `{"status":"ok"}` with the existing local Google credential.
The request used low thinking, 6,000 maximum tokens, tools disabled, and omitted
temperature. Usage: 209 input tokens, 27 output tokens, 236 total; 2.46 seconds.
This check was not a benchmark submission and did not alter any round.

Verification: 360 tests passed. Five full-suite tests could not access ignored
private historical research files in the clean worktree (feature panel and
stage1b prior records). No push or deployment was performed.
