from django.contrib import admin
from django.contrib.admin import register

from locations.models import Location, State, City, Country


@register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['country', 'city', 'state']


@register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']


@register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name']


@register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']