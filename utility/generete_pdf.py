from datetime import date
from reportlab.pdfgen import canvas
from dynaconf import settings


def generate_date():
    now_date = date.today()
    next_date = date.fromordinal((now_date.toordinal() - settings.DAYS_WORKED))
    now_date_format = now_date.strftime("%d/%m/%Y")
    next_date_format = next_date.strftime("%d/%m/%Y")

    return now_date_format, next_date_format


def create_pdf(body_pdf):
    next_date_format, now_date_format = generate_date()
    pdf_file = settings.FILE
    can = canvas.Canvas(pdf_file, bottomup=0)
    text = can.beginText(100, 50)
    text.textLines(body_pdf.format(
        now_date_format,
        next_date_format,
        settings.PAYMENT)
    )
    can.drawText(text)
    can.save()
