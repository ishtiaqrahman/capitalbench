export const MODEL_BEHAVIOR_VERSION = "model_behavior_v2";
export const MODEL_BEHAVIOR_METHOD_VERSION = "capitalbench_behavior_evidence_v2";
export const MODEL_PATTERN_REPORT_VERSION = "model_behavior_pattern_report_v2";

export const BEHAVIOR_SIGNAL_RULES = Object.freeze({
  minimum_matched_portfolios: 8,
  minimum_independent_decision_dates: 6,
  minimum_track_observations: 4,
  persistence_rate_pct: 65,
  established_minimum_decision_dates: 16,
  established_persistence_rate_pct: 75
});

const DIMENSIONS = Object.freeze([
  {
    key: "risk_taking",
    metric_key: "risk_taking_score",
    label: "Risk taking",
    short_label: "Risk",
    unit: "score_100",
    materiality_floor: 4,
    value: (row) => row.risk_pulse,
    high_modifier: "High-risk",
    low_modifier: "Risk-conscious",
    tone: "risk"
  },
  {
    key: "technology",
    metric_key: "tech_pct",
    label: "Technology",
    short_label: "Technology",
    unit: "percentage_points",
    materiality_floor: 5,
    value: (row) => row.tech_pct,
    high_modifier: "Technology-focused",
    low_modifier: "Technology-light",
    tone: "technology"
  },
  {
    key: "real_assets",
    metric_key: "real_assets_pct",
    label: "Real assets",
    short_label: "Real assets",
    unit: "percentage_points",
    materiality_floor: 5,
    value: (row) => row.real_assets_pct,
    high_modifier: "Real-asset",
    low_modifier: null,
    tone: "diversifier"
  },
  {
    key: "international",
    metric_key: "international_pct",
    label: "International assets",
    short_label: "International",
    unit: "percentage_points",
    materiality_floor: 4,
    value: (row) => row.international_pct,
    high_modifier: "International",
    low_modifier: null,
    tone: "diversifier"
  },
  {
    key: "defensive",
    metric_key: "defensive_pct",
    label: "Defensive assets",
    short_label: "Defensive",
    unit: "percentage_points",
    materiality_floor: 4,
    value: (row) => row.defensive_pct,
    high_modifier: "Defensive",
    low_modifier: null,
    tone: "diversifier"
  },
  {
    key: "cash_duration",
    metric_key: "cash_duration_pct",
    label: "Cash and duration",
    short_label: "Cash/duration",
    unit: "percentage_points",
    materiality_floor: 4,
    value: (row) => row.cash_duration_pct,
    high_modifier: "Capital-preservation",
    low_modifier: null,
    tone: "diversifier"
  },
  {
    key: "benchmark_core",
    metric_key: "benchmark_pct",
    label: "S&P 500 core",
    short_label: "S&P 500 core",
    unit: "percentage_points",
    materiality_floor: 5,
    value: (row) => row.benchmark_pct,
    high_modifier: "Benchmark-anchored",
    low_modifier: "Benchmark-light",
    tone: "stability"
  },
  {
    key: "top_allocation",
    metric_key: "average_top_allocation_pct",
    label: "Largest holding",
    short_label: "Top holding",
    unit: "percentage_points",
    materiality_floor: 5,
    value: (row) => row.top_allocation_pct,
    high_modifier: null,
    low_modifier: null,
    tone: "conviction"
  },
  {
    key: "holding_count",
    metric_key: "average_holding_count",
    label: "Holding count",
    short_label: "Holdings",
    unit: "holdings",
    materiality_floor: 0.5,
    value: (row) => row.holding_count,
    high_modifier: null,
    low_modifier: null,
    tone: "conviction"
  }
]);

function finite(value) {
  return typeof value === "number" && Number.isFinite(value);
}

function average(values) {
  const rows = values.filter(finite);
  return rows.length ? rows.reduce((total, value) => total + value, 0) / rows.length : null;
}

function median(values) {
  const rows = values.filter(finite).sort((left, right) => left - right);
  if (!rows.length) return null;
  const middle = Math.floor(rows.length / 2);
  return rows.length % 2 ? rows[middle] : (rows[middle - 1] + rows[middle]) / 2;
}

function rounded(value, digits = 2) {
  return finite(value) ? Number(value.toFixed(digits)) : null;
}

function pct(value, digits = 1) {
  return finite(value) ? `${value.toFixed(digits)}%` : "n/a";
}

