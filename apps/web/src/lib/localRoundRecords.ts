import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { parse as parseYaml } from "yaml";
import { rounds, type RoundRecord } from "../data/fallback";

type RoundManifestYaml = {
  round_id: string;
  title?: string;
  description?: string;
  decision_date?: string;
  decision_deadline?: string;
  horizon?: string;
  entry_date?: string;
  exit_date?: string;
  methodology_version?: string;
  universe_version?: string;
  submission_format?: "single_pick" | "portfolio";
  notes?: string;
};

type RunManifestYaml = {
  run_id?: string;
  run_type?: string;
  official_score_eligible?: boolean;
  operator_selected_official?: boolean;
  methodology_version?: string;
  invalid_submissions?: number;
};

function readYamlFile<T>(path: string): T | null {
  if (!existsSync(path)) return null;
  try {
    return parseYaml(readFileSync(path, "utf-8")) as T;
  } catch {
    return null;
  }
}

function publicOfficialRuns(roundPath: string): Array<{ runId: string; manifest: RunManifestYaml }> {
  const runsPath = join(roundPath, "runs");
  if (!existsSync(runsPath)) return [];
  return readdirSync(runsPath)
    .map((runId) => ({
      runId,
      manifest: readYamlFile<RunManifestYaml>(join(runsPath, runId, "run_manifest.yaml"))
    }))
    .filter((item): item is { runId: string; manifest: RunManifestYaml } => {
      return (
        item.manifest !== null &&
        item.manifest.run_type === "official" &&
        item.manifest.official_score_eligible === true &&
        Number(item.manifest.invalid_submissions ?? 0) === 0
      );
    })
    .sort((a, b) => {
      if (a.manifest.operator_selected_official && !b.manifest.operator_selected_official) return -1;
      if (!a.manifest.operator_selected_official && b.manifest.operator_selected_official) return 1;
      return a.runId.localeCompare(b.runId);
    });
}

function horizonDays(entryDate?: string, exitDate?: string): number {
  if (!entryDate || !exitDate) return 0;
  const start = Date.parse(`${entryDate}T00:00:00Z`);
  const end = Date.parse(`${exitDate}T00:00:00Z`);
  if (!Number.isFinite(start) || !Number.isFinite(end)) return 0;
  return Math.round((end - start) / 86_400_000);
}

function discoverRoundRecord(roundPath: string): RoundRecord | null {
  const manifest = readYamlFile<RoundManifestYaml>(join(roundPath, "manifest.yaml"));
  if (!manifest?.round_id) return null;
  const fallback = rounds.find((item) => item.round_id === manifest.round_id);
  const selectedRun = publicOfficialRuns(roundPath)[0];
  const hasScoredResults =
    selectedRun !== undefined &&
    existsSync(join(roundPath, "runs", selectedRun.runId, "results", "leaderboard.csv"));
  return {
    round_id: manifest.round_id,
    title: manifest.title ?? fallback?.title ?? manifest.round_id,
    description: manifest.description ?? fallback?.description ?? "CapitalBench benchmark round.",
    decision_date: manifest.decision_date ?? fallback?.decision_date ?? "",
    decision_deadline_utc: manifest.decision_deadline ?? fallback?.decision_deadline_utc ?? "",
    horizon: manifest.horizon ?? fallback?.horizon ?? "one month",
    horizon_days: fallback?.horizon_days ?? horizonDays(manifest.entry_date, manifest.exit_date),
    entry_date: manifest.entry_date ?? fallback?.entry_date ?? "",
    exit_date: manifest.exit_date ?? fallback?.exit_date ?? "",
    status: hasScoredResults ? "resolved" : fallback?.status ?? "pending",
    methodology_version:
      selectedRun?.manifest.methodology_version ??
      manifest.methodology_version ??
      fallback?.methodology_version ??
      "",
    universe_version: manifest.universe_version ?? fallback?.universe_version,
    submission_format: manifest.submission_format ?? fallback?.submission_format ?? "single_pick",
    official_run_id: selectedRun?.runId ?? fallback?.official_run_id ?? "",
    stability_run_id: fallback?.stability_run_id,
    notes: manifest.notes ?? fallback?.notes ?? ""
  };
}

export function staticRoundRecords(): RoundRecord[] {
  const byId = new Map(rounds.map((round) => [round.round_id, round]));
  const roundsRoot = join(repoRootPath(), "rounds");
  if (existsSync(roundsRoot)) {
    for (const entry of readdirSync(roundsRoot, { withFileTypes: true })) {
      if (!entry.isDirectory() || !entry.name.startsWith("CB-")) continue;
      const record = discoverRoundRecord(join(roundsRoot, entry.name));
      if (record) byId.set(record.round_id, record);
    }
  }
  return Array.from(byId.values()).sort((a, b) => b.decision_deadline_utc.localeCompare(a.decision_deadline_utc));
}

export function repoRootPath(): string {
  const candidates = [resolve(process.cwd()), resolve(process.cwd(), "../..")];
  return (
    candidates.find((candidate) => existsSync(join(candidate, "configs")) && existsSync(join(candidate, "rounds"))) ??
    resolve(process.cwd(), "../..")
  );
}
