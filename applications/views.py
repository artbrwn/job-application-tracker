from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Application
from .forms import ApplicationForm
from datetime import datetime
from django.contrib import messages

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
    applications = Application.objects.filter(user=request.user).select_related('company').order_by('-application_date')
    return render(request, "applications/applications_list.html", {'applications': applications, "form": form})

@login_required
def edit_application(request, pk):
    application = get_object_or_404(Application, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save(user=request.user)
            messages.success(request, f'La candidatura ha sido editada correctamente.')
            return redirect('applications:applications_list')

    else:
        form = ApplicationForm(instance=application, initial={
            'company_name': application.company.name
        })
    
    return render(request, 'applications/edit_application.html', {
        'form': form,
        'application': application
    })

@login_required
def delete_application(request, pk):
    application = get_object_or_404(Application, pk=pk, user=request.user)

    if request.method == "POST":
        app_title = application.title
        app_company = application.company.name

        application.delete()
        
        messages.success(request, f'La candidatura para el puesto "{app_title}" en {app_company} ha sido eliminada correctamente.')

        return redirect("applications:applications_list")
        
    return render(request, "applications/delete_application.html", {"application": application})