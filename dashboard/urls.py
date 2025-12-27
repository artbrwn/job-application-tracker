from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path("user_dashboard/", views.user_dashboard, name="user_dashboard"),
]
