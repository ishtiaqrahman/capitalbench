import {
  escapeHtml,
  getEmailProvider,
  isValidEmail,
  makeJsonResult,
  normalizeEmail,
  parseRequestPayload,
  sanitizeSource,
  sendEmail,
  sha256Hex
} from "./email/system.js";

const DEFAULT_NOTIFY_TO = "evals@capitalbench.org";
const SUPPORTED_EMAIL_PROVIDERS = new Set(["cloudflare", "resend"]);

const EVALUATING_OPTIONS = new Set([
  "Commercial foundation model",
  "Fine-tuned model",
  "Proprietary model",
  "AI investment agent",
  "RAG or research workflow",
  "Prompt or configuration variant",
  "Third-party vendor product",
  "Other"
]);

const DECISION_OPTIONS = new Set([
  "Select a model or vendor",
  "Validate a release",
  "Compare two configurations",
  "Diagnose inconsistent behavior",
  "Establish an internal baseline",
  "Support customer or investor diligence",
  "Evaluate a third-party claim",
  "Other"
]);

const ACCESS_OPTIONS = new Set([
  "Customer-hosted API endpoint",
  "Temporary provider API key",
  "CapitalBench provider account",
  "Customer-executed runner",
  "Not sure"
]);

const START_OPTIONS = new Set([
  "As soon as possible",
  "This week",
  "Next 2 weeks",
  "This month",
  "Next month",
  "Not sure"
]);

let privateEvalSchemaReady = false;

async function ensurePrivateEvalSchema(db) {
  if (privateEvalSchemaReady) return;

  await db
    .prepare(
      `create table if not exists private_eval_requests (
         id text primary key,
         full_name text not null,
         work_email text not null,
         email_normalized text not null,
         company text not null,
         company_website text not null,
         role text not null,
         evaluating text not null,
         business_decision text not null,
         access_method text not null,
         start_period text not null,
         project_summary text not null,
         optional_json text not null,
         page_url text not null,
         source text not null default 'private_evals',
         status text not null default 'requested' check (status in ('requested', 'contacted', 'scoped', 'declined')),
         notification_status text not null default 'pending' check (notification_status in ('pending', 'sent', 'failed')),
         notification_provider text,
         notification_message_id text,
         notification_error text,
         created_at text not null,
         updated_at text not null,
         notified_at text
       )`
    )
    .run();
  await db
    .prepare("create index if not exists idx_private_eval_requests_created on private_eval_requests(created_at)")
    .run();
  await db
    .prepare("create index if not exists idx_private_eval_requests_email on private_eval_requests(email_normalized)")
    .run();
  await db
    .prepare("create index if not exists idx_private_eval_requests_status on private_eval_requests(status, created_at)")
    .run();

  privateEvalSchemaReady = true;
}

function cleanText(value, max = 400) {
  return String(value ?? "")
    .trim()
    .replace(/\s+/g, " ")
    .slice(0, max);
}

