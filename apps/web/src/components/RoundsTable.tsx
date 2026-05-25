import { useEffect, useState } from "react";
import { type RoundRecord } from "../data/fallback";
import { dateOnly } from "../lib/format";
import { fetchPublicRows } from "../lib/supabase";
import { roundTrack, trackLabel } from "../lib/tracks";
import TableIsland, { type Column } from "./TableIsland";

interface Props {
  fallbackRows: RoundRecord[];
}

type RoundTableRow = RoundRecord & {
  audit_path: string;
};

function withAuditPaths(rows: RoundRecord[]): RoundTableRow[] {
  return rows.map((row) => ({
    ...row,
    audit_path: `/rounds/${row.round_id}/`
  }));
}

export default function RoundsTable({ fallbackRows }: Props) {
  const [rows, setRows] = useState<RoundTableRow[]>(withAuditPaths(fallbackRows));

  useEffect(() => {
    fetchPublicRows<RoundRecord>("rounds", fallbackRows, { column: "decision_deadline_utc", ascending: false }).then((nextRows) =>
      setRows(withAuditPaths(nextRows))
    );
  }, [fallbackRows]);

  const columns: Column<RoundTableRow>[] = [
    {
      key: "round_id",
      label: "Round",
      value: (row) => row.round_id,
      render: (row) => (
        <a className="round-link" href={row.audit_path}>
          <strong>{row.round_id}</strong>
          <span>Open round packet</span>
        </a>
      )
    },
    {
      key: "track",
      label: "Track",
      value: (row) => trackLabel(roundTrack(row)),
      mobile: "primary"
    },
    { key: "status", label: "Status", mobile: "secondary" },
    { key: "decision_deadline_utc", label: "Decision", value: (row) => dateOnly(row.decision_deadline_utc), mobile: "secondary" },
    { key: "horizon", label: "Horizon", mobile: "primary" },
    { key: "exit_date", label: "Exit", value: (row) => dateOnly(row.exit_date), mobile: "primary" },
    { key: "methodology_version", label: "Methodology", mobile: "hidden" },
    { key: "official_run_id", label: "Official Run", mobile: "hidden" },
    {
      key: "audit_path",
      label: "Audit",
      mobile: "hidden",
      value: (row) => row.audit_path,
      render: (row) => (
        <a className="small-button table-action-link" href={row.audit_path}>
          View
        </a>
      )
    }
  ];

  return (
    <TableIsland
      rows={rows}
      columns={columns}
      tableLabel="CapitalBench rounds"
      emptyText="No rounds are published yet."
      csvFilename="capitalbench-rounds.csv"
    />
  );
}
