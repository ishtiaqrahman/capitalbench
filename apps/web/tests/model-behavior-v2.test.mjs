import assert from "node:assert/strict";
import test from "node:test";
import apiReadModel from "../src/generated/apiReadModel.js";
import {
  BEHAVIOR_SIGNAL_RULES,
  MODEL_BEHAVIOR_METHOD_VERSION,
  MODEL_BEHAVIOR_VERSION,
  buildModelBehaviorV2
} from "../scripts/lib/model-behavior-v2.mjs";

const MODEL_IDS = ["model-a", "model-b", "model-c"];

function profile(modelId, overrides = {}) {
  return {
    model_id: modelId,
    label: modelId,
    sample: { portfolio_count: 8, resolved_round_count: 0 },
    metrics: {
      average_risk_pulse: 60,
      average_holding_count: 5,
      average_top_allocation_pct: 20,
      defensive_pct: 10,
      tech_pct: 10,
      cash_duration_pct: 0,
      international_pct: 0,
      real_assets_pct: 10,
      benchmark_pct: 20
    },
    peer: { average_peer_similarity: 0.5, similarity_observation_count: 8, outlier_round_count: 0 },
    turnover: { average_turnover_pct: 40, turnover_observation_count: 0 },
    performance: {},
    recent: { active_portfolio_count: 0, current_top_assets: [], top_assets: [] },
    peer_percentiles: {
      risk_pulse: 50,
      concentration: 50,
      defensiveness: 50,
      peer_similarity: 50,
      turnover_stability: 50,
      capitalbench_score: null
    },
    ...overrides
  };
}

function scoredRow({ modelId, index, track = "weekly", realAssets = 10, risk = 60, methodology = "portfolio-v2.2", ...overrides }) {
  const date = `2026-01-${String(index + 1).padStart(2, "0")}`;
  return {
    key: `${index}:${modelId}`,
    round_id: `CB-TEST-${index}-${track}`,
    run_id: `run-${index}-${track}`,
    model_id: modelId,
    track,
    status: "resolved",
    entry_date: date,
    decision_date: date,
    methodology_version: methodology,
    chronology: `${date}:${track}`,
    risk_pulse: risk,
    tech_pct: 10,
    real_assets_pct: realAssets,
    international_pct: 0,
    defensive_pct: 10,
    cash_duration_pct: 0,
    benchmark_pct: 20,
    top_allocation_pct: 20,
    holding_count: 5,
    candidate_count: null,
    selected_candidate_count: null,
    candidate_includes_sp500: null,
    average_candidate_forecast_range_pct: null,
    expected_alpha_vs_sp500_pct: null,
    submission_confidence: null,
    key_risk_count: null,
    allocations: [],
    ...overrides
  };
}

function buildFixture(rowFactory, profileOverrides = new Map(), modelOverrides = new Map()) {
  const rows = [];
  for (let index = 0; index < 8; index += 1) {
    for (const modelId of MODEL_IDS) rows.push(rowFactory({ modelId, index }));
  }
  return buildModelBehaviorV2({
    profiles: MODEL_IDS.map((modelId) => profile(modelId, profileOverrides.get(modelId))),
    scoredRows: rows,
    models: MODEL_IDS.map((modelId) => ({
      model_id: modelId,
      lifecycle_status: modelOverrides.get(modelId)?.lifecycle_status ?? "active"
    }))
  });
}

test("behavior v2 ignores a market-wide exposure shift", () => {
  const profiles = buildFixture(({ modelId, index }) =>
    scoredRow({ modelId, index, realAssets: index < 4 ? 10 : 40 })
  );
  const model = profiles.find((row) => row.model_id === "model-a");
  assert.equal(model.behavior_v2.primary_signal_key, null);
  assert.equal(model.archetype.label, "Peer-balanced allocator");
  assert.equal(model.behavior_v2.signals.real_assets.overall.median_delta, 0);
});

