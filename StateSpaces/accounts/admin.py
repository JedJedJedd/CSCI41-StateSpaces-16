from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import CustomerProfile , AgentProfile, Team

class CustomerProfileInline(admin.StackedInline):
    model = CustomerProfile
    can_delete = False

class AgentProfileInline(admin.StackedInline):
    model = AgentProfile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [CustomerProfileInline, AgentProfileInline]

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'team_assignment')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)
