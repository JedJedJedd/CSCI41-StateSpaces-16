from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import CreateUserForm, CreateAgentForm
from .models import CustomerProfile, AgentProfile
from reservations.models import Reservation

class ProfileDetailView(DetailView):
    """ 
    Display the profile page for either a customer or an agent.
    """

    model = CustomerProfile
    template_name = 'accounts/user_profile.html'
    context_object_name = 'profile'

    slug_field = 'user__username'
    slug_url_kwarg = 'username'

    def get_object(self):
        """
        Return the profile for the given username.
        """
        username = self.kwargs.get('username')

        # Attempts to return CustomerProfile first.
        try:
            return CustomerProfile.objects.get(user__username=username)
        except CustomerProfile.DoesNotExist:
            pass

        # If not Customer, try AgentProfile.
        return get_object_or_404(AgentProfile, user__username=username)

    def get_context_data(self, **kwargs):
        """ 
        Add related data to the template context.
        """
        context = super().get_context_data(**kwargs)
        profile = context['profile']

        context['is_agent'] = isinstance(profile, AgentProfile)
        context['is_customer'] = isinstance(profile, CustomerProfile)

        if context['is_customer']:
            # All reservations made by this customer.
            context['all_reservations'] = Reservation.objects.filter(customer=profile)

        elif context['is_agent']:
            # Assuming AgentProfile has a related_name of 'venues'.
            context['all_venues'] = profile.venues.all()  

        else:
            context['all_reservations'] = None

        return context


class ProfileListView(ListView):
    """
    Displays a list of all customer profiles.
    """

    model = CustomerProfile
    template_name = 'accounts/user_profile_detail.html'

class ProfileCreateView(CreateView):
    """Registration view for new users 
    
    Creates a user, then automatically creates a linked CustomerProfile with data.
    """

    model = User
    form_class = CreateUserForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        """
        Save User first, then create corresponding CustomerProfile.
        """
        new_user = form.save(commit=False)

        fullname = '{} {}'.format(
            form.cleaned_data['first_name'],
            form.cleaned_data['last_name']
        )
        birth_date = form.cleaned_data.get('birth_date')

        new_user.save()

        CustomerProfile.objects.create(
            user=new_user,
            customer_name=fullname,
            birth_date=birth_date,
            email=new_user.email,
            username = new_user.username
        )
        
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirects to login page after registration.
        """
        return reverse_lazy("login")
    
class AgentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """View for creating new agents.

    Only superusers or existing agents are allowed to access.
    """

    form_class = CreateAgentForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:profile-list')

    def test_func(self):
        """
        Restricts access so only superusers or existing agents are allowed to create new agents
        """

        u = self.request.user
        return u.is_superuser or AgentProfile.objects.filter(user=u).exists()
