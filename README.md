# Django-Development

### Basic Installation
1. Python latest version: https://www.python.org/downloads/
2. Visual Studio Code
3. Check python and pip version
```
$ python3 --version
$ pip3 --version
```
4. Installing Django
```
$ pip3 install django
```
5. Check installed django
```
$ django-admin
```
6. VSCode Extensions: Django, Python

### Create Project
1. Creating Django Project
```
$ django-admin startproject project_name
```
2. Navigate to project directory & Run Django server
```
$ python3 manage.py runserver
```

### File Structure of Django Project
```
1. Main Folder
2. Project Folder
3. App Folder
4. Media Folder
5. Template Folder
6. Static Folder
```

### Create Django App
1. Create a django app
```
$ python3 manage.py startapp app_name
```

### Database Migrations
1. Make Migrations
```
$ python3 manage.py makemigrations
```
2. Migrate
```
$ python3 manage.py migrate
```

### Create Superuser
```
$ python3 manage.py createsuperuser
```

### Installing Django Crispy Forms
1. Install Django Crispy Forms module
```
$ pip3 install django-crispy-forms
$ pip3 install crispy-bootstrap5
```
2. Add crispy_forms to INSTALLED_APPS in settings.py file
```
INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_bootstrap5",
)

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"
```

### Setup Server Time Zone
1. Update settings.py file
```
TIME_ZONE = 'Asia/Dhaka'
```

### Set MEDIA_ROOT & MEDIA_URL Key in settings.py
1. Add this inside settings.py file
```
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```
2. Add file restore in project urls.py
```
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Install Pillow package
```
$ pip3 install Pillow
```

### Install Django-multiselectfield package
1. Install django-multiselectfield package
```
$ pip3 install django-multiselectfield
```
2. Add django-multiselectfield package to settings.py
```
INSTALLED_APPS = [
    ...
    "multiselectfield",
]
```

### Django-admin shell (Python Interactive interpreter)
```
$ python3 manage.py shell
```
Uses of relative name
```
$ from tuition.models import Subject
$ physics = Subject.objects.get(name='Physics')
$ physics.subject_set.all()
```