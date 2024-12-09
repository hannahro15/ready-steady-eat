from django.db import models
from django.conf import settings

# Create your models here.

class Contact(models.Model):
        firstName = models.CharField(max_length=250, null=False, blank=True)
        lastName = models.CharField(max_length=250, null=False, blank=True)
        email = models.EmailField(max_length=250, null=False, blank=True)
        phone = models.IntegerField(null=False, blank=True)
        comments = models.TextField(max_length=250, null=False, blank=True)

class Faq(models.Model):
        question = models.CharField(max_length=250, null=False, blank=True)
        answer = models.TextField(max_length=250, null=False, blank=True)

        def __str__(self):
           return self.question