import { useEffect, useState } from "react";
import { type RoundRecord } from "../data/fallback";
import { dateOnly } from "../lib/format";
import { fetchPublicRows } from "../lib/supabase";
import TableIsland, { type Column } from "./TableIsland";

interface Props {
  fallbackRows: RoundRecord[];
}

export default function RoundsTable({ fallbackRows }: Props) {
  const [rows, setRows] = useState<RoundRecord[]>(fallbackRows);

  useEffect(() => {
    fetchPublicRows<RoundRecord>("rounds", fallbackRows, { column: "decision_deadline_utc", ascending: false }).then(setRows);
  }, [fallbackRows]);

  const columns: Column<RoundRecord>[] = [
    { key: "round_id", label: "Round" },
    { key: "status", label: "Status" },
    { key: "decision_deadline_utc", label: "Decision", value: (row) => dateOnly(row.decision_deadline_utc) },
    { key: "exit_date", label: "Exit", value: (row) => dateOnly(row.exit_date) },
    { key: "methodology_version", label: "Methodology" },
    { key: "official_run_id", label: "Official Run" }
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
