import { modelLabel, providerLabel, type LeaderboardRecord, type RoundRecord, type SubmissionRecord, type UniverseOption } from "../data/fallback";
import { allocationThemeClass, decisionAllocations, optionDisplayName, optionShortDisplayName } from "./allocations";
import {
  staticOfficialSubmissions,
  staticRoundLeaderboard,
  staticRoundRecords,
  staticUniverseOptions
} from "./localRoundRecords";
import { roundTrack, trackLabel, type BenchmarkTrack } from "./tracks";

export type ModelScopeKey = "all" | BenchmarkTrack;

export type ModelLiveRound = {
  roundId: string;
  track: BenchmarkTrack;
  exitDate: string;
  scoreEtaUtc?: string;
};

export type ModelHoldingRound = ModelLiveRound & {
  allocationPct: number;
};

export type ModelLiveHolding = {
  optionId: string;
  label: string;
  shortLabel: string;
  symbol: string;
  group: string;
  themeClass: string;
  exposurePct: number;
  portfolioCount: number;
  rounds: ModelHoldingRound[];
};

export type ModelLiveScope = {
  key: ModelScopeKey;
  label: string;
  portfolioCount: number;
  roundCount: number;
  weeklyPortfolioCount: number;
  monthlyPortfolioCount: number;
  holdings: ModelLiveHolding[];
  topHolding?: ModelLiveHolding;
  topThreePct: number;
  nextScoreDate?: string;
  activeRounds: ModelLiveRound[];
};

export type ModelTrackScore = {
  track: BenchmarkTrack;
  completedTests: number;
  wins: number;
  hitRate: number | null;
  averageReturn: number | null;
  averageSp500Return: number | null;
  averageAlpha: number | null;
  averageRank: number | null;
  bestRound?: ModelResultRow;
  worstRound?: ModelResultRow;
};

export type ModelResultRow = {
  roundId: string;
  runId: string;
  track: BenchmarkTrack;
  entryDate: string;
  exitDate: string;
  modelRank: number;
  modelCount: number;
  portfolioReturn: number | null;
  sp500Return: number | null;
  alphaVsSp500: number | null;
  primaryPick: string;
  holdingCount?: number;
};

export type ModelFingerprintAsset = {
  optionId: string;
  label: string;
  shortLabel: string;
  symbol: string;
  group: string;
  frequencyPct: number;
  averageAllocationPct: number;
  topPickCount: number;
};

export type ModelFingerprintCategory = {
  group: string;
  averageAllocationPct: number;
};

export type ModelRiskAppetite = {
  score: number | null;
  percentile: number | null;
  label: string;
  description: string;
  highRiskPct: number;
  defensivePct: number;
  techPct: number;
};

export type ModelFingerprint = {
  portfolioCount: number;
  averageHoldingCount: number | null;
  averageTopHoldingPct: number | null;
  riskAppetite: ModelRiskAppetite;
  mostCommonTopHolding?: ModelFingerprintAsset;
  assets: ModelFingerprintAsset[];
  categories: ModelFingerprintCategory[];
};

export type ModelRoundHistoryRow = {
  roundId: string;
  runId: string;
  track: BenchmarkTrack;
  entryDate: string;
  exitDate: string;
  status: RoundRecord["status"];
  portfolioLabel: string;
  portfolioSummary: Array<{
    optionId: string;
    label: string;
    allocationPct: number;
    themeClass: string;
  }>;
  rationale: string;
  keyRisks: string[];
  result?: ModelResultRow;
  parsedPath: string;
  rawPath: string;
};

export type ModelProfile = {
  modelId: string;
  label: string;
  provider: string;
  providerLabel: string;
  logoSrc?: string;
  iconSrc?: string;
  firstDecisionDate?: string;
  tracksEntered: BenchmarkTrack[];
  live: Record<ModelScopeKey, ModelLiveScope>;
  scorecards: Record<BenchmarkTrack, ModelTrackScore>;
  allResults: ModelResultRow[];
  fingerprint: ModelFingerprint;
  history: ModelRoundHistoryRow[];
};

type RoundContext = {
  round: RoundRecord;
  track: BenchmarkTrack;
  optionsById: Record<string, UniverseOption | undefined>;
  submissions: SubmissionRecord[];
  leaderboard: LeaderboardRecord[];
};

