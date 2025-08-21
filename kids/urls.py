from django.urls import path
from .views import kid_list

urlpatterns = [
    path('', kid_list, name='kid_list'),
]
