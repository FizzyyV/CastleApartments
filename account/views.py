# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
#
#
# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'account/signup.html', {
#             'form': UserCreationForm(),
#         })
#
#
#
#
#
#





from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
# from account.models import Buyer  # Ensure Buyer is imported
#
# def my_view(request):
#     from account.models import Buyer  # Move the import here to avoid circular import
#     # rest of the view code...python manage.py makemigrations
#
# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             # Save the user
#             user = form.save()
#
#             # After saving the user, create the Buyer object for this user
#             print(f"user: {user}, id: {user.id}")
#
#             Buyer.objects.create(user=user)
#
#             # Redirect to login after successful signup
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#
#     # Pass the correct form to the template
#     return render(request, 'account/signup.html', {'form': form})
#----------------------------------------------------------------------------------------------
#
# import profile
#
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
#
#
# import account
# from .forms import profile_form
# from .forms.profile_form import ProfileForm
# #from .models import User, Profile
# # Create your views here.
#
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
#
# # account/views.py
# from django.contrib.auth.forms import AuthenticationForm
# from django.shortcuts import render
# from django.contrib.auth import login
#
# from django.contrib.auth.decorators import login_required
#
# #login_required
# def profile_view(request):
#     user_profile = Profile.objects.filter(user=request.user).first()
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST,  instance=user_profile)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.user = request.user
#             instance.save()
#             return redirect('profile')
#     return render(request, 'account/profile.html', {
#         'form' : ProfileForm(instance=profile),
#     })
#
# def custom_login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('property-index')  # After login, redirect to the home page
#     else:
#         form = AuthenticationForm()
#
#     return render(request, 'registration/login_pretty.html', {'form': form})
# #
# def custom_signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request,'registration/signup.html', {'form': form})

#----------------------------------------------------------------------------------------------
























# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"
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




from django.shortcuts import render, redirect
from account.forms.profile_form import CustomUserCreationForm
from account.models import Buyer

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

            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'account/signup.html', {'form': form})