import { ChevronDown } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { modelLabel, providerLabel, type RoundRecord, type SubmissionRecord, type UniverseOption } from "../data/fallback";
import { decisionAllocations, optionDisplayName, optionShortDisplayName, type OptionLabelMap } from "../lib/allocations";

type ActiveTrack = "all" | "weekly" | "monthly";
type ActiveView = "asset" | "model";
type RoundTrack = "weekly" | "monthly" | "other";

type ActiveExposureRound = {
  round: Pick<RoundRecord, "round_id" | "title" | "entry_date" | "exit_date" | "status" | "official_run_id">;
  track: RoundTrack;
  submissions: SubmissionRecord[];
  options: UniverseOption[];
};

type ExposureGroup =
  | "AI & Technology"
  | "US Equity"
  | "International Equity"
  | "Commodities"
  | "Bonds, Cash & FX"
  | "Crypto"
  | "Other";

type ExposureContribution = {
  optionId: string;
  allocationBps: number;
  portfolioKey: string;
  modelId: string;
  provider: string;
  roundId: string;
  track: "weekly" | "monthly";
};

type AssetExposure = {
  optionId: string;
  exposurePct: number;
  totalBps: number;
  group: ExposureGroup;
  portfolios: Set<string>;
  contributions: ExposureContribution[];
  trackBps: Record<"weekly" | "monthly", number>;
};

type ModelAssetExposure = {
  optionId: string;
  exposurePct: number;
  totalBps: number;
  group: ExposureGroup;
};

type ModelExposure = {
  modelId: string;
  provider: string;
  portfolioCount: number;
  portfolioKeys: Set<string>;
  roundIds: Set<string>;
  trackCounts: Record<"weekly" | "monthly", number>;
  assets: ModelAssetExposure[];
  groups: Array<{ group: ExposureGroup; exposurePct: number }>;
  topAsset?: ModelAssetExposure;
  topGroup?: { group: ExposureGroup; exposurePct: number };
  concentrationScore: number;
};

interface Props {
  rounds: ActiveExposureRound[];
}

const GROUP_ORDER: ExposureGroup[] = [
  "AI & Technology",
  "US Equity",
  "International Equity",
  "Commodities",
  "Bonds, Cash & FX",
  "Crypto",
  "Other"
];
const TRACK_OPTIONS: Array<{ key: ActiveTrack; label: string }> = [
  { key: "all", label: "All Active" },
  { key: "weekly", label: "Weekly" },
  { key: "monthly", label: "Monthly" }
];
const VIEW_OPTIONS: Array<{ key: ActiveView; label: string }> = [
  { key: "asset", label: "By Asset" },
  { key: "model", label: "By Model" }
];
const HOLDER_PREVIEW_LIMIT = 5;
const TOP_ASSET_LIMIT = 10;
const MODEL_HOLDING_LIMIT = 4;

function formatPct(value: number): string {
  if (!Number.isFinite(value)) return "0%";
  if (value >= 10) return `${value.toFixed(1)}%`;
  if (value >= 1) return `${value.toFixed(1)}%`;
  if (value > 0) return `${value.toFixed(2)}%`;
  return "0%";
}

function groupForOption(optionId: string, option?: UniverseOption): ExposureGroup {
  const id = optionId.toUpperCase();
  const assetClass = option?.asset_class.toLowerCase() ?? "";
  const group = option?.option_group.toLowerCase() ?? "";
  const combined = `${assetClass} ${group}`;

  if (option?.is_cash || /cash|treasury|bond|fixed|credit|currency|dollar|duration|tips/.test(combined)) {
    return "Bonds, Cash & FX";
  }
  if (/commodity|energy|oil|gold|metal|agriculture|copper|silver/.test(combined)) return "Commodities";
  if (/crypto|bitcoin|ethereum/.test(combined)) return "Crypto";
  if (/international|developed|emerging|europe|japan|china|india|country|global ex/.test(combined)) {
    return "International Equity";
  }
  if (
    ["SEMICONDUCTORS", "TECHNOLOGY", "SOFTWARE", "NASDAQ100", "LARGE_GROWTH", "COMMUNICATIONS"].includes(id) ||
    /technology|software|semiconductor|growth/.test(combined)
  ) {
    return "AI & Technology";
  }
  if (/equity|stock|market|sector|style|factor/.test(combined)) return "US Equity";
  return "Other";
}

