from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import CustomerProfile, AgentProfile
from reservations.models import Reservation
from django.contrib.auth.models import User
from .forms import CreateUserForm, CreateAgentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class ProfileDetailView(DetailView):
    model = CustomerProfile
    template_name = 'accounts/user_profile.html'
    context_object_name = 'profile'

    slug_field = 'user__username'
    slug_url_kwarg = 'username'

    def get_object(self):
        username = self.kwargs.get('username')

        # Try Customer first
        try:
            return CustomerProfile.objects.get(user__username=username)
        except CustomerProfile.DoesNotExist:
            pass

        # If not Customer, try Agent
        return get_object_or_404(AgentProfile, user__username=username)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # username = self.kwargs.get('username')
        profile = ctx['profile']

        ctx['is_agent'] = isinstance(profile, AgentProfile)
        ctx['is_customer'] = isinstance(profile, CustomerProfile)

        if ctx['is_customer']:
            ctx['all_reservations'] = Reservation.objects.filter(customer=profile)
        elif ctx['is_agent']:
            ctx['all_venues'] = profile.venues.all()  # assuming a related_name of 'venues'
        else:
            ctx['all_reservations'] = None
        return ctx

        # code block below is temporary
        # def get_success_url(self):
        #     return reverse_lazy(
        #         'accounts:profile',
        #         kwargs={'username': self.object.user.customer_name}
        # )
        # ctx['profile_user'] = get_object_or_404(User, username=username)

        # if self.request.user.is_authenticated:
        #     profile = self.request.user.profile
        # else:      
        # return ctx


class ProfileListView(ListView):
    model = CustomerProfile
    template_name = 'accounts/user_profile_detail.html'

class ProfileCreateView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
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
        return reverse_lazy("login")
    
class AgentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = CreateAgentForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:profile-list')

    def test_func(self):
        u = self.request.user
        return u.is_superuser or AgentProfile.objects.filter(user=u).exists()
