from django import forms

from .models import Building, Venue, Amenity, AmenityAssignment

class BuildingForm(forms.ModelForm):
    """Form for creating/editing Building instances."""

    class Meta:
        model = Building
        fields = ["building_name", "district", "street", "city"]


class VenueForm(forms.ModelForm):
    """Form for creating/editing Venue instances with dynamic amenity fields.
    
    Dynamically generates checkbox and quantity fields for each Amenity
    Dynamically generates "other amenity fields"
    """

    def __init__(self, *args, **kwargs):
        """Dynamically add BooleanField and IntegerField for each Amenity."""
        super().__init__(*args, **kwargs)
        for amenity in Amenity.objects.all():
            field_name = f"amenity_{amenity.id}"
            qty_field_name = f"amenity_qty_{amenity.id}"
            self.fields[field_name] = forms.BooleanField(
                required=False, 
                label=amenity.amenity_type
            )
            self.fields[qty_field_name] = forms.IntegerField(
                required=False, 
                min_value=1, 
                initial=1, 
                label=f"{amenity.amenity_type} Quantity"
            )

    other_amenity = forms.CharField(max_length=255, required=False, label="Other optional amenity")
    other_quantity = forms.IntegerField(required=False, min_value= 1, label="Other amenity quantity")

    class Meta:
        model = Venue
        fields = ['venue_name', 'building_floor', 'venue_type', 'venue_capacity', 'venue_floor_area', 'under_renovation', 'building']
        widgets = {
            'venue_name': forms.TextInput(attrs={
                'style': 'background-color:#F4EFE6;'
            }),
            'building_floor': forms.TextInput(attrs={
                'type': "number",
                'style': 'background-color:#F4EFE6;'
            }),
            'venue_type': forms.Select(attrs={
                'style': 'background-color:#F4EFE6;'
            }),
            'venue_capacity': forms.TextInput(attrs={
                'type': "number",
                'style': 'background-color:#F4EFE6;'
            }),
            'venue_floor_area': forms.TextInput(attrs={
                'type': "number",
                'style': 'background-color:#F4EFE6;'
            }),
            'building': forms.Select(attrs={
                'style': 'background-color:#F4EFE6;'
            }),

        }

    def save(self, commit=True):
        """Saves the Venue and creates related AmenityAssignment records.

        Creates AmenityAssignment for each checked amenity.
        """
        venue = super().save(commit=commit)

        # Creates AmenityAssignment records for checked amenities.
        for amenity in Amenity.objects.all():
            checked = self.cleaned_data.get(f"amenity_{amenity.id}")
            qty = self.cleaned_data.get(f"amenity_qty_{amenity.id}") or 1
            if checked:
                AmenityAssignment.objects.create(
                    venue=venue, 
                    amenity=amenity, 
                    quantity=qty,
                )

        # Handles other amenities and creates new Amenity if provided
        other_name = self.cleaned_data.get("other_amenity")
        other_qty = self.cleaned_data.get("other_quantity")

        if other_name and other_qty:
            new_amenity = Amenity.objects.create(
                amenity_type=other_name, 
                description=other_name
            )
            AmenityAssignment.objects.create(
                venue=venue, 
                amenity=new_amenity, 
                quantity=other_qty
            )

        return venue