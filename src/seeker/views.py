from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SeekerLoginForm, SeekerRegisterForm
from .models import User


def login_user(request):
    if request.method == 'POST':
        form = SeekerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                print("Got user")
                login(request, user)
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Username or password was wrong')
        else:
            print(form.errors)
        return render(request, 'seeker/login.html', {'form': form})
    return render(request, 'seeker/login.html', {'form': SeekerLoginForm()})


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = SeekerRegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            User.objects.create_user(username=username, email=email,
                                     password=password)
            return redirect('/')
        else:
            messages.error(request, 'There was an error creating your account.')
    return render(request, 'seeker/register.html', {'form': form})


@login_required(login_url='/seeker/login')
def profile(request):
    return render(request, 'seeker/profile.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def index(request):
    return render(request, 'base.html')
