from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Venue
# Create your views here.
class VenuesListView(ListView):
     model = Venue
     template_name = 'venues/venues_list.html'

class VenuesSearchListView(ListView):
     model = Venue
     template_name = 'venues/search_venues.html'     

class VenueDetailView(DetailView):
     model = Venue
     template_name = 'venues/venue_detail.html'

     def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["amenities"] = self.object.amenityassignment_set.select_related("amenity")
        return ctx
     