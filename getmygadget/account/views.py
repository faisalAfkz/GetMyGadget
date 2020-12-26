from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import GeneralUser, User


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_object = GeneralUser.objects.raw('SELECT * FROM account_generaluser WHERE email '
                                              '= %s AND password = %s', [email, password])
        if user_object:
            firstname_context = " "
            username_object = GeneralUser.objects.get(email__exact=email)
            request.session['firstName'] = username_object.firstName
            request.session['location'] = username_object.location
            firstname_context = request.session['firstName']
            return render(request, 'account/home.html', {'firstname_context': firstname_context})

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
            return render(request, 'account/home.html')

    context = {'form': form}
    return render(request, 'account/signup.html', context)