function signedDelta(evidence, value, digits = 1) {
  if (!finite(value)) return "n/a";
  const sign = value > 0 ? "+" : value < 0 ? "−" : "";
  const unit = evidence.unit === "score_100" ? " pts" : evidence.unit === "holdings" ? " holdings" : "pp";
  return `${sign}${Math.abs(value).toFixed(digits)}${unit}`;
}

function formattedValue(evidence, value, digits = 1) {
  if (!finite(value)) return "n/a";
  if (evidence.unit === "score_100") return `${value.toFixed(digits)}/100`;
  if (evidence.unit === "holdings") return `${value.toFixed(digits)} holdings`;
  return `${value.toFixed(digits)}%`;
}

function formattedDelta(evidence, value, digits = 1) {
  if (!finite(value)) return "n/a";
  if (evidence.unit === "score_100") return `${Math.abs(value).toFixed(digits)} points`;
  if (evidence.unit === "holdings") return `${Math.abs(value).toFixed(digits)} holdings`;
  return `${Math.abs(value).toFixed(digits)} percentage points`;
}

function unique(values) {
  return Array.from(new Set(values.filter(Boolean)));
}

function groupBy(values, getter) {
  const output = new Map();
  for (const value of values) {
    const key = getter(value);
    output.set(key, [...(output.get(key) ?? []), value]);
  }
  return output;
}

function peerObservations(scoredRows) {
  const byModel = new Map();
  const groups = groupBy(scoredRows, (row) => `${row.round_id}:${row.run_id}:${row.track}`);
  for (const rows of groups.values()) {
    if (new Set(rows.map((row) => row.model_id)).size < 3) continue;
    for (const row of rows) {
      const dimensions = byModel.get(row.model_id) ?? new Map();
      for (const definition of DIMENSIONS) {
        const value = definition.value(row);
        const peerValues = rows
          .filter((peer) => peer.model_id !== row.model_id)
          .map((peer) => definition.value(peer))
          .filter(finite);
        const peerMedian = median(peerValues);
        if (!finite(value) || !finite(peerMedian)) continue;
        const values = dimensions.get(definition.key) ?? [];
        values.push({
          round_id: row.round_id,
          run_id: row.run_id,
          track: row.track,
          decision_date: row.decision_date || row.entry_date || row.round_id,
          methodology_version: row.methodology_version || "unknown",
          chronology: row.chronology || `${row.decision_date || row.entry_date || ""}:${row.round_id}`,
          value,
          peer_median: peerMedian,
          delta: value - peerMedian,
          peer_count: peerValues.length
        });
        dimensions.set(definition.key, values);
      }
      byModel.set(row.model_id, dimensions);
    }
  }
  return byModel;
}

function observationSummary(observations) {
  if (!observations.length) {
    return {
      observation_count: 0,
      decision_date_count: 0,
      average_value: null,
      median_value: null,
      average_peer_median: null,
      median_peer_median: null,
      average_delta: null,
      median_delta: null,
      positive_rate_pct: null,
      negative_rate_pct: null
    };
  }
  return {
    observation_count: observations.length,
    decision_date_count: unique(observations.map((row) => row.decision_date)).length,
    average_value: rounded(average(observations.map((row) => row.value))),
    median_value: rounded(median(observations.map((row) => row.value))),
    average_peer_median: rounded(average(observations.map((row) => row.peer_median))),
    median_peer_median: rounded(median(observations.map((row) => row.peer_median))),
    average_delta: rounded(average(observations.map((row) => row.delta))),
    median_delta: rounded(median(observations.map((row) => row.delta))),
    positive_rate_pct: rounded((observations.filter((row) => row.delta > 0).length / observations.length) * 100),
    negative_rate_pct: rounded((observations.filter((row) => row.delta < 0).length / observations.length) * 100)
  };
}

function latestMethodology(observations) {
  return [...observations].sort((left, right) => left.chronology.localeCompare(right.chronology)).at(-1)?.methodology_version ?? null;
}

