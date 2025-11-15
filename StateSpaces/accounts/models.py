from django.db import models
from django.contrib.auth.models import User
from venues.models import Building
# Create your models here.
class Team(models.Model):                                                       
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.get_full_name()} (Customer)"
    
class AgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} (Agent)"