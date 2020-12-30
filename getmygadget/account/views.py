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
        else:
            message = "Email or password did not match."
            return render(request, 'account/login.html', {'message': message})

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
        # email = form.POST.cleaned_data['email']
        if form.is_valid():
            email = form.cleaned_data["email"]
            user_object = GeneralUser.objects.raw('SELECT * FROM account_generaluser WHERE email = %s', [email])
            if user_object:
                message = "User with the following email already exists."
                context = {'form': form, 'message': message}
                return render(request, 'account/signup.html', context)
            else:
                form.save()
                # message = "Account Created Successfully."
                # context = {'message': message}
                # return render(request, 'account/login.html', context) //rendering does not Redirect to to login
                return redirect("/account/login")

    context = {'form': form}
    return render(request, 'account/signup.html', context)

