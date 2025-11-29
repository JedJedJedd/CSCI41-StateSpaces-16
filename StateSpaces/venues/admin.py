"""
Admin configuration for venues, buildings, and amenities.

BuildingAdmin - Custom admin for managing buildings and their related venues.
VenueInline - Inline admin to display venues within a building.
AmenityAssignmentInline - Inline admin to display amenity assignments for a venue.
"""

from django.contrib import admin

from .models import Venue, Building, AmenityAssignment, Amenity


class VenueInline(admin.TabularInline):
    """Inline admin for venues belonging to a building."""

    model = Venue

class AmenityAssignmentInline(admin.TabularInline):
    """Inline admin for amenity assignments on a venue."""
    
    model = AmenityAssignment

class BuildingAdmin(admin.ModelAdmin):
    """Admin for Building model."""

    inlines = [VenueInline]

admin.site.register(Building, BuildingAdmin)
admin.site.register(Venue)
admin.site.register(Amenity)
admin.site.register(AmenityAssignment)