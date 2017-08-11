from django.conf.urls import url
from .views import (
    index
)

urlpatterns = [
    url(r'^jobs/$', index, name='index'),
]