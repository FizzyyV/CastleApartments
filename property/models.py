from django.db import models

# Create your models here.
class Address(models.Model):
    street_name = models.CharField(max_length=100)
    house_number = models.IntegerField()
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)

class Property(models.Model):
    propertyId = models.IntegerField()
    propertyName = models.CharField(max_length=100)
    propAddress = models.ForeignKey(Address, on_delete=models.CASCADE)
    propDescription = models.TextField()
    propertyType = models.CharField(max_length=100)
    propListingPrice = models.FloatField()
    propListingDate = models.DateField()
    propThumbnail = models.ImageField()
    propImages = models.ImageField()
    propIsSold = models.BooleanField()
    propBedrooms = models.IntegerField()
    propBathrooms = models.IntegerField()
    propSquareMeters = models.FloatField()
    sellerId = models.ForeignKey() #TODO: add seller id as foreign key