function dimensionEvidence(definition, observations) {
  const overall = observationSummary(observations);
  const weekly = observationSummary(observations.filter((row) => row.track === "weekly"));
  const monthly = observationSummary(observations.filter((row) => row.track === "monthly"));
  const methodology = Object.fromEntries(
    Array.from(groupBy(observations, (row) => row.methodology_version).entries())
      .sort(([left], [right]) => left.localeCompare(right))
      .map(([key, rows]) => [key, observationSummary(rows)])
  );
  const highPersistence = overall.positive_rate_pct ?? 0;
  const lowPersistence = overall.negative_rate_pct ?? 0;
  const enoughSample =
    overall.observation_count >= BEHAVIOR_SIGNAL_RULES.minimum_matched_portfolios &&
    overall.decision_date_count >= BEHAVIOR_SIGNAL_RULES.minimum_independent_decision_dates;
  const highQualified =
    enoughSample &&
    Number(overall.median_delta) >= definition.materiality_floor &&
    highPersistence >= BEHAVIOR_SIGNAL_RULES.persistence_rate_pct;
  const lowQualified =
    enoughSample &&
    Number(overall.median_delta) <= -definition.materiality_floor &&
    lowPersistence >= BEHAVIOR_SIGNAL_RULES.persistence_rate_pct;
  const trackConflict =
    weekly.observation_count >= BEHAVIOR_SIGNAL_RULES.minimum_track_observations &&
    monthly.observation_count >= BEHAVIOR_SIGNAL_RULES.minimum_track_observations &&
    finite(weekly.median_delta) &&
    finite(monthly.median_delta) &&
    Math.abs(weekly.median_delta) >= definition.materiality_floor &&
    Math.abs(monthly.median_delta) >= definition.materiality_floor &&
    Math.sign(weekly.median_delta) !== Math.sign(monthly.median_delta);
  const currentMethod = latestMethodology(observations);
  const currentMethodSummary = currentMethod ? methodology[currentMethod] : null;
  const overallDirection = Math.sign(overall.median_delta ?? 0);
  const currentDirection = Math.sign(currentMethodSummary?.median_delta ?? 0);
  const currentPersistence =
    currentDirection > 0 ? currentMethodSummary?.positive_rate_pct ?? 0 : currentMethodSummary?.negative_rate_pct ?? 0;
  const methodologyConflict = Boolean(
    currentMethodSummary &&
      currentMethodSummary.observation_count >= BEHAVIOR_SIGNAL_RULES.minimum_matched_portfolios &&
      currentMethodSummary.decision_date_count >= BEHAVIOR_SIGNAL_RULES.minimum_independent_decision_dates &&
      Math.abs(currentMethodSummary.median_delta ?? 0) >= definition.materiality_floor &&
      currentPersistence >= BEHAVIOR_SIGNAL_RULES.persistence_rate_pct &&
      overallDirection !== 0 &&
      currentDirection !== 0 &&
      overallDirection !== currentDirection
  );
  return {
    key: definition.key,
    metric_key: definition.metric_key,
    label: definition.label,
    short_label: definition.short_label,
    unit: definition.unit,
    tone: definition.tone,
    materiality_floor: definition.materiality_floor,
    overall,
    tracks: { weekly, monthly },
    methodology,
    current_methodology_version: currentMethod,
    high_qualified: highQualified && !trackConflict,
    low_qualified: lowQualified && !trackConflict,
    track_conflict: trackConflict,
    methodology_conflict: methodologyConflict
  };
}

function strengthFor(evidence, direction) {
  const delta = Math.abs(evidence.overall.median_delta ?? 0);
  const persistence = direction === "high" ? evidence.overall.positive_rate_pct ?? 0 : evidence.overall.negative_rate_pct ?? 0;
  return {
    materiality_ratio: rounded(delta / evidence.materiality_floor, 4),
    persistence_rate_pct: rounded(persistence)
  };
}

function compareCandidates(left, right) {
  return (
    Number(right.strength.materiality_ratio ?? 0) - Number(left.strength.materiality_ratio ?? 0) ||
    Number(right.strength.persistence_rate_pct ?? 0) - Number(left.strength.persistence_rate_pct ?? 0) ||
    left.key.localeCompare(right.key)
  );
}

function exposureCandidates(evidenceByKey) {
  const output = [];
  for (const definition of DIMENSIONS.slice(0, 7)) {
    const evidence = evidenceByKey[definition.key];
    if (!evidence) continue;
    if (evidence.high_qualified && definition.high_modifier) {
      output.push({
        key: definition.key,
        metric_key: definition.metric_key,
        direction: "high",
        modifier: definition.high_modifier,
        label: definition.label,
        short_label: definition.short_label,
        tone: definition.tone,
        evidence,
        strength: strengthFor(evidence, "high")
      });
    }
    if (evidence.low_qualified && definition.low_modifier) {
      output.push({
        key: definition.key,
        metric_key: definition.metric_key,
        direction: "low",
        modifier: definition.low_modifier,
        label: definition.label,
        short_label: definition.short_label,
        tone: definition.tone,
        evidence,
        strength: strengthFor(evidence, "low")
      });
    }
  }
  return output.sort(compareCandidates);
}

