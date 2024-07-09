from django.urls import path

from .views import *

urlpatterns = [
    path("login_user/", login_user, name="login_user"),
    path("signup_user/", signup_user, name="signup_user"),
    path("logout_user/", logout_user, name="logout_user"),
]