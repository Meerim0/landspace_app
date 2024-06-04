from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InternshipApplicationForm, ContactMessageForm


def home(request):
    return render(request, 'landspaceapp/home.html') # Corrected typo (lowercase 'h')

def internship_application_view(request):
    if request.method == 'POST':
        form = InternshipApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Ваше заявление на стажировку отправлено успешно!")
    else:
        form = InternshipApplicationForm()
    return render(request, 'landscapeapp/internship_application.html', {'form': form})  # Ensure the correct path

def contact_message_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Ваше сообщение отправлено успешно!")
    else:
        form = ContactMessageForm()
    return render(request, 'landscapeapp/contact_message.html', {'form': form})