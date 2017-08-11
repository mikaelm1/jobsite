from django.shortcuts import redirect
from django.contrib import messages


def deny_acces(request):
    messages.error(request, 'Access denied')
    return redirect('/')