from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Job
from .forms import NewJob
from jobsite.utils import employer_access, deny_acces


def index(req):
    jobs = Job.objects.filter(visible=True)
    print(jobs)
    return render(req, 'jobs/index.html', {'jobs': jobs})


@user_passes_test(employer_access, login_url='/employer/login')
def add(req):
    form = NewJob(req.POST or None)
    if req.method == 'POST':
        if form.is_valid():
            employer = req.user.employer
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data.get('job_description')
            j_type = form.cleaned_data.get('job_type')
            min_salary = form.cleaned_data.get('min_salary')
            max_salary = form.cleaned_data.get('max_salary')
            print(title, desc, j_type, min_salary, max_salary)
            job = Job.objects.create(title=title, job_description=desc,
                                     job_type=j_type, salary_min=min_salary,
                                     salary_max=max_salary, employer=employer)
            messages.success(req, 'Job {} added.'.format(job.title))
            return redirect('/employer/profile/{}'.format(req.user.id))
    return render(req, 'jobs/new.html', {'form': form})


@user_passes_test(employer_access, login_url='/employer/login')
def delete_job(req, j_id):
    user = req.user
    job = Job.objects.filter(id=j_id).first()
    if user.employer.id != job.employer.id:
        return deny_acces(req)
    job.delete()
    messages.success(req, 'Job deleted.')
    return redirect('/employer/profile/{}'.format(user.id))
