from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=255, default="Welcome to IRIS FAMILY HOSTEL")
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

class AboutSection(models.Model):
    heading = models.CharField(max_length=255, default="About IRIS FAMILY HOSTEL")
    content = models.TextField(default="Hello All")

    def __str__(self):
        return "About Section"
