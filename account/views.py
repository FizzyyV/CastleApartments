from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
# Create your views here.

def login_view(request):
    """handles login view"""
    user = authenticate(request, email=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('homepage') #TODO: create homepage template
    else:
        return render(request, 'login', {'error': 'invalid credentials'})
    return render(request, '' ) #TODO: template name

def logout_view(request):
    logout(request)
    return redirect('homepage')
def signup_view(request):
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    return render(request, '' ) #TODO: template name

def profile_view(request):
    user = request.user
    return redirect(request, 'user.profile' ) #TODO: template name