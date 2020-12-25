from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from account.models import GeneralUser, User


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_object = GeneralUser.objects.raw('SELECT email, password, location FROM GeneralUser WHERE email = %s '
                                              'AND password = %s', [email, password])
        if user_object:
            request.session['username'] = user_object.email
            request.session['location'] = user_object.location
        # if password in user_ojbectList:
        #    sessionUsernameToStore = [u.__str__ for u in user_ojbectList]
        #    request.session['username'] = sessionUsernameToStore
        #    return render(request, 'account/home.html')

    # user = authenticate(request, email=email, password=password)

    # if user is not None:
    #     login(request, user)
    #     return redirect('home')
    # else:
    #     print("AUTH ERROR")
    # messages.info

    context = {}
    return render(request, 'account/login.html', context)


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'account/signup.html', context)
