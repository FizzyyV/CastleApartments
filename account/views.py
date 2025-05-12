from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


import account
from .models import User
# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView




class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"




# def index(request):
#     return render(request, "account/accounts.html", context={
#         "accounts": accounts
#     })
#
# def get_account_by_id(request, id):
#     account= [x for x in accounts if x.id == id][0]
#     return render(request, "account/accounts.detail.html", context={
#         "account": account
#     })
#
#
#
#
#
#
# def login_view(request):
#     """handles login view"""
#     user = authenticate(request, email=request.POST['username'], password=request.POST['password'])
#     if user is not None:
#         login(request, user)
#         return redirect('homepage') #TODO: create homepage template
#     else:
#         return render(request, 'login', {'error': 'invalid credentials'})
#     return render(request, '' ) #TODO: template name
#
# def logout_view(request):
#     logout(request)
#     return redirect('homepage')
# def signup_view(request):
#     user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
#     return render(request, '' ) #TODO: template name
#
# def profile_view(request):
#     user = request.user
#     return redirect(request, 'user.profile' ) #TODO: template name
#
#
