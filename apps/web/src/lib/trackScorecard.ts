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
  testsIncluded: number;
  roundsIncluded: string[];
};

export type TrackScorecardData = {
  track: BenchmarkTrack;
  label: string;
  completedRoundCount: number;
  completedRoundIds: string[];
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
  rounds: string[];
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

function normalizedScore(value: number, ceiling: number): number {
  if (!Number.isFinite(ceiling)) return 0;
  if (Math.abs(ceiling) < 0.0000001) return value === ceiling ? 100 : 0;
  return (value / ceiling) * 100;
}

function trackLabel(track: BenchmarkTrack): string {
  return track === "weekly" ? "Weekly" : "Monthly";
}

export function buildTrackScorecard(roundRows: RoundRecord[], track: BenchmarkTrack): TrackScorecardData | null {
  const completedRounds = roundRows
    .filter((round) => round.status === "resolved" && roundTrack(round) === track)
    .sort((left, right) => left.decision_deadline_utc.localeCompare(right.decision_deadline_utc));

  if (completedRounds.length === 0) return null;

  const modelAccumulators = new Map<string, ModelAccumulator>();
  const benchmarkReturns: number[] = [];
  const benchmarkScores: number[] = [];
  const benchmarkRounds: string[] = [];
  const maxPossibleReturns: number[] = [];
  const maxPossibleRounds: string[] = [];

  for (const round of completedRounds) {
    const leaderboard = staticRoundLeaderboard(round.round_id, round.official_run_id);
    const roundParticipants = leaderboard
      .map((row) => ({
        kind: "model" as const,
        modelId: row.model_id,
        provider: row.provider,
        returnValue: leaderboardReturn(row),
        alphaValue: row.alpha_vs_sp500
      }))
      .filter((row): row is typeof row & { returnValue: number } => finiteNumber(row.returnValue));

    const maxReturn = bestUniverseReturn(staticRoundReturns(round.round_id, round.official_run_id));
    if (!finiteNumber(maxReturn)) continue;

    const benchmarkReturn = leaderboard.find((row) => finiteNumber(row.sp500_return))?.sp500_return;
    if (finiteNumber(benchmarkReturn)) {
      benchmarkReturns.push(benchmarkReturn);
      benchmarkScores.push(normalizedScore(benchmarkReturn, maxReturn));
      benchmarkRounds.push(round.round_id);
    }

    for (const participant of roundParticipants) {
      const existing = modelAccumulators.get(participant.modelId) ?? {
        modelId: participant.modelId,
        provider: participant.provider,
        returns: [],
        alphas: [],
        scores: [],
        rounds: []
      };
      existing.returns.push(participant.returnValue);
      if (finiteNumber(participant.alphaValue)) existing.alphas.push(participant.alphaValue);
      existing.scores.push(normalizedScore(participant.returnValue, maxReturn));
      existing.rounds.push(round.round_id);
      modelAccumulators.set(participant.modelId, existing);
    }

    maxPossibleReturns.push(maxReturn);
    maxPossibleRounds.push(round.round_id);
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
      roundsIncluded: item.rounds
    }))
    .sort((left, right) => right.averageReturn - left.averageReturn || left.label.localeCompare(right.label));

  const modelNormalizedRows: TrackScorecardNormalizedRow[] = Array.from(modelAccumulators.values())
    .map((item) => ({
      key: item.modelId,
      kind: "model" as const,
      label: modelLabel(item.modelId),
      provider: item.provider,
      providerLabel: providerLabel(item.provider),
      logoSrc: providerLogoSrc(item.provider),
      averageScore: average(item.scores),
      averageReturn: average(item.returns),
      testsIncluded: item.scores.length,
      roundsIncluded: item.rounds
    }))
    .sort((left, right) => right.averageScore - left.averageScore || left.label.localeCompare(right.label));

  const benchmarkAverageRow: TrackScorecardAverageRow | undefined = benchmarkReturns.length
    ? {
        key: "sp500",
        kind: "benchmark",
        label: "S&P 500",
        providerLabel: "Benchmark",
        averageReturn: average(benchmarkReturns),
        averageAlphaVsSp500: 0,
        testsIncluded: benchmarkReturns.length,
        roundsIncluded: benchmarkRounds
      }
    : undefined;

  const benchmarkNormalizedRow: TrackScorecardNormalizedRow | undefined = benchmarkScores.length
    ? {
        key: "sp500",
        kind: "benchmark",
        label: "S&P 500",
        providerLabel: "Benchmark",
        averageScore: average(benchmarkScores),
        averageReturn: average(benchmarkReturns),
        testsIncluded: benchmarkScores.length,
        roundsIncluded: benchmarkRounds
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
    completedRoundCount: completedRounds.length,
    completedRoundIds: completedRounds.map((round) => round.round_id),
    latestRoundId: completedRounds[completedRounds.length - 1]?.round_id ?? "",
    averageRows,
    normalizedRows,
    topAverageRow: modelAverageRows[0],
    topNormalizedRow: modelNormalizedRows[0],
    benchmarkAverageRow
  };
}
