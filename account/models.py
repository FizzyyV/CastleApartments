#
# # Create your models here.
# from django.contrib.auth.models import AbstractUser
# from property.models import Property, Address
# from django.db import models
#
# # ====================
# # Custom User Model
# # ====================
# class User(AbstractUser):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
#     ROLE_CHOICES = (
#         ('buyer', 'Buyer'),
#         ('seller', 'Seller'),
#     )
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES)
#     profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#
#
# # ====================
# # Buyer Profile
# # ====================
# class Buyer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     #TODO: add purchase offers as attribute?
#     def __str__(self):
#         return f"{Buyer.user.name}"
# # ====================
# # Seller Profile
# # ====================
# class Seller(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     seller_type = models.CharField(max_length=50)  # 'individual' or 'agency'
#     seller_Address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
#     logo = models.ImageField(upload_to='logos/', blank=True, null=True)
#     cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
#     bio = models.TextField(blank=True)
#     def __str__(self):
#         return f"{Seller.user.name}"
#
#-----------------------------------------------------------------------------------
#
# # Create your models here.
# from django.contrib.auth.models import AbstractUser, Group, Permission
# from property.models import Property, Address
# from django.db import models
#
#
# # ====================
# # Custom User Model
# # ====================
# class User(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     #email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
#     email = models.EmailField(max_length=255, unique=True)
#
#     ROLE_CHOICES = (
#         ('buyer', 'Buyer'),
#         ('seller', 'Seller'),
#     )
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES)
#     profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     REQUIRED_FIELDS = ['email']  # Manually define required fields
#     USERNAME_FIELD = ['name']
#
#     # ✅ Add these if not inherited (should be via AbstractUser, but double-check)
#     groups = models.ManyToManyField(
#         Group,
#         related_name='custom_user_set',
#         blank=True,
#         help_text='The groups this user belongs to.'
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='custom_user_set',
#         blank=True,
#         help_text='Specific permissions for this user.'
#     )
# # ====================
# # Buyer Profile
# # ====================
# class Buyer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     #TODO: add purchase offers as attribute?
#     def __str__(self):
#         return f"{Buyer.user.name}"
# # ====================
# # Seller Profile
# # ====================
#import uuid

from django.contrib.auth.models import User
from django.db import models

from property.models import Address


class Profile(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    profile_image = models.TextField(max_length= 9999)

class Buyer(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seller_type = models.CharField(max_length=50, default='individual')  # Add default here
    seller_Address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    bio = models.TextField(blank=True)
    def __str__(self):
        return f"{self.user.username}"  # ✅ Use self.user, NOT Seller.user

