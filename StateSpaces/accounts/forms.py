from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AgentProfile, Team

class CreateUserForm(UserCreationForm):
    #display_name = forms.CharField(max_length=63)
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
        )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'birth_date', 'email','password1', 'password2']


class CreateAgentForm(UserCreationForm):
    agent_name = forms.CharField(max_length=100)
    contact_number = forms.CharField(max_length=30)
    team = forms.ModelChoiceField(queryset=Team.objects.all())
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 
            'agent_name', 'contact_number', 'team',
            'password1', 'password2'
        ]
    
    