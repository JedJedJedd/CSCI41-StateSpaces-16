from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Venue
from .forms import VenueForm

# Create your views here.
class VenuesListView(ListView):
     model = Venue
     template_name = 'venues/venues_list.html'

class VenuesSearchListView(ListView):
     model = Venue
     template_name = 'venues/search_venues.html'

class VenuesCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
     model = Venue
     template_name = 'venues/venue_add.html'
     form_class = VenueForm

     def test_func(self):
          return hasattr(self.request.user, "agent_profile")

     def get_success_url(self):
          return reverse_lazy('venues:venues-list')
     
     def form_valid(self, form):
          form.instance.author = self.request.user.agent_profile
          return super().form_valid(form)
     
class VenuesDetailView(DetailView):
     model = Venue
     template_name = 'venues/venue_detail.html'
     
     def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["amenities"] = self.object.amenityassignment_set.select_related("amenity")
        return ctx
   
