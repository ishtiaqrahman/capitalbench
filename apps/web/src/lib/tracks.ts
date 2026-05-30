import type { RoundRecord } from "../data/fallback";

export type BenchmarkTrack = "weekly" | "monthly";

export function roundTrack(round: Pick<RoundRecord, "round_id" | "horizon_days" | "horizon">): BenchmarkTrack | "other" {
  if (round.round_id.endsWith("-1W") || round.horizon_days <= 10 || /week/i.test(round.horizon)) {
    return "weekly";
  }
  if (round.round_id.endsWith("-1M") || round.horizon_days >= 28 || /month/i.test(round.horizon)) {
    return "monthly";
  }
  return "other";
}

export function trackLabel(track: BenchmarkTrack | "other"): string {
  if (track === "weekly") return "Weekly";
  if (track === "monthly") return "Monthly";
  return "Other";
}

export function latestRoundForTrack(rounds: RoundRecord[], track: BenchmarkTrack): RoundRecord | undefined {
  return rounds.find((round) => roundTrack(round) === track);
}

export function latestResolvedRoundForTrack(rounds: RoundRecord[], track: BenchmarkTrack): RoundRecord | undefined {
  return rounds.find((round) => roundTrack(round) === track && round.status === "resolved");
}

export function latestPendingRoundForTrack(rounds: RoundRecord[], track: BenchmarkTrack): RoundRecord | undefined {
  return rounds.find((round) => roundTrack(round) === track && round.status === "pending");
}

export function roundsForTrack(rounds: RoundRecord[], track: BenchmarkTrack): RoundRecord[] {
  return rounds.filter((round) => roundTrack(round) === track);
}

export function latestSlotForTrack(track: BenchmarkTrack): string {
  return `latest_${track}`;
}

export function cumulativeSlotForTrack(track: BenchmarkTrack): string {
  return `cumulative_${track}`;
}
