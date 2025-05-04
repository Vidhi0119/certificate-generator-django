A web app built with Django that allows users to generate and download custom certificates in PDF format. Ideal for course certificates or event participation.


Features:
Check if the user’s name exists in a pre-uploaded Excel sheet.
Generate certificates with personalized details (e.g., name, course).
Download the generated certificate as a PDF.


Prerequisites:
Python 3.x installed on your machine.
Git installed on your machine.
Virtual environment (recommended for project isolation).


Installation:

1. Clone the repository:
git clone https://github.com/Vidhi0119/certificate-generator.git

2. Install dependencies:
pip install -r requirements.txt

3. Set up environment variables:
Create a .env file in the project root and add:
  EMAIL_USER=your_email@example.com
  EMAIL_PASS=your_email_password
You can use the example file to get started:
  cp .env.example .env

4. Add your details in Excel file:
The app will check if the entered name exists in the file.
Only names present in the sheet are allowed to generate certificates.

5. Run migrations:
python manage.py migrate

6. Start the development server:
python manage.py runserver

7. Access the app at http://127.0.0.1:8000/.
   

Usage:
1. Enter details in the Excel file containing names of people eligible for certificates:
The app will validate users based on this file.
Only users whose names exist in the Excel sheet can proceed.

2. Enter your name on the homepage.
If your name matches an entry in the uploaded Excel file, you will be allowed to generate a certificate.

3. Generate your certificate.
The app will fill in the certificate with your name and details.
Click the download button to get your certificate as a PDF.


License:
MIT License




