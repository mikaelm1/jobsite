from django.conf.urls import url
from .views import (register, login_employer, profile,
                    profile_basics)


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login_employer, name='login'),
    url(r'^profile/(?P<id>\d+)/$', profile, name='profile'),
    url(r'^profile-basics/(?P<id>\d+)/$', profile_basics, name='profile-basics'),
]