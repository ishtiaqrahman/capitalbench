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

const DEFAULT_NOTIFY_TO = "ishtiaq@capitalbench.org";
const SUPPORTED_EMAIL_PROVIDERS = new Set(["cloudflare", "resend"]);
let apiAccessSchemaReady = false;

async function ensureApiAccessSchema(db) {
  if (apiAccessSchemaReady) return;

  await db
    .prepare(
      `create table if not exists api_access_requests (
         id text primary key,
         name text not null,
         email text not null,
         email_normalized text not null unique,
         source text not null default 'api_page',
         status text not null default 'requested' check (status in ('requested', 'contacted', 'approved', 'declined')),
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
    .prepare("create index if not exists idx_api_access_requests_status_created on api_access_requests(status, created_at)")
    .run();
  await db
    .prepare("create index if not exists idx_api_access_requests_notification_status on api_access_requests(notification_status)")
    .run();

  apiAccessSchemaReady = true;
}

function cleanName(value) {
  return String(value ?? "")
    .trim()
    .replace(/\s+/g, " ");
}

function validName(value) {
  const name = cleanName(value);
  return name.length >= 2 && name.length <= 120;
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

export function createD1ApiAccessRepository(db) {
  if (!db) {
    throw new Error("EMAIL_DB binding is not configured");
  }

  return {
    async upsertRequest(request) {
      await ensureApiAccessSchema(db);

      const existing = await db
        .prepare("select * from api_access_requests where email_normalized = ?")
        .bind(request.email_normalized)
        .first();

      if (existing) {
        await db
          .prepare(
            `update api_access_requests
             set name = ?,
                 email = ?,
                 source = ?,
                 status = 'requested',
                 notification_status = 'pending',
                 notification_error = null,
                 updated_at = ?
             where id = ?`
          )
          .bind(request.name, request.email, request.source, request.updated_at, existing.id)
          .run();
        return {
          ...existing,
          name: request.name,
          email: request.email,
          source: request.source,
          status: "requested",
          notification_status: "pending",
          notification_error: null,
          updated_at: request.updated_at
        };
      }

      await db
        .prepare(
          `insert into api_access_requests
             (id, name, email, email_normalized, source, status, notification_status, notification_provider,
              notification_message_id, notification_error, created_at, updated_at, notified_at)
           values (?, ?, ?, ?, ?, 'requested', 'pending', null, null, null, ?, ?, null)`
        )
        .bind(
          request.id,
          request.name,
          request.email,
          request.email_normalized,
          request.source,
          request.created_at,
          request.updated_at
        )
        .run();
      return request;
    },

    async updateNotification(id, patch) {
      await ensureApiAccessSchema(db);

      await db
        .prepare(
          `update api_access_requests
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

export function createMemoryApiAccessRepository() {
  const requests = new Map();
  const byEmail = new Map();

  return {
    requests,

    async upsertRequest(request) {
      const existingId = byEmail.get(request.email_normalized);
      if (existingId) {
        const existing = requests.get(existingId);
        const updated = {
          ...existing,
          name: request.name,
          email: request.email,
          source: request.source,
          status: "requested",
          notification_status: "pending",
          notification_error: null,
          updated_at: request.updated_at
        };
        requests.set(existingId, updated);
        return updated;
      }

      requests.set(request.id, request);
      byEmail.set(request.email_normalized, request.id);
      return request;
    },

    async updateNotification(id, patch) {
      const existing = requests.get(id);
      requests.set(id, { ...existing, ...patch });
    }
  };
}

function apiAccessEmail({ request, pageUrl }) {
  const safeName = escapeHtml(request.name);
  const safeEmail = escapeHtml(request.email);
  const safeSource = escapeHtml(request.source);
  const safePageUrl = escapeHtml(pageUrl);

  const html = `
<h1 style="font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:22px;line-height:1.25;margin:0 0 16px;color:#07130f">
  CapitalBench API access request
</h1>
<table style="border-collapse:collapse;font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:15px;line-height:1.5;color:#07130f">
  <tr><td style="padding:6px 16px 6px 0;color:#5f6f69;font-weight:700">Name</td><td style="padding:6px 0">${safeName}</td></tr>
  <tr><td style="padding:6px 16px 6px 0;color:#5f6f69;font-weight:700">Email</td><td style="padding:6px 0"><a href="mailto:${safeEmail}">${safeEmail}</a></td></tr>
  <tr><td style="padding:6px 16px 6px 0;color:#5f6f69;font-weight:700">Source</td><td style="padding:6px 0">${safeSource}</td></tr>
  <tr><td style="padding:6px 16px 6px 0;color:#5f6f69;font-weight:700">Page</td><td style="padding:6px 0">${safePageUrl}</td></tr>
</table>`;

  const text = [
    "CapitalBench API access request",
    "",
    `Name: ${request.name}`,
    `Email: ${request.email}`,
    `Source: ${request.source}`,
    `Page: ${pageUrl}`
  ].join("\n");

  return { html, text };
}

async function notifyApiAccessRequest({ env, request, pageUrl }) {
  const config = emailConfig(env);
  if (!config.ok) return config;

  const to = String(env.API_ACCESS_NOTIFY_TO || DEFAULT_NOTIFY_TO).trim();
  if (!isValidEmail(to)) {
    return { ok: false, error: "invalid_notify_to" };
  }

  const message = apiAccessEmail({ request, pageUrl });
  const response = await sendEmail({
    env,
    provider: config.provider,
    to,
    subject: `CapitalBench API access request: ${request.name}`,
    html: message.html,
    text: message.text,
    replyTo: request.email,
    idempotencyKey: `capitalbench-api-access-${await sha256Hex(`${request.id}:${request.email_normalized}`)}`
  });

  return {
    ok: true,
    provider: response.provider,
    messageId: response.messageId
  };
}

export async function handleApiAccessRequest({ request, env, repo, now = new Date() }) {
  let payload;
  try {
    payload = await parseRequestPayload(request);
  } catch {
    return makeJsonResult(400, { ok: false, error: "invalid_payload" });
  }

  if (String(payload.company ?? "").trim()) {
    return makeJsonResult(200, { ok: true, message: "Request received." });
  }

  const name = cleanName(payload.name);
  const email = String(payload.email ?? "").trim();

  if (!validName(name)) {
    return makeJsonResult(400, { ok: false, error: "invalid_name" });
  }
  if (!isValidEmail(email)) {
    return makeJsonResult(400, { ok: false, error: "invalid_email" });
  }

  const nowIso = now.toISOString();
  const accessRequest = await repo.upsertRequest({
    id: crypto.randomUUID(),
    name,
    email,
    email_normalized: normalizeEmail(email),
    source: sanitizeSource(payload.source || "api_page"),
    status: "requested",
    notification_status: "pending",
    created_at: nowIso,
    updated_at: nowIso
  });

  const pageUrl = String(payload.pageUrl || request.headers.get("referer") || "https://www.capitalbench.org/api").slice(0, 300);

  try {
    const notification = await notifyApiAccessRequest({ env, request: accessRequest, pageUrl });
    if (!notification.ok) {
      await repo.updateNotification(accessRequest.id, {
        notification_status: "failed",
        notification_error: notification.error || "notification_failed",
        updated_at: nowIso
      });
      return makeJsonResult(500, { ok: false, error: notification.error || "notification_failed" });
    }

    await repo.updateNotification(accessRequest.id, {
      notification_status: "sent",
      notification_provider: notification.provider,
      notification_message_id: notification.messageId,
      notified_at: nowIso,
      updated_at: nowIso
    });
  } catch (error) {
    const message = error instanceof Error ? error.message : "notification_failed";
    await repo.updateNotification(accessRequest.id, {
      notification_status: "failed",
      notification_error: message,
      updated_at: nowIso
    });
    return makeJsonResult(500, { ok: false, error: "notification_failed" });
  }

  return makeJsonResult(200, {
    ok: true,
    message: "Request received."
  });
}
