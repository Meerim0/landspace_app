from django.contrib import admin
from .models import InternshipApplication, ContactMessage

class InternshipApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'university', 'message')  # Corrected typo

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

admin.site.register(InternshipApplication, InternshipApplicationAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
