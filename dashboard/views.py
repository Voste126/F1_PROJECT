from django.shortcuts import render

# Create your views here.
# dashboard/views.py
from django.shortcuts import render

def home(request):
    context = {
        'message': 'Welcome to the F1 Dashboard!'
    }
    return render(request, 'dashboard/home.html', context)
