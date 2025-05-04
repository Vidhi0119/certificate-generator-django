from django import forms

class CertificateForm(forms.Form):
    name = forms.CharField(
        label='Full Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your full name'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    event = forms.ChoiceField(
        choices=[
            ('Hackniche', 'Hackniche'),
            ('Lines of Code', 'Lines of Code'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )