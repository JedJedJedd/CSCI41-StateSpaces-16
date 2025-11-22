from django.db import models
from django.contrib.auth.models import User
from venues.models import Building
# Create your models here.
class Team(models.Model):                                                       
    name = models.CharField(max_length=100)
    #team_id = 
    #employee_id = 
    team_assignement = models.TextField()

    def __str__(self):
        return self.name

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #customer_id = 
    customer_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()
    username = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.get_full_name()} (Customer)"
    
class AgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #agent_id = 
    agent_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.PROTECT) #prevents teams deletion if there are still members assigned
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()
    username = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.get_full_name()} (Agent)"