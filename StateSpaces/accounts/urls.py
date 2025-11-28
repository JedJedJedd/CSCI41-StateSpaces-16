from django.urls import path
from .views import ProfileDetailView, ProfileListView, ProfileCreateView

urlpatterns = [
    path('register/', ProfileCreateView.as_view(), name='register'),
    path('<str:username>/', ProfileDetailView.as_view(), name='profile'),
    path('', ProfileListView.as_view(), name='profile'),
    
]

app_name = 'accounts'
