import smtplib
from ssl import create_default_context
from email.message import EmailMessage
from utility.message import subject, body_email
from dynaconf import settings


def pdf_attchment():
    with open(settings.FILE, "rb") as f:
        file_data = f.read()
        file_name = f.name

    return file_data, file_name


def menssage_email():
    file_data, file_name = pdf_attchment()
    newMessage = EmailMessage()
    newMessage["Subject"] = subject
    newMessage["From"] = settings.SENDER_EMAIL
    newMessage["To"] = settings.RECIEVER_EMAIL
    newMessage.set_content(body_email)
    newMessage.add_attachment(
        file_data,
        maintype="application",
        subtype="octet-stream",
        filename=file_name
    )
    return newMessage


def send_email(sender_email, password, name_smtp, port):
    newMessage = menssage_email()

    with smtplib.SMTP_SSL(
        name_smtp, port,
        context=create_default_context()
    ) as smtp:

        smtp.login(sender_email, password)
        smtp.send_message(newMessage)
