from django.urls import path
from .views import invoice_list, invoice_detail, generate_invoices

urlpatterns = [
    path('invoices/', invoice_list, name='invoice_list'),
    path('invoices/<int:pk>/', invoice_detail, name='invoice_detail'),
    path('generate/', generate_invoices, name='generate_invoices'),
]
