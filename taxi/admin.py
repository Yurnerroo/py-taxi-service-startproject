from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Driver License", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Driver License", {"fields": ("license_number",)}),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    list_filter = ["name"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    search_fields = ["model"]
    list_filter = ["manufacturer"]
