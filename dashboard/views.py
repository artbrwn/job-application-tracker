from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import get_basic_metrics

# Create your views here.
@login_required
def user_dashboard(request):
    metrics = get_basic_metrics(request.user)
    return render(request, "dashboard/dashboard.html", {"metrics":metrics})