function structureCandidates(evidenceByKey, profile) {
  const top = evidenceByKey.top_allocation;
  const holdings = evidenceByKey.holding_count;
  const candidates = [];
  if (top?.high_qualified || holdings?.low_qualified) {
    const supporting = [top?.high_qualified ? strengthFor(top, "high") : null, holdings?.low_qualified ? strengthFor(holdings, "low") : null]
      .filter(Boolean)
      .sort((left, right) => Number(right.materiality_ratio) - Number(left.materiality_ratio));
    candidates.push({
      key: "concentration",
      noun: top?.high_qualified && holdings?.low_qualified ? "high-conviction concentrator" : "concentrated allocator",
      tone: "conviction",
      strength: supporting[0] ?? { materiality_ratio: 1, persistence_rate_pct: 0 },
      metric_keys: ["average_top_allocation_pct", "average_holding_count"],
      evidence_keys: [top?.high_qualified ? "top_allocation" : null, holdings?.low_qualified ? "holding_count" : null].filter(Boolean)
    });
  }
  if (top?.low_qualified || holdings?.high_qualified) {
    const supporting = [top?.low_qualified ? strengthFor(top, "low") : null, holdings?.high_qualified ? strengthFor(holdings, "high") : null]
      .filter(Boolean)
      .sort((left, right) => Number(right.materiality_ratio) - Number(left.materiality_ratio));
    candidates.push({
      key: "diversification",
      noun: "diversified allocator",
      tone: "stability",
      strength: supporting[0] ?? { materiality_ratio: 1, persistence_rate_pct: 0 },
      metric_keys: ["average_top_allocation_pct", "average_holding_count"],
      evidence_keys: [top?.low_qualified ? "top_allocation" : null, holdings?.high_qualified ? "holding_count" : null].filter(Boolean)
    });
  }

  const turnoverPercentile = profile.peer_percentiles?.turnover_stability;
  const turnoverCount = Number(profile.turnover?.turnover_observation_count ?? 0);
  if (finite(turnoverPercentile) && turnoverCount >= 6 && turnoverPercentile <= 20) {
    candidates.push({
      key: "high_turnover",
      noun: "tactical allocator",
      tone: "distinctive",
      strength: { materiality_ratio: rounded((20 - turnoverPercentile) / 20 + 1, 4), persistence_rate_pct: null },
      metric_keys: ["average_turnover_pct"],
      evidence_keys: []
    });
  }
  if (finite(turnoverPercentile) && turnoverCount >= 6 && turnoverPercentile >= 80) {
    candidates.push({
      key: "low_turnover",
      noun: "steady allocator",
      tone: "stability",
      strength: { materiality_ratio: rounded((turnoverPercentile - 80) / 20 + 1, 4), persistence_rate_pct: null },
      metric_keys: ["average_turnover_pct"],
      evidence_keys: []
    });
  }

  const similarityPercentile = profile.peer_percentiles?.peer_similarity;
  if (finite(similarityPercentile) && Number(profile.peer?.similarity_observation_count ?? 0) >= 8 && similarityPercentile <= 20) {
    candidates.push({
      key: "distinctive",
      noun: "distinctive allocator",
      tone: "distinctive",
      strength: { materiality_ratio: rounded((20 - similarityPercentile) / 20 + 1, 4), persistence_rate_pct: null },
      metric_keys: ["peer_similarity"],
      evidence_keys: []
    });
  }
  if (finite(similarityPercentile) && Number(profile.peer?.similarity_observation_count ?? 0) >= 8 && similarityPercentile >= 80) {
    candidates.push({
      key: "consensus",
      noun: "consensus-aligned allocator",
      tone: "stability",
      strength: { materiality_ratio: rounded((similarityPercentile - 80) / 20 + 1, 4), persistence_rate_pct: null },
      metric_keys: ["peer_similarity"],
      evidence_keys: []
    });
  }
  return candidates.sort(compareCandidates);
}

