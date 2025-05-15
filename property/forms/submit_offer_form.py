from django.forms import ModelForm
from django import forms

from property.models import PurchaseOffer

class SubmitOfferForm(ModelForm):
    class Meta:
        model = PurchaseOffer
        exclude = ['id', 'buyerId', 'propertyId', 'sellerId', 'dateSubmitted', 'offerStatus' ]
        widgets = {
            'offerPrice': forms.NumberInput(attrs={'class': 'form-control'}),
            'dateExpires': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }