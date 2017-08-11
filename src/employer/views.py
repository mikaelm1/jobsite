import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterEmployer
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
                messages.error('There was an error. Please try again.')
                return redirect('/employer/register')
            logger.info('Created employer: {}'.format(employer.name))
            return redirect('/')
        else:
            messages.error(req, 'There was an error creating your account')
    return render(req, 'employer/register.html', {'form': form})


def login(req):
    pass