function cleanLongText(value, max = 4000) {
  return String(value ?? "")
    .trim()
    .replace(/\r\n/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .slice(0, max);
}

function validRequiredText(value, min, max) {
  const cleaned = cleanText(value, max);
  return cleaned.length >= min && cleaned.length <= max;
}

function validCompanyWebsite(value) {
  const website = cleanText(value, 300);
  if (!website) return false;
  try {
    const parsed = new URL(website);
    return ["http:", "https:"].includes(parsed.protocol) && Boolean(parsed.hostname.includes("."));
  } catch {
    return false;
  }
}

function emailConfig(env) {
  const provider = getEmailProvider(env);
  if (!SUPPORTED_EMAIL_PROVIDERS.has(provider)) {
    return { ok: false, error: "unsupported_provider", provider };
  }

  const missing = [];
  if (provider === "cloudflare" && !env.EMAIL) missing.push("EMAIL");
  if (provider === "resend" && !env.RESEND_API_KEY) missing.push("RESEND_API_KEY");
  if (!env.EMAIL_FROM) missing.push("EMAIL_FROM");

  if (missing.length) {
    return { ok: false, error: "missing_config", missing };
  }

  return { ok: true, provider };
}

function optionalPayload(payload) {
  return {
    model_or_system_name: cleanText(payload.model_or_system_name, 180),
    current_model_provider: cleanText(payload.current_model_provider, 180),
    tools_or_browsing: cleanText(payload.tools_or_browsing, 120),
    custom_asset_universe_required: cleanText(payload.custom_asset_universe_required, 80),
    nda_required: cleanText(payload.nda_required, 80),
    sensitive_or_regulated_data: cleanText(payload.sensitive_or_regulated_data, 80),
    procurement_or_security_review: cleanText(payload.procurement_or_security_review, 80),
    referral_source: cleanText(payload.referral_source, 180)
  };
}

export function createD1PrivateEvalRepository(db) {
  if (!db) {
    throw new Error("EMAIL_DB binding is not configured");
  }

  return {
    async createRequest(request) {
      await ensurePrivateEvalSchema(db);
      await db
        .prepare(
          `insert into private_eval_requests
             (id, full_name, work_email, email_normalized, company, company_website, role, evaluating,
              business_decision, access_method, start_period, project_summary, optional_json, page_url,
              source, status, notification_status, notification_provider, notification_message_id,
              notification_error, created_at, updated_at, notified_at)
           values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'requested', 'pending', null, null, null, ?, ?, null)`
        )
        .bind(
          request.id,
          request.full_name,
          request.work_email,
          request.email_normalized,
          request.company,
          request.company_website,
          request.role,
          request.evaluating,
          request.business_decision,
          request.access_method,
          request.start_period,
          request.project_summary,
          JSON.stringify(request.optional),
          request.page_url,
          request.source,
          request.created_at,
          request.updated_at
        )
        .run();
      return request;
    },

    async updateNotification(id, patch) {
      await ensurePrivateEvalSchema(db);
      await db
        .prepare(
          `update private_eval_requests
           set notification_status = ?,
               notification_provider = ?,
               notification_message_id = ?,
               notification_error = ?,
               notified_at = ?,
               updated_at = ?
           where id = ?`
        )
        .bind(
          patch.notification_status,
          patch.notification_provider ?? null,
          patch.notification_message_id ?? null,
          patch.notification_error ?? null,
          patch.notified_at ?? null,
          patch.updated_at,
          id
        )
        .run();
    }
  };
}

export function createMemoryPrivateEvalRepository() {
  const requests = new Map();

  return {
    requests,

    async createRequest(request) {
      requests.set(request.id, request);
      return request;
    },

    async updateNotification(id, patch) {
      const existing = requests.get(id);
      requests.set(id, { ...existing, ...patch });
    }
  };
}

function tableRows(rows) {
  return rows
    .map(
      ([label, value]) =>
        `<tr><td style="padding:6px 18px 6px 0;color:#5f6f69;font-weight:700;vertical-align:top">${escapeHtml(label)}</td><td style="padding:6px 0;vertical-align:top">${escapeHtml(value || "Not provided")}</td></tr>`
    )
    .join("");
}

function privateEvalEmail({ request }) {
  const optionalRows = Object.entries(request.optional).map(([key, value]) => [
    key.replace(/_/g, " ").replace(/\b\w/g, (letter) => letter.toUpperCase()),
    value
  ]);
  const rows = [
    ["Name", request.full_name],
    ["Email", request.work_email],
    ["Company", request.company],
    ["Website", request.company_website],
    ["Role", request.role],
    ["Evaluating", request.evaluating],
    ["Business decision", request.business_decision],
    ["Access method", request.access_method],
    ["Desired start", request.start_period],
    ["Page", request.page_url],
    ["Source", request.source],
    ["Project summary", request.project_summary],
    ...optionalRows
  ];

  const html = `
<h1 style="font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:22px;line-height:1.25;margin:0 0 16px;color:#07130f">
  CapitalBench private eval request
</h1>
<table style="border-collapse:collapse;font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:15px;line-height:1.5;color:#07130f">
  ${tableRows(rows)}
</table>`;

  const text = [
    "CapitalBench private eval request",
    "",
    ...rows.map(([label, value]) => `${label}: ${value || "Not provided"}`)
  ].join("\n");

  return { html, text };
}

async function notifyPrivateEvalRequest({ env, request }) {
  const config = emailConfig(env);
  if (!config.ok) return config;

  const to = String(env.PRIVATE_EVAL_NOTIFY_TO || env.API_ACCESS_NOTIFY_TO || DEFAULT_NOTIFY_TO).trim();
  if (!isValidEmail(to)) {
    return { ok: false, error: "invalid_notify_to" };
  }

  const message = privateEvalEmail({ request });
  const response = await sendEmail({
    env,
    provider: config.provider,
    to,
    subject: `CapitalBench private eval request: ${request.company}`,
    html: message.html,
    text: message.text,
    replyTo: request.work_email,
    idempotencyKey: `capitalbench-private-eval-${await sha256Hex(`${request.id}:${request.email_normalized}`)}`
  });

  return {
    ok: true,
    provider: response.provider,
    messageId: response.messageId
  };
}

export async function handlePrivateEvalRequest({ request, env, repo, now = new Date() }) {
  let payload;
  try {
    payload = await parseRequestPayload(request);
  } catch {
    return makeJsonResult(400, { ok: false, error: "invalid_payload" });
  }

  if (cleanText(payload.fax, 80)) {
    return makeJsonResult(200, {
      ok: true,
      message: "Your request has been received."
    });
  }

  const fullName = cleanText(payload.full_name, 120);
  const workEmail = String(payload.work_email ?? "").trim();
  const company = cleanText(payload.company, 160);
  const companyWebsite = cleanText(payload.company_website, 300);
  const role = cleanText(payload.role, 120);
  const evaluating = cleanText(payload.evaluating, 120);
  const businessDecision = cleanText(payload.business_decision, 120);
  const accessMethod = cleanText(payload.access_method, 120);
  const startPeriod = cleanText(payload.start_period, 80);
  const projectSummary = cleanLongText(payload.project_summary, 4000);

  if (!validRequiredText(fullName, 2, 120)) return makeJsonResult(400, { ok: false, error: "invalid_full_name" });
  if (!isValidEmail(workEmail)) return makeJsonResult(400, { ok: false, error: "invalid_work_email" });
  if (!validRequiredText(company, 2, 160)) return makeJsonResult(400, { ok: false, error: "invalid_company" });
  if (!validCompanyWebsite(companyWebsite)) return makeJsonResult(400, { ok: false, error: "invalid_company_website" });
  if (!validRequiredText(role, 2, 120)) return makeJsonResult(400, { ok: false, error: "invalid_role" });
  if (!EVALUATING_OPTIONS.has(evaluating)) return makeJsonResult(400, { ok: false, error: "invalid_evaluating" });
  if (!DECISION_OPTIONS.has(businessDecision)) return makeJsonResult(400, { ok: false, error: "invalid_business_decision" });
  if (!ACCESS_OPTIONS.has(accessMethod)) return makeJsonResult(400, { ok: false, error: "invalid_access_method" });
  if (!START_OPTIONS.has(startPeriod)) return makeJsonResult(400, { ok: false, error: "invalid_start_period" });
  if (projectSummary.length < 20) return makeJsonResult(400, { ok: false, error: "invalid_project_summary" });
  if (String(payload.consent ?? "") !== "yes") return makeJsonResult(400, { ok: false, error: "missing_consent" });

  const nowIso = now.toISOString();
  const pageUrl = String(payload.pageUrl || request.headers.get("referer") || "https://www.capitalbench.org/private-evals").slice(
    0,
    300
  );
  const evalRequest = await repo.createRequest({
    id: crypto.randomUUID(),
    full_name: fullName,
    work_email: workEmail,
    email_normalized: normalizeEmail(workEmail),
    company,
    company_website: companyWebsite,
    role,
    evaluating,
    business_decision: businessDecision,
    access_method: accessMethod,
    start_period: startPeriod,
    project_summary: projectSummary,
    optional: optionalPayload(payload),
    page_url: pageUrl,
    source: sanitizeSource(payload.source || "private_evals"),
    status: "requested",
    notification_status: "pending",
    created_at: nowIso,
    updated_at: nowIso
  });

  try {
    const notification = await notifyPrivateEvalRequest({ env, request: evalRequest });
    if (!notification.ok) {
      await repo.updateNotification(evalRequest.id, {
        notification_status: "failed",
        notification_error: notification.error || "notification_failed",
        updated_at: nowIso
      });
      return makeJsonResult(500, { ok: false, error: notification.error || "notification_failed" });
    }

    await repo.updateNotification(evalRequest.id, {
      notification_status: "sent",
      notification_provider: notification.provider,
      notification_message_id: notification.messageId,
      notified_at: nowIso,
      updated_at: nowIso
    });
  } catch (error) {
    const message = error instanceof Error ? error.message : "notification_failed";
    await repo.updateNotification(evalRequest.id, {
      notification_status: "failed",
      notification_error: message,
      updated_at: nowIso
    });
    return makeJsonResult(500, { ok: false, error: "notification_failed" });
  }

  return makeJsonResult(200, {
    ok: true,
    message:
      "Your request has been received. The next step is a fit review followed by a proposed Evaluation Plan and fixed SOW. No payment or system access is requested until scope is agreed."
  });
}
