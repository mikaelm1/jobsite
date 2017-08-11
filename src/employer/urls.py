from django.conf.urls import url
from .views import register, login_employer, profile


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login_employer, name='login'),
    url(r'^profile/(?P<id>\d+)/$', profile, name='profile'),
]