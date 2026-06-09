import {
  modelLabel,
  providerLabel,
  type LeaderboardRecord,
  type RoundRecord
} from "../data/fallback";
import {
  staticRoundLeaderboard,
  staticRoundReturns,
  type ResultReturnRecord
} from "./localRoundRecords";
import { capitalBenchScore, cumulativeCapitalBenchScore } from "./capitalBenchScore.js";
import { providerLogoSrc } from "./scoreReturnChart";
import { roundTrack, type BenchmarkTrack } from "./tracks";

export type TrackScorecardRowKind = "model" | "benchmark" | "reference";

export type TrackScorecardAverageRow = {
  key: string;
  kind: TrackScorecardRowKind;
  label: string;
  provider?: string;
  providerLabel?: string;
  logoSrc?: string;
  averageReturn: number;
  averageAlphaVsSp500?: number;
  testsIncluded: number;
  testsRequired: number;
  isRankEligible: boolean;
  sampleStatus: "eligible" | "provisional" | "reference";
  roundsIncluded: string[];
};

export type TrackScorecardNormalizedRow = {
  key: string;
  kind: Exclude<TrackScorecardRowKind, "reference">;
  label: string;
  provider?: string;
  providerLabel?: string;
  logoSrc?: string;
  averageScore: number;
  averageReturn: number;
  totalReturn: number;
  totalMaxPossibleReturn: number;
  testsIncluded: number;
  testsRequired: number;
  isRankEligible: boolean;
  sampleStatus: "eligible" | "provisional";
  roundsIncluded: string[];
  scoreValues: number[];
};

export type TrackScorecardData = {
  track: BenchmarkTrack;
  label: string;
  completedRoundCount: number;
  completedRoundIds: string[];
  comparisonRoundCount: number;
  comparisonRoundIds: string[];
  excludedRoundIds: string[];
  comparisonModelCount: number;
  comparisonMode: "all_resolved_rounds";
  isEarlyCohort: boolean;
  latestRoundId: string;
  averageRows: TrackScorecardAverageRow[];
  normalizedRows: TrackScorecardNormalizedRow[];
  topAverageRow?: TrackScorecardAverageRow;
  topNormalizedRow?: TrackScorecardNormalizedRow;
  benchmarkAverageRow?: TrackScorecardAverageRow;
};

type ModelAccumulator = {
  modelId: string;
  provider: string;
  returns: number[];
  alphas: number[];
  scores: number[];
  maxReturns: number[];
  rounds: string[];
};

type RoundScoreInput = {
  round: RoundRecord;
  participants: Array<{
    kind: "model";
    modelId: string;
    provider: string;
    returnValue: number;
    alphaValue: number | undefined;
  }>;
  rosterModelIds: string[];
  maxReturn: number;
  benchmarkReturn: number | undefined;
};

function finiteNumber(value: number | null | undefined): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

function leaderboardReturn(row: LeaderboardRecord): number | undefined {
  return row.portfolio_return ?? row.selected_asset_return;
}

function bestUniverseReturn(rows: ResultReturnRecord[]): number | undefined {
  return rows
    .filter((row) => finiteNumber(row.return))
    .sort((left, right) => right.return - left.return)[0]?.return;
}

function average(values: number[]): number {
  if (values.length === 0) return 0;
  return values.reduce((total, value) => total + value, 0) / values.length;
}

function trackLabel(track: BenchmarkTrack): string {
  return track === "weekly" ? "Weekly" : "Monthly";
}

function roundSortKey(round: RoundRecord): string {
  return `${round.exit_date ?? ""}:${round.decision_deadline_utc ?? ""}:${round.round_id}`;
}

type RankEligibility = {
  testsRequired: number;
  isRankEligible: boolean;
  sampleStatus: "eligible" | "provisional";
};

function rankEligibility(testsIncluded: number, testsRequired: number): RankEligibility {
  const isRankEligible = testsRequired > 0 && testsIncluded === testsRequired;
  return {
    testsRequired,
    isRankEligible,
    sampleStatus: isRankEligible ? "eligible" : "provisional"
  };
}

