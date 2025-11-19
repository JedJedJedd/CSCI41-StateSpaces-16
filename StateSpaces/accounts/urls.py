from django.urls import path
from .views import ProfileDetailView, ProfileListView

urlpatterns = [
    #path('<str:username>/', ProfileDetailView.as_view(), name='profile'),
    path('', ProfileListView.as_view(), name='profile'),
]

app_name = 'reservations'
