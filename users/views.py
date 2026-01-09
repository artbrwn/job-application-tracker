from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuario creado")
            return redirect("applications:applications_list")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("applications:applications_list")
    else:
        form = CustomAuthenticationForm()
    
    return render(request, "users/login.html", {"form": form})

def profile(request):
    return HttpResponse("Profile page")

@login_required
def edit_user(request):
    current_user = request.user
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Se han guardado los cambios en tu perfil')
            return redirect("applications:applications_list")
    else:
        form = CustomUserChangeForm(instance=current_user)

    return render(request, "users/edit_user.html", {"form": form})