from email import generator
from email.policy import HTTP
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.
def home(request):
    return render(request, "generator/home.html")


def about(request):
    myname = "Oleksandr Pavych"
    return render(request, "generator/about.html", {"name": myname})

def password(request):
    characters = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    
    if request.GET.get('special'):
        characters.extend(list("!@#$%^&*()"))
    
    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))

    length = int(request.GET.get("length", 12))
    thepassword = ""

    for _ in range(length):
        thepassword += random.choice(characters)


    return render(request, "generator/password.html", {"password": thepassword})

