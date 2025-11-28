from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import CustomerProfile , AgentProfile, Team
from .models import Building, Venue

class CustomerProfileInline(admin.StackedInline):
    model = CustomerProfile
    can_delete = False
    #verbose_name_plural = 'Customer Profiles'

class AgentProfileInline(admin.StackedInline):
    model = AgentProfile
    can_delete = False
    #verbose_name_plural = 'Agent Profiles'

class UserAdmin(BaseUserAdmin):
    inlines = [CustomerProfileInline, AgentProfileInline]

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'team_assignment')

class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_name', 'building', 'agent', 'floor', 'venue_type', 'venue_capacity', 'under_renovation')
    list_filter = ('building', 'agent', 'venue_type', 'under_renovation')
    search_fields = ('venue_name', 'building__building_name', 'agent__agent_name')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Building)
admin.site.register(Venue, VenueAdmin)


# Register your models here.
