from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'seeker/login.html')


def index(request):
    return render(request, 'base.html')
