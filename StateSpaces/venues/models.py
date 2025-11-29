from django.db import models
from django.urls import reverse


class Building(models.Model):
    """Model representing a building."""

    building_name = models.CharField(max_length=255, default="Unknown Building")
    district = models.CharField(max_length=255, default="Unknown District")
    street = models.CharField(max_length=255, default="Unknown Street")
    city = models.CharField(max_length=255, default="Unknown City")
    
    def __str__(self):
        return self.building_name

class Amenity(models.Model):
    """Model representing an amenity in venues."""

    amenity_type = models.CharField(max_length=255, default="unknown")
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.amenity_type
    
class Venue(models.Model):
    """Model representing a venue inside of a building.
    
    Includes its type, capacity, floor area, renovation status, and linked agent.
    """

    VENUE_TYPE_CHOICES = [
        ('Conference', 'Conference'),
        ('Function Hall', 'Function Hall'),
        ('Banquet Hall', 'Banquet Hall'),
        ('Auditorium', 'Auditorium'),
        ('Study Room', 'Study Room'),
        ('Computer Workstations', 'Computer Workstations'),
        ('Meeting room', 'Meeting room'),
        ('Pantry', 'Pantry'),
        ('Others', 'Others'),
    ]

    YES_NO_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    venue_name = models.CharField(max_length=255, default="Unknown")
    building_floor = models.IntegerField(default=1)
    venue_type = models.CharField(max_length=50, choices=VENUE_TYPE_CHOICES, default='Study Room')
    venue_capacity = models.PositiveIntegerField(default=1)
    venue_floor_area = models.PositiveIntegerField(default=1)
    under_renovation = models.BooleanField(default=False)
    building = models.ForeignKey(
        Building, on_delete=models.RESTRICT, related_name='venues'
    )
    agent = models.ForeignKey(
        "accounts.AgentProfile", on_delete=models.RESTRICT, related_name='venues'
    )

    def __str__(self):
        return self.venue_name
    
    def get_absolute_url(self):
        """Return the URL to the venue's detail page."""
        return reverse('venues:venues-detail', args=[str(self.pk)])

class AmenityAssignment(models.Model):
    """Model representing the assignment of amenities to venues, including quantity.
    
    Allows each venue venue and amenity pair to be unique
    """
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('amenity', 'venue')

    def __str__(self):
        return f"{self.amenity.amenity_type} @ {self.venue.venue_name} (x{self.quantity})"