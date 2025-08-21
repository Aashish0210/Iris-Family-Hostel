from django.contrib import admin
from .models import Kid

@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):
    list_display = ('name','parent_name','age','room_number','active')
    search_fields = ('name','parent_name','room_number')
    list_filter = ('active',)
