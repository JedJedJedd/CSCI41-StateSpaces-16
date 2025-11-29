from django.urls import path
from .views import ConfirmationDetailView, ReservationCreateView

urlpatterns = [
    path('', ReservationCreateView.as_view(), name='reservation'),
    path('<int:pk>/confirmation/', ConfirmationDetailView.as_view(), name='reservation-confirmation'),
]

app_name = 'reservations'
