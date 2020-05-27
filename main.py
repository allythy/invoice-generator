from utility.generete_pdf import create_pdf
from utility.send_email import send_email
from utility.message import body_pdf
from loguru import logger
from dynaconf import settings


def main():
    create_pdf(body_pdf)
    logger.info("Generating PDF")
    send_email(
        settings.SENDER_EMAIL,
        settings.EMAIL_PASSWORD,
        settings.NAME_SMTP,
        settings.PORT
        )
    logger.info("Send email")


if __name__ == "__main__":
    main()
