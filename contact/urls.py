from django.urls import path
from . import views

urlpatterns = [
   path('contact/', views.contact, name='contact'),
   path('faq/', views.faq_page, name='faq_page'),
   path('edit/<int:faq_id>/', views.faq_page, name='faq_page'),
   path('delete/<int:faq_id>/', views.faq_page, name='faq_page')
]