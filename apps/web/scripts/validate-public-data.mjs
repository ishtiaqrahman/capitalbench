import { existsSync } from "node:fs";
import { join, resolve } from "node:path";
import apiReadModel from "../src/generated/apiReadModel.js";

const repoRoot = resolve(process.cwd(), "../..");
const failures = [];

function resultPath(round, filename) {
  return join(repoRoot, "rounds", round.round_id, "runs", round.official_run_id, "results", filename);
}

function rowsForRound(rows, roundId) {
  return rows.filter((row) => row.round_id === roundId);
}

for (const round of apiReadModel.rounds) {
  if (!round.official_run_id) continue;

  const leaderboardExists = existsSync(resultPath(round, "leaderboard.csv"));
  const returnsExists = existsSync(resultPath(round, "returns.csv"));
  const resultRows = rowsForRound(apiReadModel.results, round.round_id);
  const returnRows = rowsForRound(apiReadModel.returns, round.round_id);

  if (round.status === "resolved" && !leaderboardExists) {
    failures.push(`${round.round_id} is resolved but missing leaderboard.csv`);
  }
  if (round.status === "resolved" && !returnsExists) {
    failures.push(`${round.round_id} is resolved but missing returns.csv`);
  }
  if (round.status === "resolved" && resultRows.length === 0) {
    failures.push(`${round.round_id} is resolved but has no generated result rows`);
  }
  if (round.status === "resolved" && returnRows.length === 0) {
    failures.push(`${round.round_id} is resolved but has no generated asset-return rows`);
  }
  if (round.status === "active" && resultRows.length > 0) {
    failures.push(`${round.round_id} is active but has generated final result rows`);
  }
  if (resultRows.length > 0 && (!leaderboardExists || !returnsExists)) {
    failures.push(`${round.round_id} has generated result rows without complete canonical result files`);
  }
}

const cumulativeTracks = ["weekly", "monthly"];
for (const track of cumulativeTracks) {
  const rows = apiReadModel.results.filter((row) => row.track === track);
  if (rows.length === 0) continue;
  const roundIds = Array.from(new Set(rows.map((row) => row.round_id)));
  const latestRoundId = roundIds.sort((left, right) => {
    const leftRound = apiReadModel.rounds.find((round) => round.round_id === left);
    const rightRound = apiReadModel.rounds.find((round) => round.round_id === right);
    return `${leftRound?.exit_date ?? ""}:${left}`.localeCompare(`${rightRound?.exit_date ?? ""}:${right}`);
  })[roundIds.length - 1];
  const latestRosterSize = new Set(rows.filter((row) => row.round_id === latestRoundId).map((row) => row.model_id)).size;
  if (latestRosterSize === 0) {
    failures.push(`${track} cumulative data has no latest roster`);
  }
}

if (failures.length > 0) {
  console.error("Public data validation failed:");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(
  JSON.stringify({
    ok: true,
    rounds: apiReadModel.rounds.length,
    results: apiReadModel.results.length,
    returns: apiReadModel.returns.length
  })
);
