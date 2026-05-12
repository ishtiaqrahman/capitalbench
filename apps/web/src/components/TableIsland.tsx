import { ArrowUpDown, Download, Search } from "lucide-react";
import type { ReactNode } from "react";
import { useMemo, useState } from "react";

export interface Column<T> {
  key: keyof T | string;
  label: string;
  align?: "left" | "right";
  value?: (row: T) => string | number | null | undefined;
  render?: (row: T) => ReactNode;
}

interface Props<T> {
  rows: T[];
  columns: Column<T>[];
  emptyText: string;
  tableLabel: string;
  csvFilename?: string;
}

function rawValue<T>(row: T, column: Column<T>): string | number {
  const value = column.value ? column.value(row) : (row as Record<string, unknown>)[String(column.key)];
  if (value === null || value === undefined) return "";
  return typeof value === "number" ? value : String(value);
}

function csvEscape(value: string | number): string {
  const text = String(value);
  if (/[",\n]/.test(text)) {
    return `"${text.replaceAll('"', '""')}"`;
  }
  return text;
}

export default function TableIsland<T extends object>({
  rows,
  columns,
  emptyText,
  tableLabel,
  csvFilename = "capitalbench-table.csv"
}: Props<T>) {
  const [query, setQuery] = useState("");
  const [sortKey, setSortKey] = useState<string>(String(columns[0]?.key ?? ""));
  const [sortDirection, setSortDirection] = useState<"asc" | "desc">("asc");

  const sortedRows = useMemo(() => {
    const normalizedQuery = query.trim().toLowerCase();
    const filtered = normalizedQuery
      ? rows.filter((row) =>
          columns.some((column) => String(rawValue(row, column)).toLowerCase().includes(normalizedQuery))
        )
      : rows;
    const column = columns.find((item) => String(item.key) === sortKey) ?? columns[0];
    return [...filtered].sort((a, b) => {
      const aValue = rawValue(a, column);
      const bValue = rawValue(b, column);
      const result =
        typeof aValue === "number" && typeof bValue === "number"
          ? aValue - bValue
          : String(aValue).localeCompare(String(bValue), undefined, { numeric: true });
      return sortDirection === "asc" ? result : -result;
    });
  }, [columns, query, rows, sortDirection, sortKey]);

  function updateSort(nextKey: string) {
    if (nextKey === sortKey) {
      setSortDirection(sortDirection === "asc" ? "desc" : "asc");
      return;
    }
    setSortKey(nextKey);
    setSortDirection("asc");
  }

  function exportCsv() {
    const header = columns.map((column) => csvEscape(column.label)).join(",");
    const body = sortedRows
      .map((row) => columns.map((column) => csvEscape(rawValue(row, column))).join(","))
      .join("\n");
    const blob = new Blob([`${header}\n${body}\n`], { type: "text/csv;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = csvFilename;
    anchor.click();
    URL.revokeObjectURL(url);
  }

  return (
    <div className="table-shell" aria-label={tableLabel}>
      <div className="table-toolbar">
        <label className="search-box">
          <Search size={16} aria-hidden="true" />
          <input
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Search"
            aria-label={`Search ${tableLabel}`}
          />
        </label>
        <button className="icon-button" type="button" onClick={exportCsv} aria-label="Export CSV" title="Export CSV">
          <Download size={17} aria-hidden="true" />
        </button>
      </div>
      <div className="table-scroll">
        <table>
          <thead>
            <tr>
              {columns.map((column) => (
                <th key={String(column.key)} className={column.align === "right" ? "numeric" : ""}>
                  <button type="button" onClick={() => updateSort(String(column.key))}>
                    <span>{column.label}</span>
                    <ArrowUpDown size={14} aria-hidden="true" />
                  </button>
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {sortedRows.map((row, index) => (
              <tr key={String((row as Record<string, unknown>).id ?? (row as Record<string, unknown>).model_id ?? index)}>
                {columns.map((column) => (
                  <td
                    key={String(column.key)}
                    className={column.align === "right" ? "numeric" : ""}
                    data-label={column.label}
                  >
                    {column.render ? column.render(row) : rawValue(row, column)}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {sortedRows.length === 0 && <p className="empty-state">{emptyText}</p>}
    </div>
  );
}
