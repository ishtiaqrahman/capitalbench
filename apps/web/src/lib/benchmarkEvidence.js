import { buildBenchmarkSetsData, featuredBenchmarkSet } from "./benchmarkSets.js";

const TRACKS = ["weekly", "monthly"];
const TRACK_LABELS = {
  weekly: "Weekly",
  monthly: "Monthly"
};

function finiteNumber(value) {
  return typeof value === "number" && Number.isFinite(value);
}

function roundSortValue(round) {
  return `${round?.exit_date ?? ""}:${round?.decision_deadline_utc ?? ""}:${round?.round_id ?? ""}`;
}

function thresholdFor(readModel, track) {
  return Number(readModel?.benchmark_set_policy?.qualification_thresholds?.[track] ?? (track === "weekly" ? 6 : 3));
}

function maturityFor(track, roundCount, threshold) {
  const establishedThreshold = track === "weekly" ? 12 : 6;
  if (roundCount >= establishedThreshold) {
    return {
      key: "more_established",
      label: "More established",
      description: `${TRACK_LABELS[track]} evidence has enough completed rounds for stronger pattern reads, while still needing ongoing live validation.`
    };
  }
  if (roundCount >= threshold) {
    return {
      key: "qualified_forming",
      label: "Qualified but still forming",
      description: `${TRACK_LABELS[track]} evidence has crossed the current benchmark threshold, but the sample is still early for strong performance claims.`
    };
  }
  return {
    key: "early",
    label: "Early",
    description: `${TRACK_LABELS[track]} evidence has not reached the current benchmark threshold yet. Treat results as a forming sample.`
  };
}

function protocolMix(rounds) {
  const counts = rounds.reduce((map, round) => {
    const key = String(round.submission_format ?? "unknown") || "unknown";
    map.set(key, (map.get(key) ?? 0) + 1);
    return map;
  }, new Map());
  const portfolioCount = counts.get("portfolio") ?? 0;
  const singlePickCount = counts.get("single_pick") ?? 0;
  const unknownCount = counts.get("unknown") ?? 0;
  const protocolCount = Array.from(counts.values()).reduce((total, value) => total + value, 0);

  if (protocolCount === 0) {
    return {
      key: "none",
      label: "No scored protocol yet",
      description: "No completed scored rounds are available for this track yet.",
      counts: {}
    };
  }
  if (counts.size === 1 && portfolioCount > 0) {
    return {
      key: "portfolio_only",
      label: "Portfolio-only",
      description: "Completed rounds use constrained multi-asset portfolios.",
      counts: Object.fromEntries(counts)
    };
  }
  if (counts.size === 1 && singlePickCount > 0) {
    return {
      key: "single_pick_only",
      label: "Single-pick only",
      description: "Completed rounds use the original one-asset decision protocol.",
      counts: Object.fromEntries(counts)
    };
  }
  return {
    key: "mixed",
    label: "Mixed protocol",
    description: `Completed history includes ${portfolioCount} portfolio, ${singlePickCount} single-pick, and ${unknownCount} unlabelled rounds.`,
    counts: Object.fromEntries(counts)
  };
}

function insightAvailableForTrack(readModel, track, category) {
  return Boolean(
    readModel?.insights?.insights?.some(
      (insight) => insight.category === category && insight.context?.track === track && insight.status === "published"
    )
  );
}

function buildBaselineList({ readModel, track, resolvedRoundIds, resultRows }) {
  const returnRows = (readModel.returns ?? []).filter(
    (row) => row.track === track && resolvedRoundIds.has(row.round_id)
  );
  const hasSp500 =
    resultRows.some((row) => finiteNumber(row.benchmark_return_pct)) ||
    returnRows.some((row) => row.is_benchmark || row.option_id === "SP500");
  const hasOracle =
    resultRows.some((row) => finiteNumber(row.max_possible_return_pct)) ||
    returnRows.some((row) => finiteNumber(row.return_pct));
  const hasCash = returnRows.some((row) => row.is_cash || row.option_id === "CASH");
  const hasConsensus = insightAvailableForTrack(readModel, track, "consensus_performance");

  return [
    {
      key: "sp500",
      label: "S&P 500",
      available: hasSp500,
      description: "Same-window broad-market reference."
    },
    {
      key: "cash",
      label: "Cash",
      available: hasCash,
      description: "Zero-return or explicit cash row when present in the saved universe."
    },
    {
      key: "oracle",
      label: "Hindsight best asset",
      available: hasOracle,
      description: "The highest-returning scored option in the completed round window."
    },
    {
      key: "ai_consensus",
      label: "AI consensus portfolio",
      available: hasConsensus,
      description: "Average model allocation insight when generated for the latest scored round."
    }
  ];
}

