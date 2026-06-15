import { cumulativeCapitalBenchScore } from "./capitalBenchScore.js";

export const DEFAULT_BENCHMARK_SET_THRESHOLDS = {
  weekly: 6,
  monthly: 3
};

function finiteNumber(value) {
  return typeof value === "number" && Number.isFinite(value);
}

function average(values) {
  const finite = values.filter(finiteNumber);
  return finite.length ? finite.reduce((total, value) => total + value, 0) / finite.length : null;
}

function sum(values) {
  return values.filter(finiteNumber).reduce((total, value) => total + value, 0);
}

function trackLabel(track) {
  return track === "weekly" ? "Weekly" : "Monthly";
}

function roundSortValue(round) {
  return `${round?.exit_date ?? ""}:${round?.decision_deadline_utc ?? ""}:${round?.round_id ?? ""}`;
}

function thresholdFor(readModel, track) {
  return Number(
    readModel?.benchmark_set_policy?.qualification_thresholds?.[track] ??
      DEFAULT_BENCHMARK_SET_THRESHOLDS[track] ??
      1
  );
}

function modelDisplay(modelById, modelId) {
  const model = modelById.get(modelId);
  return {
    model_id: modelId,
    label: model?.label ?? modelId,
    provider: model?.provider ?? "",
    provider_label: model?.provider_label ?? model?.provider ?? "",
    logo_src: model?.logo_src ?? null
  };
}

function setStatus({ isCurrent, isQualified, includedRoundCount }) {
  if (isCurrent) return "current";
  if (isQualified) return "qualified";
  if (includedRoundCount > 0) return "forming";
  return "waiting";
}

function resultRowsForRound(readModel, round) {
  return readModel.results.filter(
    (row) =>
      row.track === round.track &&
      row.round_id === round.round_id &&
      (!round.official_run_id || row.run_id === round.official_run_id)
  );
}

function includedRoundRows(setModelIds, rows) {
  const rowsByModel = new Map(rows.map((row) => [row.model_id, row]));
  return setModelIds.map((modelId) => rowsByModel.get(modelId)).filter(Boolean);
}

