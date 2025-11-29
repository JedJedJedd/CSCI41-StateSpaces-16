from collections import defaultdict
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from .models import Venue, AmenityAssignment, Amenity
from .forms import VenueForm


class VenuesListView(ListView):
     """Displays a list of all venues."""
     model = Venue
     template_name = 'venues/venues_list.html'

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['venues'] = Venue.objects.all()
          context['amenity_assignments'] = AmenityAssignment.objects.all()
          return context

class VenuesSearchListView(ListView):
     """Search venues by name, building, type, capacity, area, or city.
     
     Allows Filter by renovation status.
     """
     model = Venue
     template_name = 'venues/search_venues.html'

     def get_context_data(self, **kwargs):
          """Pass all venues and amenity assignments to template."""
          context = super().get_context_data(**kwargs)
          context['venues'] = Venue.objects.all()
          context['amenity_assignments'] = AmenityAssignment.objects.all()
          return context

     def get_queryset(self):
          """Filter venues based on search query and renovation filter."""
          queryset = super().get_queryset()
          search_query = self.request.GET.get("q", "")
          renovation = self.request.GET.get("renovation")

          if search_query:
               queryset = queryset.filter(Q(venue_name__icontains=search_query)
                              | Q(building__building_name__icontains=search_query) 
                              | Q(venue_type__icontains=search_query) 
                              | Q(venue_floor_area__icontains=search_query) 
                              | Q(venue_capacity__icontains=search_query) 
                              | Q(building__city__icontains=search_query)
                         )
               
          if renovation == "yes":
               queryset = queryset.filter(under_renovation=True)

          elif renovation == "no":
               queryset = queryset.filter(under_renovation=False)
          else:
               queryset = queryset
          
          return queryset

class VenuesCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
     """Creates a new venue (Only agents are allowed)."""

     model = Venue
     template_name = 'venues/venue_add.html'
     form_class = VenueForm

     def test_func(self):
          """Only agents can create venues."""
          return hasattr(self.request.user, "agent_profile")

     def get_success_url(self):
          """Redirect to venues list after creation."""
          return reverse_lazy('venues:venues-list')
     
     def form_valid(self, form):
          """Automatically assign current agent to the venue."""
          form.instance.agent = self.request.user.agent_profile
          return super().form_valid(form)

     def get_context_data(self, **kwargs):
        """Pass all amenities to template."""
        ctx = super().get_context_data(**kwargs)
        ctx["amenities"] = Amenity.objects.all()
        return ctx

class VenuesDetailView(DetailView):
     """Display details of a specific venue including amenities and reservations."""
     model = Venue
     template_name = 'venues/venue_detail.html'
     
     def get_context_data(self, **kwargs):
        """Add venue's amenities and reservations to template."""
        ctx = super().get_context_data(**kwargs)
        ctx["amenities"] = AmenityAssignment.objects.select_related("amenity").filter(venue=self.object)
        ctx["reservations"] = self.object.reservations.all()
        return ctx
     
class VenuesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
     """Update an existing venue.
     
     Only agents are allowed to update.
     """

     model = Venue
     template_name = 'venues/venue_update.html'
     form_class = VenueForm

     def test_func(self):
          """Only agents can update venues."""
          return hasattr(self.request.user, "agent_profile")

     def form_valid(self, form):
          """Ensure venue keeps its assigned agent."""
          form.instance.agent = self.request.user.agent_profile
          return super().form_valid(form)
     
     def get_success_url(self):
          """Redirect to venue detail page after update."""
          return reverse_lazy(
               'venues:venues-detail', kwargs={'pk': self.get_object().pk}
          )
   
     def get_context_data(self, **kwargs):
        """Pass all amenities to template for dynamic form fields."""
        context = super().get_context_data(**kwargs)
        context["amenities"] = Amenity.objects.all()
        return context
