from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")    

def nest(request):
    return render(request, "nest.html")    

def study(request):
    return render(request, "studyroom.html")    

def chat(request):
    return render(request, "chat.html")

def wellbeing(request):
    return render(request, "wellbeing.html")    