function groupClass(group: ExposureGroup): string {
  return group
    .toLowerCase()
    .replaceAll("&", "and")
    .replaceAll(",", "")
    .replaceAll(" ", "-");
}

function optionMaps(rounds: ActiveExposureRound[]): OptionLabelMap {
  const entries = new Map<string, UniverseOption>();
  for (const round of rounds) {
    for (const option of round.options) {
      if (!entries.has(option.option_id)) entries.set(option.option_id, option);
    }
  }
  return Object.fromEntries(entries);
}

function visibleTrack(track: RoundTrack): track is "weekly" | "monthly" {
  return track === "weekly" || track === "monthly";
}

function buildExposure(rounds: ActiveExposureRound[], selectedTrack: ActiveTrack) {
  const visibleRounds = rounds.filter((round) => visibleTrack(round.track) && (selectedTrack === "all" || round.track === selectedTrack));
  const optionsById = optionMaps(visibleRounds);
  const assets = new Map<string, AssetExposure>();
  const portfolioKeys = new Set<string>();
  const trackPortfolioCounts = { weekly: 0, monthly: 0 };

  for (const round of visibleRounds) {
    if (!visibleTrack(round.track)) continue;
    trackPortfolioCounts[round.track] += round.submissions.length;
    for (const submission of round.submissions) {
      const portfolioKey = `${round.round.round_id}:${submission.run_id}:${submission.model_id}`;
      portfolioKeys.add(portfolioKey);
      const perAsset = new Map<string, number>();
      for (const allocation of decisionAllocations(submission)) {
        if (!allocation.option_id || allocation.allocation_bps <= 0) continue;
        perAsset.set(allocation.option_id, (perAsset.get(allocation.option_id) ?? 0) + allocation.allocation_bps);
      }

      for (const [optionId, allocationBps] of perAsset.entries()) {
        const option = optionsById[optionId] as UniverseOption | undefined;
        const group = groupForOption(optionId, option);
        const existing =
          assets.get(optionId) ??
          ({
            optionId,
            exposurePct: 0,
            totalBps: 0,
            group,
            portfolios: new Set<string>(),
            contributions: [],
            trackBps: { weekly: 0, monthly: 0 }
          } satisfies AssetExposure);
        existing.totalBps += allocationBps;
        existing.trackBps[round.track] += allocationBps;
        existing.portfolios.add(portfolioKey);
        existing.contributions.push({
          optionId,
          allocationBps,
          portfolioKey,
          modelId: submission.model_id,
          provider: submission.provider,
          roundId: round.round.round_id,
          track: round.track
        });
        assets.set(optionId, existing);
      }
    }
  }

  const portfolioCount = portfolioKeys.size;
  const denominatorBps = portfolioCount * 10_000;
  const assetList = Array.from(assets.values())
    .map((asset) => ({
      ...asset,
      exposurePct: denominatorBps > 0 ? (asset.totalBps / denominatorBps) * 100 : 0
    }))
    .sort((a, b) => b.exposurePct - a.exposurePct);

  const groups = GROUP_ORDER.map((group) => {
    const groupAssets = assetList.filter((asset) => asset.group === group);
    return {
      group,
      exposurePct: groupAssets.reduce((total, asset) => total + asset.exposurePct, 0),
      assets: groupAssets
    };
  }).filter((group) => group.exposurePct > 0);

  return {
    visibleRounds,
    optionsById,
    portfolioCount,
    trackPortfolioCounts,
    assets: assetList,
    groups
  };
}

