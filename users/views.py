from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    return render(request, "users/register.html")

def login(request):
    return HttpResponse("Login page")

def logout(request):
    return HttpResponse("Logout page")

def profile(request):
    return HttpResponse("Profile page")