from django.shortcuts import render
from .models import Kid

def kid_list(request):
    kids = Kid.objects.filter(active=True).order_by('name')
    return render(request, 'kids/kid_list.html', {'kids': kids})
