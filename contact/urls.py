from django.urls import path
from . import views

urlpatterns = [
   path('contact/', views.contact, name='contact'),
   path('faq/', views.faq_page, name='faq_page'),
   path('add/<int:faq_id>/', views.add_faq, name='add_faq'),
   path('edit/<int:faq_id>/', views.edit_faq, name='edit_faq'),
   path('delete/<int:faq_id>/', views.delete_faq, name='delete_faq')
]