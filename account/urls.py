# account/urls.py

from django.urls import path

from .views import SignUpView, ProfileView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/<str:username>/", ProfileView.as_view(), name="profile"),

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

