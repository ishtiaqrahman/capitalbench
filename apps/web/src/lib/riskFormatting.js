export function signedPulseChangeLabel(value) {
  if (value === null || value === undefined || value === "") return "n/a";

  const numeric = Number(value);
  if (!Number.isFinite(numeric)) return "n/a";

  const absolute = Math.abs(numeric);
  if (absolute < 0.005) return "0.0";

  const digits = absolute < 0.1 ? 2 : 1;
  const sign = numeric > 0 ? "+" : "";
  return `${sign}${numeric.toFixed(digits)}`;
}
