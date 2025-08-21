from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    # App URLs
    path('', include('core.urls')),    # Home and core app
    path('kids/', include('kids.urls')),
    path('billing/', include('billing.urls')),

    # Optional root redirect if no home view in core
    # path('', RedirectView.as_view(pattern_name='home', permanent=False)),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
