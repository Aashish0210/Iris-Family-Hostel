from django.db import models

class Kid(models.Model):
    name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    room_number = models.CharField(max_length=20, blank=True)
    guardian_contact = models.CharField(max_length=50, blank=True)
    admission_date = models.DateField()
    photo = models.ImageField(upload_to='kids_photos/', blank=True, null=True)

    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.parent_name})"
