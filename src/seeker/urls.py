from django.conf.urls import url
from .views import (
    login_user,
    register_user,
    logout_user,
    profile,
    profile_basics,
    applied,
    public_profile,
)

urlpatterns = [
    url(r'^register/$', register_user, name='register'),
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^register/$', register_user, name='register'),
    url(r'^profile/(?P<id>\d+)/$', profile, name='profile'),
    url(r'^profile-basics/(?P<id>\d+)/$', profile_basics,
        name='profile-basics'),
    url(r'^applied/$', applied, name='applied'),
    url(r'^public-profile/(?P<u_id>\d+)/$', public_profile,
        name='public_profile'),
]
