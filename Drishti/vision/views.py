from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request,'home.html')


def start(request):
    return render(request,'start.html')
