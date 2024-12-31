from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=250, null=False, blank=False)
    last_name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    phone = models.IntegerField(null=True, blank=True)
    comments = models.TextField(max_length=250, null=False, blank=False)


class Faq(models.Model):
    question = models.CharField(max_length=250, null=False, blank=True)
    answer = models.TextField(max_length=250, null=False, blank=True)

    def __str__(self):
        return self.question
