import {
  createD1PrivateEvalRepository,
  handlePrivateEvalRequest
} from "../../src/lib/privateEvals.js";
import { resultToResponse } from "../../src/lib/email/system.js";

export async function onRequestPost({ request, env }) {
  try {
    const repo = createD1PrivateEvalRepository(env.EMAIL_DB);
    const result = await handlePrivateEvalRequest({ request, env, repo });
    return resultToResponse(result);
  } catch (error) {
    const message =
      error instanceof Error ? error.message : "Private eval request service is not configured.";
    return resultToResponse({
      status: 500,
      headers: {
        "content-type": "application/json; charset=utf-8",
        "cache-control": "no-store"
      },
      body: {
        ok: false,
        error: "private_eval_unavailable",
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
