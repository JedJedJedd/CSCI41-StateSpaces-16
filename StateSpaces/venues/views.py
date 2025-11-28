from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.detail import DetailView
from .models import Venue
from .forms import VenueForm

# Create your views here.
class VenuesListView(ListView):
     model = Venue
     template_name = 'venues/venues_list.html'

class VenuesSearchListView(ListView):
     model = Venue
     template_name = 'venues/search_venues.html'     