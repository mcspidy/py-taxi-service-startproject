from django.contrib import admin
from taxi.models import Manufacturer, Driver, Car
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Manufacturer)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    manufacturer = ["manufacturer"]
    model = ["model"]


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    driver_data = ["username", "first_name", "last_name", "license_number"]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("license_number",)}),
    )
