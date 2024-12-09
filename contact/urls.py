from django.urls import path
from . import views

urlpatterns = [
   path('contact/', views.contact, name='contact'),
   path('faq/', views.faq_page, name='faq_page'),
   path('faq/edit/<int:faq_id>/', views.edit_faq, name='edit_faq'),
   path('faq/delete/<int:faq_id>/', views.delete_faq, name='fdelete_faq')
]