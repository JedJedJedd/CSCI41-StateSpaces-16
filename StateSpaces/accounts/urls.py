from django.urls import path
from .views import ProfileDetailView, ProfileListView, ProfileCreateView

urlpatterns = [
    #path('<str:username>/', ProfileDetailView.as_view(), name='profile'),
    path('', ProfileListView.as_view(), name='profile'),
    path('register/', ProfileCreateView.as_view(), name='register'),
]

app_name = 'accounts'
