import { Check, Copy } from "lucide-react";
import { useState } from "react";
import { type HashRecord } from "../data/fallback";
import { shortHash } from "../lib/format";
import TableIsland, { type Column } from "./TableIsland";

interface Props {
  rows: HashRecord[];
}

export default function HashTable({ rows }: Props) {
  const [copied, setCopied] = useState<string | null>(null);

  async function copyHash(row: HashRecord) {
    await navigator.clipboard.writeText(row.sha256);
    setCopied(row.path);
    window.setTimeout(() => setCopied(null), 1400);
  }

  const columns: Column<HashRecord>[] = [
    { key: "path", label: "Artifact" },
    {
      key: "sha256",
      label: "SHA-256",
      render: (row) => (
        <div className="hash-row">
          <span className="mono">{shortHash(row.sha256)}</span>
          <button className="icon-button" type="button" onClick={() => copyHash(row)} aria-label={`Copy ${row.path} hash`}>
            {copied === row.path ? <Check size={15} aria-hidden="true" /> : <Copy size={15} aria-hidden="true" />}
          </button>
        </div>
      ),
      value: (row) => row.sha256
    }
  ];

  return (
    <TableIsland
      rows={rows}
      columns={columns}
      tableLabel="Audit hashes"
      emptyText="No audit hashes are published yet."
      csvFilename="capitalbench-audit-hashes.csv"
    />
  );
}
