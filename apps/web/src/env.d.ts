/// <reference types="astro/client" />

interface ImportMetaEnv {
  readonly PUBLIC_SUPABASE_URL?: string;
  readonly PUBLIC_SUPABASE_ANON_KEY?: string;
  readonly PUBLIC_GA_MEASUREMENT_ID?: string;
  readonly PUBLIC_TURNSTILE_SITE_KEY?: string;
  readonly EMAIL_PROVIDER?: "cloudflare" | "resend";
  readonly RESEND_DAILY_SEND_LIMIT?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
