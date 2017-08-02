from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SeekerLoginForm


def login_user(request):
    if request.method == 'POST':
        form = SeekerLoginForm(request.POST)
        if form.is_valid():
            print("Form is valid")
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


def logout_user(request):
    logout(request)
    return redirect('/')


def index(request):
    return render(request, 'base.html')
