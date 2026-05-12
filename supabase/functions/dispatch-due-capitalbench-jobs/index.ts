import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

type AutomationJob = {
  job_id: string;
  round_id: string;
  run_id: string;
  job_type: string;
};

const supabaseUrl = Deno.env.get("SUPABASE_URL") ?? "";
const serviceRoleKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "";
const githubOwner = Deno.env.get("GITHUB_OWNER") ?? "";
const githubRepo = Deno.env.get("GITHUB_REPO") ?? "";
const githubWorkflow = Deno.env.get("GITHUB_WORKFLOW") ?? "capitalbench-resolver.yml";
const githubRef = Deno.env.get("GITHUB_REF") ?? "main";
const githubToken = Deno.env.get("GITHUB_TOKEN") ?? "";

function requireEnv(name: string, value: string) {
  if (!value) throw new Error(`${name} is required`);
}

Deno.serve(async () => {
  try {
    requireEnv("SUPABASE_URL", supabaseUrl);
    requireEnv("SUPABASE_SERVICE_ROLE_KEY", serviceRoleKey);
    requireEnv("GITHUB_OWNER", githubOwner);
    requireEnv("GITHUB_REPO", githubRepo);
    requireEnv("GITHUB_TOKEN", githubToken);

    const supabase = createClient(supabaseUrl, serviceRoleKey, {
      auth: { persistSession: false },
    });
    const now = new Date().toISOString();
    const { data, error } = await supabase
      .from("automation_jobs")
      .select("job_id,round_id,run_id,job_type")
      .in("status", ["scheduled", "failed"])
      .or(`next_attempt_at_utc.lte.${now},and(next_attempt_at_utc.is.null,due_at_utc.lte.${now})`)
      .order("next_attempt_at_utc", { ascending: true })
      .order("due_at_utc", { ascending: true })
      .limit(5);

    if (error) throw error;

    const jobs = (data ?? []) as AutomationJob[];
    const dispatched: string[] = [];
    for (const job of jobs) {
      const response = await fetch(
        `https://api.github.com/repos/${githubOwner}/${githubRepo}/actions/workflows/${githubWorkflow}/dispatches`,
        {
          method: "POST",
          headers: {
            "Authorization": `Bearer ${githubToken}`,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            ref: githubRef,
            inputs: {
              round_id: job.round_id,
              run_id: job.run_id,
              job_id: job.job_id,
            },
          }),
        },
      );
      if (!response.ok) {
        const body = await response.text();
        throw new Error(`GitHub dispatch failed for ${job.job_id}: ${response.status} ${body}`);
      }
      dispatched.push(job.job_id);
    }

    return Response.json({ ok: true, dispatched });
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return Response.json({ ok: false, error: message }, { status: 500 });
  }
});
