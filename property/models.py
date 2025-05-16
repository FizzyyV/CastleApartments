#from winreg import EnumKey

from django.db import models

#import account.models
#from account.models import Seller


# Create your models here.
class Address(models.Model):
    street_name = models.CharField(max_length=100)
    house_number = models.IntegerField()
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street_name} {self.house_number} {self.city} {self.postal_code}"

class Property(models.Model):
    class Meta:
        verbose_name_plural = "Properties"
    propertyName = models.CharField(max_length=100)
    propAddress = models.ForeignKey(Address, on_delete=models.CASCADE)
    propDescription = models.TextField()
    propertyType = models.CharField(max_length=100)
    propListingPrice = models.FloatField()
    propListingDate = models.DateField()
    propThumbnail = models.ImageField(upload_to="property/thumbnail", null=True, blank=True)
    propIsSold = models.BooleanField()
    propBedrooms = models.IntegerField()
    propBathrooms = models.IntegerField()
    propSquareMeters = models.FloatField()
    built = models.IntegerField(null=True, blank=True)
    sellerId = models.ForeignKey("account.Seller", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.propertyName}"

class PropertyImages(models.Model):
    """store multiple images for detail page"""
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="property/images", null=True, blank=True)

### OFFER CLASSES ###

class PurchaseOffer(models.Model):
    buyerId = models.ForeignKey("account.Buyer", on_delete=models.SET_NULL, null=True)
    propertyId = models.ForeignKey("Property", on_delete=models.SET_NULL, null=True)
    sellerId = models.ForeignKey("account.Seller", on_delete=models.SET_NULL, null=True)
    dateSubmitted = models.DateField(auto_now_add=True)
    dateExpires = models.DateField()
    offerPrice = models.FloatField()
    OFFER_STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Contingent', 'Contingent')
    )
    offerStatus = models.CharField(max_length=20, choices=OFFER_STATUS, default='Pending')

class FinalizedOffer(models.Model):
    offerId = models.OneToOneField("PurchaseOffer", on_delete=models.SET_NULL, null=True)
    phoneNumber = models.CharField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    nationalId = models.IntegerField()
    PAYMENT_METHOD = (
        ('Credit Card', 'Credit Card'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Mortgage', 'Mortgage')
    )
    paymentMethod = models.CharField(max_length=20, choices=PAYMENT_METHOD)
    paymentDetails = models.TextField(null=True, blank=True)
