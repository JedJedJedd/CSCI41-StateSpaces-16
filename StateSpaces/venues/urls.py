from django.urls import path
from .views import VenuesListView, VenuesSearchListView, VenuesCreateView, VenuesDetailView, VenuesUpdateView

urlpatterns = [
    path('', VenuesListView.as_view(), name='venues-list'),
    path('search/', VenuesSearchListView.as_view(), name='venues-search'),
    path('create/', VenuesCreateView.as_view(), name = 'venues-create'),
    path('<int:pk>/', VenuesDetailView.as_view(), name='venues-detail'),
    path('<int:pk>/update/', VenuesUpdateView.as_view(), name='venues-update')

]

app_name = 'venues'
