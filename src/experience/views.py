from django.shortcuts import render


def add_experience(req):
    return render(req, 'experience/add.html')
