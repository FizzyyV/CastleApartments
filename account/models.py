
# Create your models here.
from django.contrib.auth.models import AbstractUser
from property.models import Property, Address
from django.db import models

# ====================
# Custom User Model
# ====================
class User(AbstractUser):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)


# ====================
# Buyer Profile
# ====================
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #TODO: add purchase offers as attribute?
    def __str__(self):
        return f"{Buyer.user.name}"
# ====================
# Seller Profile
# ====================
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seller_type = models.CharField(max_length=50)  # 'individual' or 'agency'
    seller_Address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    bio = models.TextField(blank=True)
    def __str__(self):
        return f"{Seller.user.name}"

