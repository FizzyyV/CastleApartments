from django.contrib import admin

# Register your models here.
from .models import Property, Address
admin.site.register(Property)
admin.site.register(Address)

