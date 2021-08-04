from django.contrib import admin

from .models import Provider, ServiceArea


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name", "currency")


@admin.register(ServiceArea)
class ServiceAreaAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name", "longitude", "latitude", "price")
