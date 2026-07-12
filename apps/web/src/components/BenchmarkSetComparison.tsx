import { ArrowLeftRight, Download, Info } from "lucide-react";
import { useEffect, useMemo, useState } from "react";

type Track = "weekly" | "monthly";
type Metric = "rank" | "score" | "return" | "alpha";

type SetOption = {
  set_id: string;
  track: Track;
  label: string;
  short_label: string;
  started_at: string | null;
  status: "current" | "qualified" | "forming" | "waiting";
  status_label: string;
  model_count: number;
  shared_round_count: number;
  qualification_threshold: number;
  is_current: boolean;
  is_qualified: boolean;
};

type ModelResult = {
  rank: number;
  score: number | null;
  average_return_pct: number | null;
  average_alpha_pp: number | null;
};

type WindowResult = {
  round_count: number;
  score: number | null;
  average_return_pct: number | null;
  average_alpha_pp: number | null;
};

type ComparisonModel = {
  model_id: string;
  label: string;
  provider: string;
  provider_label: string;
  logo_src: string | null;
  roster_status: "common" | "added" | "removed";
  baseline: ModelResult | null;
  comparison: ModelResult | null;
  rank_change: number | null;
  score_change: number | null;
  windows: {
    same_rounds: WindowResult;
    baseline_only: WindowResult;
    comparison_only: WindowResult;
  };
};

type Comparison = {
  id: string;
  track: Track;
  baseline: SetOption;
  comparison: SetOption;
  rounds: {
    baseline: string[];
    comparison: string[];
    shared: string[];
    baseline_only: string[];
    comparison_only: string[];
    overlap_pct: number | null;
    baseline_excluded: Array<{ round_id: string; missing_model_ids: string[] }>;
    comparison_excluded: Array<{ round_id: string; missing_model_ids: string[] }>;
  };
  models: {
    common_count: number;
    added: string[];
    removed: string[];
    rows: ComparisonModel[];
  };
  ranking: {
    similarity: number | null;
    similarity_pct: number | null;
    similarity_label: string;
    top_three_overlap: number;
    baseline_leader: string | null;
    comparison_leader: string | null;
    same_leader: boolean;
  };
  summary: string;
  trust_guidance: string;
};

interface Props {
  sets: SetOption[];
  comparisons: Comparison[];
  defaults: Record<Track, { baseline: string; comparison: string }>;
}

const METRICS: Array<{ key: Metric; label: string }> = [
  { key: "rank", label: "Rank" },
  { key: "score", label: "Overall score" },
  { key: "return", label: "Average return" },
  { key: "alpha", label: "Return vs S&P 500" }
];

function finiteNumber(value: number | null | undefined): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

function numberLabel(value: number | null | undefined, digits = 1): string {
  return finiteNumber(value) ? value.toFixed(digits) : "n/a";
}

function signedLabel(value: number | null | undefined, suffix = "", digits = 1): string {
  if (!finiteNumber(value)) return "n/a";
  return `${value > 0 ? "+" : ""}${value.toFixed(digits)}${suffix}`;
}

function resultValue(result: ModelResult | null, metric: Metric): number | null {
  if (!result) return null;
  if (metric === "score") return result.score;
  if (metric === "return") return result.average_return_pct;
  if (metric === "alpha") return result.average_alpha_pp;
  return result.rank;
}

function metricValueLabel(value: number | null, metric: Metric): string {
  if (metric === "rank") return finiteNumber(value) ? `#${value}` : "New";
  if (metric === "return") return signedLabel(value, "%", 2);
  if (metric === "alpha") return signedLabel(value, " pp", 2);
  return numberLabel(value, 1);
}

function movementLabel(value: number | null): string {
  if (!finiteNumber(value)) return "New";
  if (value === 0) return "No change";
  return `${value > 0 ? "Up" : "Down"} ${Math.abs(value)}`;
}

function modelInitials(label: string): string {
  return label
    .split(/\s+/)
    .slice(0, 2)
    .map((part) => part[0])
    .join("")
    .toUpperCase();
}

