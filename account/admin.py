from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserAdmin
from .models import User, Buyer, Seller

admin.site.register(Buyer)
admin.site.register(Seller)