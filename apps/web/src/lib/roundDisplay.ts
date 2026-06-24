import type { RoundRecord } from "../data/fallback";

type RuntimeRoundStatus = RoundRecord["status"] | "active" | string | undefined;

export type RoundWithAuditPath = RoundRecord & {
  audit_path: string;
};

export function roundAuditPath(roundId: string): string {
  return `/rounds/${roundId}/`;
}

export function normalizeRoundStatus(status: RuntimeRoundStatus): RoundRecord["status"] {
  if (status === "resolved" || status === "overdue" || status === "archived") return status;
  return "pending";
}

export function publicRoundStatusLabel(status: RuntimeRoundStatus): string {
  const normalized = normalizeRoundStatus(status);
  if (normalized === "resolved") return "scored";
  if (normalized === "overdue") return "resolution due";
  return normalized;
}

export function isOpenRound(row: Pick<RoundRecord, "status">): boolean {
  const status = normalizeRoundStatus(row.status);
  return status === "pending" || status === "overdue";
}

export function withAuditPaths(rows: RoundRecord[]): RoundWithAuditPath[] {
  return rows.map((row) => ({
    ...row,
    audit_path: roundAuditPath(row.round_id)
  }));
}

export function mergeRemoteRoundRows(fallbackRows: RoundRecord[], remoteRows: RoundRecord[]): RoundRecord[] {
  const fallbackById = new Map(fallbackRows.map((row) => [row.round_id, row]));
  const mergedById = new Map<string, RoundRecord>();
  for (const row of fallbackRows) {
    mergedById.set(row.round_id, {
      ...row,
      status: normalizeRoundStatus(row.status)
    });
  }
  for (const remoteRow of remoteRows) {
    const fallbackRow = fallbackById.get(remoteRow.round_id);
    const remoteStatus = normalizeRoundStatus(remoteRow.status);
    const fallbackStatus = normalizeRoundStatus(fallbackRow?.status);
    const merged = {
      ...(fallbackRow ?? {}),
      ...remoteRow,
      status: fallbackStatus !== "pending" && remoteStatus === "pending" ? fallbackStatus : remoteStatus
    } as RoundRecord;
    mergedById.set(remoteRow.round_id, merged);
  }
  return Array.from(mergedById.values()).sort((left, right) =>
    String(right.decision_deadline_utc ?? "").localeCompare(String(left.decision_deadline_utc ?? ""))
  );
}
