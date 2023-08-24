from django.contrib import admin
from .models import Location


@admin.register(Location)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['title']
