import { Activity, Award, CalendarClock, CheckCircle2, Layers } from "lucide-react";
import { useEffect, useMemo, useState, type ReactNode } from "react";
import { modelLabel, type RoundRecord, type SubmissionRecord } from "../data/fallback";
import { dateOnly } from "../lib/format";
import { isOpenRound, mergeRemoteRoundRows, normalizeRoundStatus, roundAuditPath } from "../lib/roundDisplay";
import { fetchPublicRows } from "../lib/supabase";
import { roundTrack, trackLabel, type BenchmarkTrack } from "../lib/tracks";

interface Props {
  fallbackRows: RoundRecord[];
  fallbackSubmissions: SubmissionRecord[];
  latestScoredFallback?: LatestScoredSummary;
}

export interface LatestScoredSummary {
  roundId: string;
  track: BenchmarkTrack | "other";
  winnerModelId?: string;
  modelCount: number;
  exitDate?: string;
}

type KpiTone = "neutral" | "pending" | "resolved" | "overdue" | "blue";

type KpiItem = {
  label: string;
  value: string;
  detail: string;
  href?: string;
  badge?: string;
  tone: KpiTone;
  icon: ReactNode;
};

function formatDate(value: string | undefined): string {
  const day = dateOnly(value);
  if (!day) return "No date";
  const parsed = Date.parse(`${day}T00:00:00Z`);
  if (!Number.isFinite(parsed)) return day;
  return new Intl.DateTimeFormat("en-US", {
    timeZone: "UTC",
    month: "short",
    day: "numeric",
    year: "numeric"
  }).format(parsed);
}

function formatDateTimeUtc(value: string | undefined): string {
  if (!value) return "No scheduled time";
  const parsed = Date.parse(value);
  if (!Number.isFinite(parsed)) return value;
  return new Intl.DateTimeFormat("en-US", {
    timeZone: "UTC",
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "2-digit",
    timeZoneName: "short"
  }).format(parsed);
}

function sortRounds(rows: RoundRecord[]): RoundRecord[] {
  return [...rows].sort((left, right) =>
    String(right.decision_deadline_utc ?? "").localeCompare(String(left.decision_deadline_utc ?? ""))
  );
}

function rowsForTrack(rows: RoundRecord[], track: BenchmarkTrack): RoundRecord[] {
  return rows.filter((round) => roundTrack(round) === track);
}

function sortByScoreEta(rows: RoundRecord[], direction: "asc" | "desc" = "asc"): RoundRecord[] {
  const multiplier = direction === "asc" ? 1 : -1;
  return [...rows].sort((left, right) => {
    const leftValue = left.score_eta_utc || left.exit_date || left.decision_deadline_utc || "";
    const rightValue = right.score_eta_utc || right.exit_date || right.decision_deadline_utc || "";
    return multiplier * leftValue.localeCompare(rightValue);
  });
}

function dueRows(rows: RoundRecord[]): RoundRecord[] {
  const now = Date.now();
  return sortByScoreEta(
    rows.filter((row) => {
      const status = normalizeRoundStatus(row.status);
      if (status === "overdue") return true;
      if (!isOpenRound(row) || !row.score_eta_utc) return false;
      const scoreEta = Date.parse(row.score_eta_utc);
      return Number.isFinite(scoreEta) && scoreEta <= now;
    })
  );
}

function nextScheduledRound(rows: RoundRecord[]): RoundRecord | undefined {
  const now = Date.now();
  const openRows = rows.filter(isOpenRound);
  const scheduledRows = openRows.filter((row) => {
    if (!row.score_eta_utc) return false;
    const scoreEta = Date.parse(row.score_eta_utc);
    return Number.isFinite(scoreEta) && scoreEta > now;
  });
  if (scheduledRows.length > 0) {
    return sortByScoreEta(scheduledRows)[0];
  }
  return sortByScoreEta(openRows)[0];
}

function latestOpenRoundForTrack(rows: RoundRecord[], track: BenchmarkTrack): RoundRecord | undefined {
  return rowsForTrack(sortRounds(rows).filter(isOpenRound), track)[0];
}

function activeDecisionRounds(rows: RoundRecord[]): RoundRecord[] {
  return [latestOpenRoundForTrack(rows, "weekly"), latestOpenRoundForTrack(rows, "monthly")].filter(
    (round): round is RoundRecord => Boolean(round)
  );
}

function submissionCountForRounds(submissions: SubmissionRecord[], rounds: RoundRecord[]): number {
  const runByRound = new Map(rounds.map((round) => [round.round_id, round.official_run_id]));
  return submissions.filter((submission) => {
    const runId = runByRound.get(submission.round_id);
    return Boolean(runId && submission.run_id === runId);
  }).length;
}

function shortRoundId(roundId: string): string {
  return roundId.replace(/^CB-/, "");
}

function formatScoredValue(summary: LatestScoredSummary | undefined): string {
  return summary?.roundId ?? "No scored round";
}

function formatScoredDetail(summary: LatestScoredSummary | undefined): string {
  if (!summary) return "Official result will appear after scoring";
  const date = formatDate(summary.exitDate);
  const winner = summary.winnerModelId ? `Winner: ${modelLabel(summary.winnerModelId)}` : "Winner pending";
  return `${winner} · ${summary.modelCount} models · scored ${date}`;
}

