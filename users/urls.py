from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("profile/", views.profile, name="profile"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("edit_user/", views.edit_user, name="edit_user")
]
