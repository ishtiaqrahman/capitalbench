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
import { capitalBenchScore } from "./capitalBenchScore.js";
import { buildTrackScorecard, type TrackScorecardData } from "./trackScorecard";
import { providerLogoSrc } from "./scoreReturnChart";
import { latestResolvedRoundForTrack, roundTrack } from "./tracks";

export type WeeklyOracleScoreRowKind = "model" | "benchmark" | "reference";

export type WeeklyOracleScoreRow = {
  key: string;
  kind: WeeklyOracleScoreRowKind;
  label: string;
  providerLabel?: string;
  logoSrc?: string;
  score: number;
  returnValue?: number;
  alphaVsSp500?: number;
  testsIncluded?: number;
  testsRequired?: number;
  detail: string;
};

export type WeeklyOracleScoreChart = {
  title: string;
  description: string;
  rows: WeeklyOracleScoreRow[];
  domainMin: number;
  domainMax: number;
  ticks: number[];
};

export type WeeklyHistoryModelScore = {
  modelId: string;
  label: string;
  providerLabel: string;
  score: number;
  returnValue: number;
  alphaVsSp500?: number;
};

export type WeeklyHistoryPoint = {
  roundId: string;
  entryDate: string;
  exitDate: string;
  topModelLabel: string;
  topModelScore: number | null;
  averageModelScore: number | null;
  sp500Score: number | null;
  maxPossibleScore: 100;
  averageModelReturn: number | null;
  averageAlphaVsSp500: number | null;
  modelBeatCount: number;
  modelCount: number;
  modelScores: WeeklyHistoryModelScore[];
};

export type WeeklyCumulativeRow = {
  key: string;
  kind: WeeklyOracleScoreRowKind;
  label: string;
  providerLabel?: string;
  score: number;
  averageReturn: number;
  averageAlphaVsSp500?: number;
  totalReturn: number;
  totalMaxPossibleReturn: number;
  testsIncluded: number;
  testsRequired: number;
  beatSp500Count?: number;
  isRankEligible: boolean;
};

export type WeeklyTrackContext = {
  completedRoundCount: number;
  cumulativeLeaderLabel: string;
  cumulativeLeaderScore: number | null;
  sp500Score: number | null;
  averageModelReturn: number | null;
  averageAlphaVsSp500: number | null;
  modelBeatObservationCount: number;
  modelObservationCount: number;
  roundsWithModelBeat: number;
  latestNoBeatStreak: number;
  summary: string;
};

export type WeeklyResultsPageModel = {
  latestResolvedRound?: RoundRecord;
  scorecard: TrackScorecardData | null;
  latestOracleChart: WeeklyOracleScoreChart | null;
  cumulativeOracleChart: WeeklyOracleScoreChart | null;
  historyPoints: WeeklyHistoryPoint[];
  cumulativeRows: WeeklyCumulativeRow[];
  context: WeeklyTrackContext | null;
};

function finiteNumber(value: number | null | undefined): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

function average(values: number[]): number | null {
  if (values.length === 0) return null;
  return values.reduce((total, value) => total + value, 0) / values.length;
}

function leaderboardReturn(row: LeaderboardRecord): number | undefined {
  return row.portfolio_return ?? row.selected_asset_return;
}

function bestReturn(rows: ResultReturnRecord[]): ResultReturnRecord | undefined {
  return rows
    .filter((row) => finiteNumber(row.return))
    .sort((left, right) => right.return - left.return)[0];
}

function roundSortKey(round: RoundRecord): string {
  return `${round.exit_date ?? ""}:${round.decision_deadline_utc ?? ""}:${round.round_id}`;
}

function scoreDomain(rows: WeeklyOracleScoreRow[]): Pick<WeeklyOracleScoreChart, "domainMin" | "domainMax" | "ticks"> {
  const values = rows.map((row) => row.score).filter(finiteNumber);
  const minimum = Math.min(0, ...values);
  const maximum = Math.max(100, ...values);
  const padding = Math.max((maximum - minimum) * 0.06, 8);
  const domainMin = minimum < 0 ? Math.floor((minimum - padding) / 25) * 25 : 0;
  const domainMax = maximum > 100 ? Math.ceil((maximum + padding) / 25) * 25 : 100;
  const ticks = domainMin < 0 ? [domainMin, 0, 50, 100] : [0, 25, 50, 75, 100];
  return { domainMin, domainMax, ticks };
}