function decisionProcess(rows) {
  const candidateRows = rows.filter((row) => finite(row.candidate_count));
  const forecastRows = rows.filter((row) => finite(row.average_candidate_forecast_range_pct));
  const confidenceRows = rows.filter((row) => finite(row.submission_confidence));
  const expectedAlphaRows = rows.filter((row) => finite(row.expected_alpha_vs_sp500_pct));
  const keyRiskRows = rows.filter((row) => finite(row.key_risk_count));
  const spyLedgerRows = candidateRows.filter((row) => row.candidate_includes_sp500 === true);
  const coveragePct = (coveredRows) => (rows.length ? rounded((coveredRows.length / rows.length) * 100) : null);
  return {
    eligible_portfolio_count: rows.length,
    structured_candidate_coverage_count: candidateRows.length,
    structured_candidate_coverage_pct: coveragePct(candidateRows),
    average_candidate_count: rounded(average(candidateRows.map((row) => row.candidate_count))),
    average_selected_candidate_count: rounded(average(candidateRows.map((row) => row.selected_candidate_count))),
    sp500_candidate_inclusion_rate_pct: candidateRows.length ? rounded((spyLedgerRows.length / candidateRows.length) * 100) : null,
    candidate_forecast_coverage_count: forecastRows.length,
    candidate_forecast_coverage_pct: coveragePct(forecastRows),
    average_candidate_forecast_range_pct: rounded(average(forecastRows.map((row) => row.average_candidate_forecast_range_pct))),
    expected_alpha_coverage_count: expectedAlphaRows.length,
    expected_alpha_coverage_pct: coveragePct(expectedAlphaRows),
    average_expected_alpha_vs_sp500_pct: rounded(average(expectedAlphaRows.map((row) => row.expected_alpha_vs_sp500_pct))),
    submission_confidence_coverage_count: confidenceRows.length,
    submission_confidence_coverage_pct: coveragePct(confidenceRows),
    average_submission_confidence: rounded(average(confidenceRows.map((row) => row.submission_confidence)), 4),
    key_risk_coverage_count: keyRiskRows.length,
    key_risk_coverage_pct: coveragePct(keyRiskRows),
    average_key_risk_count: rounded(average(keyRiskRows.map((row) => row.key_risk_count)))
  };
}

function evidenceSentence(candidate) {
  const summary = candidate.evidence.overall;
  const direction = candidate.direction === "high" ? "above" : "below";
  const persistence = candidate.direction === "high" ? summary.positive_rate_pct : summary.negative_rate_pct;
  return `${candidate.label} averaged ${formattedValue(candidate.evidence, summary.average_value)}, with a median ${formattedDelta(candidate.evidence, summary.median_delta)} ${direction} same-round peers; the difference had the same direction in ${pct(persistence, 0)} of ${summary.observation_count} matched portfolios.`;
}

function structureSentence(profile) {
  const holdings = profile.metrics?.average_holding_count;
  const top = profile.metrics?.average_top_allocation_pct;
  const turnover = profile.turnover?.average_turnover_pct;
  return `Portfolios averaged ${finite(holdings) ? holdings.toFixed(1) : "n/a"} holdings, a ${pct(top)} largest position, and ${pct(turnover)} turnover.`;
}

function structureEvidence(profile, structure, evidenceByKey) {
  if (!structure) return structureSentence(profile);
  if (structure.key === "concentration" || structure.key === "diversification") {
    const direction = structure.key === "concentration" ? "more concentrated" : "more diversified";
    const supporting = structure.evidence_keys
      .map((key) => evidenceByKey[key])
      .filter(Boolean)
      .map((evidence) => {
        const delta = evidence.overall.median_delta;
        const comparison = Number(delta) >= 0 ? "above" : "below";
        const persistence = Number(delta) >= 0 ? evidence.overall.positive_rate_pct : evidence.overall.negative_rate_pct;
        return `${evidence.label} was a median ${formattedDelta(evidence, delta)} ${comparison} same-round peers with ${pct(persistence, 0)} directional persistence.`;
      });
    return `${structure.noun[0].toUpperCase()}${structure.noun.slice(1)} because the portfolio was persistently ${direction} than same-round peers. ${supporting.join(" ")} ${structureSentence(profile)}`;
  }
  if (structure.key === "high_turnover" || structure.key === "low_turnover") {
    const tail = structure.key === "high_turnover" ? "higher-turnover" : "lower-turnover";
    return `${pct(profile.turnover?.average_turnover_pct)} average turnover across ${profile.turnover?.turnover_observation_count ?? 0} consecutive same-track comparisons places the model in the ${tail} tail of the comparison cohort.`;
  }
  const alignment = structure.key === "distinctive" ? "lower-overlap" : "higher-overlap";
  const similarity = profile.peer?.average_peer_similarity;
  return `${pct(finite(similarity) ? similarity * 100 : null)} average cosine overlap across ${profile.peer?.similarity_observation_count ?? 0} same-round comparisons places the model in the ${alignment} tail of the comparison cohort.`;
}

