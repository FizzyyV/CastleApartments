from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from account.forms.profile_form import ProfileForm
from account.models import Profile


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('custom_login')
    else:
        return render(request, 'registration/signup.html',{
            'form': UserCreationForm()
        })

def profile(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('profile')

    return render(request, 'account/profile.html', {
        'form': ProfileForm(instance=user_profile),
    })

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('property-index')  # After login, redirect to the home page
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login_pretty.html', {'form': form})