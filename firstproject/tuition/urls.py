from django.urls import path
from .views import contact, postview, postCreate
urlpatterns = [
    path('contact/', contact, name="contact"),
    path('posts/', postview, name="posts"),
    path('create/', postCreate, name="create"),
]
