import { Clock3 } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import type { RoundStatus, ScoreEtaSource } from "../data/fallback";

interface Props {
  scoreEtaUtc?: string;
  status: RoundStatus;
  label?: string;
  source?: ScoreEtaSource;
  exitDate?: string;
  compact?: boolean;
  showIcon?: boolean;
  initialNowIso?: string;
}

const MINUTE_MS = 60_000;
const HOUR_MS = 60 * MINUTE_MS;
const DAY_MS = 24 * HOUR_MS;

function pad(value: number): string {
  return String(value).padStart(2, "0");
}

function targetLabel(scoreEtaUtc?: string, source?: ScoreEtaSource, exitDate?: string): string {
  if (!scoreEtaUtc) return exitDate ? `Exit date: ${exitDate}` : "Score ETA unavailable";
  const target = new Date(scoreEtaUtc);
  if (!Number.isFinite(target.getTime())) return exitDate ? `Exit date: ${exitDate}` : "Score ETA unavailable";
  const formatted = new Intl.DateTimeFormat("en", {
    month: "short",
    day: "numeric",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    hourCycle: "h23",
    timeZone: "UTC",
    timeZoneName: "short"
  }).format(target);
  return source === "automation" ? `Target: ${formatted}` : `Estimated target: ${formatted}`;
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

function compactText(parts: NonNullable<ReturnType<typeof partsUntil>>): string {
  if (parts.reached) return "Window reached";
  if (parts.days > 0) return `${parts.days}d ${parts.hours}h`;
  if (parts.hours > 0) return `${parts.hours}h ${pad(parts.minutes)}m`;
  return `${parts.minutes}m ${pad(parts.seconds)}s`;
}

function ariaText(parts: NonNullable<ReturnType<typeof partsUntil>> | null, status: RoundStatus): string {
  if (status === "resolved") return "Scores published.";
  if (!parts) return "Score ETA unavailable.";
  if (parts.reached) return "Scoring window reached. Waiting for score publication.";
  const segments = [];
  if (parts.days) segments.push(`${parts.days} ${parts.days === 1 ? "day" : "days"}`);
  if (parts.hours) segments.push(`${parts.hours} ${parts.hours === 1 ? "hour" : "hours"}`);
  if (!parts.days && parts.minutes) segments.push(`${parts.minutes} ${parts.minutes === 1 ? "minute" : "minutes"}`);
  return `Score ETA: ${segments.join(", ") || "less than one minute"}.`;
}

export default function ScoreCountdown({
  scoreEtaUtc,
  status,
  label = "Score ETA",
  source,
  exitDate,
  compact = false,
  showIcon = false,
  initialNowIso
}: Props) {
  const initialNow = useMemo(() => {
    const parsed = initialNowIso ? Date.parse(initialNowIso) : Number.NaN;
    return Number.isFinite(parsed) ? parsed : Date.now();
  }, [initialNowIso]);
  const [now, setNow] = useState(initialNow);

  useEffect(() => {
    const interval = window.setInterval(() => setNow(Date.now()), 1000);
    return () => window.clearInterval(interval);
  }, []);

  const parts = partsUntil(scoreEtaUtc, now);
  const target = targetLabel(scoreEtaUtc, source, exitDate);
  const isResolved = status === "resolved";
  const isReached = !isResolved && parts?.reached;
  const statusClass = isResolved ? "resolved" : isReached ? "reached" : "pending";

  return (
    <div className={`score-countdown ${compact ? "compact" : ""} ${statusClass}`} aria-label={ariaText(parts, status)} title={target}>
      <div className="score-countdown-head">
        {showIcon && <Clock3 size={15} aria-hidden="true" />}
        <span className="score-countdown-kicker">{label}</span>
      </div>
      {isResolved ? (
        <strong className="score-countdown-status">Scores published</strong>
      ) : isReached ? (
        <strong className="score-countdown-status">Scoring window reached</strong>
      ) : parts ? (
        compact ? (
          <strong className="score-countdown-compact-value" aria-hidden="true">{compactText(parts)}</strong>
        ) : (
          <div className="score-countdown-value" aria-hidden="true">
            <span>
              <b>{parts.days}</b>
              <small>d</small>
            </span>
            <span>
              <b>{pad(parts.hours)}</b>
              <small>h</small>
            </span>
            <span>
              <b>{pad(parts.minutes)}</b>
              <small>m</small>
            </span>
            <span className="score-countdown-seconds">
              <b>{pad(parts.seconds)}</b>
              <small>s</small>
            </span>
          </div>
        )
      ) : (
        <strong className="score-countdown-status">Exit date pending</strong>
      )}
      <p>{isReached ? "Waiting for score publication" : target}</p>
    </div>
  );
}

