from django.contrib import admin
from .models import Venue, Building, Amenity


class VenueInline(admin.TabularInline):
    model = Venue


class BuildingInline(admin.TabularInline):
    model = Building


class AmenityInline(admin.TabularInline):
    model = Amenity


class VenueAdmin(admin.ModelAdmin):
    inlines = [BuildingInline, AmenityInline]



admin.site.register(Venue, VenueAdmin)
admin.site.register(Building)
admin.site.register(Amenity)
