from django.conf.urls import url
from .views import (
    create_new
)

urlpatterns = [
    url(r'^create/$', create_new, name='create'),
]
