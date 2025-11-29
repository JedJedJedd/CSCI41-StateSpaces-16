"""
Models for managing venue reservations.

Reservation - Represents a booking made by a customer at a venue.
Includes validation for venue capacity, renovation status, and time conflicts.
"""

from datetime import datetime, date, timedelta
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from venues.models import Venue


class Reservation(models.Model):
    """Represents a venue reservation made by a customer.

    Includes validation for capacity, renovation status, and time conflicts.
    """

    customer = models.ForeignKey("accounts.CustomerProfile", on_delete=models.RESTRICT)
    number_of_participants = models.IntegerField(default=1)
    reservation_start_time = models.TimeField(default=timezone.localtime())
    reservation_start_date = models.DateField(default=timezone.now())
    reservation_end_time = models.TimeField(default=timezone.localtime())
    reservation_end_date = models.DateField(
        default=timezone.now() + timedelta(days=1)
    )
    venue = models.ForeignKey(
        Venue, 
        on_delete=models.CASCADE, 
        related_name='reservations'
    )

    def start_datetime(self):
        """Combines start date/time into a single object"""
        return datetime.combine(
            self.reservation_start_date, self.reservation_start_time
        )

    def end_datetime(self):
        """Combines end date/time into a single object"""
        return datetime.combine(
            self.reservation_end_date, self.reservation_end_time
        )

    def clean(self):
        """Validates the reservation before saving.
        
        Checks participant count, venue, time conflicts.
        """
        super().clean()
        errors = []

        # Check if participant count exceeds venue capacity
        if self.number_of_participants > self.venue.venue_capacity:
            errors.append(
                f"Selected participant count exceeds venue's max capacity of {self.venue.venue_capacity} people."
            )
        
        # Prevent booking venues that are under renovation
        if self.venue.under_renovation:
            errors.append(
                "The venue you are trying to reserve is under renovation. Select a different venue."
            )
            
        # Check for time conflicts with other reservations
        new_start = self.start_datetime()
        new_end = self.end_datetime()

        # Filter conflicts by checking for overlaps
        conflicts = (
            Reservation.objects.filter(venue=self.venue)
            .exclude(id=self.id).
            filter(
                reservation_start_date__lte=self.reservation_end_date,
                reservation_end_date__gte=self.reservation_start_date,
            )
        )

        conflicts = [ 
            timeslot for timeslot in conflicts
            if timeslot.start_datetime() < new_end and timeslot.end_datetime() > new_start
        ]

        if conflicts:
            errors.append(
                "This time slot conflicts with an existing reservation."
            )
        
        if new_start >= new_end:
            raise ValidationError("The reservation end date/time must be after the start date/time.")
        
        if errors:
            raise ValidationError(errors)


    def save(self, *args, **kwargs):
        """Override save to enforce validation,"""
        self.clean()
        super().save(*args, **kwargs)
        


