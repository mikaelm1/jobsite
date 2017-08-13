from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Job
from .forms import NewJob
from jobsite.utils import employer_access, deny_acces, seeker_access


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


def job_detail(req, j_id):
    job = Job.objects.filter(id=j_id).first()
    if job is None:
        messages.error(req, 'That job is no longer available.')
        return redirect('/jobs/index')
    user_type = 'anon'
    if hasattr(req.user, 'employer'):
        user_type = 'employer'
    elif hasattr(req.user, 'seeker'):
        user_type = 'seeker'
    return render(req, 'jobs/detail.html',
                  {'job': job, 'user_type': user_type})


@user_passes_test(seeker_access, login_url='/seeker/login')
def apply(req, j_id):
    if req.user.seeker.visible is False:
        messages.error(req, "You can't apply to jobs while your profile \
            is private.")
        return redirect('/seeker/profile/{}'.format(req.user.id))    
    if Job.objects.filter(id=j_id).filter(applicants__id=req.user.seeker.id).exists():
        messages.info(req, "You have already applied to this job.")
        return redirect('/seeker/profile/{}'.format(req.user.id))
    job = Job.objects.filter(id=j_id).first()
    if job is None:
        messages.error(req, 'Unable to apply to this job.')
        return redirect('/jobs/index')
    job.applicants.add(req.user.seeker)
    print(job.applicants)
    return redirect('/seeker/profile/{}'.format(req.user.id))
