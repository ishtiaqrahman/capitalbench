import { cumulativeCapitalBenchScore } from "./capitalBenchScore.js";

function finiteNumber(value) {
  return typeof value === "number" && Number.isFinite(value);
}

function average(values) {
  const finite = values.filter(finiteNumber);
  return finite.length ? finite.reduce((total, value) => total + value, 0) / finite.length : null;
}

function setStatus(set) {
  if (set.is_current) return "current";
  if (set.is_qualified) return "qualified";
  return set.comparison.comparison_round_count > 0 ? "forming" : "waiting";
}

function setStatusLabel(set) {
  const status = setStatus(set);
  if (status === "current") return "Main results";
  if (status === "qualified") return "Enough rounds";
  if (status === "forming") return "Early results";
  return "No results yet";
}

export function benchmarkSetComparisonOption(set) {
  return {
    set_id: set.set_id,
    track: set.track,
    label: set.label,
    short_label: set.short_label,
    started_at: set.started_at,
    status: setStatus(set),
    status_label: setStatusLabel(set),
    model_count: set.models.length,
    shared_round_count: set.comparison.comparison_round_count,
    qualification_threshold: set.qualification_threshold,
    is_current: set.is_current,
    is_qualified: set.is_qualified
  };
}

function pearson(left, right) {
  if (left.length < 2 || left.length !== right.length) return null;
  const leftAverage = average(left);
  const rightAverage = average(right);
  if (!finiteNumber(leftAverage) || !finiteNumber(rightAverage)) return null;
  const numerator = left.reduce(
    (total, value, index) => total + (value - leftAverage) * (right[index] - rightAverage),
    0
  );
  const leftScale = Math.sqrt(left.reduce((total, value) => total + (value - leftAverage) ** 2, 0));
  const rightScale = Math.sqrt(right.reduce((total, value) => total + (value - rightAverage) ** 2, 0));
  return leftScale > 0 && rightScale > 0 ? numerator / (leftScale * rightScale) : null;
}

function similarityLabel(value) {
  if (!finiteNumber(value)) return "Not available";
  if (value >= 0.8) return "Hardly changed";
  if (value >= 0.5) return "Changed a little";
  if (value >= 0.2) return "Changed";
  return "Changed a lot";
}

function officialResultRows(readModel, roundIds, modelId) {
  const roundIdSet = new Set(roundIds);
  const roundById = new Map(readModel.rounds.map((round) => [round.round_id, round]));
  return readModel.results.filter((row) => {
    if (!roundIdSet.has(row.round_id) || row.model_id !== modelId) return false;
    const round = roundById.get(row.round_id);
    return !round?.official_run_id || !row.run_id || row.run_id === round.official_run_id;
  });
}

function scoreWindow(readModel, roundIds, modelId) {
  const rows = officialResultRows(readModel, roundIds, modelId);
  const portfolioReturns = rows.map((row) => row.portfolio_return_pct).filter(finiteNumber);
  const maximumReturns = rows.map((row) => row.max_possible_return_pct).filter(finiteNumber);
  return {
    round_count: rows.length,
    score:
      portfolioReturns.length === rows.length && maximumReturns.length === rows.length
        ? cumulativeCapitalBenchScore(portfolioReturns, maximumReturns)
        : null,
    average_return_pct: average(portfolioReturns),
    average_alpha_pp: average(rows.map((row) => row.alpha_pp))
  };
}

function modelById(readModel, modelId) {
  return readModel.models.find((model) => model.model_id === modelId) ?? {
    model_id: modelId,
    label: modelId,
    provider: "",
    provider_label: "",
    logo_src: null
  };
}

function modelResult(row) {
  if (!row) return null;
  return {
    rank: row.rank,
    score: row.capitalbench_score,
    average_return_pct: row.portfolio_return_pct,
    average_alpha_pp: row.alpha_pp,
    wins: row.wins,
    positive_alpha_rate_pct: row.positive_alpha_rate_pct,
    included_round_ids: row.included_round_ids
  };
}

