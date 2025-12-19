from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Application

# Create your views here.
@login_required
def applications_list(request):
    applications = Application.objects.filter(user=request.user).order_by('-application_date')
    return render(request, "applications/applications_list.html", {'applications': applications})