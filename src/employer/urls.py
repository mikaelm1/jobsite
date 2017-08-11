from django.conf.urls import url
from .views import register, login_employer


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login_employer, name='login'),
]