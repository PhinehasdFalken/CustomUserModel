from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

from .models import NewUser
from users.forms import RegistrationForm, AccountAuthenticationForm

# Create your views here.
def home_view(request):
    return render(request, 'users/home.html')

def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.email}.")
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            email = form.cleaned_data.get('email').lower()
            # user_name = form.cleaned_data.get('user_name')
            # first_name = form.cleaned_data.get('first_name')
            raw_password = form.cleaned_data.get('password1')

            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination: # if destination != None
                return redirect(destination)
            return redirect('home')
        else:
            # returning the registration form back to the template if form is not valid(there are errors) 
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    context = {}

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user: # if user != None(if there is a user with the inputed email & password in the database)
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination: # if destination != None
                    return redirect(destination)
                return redirect('home')
        else:
            # returning the login form back to the template if form is not valid(there are errors) 
            context['login_form'] = form

    return render(request, 'users/login.html', context)


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))
    return redirect
