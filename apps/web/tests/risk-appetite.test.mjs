import assert from "node:assert/strict";
import { readdirSync, readFileSync } from "node:fs";
import { resolve } from "node:path";
import test from "node:test";
import { parse as parseYaml } from "yaml";
import apiReadModel from "../src/generated/apiReadModel.js";
import { buildRiskAppetiteSnapshot, scorePortfolioRisk } from "../src/lib/riskAppetiteCore.js";

const repoRoot = resolve(process.cwd(), "../..");
const riskModel = parseYaml(readFileSync(resolve(repoRoot, "configs/asset_risk_model.yaml"), "utf8"));
const definitions = riskModel.assets;

function assertApproxEqual(actual, expected, tolerance = 1e-9) {
  assert.ok(Math.abs(actual - expected) <= tolerance, `expected ${actual} to be within ${tolerance} of ${expected}`);
}

test("asset risk definitions exactly cover every published universe asset", () => {
  const universeIds = new Set();
  const universeOptions = new Map();
  for (const filename of readdirSync(resolve(repoRoot, "configs/universes")).filter((name) =>
    /^capitalbench_universe_.*\.yaml$/.test(name)
  )) {
    const universe = parseYaml(readFileSync(resolve(repoRoot, "configs/universes", filename), "utf8"));
    for (const option of universe.options ?? []) {
      universeIds.add(option.id);
      universeOptions.set(option.id, option);
    }
  }

  assert.deepEqual(Object.keys(definitions).sort(), Array.from(universeIds).sort());
  assert.ok(Object.keys(definitions).length > 0);
  for (const [optionId, definition] of Object.entries(definitions)) {
    assert.ok(Number.isInteger(definition.risk_score_1_5), `${optionId} risk score must be an integer`);
    assert.ok(definition.risk_score_1_5 >= 1 && definition.risk_score_1_5 <= 5, `${optionId} risk score`);
    assert.ok(definition.risk_on_loading >= -1 && definition.risk_on_loading <= 1, `${optionId} loading`);
    assert.ok(riskModel.regime_groups[definition.regime_group], `${optionId} regime group`);
    assert.equal(typeof definition.defensive, "boolean", `${optionId} defensive flag`);
    assert.equal(typeof definition.technology, "boolean", `${optionId} technology flag`);
  }

  const legacyTechnologyIds = new Set([
    "NASDAQ100",
    "LARGE_GROWTH",
    "TECHNOLOGY",
    "SEMICONDUCTORS",
    "SOFTWARE",
    "BROAD_AI_TECH",
    "AUTONOMOUS_ROBOTICS",
    "CYBERSECURITY"
  ]);
  const legacyDefensiveIds = new Set([
    "CASH",
    "SHORT_TREASURY",
    "INTERMEDIATE_TREASURY",
    "TIPS",
    "INVESTMENT_GRADE_CREDIT",
    "AGGREGATE_BONDS",
    "GOLD",
    "DIVIDEND",
    "LOW_VOL",
    "CONSUMER_STAPLES",
    "UTILITIES"
  ]);
  const scoreByRiskBucket = { cash: 1, low: 2, medium: 3, high: 4, very_high: 5, "very-high": 5, speculative: 5 };

  for (const [optionId, option] of universeOptions) {
    const definition = definitions[optionId];
    const group = String(option.option_group ?? "").toLowerCase();
    const name = String(option.name ?? "").toLowerCase();
    const expectedRiskScore =
      option.is_cash || option.asset_class === "cash"
        ? 1
        : option.asset_class === "crypto"
          ? 5
          : scoreByRiskBucket[String(option.risk_bucket).toLowerCase()] ?? 3;
    const expectedDefensive =
      legacyDefensiveIds.has(optionId) ||
      option.is_cash === true ||
      group.includes("cash") ||
      group.includes("bond") ||
      group.includes("credit");
    const expectedTechnology =
      legacyTechnologyIds.has(optionId) ||
      group.includes("technology") ||
      group.includes("ai") ||
      name.includes("technology") ||
      name.includes("software");

    assert.equal(definition.risk_score_1_5, expectedRiskScore, `${optionId} preserves historical 1-5 score`);
    assert.equal(definition.defensive, expectedDefensive, `${optionId} preserves historical defensive flag`);
    assert.equal(definition.technology, expectedTechnology, `${optionId} preserves historical technology flag`);
  }
});

