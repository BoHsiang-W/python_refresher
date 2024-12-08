import os
import requests
from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")


def send_simple_message(to, subject, body):
    return requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN}/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={
            "from": "Mailgun Sandbox <mailgun@{DOMAIN}>",
            "to": [to],
            "subject": subject,
            "text": body,
        },
    )


def send_user_registered_email(email, username):
    send_simple_message(
        email,
        "Sign Up Confirmation",
        f"Hello {username}, welcome to the API!",
    )
