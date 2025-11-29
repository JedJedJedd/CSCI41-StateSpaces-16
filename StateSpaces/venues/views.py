from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Venue, AmenityAssignment
from .forms import VenueForm
from django.db.models import Q

# Create your views here.
class VenuesListView(ListView):
     model = Venue
     template_name = 'venues/venues_list.html'

class VenuesSearchListView(ListView):
     model = Venue
     template_name = 'venues/search_venues.html'

     def get_queryset(self):
          qs = super().get_queryset()
          s = self.request.GET.get("q", "")
          reno = self.request.GET.get("renovation")

          if s:
               qs = qs.filter(Q(venue_name__icontains=s)| Q(building__building_name__icontains=s) | Q(venue_type__icontains=s) |
                              Q(venue_floor_area__icontains=s) | Q(venue_capacity__icontains=s) | Q(building__city__icontains=s) |
                              Q(under_renovation__icontains=s))
               
          if reno:
            qs = qs.filter(under_renovation=True)
          
          return super().get_queryset()

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
        ctx["amenities"] = AmenityAssignment.objects.select_related("amenity").filter(venue=self.object)
        ctx["reservations"] = self.object.reservations.all()
        return ctx
   
