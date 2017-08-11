from django.shortcuts import render


def index(req):
    return render(req, 'jobs/index.html')
