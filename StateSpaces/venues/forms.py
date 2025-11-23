from django import forms
from .models import Building, Venue, Amenity, AmenityAssignment

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ["building_name", "street", "district", "city"]


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['venue_name', 'building_floor', 'venue_type', 'venue_capacity', 'venue_floor_area', 'under_renovation', 'building']


class AmenityForm():
    class Meta:
        model = Amenity
        fields = ['amenity_type', 'description']


class AmenityAssignmentForm():
    class Meta:
        model = AmenityAssignment
        fields = ['amenity', 'venue', 'quantity']
