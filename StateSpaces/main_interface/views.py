from django.shortcuts import render
from django.views.generic.list import ListView
from accounts.models import CustomerProfile

# Create your views here.
class AppsListView(ListView):
     model = CustomerProfile
     template_name = 'main_interface/homepage.html'