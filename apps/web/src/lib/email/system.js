export const WEBSITE_COLLECTION_GROUP = {
  id: "website_collection",
  slug: "website_collection",
  name: "Website Collection",
  description: "Emails collected from public website signup forms."
};

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const CONSENT_VERSION = "2026-05-31.website-collection.v1";
const DEFAULT_CONSENT_TEXT =
  "By subscribing, you agree to receive occasional CapitalBench benchmark updates and product announcements. You can unsubscribe anytime.";
const SUPPORTED_EMAIL_PROVIDERS = new Set(["cloudflare", "resend"]);
const DEFAULT_RESEND_DAILY_SEND_LIMIT = 100;

export function normalizeEmail(email) {
  return String(email ?? "").trim().toLowerCase();
}

export function isValidEmail(email) {
  const normalized = normalizeEmail(email);
  return normalized.length <= 320 && EMAIL_RE.test(normalized);
}

export function sanitizeSource(source) {
  const value = String(source ?? "website").trim().toLowerCase();
  if (/^[a-z0-9_-]{1,40}$/.test(value)) return value;
  return "website";
}

export function getEmailProvider(env) {
  const configured = String(env.EMAIL_PROVIDER ?? "").trim().toLowerCase();
  if (configured) return configured;
  return env.RESEND_API_KEY ? "resend" : "cloudflare";
}

export function makeJsonResult(status, body) {
  return {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store"
    },
    body
  };
}

export function resultToResponse(result) {
  return new Response(JSON.stringify(result.body), {
    status: result.status,
    headers: result.headers
  });
}

export function htmlResponse(html, status = 200) {
  return new Response(html, {
    status,
    headers: {
      "content-type": "text/html; charset=utf-8",
      "cache-control": "no-store"
    }
  });
}

export async function parseRequestPayload(request) {
  const contentType = request.headers.get("content-type") ?? "";
  if (contentType.includes("application/json")) {
    return await request.json();
  }
  const form = await request.formData();
  return Object.fromEntries(form.entries());
}

export async function sha256Hex(value) {
  const data = new TextEncoder().encode(String(value));
  const hash = await crypto.subtle.digest("SHA-256", data);
  return Array.from(new Uint8Array(hash))
    .map((byte) => byte.toString(16).padStart(2, "0"))
    .join("");
}

function bytesToBase64url(bytes) {
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  const base64 =
    typeof btoa === "function"
      ? btoa(binary)
      : Buffer.from(binary, "binary").toString("base64");
  return base64.replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}

function base64urlToBytes(value) {
  const normalized = String(value).replace(/-/g, "+").replace(/_/g, "/");
  const padded = normalized + "=".repeat((4 - (normalized.length % 4)) % 4);
  const binary =
    typeof atob === "function"
      ? atob(padded)
      : Buffer.from(padded, "base64").toString("binary");
  return Uint8Array.from(binary, (char) => char.charCodeAt(0));
}

function encodeBase64urlText(value) {
  return bytesToBase64url(new TextEncoder().encode(String(value)));
}

function decodeBase64urlText(value) {
  return new TextDecoder().decode(base64urlToBytes(value));
}

async function hmacBase64url(secret, value) {
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const signature = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(value));
  return bytesToBase64url(new Uint8Array(signature));
}

export async function createUnsubscribeToken(subscriber, secret) {
  if (!secret) throw new Error("UNSUBSCRIBE_TOKEN_SECRET is required");
  const payload = `${subscriber.id}:${subscriber.email_normalized}`;
  const encodedPayload = encodeBase64urlText(payload);
  const signature = await hmacBase64url(secret, payload);
  return `${encodedPayload}.${signature}`;
}

export async function verifyUnsubscribeToken(token, secret) {
  if (!secret) return null;
  const [encodedPayload, signature] = String(token ?? "").split(".");
  if (!encodedPayload || !signature) return null;
  let payload;
  try {
    payload = decodeBase64urlText(encodedPayload);
  } catch {
    return null;
  }
  const expected = await hmacBase64url(secret, payload);
  if (expected !== signature) return null;
  const [id, emailNormalized] = payload.split(":");
  if (!id || !emailNormalized) return null;
  return { id, email_normalized: emailNormalized };
}