test("behavior v2 identifies a persistent peer-relative real-asset signature", () => {
  const profiles = buildFixture(({ modelId, index }) =>
    scoredRow({ modelId, index, realAssets: modelId === "model-a" ? 40 : 10 })
  );
  const model = profiles.find((row) => row.model_id === "model-a");
  assert.equal(model.behavior_v2.primary_signal_key, "real_assets");
  assert.match(model.archetype.label, /^Real-asset /);
  assert.equal(model.behavior_v2.signals.real_assets.overall.median_delta, 30);
  assert.equal(model.behavior_v2.signals.real_assets.overall.positive_rate_pct, 100);
  assert.match(model.behavior_v2.pills[0].label, /Real assets 40% · \+30pp vs peers/);
});

test("risk-score deltas use score points rather than percentage points", () => {
  const profiles = buildFixture(({ modelId, index }) =>
    scoredRow({ modelId, index, risk: modelId === "model-a" ? 75 : 60 })
  );
  const model = profiles.find((row) => row.model_id === "model-a");
  assert.match(model.behavior_v2.pills[0].label, /\+15 pts vs peers/);
  assert.match(model.behavior_v2.pills[0].evidence, /15\.0 points above same-round peers/);
});

test("one extreme portfolio cannot create a persistent signature", () => {
  const profiles = buildFixture(({ modelId, index }) =>
    scoredRow({ modelId, index, realAssets: modelId === "model-a" && index === 7 ? 100 : 10 })
  );
  const model = profiles.find((row) => row.model_id === "model-a");
  assert.equal(model.behavior_v2.primary_signal_key, null);
  assert.equal(model.behavior_v2.signals.real_assets.high_qualified, false);
});

test("opposite weekly and monthly signals are disclosed as horizon-dependent", () => {
  const rows = [];
  for (let index = 0; index < 8; index += 1) {
    const track = index < 4 ? "weekly" : "monthly";
    for (const modelId of MODEL_IDS) {
      rows.push(
        scoredRow({
          modelId,
          index,
          track,
          realAssets: modelId === "model-a" ? (track === "weekly" ? 50 : 10) : 30
        })
      );
    }
  }
  const profiles = buildModelBehaviorV2({
    profiles: MODEL_IDS.map((modelId) => profile(modelId)),
    scoredRows: rows,
    models: MODEL_IDS.map((modelId) => ({ model_id: modelId, lifecycle_status: "active" }))
  });
  const model = profiles.find((row) => row.model_id === "model-a");
  assert.equal(model.behavior_v2.signals.real_assets.track_conflict, true);
  assert.equal(model.archetype.confidence_label, "Horizon-dependent");
  assert.equal(model.archetype.label, "Horizon-dependent allocator");
});

test("a sufficiently sampled current-method reversal is disclosed as evolving", () => {
  const rows = [];
  for (let index = 0; index < 16; index += 1) {
    const currentMethod = index >= 8;
    for (const modelId of MODEL_IDS) {
      rows.push(
        scoredRow({
          modelId,
          index,
          methodology: currentMethod ? "portfolio-v2.2" : "portfolio-v2.0",
          realAssets: modelId === "model-a" ? (currentMethod ? 10 : 40) : currentMethod ? 30 : 10
        })
      );
    }
  }
  const profiles = buildModelBehaviorV2({
    profiles: MODEL_IDS.map((modelId) => profile(modelId, { sample: { portfolio_count: 16, resolved_round_count: 0 } })),
    scoredRows: rows,
    models: MODEL_IDS.map((modelId) => ({ model_id: modelId, lifecycle_status: "active" }))
  });
  const model = profiles.find((row) => row.model_id === "model-a");
  assert.equal(model.behavior_v2.signals.real_assets.methodology_conflict, true);
  assert.equal(model.archetype.confidence_label, "Evolving pattern");
  assert.match(model.archetype.confidence_reason, /reverses under the current methodology/);
});

test("a small current-method sample cannot create a reversal caveat", () => {
  const rows = [];
  for (let index = 0; index < 12; index += 1) {
    const currentMethod = index >= 8;
    for (const modelId of MODEL_IDS) {
      rows.push(
        scoredRow({
          modelId,
          index,
          methodology: currentMethod ? "portfolio-v2.2" : "portfolio-v2.0",
          realAssets: modelId === "model-a" ? (currentMethod ? 10 : 40) : currentMethod ? 30 : 10
        })
      );
    }
  }
  const profiles = buildModelBehaviorV2({
    profiles: MODEL_IDS.map((modelId) => profile(modelId, { sample: { portfolio_count: 12, resolved_round_count: 0 } })),
    scoredRows: rows,
    models: MODEL_IDS.map((modelId) => ({ model_id: modelId, lifecycle_status: "active" }))
  });
  const model = profiles.find((row) => row.model_id === "model-a");
  assert.equal(model.behavior_v2.signals.real_assets.methodology_conflict, false);
  assert.notEqual(model.archetype.confidence_label, "Evolving pattern");
});

