from django.conf.urls import url
from .views import register


urlpatterns = [
    url(r'^register/$', register, name='register'),
]