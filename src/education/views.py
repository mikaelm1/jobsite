import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib import messages
from .forms import NewEducationForm
from .models import SeekerEducation, Education


@method_decorator(login_required, name='post')
@method_decorator(login_required, name='get')
class CreateNew(View):
    def post(self, req):
        form = NewEducationForm(req.POST)
        if form.is_valid():
            user = req.user
            name = form.cleaned_data.get('name')
            city = form.cleaned_data.get('city')
            state = form.cleaned_data.get('state')
            graduated = form.cleaned_data.get('graduated')
            year_started = form.cleaned_data.get('year_started')
            year_ended = form.cleaned_data.get('year_ended')
            degree = form.cleaned_data.get('degree')
            major = form.cleaned_data.get('major')
            # print(graduated, name, city, state, year_started, year_ended)
            ed = Education.objects.filter(name=name).first()
            if ed is None:
                ed = Education.objects.create(name=name, city=city,
                                              state=state)
            ed_seeker = SeekerEducation.objects. \
                create(year_started=year_started, year_ended=year_ended,
                       graduated=graduated, seeker=user.seeker, education=ed,
                       degree=degree, major=major)
            return redirect('/seeker/profile/{}'.format(user.seeker.id))
        else:
            return render(req, 'education/new.html', {'form': form})  

    def get(self, req):
        form = NewEducationForm()
        return render(req, 'education/new.html', {'form': form})


@login_required(login_url='/seeker/login')
def delete_ed(req, ed_id):
    logger = logging.getLogger(__name__)
    if req.method == 'POST':
        ed = SeekerEducation.objects.filter(id=ed_id).first()
        print(ed)
        if ed is None:
            logger.error('Did not find seeker\'s education')
            messages.error(req, 'Error deleting your education.')
        else:
            ed.delete()
            messages.success(req, 'Profile updated.')
    else:
        logger.error('Got {} request'.format(req.method))
    return redirect('/seeker/profile/{}'.format(req.user.id))
