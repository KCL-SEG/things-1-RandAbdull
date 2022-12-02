from django.contrib import admin
from .models import Thing

@admin.register(Thing)
class UserAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for users."""

    list_display = [
        'name', 'description', 'quantity',
    ]