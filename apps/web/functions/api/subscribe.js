import {
  createD1EmailRepository,
  handleSubscribeRequest,
  resultToResponse
} from "../../src/lib/email/system.js";

export async function onRequestPost({ request, env }) {
  try {
    const repo = createD1EmailRepository(env.EMAIL_DB);
    const result = await handleSubscribeRequest({ request, env, repo });
    return resultToResponse(result);
  } catch (error) {
    return resultToResponse({
      status: 500,
      headers: {
        "content-type": "application/json; charset=utf-8",
        "cache-control": "no-store"
      },
      body: {
        ok: false,
        error: "subscription_unavailable",
        message: error instanceof Error ? error.message : "Email collection is not configured."
      }
    });
  }
}

export function onRequestGet() {
  return resultToResponse({
    status: 405,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
      allow: "POST"
    },
    body: { ok: false, error: "method_not_allowed" }
  });
}
