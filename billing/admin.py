from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('kid','month','year','amount','vat_rate','total','status')
    list_filter = ('year','month','status')
    search_fields = ('kid__name','kid__parent_name')
