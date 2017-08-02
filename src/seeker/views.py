from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SeekerLoginForm


def login(request):
    if request.method == 'POST':
        form = SeekerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                print("Login failed")
        else:
            print(form.errors)
        return render(request, 'seeker/login.html', {'form': form})
    return render(request, 'seeker/login.html', {'form': SeekerLoginForm()})


def index(request):
    return render(request, 'base.html')
