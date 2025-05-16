from django.contrib.auth.models import User
from django.db import models

# ====================
# Buyer Profile
# ====================
class Profile(models.Model):
    '''default user profile, buyers'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField()

# ====================
# Seller Profile
# ====================
class Seller(models.Model):
    '''not an actual user, but has a profile to view'''
    name = models.CharField(max_length=100)
    email = models.EmailField()
    seller_type = models.CharField(max_length=50)  # 'individual' or 'agency'
    seller_Address = models.ForeignKey("property.Address", on_delete=models.SET_NULL, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    bio = models.TextField(blank=True)
    def __str__(self):
        return f"{self.name}"


