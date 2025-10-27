from django.contrib import admin
from .models import HeroSection, Feature, AboutSection, TourSection, TourImage, Testimonial, Expection,TeamMember
from .models import ContactRequest

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_time', 'submitted_at')
    list_filter = ('date_time', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    ordering = ('-submitted_at',)


admin.site.register(HeroSection)
admin.site.register(Feature)
admin.site.register(TourSection)
admin.site.register(TourImage)
admin.site.register(AboutSection)
admin.site.register(Testimonial)
admin.site.register(Expection)
admin.site.register(TeamMember)

