from django.db import models

class InternshipApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    university = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