test("performance changes cannot alter an allocation-style profile", () => {
  const rows = [];
  for (let index = 0; index < 8; index += 1) {
    for (const modelId of MODEL_IDS) {
      rows.push(scoredRow({ modelId, index, realAssets: modelId === "model-a" ? 40 : 10 }));
    }
  }
  const base = MODEL_IDS.map((modelId) => profile(modelId));
  const changed = base.map((row) => ({
    ...row,
    performance: { average_return_pct: row.model_id === "model-a" ? -99 : 99, win_count: 100, last_count: 100 }
  }));
  const models = MODEL_IDS.map((modelId) => ({ model_id: modelId, lifecycle_status: "active" }));
  const before = buildModelBehaviorV2({ profiles: base, scoredRows: rows, models });
  const after = buildModelBehaviorV2({ profiles: changed, scoredRows: rows, models });
  assert.deepEqual(
    before.map((row) => ({ model_id: row.model_id, archetype: row.archetype, pills: row.behavior_v2.pills })),
    after.map((row) => ({ model_id: row.model_id, archetype: row.archetype, pills: row.behavior_v2.pills }))
  );
});

test("too few independent decision dates remains provisional", () => {
  const rows = [];
  for (let index = 0; index < 8; index += 1) {
    for (const modelId of MODEL_IDS) {
      rows.push(
        scoredRow({
          modelId,
          index,
          realAssets: modelId === "model-a" ? 40 : 10,
          decision_date: `2026-01-${String((index % 4) + 1).padStart(2, "0")}`
        })
      );
    }
  }
  const profiles = buildModelBehaviorV2({
    profiles: MODEL_IDS.map((modelId) => profile(modelId)),
    scoredRows: rows,
    models: MODEL_IDS.map((modelId) => ({ model_id: modelId, lifecycle_status: "active" }))
  });
  const model = profiles.find((row) => row.model_id === "model-a");
  assert.equal(model.archetype.label, "Emerging allocation profile");
  assert.equal(model.archetype.confidence_label, "Provisional");
});

test("too few peer-matched portfolios remains provisional even with enough dates", () => {
  const rows = [];
  for (let index = 0; index < 8; index += 1) {
    rows.push(scoredRow({ modelId: "model-a", index, realAssets: 40 }));
    if (index < 7) {
      rows.push(scoredRow({ modelId: "model-b", index, realAssets: 10 }));
      rows.push(scoredRow({ modelId: "model-c", index, realAssets: 10 }));
    }
  }
  const profiles = buildModelBehaviorV2({
    profiles: MODEL_IDS.map((modelId) => profile(modelId)),
    scoredRows: rows,
    models: MODEL_IDS.map((modelId) => ({ model_id: modelId, lifecycle_status: "active" }))
  });
  const model = profiles.find((row) => row.model_id === "model-a");
  assert.equal(model.archetype.confidence_label, "Provisional");
  assert.match(model.archetype.confidence_reason, /Only 7 peer-matched portfolios/);
});

test("fixed-role pills and structured decision coverage are auditable", () => {
  const profiles = buildFixture(({ modelId, index }) =>
    scoredRow({
      modelId,
      index,
      realAssets: modelId === "model-a" ? 40 : 10,
      candidate_count: 8,
      selected_candidate_count: 5,
      candidate_includes_sp500: true,
      average_candidate_forecast_range_pct: 4,
      expected_alpha_vs_sp500_pct: 0.5,
      submission_confidence: 0.6,
      key_risk_count: 4
    })
  );
  const model = profiles.find((row) => row.model_id === "model-a");
  assert.deepEqual(model.behavior_v2.pills.map((pill) => pill.role), ["Signature", "Construction", "Tempo", "Now"]);
  assert.equal(model.behavior_v2.decision_process.structured_candidate_coverage_pct, 100);
  assert.equal(model.behavior_v2.decision_process.average_candidate_count, 8);
  assert.equal(model.behavior_v2.decision_process.sp500_candidate_inclusion_rate_pct, 100);
  assert.equal(model.behavior_v2.decision_process.candidate_forecast_coverage_count, 8);
  assert.equal(model.behavior_v2.decision_process.submission_confidence_coverage_count, 8);
  assert.equal(model.behavior_v2.decision_process.key_risk_coverage_count, 8);
});

