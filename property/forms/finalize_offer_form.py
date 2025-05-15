from django.forms import ModelForm
from django import forms

from property.models import FinalizedOffer

class FinalizeOfferForm(ModelForm):

    class Meta:
        model = FinalizedOffer
        exclude = ['offerId']
        widgets = {
        'contactInfo': forms.TextInput(attrs={'class': 'form-control'}),
        'address': forms.TextInput(attrs={'class': 'form-control'}),
        'nationalId': forms.NumberInput(attrs={'class': 'form-control'}),
        'paymentMethod': forms.Select(attrs={'class': 'form-control'}),
        'paymentDetails': forms.Textarea(attrs={'class': 'form-control'}),

        }