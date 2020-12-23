from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from account.models import GeneralUser
from django import forms


class CreateUserForm(ModelForm):
    class Meta:
        model = GeneralUser
        # fields = ['email', 'password', 'firstName', 'lastName', 'location']
        fields = '__all__'
