from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AgentProfile, Team

class CreateUserForm(UserCreationForm):
    #display_name = forms.CharField(max_length=63)
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
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control border border-dark border-1', 'style': 'background-color: #F4EFE6;'})
    
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
    
    