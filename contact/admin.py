from django.contrib import admin
from .models import Faq
from .models import Contact

# Register your models here.
admin.site.register(Faq)
admin.site.register(Contact)