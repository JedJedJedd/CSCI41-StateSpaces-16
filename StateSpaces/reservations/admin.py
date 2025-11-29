from django.contrib import admin
from .models import Reservation

class ReservationInline(admin.TabularInline):
    """Inline admin for reservations."""

    model = Reservation

admin.site.register(Reservation)