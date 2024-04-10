# toggle/admin.py

from django.contrib import admin
from .models import FeatureToggle

@admin.register(FeatureToggle)
class FeatureToggleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_enabled', 'created_by', 'created_at', 'updated_at')
    list_filter = ('is_enabled', 'created_by', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'notes', 'environment', 'created_by__username')

