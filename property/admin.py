from django.contrib import admin

# Register your models here.
from .models import Property, Address, PurchaseOffer

admin.site.register(Property)
admin.site.register(Address)
admin.site.register(PurchaseOffer)
