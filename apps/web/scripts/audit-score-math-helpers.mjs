export function numberValue(value) {
  if (value === undefined || value === null || value === "") return null;
  const numeric = Number(value);
  return Number.isFinite(numeric) ? numeric : null;
}

function decimalToPct(value) {
  return value * 100;
}

export function pctLabel(value) {
  if (typeof value !== "number" || !Number.isFinite(value)) return "n/a";
  return `${decimalToPct(value).toFixed(4)}%`;
}

export function scoreLabel(value) {
  if (typeof value !== "number" || !Number.isFinite(value)) return "n/a";
  return value.toFixed(1);
}

export function portfolioReturnValue(row) {
  return numberValue(row?.portfolio_return) ?? numberValue(row?.selected_asset_return);
}
