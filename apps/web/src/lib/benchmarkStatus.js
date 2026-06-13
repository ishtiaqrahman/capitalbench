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

function latestResolvedRound(rounds) {
  return rounds
    .filter((round) => round.status === "resolved")
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

export function buildBenchmarkStatus(readModel) {
  const rounds = readModel.rounds ?? [];
  const activeRounds = rounds.filter((round) => round.status === "active");
  const latestOfficial = latestResolvedRound(rounds);
  const latestPriceDate = latestPriceClose(readModel);
  const nextScoreDate = nextScheduledScore(activeRounds, latestPriceDate);

  return {
    latestOfficialRoundId: latestOfficial?.round_id ?? "No official score",
    latestOfficialRoundHref: latestOfficial?.round_id ? `/rounds/${latestOfficial.round_id}/` : "/leaderboards/latest",
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
