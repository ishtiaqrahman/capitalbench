import {
  createD1ApiAuthRepository,
  dataResultToResponse,
  handleDataApiRequest
} from "../../../src/lib/dataApi.js";

export async function onRequest({ request, env }) {
  try {
    const authRepo = createD1ApiAuthRepository(env.EMAIL_DB);
    const result = await handleDataApiRequest({ request, env, authRepo });
    return dataResultToResponse(result);
  } catch (error) {
    return dataResultToResponse({
      status: 500,
      headers: {
        "content-type": "application/json; charset=utf-8",
        "cache-control": "no-store",
        "access-control-allow-origin": "*"
      },
      body: {
        error: "api_unavailable",
        message: error instanceof Error ? error.message : "CapitalBench API is unavailable."
      }
    });
  }
}