function buildModelExposure(rounds: ActiveExposureRound[], selectedTrack: ActiveTrack) {
  const visibleRounds = rounds.filter((round) => visibleTrack(round.track) && (selectedTrack === "all" || round.track === selectedTrack));
  const optionsById = optionMaps(visibleRounds);
  const modelRows = new Map<
    string,
    {
      modelId: string;
      provider: string;
      portfolioKeys: Set<string>;
      roundIds: Set<string>;
      trackCounts: Record<"weekly" | "monthly", number>;
      assetBps: Map<string, number>;
    }
  >();

  for (const round of visibleRounds) {
    if (!visibleTrack(round.track)) continue;
    for (const submission of round.submissions) {
      const modelKey = `${submission.provider}:${submission.model_id}`;
      const existing =
        modelRows.get(modelKey) ??
        ({
          modelId: submission.model_id,
          provider: submission.provider,
          portfolioKeys: new Set<string>(),
          roundIds: new Set<string>(),
          trackCounts: { weekly: 0, monthly: 0 },
          assetBps: new Map<string, number>()
        } satisfies {
          modelId: string;
          provider: string;
          portfolioKeys: Set<string>;
          roundIds: Set<string>;
          trackCounts: Record<"weekly" | "monthly", number>;
          assetBps: Map<string, number>;
        });

      const portfolioKey = `${round.round.round_id}:${submission.run_id}:${submission.model_id}`;
      existing.portfolioKeys.add(portfolioKey);
      existing.roundIds.add(round.round.round_id);
      existing.trackCounts[round.track] += 1;

      const perAsset = new Map<string, number>();
      for (const allocation of decisionAllocations(submission)) {
        if (!allocation.option_id || allocation.allocation_bps <= 0) continue;
        perAsset.set(allocation.option_id, (perAsset.get(allocation.option_id) ?? 0) + allocation.allocation_bps);
      }
      for (const [optionId, allocationBps] of perAsset.entries()) {
        existing.assetBps.set(optionId, (existing.assetBps.get(optionId) ?? 0) + allocationBps);
      }

      modelRows.set(modelKey, existing);
    }
  }

  const models: ModelExposure[] = Array.from(modelRows.values())
    .map((model) => {
      const portfolioCount = model.portfolioKeys.size;
      const denominatorBps = portfolioCount * 10_000;
      const assets = Array.from(model.assetBps.entries())
        .map(([optionId, totalBps]) => {
          const option = optionsById[optionId] as UniverseOption | undefined;
          return {
            optionId,
            totalBps,
            exposurePct: denominatorBps > 0 ? (totalBps / denominatorBps) * 100 : 0,
            group: groupForOption(optionId, option)
          };
        })
        .sort((a, b) => b.exposurePct - a.exposurePct);
      const groups = GROUP_ORDER.map((group) => ({
        group,
        exposurePct: assets.filter((asset) => asset.group === group).reduce((total, asset) => total + asset.exposurePct, 0)
      }))
        .filter((group) => group.exposurePct > 0)
        .sort((a, b) => b.exposurePct - a.exposurePct);
      return {
        modelId: model.modelId,
        provider: model.provider,
        portfolioCount,
        portfolioKeys: model.portfolioKeys,
        roundIds: model.roundIds,
        trackCounts: model.trackCounts,
        assets,
        groups,
        topAsset: assets[0],
        topGroup: groups[0],
        concentrationScore: assets.reduce((total, asset) => total + (asset.exposurePct / 100) ** 2, 0)
      };
    })
    .sort(
      (a, b) =>
        providerLabel(a.provider).localeCompare(providerLabel(b.provider)) ||
        modelLabel(a.modelId).localeCompare(modelLabel(b.modelId))
    );

  const sharedTopAssets = new Map<string, { count: number; totalPct: number }>();
  for (const model of models) {
    if (!model.topAsset) continue;
    const current = sharedTopAssets.get(model.topAsset.optionId) ?? { count: 0, totalPct: 0 };
    current.count += 1;
    current.totalPct += model.topAsset.exposurePct;
    sharedTopAssets.set(model.topAsset.optionId, current);
  }
  const sharedTopHolding = Array.from(sharedTopAssets.entries())
    .map(([optionId, value]) => ({
      optionId,
      count: value.count,
      averagePct: value.count > 0 ? value.totalPct / value.count : 0
    }))
    .sort((a, b) => b.count - a.count || b.averagePct - a.averagePct)[0];
  const mostConcentrated = [...models].sort((a, b) => b.concentrationScore - a.concentrationScore)[0];
  const mostDiversified = [...models].filter((model) => model.assets.length > 0).sort((a, b) => a.concentrationScore - b.concentrationScore)[0];

  return {
    visibleRounds,
    optionsById,
    models,
    sharedTopHolding,
    mostConcentrated,
    mostDiversified
  };
}

