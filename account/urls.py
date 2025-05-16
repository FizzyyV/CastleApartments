# account/urls.py
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views



urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.custom_login, name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', views.profile, name='profile'),
]
