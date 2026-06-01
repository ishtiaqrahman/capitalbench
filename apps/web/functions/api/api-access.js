import {
  createD1ApiAccessRepository,
  handleApiAccessRequest
} from "../../src/lib/apiAccess.js";
import { resultToResponse } from "../../src/lib/email/system.js";

export async function onRequestPost({ request, env }) {
  try {
    const repo = createD1ApiAccessRepository(env.EMAIL_DB);
    const result = await handleApiAccessRequest({ request, env, repo });
    return resultToResponse(result);
  } catch (error) {
    const message =
      error instanceof Error ? error.message : "API access request service is not configured.";
    return resultToResponse({
      status: 500,
      headers: {
        "content-type": "application/json; charset=utf-8",
        "cache-control": "no-store"
      },
      body: {
        ok: false,
        error: "api_access_unavailable",
        message
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
    body: {
      ok: false,
      error: "method_not_allowed"
    }
  });
}
