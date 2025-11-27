from django.contrib import admin
from .models import Venue, Building


class VenueInline(admin.TabularInline):
    model = Venue



class BuildingAdmin(admin.ModelAdmin):
    inlines = [VenueInline]



admin.site.register(Building, BuildingAdmin)
admin.site.register(Venue)