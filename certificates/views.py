from django.shortcuts import render
from .forms import CertificateForm
from . import animate  # this is your file
from django.core.mail import EmailMessage

def index(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            event = form.cleaned_data['event']

            if not animate.is_name_in_csv(name):
                return render(request, 'certificates/index.html', {
                    'form': form,
                    'error': 'Name not found in attendance list'
                })

            pdf = animate.generate_pdf_with_image(name, event)
            animate.send_email(name, event, email, pdf)
            return render(request, 'certificates/index.html', {
                'form': CertificateForm(),
                'success': 'Certificate sent to your email!'
            })
    else:
        form = CertificateForm()
    return render(request, 'certificates/index.html', {'form': form})

