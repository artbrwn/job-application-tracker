from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path("applications_list/", views.applications_list, name="applications_list"),
]
