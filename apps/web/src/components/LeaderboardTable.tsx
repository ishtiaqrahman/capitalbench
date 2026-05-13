import { CalendarClock } from "lucide-react";
import { useEffect, useState } from "react";
import { modelLabel, providerLabel, type LeaderboardRecord } from "../data/fallback";
import { pct } from "../lib/format";
import { fetchPublicRows } from "../lib/supabase";
import TableIsland, { type Column } from "./TableIsland";

interface Props {
  fallbackRows: LeaderboardRecord[];
  kind: "latest" | "official" | "stability";
}

const tableByKind = {
  latest: "latest_leaderboard",
  official: "cumulative_official_leaderboard",
  stability: "cumulative_stability_leaderboard"
};

export default function LeaderboardTable({ fallbackRows, kind }: Props) {
  const [rows, setRows] = useState<LeaderboardRecord[]>(fallbackRows);

  useEffect(() => {
    const orderColumn =
      kind === "stability" ? "average_repeated_alpha_vs_sp500" : kind === "official" ? "average_alpha_vs_sp500" : "alpha_vs_sp500";
    fetchPublicRows<LeaderboardRecord>(tableByKind[kind], fallbackRows, {
      column: orderColumn,
      ascending: false
    }).then(setRows);
  }, [fallbackRows, kind]);

  const latestColumns: Column<LeaderboardRecord>[] = [
    { key: "model_id", label: "Model", value: (row) => modelLabel(row.model_id) },
    { key: "provider", label: "Provider", value: (row) => providerLabel(row.provider) },
    { key: "selected_option_id", label: "Pick" },
    { key: "holding_count", label: "Holdings", align: "right" },
    { key: "selected_asset_return", label: "Return", align: "right", value: (row) => pct(row.selected_asset_return) },
    { key: "sp500_return", label: "S&P 500", align: "right", value: (row) => pct(row.sp500_return) },
    { key: "alpha_vs_sp500", label: "Alpha", align: "right", value: (row) => pct(row.alpha_vs_sp500) },
    { key: "rank_among_options", label: "Rank", align: "right" }
  ];

  const officialColumns: Column<LeaderboardRecord>[] = [
    { key: "model_id", label: "Model", value: (row) => modelLabel(row.model_id) },
    { key: "provider", label: "Provider", value: (row) => providerLabel(row.provider) },
    { key: "resolved_rounds", label: "Rounds", align: "right" },
    { key: "average_alpha_vs_sp500", label: "Avg Alpha", align: "right", value: (row) => pct(row.average_alpha_vs_sp500) }
  ];

  const stabilityColumns: Column<LeaderboardRecord>[] = [
    { key: "model_id", label: "Model", value: (row) => modelLabel(row.model_id) },
    { key: "provider", label: "Provider", value: (row) => providerLabel(row.provider) },
    { key: "resolved_rounds", label: "Rounds", align: "right" },
    {
      key: "average_repeated_alpha_vs_sp500",
      label: "Avg Repeated Alpha",
      align: "right",
      value: (row) => pct(row.average_repeated_alpha_vs_sp500)
    },
    { key: "average_consistency_rate", label: "Consistency", align: "right", value: (row) => pct(row.average_consistency_rate) }
  ];

  const columns = kind === "latest" ? latestColumns : kind === "official" ? officialColumns : stabilityColumns;
  const emptyText =
    kind === "latest"
      ? "No resolved official round is published yet. Round 1 remains pending until exit prices are available."
      : "No resolved rounds are published for this leaderboard yet.";

  if (rows.length === 0) {
    return (
      <div className="pending-state">
        <CalendarClock size={22} aria-hidden="true" />
        <strong>{kind === "latest" ? "No resolved official leaderboard yet." : "No cumulative rows yet."}</strong>
        <span>{emptyText}</span>
      </div>
    );
  }

  return (
    <TableIsland
      rows={rows}
      columns={columns}
      tableLabel={`${kind} leaderboard`}
      emptyText={emptyText}
      csvFilename={`capitalbench-${kind}-leaderboard.csv`}
    />
  );
}
