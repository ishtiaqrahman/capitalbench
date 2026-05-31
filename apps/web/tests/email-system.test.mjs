import assert from "node:assert/strict";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import test from "node:test";
import {
  WEBSITE_COLLECTION_GROUP,
  createMemoryEmailRepository,
  createUnsubscribeToken,
  handleAdminSendRequest,
  handleSubscribeRequest,
  handleUnsubscribeRequest
} from "../src/lib/email/system.js";

const execFileAsync = promisify(execFile);

function jsonRequest(url, body, headers = {}) {
  return new Request(url, {
    method: "POST",
    headers: { "content-type": "application/json", ...headers },
    body: JSON.stringify(body)
  });
}

function makeEnv(overrides = {}) {
  const sent = [];
  return {
    sent,
    EMAIL: {
      async send(message) {
        sent.push(message);
        return { messageId: `message-${sent.length}` };
      }
    },
    EMAIL_FROM: "updates@capitalbench.org",
    EMAIL_REPLY_TO: "hello@capitalbench.org",
    EMAIL_PUBLIC_BASE_URL: "https://www.capitalbench.org",
    EMAIL_ADMIN_TOKEN: "admin-token",
    UNSUBSCRIBE_TOKEN_SECRET: "test-secret",
    EMAIL_MAILING_ADDRESS: "CapitalBench, 123 Test St, Test City",
    ...overrides
  };
}

async function withMockFetch(fn) {
  const originalFetch = globalThis.fetch;
  const calls = [];
  globalThis.fetch = async (url, init = {}) => {
    calls.push({
      url,
      init,
      body: init.body ? JSON.parse(init.body) : null
    });
    return new Response(JSON.stringify({ id: `resend-message-${calls.length}` }), {
      status: 200,
      headers: { "content-type": "application/json" }
    });
  };

  try {
    return await fn(calls);
  } finally {
    globalThis.fetch = originalFetch;
  }
}

async function subscribe(repo, env, email = "reader@example.com", source = "homepage") {
  return await handleSubscribeRequest({
    request: jsonRequest("https://www.capitalbench.org/api/subscribe", { email, source }),
    env,
    repo,
    now: new Date("2026-05-31T12:00:00Z")
  });
}

test("subscribes an email into Website Collection", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv();

  const result = await subscribe(repo, env, "Reader@Example.com", "homepage");

  assert.equal(result.status, 200);
  assert.equal(result.body.ok, true);
  assert.equal(result.body.group, "Website Collection");
  assert.equal(repo.groups.get(WEBSITE_COLLECTION_GROUP.id).name, "Website Collection");
  assert.equal(repo.subscribers.size, 1);
  const subscriber = Array.from(repo.subscribers.values())[0];
  assert.equal(subscriber.email_normalized, "reader@example.com");
  const membership = Array.from(repo.memberships.values())[0];
  assert.equal(membership.group_id, "website_collection");
  assert.equal(membership.source, "homepage");
  assert.equal(membership.status, "active");
});

test("duplicate signup updates the existing subscriber without duplicating rows", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv();

  await subscribe(repo, env, "reader@example.com", "homepage");
  await subscribe(repo, env, "READER@example.com", "footer");

  assert.equal(repo.subscribers.size, 1);
  assert.equal(repo.memberships.size, 1);
  const membership = Array.from(repo.memberships.values())[0];
  assert.equal(membership.source, "footer");
});

test("honeypot submission returns success without storing an email", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv();
  const result = await handleSubscribeRequest({
    request: jsonRequest("https://www.capitalbench.org/api/subscribe", {
      email: "bot@example.com",
      source: "homepage",
      company: "Bot Corp"
    }),
    env,
    repo
  });

  assert.equal(result.status, 200);
  assert.equal(result.body.ok, true);
  assert.equal(repo.subscribers.size, 0);
});

test("invalid email is rejected", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv();
  const result = await subscribe(repo, env, "not-an-email");

  assert.equal(result.status, 400);
  assert.equal(result.body.error, "invalid_email");
  assert.equal(repo.subscribers.size, 0);
});

test("unsubscribe token marks subscriber and membership unsubscribed", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv();
  await subscribe(repo, env);
  const subscriber = Array.from(repo.subscribers.values())[0];
  const token = await createUnsubscribeToken(subscriber, env.UNSUBSCRIBE_TOKEN_SECRET);

  const response = await handleUnsubscribeRequest({
    request: new Request(`https://www.capitalbench.org/unsubscribe?token=${encodeURIComponent(token)}`),
    env,
    repo,
    now: new Date("2026-06-01T12:00:00Z")
  });

  assert.equal(response.status, 200);
  assert.equal(repo.subscribers.get(subscriber.id).status, "unsubscribed");
  assert.equal(Array.from(repo.memberships.values())[0].status, "unsubscribed");
});

