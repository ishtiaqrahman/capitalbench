# Research Record Protocol

## Purpose

Every return-improvement experiment must remain understandable and
reproducible after the conversation or Codex session that created it ends.

## Required Lifecycle

### 1. Register before calls

Add an `active` entry to `research/registry.yaml` before any paid model call.
The entry must identify the question, frozen design, sample, gates, canonical
protocol/config paths, and the maximum call budget.

### 2. Freeze inputs

Freeze the episode list, treatment text, model roster, model-name overrides,
response schema, primary metrics, stopping rules, and hashes before loading
outcomes into the experiment process. Research reports constructed
retrospectively must be clearly labeled as such and may use only information
published by the episode cutoff.

### 3. Preserve raw execution

Raw packets, responses, and detailed score tables may remain under the ignored
`output/` directory. The runner must record hashes, provider/model names,
timestamps, validation errors, usage, and the frozen configuration so an audit
can connect disposable execution files to the canonical record.

### 4. Promote the result

After scoring, copy a concise report and machine-readable summary to tracked
paths. Update the registry entry with the decision, primary metrics, lessons,
limitations, and exact next action. An experiment is not complete until these
canonical artifacts exist.

### 5. Validate

Run:

```bash
python scripts/validate_research_registry.py
pytest tests/test_research_registry.py
```

The validator rejects duplicate IDs, missing fields, missing canonical
artifacts, and canonical records that point into ignored `output/` paths.

## Minimum Experiment Record

Each registry entry contains:

- stable experiment ID and date;
- status and decision;
- research question and method;
- sample, models, and call count/budget;
- frozen gates or explicit diagnostic-only designation;
- quantitative findings;
- lessons and limitations;
- canonical artifact paths;
- related experiments and next action.

## Evidence Labels

- `active`: frozen or running; no conclusion yet.
- `complete`: execution and canonical report are complete.
- `rejected`: failed a frozen adoption gate.
- `inconclusive`: informative but insufficient for adoption.
- `diagnostic_only`: no adoption claim was allowed by design.
- `accepted`: passed a frozen gate. This still does not alter production unless
  the operator explicitly adopts it.

## Research Separation

Private research must use `official_score_eligible: false` and
`publication_stream: private_research`. It must not alter frozen official
submissions or enter public benchmark calculations. Production adoption and
research evidence are separate decisions and must be recorded separately.
