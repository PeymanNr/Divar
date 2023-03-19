from django.contrib import admin
from django.contrib.admin import register

from advertisements.models import Advertisement


@register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'price']
