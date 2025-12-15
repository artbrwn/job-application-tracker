from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})

def login(request):
    return HttpResponse("Login page")

def logout(request):
    return HttpResponse("Logout page")

def profile(request):
    return HttpResponse("Profile page")