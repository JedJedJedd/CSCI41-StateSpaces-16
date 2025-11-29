"""
Forms for user and agent registration.

Both forms apply Bootstrap styling to fields for consistent UI appearance.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AgentProfile, Team

class CreateUserForm(UserCreationForm):
    """Form for registering a new user."""

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
        })
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
        })
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
        })
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email Address',
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password Again',
        })
    )

    def __init__(self, *args, **kwargs):
        """Adds Bootstrap implementation to all fields"""
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control border border-dark border-1', 
                'style': 'background-color: #F4EFE6;'
            })
    
    class Meta:
        model = User
        #lists fields to show on form
        fields = ['username', 'first_name', 'last_name', 'birth_date', 'email','password1', 'password2']


class CreateAgentForm(UserCreationForm):
    """Form for registering a new agent"""
    
    agent_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Agent Name',
        })
    )

    contact_number = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Contact Number',
        })
    )

    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        widget=forms.Select())
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email Address'
        })
    )

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name'
        })
    )

    last_name = forms.CharField(
        max_length=30, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name'
        })
    )

    def __init__(self, *args, **kwargs):
        """Adds Bootstrap implementation to all fields"""
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control border border-dark border-1', 'style': 'background-color: #F4EFE6;'})

    class Meta:
        model = User
        #lists fields to show on form
        fields = [
            'username', 'first_name', 'last_name', 'email', 
            'agent_name', 'contact_number', 'team',
            'password1', 'password2'
        ]

    def save(self, commit=True):
        """Save the User and create a related AgentProfile instance."""
        user = super().save(commit=commit)
        AgentProfile.objects.create(
            user=user,
            agent_name=self.cleaned_data['agent_name'],
            contact_number=self.cleaned_data['contact_number'],
            team=self.cleaned_data['team'],
        )
        return user
    
    
    