function buildSetRows({ readModel, definition, candidateRounds, includedRounds, modelById }) {
  const byModel = new Map();
  const benchmarkReturnValues = [];
  const benchmarkMaxReturnValues = [];
  const maxPossibleReturnValues = [];

  for (const round of includedRounds) {
    const rows = includedRoundRows(definition.model_ids, resultRowsForRound(readModel, round));
    const setRankedRows = [...rows].sort(
      (left, right) =>
        Number(right.portfolio_return_pct ?? -Infinity) - Number(left.portfolio_return_pct ?? -Infinity) ||
        String(left.model_id).localeCompare(String(right.model_id))
    );
    const winnerModelId = setRankedRows[0]?.model_id ?? "";
    const referenceRow = rows[0];

    if (finiteNumber(referenceRow?.benchmark_return_pct) && finiteNumber(referenceRow?.max_possible_return_pct)) {
      benchmarkReturnValues.push(referenceRow.benchmark_return_pct);
      benchmarkMaxReturnValues.push(referenceRow.max_possible_return_pct);
    }
    if (finiteNumber(referenceRow?.max_possible_return_pct)) {
      maxPossibleReturnValues.push(referenceRow.max_possible_return_pct);
    }

    for (const row of rows) {
      const display = modelDisplay(modelById, row.model_id);
      const existing =
        byModel.get(row.model_id) ??
        {
          ...display,
          portfolio_return_values: [],
          benchmark_return_values: [],
          alpha_values: [],
          max_possible_return_values: [],
          wins: 0,
          positive_alpha: 0,
          round_ids: []
        };
      if (finiteNumber(row.portfolio_return_pct)) existing.portfolio_return_values.push(row.portfolio_return_pct);
      if (finiteNumber(row.benchmark_return_pct)) existing.benchmark_return_values.push(row.benchmark_return_pct);
      if (finiteNumber(row.alpha_pp)) {
        existing.alpha_values.push(row.alpha_pp);
        if (row.alpha_pp > 0) existing.positive_alpha += 1;
      }
      if (finiteNumber(row.max_possible_return_pct)) existing.max_possible_return_values.push(row.max_possible_return_pct);
      if (row.model_id === winnerModelId) existing.wins += 1;
      existing.round_ids.push(round.round_id);
      byModel.set(row.model_id, existing);
    }
  }

  const testsRequired = includedRounds.length;
  const data = Array.from(byModel.values())
    .map((row) => {
      const testsIncluded = row.round_ids.length;
      const isRankEligible = testsRequired > 0 && testsIncluded === testsRequired;
      const totalPortfolioReturn = sum(row.portfolio_return_values);
      const totalMaxPossibleReturn = sum(row.max_possible_return_values);
      return {
        model_id: row.model_id,
        label: row.label,
        provider: row.provider,
        provider_label: row.provider_label,
        logo_src: row.logo_src,
        portfolio_return_pct: average(row.portfolio_return_values),
        benchmark_return_pct: average(row.benchmark_return_values),
        alpha_pp: average(row.alpha_values),
        max_possible_return_pct: average(row.max_possible_return_values),
        total_portfolio_return_pct: totalPortfolioReturn,
        total_max_possible_return_pct: totalMaxPossibleReturn,
        capitalbench_score: cumulativeCapitalBenchScore(row.portfolio_return_values, row.max_possible_return_values),
        round_count: testsIncluded,
        tests_required: testsRequired,
        tests_included: testsIncluded,
        is_rank_eligible: isRankEligible,
        sample_status: isRankEligible ? "eligible" : "not_ranked",
        wins: row.wins,
        win_rate_pct: testsIncluded ? (row.wins / testsIncluded) * 100 : null,
        positive_alpha_rate_pct: testsIncluded ? (row.positive_alpha / testsIncluded) * 100 : null,
        included_round_ids: row.round_ids
      };
    })
    .sort(
      (left, right) =>
        Number(right.is_rank_eligible) - Number(left.is_rank_eligible) ||
        Number(right.capitalbench_score ?? -Infinity) - Number(left.capitalbench_score ?? -Infinity) ||
        Number(right.alpha_pp ?? -Infinity) - Number(left.alpha_pp ?? -Infinity) ||
        String(left.label).localeCompare(String(right.label))
    )
    .map((row, index) => ({ rank: index + 1, ...row }));

  const benchmarkTotalReturn = sum(benchmarkReturnValues);
  const benchmarkTotalMaxReturn = sum(benchmarkMaxReturnValues);
  const maxPossibleTotalReturn = sum(maxPossibleReturnValues);
  const completedRoundIds = candidateRounds.map((round) => round.round_id);
  return {
    data,
    benchmark: benchmarkReturnValues.length
      ? {
          label: "S&P 500",
          return_pct: average(benchmarkReturnValues),
          total_return_pct: benchmarkTotalReturn,
          total_max_possible_return_pct: benchmarkTotalMaxReturn,
          capitalbench_score: cumulativeCapitalBenchScore(benchmarkReturnValues, benchmarkMaxReturnValues),
          tests_included: benchmarkReturnValues.length,
          tests_required: testsRequired
        }
      : null,
    max_possible: maxPossibleReturnValues.length
      ? {
          label: "Max possible",
          return_pct: average(maxPossibleReturnValues),
          total_return_pct: maxPossibleTotalReturn,
          total_max_possible_return_pct: maxPossibleTotalReturn,
          capitalbench_score: 100,
          tests_included: maxPossibleReturnValues.length,
          tests_required: testsRequired
        }
      : null,
    comparison: {
      mode: "comparison_set",
      completed_round_count: completedRoundIds.length,
      completed_round_ids: completedRoundIds,
      comparison_round_count: testsRequired,
      comparison_round_ids: includedRounds.map((round) => round.round_id),
      comparison_model_count: definition.model_ids.length,
      is_early_cohort: testsRequired < thresholdFor(readModel, definition.track)
    }
  };
}

