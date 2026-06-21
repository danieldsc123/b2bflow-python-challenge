from supabase import create_client

from app.config import get_env_var

def create_supabase_client():
    supabase_url = get_env_var("SUPABASE_URL")
    supabase_key = get_env_var("SUPABASE_KEY")

    return create_client(supabase_url, supabase_key)