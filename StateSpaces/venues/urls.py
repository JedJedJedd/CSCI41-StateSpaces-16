from django.urls import path
from .views import VenuesListView, VenuesSearchListView, VenuesCreateView, VenuesDetailView

urlpatterns = [
    path('', VenuesListView.as_view(), name='venues-list'),
    path('search/', VenuesSearchListView.as_view(), name='venues-search'),
    path('<id>/', VenuesDetailView.as_view(), name='venues-detail'),
    path('create/', VenuesCreateView.as_view(), name = 'venues-create'),
    path('<int:pk>/', VenuesDetailView.as_view(), name='venues-detail'),
]

app_name = 'venues'
