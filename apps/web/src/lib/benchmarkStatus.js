function shortDate(value) {
  if (!value) return "n/a";
  const date = new Date(`${String(value).slice(0, 10)}T00:00:00Z`);
  if (Number.isNaN(date.getTime())) return String(value);
  return new Intl.DateTimeFormat("en", { month: "short", day: "numeric", timeZone: "UTC" }).format(date);
}

function refreshTimestamp(value) {
  if (!value) return "n/a";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return String(value);
  return new Intl.DateTimeFormat("en", {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    timeZone: "UTC",
    timeZoneName: "short"
  }).format(date);
}

function roundTrack(round) {
  if (!round) return "other";
  const roundId = String(round.round_id ?? "");
  const horizon = String(round.horizon ?? "");
  const horizonDays = Number(round.horizon_days);
  if (roundId.endsWith("-1W") || horizonDays <= 10 || /week/i.test(horizon)) return "weekly";
  if (roundId.endsWith("-1M") || horizonDays >= 28 || /month/i.test(horizon)) return "monthly";
  return "other";
}

function trackLabel(track) {
  if (track === "weekly") return "Weekly";
  if (track === "monthly") return "Monthly";
  return "";
}

function latestResolvedRound(rounds, track) {
  return rounds
    .filter((round) => round.status === "resolved" && (!track || roundTrack(round) === track))
    .sort(
      (left, right) =>
        String(right.exit_date ?? "").localeCompare(String(left.exit_date ?? "")) ||
        String(right.decision_deadline_utc ?? "").localeCompare(String(left.decision_deadline_utc ?? "")) ||
        String(right.round_id ?? "").localeCompare(String(left.round_id ?? ""))
    )[0];
}

function latestPriceClose(readModel) {
  return (readModel.interim_performance ?? []).reduce(
    (latest, row) => (String(row.price_date ?? "") > latest ? String(row.price_date ?? "") : latest),
    ""
  );
}

function nextScheduledScore(activeRounds, latestPriceDate) {
  return activeRounds
    .map((round) => String(round.exit_date ?? "").slice(0, 10))
    .filter((date) => date && (!latestPriceDate || date > latestPriceDate))
    .sort()[0] ?? "";
}

export function buildBenchmarkStatus(readModel, options = {}) {
  const track = options.track === "weekly" || options.track === "monthly" ? options.track : undefined;
  const resolvedTrackLabel = trackLabel(track);
  const rounds = readModel.rounds ?? [];
  const activeRounds = rounds.filter((round) => round.status === "active" && (!track || roundTrack(round) === track));
  const latestOfficial = latestResolvedRound(rounds, track);
  const latestPriceDate = latestPriceClose(readModel);
  const nextScoreDate = nextScheduledScore(activeRounds, latestPriceDate);

  return {
    latestOfficialLabel: resolvedTrackLabel ? `Latest ${resolvedTrackLabel.toLowerCase()} score` : "Latest official score",
    latestOfficialRoundId: latestOfficial?.round_id ?? "No official score",
    latestOfficialRoundHref: latestOfficial?.round_id ? `/rounds/${latestOfficial.round_id}/` : "/leaderboards/latest",
    liveRoundLabel: resolvedTrackLabel ? `${resolvedTrackLabel} live` : "Live rounds",
    liveRoundCount: activeRounds.length,
    latestPriceDate,
    latestPriceLabel: shortDate(latestPriceDate),
    nextScoreDate,
    nextScoreLabel: shortDate(nextScoreDate),
    refreshedAt: readModel.generated_at ?? "",
    refreshedAtLabel: refreshTimestamp(readModel.generated_at)
  };
}

export { refreshTimestamp, shortDate };
