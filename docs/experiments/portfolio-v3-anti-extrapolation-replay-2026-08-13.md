# Portfolio V3 Anti-Extrapolation Replay Protocol

## Purpose

This private experiment tests one fixed Portfolio V3 design intended to repair
the two dominant prospective V2.2 failures: incomplete candidate discovery and
poor ranking among considered assets. It does not change production, official
rounds, or published scores.

The design is evaluated unchanged on exactly three non-overlapping weekly
windows. The three windows are the first three non-overlapping resolved V2.2
weeks: July 21-28, July 28-August 4, and August 4-11. Each begins after the
first eligible date of every tested model. Existing official V2.2 responses are
the paired controls, so the experiment requires only 12 new calls.

## Research Basis

The 11 resolved V2.2 weekly rounds available on August 13 contain 44 paired
decisions from the four approved models. The models averaged -1.16 percentage
points of alpha versus SPY. Their ledgers contained a realized top-three asset
in 13/44 cells, their final portfolios contained one in 6/44, and the mean
within-ledger rank correlation between base forecasts and realized returns was
negative. Candidate discovery and ranking therefore need to change together.

Published research also reports that general-purpose LLMs extrapolate recent
stock returns too strongly and are miscalibrated when giving point forecasts.
V3A counters that failure directly instead of adding more unrestricted prose.

## Frozen V3A Treatment

For each entry date, deterministic code constructs one candidate slate from
cutoff-safe data only:

- the five lowest five-session active returns (`shock_reversal`);
- the three highest prior 16-session active returns (`medium_strength`);
- the two highest five-session active returns (`short_continuation`);
- the three highest fixed V2.2 quality-evidence scores (`quality_pullback`);
- the two largest absolute volume dislocations (`volume_dislocation`);
- SPY as the required benchmark.

Duplicates remain one candidate and retain every qualifying lane. The model
must assess every deterministic candidate. It may add at most two wildcards
from the complete universe only when the supplied briefing gives a specific
reason that the mechanical slate missed.

The task removes unconstrained point-estimate portfolio construction. For each
candidate, the model reports:

- probability of beating SPY;
- probability of finishing in the realized top three;
- 10th, 50th, and 90th percentile excess-return estimates;
- a continuation, reversal, catalyst, defensive, or no-edge mechanism;
- an explicit interpretation of whether recent performance is signal or noise.

The prompt states the neutral top-three base rate of roughly 4.3% (3 of 69
active non-cash choices) and prohibits treating recent performance as evidence
by itself. The final three ranked assets receive fixed 35%, 35%, and 30%
weights. This leaves discovery and ranking to the model while preventing
allocation arithmetic from masking those stages.

## Leakage And Call Controls

- `prepare` reads only the round manifest, options, briefing, decision context,
  and V2.2 quality evidence.
- It writes the exact prompts and hashes them with `outcomes_loaded: false`.
- Outcome and official-control files are loaded only by the later `score`
  command.
- Participant calls are single-turn, non-agentic, and receive no tools,
  browsing, retrieval, or follow-up.
- Only GPT-5.6 SOL, Gemini 3.1 Pro, Grok 4.3, and Grok 4.5 are allowed.
- The runner rejects more than three test sets or more than 12 planned calls.
- No Anthropic model or GPT-5.5 is permitted.

## Outbound Data And Cost Ceiling

Each provider receives only the corresponding frozen text packet: public
market facts, cutoff-safe mechanical price features, the allowed asset
universe, and the V3A instructions/schema. The packets are 23.7-25.4 KB. They
contain no credentials, email addresses, local paths, private personal data,
or realized-result files. Provider requests use direct generation endpoints
and do not configure web search, retrieval, code execution, or other tools.

The August 13, 2026 standard text rates are:

- GPT-5.6 SOL: $5/M input tokens and $30/M output tokens;
- Gemini 3.1 Pro Preview below 200K input: $2/M input and $12/M output;
- Grok 4.3: $1.25/M input and $2.50/M output;
- Grok 4.5: $2/M input and $6/M output.

Using a conservative 10,000 billable input tokens and the configured 6,000
output-token maximum for every request, all 12 requests cost no more than
approximately $1.22. The runner permits no transport retry, so the experiment
cannot silently exceed 12 paid requests.

Rate references:

- https://developers.openai.com/api/docs/models/gpt-5.6-sol
- https://ai.google.dev/gemini-api/docs/gemini-3
- https://docs.x.ai/developers/pricing

## Frozen Decision Gate

V3A advances only to a fresh private prospective shadow when all conditions
hold:

- at least 10 of 12 paired responses are valid;
- mean V3A alpha versus SPY is positive;
- mean paired improvement over V2.2 is at least 1.00 percentage point;
- at least 8 paired cells improve;
- at least 3 of 4 models have positive mean alpha;
- at least 2 of 3 periods have positive mean alpha;
- the worst period does not trail its V2.2 control by more than 0.50 point;
- selected top-three capture does not decline.

Passing this replay is not production confirmation. Historical replay can
reject V3A or justify one unchanged prospective shadow. Production adoption
still requires fresh future outcomes.
