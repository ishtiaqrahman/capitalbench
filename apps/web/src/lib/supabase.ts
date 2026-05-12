import { createClient, type SupabaseClient } from "@supabase/supabase-js";

let client: SupabaseClient | null = null;

export function hasSupabaseConfig(): boolean {
  return Boolean(import.meta.env.PUBLIC_SUPABASE_URL && import.meta.env.PUBLIC_SUPABASE_ANON_KEY);
}

export function getSupabaseClient(): SupabaseClient | null {
  if (!hasSupabaseConfig()) {
    return null;
  }
  if (client === null) {
    client = createClient(import.meta.env.PUBLIC_SUPABASE_URL!, import.meta.env.PUBLIC_SUPABASE_ANON_KEY!);
  }
  return client;
}

export async function fetchPublicRows<T>(
  table: string,
  fallback: T[],
  order?: { column: string; ascending?: boolean }
): Promise<T[]> {
  const supabase = getSupabaseClient();
  if (supabase === null) {
    return fallback;
  }
  let query = supabase.from(table).select("*").eq("published", true);
  if (order) {
    query = query.order(order.column, { ascending: order.ascending ?? true });
  }
  const { data, error } = await query;
  if (error || !data) {
    return fallback;
  }
  return data as T[];
}
