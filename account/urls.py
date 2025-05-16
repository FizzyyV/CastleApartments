# account/urls.py

from django.urls import path
from . import views
#from .views import SignUpView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),



    #path('login/', views.custom_login, name='login'),
    #path("signup/", views.custom_signup(), name="signup"),
    #path("profile/", views.profile_view, name='profile'),
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

