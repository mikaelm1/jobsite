from django.shortcuts import render


def create_new(req):
    return render(req, 'education/new.html')
