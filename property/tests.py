from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from account.models import Buyer
from property.models import Property, PurchaseOffer

def run():
    User = get_user_model()

    user, _ = User.objects.get_or_create(username="testbuyer", email="test@example.com", role="buyer")
    user.set_password("test123")
    user.save()

    buyer, _ = Buyer.objects.get_or_create(user=user)

    property, _ = Property.objects.get_or_create(
        propertyName="Test Home",
        propDescription="Temporary testing property",
        propertyType="House",
        propListingPrice=99999999,
        propListingDate="2024-05-01",
        propIsSold=False,
        propBedrooms=3,
        propBathrooms=2,
        propSquareMeters=123.4
    )

    offer, _ = PurchaseOffer.objects.get_or_create(
        buyerId=buyer,
        propertyId=property,
        offerPrice=95000000,
        dateExpires="2024-06-01",
        offerStatus="Accepted"
    )

    print("Test user:", user.username)
    print("Test property:", property.propertyName)
    print("Test offer:", offer.offerPrice)
