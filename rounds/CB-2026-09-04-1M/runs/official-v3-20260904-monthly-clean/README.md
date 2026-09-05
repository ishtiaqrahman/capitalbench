# CB-2026-09-04-1M collection recovery

Clean official run assembled after the operator agent crashed during collection. Every saved valid original decision is reused byte-for-byte; only models with no saved response were called in the recovery source run. Calls potentially in flight at the crash have no recoverable response and are disclosed as infrastructure recovery. All decisions use the unchanged frozen prompt and precede the decision deadline. Source runs remain ineligible; no best-of-many selection or portfolio edits occurred. The original buffered run log was empty; reconstructed records preserve saved usage and response hashes, with unavailable original call timestamps explicitly null.

The per-model source IDs and artifact hashes are recorded in `recovery_provenance.json`. Raw provider response text remains private under the repository publication policy.
