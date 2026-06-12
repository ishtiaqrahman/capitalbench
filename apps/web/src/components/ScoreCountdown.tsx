import { Clock3 } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import type { RoundStatus, ScoreEtaSource } from "../data/fallback";

type ScoreCountdownVariant = "hero" | "panel" | "inline" | "chip";
type ScoreCountdownPrecision = "days" | "hours";

interface Props {
  scoreEtaUtc?: string;
  status: RoundStatus;
  label?: string;
  source?: ScoreEtaSource;
  exitDate?: string;
  compact?: boolean;
  showIcon?: boolean;
  initialNowIso?: string;
  variant?: ScoreCountdownVariant;
  precision?: ScoreCountdownPrecision;
  showRemaining?: boolean;
  metaText?: string;
}

const MINUTE_MS = 60_000;
const HOUR_MS = 60 * MINUTE_MS;
const DAY_MS = 24 * HOUR_MS;

function plural(value: number, unit: string): string {
  return `${value} ${unit}${value === 1 ? "" : "s"}`;
}

function formatTarget(scoreEtaUtc?: string, mode: "date" | "datetime" = "datetime", exitDate?: string): string {
  const target = scoreEtaUtc ? new Date(scoreEtaUtc) : null;
  if (!target || !Number.isFinite(target.getTime())) return exitDate ?? "Target pending";
  return new Intl.DateTimeFormat("en", {
    month: "short",
    day: "numeric",
    year: "numeric",
    ...(mode === "datetime"
      ? {
          hour: "2-digit",
          minute: "2-digit",
          hourCycle: "h23" as const,
          timeZoneName: "short" as const
        }
      : {}),
    timeZone: "UTC",
  }).format(target);
}

function partsUntil(scoreEtaUtc: string | undefined, now: number) {
  const targetMs = scoreEtaUtc ? Date.parse(scoreEtaUtc) : Number.NaN;
  if (!Number.isFinite(targetMs)) return null;
  const remainingMs = targetMs - now;
  if (remainingMs <= 0) return { reached: true, days: 0, hours: 0, minutes: 0, seconds: 0 };
  const days = Math.floor(remainingMs / DAY_MS);
  const hours = Math.floor((remainingMs % DAY_MS) / HOUR_MS);
  const minutes = Math.floor((remainingMs % HOUR_MS) / MINUTE_MS);
  const seconds = Math.floor((remainingMs % MINUTE_MS) / 1000);
  return { reached: false, days, hours, minutes, seconds };
}

function remainingText(
  parts: NonNullable<ReturnType<typeof partsUntil>> | null,
  precision: ScoreCountdownPrecision,
  approximate = false
): string {
  if (!parts) return "Timing pending";
  if (parts.reached) return "Scoring window reached";
  if (approximate && precision === "days" && parts.days > 0) return `~${parts.days}d remaining`;
  const prefix = approximate ? "~" : "";
  if (precision === "days" && parts.days > 0) return `${prefix}${plural(parts.days, "day")} remaining`;
  if (parts.days > 0) {
    const hours = parts.hours > 0 ? `, ${plural(parts.hours, "hour")}` : "";
    return `${plural(parts.days, "day")}${hours} remaining`;
  }
  if (parts.hours > 0) return `${plural(parts.hours, "hour")} remaining`;
  return "Less than one hour remaining";
}

function ariaText(parts: NonNullable<ReturnType<typeof partsUntil>> | null, status: RoundStatus): string {
  if (status === "resolved") return "Scores published.";
  if (status === "overdue") return "Scoring window passed. Waiting for score publication.";
  if (!parts) return "Scoring target unavailable.";
  if (parts.reached) return "Scoring window reached. Waiting for score publication.";
  const segments = [];
  if (parts.days) segments.push(`${parts.days} ${parts.days === 1 ? "day" : "days"}`);
  if (parts.hours) segments.push(`${parts.hours} ${parts.hours === 1 ? "hour" : "hours"}`);
  if (!parts.days && parts.minutes) segments.push(`${parts.minutes} ${parts.minutes === 1 ? "minute" : "minutes"}`);
  return `Scoring target: ${segments.join(", ") || "less than one hour"}.`;
}

function statusTarget(status: RoundStatus, parts: NonNullable<ReturnType<typeof partsUntil>> | null, target: string): string {
  if (status === "resolved") return "Scores published";
  if (status === "overdue") return "Resolution due";
  if (parts?.reached) return "Scoring window reached";
  return target;
}

export default function ScoreCountdown({
  scoreEtaUtc,
  status,
  label = "Scoring target",
  source,
  exitDate,
  compact = false,
  showIcon = false,
  initialNowIso,
  variant,
  precision = "hours",
  showRemaining = true,
  metaText
}: Props) {
  const resolvedVariant = variant ?? (compact ? "chip" : "hero");
  const initialNow = useMemo(() => {
    const parsed = initialNowIso ? Date.parse(initialNowIso) : Number.NaN;
    return Number.isFinite(parsed) ? parsed : Date.now();
  }, [initialNowIso]);
  const [now, setNow] = useState(initialNow);

  useEffect(() => {
    const interval = window.setInterval(() => setNow(Date.now()), MINUTE_MS);
    return () => window.clearInterval(interval);
  }, []);

  const parts = partsUntil(scoreEtaUtc, now);
  const targetMode = resolvedVariant === "chip" || resolvedVariant === "inline" ? "date" : "datetime";
  const target = formatTarget(scoreEtaUtc, targetMode, exitDate);
  const isResolved = status === "resolved";
  const isOverdue = status === "overdue";
  const isReached = !isResolved && parts?.reached;
  const statusClass = isResolved ? "resolved" : isOverdue ? "overdue" : isReached ? "reached" : "pending";
  const targetText = statusTarget(status, parts, target);
  const remaining = isOverdue ? "Waiting for score publication" : isReached ? "Waiting for score publication" : remainingText(parts, precision, resolvedVariant === "chip");
  const shouldShowIcon = showIcon || resolvedVariant === "panel";
  const sourceLabel = source === "automation" ? "Automation target" : source === "derived" ? "Estimated from exit date" : "Scoring target";
  const displayedMeta = isResolved ? "Leaderboard is live" : metaText ?? (showRemaining ? remaining : sourceLabel);
  const title = `${sourceLabel}: ${target}`;

  return (
    <div
      className={`score-countdown score-countdown-${resolvedVariant} ${statusClass}`}
      aria-label={ariaText(parts, status)}
      title={title}
    >
      <div className="score-countdown-head">
        {!shouldShowIcon && <span className="score-countdown-dot" aria-hidden="true" />}
        {shouldShowIcon && <Clock3 size={15} aria-hidden="true" />}
        <span className="score-countdown-kicker">{label}</span>
      </div>
      <strong className="score-countdown-target">{targetText}</strong>
      <p className="score-countdown-meta">{displayedMeta}</p>
    </div>
  );
}
