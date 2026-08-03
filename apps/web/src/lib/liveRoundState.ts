import type { RoundRecord, SubmissionRecord, UniverseOption } from "../data/fallback";
import { decisionAllocations } from "./allocations";
import {
  staticAllWeeklyPerformance,
  staticOfficialSubmissions,
  staticUniverseOptions,
  type LivePerformanceRecord
} from "./localRoundRecords";
import { roundTrack, type BenchmarkTrack } from "./tracks";

export type ActiveExposureRound = {
  round: RoundRecord;
  track: BenchmarkTrack;
  submissions: SubmissionRecord[];
  options: UniverseOption[];
};

export type LiveRoundState = {
  activeExposureRounds: ActiveExposureRound[];
  livePerformanceRows: LivePerformanceRecord[];
  openRoundCounts: {
    all: number;
    weekly: number;
    monthly: number;
  };
  livePortfolioCount: number;
  liveHeldAssetCount: number;
  latestCloseDate?: string;
  nextScoreDate?: string;
};

export function buildLiveRoundState(roundRows: RoundRecord[]): LiveRoundState {
  const activeExposureRounds = roundRows
    .filter((round) => round.status === "pending" && round.official_run_id)
    .map((round) => ({
      round,
      track: roundTrack(round),
      submissions: staticOfficialSubmissions(round.round_id, round.official_run_id),
      options: staticUniverseOptions(round.round_id)
    }))
    .filter(
      (item): item is ActiveExposureRound =>
        (item.track === "weekly" || item.track === "monthly") && item.submissions.length > 0
    );
  const livePerformanceRows = staticAllWeeklyPerformance(roundRows).filter((row) => row.status === "pending");
  const openRoundCounts = {
    all: activeExposureRounds.length,
    weekly: activeExposureRounds.filter((item) => item.track === "weekly").length,
    monthly: activeExposureRounds.filter((item) => item.track === "monthly").length
  };
  const livePortfolioCount = activeExposureRounds.reduce((total, item) => total + item.submissions.length, 0);
  const liveHeldAssetCount = new Set(
    activeExposureRounds.flatMap((item) =>
      item.submissions.flatMap((submission) => decisionAllocations(submission).map((allocation) => allocation.option_id))
    )
  ).size;
  const latestCloseDate = livePerformanceRows
    .map((row) => row.price_date)
    .filter(Boolean)
    .sort()
    .at(-1);
  const nextScoreDate = activeExposureRounds
    .map((item) => item.round.score_eta_utc || item.round.exit_date)
    .filter(Boolean)
    .sort()[0];

  return {
    activeExposureRounds,
    livePerformanceRows,
    openRoundCounts,
    livePortfolioCount,
    liveHeldAssetCount,
    latestCloseDate,
    nextScoreDate
  };
}
