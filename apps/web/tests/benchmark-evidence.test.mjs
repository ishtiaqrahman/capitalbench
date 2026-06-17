import assert from "node:assert/strict";
import test from "node:test";
import { buildBenchmarkEvidence } from "../src/lib/benchmarkEvidence.js";

function dateFor(index) {
  return `2026-06-${String(index).padStart(2, "0")}`;
}

function makeRound({ id, track, index, submissionFormat = "portfolio" }) {
  return {
    round_id: id,
    track,
    status: "resolved",
    decision_deadline_utc: `${dateFor(index)}T21:00:00Z`,
    decision_date: dateFor(index),
    entry_date: dateFor(index),
    exit_date: dateFor(index + 7),
    submission_format: submissionFormat,
    official_run_id: "official"
  };
}

function makeResult(round, modelId, rank) {
  return {
    round_id: round.round_id,
    run_id: round.official_run_id,
    track: round.track,
    model_id: modelId,
    provider: modelId === "m1" ? "openai" : "anthropic",
    rank,
    portfolio_return_pct: rank === 1 ? 1.2 : 0.7,
    benchmark_return_pct: 0.6,
    max_possible_return_pct: 2.4,
    capitalbench_score: rank === 1 ? 50 : 29.1666666667,
    submission_format: round.submission_format
  };
}

function makeReturn(round, optionId, returnPct, flags = {}) {
  return {
    round_id: round.round_id,
    run_id: round.official_run_id,
    track: round.track,
    option_id: optionId,
    label: optionId,
    return_pct: returnPct,
    is_benchmark: Boolean(flags.is_benchmark),
    is_cash: Boolean(flags.is_cash)
  };
}

function syntheticReadModel({ weeklyCount = 9, monthlyCount = 1 } = {}) {
  const weeklyRounds = Array.from({ length: weeklyCount }, (_, index) =>
    makeRound({
      id: `W-${index + 1}`,
      track: "weekly",
      index: index + 1,
      submissionFormat: index === 0 ? "single_pick" : "portfolio"
    })
  );
  const monthlyRounds = Array.from({ length: monthlyCount }, (_, index) =>
    makeRound({
      id: `M-${index + 1}`,
      track: "monthly",
      index: index + 1,
      submissionFormat: "single_pick"
    })
  );
  const rounds = [...weeklyRounds, ...monthlyRounds];
  const results = rounds.flatMap((round) => [makeResult(round, "m1", 1), makeResult(round, "m2", 2)]);
  const returns = rounds.flatMap((round) => [
    makeReturn(round, "SP500", 0.6, { is_benchmark: true }),
    makeReturn(round, "CASH", 0, { is_cash: true }),
    makeReturn(round, "ORACLE_ASSET", 2.4)
  ]);

  return {
    generated_at: "2026-06-17T12:00:00Z",
    benchmark_set_policy: {
      version: "benchmark_sets_v1",
      qualification_thresholds: {
        weekly: 6,
        monthly: 3
      }
    },
    benchmark_set_definitions: [
      {
        set_id: "weekly-set",
        track: "weekly",
        label: "Weekly Set",
        short_label: "Weekly Set",
        started_round_id: "W-1",
        model_ids: ["m1", "m2"]
      },
      {
        set_id: "monthly-set",
        track: "monthly",
        label: "Monthly Set",
        short_label: "Monthly Set",
        started_round_id: "M-1",
        model_ids: ["m1", "m2"]
      }
    ],
    rounds,
    models: [
      { model_id: "m1", label: "Model One", provider: "openai", provider_label: "OpenAI" },
      { model_id: "m2", label: "Model Two", provider: "anthropic", provider_label: "Anthropic" }
    ],
    results,
    returns,
    insights: {
      insights: [
        {
          category: "consensus_performance",
          status: "published",
          context: {
            track: "weekly"
          }
        }
      ]
    }
  };
}

test("benchmark evidence summarizes maturity, protocols, equal-run sets, and baselines", () => {
  const evidence = buildBenchmarkEvidence(syntheticReadModel());

  assert.equal(evidence.version, "benchmark_evidence_v1");
  assert.equal(evidence.tracks.weekly.resolved_round_count, 9);
  assert.equal(evidence.tracks.weekly.resolved_model_result_count, 18);
  assert.equal(evidence.tracks.weekly.sample_maturity.key, "qualified_forming");
  assert.equal(evidence.tracks.weekly.protocol_mix.key, "mixed");
  assert.equal(evidence.tracks.weekly.equal_run_comparison.current_set_id, "weekly-set");
  assert.equal(evidence.tracks.weekly.equal_run_comparison.shared_round_count, 9);
  assert.equal(evidence.tracks.weekly.baselines.find((baseline) => baseline.key === "ai_consensus").available, true);

  assert.equal(evidence.tracks.monthly.resolved_round_count, 1);
  assert.equal(evidence.tracks.monthly.sample_maturity.key, "early");
  assert.equal(evidence.tracks.monthly.protocol_mix.key, "single_pick_only");
  assert.equal(evidence.tracks.monthly.equal_run_comparison.is_qualified, false);
  assert.equal(evidence.tracks.monthly.baselines.find((baseline) => baseline.key === "ai_consensus").available, false);
});

test("benchmark evidence handles empty public result data without crashing", () => {
  const evidence = buildBenchmarkEvidence({
    generated_at: "2026-06-17T12:00:00Z",
    benchmark_set_policy: {
      qualification_thresholds: {
        weekly: 6,
        monthly: 3
      }
    },
    benchmark_set_definitions: [],
    rounds: [],
    models: [],
    results: [],
    returns: [],
    insights: { insights: [] }
  });

  assert.equal(evidence.tracks.weekly.resolved_round_count, 0);
  assert.equal(evidence.tracks.weekly.sample_maturity.key, "early");
  assert.equal(evidence.tracks.weekly.protocol_mix.key, "none");
  assert.equal(evidence.tracks.weekly.equal_run_comparison.available, false);
  assert.equal(evidence.tracks.weekly.baselines.every((baseline) => baseline.available === false), true);
});
