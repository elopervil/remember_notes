from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout")
]
