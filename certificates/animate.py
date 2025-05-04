import io
import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

FONT_PATH = os.path.abspath("times.ttf")
CSV_PATH = os.path.join(os.path.dirname(__file__), 'event_participants.csv')

TEMPLATES = {
    "Hackniche": os.path.join(os.path.dirname(__file__), "camp.jpg"),
    "Hackniche": os.path.join(os.path.dirname(__file__), "camp.jpg"),
}

def is_name_in_csv(name):
    try:
        df = pd.read_csv(CSV_PATH)
        df.columns = df.columns.str.strip()
        df["Name"] = df["Name"].astype(str).str.strip().str.lower()
        return name.strip().lower() in df["Name"].values
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return False

def get_user_details(name):
    try:
        df = pd.read_csv(CSV_PATH)
        df.columns = df.columns.str.strip()
        row = df[df["Name"].str.strip().str.lower() == name.strip().lower()]
        if not row.empty:
            user_data = row.iloc[0]
            user_department = user_data.get("Department", "")
            user_event = user_data.get("Event", "")
            user_organization = user_data.get("Organization", "")
            return user_department, user_event, user_organization
        else:
            return "", "", ""
    except Exception as e:
        print(f"Error fetching user details: {e}")
        return "", "", ""

def overlay_name_on_template(name, event):
    img_path = TEMPLATES.get(event, list(TEMPLATES.values())[0])
    template_img = Image.open(img_path)
    draw = ImageDraw.Draw(template_img)

    font_title = ImageFont.truetype(FONT_PATH, 60)  # Name Font
    font_medium = ImageFont.truetype(FONT_PATH, 40) # Other text font

    x_center = template_img.width / 2

    # Fetch user details
    user_department, user_event, user_organization = get_user_details(name)

    # Draw the Name
    draw.text((x_center, 660), name, fill="black", font=font_title, anchor="mm")

    # Draw Department (left to right)
    draw.text((x_center - 85, 760), str(user_department), fill="black", font=font_medium, anchor="mm")

    # Draw Event (right to left)
    draw.text((x_center - 400, 860), str(user_event), fill="black", font=font_medium, anchor="mm")

    # Draw Organization (bottom center)
    draw.text((x_center + 500, 860), str(user_organization), fill="black", font=font_medium, anchor="mm")

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
