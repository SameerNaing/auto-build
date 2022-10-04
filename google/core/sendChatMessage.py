from settings import CHAT_SPACE_ID

from .credential import chat_credential


__all__ = ["send_message"]


def send_message(message: dict):
    """Function to send message on google chat

    Args:
        message (dict): {"text":"..."} or {"card", ...}, message to send
    """
    try:
        chat_credential.spaces().messages().create(
            parent=f"spaces/{CHAT_SPACE_ID}",
            body=message
        ).execute()
    except Exception as e:
        return
