from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReservationForm
from .models import Reservation


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservations/reservation_form.html'

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer_profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('reservations:reservation-confirmation', kwargs={'pk': self.object.pk})

class ConfirmationDetailView(DetailView):
    model = Reservation
    template_name = 'reservations/reservation_confirmation.html'
    
    def get_success_url(self):
        return reverse_lazy('reservations:reservation-detail', kwargs={'pk': self.object.pk})                            