function buildTrackEvidence(readModel, track, benchmarkSets) {
  const threshold = thresholdFor(readModel, track);
  const resolvedRounds = (readModel.rounds ?? [])
    .filter((round) => round.track === track && round.status === "resolved")
    .filter((round) => (readModel.results ?? []).some((row) => row.round_id === round.round_id && row.track === track))
    .sort((left, right) => roundSortValue(left).localeCompare(roundSortValue(right)));
  const resolvedRoundIds = new Set(resolvedRounds.map((round) => round.round_id));
  const resultRows = (readModel.results ?? []).filter(
    (row) => row.track === track && resolvedRoundIds.has(row.round_id)
  );
  const modelIds = new Set(resultRows.map((row) => row.model_id).filter(Boolean));
  const currentSetId = benchmarkSets.current?.[track] ?? null;
  const currentSet = currentSetId ? benchmarkSets.sets.find((set) => set.set_id === currentSetId) ?? null : null;
  const featuredSet = featuredBenchmarkSet(readModel, track);
  const displaySet = currentSet ?? featuredSet;
  const sharedRoundCount = displaySet?.comparison?.comparison_round_count ?? 0;
  const sharedModelCount = displaySet?.comparison?.comparison_model_count ?? displaySet?.model_ids?.length ?? 0;
  const maturity = maturityFor(track, resolvedRounds.length, threshold);
  const equalRunAvailable = Boolean(displaySet && sharedRoundCount > 0);

  return {
    track,
    label: TRACK_LABELS[track],
    resolved_round_count: resolvedRounds.length,
    resolved_model_result_count: resultRows.length,
    model_count: modelIds.size,
    latest_resolved_round_id: resolvedRounds.at(-1)?.round_id ?? null,
    latest_resolved_exit_date: resolvedRounds.at(-1)?.exit_date ?? null,
    qualification_threshold: threshold,
    sample_maturity: maturity,
    protocol_mix: protocolMix(resolvedRounds),
    equal_run_comparison: {
      available: equalRunAvailable,
      label: equalRunAvailable ? "Equal-run comparison available" : "No equal-run comparison yet",
      description: equalRunAvailable
        ? "Every ranked model in the displayed comparison set completed the same included rounds."
        : "This track has not yet produced a shared-round comparison set with completed model results.",
      current_set_id: currentSet?.set_id ?? null,
      featured_set_id: displaySet?.set_id ?? null,
      featured_set_label: displaySet?.short_label ?? displaySet?.label ?? null,
      shared_round_count: sharedRoundCount,
      shared_model_count: sharedModelCount,
      is_current: Boolean(displaySet?.is_current),
      is_qualified: Boolean(displaySet?.is_qualified),
      excluded_round_count: displaySet?.comparison?.excluded_round_count ?? 0
    },
    baselines: buildBaselineList({ readModel, track, resolvedRoundIds, resultRows }),
    score_scale: {
      key: "oracle_relative",
      label: "Oracle-relative CapitalBench Score",
      description: "100 means matching the hindsight best asset for the same scored window; negative values preserve losses.",
      href: "/scoring/#capitalbench-score",
      investable_strategy_result: false
    },
    caveat:
      "Use this as benchmark evidence, not an investable strategy result. More resolved rounds are needed before making strong performance claims."
  };
}

export function buildBenchmarkEvidence(readModel) {
  const benchmarkSets = buildBenchmarkSetsData(readModel);
  const tracks = Object.fromEntries(TRACKS.map((track) => [track, buildTrackEvidence(readModel, track, benchmarkSets)]));

  return {
    version: "benchmark_evidence_v1",
    generated_at: readModel.generated_at ?? new Date().toISOString(),
    policy: {
      qualification_thresholds: {
        weekly: thresholdFor(readModel, "weekly"),
        monthly: thresholdFor(readModel, "monthly")
      },
      maturity_thresholds: {
        weekly: {
          early_below: thresholdFor(readModel, "weekly"),
          more_established_at: 12
        },
        monthly: {
          early_below: thresholdFor(readModel, "monthly"),
          more_established_at: 6
        }
      }
    },
    tracks
  };
}

export default buildBenchmarkEvidence;
