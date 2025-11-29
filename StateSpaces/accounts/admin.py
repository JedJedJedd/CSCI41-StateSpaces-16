"""
Admin configuration for user-related models.

Customizes Django admin interface for CustomerProfile, AgentProfile, UserAdmin, TeamAdmin
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import CustomerProfile , AgentProfile, Team

class CustomerProfileInline(admin.StackedInline):
    """Inline admin for customer profile"""

    model = CustomerProfile
    can_delete = False

class AgentProfileInline(admin.StackedInline):
    """Inline admin for agent profile"""

    model = AgentProfile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    """Extends default User admin with customer and agent profiles."""

    inlines = [CustomerProfileInline, AgentProfileInline]

class TeamAdmin(admin.ModelAdmin):
    """Admin configuration to manage teams."""
    
    list_display = ('name', 'team_assignment')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)
