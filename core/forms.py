from django import forms
from .models import ContactRequest, Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Your Name'}),
            'message': forms.Textarea(attrs={'class': 'textarea-field', 'placeholder': 'Write your testimonial...'}),
        }


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'date_time', 'message']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',  # browser calendar & time picker
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 4}),
        }

