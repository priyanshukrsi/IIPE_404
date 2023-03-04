from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request,'index.html')


def camera(request):
    return render(request,'camera.html')


import subprocess
from django.http import HttpResponse


def start(request):

    subprocess.call(["python", "/path/to/your/script.py"])
    return HttpResponse("Script has been run!")



    
