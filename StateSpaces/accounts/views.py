from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import CustomerProfile, AgentProfile
# Create your views here.


class ProfileDetailView(DetailView):
    model = CustomerProfile
    template_name = 'accounts/user_profile_detail.html'
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