test("construction evidence names the metric that actually supplied the style", () => {
  const profileOverrides = new Map([
    [
      "model-a",
      {
        peer: { average_peer_similarity: 0.3, similarity_observation_count: 8, outlier_round_count: 0 },
        peer_percentiles: {
          risk_pulse: 50,
          concentration: 50,
          defensiveness: 50,
          peer_similarity: 0,
          turnover_stability: 50,
          capitalbench_score: null
        }
      }
    ]
  ]);
  const profiles = buildFixture(({ modelId, index }) => scoredRow({ modelId, index }), profileOverrides);
  const model = profiles.find((row) => row.model_id === "model-a");
  assert.equal(model.behavior_v2.construction_signal_key, "distinctive");
  assert.match(model.behavior_v2.pills[1].evidence, /average cosine overlap/);
  assert.doesNotMatch(model.behavior_v2.pills[1].evidence, /based on peer-normalized holding count/);
});

test("an active model without an open portfolio does not receive a stale Now claim", () => {
  const profileOverrides = new Map([
    [
      "model-a",
      {
        recent: {
          active_portfolio_count: 0,
          current_top_assets: [],
          top_assets: [{ label: "Historical Energy", ticker: "XLE", average_allocation_pct: 25 }]
        }
      }
    ]
  ]);
  const profiles = buildFixture(({ modelId, index }) => scoredRow({ modelId, index }), profileOverrides);
  const model = profiles.find((row) => row.model_id === "model-a");
  assert.equal(model.behavior_v2.pills[3].role, "Now");
  assert.equal(model.behavior_v2.pills[3].label, "No open portfolio");
  assert.doesNotMatch(model.behavior_v2.pills[3].evidence, /Historical Energy/);
});

test("retired models receive a lifecycle pill instead of a current-style claim", () => {
  const modelOverrides = new Map([["model-a", { lifecycle_status: "retired" }]]);
  const profileOverrides = new Map([
    [
      "model-a",
      {
        recent: {
          active_portfolio_count: 0,
          current_top_assets: [],
          top_assets: [{ label: "Energy Sector", ticker: "XLE", average_allocation_pct: 25 }]
        }
      }
    ]
  ]);
  const profiles = buildFixture(
    ({ modelId, index }) => scoredRow({ modelId, index }),
    profileOverrides,
    modelOverrides
  );
  const model = profiles.find((row) => row.model_id === "model-a");
  assert.equal(model.behavior_v2.pills[3].role, "Lifecycle");
  assert.equal(model.behavior_v2.pills[3].label, "Historical · retired");
});

test("generated production profiles publish v2, retain v1 shadow, and exclude retired models from active leaders", () => {
  assert.equal(apiReadModel.model_behavior.version, MODEL_BEHAVIOR_VERSION);
  assert.equal(apiReadModel.model_behavior.method_version, MODEL_BEHAVIOR_METHOD_VERSION);
  assert.equal(apiReadModel.model_behavior.shadow_v1.version, "model_behavior_v1");
  assert.equal(apiReadModel.model_behavior.pattern_report.version, "model_behavior_pattern_report_v2");
  assert.equal(apiReadModel.model_behavior.methodology.rules.persistence_rate_pct, BEHAVIOR_SIGNAL_RULES.persistence_rate_pct);

  const retiredIds = new Set(apiReadModel.models.filter((model) => model.lifecycle_status === "retired").map((model) => model.model_id));
  for (const [key, modelId] of Object.entries(apiReadModel.model_behavior.summary)) {
    if (key.endsWith("_model_id") && modelId) assert.equal(retiredIds.has(modelId), false, `${key} must use the active cohort`);
  }
  for (const profileRow of apiReadModel.model_behavior.profiles) {
    assert.equal(profileRow.behavior_v2.pills.length, 4);
    assert.ok(profileRow.archetype.description.length > 40);
  }
});