export function createD1EmailRepository(db) {
  if (!db) {
    throw new Error("EMAIL_DB binding is not configured");
  }

  return {
    async ensureWebsiteCollection(nowIso) {
      await db
        .prepare(
          `insert into audience_groups (id, slug, name, description, created_at)
           values (?, ?, ?, ?, ?)
           on conflict(slug) do update set
             name = excluded.name,
             description = excluded.description`
        )
        .bind(
          WEBSITE_COLLECTION_GROUP.id,
          WEBSITE_COLLECTION_GROUP.slug,
          WEBSITE_COLLECTION_GROUP.name,
          WEBSITE_COLLECTION_GROUP.description,
          nowIso
        )
        .run();
      return WEBSITE_COLLECTION_GROUP;
    },

    async upsertSubscriber(email, nowIso) {
      const emailNormalized = normalizeEmail(email);
      const existing = await db
        .prepare("select * from subscribers where email_normalized = ?")
        .bind(emailNormalized)
        .first();
      if (existing) {
        await db
          .prepare(
            `update subscribers
             set email = ?, status = 'active', updated_at = ?
             where id = ?`
          )
          .bind(email, nowIso, existing.id)
          .run();
        return { ...existing, email, status: "active", updated_at: nowIso };
      }

      const subscriber = {
        id: crypto.randomUUID(),
        email,
        email_normalized: emailNormalized,
        status: "active",
        created_at: nowIso,
        updated_at: nowIso
      };
      await db
        .prepare(
          `insert into subscribers
             (id, email, email_normalized, status, created_at, updated_at)
           values (?, ?, ?, ?, ?, ?)`
        )
        .bind(
          subscriber.id,
          subscriber.email,
          subscriber.email_normalized,
          subscriber.status,
          subscriber.created_at,
          subscriber.updated_at
        )
        .run();
      return subscriber;
    },

    async addMembership({ subscriberId, groupId, source, consentText, consentVersion, nowIso }) {
      await db
        .prepare(
          `insert into audience_memberships
             (subscriber_id, group_id, status, source, consent_text, consent_version, created_at, updated_at)
           values (?, ?, 'active', ?, ?, ?, ?, ?)
           on conflict(subscriber_id, group_id) do update set
             status = 'active',
             source = excluded.source,
             consent_text = excluded.consent_text,
             consent_version = excluded.consent_version,
             updated_at = excluded.updated_at`
        )
        .bind(subscriberId, groupId, source, consentText, consentVersion, nowIso, nowIso)
        .run();
    },

    async getSubscriberById(id) {
      return await db.prepare("select * from subscribers where id = ?").bind(id).first();
    },

    async unsubscribeSubscriber(id, nowIso) {
      await db
        .prepare("update subscribers set status = 'unsubscribed', updated_at = ? where id = ?")
        .bind(nowIso, id)
        .run();
      await db
        .prepare("update audience_memberships set status = 'unsubscribed', updated_at = ? where subscriber_id = ?")
        .bind(nowIso, id)
        .run();
    },

    async listActiveMembers(groupSlug) {
      const result = await db
        .prepare(
          `select s.*
           from subscribers s
           join audience_memberships m on m.subscriber_id = s.id
           join audience_groups g on g.id = m.group_id
           where g.slug = ?
             and s.status = 'active'
             and m.status = 'active'
           order by s.created_at asc`
        )
        .bind(groupSlug)
        .all();
      return result.results ?? [];
    },

    async createCampaign(campaign) {
      await db
        .prepare(
          `insert into email_campaigns
             (id, group_id, provider, subject, content_hash, status, recipient_count, sent_count, failed_count, created_at, sent_at)
           values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
        )
        .bind(
          campaign.id,
          campaign.group_id,
          campaign.provider,
          campaign.subject,
          campaign.content_hash,
          campaign.status,
          campaign.recipient_count,
          campaign.sent_count,
          campaign.failed_count,
          campaign.created_at,
          campaign.sent_at ?? null
        )
        .run();
      return campaign;
    },

    async updateCampaign(id, patch) {
      await db
        .prepare(
          `update email_campaigns
           set status = ?, recipient_count = ?, sent_count = ?, failed_count = ?, sent_at = ?
           where id = ?`
        )
        .bind(
          patch.status,
          patch.recipient_count,
          patch.sent_count,
          patch.failed_count,
          patch.sent_at ?? null,
          id
        )
        .run();
    }
  };
}

export function createMemoryEmailRepository() {
  const groups = new Map();
  const subscribers = new Map();
  const subscribersByEmail = new Map();
  const memberships = new Map();
  const campaigns = new Map();

  return {
    groups,
    subscribers,
    memberships,
    campaigns,

    async ensureWebsiteCollection(nowIso) {
      const group = { ...WEBSITE_COLLECTION_GROUP, created_at: nowIso };
      groups.set(group.id, group);
      return group;
    },

    async upsertSubscriber(email, nowIso) {
      const emailNormalized = normalizeEmail(email);
      const existingId = subscribersByEmail.get(emailNormalized);
      if (existingId) {
        const existing = subscribers.get(existingId);
        const updated = { ...existing, email, status: "active", updated_at: nowIso };
        subscribers.set(existingId, updated);
        return updated;
      }
      const subscriber = {
        id: crypto.randomUUID(),
        email,
        email_normalized: emailNormalized,
        status: "active",
        created_at: nowIso,
        updated_at: nowIso
      };
      subscribers.set(subscriber.id, subscriber);
      subscribersByEmail.set(emailNormalized, subscriber.id);
      return subscriber;
    },

    async addMembership({ subscriberId, groupId, source, consentText, consentVersion, nowIso }) {
      memberships.set(`${subscriberId}:${groupId}`, {
        subscriber_id: subscriberId,
        group_id: groupId,
        status: "active",
        source,
        consent_text: consentText,
        consent_version: consentVersion,
        created_at: nowIso,
        updated_at: nowIso
      });
    },

    async getSubscriberById(id) {
      return subscribers.get(id) ?? null;
    },

    async unsubscribeSubscriber(id, nowIso) {
      const subscriber = subscribers.get(id);
      if (subscriber) {
        subscribers.set(id, { ...subscriber, status: "unsubscribed", updated_at: nowIso });
      }
      for (const [key, membership] of memberships) {
        if (membership.subscriber_id === id) {
          memberships.set(key, { ...membership, status: "unsubscribed", updated_at: nowIso });
        }
      }
    },

    async listActiveMembers(groupSlug) {
      const group = Array.from(groups.values()).find((item) => item.slug === groupSlug);
      if (!group) return [];
      return Array.from(memberships.values())
        .filter((membership) => membership.group_id === group.id && membership.status === "active")
        .map((membership) => subscribers.get(membership.subscriber_id))
        .filter((subscriber) => subscriber?.status === "active")
        .sort((a, b) => a.created_at.localeCompare(b.created_at));
    },

    async createCampaign(campaign) {
      campaigns.set(campaign.id, campaign);
      return campaign;
    },

    async updateCampaign(id, patch) {
      const existing = campaigns.get(id);
      campaigns.set(id, { ...existing, ...patch });
    }
  };
}

async function verifyTurnstile({ token, request, env }) {
  const secret = env.TURNSTILE_SECRET_KEY;
  if (!secret) return { ok: true, skipped: true };
  if (!token) return { ok: false, reason: "missing_turnstile" };
  const form = new FormData();
  form.append("secret", secret);
  form.append("response", token);
  const ip = request.headers.get("CF-Connecting-IP");
  if (ip) form.append("remoteip", ip);
  const response = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
    method: "POST",
    body: form
  });
  const result = await response.json();
  return result.success ? { ok: true } : { ok: false, reason: "turnstile_failed" };
}

export async function handleSubscribeRequest({ request, env, repo, now = new Date() }) {
  let payload;
  try {
    payload = await parseRequestPayload(request);
  } catch {
    return makeJsonResult(400, { ok: false, error: "invalid_payload" });
  }

  if (String(payload.company ?? "").trim()) {
    return makeJsonResult(200, { ok: true, message: "You are on the list." });
  }

  const email = String(payload.email ?? "").trim();
  if (!isValidEmail(email)) {
    return makeJsonResult(400, { ok: false, error: "invalid_email" });
  }

  const turnstile = await verifyTurnstile({
    token: payload.turnstileToken ?? payload["cf-turnstile-response"],
    request,
    env
  });
  if (!turnstile.ok) {
    return makeJsonResult(400, { ok: false, error: turnstile.reason });
  }

  const nowIso = now.toISOString();
  const source = sanitizeSource(payload.source);
  const group = await repo.ensureWebsiteCollection(nowIso);
  const subscriber = await repo.upsertSubscriber(email, nowIso);
  await repo.addMembership({
    subscriberId: subscriber.id,
    groupId: group.id,
    source,
    consentText: DEFAULT_CONSENT_TEXT,
    consentVersion: CONSENT_VERSION,
    nowIso
  });

  return makeJsonResult(200, {
    ok: true,
    message: "You are on the list.",
    group: group.name
  });
}

export async function handleUnsubscribeRequest({ request, env, repo, now = new Date() }) {
  const url = new URL(request.url);
  const token = url.searchParams.get("token");
  const verified = await verifyUnsubscribeToken(token, env.UNSUBSCRIBE_TOKEN_SECRET);
  if (!verified) {
    return htmlResponse(renderUnsubscribePage("Invalid unsubscribe link", "This unsubscribe link is invalid or expired."), 400);
  }

  const subscriber = await repo.getSubscriberById(verified.id);
  if (!subscriber || subscriber.email_normalized !== verified.email_normalized) {
    return htmlResponse(renderUnsubscribePage("Email not found", "This email is not active in the mailing list."), 404);
  }

  await repo.unsubscribeSubscriber(subscriber.id, now.toISOString());
  return htmlResponse(
    renderUnsubscribePage("You are unsubscribed", "You will no longer receive CapitalBench update emails.")
  );
}

function renderUnsubscribePage(title, message) {
  return `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>${escapeHtml(title)} - CapitalBench</title>
    <style>
      body { margin: 0; font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #f5f7f6; color: #07130f; }
      main { min-height: 100vh; display: grid; place-items: center; padding: 24px; }
      section { max-width: 520px; border: 1px solid #d7e0dc; border-radius: 10px; padding: 28px; background: white; box-shadow: 0 16px 40px rgb(14 32 27 / 10%); }
      h1 { margin: 0 0 10px; font-size: 1.7rem; }
      p { margin: 0 0 18px; color: #51615b; line-height: 1.55; }
      a { color: #006b5f; font-weight: 700; }
    </style>
  </head>
  <body>
    <main>
      <section>
        <h1>${escapeHtml(title)}</h1>
        <p>${escapeHtml(message)}</p>
        <a href="/">Return to CapitalBench</a>
      </section>
    </main>
  </body>
</html>`;
}

export function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function appendEmailFooter({ html, text, unsubscribeUrl, mailingAddress }) {
  const safeUrl = escapeHtml(unsubscribeUrl);
  const safeAddress = escapeHtml(mailingAddress || "CapitalBench");
  const htmlFooter = `
<hr style="border:0;border-top:1px solid #d7e0dc;margin:28px 0 16px">
<p style="color:#5f6f69;font-size:13px;line-height:1.5">
  You are receiving this because you subscribed to CapitalBench updates.
  <a href="${safeUrl}">Unsubscribe</a>.
  <br>${safeAddress}
</p>`;
  const textFooter = `\n\n---\nYou are receiving this because you subscribed to CapitalBench updates.\nUnsubscribe: ${unsubscribeUrl}\n${mailingAddress || "CapitalBench"}`;
  return {
    html: `${html}${htmlFooter}`,
    text: `${text}${textFooter}`
  };
}

function requireEmailConfig(env) {
  const missing = [];
  const provider = getEmailProvider(env);
  if (!SUPPORTED_EMAIL_PROVIDERS.has(provider)) {
    return { ok: false, error: "unsupported_provider", provider };
  }
  if (provider === "cloudflare" && !env.EMAIL) missing.push("EMAIL");
  if (provider === "resend" && !env.RESEND_API_KEY) missing.push("RESEND_API_KEY");
  if (!env.EMAIL_FROM) missing.push("EMAIL_FROM");
  if (!env.EMAIL_PUBLIC_BASE_URL) missing.push("EMAIL_PUBLIC_BASE_URL");
  if (!env.UNSUBSCRIBE_TOKEN_SECRET) missing.push("UNSUBSCRIBE_TOKEN_SECRET");
  if (!env.EMAIL_ADMIN_TOKEN) missing.push("EMAIL_ADMIN_TOKEN");
  if (!env.EMAIL_MAILING_ADDRESS) missing.push("EMAIL_MAILING_ADDRESS");
  if (missing.length) {
    return { ok: false, missing };
  }
  return { ok: true, provider };
}

function authorized(request, env) {
  const expected = env.EMAIL_ADMIN_TOKEN;
  const header = request.headers.get("authorization") ?? "";
  if (!expected || !header.startsWith("Bearer ")) return false;
  return header.slice("Bearer ".length) === expected;
}

function getDailySendLimit(env, provider) {
  if (provider !== "resend") return null;
  const configured = String(env.RESEND_DAILY_SEND_LIMIT ?? DEFAULT_RESEND_DAILY_SEND_LIMIT).trim().toLowerCase();
  if (configured === "0" || configured === "none" || configured === "unlimited") return null;
  const parsed = Number(configured);
  if (!Number.isFinite(parsed) || parsed <= 0) return DEFAULT_RESEND_DAILY_SEND_LIMIT;
  return Math.floor(parsed);
}

async function sendEmail({ env, provider, to, subject, html, text, headers = {}, idempotencyKey }) {
  const replyTo = env.EMAIL_REPLY_TO || env.EMAIL_FROM;

  if (provider === "cloudflare") {
    const response = await env.EMAIL.send({
      to,
      from: env.EMAIL_FROM,
      subject,
      html,
      text,
      headers: {
        "Reply-To": replyTo,
        ...headers
      }
    });
    return { provider, messageId: response?.messageId ?? null };
  }

  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      authorization: `Bearer ${env.RESEND_API_KEY}`,
      "content-type": "application/json",
      ...(idempotencyKey ? { "Idempotency-Key": idempotencyKey } : {})
    },
    body: JSON.stringify({
      from: env.EMAIL_FROM,
      to,
      subject,
      html,
      text,
      reply_to: replyTo,
      headers
    })
  });
  const result = await response.json().catch(() => ({}));
  if (!response.ok) {
    const message = result?.message || result?.error?.message || `Resend send failed with HTTP ${response.status}`;
    throw new Error(message);
  }
  return { provider, messageId: result.id ?? result.data?.id ?? null };
}

export async function handleAdminSendRequest({ request, env, repo, now = new Date() }) {
  if (!authorized(request, env)) {
    return makeJsonResult(401, { ok: false, error: "unauthorized" });
  }

  const config = requireEmailConfig(env);
  if (config.error === "unsupported_provider") {
    return makeJsonResult(500, {
      ok: false,
      error: "unsupported_provider",
      provider: config.provider,
      supportedProviders: Array.from(SUPPORTED_EMAIL_PROVIDERS)
    });
  }
  if (!config.ok) {
    return makeJsonResult(500, { ok: false, error: "missing_config", missing: config.missing });
  }
  const provider = config.provider;

  let payload;
  try {
    payload = await request.json();
  } catch {
    return makeJsonResult(400, { ok: false, error: "invalid_payload" });
  }

  const groupSlug = sanitizeSource(payload.groupSlug ?? WEBSITE_COLLECTION_GROUP.slug);
  const subject = String(payload.subject ?? "").trim();
  const html = String(payload.html ?? "").trim();
  const text = String(payload.text ?? "").trim();
  const testRecipient = payload.testRecipient ? String(payload.testRecipient).trim() : "";

  if (groupSlug !== WEBSITE_COLLECTION_GROUP.slug) {
    return makeJsonResult(400, {
      ok: false,
      error: "unsupported_group",
      supportedGroups: [WEBSITE_COLLECTION_GROUP.slug]
    });
  }
  if (!subject || subject.length > 160) {
    return makeJsonResult(400, { ok: false, error: "invalid_subject" });
  }
  if (!html || !text) {
    return makeJsonResult(400, { ok: false, error: "missing_content" });
  }
  if (testRecipient && !isValidEmail(testRecipient)) {
    return makeJsonResult(400, { ok: false, error: "invalid_test_recipient" });
  }

  if (testRecipient) {
    const unsubscribeUrl = `${env.EMAIL_PUBLIC_BASE_URL.replace(/\/$/, "")}/unsubscribe?token=test`;
    const message = appendEmailFooter({
      html,
      text,
      unsubscribeUrl,
      mailingAddress: env.EMAIL_MAILING_ADDRESS
    });
    const response = await sendEmail({
      env,
      provider,
      to: testRecipient,
      subject: `[TEST] ${subject}`,
      html: message.html,
      text: message.text,
      idempotencyKey: `capitalbench-test-${await sha256Hex(`${subject}:${testRecipient}:${now.toISOString()}`)}`
    });
    return makeJsonResult(200, {
      ok: true,
      mode: "test",
      provider: response.provider,
      messageId: response.messageId
    });
  }

  await repo.ensureWebsiteCollection(now.toISOString());
  const recipients = await repo.listActiveMembers(groupSlug);
  const dailySendLimit = getDailySendLimit(env, provider);
  if (dailySendLimit !== null && recipients.length > dailySendLimit) {
    return makeJsonResult(409, {
      ok: false,
      error: "daily_send_limit_exceeded",
      provider,
      recipientCount: recipients.length,
      dailySendLimit
    });
  }
  const contentHash = await sha256Hex(`${subject}\n${html}\n${text}`);
  const campaign = await repo.createCampaign({
    id: crypto.randomUUID(),
    group_id: WEBSITE_COLLECTION_GROUP.id,
    provider,
    subject,
    content_hash: contentHash,
    status: "sending",
    recipient_count: recipients.length,
    sent_count: 0,
    failed_count: 0,
    created_at: now.toISOString(),
    sent_at: null
  });

  let sent = 0;
  let failed = 0;
  const errors = [];

  for (const recipient of recipients) {
    try {
      const token = await createUnsubscribeToken(recipient, env.UNSUBSCRIBE_TOKEN_SECRET);
      const unsubscribeUrl = `${env.EMAIL_PUBLIC_BASE_URL.replace(/\/$/, "")}/unsubscribe?token=${encodeURIComponent(token)}`;
      const message = appendEmailFooter({
        html,
        text,
        unsubscribeUrl,
        mailingAddress: env.EMAIL_MAILING_ADDRESS
      });
      await sendEmail({
        env,
        provider,
        to: recipient.email,
        subject,
        html: message.html,
        text: message.text,
        headers: {
          "List-Unsubscribe": `<${unsubscribeUrl}>`
        },
        idempotencyKey: `${campaign.id}-${recipient.id}`
      });
      sent += 1;
    } catch (error) {
      failed += 1;
      errors.push({ email: recipient.email, error: error instanceof Error ? error.message : String(error) });
    }
  }

  const finalStatus = failed > 0 ? "failed" : "sent";
  await repo.updateCampaign(campaign.id, {
    status: finalStatus,
    recipient_count: recipients.length,
    sent_count: sent,
    failed_count: failed,
    sent_at: new Date().toISOString()
  });

  return makeJsonResult(200, {
    ok: failed === 0,
    campaignId: campaign.id,
    group: groupSlug,
    provider,
    recipientCount: recipients.length,
    sentCount: sent,
    failedCount: failed,
    errors
  });
}