function confidenceFor({ primary, evidenceByKey }) {
  const matchedPortfolios = Math.max(...Object.values(evidenceByKey).map((row) => row.overall.observation_count), 0);
  const decisionDates = Math.max(...Object.values(evidenceByKey).map((row) => row.overall.decision_date_count), 0);
  const conflicts = Object.values(evidenceByKey).filter((row) => row.track_conflict || row.methodology_conflict);
  if (
    matchedPortfolios < BEHAVIOR_SIGNAL_RULES.minimum_matched_portfolios ||
    decisionDates < BEHAVIOR_SIGNAL_RULES.minimum_independent_decision_dates
  ) {
    return {
      level: "low",
      label: "Provisional",
      reason: `Only ${matchedPortfolios} peer-matched portfolio${matchedPortfolios === 1 ? "" : "s"} across ${decisionDates} independent decision date${decisionDates === 1 ? "" : "s"} are available; stable labels require ${BEHAVIOR_SIGNAL_RULES.minimum_matched_portfolios} and ${BEHAVIOR_SIGNAL_RULES.minimum_independent_decision_dates}, respectively.`
    };
  }
  if (conflicts.some((row) => row.track_conflict)) {
    return {
      level: "low",
      label: "Horizon-dependent",
      reason: "At least one material behavior signal points in opposite directions for weekly and monthly portfolios."
    };
  }
  if (conflicts.some((row) => row.methodology_conflict)) {
    return {
      level: "medium",
      label: "Evolving pattern",
      reason: "At least one material lifetime signal reverses under the current methodology sample."
    };
  }
  if (
    primary &&
    decisionDates >= BEHAVIOR_SIGNAL_RULES.established_minimum_decision_dates &&
    Number(primary.strength?.persistence_rate_pct ?? 0) >= BEHAVIOR_SIGNAL_RULES.established_persistence_rate_pct
  ) {
    return {
      level: "high",
      label: "Established pattern",
      reason: `${decisionDates} independent decision dates and ${pct(primary.strength.persistence_rate_pct, 0)} directional persistence support the primary signal.`
    };
  }
  return {
    level: "medium",
    label: "Moderate evidence",
    reason: `${decisionDates} independent decision dates support comparison, but the leading signal is not yet established.`
  };
}

function currentPill(profile, lifecycleStatus) {
  const historicalTop = profile.recent?.top_assets?.[0];
  if (lifecycleStatus === "retired") {
    return {
      key: "current",
      role: "Lifecycle",
      label: "Historical · retired",
      evidence: historicalTop
        ? `Historical portfolios most recently emphasized ${historicalTop.label}${historicalTop.ticker ? ` (${historicalTop.ticker})` : ""} at ${pct(historicalTop.average_allocation_pct)} average allocation.`
        : "Retired models remain in the historical record but do not enter new official rounds.",
      tone: "sample",
      scope: "historical",
      metric_keys: []
    };
  }
  const hasOpenPortfolio = Number(profile.recent?.active_portfolio_count ?? 0) > 0;
  const top = hasOpenPortfolio ? profile.recent?.current_top_assets?.[0] ?? historicalTop : null;
  if (top) {
    const short = top.ticker || top.label;
    return {
      key: "current",
      role: "Now",
      label: `Now: ${short} ${pct(top.average_allocation_pct, 0)}`,
      evidence: `${top.label}${top.ticker ? ` (${top.ticker})` : ""} is the largest aggregate exposure across currently open official portfolios at ${pct(top.average_allocation_pct)}.`,
      tone: "diversifier",
      scope: "current_open_portfolios",
      metric_keys: ["current_top_asset_pct"]
    };
  }
  return {
    key: "current",
    role: "Now",
    label: "No open portfolio",
    evidence: "This model has no currently open official portfolio.",
    tone: "sample",
    scope: "current_open_portfolios",
    metric_keys: []
  };
}

