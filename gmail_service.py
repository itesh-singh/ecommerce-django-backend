import os
import base64
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def send_gmail_email(to_email, subject, html_message):
    creds = Credentials(
        None,
        refresh_token=os.getenv("GMAIL_REFRESH_TOKEN"),
        token_uri=os.getenv("GMAIL_TOKEN_URI"),
        client_id=os.getenv("GMAIL_CLIENT_ID"),
        client_secret=os.getenv("GMAIL_CLIENT_SECRET"),
        scopes=SCOPES,
    )

    creds.refresh(Request())

    service = build('gmail', 'v1', credentials=creds)

    message = MIMEText(html_message, 'html')
    message['to'] = to_email
    message['from'] = os.getenv("GMAIL_SENDER_EMAIL")
    message['subject'] = subject

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    send_message = (
        service.users()
        .messages()
        .send(userId='me', body={'raw': raw_message})
        .execute()
    )

    return send_message