function buildBenchmarkSet(readModel, definition, currentSetIds = new Set()) {
  const roundById = new Map(readModel.rounds.map((round) => [round.round_id, round]));
  const modelById = new Map(readModel.models.map((model) => [model.model_id, model]));
  const startRound = roundById.get(definition.started_round_id);
  const startSort = roundSortValue(startRound);
  const threshold = thresholdFor(readModel, definition.track);
  const resolvedRounds = readModel.rounds
    .filter((round) => round.track === definition.track && round.status === "resolved")
    .filter((round) => !startRound || roundSortValue(round) >= startSort)
    .filter((round) => resultRowsForRound(readModel, round).length > 0)
    .sort((left, right) => roundSortValue(left).localeCompare(roundSortValue(right)));

  const includedRounds = [];
  const excludedRounds = [];
  for (const round of resolvedRounds) {
    const rows = resultRowsForRound(readModel, round);
    const presentModelIds = new Set(rows.map((row) => row.model_id));
    const missingModelIds = definition.model_ids.filter((modelId) => !presentModelIds.has(modelId));
    if (missingModelIds.length === 0) {
      includedRounds.push(round);
    } else {
      excludedRounds.push({
        round_id: round.round_id,
        missing_model_ids: missingModelIds,
        present_model_ids: rows.map((row) => row.model_id).sort(),
        reason: "missing_set_model"
      });
    }
  }

  const modelRoster = definition.model_ids.map((modelId) => modelDisplay(modelById, modelId));
  const rows = buildSetRows({ readModel, definition, candidateRounds: resolvedRounds, includedRounds, modelById });
  const isQualified = rows.comparison.comparison_round_count >= threshold;
  const isCurrent = currentSetIds.has(definition.set_id);

  return {
    set_id: definition.set_id,
    track: definition.track,
    label: definition.label,
    short_label: definition.short_label || definition.label,
    description: definition.description || "",
    started_round_id: definition.started_round_id,
    started_at: startRound?.decision_date ?? null,
    model_ids: definition.model_ids,
    models: modelRoster,
    qualification_threshold: threshold,
    is_qualified: isQualified,
    is_current: isCurrent,
    status: setStatus({
      isCurrent,
      isQualified,
      includedRoundCount: rows.comparison.comparison_round_count
    }),
    latest_included_round_id: rows.comparison.comparison_round_ids.at(-1) ?? null,
    latest_completed_round_id: rows.comparison.completed_round_ids.at(-1) ?? null,
    excluded_rounds: excludedRounds,
    excluded_round_ids: excludedRounds.map((round) => round.round_id),
    leader: rows.data.find((row) => row.is_rank_eligible) ?? null,
    ...rows,
    comparison: {
      ...rows.comparison,
      excluded_round_count: excludedRounds.length,
      excluded_round_ids: excludedRounds.map((round) => round.round_id),
      qualification_threshold: threshold,
      is_qualified: isQualified,
      is_current: isCurrent,
      status: setStatus({
        isCurrent,
        isQualified,
        includedRoundCount: rows.comparison.comparison_round_count
      })
    }
  };
}

function currentSetIds(readModel) {
  const definitions = readModel.benchmark_set_definitions ?? [];
  const prelim = definitions.map((definition) => buildBenchmarkSet(readModel, definition));
  const ids = new Set();
  for (const track of ["weekly", "monthly"]) {
    const qualified = prelim
      .filter((set) => set.track === track && set.is_qualified)
      .sort((left, right) => {
        const leftRound = readModel.rounds.find((round) => round.round_id === left.started_round_id);
        const rightRound = readModel.rounds.find((round) => round.round_id === right.started_round_id);
        return roundSortValue(rightRound).localeCompare(roundSortValue(leftRound)) || right.set_id.localeCompare(left.set_id);
      });
    if (qualified[0]) ids.add(qualified[0].set_id);
  }
  return ids;
}

export function buildBenchmarkSetsData(readModel) {
  const ids = currentSetIds(readModel);
  const sets = (readModel.benchmark_set_definitions ?? [])
    .map((definition) => buildBenchmarkSet(readModel, definition, ids))
    .sort((left, right) => {
      const trackOrder = left.track.localeCompare(right.track);
      if (trackOrder !== 0) return trackOrder;
      const leftRound = readModel.rounds.find((round) => round.round_id === left.started_round_id);
      const rightRound = readModel.rounds.find((round) => round.round_id === right.started_round_id);
      return roundSortValue(rightRound).localeCompare(roundSortValue(leftRound)) || left.label.localeCompare(right.label);
    });

  return {
    policy: {
      version: readModel.benchmark_set_policy?.version ?? "benchmark_sets_v1",
      qualification_thresholds: {
        weekly: thresholdFor(readModel, "weekly"),
        monthly: thresholdFor(readModel, "monthly")
      }
    },
    current: {
      weekly: sets.find((set) => set.track === "weekly" && set.is_current)?.set_id ?? null,
      monthly: sets.find((set) => set.track === "monthly" && set.is_current)?.set_id ?? null
    },
    sets
  };
}

