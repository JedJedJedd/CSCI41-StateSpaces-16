from django.urls import path
from .views import ReservationDetailView, ConfirmationDetailView, ReservationCreateView#, ReservationListView

urlpatterns = [
    path('', ReservationCreateView.as_view(), name='reservation'),
    #path('<int:pk>/confirmation/', ReservationDetailView.as_view(), name='confirmation'),
    #commented out detail view above temporarily while we dont have data set
    path('<int:pk>/confirmation/', ConfirmationDetailView.as_view(), name='reservation-confirmation'),


]

app_name = 'reservations'
