
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import teacher

# Create your views here.
def index(request):
    teach = teacher.objects.all()
    return render(request, "MyApp1/index.html", {'content' : teach})

def home(request):
    teach = teacher.objects.all()
    return render(request, "MyApp1/home.html", {'content' : teach})


def about(request):
    teach = teacher.objects.all()
    return render(request, "MyApp1/about.html")
    return HttpResponse("This is the home page")