export function benchmarkSetById(readModel, setId) {
  return buildBenchmarkSetsData(readModel).sets.find((set) => set.set_id === setId) ?? null;
}

export function benchmarkSetsForTrack(readModel, track) {
  return buildBenchmarkSetsData(readModel).sets.filter((set) => set.track === track);
}

export function benchmarkSetsForModel(readModel, modelId) {
  const statusOrder = {
    current: 0,
    qualified: 1,
    forming: 2,
    waiting: 3
  };
  const trackOrder = {
    weekly: 0,
    monthly: 1
  };

  return buildBenchmarkSetsData(readModel).sets
    .filter((set) => set.model_ids.includes(modelId))
    .map((set) => ({
      ...set,
      model_row: set.data.find((row) => row.model_id === modelId) ?? null
    }))
    .sort(
      (left, right) =>
        (statusOrder[left.status] ?? 9) - (statusOrder[right.status] ?? 9) ||
        (trackOrder[left.track] ?? 9) - (trackOrder[right.track] ?? 9) ||
        String(right.started_at ?? "").localeCompare(String(left.started_at ?? "")) ||
        String(left.label).localeCompare(String(right.label))
    );
}

export function currentBenchmarkSet(readModel, track) {
  return benchmarkSetsForTrack(readModel, track).find((set) => set.is_current) ?? null;
}

export function featuredBenchmarkSet(readModel, track) {
  const sets = benchmarkSetsForTrack(readModel, track);
  return (
    sets.find((set) => set.is_current) ??
    [...sets].sort(
      (left, right) =>
        right.comparison.comparison_round_count - left.comparison.comparison_round_count ||
        String(right.started_at ?? "").localeCompare(String(left.started_at ?? ""))
    )[0] ??
    null
  );
}

function displayReturn(value) {
  return finiteNumber(value) ? value / 100 : 0;
}

function displayScore(value) {
  return finiteNumber(value) ? value : 0;
}

function displaySampleStatus(set) {
  if (set.is_current) return "current";
  if (set.is_qualified) return "eligible";
  return "forming";
}

