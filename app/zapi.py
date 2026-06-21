import requests

from app.config import get_env_var


def send_message(phone, message):
    instance_id = get_env_var("ZAPI_INSTANCE_ID")
    instance_token = get_env_var("ZAPI_INSTANCE_TOKEN")
    url = f"https://api.z-api.io/instances/{instance_id}/token/{instance_token}/send-text"
    payload = {
        "phone": phone,
        "message": message
    }
    response = requests.post(
        url,
        json=payload
    )
    if response.status_code == 200:
        return True
    else:
        print(response.text)
        return False