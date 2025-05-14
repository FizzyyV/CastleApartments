# account/urls.py

from django.urls import path
from . import views
from .views import SignUpView


urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path("signup/", SignUpView.as_view(), name="signup"),
]



# from django.urls import path
# from . import views
#
# urlpatterns = [
#
#
#     path('login/', views.login_view, name='login'),
#     path('signup/', views.signup_view, name='signup'),
#     path('profile/', views.profile_view, name='profile'),
# ]

