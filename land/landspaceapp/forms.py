from django import forms
from .models import InternshipApplication, ContactMessage

class InternshipApplicationForm(forms.ModelForm):
    class Meta:
        model = InternshipApplication
        fields = ['name', 'email', 'university', 'message']

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
