from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    #display_name = forms.CharField(max_length=63)
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'password1', 'password2']
        exclude = ['email']
