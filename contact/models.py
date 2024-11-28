from django.db import models
from django.conf import settings

# Create your models here.

class Faq(models.Model):
        question = models.CharField(max_length=250, null=False, blank=True)
        answer = models.TextField(max_length=250, null=False, blank=True)

        def __str__(self):
           return self.question