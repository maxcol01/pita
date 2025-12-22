import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("PASSWORD2")
SUBJECT = f"Contact from {email} concerning {subject}"
SERVER = "smtp.gmail.com"
FILE = "email_list.txt"

message = MIMEMultipart()

message["From"] = SENDER_EMAIL
message["Subject"] = SUBJECT

BODY = f"{message_content}"


message.attach(MIMEText(BODY, "plain"))
message_string = message.as_string()

message["To"] = f"{email_contact}"


with smtplib.SMTP(SERVER) as connection:
    connection.starttls()
    connection.login(user=SENDER_EMAIL,password=PASSWORD)
    connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=email_contact, msg=message_string)