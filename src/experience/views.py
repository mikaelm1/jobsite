from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddExperience
from .models import Experience


@login_required(login_url='/seeker/login')
def add_experience(req):
    form = AddExperience(req.POST or None)
    if req.method == 'POST':
        if form.is_valid():
            user = req.user
            title = form.cleaned_data.get('title')
            company_name = form.cleaned_data.get('company_name')
            job_description = form.cleaned_data.get('job_description')
            start_year = form.cleaned_data.get('start_year')
            start_month = form.cleaned_data.get('start_month')
            end_month = form.cleaned_data.get('end_month')
            end_year = form.cleaned_data.get('end_year')
            present = form.cleaned_data.get('present')
            ex = Experience.objects. \
                create(title=title, company_name=company_name,
                       job_description=job_description,
                       start_year=start_year, start_month=start_month,
                       end_year=end_year, end_month=end_month,
                       present=present)
            messages.success(req, '{} was added to your profile.'.format(title))
            return redirect('/seeker/profile/{}'.format(user.id))
        else:
            print(form.errors)
    return render(req, 'experience/add.html', {'form': form})
