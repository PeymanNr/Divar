from django.contrib import admin
from django.contrib.admin import register

from advertisements.models import Advertisement, AdvertisementImage


class AdvertisementImageInline(admin.TabularInline):
    model = AdvertisementImage


@register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'price']
    list_filter = ['user']
    list_display_links = ['user']
    search_fields = ['user', 'title']
    inlines = [AdvertisementImageInline, ]



