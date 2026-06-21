from app.database import get_contacts
from app.messages import build_message
from app.zapi import send_message


def main():
    contacts = get_contacts()

    for contact in contacts:
        message = build_message(contact["nome_contato"])
        phone = contact["telefone"]
        send_message(phone, message)






if __name__ == "__main__":
    main()