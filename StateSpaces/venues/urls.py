from django.urls import path
from .views import VenuesListView, VenuesSearchListView, VenuesCreateView

urlpatterns = [
    path('', VenuesListView.as_view(), name='venues-list'),
    path('search/', VenuesSearchListView.as_view(), name='venues-search'),
    path('create/', VenuesCreateView.as_view(), name = 'venues-create'),
]

app_name = 'venues'
