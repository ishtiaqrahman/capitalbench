# dispatch-due-capitalbench-jobs

Supabase Edge Function that wakes the GitHub Actions resolver for due
`automation_jobs`. The function does not mark jobs as running; the Python
resolver claims jobs atomically through `claim_due_automation_job` immediately
before publishing.

Required Edge Function secrets:

```bash
supabase secrets set \
  GITHUB_OWNER=ishtiaqrahman \
  GITHUB_REPO=capitalbench \
  GITHUB_WORKFLOW=capitalbench-resolver.yml \
  GITHUB_REF=main \
  GITHUB_TOKEN=<fine-grained-token-with-actions-write>
```

Create the Supabase schedule after deploying the function:

```sql
select cron.schedule(
  'dispatch-due-capitalbench-jobs',
  '17,47 * * * *',
  $$
  select net.http_post(
    url := 'https://<project-ref>.functions.supabase.co/dispatch-due-capitalbench-jobs',
    headers := jsonb_build_object(
      'Content-Type', 'application/json',
      'Authorization', 'Bearer <SUPABASE_ANON_OR_FUNCTION_TOKEN>'
    ),
    body := '{}'::jsonb
  );
  $$
);
```
