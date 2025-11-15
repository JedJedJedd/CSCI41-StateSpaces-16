from django.db import models
from venues.models import Venue

# Create your models here.
class Reservation(models.Model):
    # customer_id = ill implement it later when i set up the profiles
    number_of_participants = models.IntegerField()
    reservation_start_time = models.TimeField()
    reservation_start_date = models.DateField()
    reservation_end_time = models.TimeField()
    reservation_end_date = models.DateField()
    # agent_id = ill implement this later as well
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
