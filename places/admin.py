from django.contrib import admin
from .models import Location, Picture


@admin.register(Location)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Picture)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['number', 'location']
