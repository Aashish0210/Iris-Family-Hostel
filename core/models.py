from django.db import models
from django.utils import timezone

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)  # Only approved testimonials will be displayed

    def __str__(self):
        return f"{self.name} - {self.submitted_at.strftime('%Y-%m-%d')}"


class HeroSection(models.Model):
    title = models.TextField(max_length=255, default="Welcome to IRIS FAMILY HOSTEL")
    description = models.TextField(default="Where learning, care, and comfort come together.")
    button_text = models.CharField(max_length=50, default="Meet Our Kids")
    button_link = models.CharField(max_length=255, default="/kids/")
    image = models.ImageField(upload_to="hero_images/")

    def __str__(self):
        return "Hero Section"

class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="feature_images/", blank=True, null=True)

    def __str__(self):
        return self.title
    
class Expection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="expection_images/", blank=True, null=True)

    def __str__(self):
        return self.title

class TourSection(models.Model):
    head = models.CharField(max_length=255, default="About IRIS FAMILY HOSTEL")
    content = models.TextField(default="Hello All")

    def __str__(self):
        return self.head


class TourImage(models.Model):
    tour = models.ForeignKey(TourSection, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="Tour_images/")

    def __str__(self):
        return f"Image for {self.tour.head}"

    
class AboutSection(models.Model):
    heading = models.CharField(max_length=255, default="About IRIS FAMILY HOSTEL")
    content = models.TextField(default="Hello All")
    image = models.ImageField(upload_to="feature_images/", blank=True, null=True)


    def __str__(self):
        return self.heading
    
class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_time = models.DateTimeField()
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.date_time}"

class TeamMember(models.Model):
    role = models.CharField(max_length=100, help_text="Position or role of the team member, e.g., House Warden")
    name = models.CharField(max_length=100, help_text="Full name of the team member")
    photo = models.ImageField(upload_to="team_photos/", blank=True, null=True)
    description = models.TextField(help_text="Short bio or introduction for the team member")
    is_active = models.BooleanField(default=True, help_text="If True, will be displayed on the About page")
    order = models.PositiveIntegerField(default=0, help_text="Order of appearance on the page")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.role}"