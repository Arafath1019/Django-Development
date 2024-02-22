from django import forms
from .models import Contact

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, label="Your Name")
#     phone = forms.CharField(max_length=100, label="Your Phone")
#     content = forms.CharField(max_length=100, label="Your content")
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'