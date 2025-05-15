from django.contrib.auth import forms
from django.forms import ModelForm
from django import forms

from account.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'id']
        widgets = {
            'profile_image' :forms.TextInput(attrs={'class':'form-control'}),
        }

