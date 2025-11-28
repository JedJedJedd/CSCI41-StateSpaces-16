from django.contrib import admin
from .models import Reservation

class ReservationInline(admin.TabularInline):
    model = Reservation

admin.site.register(Reservation)