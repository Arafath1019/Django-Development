from django.urls import path
from .views import contact, postview, postCreate, subjectview, ContactView
from .forms import ContactForm2

urlpatterns = [
    # path('contact/', contact, name="contact"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('contact2/', ContactView.as_view(form_class=ContactForm2, template_name="contact2.html"), name="contact"),
    path('posts/', postview, name="posts"),
    path('create/', postCreate, name="create"),
    path('subjects/', subjectview, name="subjects"),
]
