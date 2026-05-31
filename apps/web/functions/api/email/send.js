import {
  createD1EmailRepository,
  handleAdminSendRequest,
  resultToResponse
} from "../../../src/lib/email/system.js";

export async function onRequestPost({ request, env }) {
  try {
    const repo = createD1EmailRepository(env.EMAIL_DB);
    const result = await handleAdminSendRequest({ request, env, repo });
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
        error: "email_send_unavailable",
        message: error instanceof Error ? error.message : "Email sending is not configured."
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