export function buildTrackScorecard(roundRows: RoundRecord[], track: BenchmarkTrack): TrackScorecardData | null {
  const completedRounds = roundRows
    .filter((round) => round.status === "resolved" && roundTrack(round) === track)
    .sort((left, right) => roundSortKey(left).localeCompare(roundSortKey(right)));

  if (completedRounds.length === 0) return null;

  const scoredRounds = completedRounds
    .map((round): RoundScoreInput | null => {
      const leaderboard = staticRoundLeaderboard(round.round_id, round.official_run_id);
      const participants: RoundScoreInput["participants"] = leaderboard
        .map((row) => ({
          kind: "model" as const,
          modelId: row.model_id,
          provider: row.provider,
          returnValue: leaderboardReturn(row),
          alphaValue: row.alpha_vs_sp500
        }))
        .filter((row): row is typeof row & { returnValue: number } => finiteNumber(row.returnValue));

      const maxReturn = bestUniverseReturn(staticRoundReturns(round.round_id, round.official_run_id));
      if (participants.length === 0 || !finiteNumber(maxReturn)) return null;

      return {
        round,
        participants,
        rosterModelIds: participants.map((participant) => participant.modelId).sort(),
        maxReturn,
        benchmarkReturn: leaderboard.find((row) => finiteNumber(row.sp500_return))?.sp500_return
      };
    })
    .filter((item): item is RoundScoreInput => item !== null);

  if (scoredRounds.length === 0) return null;

  const comparisonRounds = scoredRounds;
  const comparisonRoundCount = comparisonRounds.length;
  if (comparisonRoundCount === 0) return null;

  const modelAccumulators = new Map<string, ModelAccumulator>();
  const benchmarkReturns: number[] = [];
  const benchmarkScores: number[] = [];
  const benchmarkMaxReturns: number[] = [];
  const benchmarkRounds: string[] = [];
  const maxPossibleReturns: number[] = [];
  const maxPossibleRounds: string[] = [];

  for (const roundScore of comparisonRounds) {
    if (finiteNumber(roundScore.benchmarkReturn)) {
      benchmarkReturns.push(roundScore.benchmarkReturn);
      const benchmarkScore = capitalBenchScore(roundScore.benchmarkReturn, roundScore.maxReturn);
      if (finiteNumber(benchmarkScore)) benchmarkScores.push(benchmarkScore);
      benchmarkMaxReturns.push(roundScore.maxReturn);
      benchmarkRounds.push(roundScore.round.round_id);
    }

    for (const participant of roundScore.participants) {
      const existing = modelAccumulators.get(participant.modelId) ?? {
        modelId: participant.modelId,
        provider: participant.provider,
        returns: [],
        alphas: [],
        scores: [],
        maxReturns: [],
        rounds: []
      };
      existing.returns.push(participant.returnValue);
      if (finiteNumber(participant.alphaValue)) existing.alphas.push(participant.alphaValue);
      const score = capitalBenchScore(participant.returnValue, roundScore.maxReturn);
      if (finiteNumber(score)) existing.scores.push(score);
      existing.maxReturns.push(roundScore.maxReturn);
      existing.rounds.push(roundScore.round.round_id);
      modelAccumulators.set(participant.modelId, existing);
    }

    maxPossibleReturns.push(roundScore.maxReturn);
    maxPossibleRounds.push(roundScore.round.round_id);
  }

  const modelAverageRows: TrackScorecardAverageRow[] = Array.from(modelAccumulators.values())
    .map((item) => ({
      key: item.modelId,
      kind: "model" as const,
      label: modelLabel(item.modelId),
      provider: item.provider,
      providerLabel: providerLabel(item.provider),
      logoSrc: providerLogoSrc(item.provider),
      averageReturn: average(item.returns),
      averageAlphaVsSp500: item.alphas.length ? average(item.alphas) : undefined,
      testsIncluded: item.returns.length,
      ...rankEligibility(item.returns.length, comparisonRoundCount),
      roundsIncluded: item.rounds
    }))
    .sort(
      (left, right) =>
        Number(right.isRankEligible) - Number(left.isRankEligible) ||
        right.averageReturn - left.averageReturn ||
        left.label.localeCompare(right.label)
    );

  const modelNormalizedRows: TrackScorecardNormalizedRow[] = Array.from(modelAccumulators.values())
    .map((item) => ({
      key: item.modelId,
      kind: "model" as const,
      label: modelLabel(item.modelId),
      provider: item.provider,
      providerLabel: providerLabel(item.provider),
      logoSrc: providerLogoSrc(item.provider),
      averageScore: cumulativeCapitalBenchScore(item.returns, item.maxReturns) ?? 0,
      averageReturn: average(item.returns),
      totalReturn: item.returns.reduce((total, value) => total + value, 0),
      totalMaxPossibleReturn: item.maxReturns.reduce((total, value) => total + value, 0),
      testsIncluded: item.returns.length,
      ...rankEligibility(item.returns.length, comparisonRoundCount),
      roundsIncluded: item.rounds,
      scoreValues: item.scores
    }))
    .sort(
      (left, right) =>
        Number(right.isRankEligible) - Number(left.isRankEligible) ||
        right.averageScore - left.averageScore ||
        left.label.localeCompare(right.label)
    );

  const benchmarkAverageRow: TrackScorecardAverageRow | undefined = benchmarkReturns.length
    ? {
        key: "sp500",
        kind: "benchmark",
        label: "S&P 500",
        providerLabel: "Benchmark",
        averageReturn: average(benchmarkReturns),
        averageAlphaVsSp500: 0,
        testsIncluded: benchmarkReturns.length,
        testsRequired: comparisonRoundCount,
        isRankEligible: benchmarkReturns.length === comparisonRoundCount,
        sampleStatus: benchmarkReturns.length === comparisonRoundCount ? "eligible" : "provisional",
        roundsIncluded: benchmarkRounds
      }
    : undefined;

  const benchmarkNormalizedRow: TrackScorecardNormalizedRow | undefined = benchmarkScores.length
    ? {
        key: "sp500",
        kind: "benchmark",
        label: "S&P 500",
        providerLabel: "Benchmark",
        averageScore: cumulativeCapitalBenchScore(benchmarkReturns, benchmarkMaxReturns) ?? 0,
        averageReturn: average(benchmarkReturns),
        totalReturn: benchmarkReturns.reduce((total, value) => total + value, 0),
        totalMaxPossibleReturn: benchmarkMaxReturns.reduce((total, value) => total + value, 0),
        testsIncluded: benchmarkReturns.length,
        testsRequired: comparisonRoundCount,
        isRankEligible: benchmarkReturns.length === comparisonRoundCount,
        sampleStatus: benchmarkReturns.length === comparisonRoundCount ? "eligible" : "provisional",
        roundsIncluded: benchmarkRounds,
        scoreValues: benchmarkScores
      }
    : undefined;

  const maxPossibleAverageRow: TrackScorecardAverageRow | undefined = maxPossibleReturns.length
    ? {
        key: "max-possible",
        kind: "reference",
        label: "Max possible",
        providerLabel: "Best asset in universe",
        averageReturn: average(maxPossibleReturns),
        testsIncluded: maxPossibleReturns.length,
        testsRequired: comparisonRoundCount,
        isRankEligible: true,
        sampleStatus: "reference",
        roundsIncluded: maxPossibleRounds
      }
    : undefined;

  const averageRows = [
    ...modelAverageRows,
    ...(benchmarkAverageRow ? [benchmarkAverageRow] : []),
    ...(maxPossibleAverageRow ? [maxPossibleAverageRow] : [])
  ];
  const normalizedRows = [
    ...modelNormalizedRows,
    ...(benchmarkNormalizedRow ? [benchmarkNormalizedRow] : [])
  ];

  if (averageRows.length === 0 || normalizedRows.length === 0) return null;

  return {
    track,
    label: trackLabel(track),
    completedRoundCount: scoredRounds.length,
    completedRoundIds: scoredRounds.map((roundScore) => roundScore.round.round_id),
    comparisonRoundCount,
    comparisonRoundIds: comparisonRounds.map((roundScore) => roundScore.round.round_id),
    excludedRoundIds: [],
    comparisonModelCount: new Set(comparisonRounds.flatMap((roundScore) => roundScore.rosterModelIds)).size,
    comparisonMode: "all_resolved_rounds",
    isEarlyCohort: comparisonRoundCount === 1,
    latestRoundId: comparisonRounds[comparisonRounds.length - 1]?.round.round_id ?? "",
    averageRows,
    normalizedRows,
    topAverageRow: modelAverageRows.find((row) => row.isRankEligible),
    topNormalizedRow: modelNormalizedRows.find((row) => row.isRankEligible),
    benchmarkAverageRow
  };
}
