from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_id', 'number_of_participants', 'reservation_start_time', 'reservation_start_date', 'reservation_end_time', 'reservation_end_date', 'agent_id', 'venue']