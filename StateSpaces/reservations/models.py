from django.db import models
from venues.models import Venue
from datetime import datetime, date, timedelta
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Reservation(models.Model):
    customer = models.ForeignKey("accounts.CustomerProfile", on_delete=models.RESTRICT)
    number_of_participants = models.IntegerField(default=1)
    reservation_start_time = models.TimeField(default=timezone.localtime())
    reservation_start_date = models.DateField(default=timezone.now())
    reservation_end_time = models.TimeField(default=timezone.localtime())
    reservation_end_date = models.DateField(default=timezone.now() + timedelta(days=1))
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='reservations')

    def start_datetime(self):
        return datetime.combine(self.reservation_start_date, self.reservation_start_time)

    def end_datetime(self):
        return datetime.combine(self.reservation_end_date, self.reservation_end_time)

    #https://www.w3schools.com/django/ref_lookups_lte.php
    #https://docs.djangoproject.com/en/5.2/ref/forms/validation/
    #https://stackoverflow.com/questions/68418311/why-we-use-args-and-kwargs-in-super-save
    def clean(self):
        super().clean()
        errors = []

        if self.number_of_participants > self.venue.venue_capacity:
            errors.append(
                f"Selected participant count exceeds venue's max capacity of {self.venue.venue_capacity} people."
            )
        
        if self.venue.under_renovation:
            errors.append(
                "The venue you are trying to reserve is under renovation. Select a different venue."
            )
            

        new_start = self.start_datetime()
        new_end = self.end_datetime()

        conflicts = Reservation.objects.filter(venue=self.venue).exclude(id=self.id).filter(
            reservation_start_date__lte=self.reservation_end_date,
            reservation_end_date__gte=self.reservation_start_date,
        )

        conflicts = [ 
            timeslot for timeslot in conflicts
            if timeslot.start_datetime() < new_end and timeslot.end_datetime() > new_start
        ]

        if conflicts:
            errors.append(
                "This time slot conflicts with an existing reservation."
            )
        
        if errors:
            raise ValidationError(errors)


    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        