test("admin send requires bearer token", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv();
  const result = await handleAdminSendRequest({
    request: jsonRequest("https://www.capitalbench.org/api/email/send", {
      groupSlug: "website_collection",
      subject: "Update",
      html: "<p>Hello</p>",
      text: "Hello"
    }),
    env,
    repo
  });

  assert.equal(result.status, 401);
  assert.equal(result.body.error, "unauthorized");
});

test("admin test send sends only to requested test recipient", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv();
  await subscribe(repo, env, "reader@example.com");
  const result = await handleAdminSendRequest({
    request: jsonRequest(
      "https://www.capitalbench.org/api/email/send",
      {
        groupSlug: "website_collection",
        subject: "Update",
        html: "<p>Hello</p>",
        text: "Hello",
        testRecipient: "test@example.com"
      },
      { authorization: "Bearer admin-token" }
    ),
    env,
    repo
  });

  assert.equal(result.status, 200);
  assert.equal(result.body.mode, "test");
  assert.equal(env.sent.length, 1);
  assert.equal(env.sent[0].to, "test@example.com");
  assert.equal(env.sent[0].subject, "[TEST] Update");
});

test("admin send refuses to send without mailing address footer config", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv({ EMAIL_MAILING_ADDRESS: "" });
  const result = await handleAdminSendRequest({
    request: jsonRequest(
      "https://www.capitalbench.org/api/email/send",
      {
        groupSlug: "website_collection",
        subject: "Update",
        html: "<p>Hello</p>",
        text: "Hello",
        testRecipient: "test@example.com"
      },
      { authorization: "Bearer admin-token" }
    ),
    env,
    repo
  });

  assert.equal(result.status, 500);
  assert.equal(result.body.error, "missing_config");
  assert.deepEqual(result.body.missing, ["EMAIL_MAILING_ADDRESS"]);
  assert.equal(env.sent.length, 0);
});

test("admin send requires Resend API key when Resend provider is selected", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv({ EMAIL_PROVIDER: "resend", RESEND_API_KEY: "" });
  const result = await handleAdminSendRequest({
    request: jsonRequest(
      "https://www.capitalbench.org/api/email/send",
      {
        groupSlug: "website_collection",
        subject: "Update",
        html: "<p>Hello</p>",
        text: "Hello",
        testRecipient: "test@example.com"
      },
      { authorization: "Bearer admin-token" }
    ),
    env,
    repo
  });

  assert.equal(result.status, 500);
  assert.equal(result.body.error, "missing_config");
  assert.deepEqual(result.body.missing, ["RESEND_API_KEY"]);
});

test("admin test send uses Resend when Resend provider is selected", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv({
    EMAIL: undefined,
    EMAIL_PROVIDER: "resend",
    RESEND_API_KEY: "resend-key"
  });

  await withMockFetch(async (calls) => {
    const result = await handleAdminSendRequest({
      request: jsonRequest(
        "https://www.capitalbench.org/api/email/send",
        {
          groupSlug: "website_collection",
          subject: "Update",
          html: "<p>Hello</p>",
          text: "Hello",
          testRecipient: "test@example.com"
        },
        { authorization: "Bearer admin-token" }
      ),
      env,
      repo,
      now: new Date("2026-05-31T13:00:00Z")
    });

    assert.equal(result.status, 200);
    assert.equal(result.body.provider, "resend");
    assert.equal(result.body.messageId, "resend-message-1");
    assert.equal(calls.length, 1);
    assert.equal(calls[0].url, "https://api.resend.com/emails");
    assert.equal(calls[0].init.headers.authorization, "Bearer resend-key");
    assert.ok(calls[0].init.headers["Idempotency-Key"]);
    assert.equal(calls[0].body.from, "updates@capitalbench.org");
    assert.equal(calls[0].body.to, "test@example.com");
    assert.equal(calls[0].body.subject, "[TEST] Update");
    assert.equal(calls[0].body.reply_to, "hello@capitalbench.org");
    assert.match(calls[0].body.html, /Unsubscribe/);
  });
});

test("admin send rejects unsupported audience groups", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv();
  const result = await handleAdminSendRequest({
    request: jsonRequest(
      "https://www.capitalbench.org/api/email/send",
      {
        groupSlug: "future_group",
        subject: "Update",
        html: "<p>Hello</p>",
        text: "Hello"
      },
      { authorization: "Bearer admin-token" }
    ),
    env,
    repo
  });

  assert.equal(result.status, 400);
  assert.equal(result.body.error, "unsupported_group");
  assert.deepEqual(result.body.supportedGroups, ["website_collection"]);
  assert.equal(env.sent.length, 0);
});