test("portfolio pulse maps asset loadings onto the documented 0-100 scale", () => {
  assertApproxEqual(scorePortfolioRisk([{ option_id: "CASH", allocation_pct: 100 }], definitions).score, 0);
  assertApproxEqual(scorePortfolioRisk([{ option_id: "SP500", allocation_pct: 100 }], definitions).score, 67.5);
  assertApproxEqual(
    scorePortfolioRisk([{ option_id: "SEMICONDUCTORS", allocation_pct: 100 }], definitions).score,
    97.5
  );
  assertApproxEqual(
    scorePortfolioRisk(
      [
        { option_id: "CASH", allocation_pct: 50 },
        { option_id: "SEMICONDUCTORS", allocation_pct: 50 }
      ],
      definitions
    ).score,
    48.75
  );
});

test("generated live risk snapshot is reproducible from public rounds and portfolios", () => {
  const rebuilt = buildRiskAppetiteSnapshot({
    rounds: apiReadModel.rounds,
    portfolios: apiReadModel.portfolios,
    assets: apiReadModel.assets,
    definitions,
    version: riskModel.version
  });

  assert.deepEqual(apiReadModel.risk_appetite, rebuilt);
  assertApproxEqual(
    rebuilt.current_decision_pulse.score,
    (rebuilt.current_decision_pulse.weekly.score + rebuilt.current_decision_pulse.monthly.score) / 2
  );
  assertApproxEqual(
    rebuilt.current_decision_pulse.top_assets.reduce((total, row) => total + row.allocation_pct, 0),
    100
  );
  assertApproxEqual(
    rebuilt.current_decision_pulse.regime_exposure.reduce((total, row) => total + row.allocation_pct, 0),
    100
  );
});

test("risk appetite history is ordered and preserves separate track calculations", () => {
  const history = apiReadModel.risk_appetite.history;
  const dates = history.decision_pulse.map((point) => point.date);

  assert.deepEqual(dates, [...dates].sort());
  assert.equal(new Set(dates).size, dates.length);
  assert.deepEqual(history.outstanding_live_book.map((point) => point.date), dates);

  for (const point of history.decision_pulse) {
    const availableScores = [point.weekly_score, point.monthly_score].filter(
      (value) => typeof value === "number"
    );
    assert.ok(availableScores.length > 0, `${point.date} should have at least one track score`);
    assertApproxEqual(
      point.combined_score,
      availableScores.reduce((total, value) => total + value, 0) / availableScores.length
    );
    assertApproxEqual(
      point.regime_exposure.reduce((total, row) => total + row.allocation_pct, 0),
      100
    );

    for (const track of ["weekly", "monthly"]) {
      const roundId = point[`${track}_round_id`];
      const trackScore = point[`${track}_score`];
      if (!roundId) {
        assert.equal(trackScore, null);
        continue;
      }
      const portfolios = apiReadModel.portfolios.filter((portfolio) => portfolio.round_id === roundId);
      const byModel = new Map();
      for (const portfolio of portfolios) {
        const values = byModel.get(portfolio.model_id) ?? [];
        values.push(scorePortfolioRisk(portfolio.allocations, definitions).score);
        byModel.set(portfolio.model_id, values);
      }
      const modelScores = Array.from(byModel.values()).map(
        (values) => values.reduce((total, value) => total + value, 0) / values.length
      );
      assertApproxEqual(
        trackScore,
        modelScores.reduce((total, value) => total + value, 0) / modelScores.length
      );
    }
  }

  const latestDecision = history.decision_pulse.at(-1);
  const latestOutstanding = history.outstanding_live_book.at(-1);
  assertApproxEqual(latestDecision.combined_score, apiReadModel.risk_appetite.current_decision_pulse.score);
  assertApproxEqual(latestOutstanding.score, apiReadModel.risk_appetite.outstanding_live_book.score);
  assert.equal(
    latestOutstanding.portfolio_count,
    apiReadModel.risk_appetite.outstanding_live_book.portfolio_count
  );
  assert.ok(!JSON.stringify(history).includes("return_pct"));
  assert.ok(!JSON.stringify(history).includes("price"));
});
