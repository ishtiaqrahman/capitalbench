export function pct(value: number | string | null | undefined): string {
  if (value === null || value === undefined || value === "") return "";
  const numeric = typeof value === "number" ? value : Number(value);
  if (!Number.isFinite(numeric)) return "";
  return `${(numeric * 100).toFixed(2)}%`;
}

export function number(value: number | string | null | undefined, digits = 2): string {
  if (value === null || value === undefined || value === "") return "";
  const numeric = typeof value === "number" ? value : Number(value);
  if (!Number.isFinite(numeric)) return "";
  return numeric.toFixed(digits);
}

export function dateOnly(value: string | null | undefined): string {
  if (!value) return "";
  return value.slice(0, 10);
}

export function shortHash(value: string): string {
  return `${value.slice(0, 12)}...${value.slice(-8)}`;
}
