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
    propertyName = models.CharField(max_length=100)
    propAddress = models.ForeignKey(Address, on_delete=models.CASCADE)
    propDescription = models.TextField()
    propertyType = models.CharField(max_length=100)
    propListingPrice = models.FloatField()
    propListingDate = models.DateField()
    propThumbnail = models.ImageField(upload_to="property/thumbnail", null=True, blank=True)
    propImages = models.ImageField(upload_to="property/images", null=True, blank=True)
    propIsSold = models.BooleanField()
    propBedrooms = models.IntegerField()
    propBathrooms = models.IntegerField()
    propSquareMeters = models.FloatField()
    sellerId = models.ForeignKey("account.Seller", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.propertyName}"