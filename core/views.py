from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HeroSection, Feature, AboutSection, TourSection, Testimonial, Expection, TeamMember
from .forms import ContactRequestForm, TestimonialForm

def home_view(request):
    # Fetch sections
    hero = HeroSection.objects.first()
    features = Feature.objects.all()
    expections = Expection.objects.all()
    about = AboutSection.objects.all()
    tour = TourSection.objects.first()
    team_members = TeamMember.objects.filter(is_active=True).order_by('order')

    # Initialize forms
    testimonial_form = TestimonialForm(prefix="testimonial")
    contact_form = ContactRequestForm(prefix="contact")

    # Handle POST requests
    if request.method == 'POST':
        # Testimonial submission
        if 'testimonial-submit' in request.POST:
            testimonial_form = TestimonialForm(request.POST, prefix="testimonial")
            if testimonial_form.is_valid():
                testimonial = testimonial_form.save(commit=False)
                # Require admin approval before displaying
                testimonial.approved = False  
                testimonial.save()
                messages.success(request, 'Thank you! Your testimonial has been submitted and is pending admin approval.')
                return redirect('home')

        # Contact form submission
        elif 'contact-submit' in request.POST:
            contact_form = ContactRequestForm(request.POST, prefix="contact")
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, 'Your request has been submitted successfully!')
                return redirect('home')

    # Fetch only approved testimonials for display
    testimonials = Testimonial.objects.filter(approved=True).order_by('-submitted_at')

    # Render template
    return render(request, 'core/home.html', {
        'hero': hero,
        'features': features,
        'expections': expections,
        'about': about,
        'team_members': team_members,
        'tour': tour,
        'testimonial_form': testimonial_form,
        'contact_form': contact_form,
        'testimonials': testimonials,
    })


def about_view(request):
    # Fetch About section and active team members
    about = AboutSection.objects.first()
    team_members = TeamMember.objects.filter(is_active=True).order_by('order')

    return render(request, 'core/about.html', {
        'about': about,
        'team_members': team_members,
    })
