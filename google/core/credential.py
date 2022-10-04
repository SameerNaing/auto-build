from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from apiclient import discovery


__all__ = ["chat_credential", "drive_credential"]

SCOPES = ['https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/drive.metadata',
            'https://www.googleapis.com/auth/chat.bot'
            ]


CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(
    "google-service-key.json", SCOPES)

chat_credential = discovery.build(
    "chat", "v1", http=CREDENTIALS.authorize(Http()))

drive_credential = discovery.build(
    "drive", "v3", http=CREDENTIALS.authorize(Http()))
