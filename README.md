A web app built with Django that allows users to generate and download custom certificates in PDF format. Ideal for course certificates or event participation.


Features:
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

4. Run migrations:
python manage.py migrate

5. Start the development server:
python manage.py runserver

6. Access the app at http://127.0.0.1:8000/.
   

Usage:
Navigate to the web app’s main page to enter the details for the certificate.
Fill in the required fields (e.g., name, course name, date).
Click the "Generate Certificate" button to create your certificate.
You can download the certificate in PDF format.


License:
MIT License




