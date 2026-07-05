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

function utcDateFromValue(value) {
  if (!value) return null;

  const [year, month, day] = String(value).slice(0, 10).split("-").map(Number);
  if (!year || !month || !day) return null;

  const date = new Date(Date.UTC(year, month - 1, day));
  return Number.isFinite(date.getTime()) ? date : null;
}

function fallbackDateText(value, fallback) {
  return value ? String(value).slice(0, 10) : fallback;
}

export function shortMonthDay(value, fallback = "") {
  const date = utcDateFromValue(value);
  if (!date) return fallbackDateText(value, fallback);
  return new Intl.DateTimeFormat("en-US", { month: "short", day: "numeric", timeZone: "UTC" }).format(date);
}

export function longMonthDayYear(value, fallback = "") {
  const date = utcDateFromValue(value);
  if (!date) return fallbackDateText(value, fallback);
  return new Intl.DateTimeFormat("en-US", { month: "long", day: "numeric", year: "numeric", timeZone: "UTC" }).format(date);
}

export function dateFromRoundId(roundId) {
  const match = roundId?.match(/^CB-(\d{4}-\d{2}-\d{2})-/);
  return match?.[1] ?? "";
}

export function pairedPulseDateLabel(weeklyDate, monthlyDate) {
  const weekly = shortMonthDay(weeklyDate);
  const monthly = shortMonthDay(monthlyDate);
  if (weekly && monthly && weekly === monthly) return weekly;
  if (weekly && monthly) return `${monthly} monthly + ${weekly} weekly`;
  return monthly || weekly || "";
}

export function pairedPulseFullDateLabel(weeklyDate, monthlyDate) {
  const weekly = longMonthDayYear(weeklyDate);
  const monthly = longMonthDayYear(monthlyDate);
  if (weekly && monthly && weekly === monthly) return weekly;
  if (weekly && monthly) return `${monthly} monthly + ${weekly} weekly`;
  return monthly || weekly || "";
}

export function currentRiskDateLabel(pulse, fallback = "Latest active portfolios") {
  const label = pairedPulseFullDateLabel(pulse?.weekly?.decision_date, pulse?.monthly?.decision_date);
  return label ? `As of ${label}` : fallback;
}

export function pulseDateLabel(pulse, fallback = "Latest decision") {
  const label = longMonthDayYear(pulse?.decision_date);
  return label ? `As of ${label}` : fallback;
}
