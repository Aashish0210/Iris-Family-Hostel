from django.shortcuts import render
from .models import HeroSection, Feature, AboutSection

def home(request):
    hero = HeroSection.objects.first()
    features = Feature.objects.all()
    about = AboutSection.objects.first()
    return render(request, 'core/home.html', {'hero': hero, 'features': features, 'about': about})
