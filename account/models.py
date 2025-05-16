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
#--------------------
# from django.contrib.auth.models import User
#
# from django.contrib.auth.models import User
# from django.db import models
#
#
# from property.models import Address
# class ProfileManager(models.Manager):
#     pass  # add custom queryset methods here if needed
#
#
# class Buyer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"Buyer: {self.user.username}"
#
# class Profile(models.Model):
#     #objects = None
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#
#     profile_image = models.TextField(max_length=9999)
#     objects = ProfileManager()  # ✅ Valid custom manager
#
#
# class Seller(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     seller_type = models.CharField(max_length=50, default='individual')  # Add default here
#     seller_Address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
#     logo = models.ImageField(upload_to='logos/', blank=True, null=True)
#     cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
#     bio = models.TextField(blank=True)
#     def __str__(self):
#         return f"{self.user.username}"  # ✅ Use self.user, NOT Seller.user
#


# from django.db import models
#
#
# class User(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=150, blank=True)
#     email = models.EmailField(max_length=254, blank=True)
#     password = models.CharField(max_length=128)
#
#     # Add any other fields you need, such as profile info or permissions
#
#     def __str__(self):
#         return self.username
#
#
# # account/models.py
# from django.db import models
# from django.contrib.auth import get_user_model
#
#
# class Buyer(models.Model):
#     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
#
#     # Add any additional fields for Buyer model
#
#     def __str__(self):
#         return f"Buyer: {self.user.username}"


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
    objects = ProfileManager()

    def __str__(self):
        return f"Profile: {self.user.username}"
