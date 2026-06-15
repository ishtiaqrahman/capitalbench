import { modelLabel, type RoundRecord, type UniverseOption } from "../data/fallback";
import {
  staticRoundAllocations,
  staticRoundLeaderboard,
  staticRoundReturns,
  staticUniverseOptions
} from "./localRoundRecords";
import { buildScoreReturnChartData, type ScoreReturnChartData } from "./scoreReturnChart";
import { roundsForTrack, type BenchmarkTrack } from "./tracks";

export type LatestOfficialResultItem = {
  key: string;
  roundId: string;
  title: string;
  subtitle: string;
  chartLabel: string;
  dateRangeLabel: string;
  scoreDateLabel: string;
  modelCount: number;
  assetCount: number;
  horizonLabel: string;
  winnerLabel: string;
  auditHref: string;
  leaderboardHref: string;
  chart: ScoreReturnChartData;
};

export type LatestOfficialResultTrack = {
  track: BenchmarkTrack;
  label: string;
  tabLabel: string;
  description: string;
  results: LatestOfficialResultItem[];
};

function shortMonthDay(value?: string | null): string {
  if (!value) return "";
  const [year, month, day] = value.slice(0, 10).split("-").map((part) => Number(part));
  if (!year || !month || !day) return value.slice(0, 10);
  return new Intl.DateTimeFormat("en", {
    month: "short",
    day: "numeric",
    timeZone: "UTC"
  }).format(new Date(Date.UTC(year, month - 1, day)));
}

function trackLabel(track: BenchmarkTrack): string {
  return track === "weekly" ? "Weekly" : "Monthly";
}

function resultNoun(track: BenchmarkTrack): string {
  return track === "weekly" ? "one-week" : "one-month";
}

export function buildLatestOfficialResultTrack(track: BenchmarkTrack, rounds: RoundRecord[]): LatestOfficialResultTrack {
  const label = trackLabel(track);
  const resolvedRounds = rounds
    .filter((round) => round.status === "resolved")
    .sort((left, right) => (right.exit_date || right.decision_date || "").localeCompare(left.exit_date || left.decision_date || ""));

  return {
    track,
    label,
    tabLabel: label,
    description: `${label} results, newest official score first`,
    results: resolvedRounds
      .map((round) => {
        const leaderboard = staticRoundLeaderboard(round.round_id, round.official_run_id);
        if (leaderboard.length === 0) return null;

        const options = staticUniverseOptions(round.round_id);
        const optionsById: Record<string, UniverseOption | undefined> = Object.fromEntries(
          options.map((option) => [option.option_id, option])
        );
        const returns = staticRoundReturns(round.round_id, round.official_run_id);
        const allocations = staticRoundAllocations(round.round_id, round.official_run_id);
        const scoreDateLabel = shortMonthDay(round.exit_date) || round.exit_date;
        const entryDateLabel = shortMonthDay(round.entry_date) || round.entry_date;
        const winner = leaderboard[0];

        return {
          key: round.round_id,
          roundId: round.round_id,
          title: `${label} result scored ${scoreDateLabel}`,
          subtitle: `Frozen model portfolios scored after the ${resultNoun(track)} window. Live rounds stay out until final prices are available.`,
          chartLabel: `${label} official result`,
          dateRangeLabel: `${entryDateLabel} to ${scoreDateLabel}`,
          scoreDateLabel,
          modelCount: leaderboard.length,
          assetCount: options.length,
          horizonLabel: label,
          winnerLabel: winner ? modelLabel(winner.model_id) : "No scored leader",
          auditHref: `/rounds/${round.round_id}/`,
          leaderboardHref: `/leaderboards/latest-${track}`,
          chart: buildScoreReturnChartData({
            leaderboard,
            returns,
            optionsById,
            allocations
          })
        };
      })
      .filter((result): result is LatestOfficialResultItem => result !== null)
  };
}

export function buildLatestOfficialResultTracks(
  rounds: RoundRecord[],
  tracks: BenchmarkTrack[] = ["weekly", "monthly"]
): LatestOfficialResultTrack[] {
  return tracks.map((track) => buildLatestOfficialResultTrack(track, roundsForTrack(rounds, track)));
}
