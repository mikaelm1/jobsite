from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.forms.models import model_to_dict
from .forms import (
    SeekerLoginForm, SeekerRegisterForm, SeekerEditForm,
    SeekerProfile
)
from .models import User
from education.models import SeekerEducation
from jobsite.utils import deny_acces, seeker_access


def login_user(request):
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
                messages.add_message(request, messages.ERROR, 'Username or password was wrong')
        else:
            print(form.errors)
        return render(request, 'seeker/login.html', {'form': form})
    return render(request, 'seeker/login.html', {'form': SeekerLoginForm()})


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = SeekerRegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email').lower()
            first_name = form.cleaned_data.get('first_name').title()
            last_name = form.cleaned_data.get('last_name').title()
            user = User.objects.create_user(username=username, email=email,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name)
            login(request, user)
            return redirect('/seeker/profile/{}'.format(user.id))
        else:
            messages.error(request, 'There was an error creating your account.')
    return render(request, 'seeker/register.html', {'form': form})


@login_required(login_url='/seeker/login')
def profile(request, id):
    user = User.objects.get(id=id)
    if hasattr(user, 'seeker') is False:
        return deny_acces()
    if user.id != request.user.id:
        return deny_acces(request)
    form = SeekerProfile(request.POST or None)
    ed = user.seeker.seekereducation_set.all().order_by('-year_ended')
    ex = user.seeker.experience_set.all().order_by('-date_added')
    # post means toggle profile visibility
    if request.method == 'POST':
        if user.seeker.visible:
            user.seeker.visible = False
        else:
            user.seeker.visible = True
        user.seeker.save()
        user.save()
        return redirect('/seeker/profile/{}'.format(id))
    return render(request, 'seeker/profile.html', {'user': user, 'form': form,
                                                   'schools': ed,
                                                   'experiences': ex})


@user_passes_test(seeker_access)
def public_profile(req, u_id):
    user = User.objects.filter(id=u_id).first()
    if user is None:
        messages.error(req, 'There was an error locating the user.')
        return redirect('/employer/profile/{}'.format(req.user.id))
    ed = user.seeker.seekereducation_set.all()
    exp = user.seeker.experience_set.all()
    return render(req, 'seeker/public_profile.html',
                  {'user': user, 'schools': ed, 'experiences': exp})


@login_required(login_url='/seeker/login')
def profile_basics(request, id):
    user = User.objects.filter(id=id).first()
    if user.id != request.user.id:
        return deny_acces()
    if user is None:
        messages.error(request, 'There was an error getting your profile')
        return redirect('/seeker/profile/{}'.format(id))
    if request.method == 'POST':
        form = SeekerEditForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email').lower()
            u = User.objects.filter(email=email).first()
            if u and u.email != user.email:
                messages.error(request, 'Another user already has that email')
            first_name = form.cleaned_data.get('first_name').title()
            last_name = form.cleaned_data.get('last_name').title()
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            return redirect('/seeker/profile/{}'.format(id))
        else:
            print('Form is not valid')
            print(form.errors)
    else:
        data = model_to_dict(user)
        form = SeekerEditForm(data)
    return render(request, 'seeker/profile_basics.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')


@user_passes_test(seeker_access)
def applied(req):
    jobs = req.user.seeker.job_set.all()
    return render(req, 'seeker/applied.html', {'jobs': jobs})
