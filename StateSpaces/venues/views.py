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

class VenuesCreateView(PermissionRequiredMixin, CreateView):
     model = Venue
     template_name = 'venues/venue_add.html'
     permission_required = "user.can_add_venue"
     form_class = VenueForm

     def get_success_url(self):
          return reverse_lazy('venues:create-view')
     
     def form_valid(self, form):
          form.instance.author = self.request.user.profile
          return super().form_vaild(form)

class VenuesDetailView(DetailView):
     model = Venue
     template_name = 'venues/venue_detail.html'

     def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["amenities"] = self.object.amenityassignment_set.select_related("amenity")
        return ctx
     
