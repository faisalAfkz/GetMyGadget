from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import UserAccount


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = UserAccount
        fields = ("email", "username", "password1", "password2")
