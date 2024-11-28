from django.contrib import admin
from .models import Faq

# Register your models here.
class Faq(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
    )