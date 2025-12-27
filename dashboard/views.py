from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import get_basic_metrics, get_evolution_data
import json

# Create your views here.
@login_required
def user_dashboard(request):
    metrics = get_basic_metrics(request.user)
    evolution_data = get_evolution_data(request.user)
    
    return render(request, "dashboard/dashboard.html", {
        "metrics": metrics, 
        "evolution_data": json.dumps(evolution_data)
    })