from django.shortcuts import render, HttpResponse
from .models import Contact, Post, Subject
from .forms import ContactForm, PostForm
from django.views import View

# Create your views here.

class ContactView(View):
    form_class = ContactForm
    template_name = "contact.html"
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        
        return render(request, self.template_name, {"form": form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # if form.is_valid():
        #     name = form.cleaned_data['name']
        #     phone = form.cleaned_data['phone']
        #     content = form.cleaned_data['content']
        #     obj = Contact(name=name, phone=phone, content=content)
        #     obj.save()
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def postview(request):
    post = Post.objects.all()
    
    return render(request, 'tuition/postview.html', {'post': post})

def subjectview(request):
    sub = Subject.objects.get(name="English")
    post = sub.subject_set.all()
    return render(request, 'tuition/subjectview.html', {'sub': sub, 'post': post})

def postCreate(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            sub = form.cleaned_data['subject']
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in = form.cleaned_data['class_in']
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
            return HttpResponse("Success")
    else:
        form = PostForm()
    
    return render(request, 'tuition/postcreate.html', {'form': form})
