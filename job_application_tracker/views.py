from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        return redirect("applications:applications_list")
    else:
        return render(request, "home.html")