function oracleChart(title: string, description: string, rows: WeeklyOracleScoreRow[]): WeeklyOracleScoreChart | null {
  if (rows.length === 0) return null;
  return {
    title,
    description,
    rows,
    ...scoreDomain(rows)
  };
}

function latestOracleRows(leaderboard: LeaderboardRecord[], returns: ResultReturnRecord[]): WeeklyOracleScoreRow[] {
  const maxReturnRow = bestReturn(returns);
  const maxReturn = maxReturnRow?.return;
  if (!finiteNumber(maxReturn)) return [];

  const modelRows = leaderboard
    .map((row): WeeklyOracleScoreRow | null => {
      const returnValue = leaderboardReturn(row);
      if (!finiteNumber(returnValue)) return null;
      const score = capitalBenchScore(returnValue, maxReturn);
      if (!finiteNumber(score)) return null;
      return {
        key: row.model_id,
        kind: "model",
        label: modelLabel(row.model_id),
        providerLabel: providerLabel(row.provider),
        logoSrc: providerLogoSrc(row.provider),
        score,
        returnValue,
        alphaVsSp500: row.alpha_vs_sp500,
        detail: `${providerLabel(row.provider)} model portfolio`
      };
    })
    .filter((row): row is WeeklyOracleScoreRow => row !== null)
    .sort((left, right) => right.score - left.score || left.label.localeCompare(right.label));

  const benchmarkReturn = leaderboard.find((row) => finiteNumber(row.sp500_return))?.sp500_return;
  const benchmarkScore = finiteNumber(benchmarkReturn) ? capitalBenchScore(benchmarkReturn, maxReturn) : null;
  const benchmarkRow: WeeklyOracleScoreRow[] = finiteNumber(benchmarkScore) && finiteNumber(benchmarkReturn)
    ? [
        {
          key: "sp500",
          kind: "benchmark",
          label: "S&P 500",
          providerLabel: "Benchmark",
          score: benchmarkScore,
          returnValue: benchmarkReturn,
          alphaVsSp500: 0,
          detail: "S&P 500 return over the same scoring window"
        }
      ]
    : [];

  return [
    {
      key: "max-possible",
      kind: "reference",
      label: "Max possible",
      providerLabel: maxReturnRow?.asset_symbol || "Oracle",
      score: 100,
      returnValue: maxReturn,
      detail: `Hindsight best eligible asset: ${maxReturnRow?.label ?? "best asset"}`
    },
    ...benchmarkRow,
    ...modelRows
  ];
}

function cumulativeOracleRows(scorecard: TrackScorecardData | null): WeeklyOracleScoreRow[] {
  if (!scorecard) return [];
  const reference = scorecard.normalizedRows.find((row) => row.kind === "reference");
  const benchmark = scorecard.normalizedRows.find((row) => row.kind === "benchmark");
  const models = scorecard.normalizedRows
    .filter((row) => row.kind === "model" && row.isRankEligible)
    .sort((left, right) => right.averageScore - left.averageScore || left.label.localeCompare(right.label));

  return [
    ...(reference
      ? [
          {
            key: reference.key,
            kind: "reference" as const,
            label: reference.label,
            providerLabel: reference.providerLabel,
            score: reference.averageScore,
            returnValue: reference.totalReturn,
            testsIncluded: reference.testsIncluded,
            testsRequired: reference.testsRequired,
            detail: "Hindsight best eligible asset in each resolved weekly round"
          }
        ]
      : []),
    ...models.map((row) => ({
      key: row.key,
      kind: "model" as const,
      label: row.label,
      providerLabel: row.providerLabel,
      logoSrc: row.logoSrc,
      score: row.averageScore,
      returnValue: row.totalReturn,
      testsIncluded: row.testsIncluded,
      testsRequired: row.testsRequired,
      detail: `${row.providerLabel ?? "Model"} full-history weekly score`
    })),
    ...(benchmark
      ? [
          {
            key: benchmark.key,
            kind: "benchmark" as const,
            label: benchmark.label,
            providerLabel: benchmark.providerLabel,
            score: benchmark.averageScore,
            returnValue: benchmark.totalReturn,
            testsIncluded: benchmark.testsIncluded,
            testsRequired: benchmark.testsRequired,
            detail: "S&P 500 score across the same weekly windows"
          }
        ]
      : [])
  ];
}