function modelRows(readModel, baselineSet, comparisonSet, roundGroups) {
  const baselineByModel = new Map(baselineSet.data.map((row) => [row.model_id, row]));
  const comparisonByModel = new Map(comparisonSet.data.map((row) => [row.model_id, row]));
  const modelIds = Array.from(new Set([...baselineSet.model_ids, ...comparisonSet.model_ids]));
  return modelIds
    .map((modelId) => {
      const model = modelById(readModel, modelId);
      const baseline = baselineByModel.get(modelId);
      const comparison = comparisonByModel.get(modelId);
      const inBaseline = baselineSet.model_ids.includes(modelId);
      const inComparison = comparisonSet.model_ids.includes(modelId);
      return {
        model_id: modelId,
        label: model.label ?? modelId,
        provider: model.provider ?? "",
        provider_label: model.provider_label ?? model.provider ?? "",
        logo_src: model.logo_src ?? null,
        roster_status: inBaseline && inComparison ? "common" : inComparison ? "added" : "removed",
        baseline: modelResult(baseline),
        comparison: modelResult(comparison),
        rank_change:
          baseline && comparison && finiteNumber(baseline.rank) && finiteNumber(comparison.rank)
            ? baseline.rank - comparison.rank
            : null,
        score_change:
          baseline && comparison && finiteNumber(baseline.capitalbench_score) && finiteNumber(comparison.capitalbench_score)
            ? comparison.capitalbench_score - baseline.capitalbench_score
            : null,
        windows: {
          same_rounds: scoreWindow(readModel, roundGroups.shared, modelId),
          baseline_only: scoreWindow(readModel, roundGroups.baselineOnly, modelId),
          comparison_only: scoreWindow(readModel, roundGroups.comparisonOnly, modelId)
        }
      };
    })
    .sort((left, right) => {
      const leftRank = left.comparison?.rank ?? left.baseline?.rank ?? 9999;
      const rightRank = right.comparison?.rank ?? right.baseline?.rank ?? 9999;
      return leftRank - rightRank || left.label.localeCompare(right.label);
    });
}

function summaryText(baselineSet, comparisonSet, rows, roundGroups) {
  const baselineLeader = baselineSet.leader?.label ?? null;
  const comparisonLeader = comparisonSet.leader?.label ?? null;
  const waitingSets = [baselineSet, comparisonSet].filter(
    (set) => set.comparison.comparison_round_count === 0
  );
  if (waitingSets.length) {
    const waitingLabels = waitingSets.map((set) => set.short_label).join(" and ");
    const subject = waitingSets.length === 1 ? "has" : "have";
    return `${waitingLabels} ${subject} no results yet. You can compare the models included, but not performance.`;
  }

  const added = rows.filter((row) => row.roster_status === "added").map((row) => row.label);
  const removed = rows.filter((row) => row.roster_status === "removed").map((row) => row.label);
  const leaderText =
    baselineLeader && comparisonLeader && baselineLeader !== comparisonLeader
      ? `${baselineLeader} ranks first in ${baselineSet.short_label}. ${comparisonLeader} ranks first in ${comparisonSet.short_label}.`
      : baselineLeader
        ? `${baselineLeader} ranks first in both groups.`
        : "The groups do not have results to rank yet.";
  const windowText = roundGroups.shared.length
    ? `The groups share ${roundGroups.shared.length} completed round${roundGroups.shared.length === 1 ? "" : "s"}`
    : "The groups have no completed rounds in common";
  const extraRoundText = [
    roundGroups.baselineOnly.length
      ? `${baselineSet.short_label} includes ${roundGroups.baselineOnly.length} more round${roundGroups.baselineOnly.length === 1 ? "" : "s"}`
      : null,
    roundGroups.comparisonOnly.length
      ? `${comparisonSet.short_label} includes ${roundGroups.comparisonOnly.length} more round${roundGroups.comparisonOnly.length === 1 ? "" : "s"}`
      : null
  ].filter(Boolean).join(", while ");
  const modelText = [
    added.length
      ? `${added.join(", ")} ${added.length === 1 ? "appears" : "appear"} only in ${comparisonSet.short_label}.`
      : null,
    removed.length
      ? `${removed.join(", ")} ${removed.length === 1 ? "appears" : "appear"} only in ${baselineSet.short_label}.`
      : null
  ].filter(Boolean).join(" ");
  return `${leaderText} ${windowText}.${extraRoundText ? ` ${extraRoundText}.` : ""}${modelText ? ` ${modelText}` : ""}`;
}

function trustText(baselineSet, comparisonSet) {
  const sets = [baselineSet, comparisonSet];
  const waitingSets = sets.filter((set) => setStatus(set) === "waiting");
  const scoredSets = sets
    .filter((set) => set.comparison.comparison_round_count > 0)
    .sort((left, right) => right.comparison.comparison_round_count - left.comparison.comparison_round_count);
  if (!scoredSets.length) {
    return "Neither group has results yet. You can compare which models are included, but wait for completed rounds before comparing performance.";
  }
  if (waitingSets.length) {
    const scoredSet = scoredSets[0];
    return `Use ${scoredSet.short_label} because it has ${scoredSet.comparison.comparison_round_count} completed rounds. ${waitingSets.map((set) => set.short_label).join(" and ")} ${waitingSets.length === 1 ? "has" : "have"} no results yet.`;
  }

  const formingSets = sets.filter((set) => setStatus(set) === "forming");
  if (formingSets.length === 2) {
    return "Neither group has enough completed rounds yet. Treat both rankings as early results that may change.";
  }
  if (formingSets.length === 1) {
    const formingSet = formingSets[0];
    const establishedSet = sets.find((set) => set.set_id !== formingSet.set_id);
    const remaining = Math.max(
      0,
      formingSet.qualification_threshold - formingSet.comparison.comparison_round_count
    );
    return `Use ${establishedSet.short_label} as the more reliable ranking because it has ${establishedSet.comparison.comparison_round_count} completed rounds. ${formingSet.short_label} has ${formingSet.comparison.comparison_round_count} and needs ${remaining} more before it has enough evidence to become the main ranking.`;
  }

  const currentSet = sets.find((set) => setStatus(set) === "current");
  if (currentSet) {
    const otherSet = sets.find((set) => set.set_id !== currentSet.set_id);
    return `${currentSet.short_label} is the main published ranking. ${otherSet.short_label} also has enough rounds, so compare them to see whether the results hold across different model groups.`;
  }
  return "Both groups have enough completed rounds. Use the models included and the rounds they share to understand any difference in results.";
}

