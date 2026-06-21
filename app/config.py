import os

from dotenv import load_dotenv


load_dotenv()

def get_env_var(name):
    value = os.getenv(name)

    if not value:
        raise ValueError(
            f"Environment variable '{name}' is missing."
        )

    return value