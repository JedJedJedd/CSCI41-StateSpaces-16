from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from venues.models import Building
# Create your models here.
class Team(models.Model):                                                       
    name = models.CharField(max_length=100)
    team_assignment = models.TextField()

    def __str__(self):
        return self.name

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    customer_name = models.CharField(max_length=100, default="Unknown")
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(default="unknown")
    username = models.CharField(max_length=100, default="Username")

    def __str__(self):
        return self.customer_name
    
    def get_profile_url(self):
        return reverse('accounts:profile', kwargs={'username': self.user.username})
    
class AgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agent_profile')
    agent_name = models.CharField(max_length=100, default='Unknown')
    contact_number = models.CharField(max_length=30,default="09991234567")
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    building = models.ForeignKey("venues.Building", on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default="Username")
    template_name = 'accounts/customer_profile.html' 

    def get_profile_url(self):
        return reverse('accounts:agent-profile', kwargs={'username': self.user.username})

    def __str__(self):
        return self.agent_name