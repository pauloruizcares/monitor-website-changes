from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
import os

def sendEmail(message):
    port = os.environ.get('PORT')  # For SSL
    password = os.environ.get('PASSWORD_EMAIL')

    sender_email=os.environ.get('SENDER_EMAIL')
    receiver_email=os.environ.get('RECEIVER_EMAIL')

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Reservas"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Create a secure SSL context
    context = ssl.create_default_context()

    message_html = MIMEText(message, 'html')

    msg.attach(message_html)

    with smtplib.SMTP_SSL(os.environ.get('SMTP'), port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
