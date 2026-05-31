import {
  createD1EmailRepository,
  handleUnsubscribeRequest,
  htmlResponse
} from "../src/lib/email/system.js";

export async function onRequestGet({ request, env }) {
  try {
    const repo = createD1EmailRepository(env.EMAIL_DB);
    return await handleUnsubscribeRequest({ request, env, repo });
  } catch (error) {
    return htmlResponse(
      `<!doctype html>
<html lang="en">
  <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Email unavailable - CapitalBench</title></head>
  <body>
    <main style="font-family:system-ui,sans-serif;max-width:560px;margin:12vh auto;padding:24px;line-height:1.5">
      <h1>Email system unavailable</h1>
      <p>${error instanceof Error ? error.message : "The unsubscribe service is not configured."}</p>
      <p><a href="/">Return to CapitalBench</a></p>
    </main>
  </body>
</html>`,
      500
    );
  }
}
