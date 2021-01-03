from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistrationForm


def login_view(request):
    context = {}
    if request.POST:
        form = ''
    else:
        form = ''

    return render(request, 'accounts/login.html')


def home_view(request):
    return render(request, 'accounts/home.html')


def signup_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('/accounts/home')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')
