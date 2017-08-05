from django.conf.urls import url
from .views import (
    login_user,
    register_user,
    logout_user,
    profile,
    profile_basics,
)

urlpatterns = [
    url(r'^register/$', register_user, name='register'),
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^register/$', register_user, name='register'),
    url(r'^profile/(?P<id>\d+)/$', profile, name='profile'),
    url(r'^profile-basics/(?P<id>\d+)/$', profile_basics, name='profile-basics'),
]
