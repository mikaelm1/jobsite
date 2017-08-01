from django.shortcuts import render


def login(request):
    
    return render(request, 'seeker/login.html')


def index(request):
    return render(request, 'base.html')
