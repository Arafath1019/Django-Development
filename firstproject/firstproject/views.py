from django.shortcuts import render, HttpResponse

def home(request):
    if request.method == 'GET':
        name = ['fahad', 'hossain', 'fahmida', 'farhana']
    else:
        name = []
    context = {
        'name': name
    }
    return render(request, 'home.html', context)