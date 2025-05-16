from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from account.forms.profile_form import CustomUserCreationForm, ProfileForm
from account.models import Buyer, Profile
from django.core.exceptions import ObjectDoesNotExist


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"user: {user}, id: {user.id}")

            if user.role == 'buyer':
                Buyer.objects.create(user=user)
            elif user.role == 'seller':
                pass  # Optional: Create Seller.objects.create(user=user)
            Profile.objects.create(user=user, profile_image='')  # Use default image or logic


            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'account/signup.html', {'form': form})

def profile(request):
    try:
        account_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Create one if it doesn’t exist, or redirect to a profile creation form
        account_profile = Profile.objects.create(user=request.user,profile_image='')  # adjust default image logic as needed
    #account_profile = Profile.objects.get(user=request.user).first()
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=account_profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=account_profile)

    return render(request, 'account/profile.html', {
        'form': ProfileForm(instance=account_profile),
    })

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('property-index')  # Or whatever page you want
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login_pretty.html', {'form': form})



