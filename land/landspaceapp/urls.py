from django.urls import path
from .views import home, internship_application_view, contact_message_view

urlpatterns = [
    path('', home, name='home'),
    path('internship_application/', internship_application_view, name='internship_application'),
    path('contact_message/', contact_message_view, name='contact_message'),
]
