from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path("applications_list/", views.applications_list, name="applications_list"),
    path("edit_application/<int:pk>", views.edit_application, name="edit_application"),
    path("delete_application/<int:pk>", views.delete_application, name="delete_application")
]
