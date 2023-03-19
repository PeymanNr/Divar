from django.contrib import admin
from category.models import Category
from django.contrib.admin import register


@register(Category)
class AdminCategory(admin.ModelAdmin):
    fields = ('name', 'parent', 'slug')
    list_display = ('name', 'parent')
    list_display_links = ('name', 'parent')