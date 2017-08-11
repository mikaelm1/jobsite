from django.conf.urls import url
from .views import (
    index,
    add
)

urlpatterns = [
    url(r'^jobs/$', index, name='index'),
    url(r'^add-job/$', add, name='add-job'),
]
