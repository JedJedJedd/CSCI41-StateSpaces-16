from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Reservation

# Create your views here.
class ReservationListView(ListView):
     model = Reservation
     template_name = 'reservations/reservation_form.html'

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'reservations/reservation_confirmation.html'

    def get_success_url(self):
        return reverse_lazy('forum:thread-detail',
                            kwargs={'pk': self.object.pk})

class ConfirmationListView(ListView):
    model = Reservation
    template_name = 'reservations/reservation_confirmation.html'
    
    def get_success_url(self):
        return reverse_lazy('forum:thread-detail',
                            kwargs={'pk': self.object.pk})                            