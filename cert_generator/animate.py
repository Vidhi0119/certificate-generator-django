import io
import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

FONT_PATH = os.path.abspath("times.ttf")
CSV_PATH = os.path.abspath("nss_camp_2025.csv")
TEMPLATES = {
    "NSS Camp 2025": os.path.abspath("camp.jpg"),
    "Stem Cell Donation Drive": os.path.abspath("stemcell.jpg"),
    "Grain-a-thon 2.0": os.path.abspath("grainathon.jpg"),
}

def is_name_in_csv(name):
    try:
        df = pd.read_csv(CSV_PATH)
        df["Name"] = df["Name"].str.strip().str.lower()
        return name.strip().lower() in df["Name"].values
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return False

def overlay_name_on_template(name, event):
    img_path = TEMPLATES.get(event, list(TEMPLATES.values())[0])
    template_img = Image.open(img_path)
    draw = ImageDraw.Draw(template_img)

    x = template_img.width / 2
    y = template_img.height / 2 - 50

    font = ImageFont.truetype(FONT_PATH, 80)
    draw.text((x, y), name, fill=(0, 0, 0), anchor="mm", font=font)
    return template_img

def generate_pdf_with_image(name, event):
    img_with_overlay = overlay_name_on_template(name, event)
    img_buffer = io.BytesIO()
    img_with_overlay.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=(img_with_overlay.width, img_with_overlay.height))
    img = ImageReader(img_buffer)
    c.drawImage(img, 0, 0, width=img_with_overlay.width, height=img_with_overlay.height)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer


def send_email(name, event, email, pdf_buffer):
    from django.core.mail import EmailMessage
    subject = f"Your Certificate for {event}"
    body = f"Dear {name},\n\nYour participation in {event} has been acknowledged. Your certificate is attached."
    message = EmailMessage(subject, body, to=[email])
    message.attach(f"{name}_{event}.pdf", pdf_buffer.read(), 'application/pdf')
    message.send()
