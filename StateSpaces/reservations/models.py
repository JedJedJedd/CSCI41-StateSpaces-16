from django.db import models
from venues.models import Venue
from datetime import datetime

# Create your models here.
class Reservation(models.Model):
    customer = models.ForeignKey("accounts.CustomerProfile", on_delete=models.RESTRICT)
    number_of_participants = models.IntegerField()
    reservation_start_time = models.TimeField()
    reservation_start_date = models.DateField()
    reservation_end_time = models.TimeField()
    reservation_end_date = models.DateField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='reservations')

    def start_datetime(self):
        return datetime.combine(self.reservation_start_date, self.reservation_start_time)

    def end_datetime(self):
        return datetime.combine(self.reservation_end_date, self.reservation_end_time)
