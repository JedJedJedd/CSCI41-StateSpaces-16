from django.contrib import admin
from .models import Reservation


class ReservationInline(admin.TabularInline):
    model = Reservation


class ReservationAdmin(admin.ModelAdmin):
    inlines = [ReservationInline]



admin.site.register(Reservation, ReservationAdmin)
