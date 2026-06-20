# CapitalBench Private Eval Sprint - Endpoint Test Procedure

This procedure is used when a customer-hosted endpoint or temporary provider credential is part of the sprint.

## 1. Scope Confirmation

- Confirm endpoint URL or execution channel.
- Confirm authentication method.
- Confirm rate limits and expected latency.
- Confirm that no production customer data, brokerage credentials, or secrets are included in task inputs.

## 2. Non-Scored Validation Call

CapitalBench sends a non-scored validation packet to confirm:

- Connectivity
- Authentication
- Response schema compatibility
- Timeout behavior
- Error handling
- Logging requirements

The validation call does not consume the official run.

## 3. Freeze

After validation, the Evaluation Plan freezes:

- Prompt
- Briefing
- Asset universe
- Response schema
- Portfolio constraints
- Official-run policy
- Consistency-run policy
- Market window
- Price source and fallbacks

## 4. Official Execution

One official response is collected from each system. Invalid and failed responses remain part of the record. Retries are allowed only under the pre-approved policy.

## 5. Post-Execution

- Remove temporary credentials.
- Record credential deletion.
- Preserve audit hashes.
- Preserve run logs and parsed outputs according to the retention policy.