function buildHistory(roundRows: RoundRecord[]): WeeklyHistoryPoint[] {
  return roundRows
    .filter((round) => round.status === "resolved" && roundTrack(round) === "weekly")
    .sort((left, right) => roundSortKey(left).localeCompare(roundSortKey(right)))
    .map((round): WeeklyHistoryPoint | null => {
      const leaderboard = staticRoundLeaderboard(round.round_id, round.official_run_id);
      const returns = staticRoundReturns(round.round_id, round.official_run_id);
      const maxReturn = bestReturn(returns)?.return;
      if (!finiteNumber(maxReturn)) return null;

      const modelScores = leaderboard
        .map((row): WeeklyHistoryModelScore | null => {
          const returnValue = leaderboardReturn(row);
          if (!finiteNumber(returnValue)) return null;
          const score = capitalBenchScore(returnValue, maxReturn);
          if (!finiteNumber(score)) return null;
          return {
            modelId: row.model_id,
            label: modelLabel(row.model_id),
            providerLabel: providerLabel(row.provider),
            score,
            returnValue,
            alphaVsSp500: row.alpha_vs_sp500
          };
        })
        .filter((row): row is WeeklyHistoryModelScore => row !== null)
        .sort((left, right) => right.score - left.score || left.label.localeCompare(right.label));

      if (modelScores.length === 0) return null;
      const benchmarkReturn = leaderboard.find((row) => finiteNumber(row.sp500_return))?.sp500_return;
      const sp500Score = finiteNumber(benchmarkReturn) ? capitalBenchScore(benchmarkReturn, maxReturn) : null;
      const alphas = modelScores.map((row) => row.alphaVsSp500).filter(finiteNumber);

      return {
        roundId: round.round_id,
        entryDate: round.entry_date,
        exitDate: round.exit_date,
        topModelLabel: modelScores[0]?.label ?? "n/a",
        topModelScore: modelScores[0]?.score ?? null,
        averageModelScore: average(modelScores.map((row) => row.score)),
        sp500Score: finiteNumber(sp500Score) ? sp500Score : null,
        maxPossibleScore: 100,
        averageModelReturn: average(modelScores.map((row) => row.returnValue)),
        averageAlphaVsSp500: average(alphas),
        modelBeatCount: alphas.filter((alpha) => alpha > 0).length,
        modelCount: modelScores.length,
        modelScores
      };
    })
    .filter((row): row is WeeklyHistoryPoint => row !== null);
}

function cumulativeRows(scorecard: TrackScorecardData | null, historyPoints: WeeklyHistoryPoint[]): WeeklyCumulativeRow[] {
  if (!scorecard) return [];
  const beatCounts = new Map<string, number>();
  for (const point of historyPoints) {
    for (const model of point.modelScores) {
      if (finiteNumber(model.alphaVsSp500) && model.alphaVsSp500 > 0) {
        beatCounts.set(model.modelId, (beatCounts.get(model.modelId) ?? 0) + 1);
      }
    }
  }
  const averageByKey = new Map(scorecard.averageRows.map((row) => [row.key, row]));
  return scorecard.normalizedRows
    .filter((row) => row.kind !== "reference")
    .map((row) => {
      const averageRow = averageByKey.get(row.key);
      return {
        key: row.key,
        kind: row.kind,
        label: row.label,
        providerLabel: row.providerLabel,
        score: row.averageScore,
        averageReturn: row.averageReturn,
        averageAlphaVsSp500: averageRow?.averageAlphaVsSp500,
        totalReturn: row.totalReturn,
        totalMaxPossibleReturn: row.totalMaxPossibleReturn,
        testsIncluded: row.testsIncluded,
        testsRequired: row.testsRequired,
        beatSp500Count: row.kind === "model" ? beatCounts.get(row.key) ?? 0 : undefined,
        isRankEligible: row.isRankEligible
      };
    })
    .sort(
      (left, right) =>
        Number(right.kind === "model" && right.isRankEligible) - Number(left.kind === "model" && left.isRankEligible) ||
        right.score - left.score ||
        left.label.localeCompare(right.label)
    );
}