test("admin group send stops before Resend free daily cap is exceeded", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv({
    EMAIL: undefined,
    EMAIL_PROVIDER: "resend",
    RESEND_API_KEY: "resend-key",
    RESEND_DAILY_SEND_LIMIT: "1"
  });
  await subscribe(repo, env, "one@example.com", "homepage");
  await subscribe(repo, env, "two@example.com", "footer");

  await withMockFetch(async (calls) => {
    const result = await handleAdminSendRequest({
      request: jsonRequest(
        "https://www.capitalbench.org/api/email/send",
        {
          groupSlug: "website_collection",
          subject: "CapitalBench update",
          html: "<p>Hello</p>",
          text: "Hello"
        },
        { authorization: "Bearer admin-token" }
      ),
      env,
      repo
    });

    assert.equal(result.status, 409);
    assert.equal(result.body.error, "daily_send_limit_exceeded");
    assert.equal(result.body.provider, "resend");
    assert.equal(result.body.recipientCount, 2);
    assert.equal(result.body.dailySendLimit, 1);
    assert.equal(calls.length, 0);
    assert.equal(repo.campaigns.size, 0);
  });
});

test("admin group send sends to active Website Collection members and skips unsubscribed", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv();
  await subscribe(repo, env, "one@example.com", "homepage");
  await subscribe(repo, env, "two@example.com", "footer");
  const unsubscribed = Array.from(repo.subscribers.values()).find((item) => item.email === "two@example.com");
  await repo.unsubscribeSubscriber(unsubscribed.id, "2026-06-01T12:00:00Z");

  const result = await handleAdminSendRequest({
    request: jsonRequest(
      "https://www.capitalbench.org/api/email/send",
      {
        groupSlug: "website_collection",
        subject: "CapitalBench update",
        html: "<p>Hello</p>",
        text: "Hello"
      },
      { authorization: "Bearer admin-token" }
    ),
    env,
    repo
  });

  assert.equal(result.status, 200);
  assert.equal(result.body.ok, true);
  assert.equal(result.body.recipientCount, 1);
  assert.equal(result.body.sentCount, 1);
  assert.equal(env.sent.length, 1);
  assert.equal(env.sent[0].to, "one@example.com");
  assert.match(env.sent[0].html, /Unsubscribe/);
  assert.match(env.sent[0].headers["List-Unsubscribe"], /\/unsubscribe\?token=/);
  assert.equal(repo.campaigns.size, 1);
  assert.equal(Array.from(repo.campaigns.values())[0].status, "sent");
});

test("admin group send uses Resend for active Website Collection members", async () => {
  const repo = createMemoryEmailRepository();
  const env = makeEnv({
    EMAIL: undefined,
    EMAIL_PROVIDER: "resend",
    RESEND_API_KEY: "resend-key"
  });
  await subscribe(repo, env, "one@example.com", "homepage");

  await withMockFetch(async (calls) => {
    const result = await handleAdminSendRequest({
      request: jsonRequest(
        "https://www.capitalbench.org/api/email/send",
        {
          groupSlug: "website_collection",
          subject: "CapitalBench update",
          html: "<p>Hello</p>",
          text: "Hello"
        },
        { authorization: "Bearer admin-token" }
      ),
      env,
      repo,
      now: new Date("2026-05-31T13:00:00Z")
    });

    assert.equal(result.status, 200);
    assert.equal(result.body.provider, "resend");
    assert.equal(result.body.sentCount, 1);
    assert.equal(calls.length, 1);
    assert.equal(calls[0].body.to, "one@example.com");
    assert.match(calls[0].body.headers["List-Unsubscribe"], /\/unsubscribe\?token=/);
    assert.equal(Array.from(repo.campaigns.values())[0].provider, "resend");
  });
});

test("campaign CLI dry-run renders a local campaign file", async () => {
  const { stdout } = await execFileAsync(
    process.execPath,
    [
      "scripts/email-campaign.mjs",
      "--file",
      "campaigns/example/update.md",
      "--subject",
      "CapitalBench update",
      "--dry-run"
    ],
    { cwd: new URL("..", import.meta.url).pathname }
  );
  const result = JSON.parse(stdout);
  assert.equal(result.ok, true);
  assert.equal(result.mode, "dry-run");
  assert.equal(result.group, "website_collection");
  assert.ok(result.htmlBytes > 0);
});