function pillsFor({ profile, primary, structure, lifecycleStatus, confidence, evidenceByKey }) {
  const signature = primary
    ? {
        key: "signature",
        role: "Signature",
        label: `${primary.short_label} ${formattedValue(primary.evidence, primary.evidence.overall.average_value, 0)} · ${signedDelta(primary.evidence, primary.evidence.overall.median_delta, 0)} vs peers`,
        evidence: evidenceSentence(primary),
        tone: primary.tone,
        scope: "typical_peer_normalized",
        metric_keys: [primary.metric_key]
      }
    : {
        key: "signature",
        role: "Signature",
        label: confidence.label === "Provisional" ? "Pattern still forming" : "Near peer mix",
        evidence:
          confidence.label === "Provisional"
            ? confidence.reason
            : "No exposure or risk dimension cleared the materiality, persistence, and sample gates against same-round peers.",
        tone: confidence.label === "Provisional" ? "sample" : "stability",
        scope: "typical_peer_normalized",
        metric_keys: []
      };
  const construction = {
    key: "construction",
    role: "Construction",
    label: `${finite(profile.metrics?.average_holding_count) ? profile.metrics.average_holding_count.toFixed(1) : "n/a"} holdings · ${pct(profile.metrics?.average_top_allocation_pct, 0)} top`,
    evidence: structureEvidence(profile, structure, evidenceByKey),
    tone: structure?.tone ?? "conviction",
    scope: structure ? "typical_peer_normalized" : "typical",
    metric_keys: ["average_holding_count", "average_top_allocation_pct"]
  };
  const tempo = {
    key: "tempo",
    role: "Tempo",
    label: finite(profile.turnover?.average_turnover_pct) ? `${pct(profile.turnover.average_turnover_pct, 0)} turnover` : "Turnover building",
    evidence: finite(profile.turnover?.average_turnover_pct)
      ? `${pct(profile.turnover.average_turnover_pct)} average one-half absolute allocation change across ${profile.turnover.turnover_observation_count} consecutive same-track comparisons.`
      : "More consecutive same-track portfolios are needed to measure turnover.",
    tone: structure?.key === "high_turnover" ? "distinctive" : "stability",
    scope: "typical",
    metric_keys: ["average_turnover_pct"]
  };
  return [signature, construction, tempo, currentPill(profile, lifecycleStatus)];
}

function traitRows(profile, primary, structure, confidence, evidenceByKey) {
  const rows = [];
  if (primary) {
    rows.push({
      key: primary.key,
      label: `${primary.modifier} signature`,
      evidence: evidenceSentence(primary),
      metric_keys: [primary.metric_key],
      scope: "typical_peer_normalized"
    });
  }
  if (structure) {
    rows.push({
      key: structure.key,
      label: structure.noun[0].toUpperCase() + structure.noun.slice(1),
      evidence: structureEvidence(profile, structure, evidenceByKey),
      metric_keys: structure.metric_keys,
      scope: "typical_peer_normalized"
    });
  }
  rows.push({
    key: "confidence",
    label: confidence.label,
    evidence: confidence.reason,
    metric_keys: ["portfolio_count"],
    scope: "sample"
  });
  return rows;
}

function labelFor(primary, structure, confidence) {
  if (confidence.label === "Provisional") return "Emerging allocation profile";
  if (confidence.label === "Horizon-dependent" && !primary) return "Horizon-dependent allocator";
  if (!primary && !structure) return "Peer-balanced allocator";
  if (primary?.modifier === "Benchmark-anchored" && !structure) return "Benchmark-anchored allocator";
  if (!primary) return structure.noun[0].toUpperCase() + structure.noun.slice(1);
  const noun = structure?.noun ?? "allocator";
  return `${primary.modifier} ${noun}`;
}

