# forms.py
from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Your Name'}),
            'message': forms.Textarea(attrs={'class': 'textarea-field', 'placeholder': 'Write your testimonial...'}),
        }
