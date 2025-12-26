import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("EMAIL_SENDER")
PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_contact_email(user_name, user_email, subject, message_content):
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = SENDER_EMAIL  # you receive the message
    message["Reply-To"] = user_email
    message["Subject"] = f"[Contact] {subject}"

    body = f"""
    New contact message:
    
    Name: {user_name}
    Email: {user_email}
    
    Message:
    {message_content}
    """
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, PASSWORD)
            server.send_message(message)
