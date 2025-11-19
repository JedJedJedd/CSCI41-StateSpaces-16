from django.urls import path
from .views import VenuesListView, VenuesSearchListView

urlpatterns = [
    path('', VenuesListView.as_view(), name='venues-list'),
    path('search/', VenuesSearchListView.as_view(), name='venues-search'),
]

app_name = 'venues'