function roundDateLabel(roundId: string): string {
  const match = roundId.match(/^CB-(\d{4})-(\d{2})-(\d{2})-/);
  if (!match) return roundId;
  const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  const month = months[Number(match[2]) - 1];
  return `${month} ${Number(match[3])}, ${match[1]}`;
}

function optionLabel(set: SetOption): string {
  const rounds = `${set.shared_round_count} completed round${set.shared_round_count === 1 ? "" : "s"}`;
  const status = set.status === "forming"
    ? `${set.status_label}, ${Math.max(0, set.qualification_threshold - set.shared_round_count)} more needed`
    : set.status_label;
  return `${set.short_label} — ${status} — ${rounds}`;
}

function setHref(setId: string): string {
  return `/leaderboards/benchmark-sets/${setId}/`;
}

function csvCell(value: string | number | null | undefined): string {
  const text = value === null || value === undefined ? "" : String(value);
  return `"${text.replaceAll('"', '""')}"`;
}

export default function BenchmarkSetComparison({ sets, comparisons, defaults }: Props) {
  const [track, setTrack] = useState<Track>("weekly");
  const [baselineId, setBaselineId] = useState(defaults.weekly.baseline);
  const [comparisonId, setComparisonId] = useState(defaults.weekly.comparison);
  const [metric, setMetric] = useState<Metric>("rank");

  const trackSets = useMemo(() => sets.filter((set) => set.track === track), [sets, track]);
  const comparison = useMemo(
    () => comparisons.find((row) => row.baseline.set_id === baselineId && row.comparison.set_id === comparisonId),
    [comparisons, baselineId, comparisonId]
  );

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const requestedTrack = params.get("track");
    const nextTrack: Track = requestedTrack === "monthly" ? "monthly" : "weekly";
    const requestedBaseline = params.get("base") ?? defaults[nextTrack].baseline;
    const requestedComparison = params.get("compare") ?? defaults[nextTrack].comparison;
    const requestedMetric = params.get("view");
    const validComparison = comparisons.some(
      (row) => row.track === nextTrack && row.baseline.set_id === requestedBaseline && row.comparison.set_id === requestedComparison
    );
    setTrack(nextTrack);
    setBaselineId(validComparison ? requestedBaseline : defaults[nextTrack].baseline);
    setComparisonId(validComparison ? requestedComparison : defaults[nextTrack].comparison);
    if (METRICS.some((item) => item.key === requestedMetric)) setMetric(requestedMetric as Metric);
  }, [comparisons, defaults]);

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    params.set("track", track);
    params.set("base", baselineId);
    params.set("compare", comparisonId);
    params.set("view", metric);
    window.history.replaceState({}, "", `${window.location.pathname}?${params.toString()}`);
  }, [track, baselineId, comparisonId, metric]);

  function changeTrack(nextTrack: Track) {
    setTrack(nextTrack);
    setBaselineId(defaults[nextTrack].baseline);
    setComparisonId(defaults[nextTrack].comparison);
  }

  function changeBaseline(nextId: string) {
    if (nextId === comparisonId) {
      const fallback = trackSets.find((set) => set.set_id !== nextId);
      if (fallback) setComparisonId(fallback.set_id);
    }
    setBaselineId(nextId);
  }

  function changeComparison(nextId: string) {
    if (nextId === baselineId) {
      const fallback = trackSets.find((set) => set.set_id !== nextId);
      if (fallback) setBaselineId(fallback.set_id);
    }
    setComparisonId(nextId);
  }

  function swapSets() {
    setBaselineId(comparisonId);
    setComparisonId(baselineId);
  }

  function downloadCsv() {
    if (!comparison) return;
    const header = [
      "model_id",
      "model",
      "included_in",
      "first_group_rank",
      "second_group_rank",
      "rank_change",
      "first_group_score",
      "second_group_score",
      "score_change",
      "first_group_average_return_pct",
      "second_group_average_return_pct",
      "first_group_return_vs_sp500_pp",
      "second_group_return_vs_sp500_pp"
    ];
    const lines = comparison.models.rows.map((row) =>
      [
        row.model_id,
        row.label,
        row.roster_status === "common"
          ? "both_groups"
          : row.roster_status === "added"
            ? comparison.comparison.short_label
            : comparison.baseline.short_label,
        row.baseline?.rank,
        row.comparison?.rank,
        row.rank_change,
        row.baseline?.score,
        row.comparison?.score,
        row.score_change,
        row.baseline?.average_return_pct,
        row.comparison?.average_return_pct,
        row.baseline?.average_alpha_pp,
        row.comparison?.average_alpha_pp
      ]
        .map(csvCell)
        .join(",")
    );
    const blob = new Blob([[header.join(","), ...lines].join("\n")], { type: "text/csv;charset=utf-8" });
    const href = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = href;
    anchor.download = `${comparison.baseline.set_id}-vs-${comparison.comparison.set_id}.csv`;
    anchor.click();
    URL.revokeObjectURL(href);
  }

  if (!comparison) return null;

  const rankedRows = comparison.models.rows.filter((row) => row.baseline || row.comparison);
  const numericValues = rankedRows
    .flatMap((row) => [resultValue(row.baseline, metric), resultValue(row.comparison, metric)])
    .filter(finiteNumber);
  const numericDomain = Math.max(1, ...numericValues.map((value) => Math.abs(value)));
  const addedLabels = comparison.models.rows.filter((row) => row.roster_status === "added").map((row) => row.label);
  const removedLabels = comparison.models.rows.filter((row) => row.roster_status === "removed").map((row) => row.label);
  const roundUnionCount =
    comparison.rounds.shared.length + comparison.rounds.baseline_only.length + comparison.rounds.comparison_only.length;
  const hasPerformance = comparison.baseline.shared_round_count > 0 && comparison.comparison.shared_round_count > 0;
  const addedText = addedLabels.length ? `${addedLabels.length} only in ${comparison.comparison.short_label}` : null;
  const removedText = removedLabels.length ? `${removedLabels.length} only in ${comparison.baseline.short_label}` : null;
  const modelDifferenceText = [addedText, removedText].filter(Boolean).join("; ") || "The same models are included";
  const extraRoundText = [
    comparison.rounds.baseline_only.length
      ? `${comparison.baseline.short_label} has ${comparison.rounds.baseline_only.length} more`
      : null,
    comparison.rounds.comparison_only.length
      ? `${comparison.comparison.short_label} has ${comparison.rounds.comparison_only.length} more`
      : null
  ].filter(Boolean).join("; ") || "Both use the same rounds";
  const roundExplanation = [
    `${comparison.rounds.shared.length} completed round${comparison.rounds.shared.length === 1 ? " is" : "s are"} used by both groups.`,
    comparison.rounds.baseline_only.length
      ? `${comparison.baseline.short_label} also uses ${comparison.rounds.baseline_only.length} other round${comparison.rounds.baseline_only.length === 1 ? "" : "s"}.`
      : null,
    comparison.rounds.comparison_only.length
      ? `${comparison.comparison.short_label} also uses ${comparison.rounds.comparison_only.length} other round${comparison.rounds.comparison_only.length === 1 ? "" : "s"}.`
      : null,
    "Different rounds can change scores and ranks."
  ].filter(Boolean).join(" ");
  const modelLabelsById = new Map(comparison.models.rows.map((row) => [row.model_id, row.label]));
  const excludedGroups = Array.from(
    comparison.rounds.comparison_excluded.reduce((groups, round) => {
      const missingLabels = round.missing_model_ids.map((modelId) => modelLabelsById.get(modelId) ?? modelId).sort();
      const key = missingLabels.join("|");
      const group = groups.get(key) ?? { missingLabels, roundIds: [] as string[] };
      group.roundIds.push(round.round_id);
      groups.set(key, group);
      return groups;
    }, new Map<string, { missingLabels: string[]; roundIds: string[] }>()).values()
  );
  const excludedRoundCount = comparison.rounds.comparison_excluded.length;
  const excludedExplanation = excludedRoundCount === 0
    ? `No. Every possible ${comparison.comparison.short_label} round had a result from every model in the group.`
    : excludedGroups.length === 1 && excludedGroups[0].roundIds.length === excludedRoundCount
      ? `All ${excludedRoundCount} rounds were left out because ${excludedGroups[0].missingLabels.join(" and ")} had no recorded result. To keep the ranking fair, those rounds were left out for every model in ${comparison.comparison.short_label}.`
      : `${excludedRoundCount} rounds were left out because at least one model in ${comparison.comparison.short_label} had no recorded result. A round counts only when every model in the group has a result.`;

  return (
    <div className={`set-compare-workspace set-compare-${track}`}>
      <section className="set-compare-controls" aria-labelledby="set-compare-controls-title">
        <div className="set-compare-control-head">
          <div>
            <span className="panel-kicker">Choose two groups</span>
            <h2 id="set-compare-controls-title">Which results do you want to compare?</h2>
          </div>
          <p>A round is one timed market test. A model group uses only rounds completed by every model being ranked together.</p>
        </div>
        <div className="set-compare-track-tabs" role="tablist" aria-label="Round length">
          {(["weekly", "monthly"] as Track[]).map((item) => (
            <button
              type="button"
              role="tab"
              aria-selected={track === item}
              className={track === item ? "is-active" : ""}
              onClick={() => changeTrack(item)}
              key={item}
            >
              {item === "weekly" ? "Weekly rounds" : "Monthly rounds"}
            </button>
          ))}
        </div>
        <label>
          <span>First model group</span>
          <select value={baselineId} onChange={(event) => changeBaseline(event.target.value)}>
            {trackSets.map((set) => (
              <option value={set.set_id} key={set.set_id}>{optionLabel(set)}</option>
            ))}
          </select>
        </label>
        <button type="button" className="set-compare-swap" onClick={swapSets} aria-label="Switch the first and second model groups">
          <ArrowLeftRight size={18} aria-hidden="true" />
          <span>Switch order</span>
        </button>
        <label>
          <span>Second model group</span>
          <select value={comparisonId} onChange={(event) => changeComparison(event.target.value)}>
            {trackSets.map((set) => (
              <option value={set.set_id} key={set.set_id}>{optionLabel(set)}</option>
            ))}
          </select>
        </label>
      </section>

      <section className="set-compare-answer" aria-labelledby="set-compare-answer-title">
        <div>
          <span className="panel-kicker">Bottom line</span>
          <h2 id="set-compare-answer-title">What changed?</h2>
          <p>{comparison.summary}</p>
        </div>
        <div className="set-compare-status-pair" aria-label="Selected model groups">
          <a href={setHref(comparison.baseline.set_id)}>
            <span>{comparison.baseline.status_label}</span>
            <strong>{comparison.baseline.short_label}</strong>
            <em>{comparison.baseline.shared_round_count} rounds completed by all {comparison.baseline.model_count} models</em>
          </a>
          <a href={setHref(comparison.comparison.set_id)}>
            <span>{comparison.comparison.status_label}</span>
            <strong>{comparison.comparison.short_label}</strong>
            <em>{comparison.comparison.shared_round_count} rounds completed by all {comparison.comparison.model_count} models</em>
          </a>
        </div>
      </section>

      <section className="set-compare-summary" aria-label="Comparison summary">
        <article>
          <span>Models in both groups</span>
          <strong>{comparison.models.common_count}</strong>
          <em>{modelDifferenceText}</em>
        </article>
        <article>
          <span>Rounds used by both</span>
          <strong>{comparison.rounds.shared.length}</strong>
          <em>{extraRoundText}</em>
        </article>
        <article>
          <span className="set-compare-label-with-info">
            Did the order change?
            <span className="set-compare-info" tabIndex={0} aria-label="We compare the order of models that appear in both groups. 'Changed a lot' means those models moved substantially relative to one another.">
              <Info size={14} aria-hidden="true" />
            </span>
          </span>
          <strong>{comparison.ranking.similarity_label}</strong>
          <em>{hasPerformance ? "Based on models in both groups" : "Waiting for results"}</em>
        </article>
        <article>
          <span>Did the top model change?</span>
          <strong>{hasPerformance ? (comparison.ranking.same_leader ? "No" : "Yes") : "Not available"}</strong>
          <em>{hasPerformance ? `${comparison.ranking.top_three_overlap} of 3 stayed in the top three` : "Waiting for results"}</em>
        </article>
      </section>

      {!hasPerformance ? (
        <section className="set-compare-waiting" aria-labelledby="set-compare-waiting-title">
          <span className="panel-kicker">What is available</span>
          <h2 id="set-compare-waiting-title">What can you compare right now?</h2>
          <p>{comparison.trust_guidance}</p>
          <div className="set-compare-roster-change">
            {addedLabels.length > 0 && <span><strong>Only in {comparison.comparison.short_label}:</strong> {addedLabels.join(", ")}</span>}
            {removedLabels.length > 0 && <span><strong>Only in {comparison.baseline.short_label}:</strong> {removedLabels.join(", ")}</span>}
          </div>
        </section>
      ) : (
        <>
          <section className="set-compare-rankings" aria-labelledby="set-compare-rankings-title">
            <div className="set-compare-section-head">
              <div>
                <span className="panel-kicker">Model by model</span>
                <div className="set-compare-heading-with-info">
                  <h2 id="set-compare-rankings-title">How did each model's result change?</h2>
                  <span className="set-compare-info" tabIndex={0} aria-label="Overall score compares a model's total return with the best return available in the same rounds. Higher is better.">
                    <Info size={14} aria-hidden="true" />
                  </span>
                </div>
                <p>Each group uses all of its completed rounds. Models that appear in only one group are marked clearly.</p>
              </div>
              <div className="set-compare-metric-tabs" role="tablist" aria-label="Comparison metric">
                {METRICS.map((item) => (
                  <button
                    type="button"
                    role="tab"
                    aria-selected={metric === item.key}
                    className={metric === item.key ? "is-active" : ""}
                    onClick={() => setMetric(item.key)}
                    key={item.key}
                  >
                    {item.label}
                  </button>
                ))}
              </div>
            </div>

            {metric === "rank" ? (
              <div className="set-compare-rank-lanes">
                <div className="set-compare-rank-head" aria-hidden="true">
                  <span>{comparison.baseline.short_label} rank</span>
                  <span>Model</span>
                  <span>{comparison.comparison.short_label} rank</span>
                  <span>Change</span>
                </div>
                {rankedRows.map((row) => (
                  <div className={`set-compare-rank-row is-${row.roster_status}`} key={row.model_id}>
                    <strong>
                      <span className="set-compare-mobile-column-label">{comparison.baseline.short_label}</span>
                      {row.baseline ? `#${row.baseline.rank}` : "Not included"}
                    </strong>
                    <span className="set-compare-model">
                      {row.logo_src ? <img src={row.logo_src} alt="" /> : <span>{modelInitials(row.label)}</span>}
                      <span>
                        <b>{row.label}</b>
                        <em>
                          {row.roster_status === "added"
                            ? `Only in ${comparison.comparison.short_label}`
                            : row.roster_status === "removed"
                              ? `Only in ${comparison.baseline.short_label}`
                              : row.provider_label}
                        </em>
                      </span>
                    </span>
                    <strong>
                      <span className="set-compare-mobile-column-label">{comparison.comparison.short_label}</span>
                      {row.comparison ? `#${row.comparison.rank}` : "Not included"}
                    </strong>
                    <em className={finiteNumber(row.rank_change) && row.rank_change > 0 ? "is-up" : finiteNumber(row.rank_change) && row.rank_change < 0 ? "is-down" : ""}>
                      {row.roster_status === "common" ? movementLabel(row.rank_change) : row.roster_status === "added" ? "Added" : "Not included"}
                    </em>
                  </div>
                ))}
              </div>
            ) : (
              <div className="set-compare-paired-bars">
                <div className="set-compare-bar-key" aria-hidden="true">
                  <span className="is-baseline">{comparison.baseline.short_label}</span>
                  <span className="is-comparison">{comparison.comparison.short_label}</span>
                </div>
                {rankedRows.map((row) => {
                  const baselineValue = resultValue(row.baseline, metric);
                  const comparisonValue = resultValue(row.comparison, metric);
                  const baselineWidth = finiteNumber(baselineValue) ? (Math.abs(baselineValue) / numericDomain) * 48 : 0;
                  const comparisonWidth = finiteNumber(comparisonValue) ? (Math.abs(comparisonValue) / numericDomain) * 48 : 0;
                  return (
                    <div className="set-compare-bar-row" key={row.model_id}>
                      <span className="set-compare-model">
                        {row.logo_src ? <img src={row.logo_src} alt="" /> : <span>{modelInitials(row.label)}</span>}
                        <b>{row.label}</b>
                      </span>
                      <div className="set-compare-pair-track" aria-label={`${row.label}: ${comparison.baseline.short_label} ${metricValueLabel(baselineValue, metric)}, ${comparison.comparison.short_label} ${metricValueLabel(comparisonValue, metric)}`}>
                        <span className="set-compare-zero" />
                        {finiteNumber(baselineValue) && (
                          <span className="set-compare-pair-bar is-baseline" style={{ left: `${baselineValue < 0 ? 50 - baselineWidth : 50}%`, width: `${baselineWidth}%` }} />
                        )}
                        {finiteNumber(comparisonValue) && (
                          <span className="set-compare-pair-bar is-comparison" style={{ left: `${comparisonValue < 0 ? 50 - comparisonWidth : 50}%`, width: `${comparisonWidth}%` }} />
                        )}
                      </div>
                      <span className="set-compare-values">
                        <em>{metricValueLabel(baselineValue, metric)}</em>
                        <strong>{metricValueLabel(comparisonValue, metric)}</strong>
                      </span>
                    </div>
                  );
                })}
              </div>
            )}
          </section>

          <section className="set-compare-rounds" aria-labelledby="set-compare-rounds-title">
            <div className="set-compare-section-head">
              <div>
                <span className="panel-kicker">Fair comparison</span>
                <h2 id="set-compare-rounds-title">Did both groups use the same rounds?</h2>
                <p>{roundExplanation}</p>
              </div>
            </div>
            <div className="set-compare-round-timeline" aria-label="Rounds used by each model group">
              {roundUnionCount > 0 && (
                <>
                  <span className="is-shared" style={{ width: `${(comparison.rounds.shared.length / roundUnionCount) * 100}%` }} />
                  <span className="is-baseline-only" style={{ width: `${(comparison.rounds.baseline_only.length / roundUnionCount) * 100}%` }} />
                  <span className="is-comparison-only" style={{ width: `${(comparison.rounds.comparison_only.length / roundUnionCount) * 100}%` }} />
                </>
              )}
            </div>
            <div className="set-compare-round-key">
              <span className="is-shared"><strong>{comparison.rounds.shared.length}</strong> used by both</span>
              <span className="is-baseline-only"><strong>{comparison.rounds.baseline_only.length}</strong> only in {comparison.baseline.short_label}</span>
              <span className="is-comparison-only"><strong>{comparison.rounds.comparison_only.length}</strong> only in {comparison.comparison.short_label}</span>
            </div>
            <div className="set-compare-window-table">
              {comparison.models.rows.filter((row) => row.roster_status === "common").map((row) => (
                <div key={row.model_id}>
                  <span className="set-compare-model">
                    {row.logo_src ? <img src={row.logo_src} alt="" /> : <span>{modelInitials(row.label)}</span>}
                    <b>{row.label}</b>
                  </span>
                  <span><em>Overall score on {comparison.rounds.shared.length} shared rounds</em><strong>{numberLabel(row.windows.same_rounds.score)}</strong></span>
                  <span><em>Overall score on {comparison.rounds.baseline_only.length} other {comparison.baseline.short_label} rounds</em><strong>{numberLabel(row.windows.baseline_only.score)}</strong></span>
                  <span><em>Overall score on all {comparison.baseline.shared_round_count} {comparison.baseline.short_label} rounds</em><strong>{numberLabel(row.baseline?.score)}</strong></span>
                </div>
              ))}
            </div>
            <div className="set-compare-audit-details">
              <details>
                <summary>See exactly which rounds were used</summary>
                <div>
                  <p><strong>Used by both:</strong> {comparison.rounds.shared.join(", ") || "None"}</p>
                  <p><strong>Only in {comparison.baseline.short_label}:</strong> {comparison.rounds.baseline_only.join(", ") || "None"}</p>
                  <p><strong>Only in {comparison.comparison.short_label}:</strong> {comparison.rounds.comparison_only.join(", ") || "None"}</p>
                </div>
              </details>
              <details>
                <summary>
                  {excludedRoundCount > 0
                    ? `Why were ${excludedRoundCount} rounds left out of ${comparison.comparison.short_label}?`
                    : `Were any ${comparison.comparison.short_label} rounds left out?`}
                </summary>
                <div>
                  <p className="set-compare-exclusion-explanation">{excludedExplanation}</p>
                  {excludedGroups.map((group) => (
                    <p key={group.missingLabels.join("|")}>
                      <strong>{group.missingLabels.join(" and ")} had no result:</strong>{" "}
                      {group.roundIds.map(roundDateLabel).join(", ")}
                    </p>
                  ))}
                </div>
              </details>
            </div>
          </section>

          <section className="set-compare-trust" aria-labelledby="set-compare-trust-title">
            <div>
              <span className="panel-kicker">What this means</span>
              <h2 id="set-compare-trust-title">Which results should you rely on?</h2>
              <p>{comparison.trust_guidance}</p>
            </div>
            <div className="set-compare-actions">
              <a href={setHref(comparison.baseline.set_id)}>Open {comparison.baseline.short_label}</a>
              <a href={setHref(comparison.comparison.set_id)}>Open {comparison.comparison.short_label}</a>
              <button type="button" onClick={downloadCsv}>
                <Download size={16} aria-hidden="true" />
                Download results
              </button>
            </div>
          </section>

          <section className="set-compare-table-section" aria-labelledby="set-compare-table-title">
            <div className="set-compare-section-head">
              <div>
                <span className="panel-kicker">All results</span>
                <h2 id="set-compare-table-title">What are all the numbers?</h2>
              </div>
            </div>
            <div className="table-wrap">
              <table className="set-compare-table">
                <thead>
                  <tr>
                    <th>Model</th>
                    <th>Included in</th>
                    <th>{comparison.baseline.short_label} rank</th>
                    <th>{comparison.comparison.short_label} rank</th>
                    <th>Change</th>
                    <th>{comparison.baseline.short_label} overall score</th>
                    <th>{comparison.comparison.short_label} overall score</th>
                    <th>Overall score change</th>
                  </tr>
                </thead>
                <tbody>
                  {comparison.models.rows.map((row) => (
                    <tr key={row.model_id}>
                      <td><strong>{row.label}</strong><small>{row.provider_label}</small></td>
                      <td>
                        {row.roster_status === "common"
                          ? "Both groups"
                          : row.roster_status === "added"
                            ? `Only ${comparison.comparison.short_label}`
                            : `Only ${comparison.baseline.short_label}`}
                      </td>
                      <td>{row.baseline ? `#${row.baseline.rank}` : "—"}</td>
                      <td>{row.comparison ? `#${row.comparison.rank}` : "—"}</td>
                      <td>{row.roster_status === "common" ? movementLabel(row.rank_change) : row.roster_status === "added" ? "Added" : "Not included"}</td>
                      <td>{numberLabel(row.baseline?.score)}</td>
                      <td>{numberLabel(row.comparison?.score)}</td>
                      <td>{signedLabel(row.score_change)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        </>
      )}
    </div>
  );
}
