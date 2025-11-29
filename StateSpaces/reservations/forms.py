from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'venue',
            'number_of_participants',
            'reservation_start_time',
            'reservation_start_date',
            'reservation_end_time',
            'reservation_end_date',
        ]
        widgets = {
            'reservation_start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control border border-dark border-1',
                'style': 'background-color:#F4EFE6;'
            }),
            'reservation_end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control border border-dark border-1',
                'style': 'background-color:#F4EFE6;'
            }),
            'reservation_start_time': forms.TimeInput(format='%H:%M', attrs={
                'type': 'time',
                'class': 'form-control border border-dark border-1',
                'style': 'background-color:#F4EFE6;'
            }),
            'reservation_end_time': forms.TimeInput(format='%H:%M', attrs={
                'type': 'time', 
                'class': 'form-control border border-dark border-1',
                'style': 'background-color:#F4EFE6;'
            }),
            'number_of_participants': forms.NumberInput(attrs={
                'class': 'form-control border border-dark border-1',
                'min': 1,
                'style': 'background-color:#F4EFE6;'
            }),
            'venue': forms.Select(attrs={
                'class': 'form-select border border-dark border-1',
                'style': 'background-color:#F4EFE6;'
            }),
        }
