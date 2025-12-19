from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Application
from .forms import ApplicationForm
from datetime import datetime

# Create your views here.
@login_required
def applications_list(request):
    
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.application_date = datetime.now()
            application.save()
            return redirect('applications:applications_list')
            
    form = ApplicationForm()
    applications = Application.objects.filter(user=request.user).order_by('-application_date')

    return render(request, "applications/applications_list.html", {'applications': applications, "form": form})