export function benchmarkSetToScorecard(set, options = {}) {
  if (!set || set.comparison.comparison_round_count === 0) return null;
  const label = trackLabel(set.track);
  const statusLabel = set.is_current
    ? `Current ${label} Benchmark`
    : set.is_qualified
      ? `${label} Qualified Comparison Set`
      : `${label} Benchmark Forming`;

  const modelAverageRows = set.data.map((row) => ({
    key: row.model_id,
    kind: "model",
    label: row.label,
    provider: row.provider,
    providerLabel: row.provider_label,
    logoSrc: row.logo_src,
    averageReturn: displayReturn(row.portfolio_return_pct),
    averageAlphaVsSp500: displayReturn(row.alpha_pp),
    testsIncluded: row.tests_included,
    testsRequired: row.tests_required,
    isRankEligible: row.is_rank_eligible,
    sampleStatus: displaySampleStatus(set),
    roundsIncluded: row.included_round_ids
  }));

  const modelNormalizedRows = set.data.map((row) => ({
    key: row.model_id,
    kind: "model",
    label: row.label,
    provider: row.provider,
    providerLabel: row.provider_label,
    logoSrc: row.logo_src,
    averageScore: displayScore(row.capitalbench_score),
    averageReturn: displayReturn(row.portfolio_return_pct),
    totalReturn: displayReturn(row.total_portfolio_return_pct),
    totalMaxPossibleReturn: displayReturn(row.total_max_possible_return_pct),
    testsIncluded: row.tests_included,
    testsRequired: row.tests_required,
    isRankEligible: row.is_rank_eligible,
    sampleStatus: displaySampleStatus(set),
    roundsIncluded: row.included_round_ids,
    scoreValues: []
  }));

  const benchmarkAverageRow = set.benchmark
    ? {
        key: "sp500",
        kind: "benchmark",
        label: "S&P 500",
        providerLabel: "Benchmark",
        averageReturn: displayReturn(set.benchmark.return_pct),
        averageAlphaVsSp500: 0,
        testsIncluded: set.benchmark.tests_included,
        testsRequired: set.benchmark.tests_required,
        isRankEligible: set.benchmark.tests_included === set.benchmark.tests_required,
        sampleStatus: "reference",
        roundsIncluded: set.comparison.comparison_round_ids
      }
    : undefined;

  const benchmarkNormalizedRow = set.benchmark
    ? {
        key: "sp500",
        kind: "benchmark",
        label: "S&P 500",
        providerLabel: "Benchmark",
        averageScore: displayScore(set.benchmark.capitalbench_score),
        averageReturn: displayReturn(set.benchmark.return_pct),
        totalReturn: displayReturn(set.benchmark.total_return_pct),
        totalMaxPossibleReturn: displayReturn(set.benchmark.total_max_possible_return_pct),
        testsIncluded: set.benchmark.tests_included,
        testsRequired: set.benchmark.tests_required,
        isRankEligible: set.benchmark.tests_included === set.benchmark.tests_required,
        sampleStatus: "reference",
        roundsIncluded: set.comparison.comparison_round_ids,
        scoreValues: []
      }
    : undefined;

  const maxPossibleAverageRow = set.max_possible
    ? {
        key: "max-possible",
        kind: "reference",
        label: "Max possible",
        providerLabel: "Best asset in universe",
        averageReturn: displayReturn(set.max_possible.return_pct),
        testsIncluded: set.max_possible.tests_included,
        testsRequired: set.max_possible.tests_required,
        isRankEligible: true,
        sampleStatus: "reference",
        roundsIncluded: set.comparison.comparison_round_ids
      }
    : undefined;

  const maxPossibleNormalizedRow = set.max_possible
    ? {
        key: "max-possible",
        kind: "reference",
        label: "Max possible",
        providerLabel: "Hindsight best asset",
        averageScore: 100,
        averageReturn: displayReturn(set.max_possible.return_pct),
        totalReturn: displayReturn(set.max_possible.total_return_pct),
        totalMaxPossibleReturn: displayReturn(set.max_possible.total_max_possible_return_pct),
        testsIncluded: set.max_possible.tests_included,
        testsRequired: set.max_possible.tests_required,
        isRankEligible: true,
        sampleStatus: "reference",
        roundsIncluded: set.comparison.comparison_round_ids,
        scoreValues: []
      }
    : undefined;

  const averageRows = [
    ...modelAverageRows,
    ...(benchmarkAverageRow ? [benchmarkAverageRow] : []),
    ...(maxPossibleAverageRow ? [maxPossibleAverageRow] : [])
  ];
  const normalizedRows = [
    ...modelNormalizedRows,
    ...(benchmarkNormalizedRow ? [benchmarkNormalizedRow] : []),
    ...(maxPossibleNormalizedRow ? [maxPossibleNormalizedRow] : [])
  ];

  return {
    track: set.track,
    label,
    setId: set.set_id,
    setLabel: set.label,
    setShortLabel: set.short_label,
    setDescription: set.description,
    displayKicker: options.displayKicker ?? "Equal-run benchmark",
    displayTitle: options.displayTitle ?? statusLabel,
    description:
      options.description ??
      `Every ranked model in this set completed the same ${set.comparison.comparison_round_count} ${label.toLowerCase()} rounds.`,
    scoreChartKicker: "Shared resolved rounds",
    scoreChartTitle: "CapitalBench Score",
    scoreChartDescription:
      "Max possible = best eligible asset in each included round. Every ranked model has the same included rounds.",
    completedRoundCount: set.comparison.completed_round_count,
    completedRoundIds: set.comparison.completed_round_ids,
    comparisonRoundCount: set.comparison.comparison_round_count,
    comparisonRoundIds: set.comparison.comparison_round_ids,
    excludedRoundIds: set.comparison.excluded_round_ids,
    excludedRounds: set.excluded_rounds,
    comparisonModelCount: set.comparison.comparison_model_count,
    comparisonMode: "comparison_set",
    qualificationThreshold: set.qualification_threshold,
    isQualified: set.is_qualified,
    isCurrent: set.is_current,
    isEarlyCohort: !set.is_qualified,
    latestRoundId: set.latest_included_round_id ?? "",
    averageRows,
    normalizedRows,
    topAverageRow: modelAverageRows.find((row) => row.isRankEligible),
    topNormalizedRow: modelNormalizedRows.find((row) => row.isRankEligible),
    benchmarkAverageRow
  };
}