function topModelSegments(model: ModelExposure) {
  const topAssets = model.assets.slice(0, MODEL_HOLDING_LIMIT);
  const otherPct = model.assets.slice(MODEL_HOLDING_LIMIT).reduce((total, asset) => total + asset.exposurePct, 0);
  return otherPct > 0
    ? [...topAssets, { optionId: "OTHER", exposurePct: otherPct, totalBps: 0, group: "Other" as ExposureGroup }]
    : topAssets;
}

function trackLabel(track: ActiveTrack): string {
  if (track === "weekly") return "Weekly";
  if (track === "monthly") return "Monthly";
  return "All Active";
}

export default function ActiveExposureMap({ rounds }: Props) {
  const [track, setTrack] = useState<ActiveTrack>("all");
  const [view, setView] = useState<ActiveView>("asset");
  const [selectedGroup, setSelectedGroup] = useState<ExposureGroup | "all">("all");
  const [selectedOptionId, setSelectedOptionId] = useState<string | null>(null);
  const [showAllHolders, setShowAllHolders] = useState(false);
  const [expandedModelKey, setExpandedModelKey] = useState<string | null>(null);
  const summary = useMemo(() => buildExposure(rounds, track), [rounds, track]);
  const modelSummary = useMemo(() => buildModelExposure(rounds, track), [rounds, track]);
  const selectedAsset = summary.assets.find((asset) => asset.optionId === selectedOptionId) ?? summary.assets[0];
  const leadingGroup = [...summary.groups].sort((a, b) => b.exposurePct - a.exposurePct)[0];
  const largestExposure = summary.assets[0];
  const sharedTopHolding = modelSummary.sharedTopHolding;
  const focusedAssets = selectedGroup === "all" ? summary.assets : summary.assets.filter((asset) => asset.group === selectedGroup);
  const rankedAssets = focusedAssets.slice(0, TOP_ASSET_LIMIT);
  const remainingAssets = focusedAssets.slice(TOP_ASSET_LIMIT);
  const remainingExposure = remainingAssets.reduce((total, asset) => total + asset.exposurePct, 0);
  const holderRows = selectedAsset ? [...selectedAsset.contributions].sort((a, b) => b.allocationBps - a.allocationBps) : [];
  const visibleHolderRows = showAllHolders ? holderRows : holderRows.slice(0, HOLDER_PREVIEW_LIMIT);
  const modelPortfolioScope = track === "all" ? "open weekly and monthly" : `open ${track}`;

  useEffect(() => {
    if (summary.assets.length === 0) {
      setSelectedOptionId(null);
      return;
    }
    if (!selectedOptionId || !summary.assets.some((asset) => asset.optionId === selectedOptionId)) {
      setSelectedOptionId(summary.assets[0].optionId);
    }
  }, [selectedOptionId, summary.assets]);

  useEffect(() => {
    setShowAllHolders(false);
  }, [selectedOptionId, track, view]);

  useEffect(() => {
    setExpandedModelKey(null);
  }, [track, view]);

  if (rounds.length === 0) {
    return (
      <div className="active-exposure-empty">
        <strong>No active portfolios are waiting for scores.</strong>
        <span>Completed tests are excluded from this view.</span>
      </div>
    );
  }

  return (
    <div className="active-exposure-shell">
      <div className="active-exposure-hero">
        <div className="active-exposure-hero-copy">
          <div className="active-exposure-toolbar">
            <div className="active-exposure-control-cluster">
              <div className="active-exposure-control">
                <span>Scope</span>
                <div className="active-exposure-tabs" aria-label="Filter active exposure by track">
                  {TRACK_OPTIONS.map((option) => (
                    <button
                      key={option.key}
                      className={track === option.key ? "is-active" : ""}
                      type="button"
                      onClick={() => {
                        setTrack(option.key);
                        setSelectedGroup("all");
                      }}
                      aria-pressed={track === option.key}
                    >
                      {option.label}
                    </button>
                  ))}
                </div>
              </div>
              <div className="active-exposure-control">
                <span>View</span>
                <div className="active-exposure-tabs active-exposure-view-tabs" aria-label="Choose active exposure view">
                  {VIEW_OPTIONS.map((option) => (
                    <button
                      key={option.key}
                      className={view === option.key ? "is-active" : ""}
                      type="button"
                      onClick={() => setView(option.key)}
                      aria-pressed={view === option.key}
                    >
                      {option.label}
                    </button>
                  ))}
                </div>
              </div>
            </div>
            <span>{trackLabel(track)} portfolios only</span>
          </div>
          <span className="panel-kicker">Active capital map</span>
          <h3>
            {view === "model"
              ? "Where each model's open portfolios are invested."
              : largestExposure && leadingGroup
              ? `${optionDisplayName(largestExposure.optionId, summary.optionsById)} is the largest active allocation.`
              : "No active model capital is allocated yet."}
          </h3>
          <p>
            {view === "model"
              ? `Each row averages that model's ${modelPortfolioScope} portfolios into one live allocation. Completed tests are excluded.`
              : largestExposure && leadingGroup
              ? `${formatPct(largestExposure.exposurePct)} is allocated to ${optionDisplayName(
                  largestExposure.optionId,
                  summary.optionsById
                )}, while ${leadingGroup.group} accounts for ${formatPct(leadingGroup.exposurePct)} of open portfolios.`
              : "When active tests are waiting for final prices, their current allocations appear here."}
          </p>
        </div>

        <div className="active-exposure-stat-grid" aria-label="Active exposure summary">
          {view === "asset" ? (
            <>
              <div>
                <span>Largest asset</span>
                <strong>{largestExposure ? optionShortDisplayName(largestExposure.optionId, summary.optionsById) : "None"}</strong>
                <small>{largestExposure ? formatPct(largestExposure.exposurePct) : "0%"}</small>
              </div>
              <div>
                <span>Lead category</span>
                <strong>{leadingGroup?.group ?? "None"}</strong>
                <small>{leadingGroup ? formatPct(leadingGroup.exposurePct) : "0%"}</small>
              </div>
              <div>
                <span>Active tests</span>
                <strong>{summary.visibleRounds.length}</strong>
                <small>{trackLabel(track)}</small>
              </div>
              <div>
                <span>Portfolios</span>
                <strong>{summary.portfolioCount}</strong>
                <small>{summary.assets.length} assets held</small>
              </div>
            </>
          ) : (
            <>
              <div>
                <span>Models</span>
                <strong>{modelSummary.models.length}</strong>
                <small>{trackLabel(track)}</small>
              </div>
              <div>
                <span>Shared top holding</span>
                <strong>{sharedTopHolding ? optionShortDisplayName(sharedTopHolding.optionId, modelSummary.optionsById) : "None"}</strong>
                <small>
                  {sharedTopHolding ? `${sharedTopHolding.count} of ${modelSummary.models.length} models` : "No common top asset"}
                </small>
              </div>
              <div>
                <span>Most concentrated</span>
                <strong>{modelSummary.mostConcentrated ? modelLabel(modelSummary.mostConcentrated.modelId) : "None"}</strong>
                <small>
                  {modelSummary.mostConcentrated?.topAsset
                    ? `${optionShortDisplayName(
                        modelSummary.mostConcentrated.topAsset.optionId,
                        modelSummary.optionsById
                      )} ${formatPct(modelSummary.mostConcentrated.topAsset.exposurePct)}`
                    : "No active holdings"}
                </small>
              </div>
              <div>
                <span>Most diversified</span>
                <strong>{modelSummary.mostDiversified ? modelLabel(modelSummary.mostDiversified.modelId) : "None"}</strong>
                <small>{modelSummary.mostDiversified ? `${modelSummary.mostDiversified.assets.length} assets held` : "No active holdings"}</small>
              </div>
            </>
          )}
        </div>
      </div>

      {summary.portfolioCount > 0 ? (
        <div className="active-exposure-content">
          {view === "asset" ? (
            <>
          <section className="active-exposure-ribbon-panel" aria-labelledby="active-category-title">
            <div className="active-exposure-panel-head">
              <div>
                <span className="metric-label">Category mix</span>
                <strong id="active-category-title">Click a category to focus the exposure list</strong>
              </div>
              {selectedGroup !== "all" && (
                <button className="active-exposure-clear" type="button" onClick={() => setSelectedGroup("all")}>
                  All categories
                </button>
              )}
            </div>
            <div className="active-exposure-ribbon" aria-label="Active model capital by asset category">
              {summary.groups.map((group) => (
                <button
                  key={group.group}
                  className={`active-exposure-segment exposure-${groupClass(group.group)} ${selectedGroup === group.group ? "is-selected" : ""}`}
                  type="button"
                  style={{ flexGrow: Math.max(group.exposurePct, 1) }}
                  onClick={() => setSelectedGroup(selectedGroup === group.group ? "all" : group.group)}
                  aria-pressed={selectedGroup === group.group}
                  title={`${group.group}: ${formatPct(group.exposurePct)}`}
                >
                  <strong>{group.group}</strong>
                  <span>{formatPct(group.exposurePct)}</span>
                </button>
              ))}
            </div>
          </section>

          <div className="active-exposure-layout">
            <section className="active-exposure-ranking" aria-label="Ranked active asset exposures">
              <div className="active-exposure-ranking-head">
                <div>
                  <span className="metric-label">{selectedGroup === "all" ? "Top exposures" : selectedGroup}</span>
                  <strong>{selectedGroup === "all" ? "Assets with the most active model capital" : "Assets in selected category"}</strong>
                </div>
                <span>{focusedAssets.length} assets</span>
              </div>

              <div className="active-exposure-bars">
                {rankedAssets.map((asset) => (
                  <button
                    key={asset.optionId}
                    type="button"
                    className={selectedAsset?.optionId === asset.optionId ? "is-selected" : ""}
                    onClick={() => setSelectedOptionId(asset.optionId)}
                  >
                    <span className={`active-exposure-dot exposure-${groupClass(asset.group)}`} aria-hidden="true" />
                    <span className="active-exposure-bar-label">
                      <strong>{optionDisplayName(asset.optionId, summary.optionsById)}</strong>
                      <small>{asset.group}</small>
                    </span>
                    <span className="active-exposure-rank-bar" aria-hidden="true">
                      <span className={`exposure-${groupClass(asset.group)}`} style={{ width: `${Math.max(2, asset.exposurePct)}%` }} />
                    </span>
                    <span className="active-exposure-bar-value">{formatPct(asset.exposurePct)}</span>
                  </button>
                ))}
                {remainingAssets.length > 0 && (
                  <div className="active-exposure-other-row">
                    <span>{remainingAssets.length} smaller active exposures</span>
                    <strong>{formatPct(remainingExposure)}</strong>
                  </div>
                )}
              </div>
            </section>

            <aside className="active-exposure-detail" aria-live="polite">
              {selectedAsset ? (
                <>
                  <div className="active-exposure-detail-head">
                    <span className={`active-exposure-dot exposure-${groupClass(selectedAsset.group)}`} aria-hidden="true" />
                    <div>
                      <span>{selectedAsset.group}</span>
                      <strong>{optionDisplayName(selectedAsset.optionId, summary.optionsById)}</strong>
                    </div>
                  </div>
                  <div className="active-exposure-detail-number">
                    <strong>{formatPct(selectedAsset.exposurePct)}</strong>
                    <span>of active model capital</span>
                  </div>
                  <div className="active-exposure-split">
                    <div>
                      <span>Held by</span>
                      <strong>
                        {selectedAsset.portfolios.size} of {summary.portfolioCount}
                      </strong>
                    </div>
                    <div>
                      <span>Weekly share</span>
                      <strong>
                        {formatPct(
                          summary.trackPortfolioCounts.weekly > 0
                            ? (selectedAsset.trackBps.weekly / (summary.trackPortfolioCounts.weekly * 10_000)) * 100
                            : 0
                        )}
                      </strong>
                    </div>
                    <div>
                      <span>Monthly share</span>
                      <strong>
                        {formatPct(
                          summary.trackPortfolioCounts.monthly > 0
                            ? (selectedAsset.trackBps.monthly / (summary.trackPortfolioCounts.monthly * 10_000)) * 100
                            : 0
                        )}
                      </strong>
                    </div>
                  </div>
                  <div className="active-exposure-holder-list">
                    <div className="active-exposure-holder-head">
                      <span className="metric-label">Largest model positions</span>
                      <span>
                        {Math.min(visibleHolderRows.length, holderRows.length)} of {holderRows.length}
                      </span>
                    </div>
                    {visibleHolderRows.map((contribution) => (
                      <div key={`${contribution.portfolioKey}:${contribution.optionId}`}>
                        <div>
                          <strong>{modelLabel(contribution.modelId)}</strong>
                          <span>
                            {providerLabel(contribution.provider)} / {contribution.roundId}
                          </span>
                        </div>
                        <span>{formatPct(contribution.allocationBps / 100)}</span>
                      </div>
                    ))}
                    {holderRows.length > HOLDER_PREVIEW_LIMIT && (
                      <button className="active-exposure-expand" type="button" onClick={() => setShowAllHolders(!showAllHolders)}>
                        {showAllHolders ? "Show fewer holders" : `Show all ${holderRows.length} holders`}
                        <ChevronDown size={14} aria-hidden="true" />
                      </button>
                    )}
                  </div>
                </>
              ) : (
                <div className="pending-state compact">
                  <strong>No active allocation selected.</strong>
                  <span>Choose a track with pending model portfolios.</span>
                </div>
              )}
            </aside>
          </div>
            </>
          ) : (
            <section className="active-model-panel" aria-labelledby="active-model-title">
              <div className="active-exposure-panel-head active-model-panel-head">
                <div>
                  <span className="metric-label">Live model allocation profiles</span>
                  <strong id="active-model-title">How each model is positioned across active tests</strong>
                  <p>Each model's {modelPortfolioScope} portfolios are averaged into one profile. Completed tests are not counted.</p>
                </div>
                <span>{modelSummary.models.length} models</span>
              </div>

              <div className="active-model-insights" aria-label="Model allocation highlights">
                <div>
                  <span>Most common top asset</span>
                  <strong>{sharedTopHolding ? optionShortDisplayName(sharedTopHolding.optionId, modelSummary.optionsById) : "None"}</strong>
                  <small>
                    {sharedTopHolding ? `${sharedTopHolding.count} models lead with it` : "No active top holding"}
                  </small>
                </div>
                <div>
                  <span>Highest concentration</span>
                  <strong>{modelSummary.mostConcentrated ? modelLabel(modelSummary.mostConcentrated.modelId) : "None"}</strong>
                  <small>
                    {modelSummary.mostConcentrated?.topAsset
                      ? `${formatPct(modelSummary.mostConcentrated.topAsset.exposurePct)} in ${optionShortDisplayName(
                          modelSummary.mostConcentrated.topAsset.optionId,
                          modelSummary.optionsById
                        )}`
                      : "No active holdings"}
                  </small>
                </div>
                <div>
                  <span>Broadest allocation</span>
                  <strong>{modelSummary.mostDiversified ? modelLabel(modelSummary.mostDiversified.modelId) : "None"}</strong>
                  <small>{modelSummary.mostDiversified ? `${modelSummary.mostDiversified.assets.length} assets held` : "No active holdings"}</small>
                </div>
              </div>

              <div className="active-model-grid">
                {modelSummary.models.map((model) => {
                  const modelKey = `${model.provider}:${model.modelId}`;
                  const segments = topModelSegments(model);
                  const expanded = expandedModelKey === modelKey;
                  return (
                    <article className={`active-model-card ${expanded ? "is-expanded" : ""}`} key={modelKey}>
                      <div className="active-model-card-head">
                        <div>
                          <span>{providerLabel(model.provider)}</span>
                          <strong>{modelLabel(model.modelId)}</strong>
                        </div>
                        <span>{model.portfolioCount} active</span>
                      </div>

                      <div className="active-model-meta">
                        <div>
                          <span>Top category</span>
                          <strong>{model.topGroup ? `${model.topGroup.group} ${formatPct(model.topGroup.exposurePct)}` : "None"}</strong>
                        </div>
                        <div>
                          <span>Largest holding</span>
                          <strong>
                            {model.topAsset
                              ? `${optionShortDisplayName(model.topAsset.optionId, modelSummary.optionsById)} ${formatPct(model.topAsset.exposurePct)}`
                              : "None"}
                          </strong>
                        </div>
                      </div>

                      <div className="active-model-stack" aria-label={`${modelLabel(model.modelId)} live aggregate allocation`}>
                        {segments.map((segment) => (
                          <span
                            key={segment.optionId}
                            className={`exposure-${groupClass(segment.group)}`}
                            style={{ width: `${Math.max(segment.exposurePct, 2)}%` }}
                            title={`${
                              segment.optionId === "OTHER"
                                ? "Other holdings"
                                : optionDisplayName(segment.optionId, modelSummary.optionsById)
                            }: ${formatPct(segment.exposurePct)}`}
                          />
                        ))}
                      </div>

                      <div className="active-model-top-list" aria-label={`${modelLabel(model.modelId)} largest active holdings`}>
                        {segments.slice(0, 4).map((segment) => (
                          <div key={segment.optionId}>
                            <span className={`active-exposure-dot exposure-${groupClass(segment.group)}`} aria-hidden="true" />
                            <span>{segment.optionId === "OTHER" ? "Other holdings" : optionDisplayName(segment.optionId, modelSummary.optionsById)}</span>
                            <strong>{formatPct(segment.exposurePct)}</strong>
                          </div>
                        ))}
                      </div>

                      <button
                        className="active-model-toggle"
                        type="button"
                        onClick={() => setExpandedModelKey(expanded ? null : modelKey)}
                        aria-expanded={expanded}
                      >
                        {expanded ? "Hide allocation details" : "Show allocation details"}
                        <ChevronDown size={14} aria-hidden="true" />
                      </button>

                      {expanded && (
                        <div className="active-model-details">
                          <div className="active-model-track-split">
                            <div>
                              <span>Weekly portfolios</span>
                              <strong>{model.trackCounts.weekly}</strong>
                            </div>
                            <div>
                              <span>Monthly portfolios</span>
                              <strong>{model.trackCounts.monthly}</strong>
                            </div>
                          </div>

                          <div className="active-model-rounds">
                            <span>Included rounds</span>
                            <div>
                              {Array.from(model.roundIds).map((roundId) => (
                                <a href={`/rounds/${roundId}/`} key={roundId}>
                                  {roundId}
                                </a>
                              ))}
                            </div>
                          </div>

                          <div className="active-model-allocation-list">
                            {model.assets.map((asset) => (
                              <div key={asset.optionId}>
                                <span>
                                  {optionDisplayName(asset.optionId, modelSummary.optionsById)}
                                  <small>{asset.group}</small>
                                </span>
                                <strong>{formatPct(asset.exposurePct)}</strong>
                              </div>
                            ))}
                          </div>
                        </div>
                      )}
                    </article>
                  );
                })}
              </div>
            </section>
          )}
        </div>
      ) : (
        <div className="active-exposure-empty">
          <strong>No active portfolios in this filter.</strong>
          <span>Try All Active or wait for another test to be locked.</span>
        </div>
      )}
    </div>
  );
}