export function defaultBenchmarkSetComparison(sets, track) {
  const trackSets = sets.filter((set) => set.track === track);
  const baseline =
    trackSets.find((set) => set.is_current) ??
    trackSets.find((set) => set.is_qualified) ??
    trackSets.find((set) => set.comparison.comparison_round_count > 0) ??
    trackSets[0];
  const comparison =
    trackSets
      .filter((set) => set.set_id !== baseline?.set_id && set.comparison.comparison_round_count > 0)
      .sort((left, right) => String(right.started_at ?? "").localeCompare(String(left.started_at ?? "")))[0] ??
    trackSets.find((set) => set.set_id !== baseline?.set_id);
  return baseline && comparison ? { baseline, comparison } : null;
}

export function buildBenchmarkSetComparison(readModel, baselineSet, comparisonSet) {
  if (!baselineSet || !comparisonSet) throw new Error("Two benchmark sets are required.");
  if (baselineSet.set_id === comparisonSet.set_id) throw new Error("Benchmark sets must be different.");
  if (baselineSet.track !== comparisonSet.track) throw new Error("Benchmark sets must use the same track.");

  const baselineRoundIds = baselineSet.comparison.comparison_round_ids;
  const comparisonRoundIds = comparisonSet.comparison.comparison_round_ids;
  const baselineRoundSet = new Set(baselineRoundIds);
  const comparisonRoundSet = new Set(comparisonRoundIds);
  const roundGroups = {
    shared: baselineRoundIds.filter((roundId) => comparisonRoundSet.has(roundId)),
    baselineOnly: baselineRoundIds.filter((roundId) => !comparisonRoundSet.has(roundId)),
    comparisonOnly: comparisonRoundIds.filter((roundId) => !baselineRoundSet.has(roundId))
  };
  const rows = modelRows(readModel, baselineSet, comparisonSet, roundGroups);
  const rankedCommonRows = rows.filter((row) => row.baseline?.rank && row.comparison?.rank);
  const rankSimilarity = pearson(
    rankedCommonRows.map((row) => row.baseline.rank),
    rankedCommonRows.map((row) => row.comparison.rank)
  );
  const baselineTopThree = new Set(
    baselineSet.data.filter((row) => row.rank <= 3).map((row) => row.model_id)
  );
  const comparisonTopThree = new Set(
    comparisonSet.data.filter((row) => row.rank <= 3).map((row) => row.model_id)
  );
  const topThreeOverlap = Array.from(baselineTopThree).filter((modelId) => comparisonTopThree.has(modelId)).length;
  const roundUnionCount = new Set([...baselineRoundIds, ...comparisonRoundIds]).size;

  return {
    id: `${baselineSet.set_id}--${comparisonSet.set_id}`,
    track: baselineSet.track,
    baseline: benchmarkSetComparisonOption(baselineSet),
    comparison: benchmarkSetComparisonOption(comparisonSet),
    rounds: {
      baseline: baselineRoundIds,
      comparison: comparisonRoundIds,
      shared: roundGroups.shared,
      baseline_only: roundGroups.baselineOnly,
      comparison_only: roundGroups.comparisonOnly,
      overlap_pct: roundUnionCount ? (roundGroups.shared.length / roundUnionCount) * 100 : null,
      baseline_excluded: baselineSet.excluded_rounds,
      comparison_excluded: comparisonSet.excluded_rounds
    },
    models: {
      common_count: rows.filter((row) => row.roster_status === "common").length,
      added: rows.filter((row) => row.roster_status === "added").map((row) => row.model_id),
      removed: rows.filter((row) => row.roster_status === "removed").map((row) => row.model_id),
      rows
    },
    ranking: {
      similarity: rankSimilarity,
      similarity_pct: finiteNumber(rankSimilarity) ? rankSimilarity * 100 : null,
      similarity_label: similarityLabel(rankSimilarity),
      top_three_overlap: topThreeOverlap,
      baseline_leader: baselineSet.leader?.model_id ?? null,
      comparison_leader: comparisonSet.leader?.model_id ?? null,
      same_leader:
        Boolean(baselineSet.leader?.model_id) && baselineSet.leader?.model_id === comparisonSet.leader?.model_id
    },
    summary: summaryText(baselineSet, comparisonSet, rows, roundGroups),
    trust_guidance: trustText(baselineSet, comparisonSet)
  };
}
