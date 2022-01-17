from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200,unique=True)
    phone_no = models.CharField(max_length=15,unique=True)
    body = models.TextField()

    def __str__(self):
        return f"{self.name}"

