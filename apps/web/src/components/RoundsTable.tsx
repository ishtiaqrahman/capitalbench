import { useEffect, useState } from "react";
import { type RoundRecord } from "../data/fallback";
import { dateOnly } from "../lib/format";
import { mergeRemoteRoundRows, publicRoundStatusLabel, type RoundWithAuditPath, withAuditPaths } from "../lib/roundDisplay";
import { fetchPublicRows } from "../lib/supabase";
import { roundTrack, trackLabel } from "../lib/tracks";
import TableIsland, { type Column } from "./TableIsland";

interface Props {
  fallbackRows: RoundRecord[];
}

export default function RoundsTable({ fallbackRows }: Props) {
  const [rows, setRows] = useState<RoundWithAuditPath[]>(withAuditPaths(mergeRemoteRoundRows(fallbackRows, [])));

  useEffect(() => {
    fetchPublicRows<RoundRecord>("rounds", fallbackRows, { column: "decision_deadline_utc", ascending: false }).then((nextRows) =>
      setRows(withAuditPaths(mergeRemoteRoundRows(fallbackRows, nextRows)))
    );
  }, [fallbackRows]);

  const columns: Column<RoundWithAuditPath>[] = [
    {
      key: "round_id",
      label: "Round",
      value: (row) => row.round_id,
      render: (row) => (
        <a className="round-link" href={row.audit_path}>
          <strong>{row.round_id}</strong>
          <span>Open audit packet</span>
        </a>
      )
    },
    {
      key: "track",
      label: "Test Type",
      value: (row) => trackLabel(roundTrack(row)),
      mobile: "primary"
    },
    { key: "status", label: "Status", value: (row) => publicRoundStatusLabel(row.status), mobile: "secondary" },
    { key: "decision_deadline_utc", label: "Portfolios Frozen", value: (row) => dateOnly(row.decision_deadline_utc), mobile: "secondary" },
    { key: "horizon", label: "Length", mobile: "primary" },
    { key: "exit_date", label: "End", value: (row) => dateOnly(row.exit_date), mobile: "primary" },
    { key: "methodology_version", label: "Methodology", mobile: "hidden" },
    { key: "official_run_id", label: "Run ID", mobile: "hidden" },
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