const PROVIDER_LOGOS: Record<string, string> = {
  anthropic: "/labs/icons/claude-icon.svg",
  google: "/labs/icons/gemini-icon.svg",
  openai: "/labs/icons/openai-icon.svg",
  xai: "/labs/icons/xai-icon.svg"
};

const PROVIDER_ICONS: Record<string, string> = PROVIDER_LOGOS;

const GROUP_LABELS: Record<string, string> = {
  ai_and_technology: "AI and Technology",
  bonds_and_rates: "Bonds and Rates",
  cash: "Cash",
  cash_and_short_duration: "Cash and Short Duration",
  clean_energy: "Clean Energy",
  commodities: "Commodities",
  country_equity: "Country Equity",
  credit: "Credit",
  crypto: "Crypto",
  currencies: "Currencies",
  international_equity: "International Equity",
  us_broad_market: "US Broad Market",
  us_factor_equity: "US Factor Equity",
  us_growth_and_technology: "US Growth and Technology",
  us_industry: "US Industry",
  us_sector: "US Sector",
  us_size_factor: "US Size Factor",
  us_style_factor: "US Style Factor"
};

const TECH_OPTION_IDS = new Set(["NASDAQ100", "LARGE_GROWTH", "TECHNOLOGY", "SEMICONDUCTORS", "SOFTWARE"]);
const DEFENSIVE_OPTION_IDS = new Set([
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

function percentFromBps(bps: number, denominatorBps: number): number {
  if (denominatorBps <= 0) return 0;
  return (bps / denominatorBps) * 100;
}

function average(values: Array<number | null | undefined>): number | null {
  const finite = values.filter((value): value is number => typeof value === "number" && Number.isFinite(value));
  if (finite.length === 0) return null;
  return finite.reduce((total, value) => total + value, 0) / finite.length;
}

function clampPercent(value: number): number {
  if (!Number.isFinite(value)) return 0;
  return Math.min(100, Math.max(0, value));
}

function riskBucketScore(option: UniverseOption | undefined): number {
  if (!option) return 3;
  if (option.is_cash) return 1;
  const group = option.option_group.toLowerCase();
  if (group === "crypto" || option.asset_class.toLowerCase() === "crypto") return 5;
  switch (option.risk_bucket.toLowerCase()) {
    case "cash":
      return 1;
    case "low":
      return 2;
    case "medium":
      return 3;
    case "high":
      return 4;
    case "very_high":
    case "very-high":
    case "speculative":
      return 5;
    default:
      return 3;
  }
}

function isDefensiveOption(optionId: string, option: UniverseOption | undefined): boolean {
  if (DEFENSIVE_OPTION_IDS.has(optionId)) return true;
  if (option?.is_cash) return true;
  const group = option?.option_group.toLowerCase() ?? "";
  return group.includes("cash") || group.includes("bond") || group.includes("credit");
}

function isTechnologyOption(optionId: string, option: UniverseOption | undefined): boolean {
  if (TECH_OPTION_IDS.has(optionId)) return true;
  const group = option?.option_group.toLowerCase() ?? "";
  const name = option?.name.toLowerCase() ?? "";
  return group.includes("technology") || group.includes("ai") || name.includes("technology") || name.includes("software");
}

function riskAppetiteLabel(score: number | null): string {
  if (score === null) return "Not enough history";
  if (score < 2.15) return "Defensive";
  if (score < 3.15) return "Balanced";
  if (score < 4.15) return "Growth";
  return "Aggressive";
}

function riskAppetiteDescription(label: string): string {
  if (label === "Defensive") return "Usually favors cash, bonds, gold, or lower-volatility exposure.";
  if (label === "Balanced") return "Mixes equity risk with defensive ballast.";
  if (label === "Growth") return "Usually favors equities, sectors, or thematic growth exposure.";
  if (label === "Aggressive") return "Frequently leans into high-beta or narrow thematic exposure.";
  return "Calculated after the model has at least one saved official portfolio.";
}

function buildRiskAppetite(
  score: number | null,
  denominatorBps: number,
  highRiskBps: number,
  defensiveBps: number,
  techBps: number
): ModelRiskAppetite {
  const label = riskAppetiteLabel(score);
  return {
    score,
    percentile: score === null ? null : clampPercent(((score - 1) / 4) * 100),
    label,
    description: riskAppetiteDescription(label),
    highRiskPct: percentFromBps(highRiskBps, denominatorBps),
    defensivePct: percentFromBps(defensiveBps, denominatorBps),
    techPct: percentFromBps(techBps, denominatorBps)
  };
}

function optionGroup(optionId: string, optionsById: Record<string, UniverseOption | undefined>): string {
  const option = optionsById[optionId];
  if (!option?.option_group) return "Other";
  const normalized = option.option_group.toLowerCase();
  if (GROUP_LABELS[normalized]) return GROUP_LABELS[normalized];
  return option.option_group
    .replaceAll("_", " ")
    .split(" ")
    .filter(Boolean)
    .map((part) => part[0]?.toUpperCase() + part.slice(1))
    .join(" ");
}

function roundContexts(roundRows = staticRoundRecords()): RoundContext[] {
  return roundRows
    .map((round) => {
      const track = roundTrack(round);
      if (track !== "weekly" && track !== "monthly") return null;
      const submissions = staticOfficialSubmissions(round.round_id, round.official_run_id);
      if (submissions.length === 0) return null;
      const options = staticUniverseOptions(round.round_id);
      const optionsById: Record<string, UniverseOption | undefined> = Object.fromEntries(options.map((option) => [option.option_id, option]));
      return {
        round,
        track,
        optionsById,
        submissions,
        leaderboard: staticRoundLeaderboard(round.round_id, round.official_run_id)
      };
    })
    .filter((context): context is RoundContext => context !== null);
}

function portfolioAllocations(submission: SubmissionRecord): Array<{ optionId: string; allocationBps: number; allocationPct: number }> {
  const perAsset = new Map<string, number>();
  for (const allocation of decisionAllocations(submission)) {
    if (!allocation.option_id || allocation.allocation_bps <= 0) continue;
    perAsset.set(allocation.option_id, (perAsset.get(allocation.option_id) ?? 0) + allocation.allocation_bps);
  }
  return Array.from(perAsset.entries())
    .map(([optionId, allocationBps]) => ({ optionId, allocationBps, allocationPct: allocationBps / 100 }))
    .sort((a, b) => b.allocationBps - a.allocationBps);
}

function buildLiveScope(modelId: string, contexts: RoundContext[], scope: ModelScopeKey): ModelLiveScope {
  const scopedContexts = contexts.filter(
    (context) => context.round.status === "pending" && (scope === "all" || context.track === scope)
  );
  const holdings = new Map<
    string,
    {
      totalBps: number;
      portfolioKeys: Set<string>;
      rounds: ModelHoldingRound[];
      optionsById: Record<string, UniverseOption | undefined>;
    }
  >();
  const portfolioKeys = new Set<string>();
  const activeRounds = new Map<string, ModelLiveRound>();
  let weeklyPortfolioCount = 0;
  let monthlyPortfolioCount = 0;

  for (const context of scopedContexts) {
    const modelSubmissions = context.submissions.filter((submission) => submission.model_id === modelId);
    if (modelSubmissions.length === 0) continue;
    activeRounds.set(context.round.round_id, {
      roundId: context.round.round_id,
      track: context.track,
      exitDate: context.round.exit_date,
      scoreEtaUtc: context.round.score_eta_utc
    });
    if (context.track === "weekly") weeklyPortfolioCount += modelSubmissions.length;
    if (context.track === "monthly") monthlyPortfolioCount += modelSubmissions.length;

    for (const submission of modelSubmissions) {
      const portfolioKey = `${context.round.round_id}:${submission.run_id}:${submission.model_id}`;
      portfolioKeys.add(portfolioKey);
      for (const allocation of portfolioAllocations(submission)) {
        const existing =
          holdings.get(allocation.optionId) ??
          ({
            totalBps: 0,
            portfolioKeys: new Set<string>(),
            rounds: [],
            optionsById: context.optionsById
          } satisfies {
            totalBps: number;
            portfolioKeys: Set<string>;
            rounds: ModelHoldingRound[];
            optionsById: Record<string, UniverseOption | undefined>;
          });
        existing.totalBps += allocation.allocationBps;
        existing.portfolioKeys.add(portfolioKey);
        existing.optionsById = { ...existing.optionsById, ...context.optionsById };
        existing.rounds.push({
          roundId: context.round.round_id,
          track: context.track,
          exitDate: context.round.exit_date,
          scoreEtaUtc: context.round.score_eta_utc,
          allocationPct: allocation.allocationPct
        });
        holdings.set(allocation.optionId, existing);
      }
    }
  }

  const denominatorBps = portfolioKeys.size * 10_000;
  const holdingRows = Array.from(holdings.entries())
    .map(([optionId, holding]) => ({
      optionId,
      label: optionDisplayName(optionId, holding.optionsById),
      shortLabel: optionShortDisplayName(optionId, holding.optionsById),
      symbol: holding.optionsById[optionId]?.symbol ?? "",
      group: optionGroup(optionId, holding.optionsById),
      themeClass: allocationThemeClass(optionId),
      exposurePct: percentFromBps(holding.totalBps, denominatorBps),
      portfolioCount: holding.portfolioKeys.size,
      rounds: holding.rounds.sort((a, b) => b.roundId.localeCompare(a.roundId))
    }))
    .sort((a, b) => b.exposurePct - a.exposurePct || a.label.localeCompare(b.label));
  const activeRoundRows = Array.from(activeRounds.values()).sort((a, b) => a.exitDate.localeCompare(b.exitDate));
  const nextScoreDate = activeRoundRows
    .map((round) => round.scoreEtaUtc ?? (round.exitDate ? `${round.exitDate}T23:30:00Z` : undefined))
    .filter((value): value is string => Boolean(value))
    .sort()[0];

  return {
    key: scope,
    label: scope === "all" ? "All Live" : trackLabel(scope),
    portfolioCount: portfolioKeys.size,
    roundCount: activeRoundRows.length,
    weeklyPortfolioCount,
    monthlyPortfolioCount,
    holdings: holdingRows,
    topHolding: holdingRows[0],
    topThreePct: holdingRows.slice(0, 3).reduce((total, holding) => total + holding.exposurePct, 0),
    nextScoreDate,
    activeRounds: activeRoundRows
  };
}

function buildResults(modelId: string, contexts: RoundContext[]): ModelResultRow[] {
  const rows: ModelResultRow[] = [];
  for (const context of contexts) {
    if (context.leaderboard.length === 0) continue;
    const resultIndex = context.leaderboard.findIndex((row) => row.model_id === modelId);
    if (resultIndex < 0) continue;
    const row = context.leaderboard[resultIndex];
    rows.push({
      roundId: context.round.round_id,
      runId: row.run_id ?? context.round.official_run_id,
      track: context.track,
      entryDate: context.round.entry_date,
      exitDate: context.round.exit_date,
      modelRank: resultIndex + 1,
      modelCount: context.leaderboard.length,
      portfolioReturn: row.portfolio_return ?? row.selected_asset_return ?? null,
      sp500Return: row.sp500_return ?? null,
      alphaVsSp500: row.alpha_vs_sp500 ?? null,
      primaryPick: row.selected_option_id ?? "",
      holdingCount: row.holding_count
    });
  }
  return rows.sort((a, b) => b.exitDate.localeCompare(a.exitDate));
}

function buildTrackScore(track: BenchmarkTrack, results: ModelResultRow[]): ModelTrackScore {
  const trackRows = results.filter((row) => row.track === track);
  const completedTests = trackRows.length;
  const wins = trackRows.filter((row) => row.modelRank === 1).length;
  const hitCount = trackRows.filter((row) => typeof row.alphaVsSp500 === "number" && row.alphaVsSp500 > 0).length;
  const sortedByAlpha = [...trackRows].sort((a, b) => Number(b.alphaVsSp500 ?? -Infinity) - Number(a.alphaVsSp500 ?? -Infinity));
  return {
    track,
    completedTests,
    wins,
    hitRate: completedTests > 0 ? hitCount / completedTests : null,
    averageReturn: average(trackRows.map((row) => row.portfolioReturn)),
    averageSp500Return: average(trackRows.map((row) => row.sp500Return)),
    averageAlpha: average(trackRows.map((row) => row.alphaVsSp500)),
    averageRank: average(trackRows.map((row) => row.modelRank)),
    bestRound: sortedByAlpha[0],
    worstRound: sortedByAlpha.at(-1)
  };
}

function buildFingerprint(modelId: string, contexts: RoundContext[]): ModelFingerprint {
  const assetRows = new Map<
    string,
    {
      totalBps: number;
      portfolioKeys: Set<string>;
      topPickCount: number;
      optionsById: Record<string, UniverseOption | undefined>;
    }
  >();
  const categoryBps = new Map<string, number>();
  const portfolioKeys = new Set<string>();
  const holdingCounts: number[] = [];
  const topHoldingBps: number[] = [];
  const portfolioRiskScores: number[] = [];
  let totalPortfolioBps = 0;
  let highRiskBps = 0;
  let defensiveBps = 0;
  let techBps = 0;

  for (const context of contexts) {
    for (const submission of context.submissions.filter((row) => row.model_id === modelId)) {
      const portfolioKey = `${context.round.round_id}:${submission.run_id}:${submission.model_id}`;
      const allocations = portfolioAllocations(submission);
      if (allocations.length === 0) continue;
      portfolioKeys.add(portfolioKey);
      holdingCounts.push(allocations.length);
      topHoldingBps.push(allocations[0]?.allocationBps ?? 0);
      const portfolioBps = allocations.reduce((total, allocation) => total + allocation.allocationBps, 0);
      totalPortfolioBps += portfolioBps;
      let portfolioRiskScore = 0;
      allocations.forEach((allocation, index) => {
        const option = context.optionsById[allocation.optionId];
        const score = riskBucketScore(option);
        portfolioRiskScore += portfolioBps > 0 ? (allocation.allocationBps / portfolioBps) * score : 0;
        if (score >= 4) highRiskBps += allocation.allocationBps;
        if (isDefensiveOption(allocation.optionId, option)) defensiveBps += allocation.allocationBps;
        if (isTechnologyOption(allocation.optionId, option)) techBps += allocation.allocationBps;
        const existing =
          assetRows.get(allocation.optionId) ??
          ({
            totalBps: 0,
            portfolioKeys: new Set<string>(),
            topPickCount: 0,
            optionsById: context.optionsById
          } satisfies {
            totalBps: number;
            portfolioKeys: Set<string>;
            topPickCount: number;
            optionsById: Record<string, UniverseOption | undefined>;
          });
        existing.totalBps += allocation.allocationBps;
        existing.portfolioKeys.add(portfolioKey);
        existing.topPickCount += index === 0 ? 1 : 0;
        existing.optionsById = { ...existing.optionsById, ...context.optionsById };
        assetRows.set(allocation.optionId, existing);
        const group = optionGroup(allocation.optionId, context.optionsById);
        categoryBps.set(group, (categoryBps.get(group) ?? 0) + allocation.allocationBps);
      });
      portfolioRiskScores.push(portfolioRiskScore);
    }
  }

  const portfolioCount = portfolioKeys.size;
  const denominatorBps = portfolioCount * 10_000;
  const assets = Array.from(assetRows.entries())
    .map(([optionId, asset]) => ({
      optionId,
      label: optionDisplayName(optionId, asset.optionsById),
      shortLabel: optionShortDisplayName(optionId, asset.optionsById),
      symbol: asset.optionsById[optionId]?.symbol ?? "",
      group: optionGroup(optionId, asset.optionsById),
      frequencyPct: portfolioCount > 0 ? (asset.portfolioKeys.size / portfolioCount) * 100 : 0,
      averageAllocationPct: percentFromBps(asset.totalBps, denominatorBps),
      topPickCount: asset.topPickCount
    }))
    .sort((a, b) => b.frequencyPct - a.frequencyPct || b.averageAllocationPct - a.averageAllocationPct || a.label.localeCompare(b.label));

  return {
    portfolioCount,
    averageHoldingCount: average(holdingCounts),
    averageTopHoldingPct: average(topHoldingBps.map((value) => value / 100)),
    riskAppetite: buildRiskAppetite(average(portfolioRiskScores), totalPortfolioBps, highRiskBps, defensiveBps, techBps),
    mostCommonTopHolding: [...assets].sort((a, b) => b.topPickCount - a.topPickCount || b.averageAllocationPct - a.averageAllocationPct)[0],
    assets,
    categories: Array.from(categoryBps.entries())
      .map(([group, bps]) => ({ group, averageAllocationPct: percentFromBps(bps, denominatorBps) }))
      .sort((a, b) => b.averageAllocationPct - a.averageAllocationPct)
  };
}

function buildHistory(modelId: string, contexts: RoundContext[], results: ModelResultRow[]): ModelRoundHistoryRow[] {
  const resultByRound = new Map(results.map((result) => [result.roundId, result]));
  return contexts
    .flatMap((context) =>
      context.submissions
        .filter((submission) => submission.model_id === modelId)
        .map((submission) => {
          const allocations = portfolioAllocations(submission);
          return {
            roundId: context.round.round_id,
            runId: submission.run_id,
            track: context.track,
            entryDate: context.round.entry_date,
            exitDate: context.round.exit_date,
            status: context.round.status,
            portfolioLabel: allocations.map((allocation) => `${allocation.optionId} ${allocation.allocationPct}%`).join(", "),
            portfolioSummary: allocations.map((allocation) => ({
              optionId: allocation.optionId,
              label: optionDisplayName(allocation.optionId, context.optionsById),
              allocationPct: allocation.allocationPct,
              themeClass: allocationThemeClass(allocation.optionId)
            })),
            rationale: submission.rationale_summary || submission.portfolio_rationale || "",
            keyRisks: submission.key_risks ?? [],
            result: resultByRound.get(context.round.round_id),
            parsedPath: `rounds/${context.round.round_id}/runs/${submission.run_id}/submissions/parsed/${submission.model_id}.json`,
            rawPath: `rounds/${context.round.round_id}/runs/${submission.run_id}/submissions/raw/${submission.model_id}.json`
          };
        })
    )
    .sort((a, b) => b.entryDate.localeCompare(a.entryDate) || b.roundId.localeCompare(a.roundId));
}

export function staticModelProfiles(): ModelProfile[] {
  const contexts = roundContexts();
  const modelProviders = new Map<string, string>();
  for (const context of contexts) {
    for (const submission of context.submissions) {
      if (!modelProviders.has(submission.model_id)) modelProviders.set(submission.model_id, submission.provider);
    }
  }

  return Array.from(modelProviders.entries())
    .map(([modelId, provider]) => {
      const modelContexts = contexts.filter((context) => context.submissions.some((submission) => submission.model_id === modelId));
      const results = buildResults(modelId, modelContexts);
      const history = buildHistory(modelId, modelContexts, results);
      const enteredTrackSet = new Set(modelContexts.map((context) => context.track));
      const tracksEntered = (["weekly", "monthly"] as const).filter((track) => enteredTrackSet.has(track));
      return {
        modelId,
        label: modelLabel(modelId),
        provider,
        providerLabel: providerLabel(provider),
        logoSrc: PROVIDER_LOGOS[provider],
        iconSrc: PROVIDER_ICONS[provider],
        firstDecisionDate: [...modelContexts].sort((a, b) => a.round.decision_date.localeCompare(b.round.decision_date))[0]?.round.decision_date,
        tracksEntered,
        live: {
          all: buildLiveScope(modelId, modelContexts, "all"),
          weekly: buildLiveScope(modelId, modelContexts, "weekly"),
          monthly: buildLiveScope(modelId, modelContexts, "monthly")
        },
        scorecards: {
          weekly: buildTrackScore("weekly", results),
          monthly: buildTrackScore("monthly", results)
        },
        allResults: results,
        fingerprint: buildFingerprint(modelId, modelContexts),
        history
      } satisfies ModelProfile;
    })
    .sort((a, b) => a.providerLabel.localeCompare(b.providerLabel) || a.label.localeCompare(b.label));
}

export function staticModelProfile(modelId: string): ModelProfile | undefined {
  return staticModelProfiles().find((profile) => profile.modelId === modelId);
}
