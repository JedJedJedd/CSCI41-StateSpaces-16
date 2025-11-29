from django.contrib import admin
from .models import Venue, Building, AmenityAssignment, Amenity


class VenueInline(admin.TabularInline):
    model = Venue

class AmenityAssignmentInline(admin.TabularInline):
    model = AmenityAssignment

class BuildingAdmin(admin.ModelAdmin):
    inlines = [VenueInline]

admin.site.register(Building, BuildingAdmin)
admin.site.register(Venue)
admin.site.register(Amenity)
admin.site.register(AmenityAssignment)