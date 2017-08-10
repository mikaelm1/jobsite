from django.shortcuts import render


def register(req):
    return render(req, 'employer/register.html')

