from django.db import models
from django.urls import reverse

# Create your models here.
class Building(models.Model):
    building_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    
    def __str__(self):
        return self.building_name

class Amenity(models.Model):
    amenity_type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Venue(models.Model):
    venue_name = models.CharField(max_length=255)
    building_floor = models.IntegerField()
    venue_type = models.CharField(max_length=255)
    venue_capacity = models.IntegerField()
    venue_floor_area = models.IntegerField()
    under_renovation = models.BooleanField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='venues')

    def __str__(self):
        return self.venue_name
    
    def get_absolute_url(self):
        return reverse('venues:venues-detail', args=[str(self.pk)])


class AmenityAssignment(models.Model):
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('amenity', 'venue')