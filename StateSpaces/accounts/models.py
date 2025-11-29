from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from venues.models import Building
# Create your models here.
class Team(models.Model):                                                       
    name = models.CharField(max_length=100)
    #team_id = 
    #employee_id = 
    team_assignment = models.TextField()

    def __str__(self):
        return self.name
    
# class Venue(models.Model):
#     VENUE_TYPE_CHOICES = [
#         ('Conference', 'Conference'),
#         ('Hall', 'Hall'),
#         ('Auditorium', 'Auditorium'),
#         ('Study Room', 'Study Room')
#     ]

#     YES_NO_CHOICES = [
#         ('Y', 'Yes'),
#         ('N', 'No'),
#     ]

#     venue_name = models.CharField(max_length=255)
#     building = models.ForeignKey('Building', on_delete=models.PROTECT, related_name='venuesAgent')
#     agent = models.ForeignKey('AgentProfile', on_delete=models.SET_NULL, null=True, blank=True, related_name='venuesAgent') 
#     floor_area = models.PositiveIntegerField()  # in square meters
#     venue_type = models.CharField(max_length=50, choices=VENUE_TYPE_CHOICES)
#     venue_capacity = models.PositiveIntegerField()
#     floor = models.CharField(max_length=50)
#     under_renovation = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

#     def __str__(self):
#         return self.venue_name

#     def get_absolute_url(self):
#         return reverse('venues:venue-detail', kwargs={'pk': self.pk})

# class Building(models.Model):
#     building_id = models.AutoField(primary_key=True) 
#     building_name = models.CharField(max_length=255, default="Unknown Building")
#     street = models.CharField(max_length=255, default="Unknown Street")
#     city = models.CharField(max_length=255, default="Unknown City")
    
#     def __str__(self):
#         return self.building_name

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    customer_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name
    
    def get_profile_url(self):
        return reverse('accounts:profile', kwargs={'username': self.user.username})
    
class AgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agent_profile')
    agent_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    building = models.ForeignKey("venues.Building", on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=100)
    template_name = 'accounts/customer_profile.html' 

    def get_profile_url(self):
        return reverse('accounts:agent-profile', kwargs={'username': self.user.username})

    def __str__(self):
        return self.agent_name