function formatActiveDecisionDetail(rounds: RoundRecord[]): string {
  if (rounds.length === 0) return "No open weekly or monthly rounds";
  return rounds.map((round) => shortRoundId(round.round_id)).join(" + ");
}

function KpiCard({ item }: { item: KpiItem }) {
  const className = `rounds-kpi-card rounds-kpi-card-${item.tone}`;
  const content = (
    <>
      <span className="rounds-kpi-icon" aria-hidden="true">
        {item.icon}
      </span>
      <span className="rounds-kpi-label">{item.label}</span>
      <strong>{item.value}</strong>
      <span className="rounds-kpi-detail">{item.detail}</span>
      {item.badge && <span className={`rounds-kpi-badge status-${item.tone}`}>{item.badge}</span>}
    </>
  );

  if (item.href) {
    return (
      <a className={className} href={item.href} aria-label={`${item.label}: ${item.value}. ${item.detail}`}>
        {content}
      </a>
    );
  }
  return <article className={className}>{content}</article>;
}

export default function RoundsKpiPanel({ fallbackRows, fallbackSubmissions, latestScoredFallback }: Props) {
  const [rows, setRows] = useState<RoundRecord[]>(mergeRemoteRoundRows(fallbackRows, []));

  useEffect(() => {
    fetchPublicRows<RoundRecord>("rounds", fallbackRows, { column: "decision_deadline_utc", ascending: false }).then(
      (nextRows) => setRows(mergeRemoteRoundRows(fallbackRows, nextRows))
    );
  }, [fallbackRows]);

  const items = useMemo<KpiItem[]>(() => {
    const total = rows.length;
    const openRows = rows.filter(isOpenRound);
    const openWeeklyCount = rowsForTrack(openRows, "weekly").length;
    const openMonthlyCount = rowsForTrack(openRows, "monthly").length;
    const rowsDueNow = dueRows(rows);
    const nextRound = nextScheduledRound(rows);
    const activeRounds = activeDecisionRounds(rows);
    const activeSubmissionCount = submissionCountForRounds(fallbackSubmissions, activeRounds);
    const activeTrackSummary = activeRounds.map((round) => trackLabel(roundTrack(round))).join(" + ");
    const overdueCount = rows.filter((row) => normalizeRoundStatus(row.status) === "overdue").length;
    const dueBadge = rowsDueNow.length > 0 ? `${rowsDueNow.length} due` : "clear";
    const dueRound = rowsDueNow[0];

    return [
      {
        label: "Open rounds",
        value: String(openRows.length),
        detail: `${openWeeklyCount} weekly · ${openMonthlyCount} monthly · ${total} total`,
        badge: overdueCount ? `${overdueCount} due` : "live",
        tone: overdueCount ? "overdue" : "pending",
        icon: <Layers size={18} />
      },
      {
        label: "Due now / overdue",
        value: rowsDueNow.length > 0 ? String(rowsDueNow.length) : "0",
        detail: dueRound ? `${dueRound.round_id} · ${trackLabel(roundTrack(dueRound))}` : "No scoring jobs currently due",
        href: dueRound ? roundAuditPath(dueRound.round_id) : undefined,
        badge: dueBadge,
        tone: rowsDueNow.length > 0 ? "overdue" : "resolved",
        icon: <CheckCircle2 size={18} />
      },
      {
        label: "Next scheduled score",
        value: nextRound?.round_id ?? "None",
        detail: nextRound ? formatDateTimeUtc(nextRound.score_eta_utc) : "No future scoring window",
        href: nextRound ? roundAuditPath(nextRound.round_id) : undefined,
        badge: nextRound ? trackLabel(roundTrack(nextRound)) : undefined,
        tone: "pending",
        icon: <CalendarClock size={18} />
      },
      {
        label: "Latest scored round",
        value: formatScoredValue(latestScoredFallback),
        detail: formatScoredDetail(latestScoredFallback),
        href: latestScoredFallback ? roundAuditPath(latestScoredFallback.roundId) : undefined,
        badge: latestScoredFallback ? trackLabel(latestScoredFallback.track) : undefined,
        tone: "resolved",
        icon: <Award size={18} />
      },
      {
        label: "Newest open rounds",
        value: activeRounds.length > 0 ? `${activeRounds.length} rounds` : "None",
        detail:
          activeSubmissionCount > 0
            ? `${formatActiveDecisionDetail(activeRounds)} · ${activeSubmissionCount} frozen portfolios`
            : formatActiveDecisionDetail(activeRounds),
        href: activeRounds[0] ? roundAuditPath(activeRounds[0].round_id) : undefined,
        badge: activeTrackSummary ? `Open ${activeTrackSummary}` : undefined,
        tone: "blue",
        icon: <Activity size={18} />
      }
    ];
  }, [fallbackSubmissions, latestScoredFallback, rows]);

  return (
    <section className="rounds-kpi-panel" aria-label="Rounds snapshot">
      <div className="rounds-kpi-head">
        <div>
          <span className="panel-kicker">Rounds snapshot</span>
          <h2>Current Round Operations</h2>
        </div>
        <p>Open windows, due scoring jobs, latest official score, and newest open rounds.</p>
      </div>
      <div className="rounds-kpi-grid">
        {items.map((item) => (
          <KpiCard key={item.label} item={item} />
        ))}
      </div>
    </section>
  );
}
