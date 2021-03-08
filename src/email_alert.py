from smtplib import SMTP
import smtplib, ssl
import os

def sendEmail():
    port = os.environ.get('PORT')  # For SSL
    password = os.environ.get('PASSWORD_EMAIL')

    # Create a secure SSL context
    context = ssl.create_default_context()

    sender_email=os.environ.get('SENDER_EMAIL')
    receiver_email=os.environ.get('RECEIVER_EMAIL')
    message="""\
    Subject: Hi there
    This message is sent from Python."""

    with smtplib.SMTP_SSL(os.environ.get('SMTP'), port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
