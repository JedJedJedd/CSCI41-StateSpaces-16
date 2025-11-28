from django.urls import path
from .views import VenuesListView, VenuesSearchListView, VenuesDetailView, VenuesAddView

urlpatterns = [
    path('', VenuesListView.as_view(), name='venues-list'),
    path('search/', VenuesSearchListView.as_view(), name='venues-search'),
    path('<id>/', VenuesDetailView.as_view(), name='venues-detail'),
]

app_name = 'venues'
