from django import forms
from .models import Building, Venue, Amenity, AmenityAssignment

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ["building_name", "street", "city"]


class VenueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for amenity in Amenity.objects.all():
            field_name = f"amenity_{amenity.id}"
            qty_field_name = f"amenity_qty_{amenity.id}"
            self.fields[field_name] = forms.BooleanField(required=False, label=amenity.amenity_type)
            self.fields[qty_field_name] = forms.IntegerField(required=False, min_value=1, initial=1, label="Quantity")

    #amenity = forms.ModelChoiceField(queryset=Amenity.objects.all(), required=False, label="Amenity")
    #amenity_quantity = forms.IntegerField(required=False, min_value=1, label="Amenity quantity")

    other_amenity = forms.CharField(max_length=255, required=False, label="Other optional amenity")
    other_quantity = forms.IntegerField(required=False, min_value= 1, label="Other amenity quantity")

    class Meta:
        model = Venue
        fields = ['venue_name', 'building_floor', 'venue_type', 'venue_capacity', 'venue_floor_area', 'under_renovation', 'building']

    def save(self, commit=True):
        venue = super().save(commit=commit)

        for amenity in Amenity.objects.all():
            checked = self.cleaned_data.get(f"amenity_{amenity.id}")
            qty = self.cleaned_data.get(f"amenity_qty_{amenity.id}") or 1
            if checked:
                AmenityAssignment.objects.create(venue=venue, amenity=amenity, quantity=qty,)

        other_name = self.cleaned_data.get("other_amenity")
        other_qty = self.cleaned_data.get("other_quantity")

        if other_name and other_qty:
            new_amenity = Amenity.objects.create(amenity_type=other_name, description=other_name)
            AmenityAssignment.objects.create(venue=venue, amenity=new_amenity, quantity=other_qty)

        return venue



class AmenityForm(forms.ModelForm):
    class Meta:
        model = Amenity
        fields = ['amenity_type', 'description']


class AmenityAssignmentForm(forms.ModelForm):
    class Meta:
        model = AmenityAssignment
        fields = ['amenity', 'venue', 'quantity']
