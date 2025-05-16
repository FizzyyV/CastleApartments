
from django.db import models
from django.contrib.auth.models import AbstractUser
from property.models import Address


# ====================
# Custom User Model
# ====================
class User(AbstractUser):
    # Use email as the unique identifier
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username


# ====================
# Buyer Profile
# ====================
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Buyer: {self.user.username}"


# ====================
# Seller Profile
# ====================
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seller_type = models.CharField(max_length=50, default='individual')  # 'individual' or 'agency'
    seller_Address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Seller: {self.user.username}"


# ====================
# Optional Profile Model (if needed)
# ====================
class ProfileManager(models.Manager):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.TextField(max_length=9999)
    #profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    objects = ProfileManager()

    def __str__(self):
        return f"Profile: {self.user.username}"
