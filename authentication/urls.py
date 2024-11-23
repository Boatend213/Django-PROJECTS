from django.contrib.auth.views import LogoutView

from django.urls import path

from .views import *

urlpatterns = [

path("send_welcome_email/",send_welcome_email,name="send_welcome_email"),
path("login/",CustomLoginView.as_view(),name="login"),
path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
path("register/",CustomRegisterView.as_view(),name="register")
]


