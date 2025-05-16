from django.forms import ModelForm
from django import forms

from property.models import FinalizedOffer, Address


class FinalizeOfferForm(ModelForm):
    #extra input fields for payment
    cardholder = forms.CharField(required=False)
    card_number = forms.CharField(required=False)
    card_expiry = forms.CharField(required=False)
    card_cvc = forms.CharField(required=False)

    bank_name = forms.CharField(required=False)
    account_number = forms.CharField(required=False)

    mortgage_lender = forms.CharField(required=False)
    agreement_ref = forms.CharField(required=False)

    street_name = forms.CharField()
    city = forms.CharField()
    postal_code = forms.CharField()

    class Meta:
        model = FinalizedOffer
        exclude = ['offerId', 'paymentDetails', 'address']
        widgets = {
        'phoneNumber': forms.TextInput(attrs={'class': 'form-control'}),
        'nationalId': forms.NumberInput(attrs={'class': 'form-control'}),
        'paymentMethod': forms.Select(attrs={'class': 'form-control'}),

        }

    def save(self, commit=True):
        obj = super().save(commit=False)
        # 1. Save address from form fields
        address = Address.objects.create(
            street_name=self.cleaned_data['street_name'],
            house_number=0,  # You can add a field for this if needed
            city=self.cleaned_data['city'],
            postal_code=self.cleaned_data['postal_code'],
            country=self.cleaned_data['country']
        )
        obj.address = address
        # build payment details string
        method = self.cleaned_data.get('paymentMethod')

        if method == 'Credit Card':
            details = (
                f"Cardholder: {self.cleaned_data['cardholder']}\n"
                f"Card Number: {self.cleaned_data['card_number']}\n"
                f"Expiry: {self.cleaned_data['card_expiry']}\n"
                f"CVC: {self.cleaned_data['card_cvc']}"
            )
        elif method == 'Bank Transfer':
            details = (
                f"Bank Name: {self.cleaned_data['bank_name']}\n"
                f"Account Number: {self.cleaned_data['account_number']}"
            )
        elif method == 'Mortgage':
            details = (
                f"Lender: {self.cleaned_data['mortgage_lender']}\n"
                f"Agreement Ref: {self.cleaned_data['agreement_ref']}"
            )
        else:
            details = "Unknown method"

        obj.paymentDetails = details
        if commit:
            obj.save()
        return obj