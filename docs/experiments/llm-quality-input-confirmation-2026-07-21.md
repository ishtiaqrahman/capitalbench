# LLM Quality-Input Confirmation

## Purpose

Confirm the unchanged Q2 treatment on periods that were not used to estimate
its development result. Q2 gives each LLM a complete option-level quality
evidence table and requires at least three quality top-ten options in the
ten-name shortlist and two in the final five. The LLM still makes every
forecast and final ranking inside one non-agentic call.

## Frozen Comparison

The treatment is run on D1, D2, and D3: May 24, June 2, and June 9 weekly
rounds. Each Q2 response is paired with the exact valid H4 response previously
saved for the same model and period. The four-model roster is Gemini 3.1 Pro
Preview, Grok 4.3, Grok 4.5, and GPT-5.6 SOL. No provider search or tools are
enabled.

Q2 wording, quality weights, shortlist requirements, response schema, and
scoring are unchanged from the development replay. The only endpoint change is
using the configured Gemini production participant because the separate Flash
free-tier quota was exhausted.

## Frozen Gate

At least ten paired cells must be valid. Mean top-five return must improve by
at least 1.00 percentage point and treatment alpha versus SPY must be positive.
At least eight pairs, all four models, and two of three periods must improve.
The worst period may deteriorate by no more than 0.50 points. Shortlist regret
and top-three capture are reported as diagnostics but are not gates because
the research objective is realized portfolio return.

A pass authorizes only an unchanged prospective private LLM shadow. It does
not change Portfolio V2.0, any frozen round, or official scores.