function buildProfileV2({ profile, scoredRows, observations, lifecycleStatus }) {
  const evidenceByKey = Object.fromEntries(
    DIMENSIONS.map((definition) => [definition.key, dimensionEvidence(definition, observations.get(definition.key) ?? [])])
  );
  const exposure = exposureCandidates(evidenceByKey);
  const structures = structureCandidates(evidenceByKey, profile);
  const primary = exposure[0] ?? null;
  const structure = structures[0] ?? null;
  const confidence = confidenceFor({ primary, evidenceByKey });
  const label = labelFor(primary, structure, confidence);
  const summary =
    confidence.label === "Provisional"
      ? `Emerging pattern across ${profile.sample?.portfolio_count ?? 0} official portfolios. ${structureSentence(profile)}`
      : `${primary ? evidenceSentence(primary) : "No exposure or risk dimension is persistently far from same-round peer norms."} ${structureSentence(profile)}`;
  const pills = pillsFor({ profile, primary, structure, lifecycleStatus, confidence, evidenceByKey });
  return {
    version: MODEL_BEHAVIOR_VERSION,
    method_version: MODEL_BEHAVIOR_METHOD_VERSION,
    archetype: {
      label,
      description: summary,
      confidence: confidence.level,
      confidence_label: confidence.label,
      confidence_reason: confidence.reason
    },
    behavior_summary: summary,
    primary_signal_key: primary?.key ?? null,
    construction_signal_key: structure?.key ?? null,
    confidence,
    signals: evidenceByKey,
    qualifying_signals: exposure.map((candidate) => ({
      key: candidate.key,
      metric_key: candidate.metric_key,
      direction: candidate.direction,
      modifier: candidate.modifier,
      materiality_ratio: candidate.strength.materiality_ratio,
      persistence_rate_pct: candidate.strength.persistence_rate_pct
    })),
    structure_candidates: structures.map((candidate) => ({
      key: candidate.key,
      label: candidate.noun,
      metric_keys: candidate.metric_keys,
      materiality_ratio: candidate.strength.materiality_ratio
    })),
    traits: traitRows(profile, primary, structure, confidence, evidenceByKey),
    pills,
    decision_process: decisionProcess(scoredRows),
    methodology: {
      comparison_baseline: "leave-one-model-out same-round peer median",
      materiality_policy: "dimension-specific minimum absolute peer difference",
      persistence_policy: `same-direction difference in at least ${BEHAVIOR_SIGNAL_RULES.persistence_rate_pct}% of matched portfolios`,
      sample_policy: `at least ${BEHAVIOR_SIGNAL_RULES.minimum_matched_portfolios} matched portfolios across ${BEHAVIOR_SIGNAL_RULES.minimum_independent_decision_dates} independent decision dates`,
      typical_scope: "all eligible official frozen portfolios",
      current_scope: "currently open eligible official portfolios",
      performance_policy: "realized performance does not determine the allocation-style archetype"
    }
  };
}

export function buildModelBehaviorV2({ profiles, scoredRows, models }) {
  const peerRows = peerObservations(scoredRows);
  const rowsByModel = groupBy(scoredRows, (row) => row.model_id);
  const lifecycleByModel = new Map(models.map((model) => [model.model_id, model.lifecycle_status ?? "active"]));
  return profiles.map((profile) => {
    const behaviorV2 = buildProfileV2({
      profile,
      scoredRows: rowsByModel.get(profile.model_id) ?? [],
      observations: peerRows.get(profile.model_id) ?? new Map(),
      lifecycleStatus: lifecycleByModel.get(profile.model_id) ?? "active"
    });
    return {
      ...profile,
      lifecycle_status: lifecycleByModel.get(profile.model_id) ?? "active",
      archetype: behaviorV2.archetype,
      behavior_v2: behaviorV2
    };
  });
}

export function behaviorMethodologyDefinitions() {
  return {
    version: MODEL_BEHAVIOR_METHOD_VERSION,
    rules: BEHAVIOR_SIGNAL_RULES,
    dimensions: DIMENSIONS.map((definition) => ({
      key: definition.key,
      metric_key: definition.metric_key,
      label: definition.label,
      materiality_floor: definition.materiality_floor,
      unit: definition.unit
    })),
    included_evidence: [
      "eligible official frozen allocations",
      "asset risk and regime definitions",
      "round track, methodology, roster, and lifecycle metadata",
      "same-round peer allocations",
      "structured candidate ledgers, forecasts, confidence, and key-risk counts when available",
      "currently open official portfolios for the Now pill"
    ],
    headline_exclusions: [
      "realized returns and finishing ranks",
      "ineligible, invalid, retrospective, or pilot runs",
      "free-form rationale wording as a classification input",
      "market briefing prose and future information"
    ]
  };
}

export const __test__ = {
  dimensionEvidence,
  observationSummary,
  peerObservations,
  exposureCandidates,
  labelFor
};