function buildContext(scorecard: TrackScorecardData | null, historyPoints: WeeklyHistoryPoint[]): WeeklyTrackContext | null {
  if (!scorecard || historyPoints.length === 0) return null;
  const modelObservations = historyPoints.flatMap((point) => point.modelScores);
  const alphaValues = modelObservations.map((row) => row.alphaVsSp500).filter(finiteNumber);
  const modelBeatObservationCount = alphaValues.filter((alpha) => alpha > 0).length;
  const roundsWithModelBeat = historyPoints.filter((point) => point.modelBeatCount > 0).length;
  let latestNoBeatStreak = 0;
  for (const point of [...historyPoints].reverse()) {
    if (point.modelBeatCount > 0) break;
    latestNoBeatStreak += 1;
  }

  const cumulativeLeader = scorecard.topNormalizedRow;
  const benchmark = scorecard.normalizedRows.find((row) => row.kind === "benchmark");
  const averageRows = scorecard.averageRows.filter((row) => row.kind === "model" && row.isRankEligible);
  const averageModelReturn = average(averageRows.map((row) => row.averageReturn).filter(finiteNumber));
  const averageAlphaVsSp500 = average(averageRows.map((row) => row.averageAlphaVsSp500).filter(finiteNumber));
  const streakSentence =
    latestNoBeatStreak > 0
      ? `No model has beaten the S&P 500 in the last ${latestNoBeatStreak} completed weekly round${latestNoBeatStreak === 1 ? "" : "s"}.`
      : "At least one model beat the S&P 500 in the latest completed weekly round.";

  return {
    completedRoundCount: historyPoints.length,
    cumulativeLeaderLabel: cumulativeLeader?.label ?? "n/a",
    cumulativeLeaderScore: cumulativeLeader?.averageScore ?? null,
    sp500Score: benchmark?.averageScore ?? null,
    averageModelReturn,
    averageAlphaVsSp500,
    modelBeatObservationCount,
    modelObservationCount: modelObservations.length,
    roundsWithModelBeat,
    latestNoBeatStreak,
    summary: `Models have beaten the S&P 500 in ${roundsWithModelBeat}/${historyPoints.length} completed weekly rounds and ${modelBeatObservationCount}/${modelObservations.length} model-round observations. ${streakSentence}`
  };
}

export function buildWeeklyResultsPageModel(roundRows: RoundRecord[]): WeeklyResultsPageModel {
  const latestResolvedRound = latestResolvedRoundForTrack(roundRows, "weekly");
  const scorecard = buildTrackScorecard(roundRows, "weekly");
  const latestLeaderboard = latestResolvedRound
    ? staticRoundLeaderboard(latestResolvedRound.round_id, latestResolvedRound.official_run_id)
    : [];
  const latestReturns = latestResolvedRound
    ? staticRoundReturns(latestResolvedRound.round_id, latestResolvedRound.official_run_id)
    : [];
  const historyPoints = buildHistory(roundRows);
  const latestRows = latestOracleRows(latestLeaderboard, latestReturns);
  const cumulativeRowsForChart = cumulativeOracleRows(scorecard);
  const cumulativeTableRows = cumulativeRows(scorecard, historyPoints);

  return {
    latestResolvedRound,
    scorecard,
    latestOracleChart: oracleChart(
      "Latest Round CapitalBench Score",
      "CapitalBench Score compares each portfolio with the best eligible asset in hindsight for this exact weekly window. Max possible is 100.",
      latestRows
    ),
    cumulativeOracleChart: oracleChart(
      "Full-History Weekly CapitalBench Score",
      "Full-history scores divide total model return by total max-possible return across every resolved weekly round.",
      cumulativeRowsForChart
    ),
    historyPoints,
    cumulativeRows: cumulativeTableRows,
    context: buildContext(scorecard, historyPoints)
  };
}
