import { ChevronDown } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { modelLabel, providerLabel, type RoundRecord, type SubmissionRecord, type UniverseOption } from "../data/fallback";
import { decisionAllocations, optionDisplayName, optionShortDisplayName, type OptionLabelMap } from "../lib/allocations";

type ActiveTrack = "all" | "weekly" | "monthly";
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
const HOLDER_PREVIEW_LIMIT = 5;
const TOP_ASSET_LIMIT = 10;

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

function trackLabel(track: ActiveTrack): string {
  if (track === "weekly") return "Weekly";
  if (track === "monthly") return "Monthly";
  return "All Active";
}

export default function ActiveExposureMap({ rounds }: Props) {
  const [track, setTrack] = useState<ActiveTrack>("all");
  const [selectedGroup, setSelectedGroup] = useState<ExposureGroup | "all">("all");
  const [selectedOptionId, setSelectedOptionId] = useState<string | null>(null);
  const [showAllHolders, setShowAllHolders] = useState(false);
  const summary = useMemo(() => buildExposure(rounds, track), [rounds, track]);
  const selectedAsset = summary.assets.find((asset) => asset.optionId === selectedOptionId) ?? summary.assets[0];
  const leadingGroup = [...summary.groups].sort((a, b) => b.exposurePct - a.exposurePct)[0];
  const largestExposure = summary.assets[0];
  const focusedAssets = selectedGroup === "all" ? summary.assets : summary.assets.filter((asset) => asset.group === selectedGroup);
  const rankedAssets = focusedAssets.slice(0, TOP_ASSET_LIMIT);
  const remainingAssets = focusedAssets.slice(TOP_ASSET_LIMIT);
  const remainingExposure = remainingAssets.reduce((total, asset) => total + asset.exposurePct, 0);
  const holderRows = selectedAsset ? [...selectedAsset.contributions].sort((a, b) => b.allocationBps - a.allocationBps) : [];
  const visibleHolderRows = showAllHolders ? holderRows : holderRows.slice(0, HOLDER_PREVIEW_LIMIT);

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
  }, [selectedOptionId, track]);

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
            <span>{trackLabel(track)} portfolios only</span>
          </div>
          <span className="panel-kicker">Active capital map</span>
          <h3>
            {largestExposure && leadingGroup
              ? `${optionDisplayName(largestExposure.optionId, summary.optionsById)} is the largest active allocation.`
              : "No active model capital is allocated yet."}
          </h3>
          <p>
            {largestExposure && leadingGroup
              ? `${formatPct(largestExposure.exposurePct)} is allocated to ${optionDisplayName(
                  largestExposure.optionId,
                  summary.optionsById
                )}, while ${leadingGroup.group} accounts for ${formatPct(leadingGroup.exposurePct)} of open portfolios.`
              : "When active tests are waiting for final prices, their current allocations appear here."}
          </p>
        </div>

        <div className="active-exposure-stat-grid" aria-label="Active exposure summary">
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
        </div>
      </div>

      {summary.portfolioCount > 0 ? (
        <div className="active-exposure-content">
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
