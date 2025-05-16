from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from account.models import User, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'id']
        widgets = {
            'profile_image': forms.TextInput(attrs={'class': 'form-control'}),
        }
