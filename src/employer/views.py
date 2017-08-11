import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegisterEmployer, LoginEmployer
from .models import Employer, User

logger = logging.getLogger(__name__)


def register(req):
    form = RegisterEmployer(req.POST or None)
    if req.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            city = form.cleaned_data.get('city')
            state = form.cleaned_data.get('state')
            url = form.cleaned_data.get('web_url')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=pwd,
                                            email=email)
            if user is None:
                messages.error('There was an error. Please try again.')
                return redirect('/employer/register')
            employer = Employer.objects. \
                create(name=name, city=city, state=state, web_url=url,
                       user=user)
            if employer is None:
                user.delete()
                messages.error('There was an error. Please try again.')
                return redirect('/employer/register')
            login(req, user)
            logger.info('Created employer: {}'.format(employer.name))
            return redirect('/')
        else:
            messages.error(req, 'There was an error creating your account')
    return render(req, 'employer/register.html', {'form': form})


def login_employer(req):
    form = LoginEmployer(req.POST or None)
    if req.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(req, username=username, password=pwd)
            if user:
                login(req, user)
                return redirect('/')
            else:
                messages.error(req, 'Invalid login credentials')
        else:
            print("Form errors")
    return render(req, 'employer/login.html', {'form': form})


@login_required(login_url='/employer/login')
def profile(req, id):
    u = User.objects.get(id=id)
    if u.id != req.user.id:
        messages.error(req, 'Access denied')
        return redirect('/')
    employer = u.employer
    return render(req, 'employer/profile.html', {'employer': employer})


@login_required(login_url='/employer/login')
def profile_update(req, id):
    pass