from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Venue
# Create your views here.
class VenuesListView(ListView):
     model = Venue
     template_name = 'venues/venues_list.html'

class VenuesSearchListView(ListView):
     model = Venue
     template_name = 'venues/search_venues.html'

class VenuesDetailView(DetailView):
     model = Venue
     template_name = 'venues/venue_detail.html'
