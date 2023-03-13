from django.contrib import admin
from django.contrib.admin import register

from advertisements.models import Category, Advertisement


# Register your models here.
@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'price']
