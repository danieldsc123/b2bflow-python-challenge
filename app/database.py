from supabase import create_client

from app.config import get_env_var


def create_supabase_client():
    supabase_url = get_env_var("SUPABASE_URL")
    supabase_key = get_env_var("SUPABASE_KEY")

    return create_client(supabase_url, supabase_key)


def get_contacts():
    supabase = create_supabase_client()

    response = (
        supabase
        .table("contacts")
        .select("nome_contato, telefone")
        .limit(3)
        .execute()
    )

    return response.data