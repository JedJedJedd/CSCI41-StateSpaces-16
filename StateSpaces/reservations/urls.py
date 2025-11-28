from django.urls import path
from .views import ReservationListView, ReservationDetailView, ConfirmationListView

urlpatterns = [
    path('', ReservationListView.as_view(), name='reservation'),
    #path('<int:pk>/confirmation/', ReservationDetailView.as_view(), name='confirmation'),
    #commented out detail view above temporarily while we dont have data set
    path('confirmation/', ConfirmationListView.as_view(), name='reservation-confirmation'),


]

app_name = 'reservations'
