from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

import account
from .models import User
# Create your views here.

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request, username):
        profile_user = get_object_or_404(User, username=username)
        return render(request, "registration/profile.html", {
            "profile_user": profile_user
        })





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
