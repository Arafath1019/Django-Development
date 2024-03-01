from django import forms
from .models import Contact, Post

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, label="Your Name")
#     phone = forms.CharField(max_length=100, label="Your Phone")
#     content = forms.CharField(max_length=100, label="Your content")
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
class ContactForm2(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','id','created_at','slug']
        widgets = {
            'class_in': forms.CheckboxSelectMultiple(attrs={
                'multiple': True,
            }),
            'subject': forms.CheckboxSelectMultiple(attrs={
                'multiple': True,
            })
        }