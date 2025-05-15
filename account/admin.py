# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User, Buyer, Seller
#
# # @admin.register(User)
# # class CustomUserAdmin(BaseUserAdmin):
# #     list_display = ('username', 'email', 'role', 'is_staff')
# #     list_filter = ('role', 'is_staff', 'is_superuser')
# #     fieldsets = BaseUserAdmin.fieldsets + (
# #         ('Custom Fields', {'fields': ('role', 'profile_image')}),
# #     )
#
#
# @admin.register(User)
# class CustomUserAdmin(BaseUserAdmin):
#     list_display = ('username', 'email', 'role', 'is_staff')
#     list_filter = ('role', 'is_staff', 'is_superuser')
#
#     fieldsets = BaseUserAdmin.fieldsets + (
#         ('Custom Fields', {'fields': ('role', 'profile_image')}),
#     )
#
#     add_fieldsets = BaseUserAdmin.add_fieldsets + (
#         ('Custom Fields', {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'role', 'profile_image', 'password1', 'password2'),
#         }),
#     )
#
# @admin.register(Buyer)
# class BuyerAdmin(admin.ModelAdmin):
#     list_display = ('user',)
#
# @admin.register(Seller)
# class SellerAdmin(admin.ModelAdmin):
#     list_display = ('user', 'seller_type', 'get_address', 'logo')
#     list_filter = ('seller_type',)
#     search_fields = ('user__username', 'bio')
#
#     def get_address(self, obj):
#         if obj.seller_Address:
#             return f"{obj.seller_Address.street_name}, {obj.seller_Address.city}"
#         return "—"
#     get_address.short_description = 'Address'
#
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User
#
