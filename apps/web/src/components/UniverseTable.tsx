import { useEffect, useState } from "react";
import { type UniverseOption } from "../data/fallback";
import { getSupabaseClient, hasSupabaseConfig } from "../lib/supabase";
import TableIsland, { type Column } from "./TableIsland";

interface Props {
  fallbackRows: UniverseOption[];
  roundId?: string;
  disableRemote?: boolean;
}

export default function UniverseTable({ fallbackRows, roundId, disableRemote = false }: Props) {
  const [rows, setRows] = useState<UniverseOption[]>(fallbackRows);

  useEffect(() => {
    if (disableRemote || !roundId) return;
    const supabase = getSupabaseClient();
    if (!hasSupabaseConfig() || supabase === null) return;
    supabase
      .from("options")
      .select("option_id,name,symbol,asset_class,option_group,risk_bucket,is_cash,is_benchmark,sort_order")
      .eq("published", true)
      .eq("round_id", roundId)
      .order("sort_order", { ascending: true, nullsFirst: false })
      .order("option_id", { ascending: true })
      .then(({ data, error }) => {
        if (!error && data) setRows(data as UniverseOption[]);
      });
  }, [disableRemote, roundId]);

  const columns: Column<UniverseOption>[] = [
    { key: "option_id", label: "Option ID", mobile: "primary" },
    { key: "name", label: "Name", mobile: "primary" },
    { key: "symbol", label: "Symbol", mobile: "primary" },
    { key: "asset_class", label: "Asset Class", mobile: "hidden" },
    { key: "option_group", label: "Group", mobile: "hidden" },
    { key: "risk_bucket", label: "Risk", mobile: "secondary" }
  ];

  return (
    <TableIsland
      rows={rows}
      columns={columns}
      tableLabel="CapitalBench option universe"
      emptyText="No option universe is published yet."
      csvFilename="capitalbench-universe.csv"
      initialSortKey="sort_order"
    />
  );
}
