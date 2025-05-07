
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# ====================
# Custom User Model
# ====================
class User(AbstractUser):
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

# ====================
# Buyer Profile (optional)
# ====================
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# ====================
# Seller Profile
# ====================
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seller_type = models.CharField(max_length=50)  # 'individual' or 'agency'
    address = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    bio = models.TextField(blank=True)



# ====================
# Purchase Offer
# ====================


