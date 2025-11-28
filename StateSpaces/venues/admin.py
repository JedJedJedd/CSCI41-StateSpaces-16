from django.contrib import admin
from .models import Venue, Building, AmenityAssignment


class VenueInline(admin.TabularInline):
    model = Venue

class AmenityAssignmentInline(admin.TabularInline):
    model = AmenityAssignment

class BuildingAdmin(admin.ModelAdmin):
    inlines = [VenueInline]

#class VenueAdmin(admin.ModelAdmin):
    #inlines = [AmenityAssignmentInline]

admin.site.register(Building, BuildingAdmin)
admin.site.register(Venue)
#admin.site.register(AmenityAssignment)