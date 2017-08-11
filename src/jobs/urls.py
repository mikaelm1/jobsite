from django.conf.urls import url
from .views import (
    index,
    add,
    delete_job
)


urlpatterns = [
    url(r'^jobs/$', index, name='index'),
    url(r'^add-job/$', add, name='add-job'),
    url(r'^delete-job/(?P<j_id>\d+)/$', delete_job, name='delete-job'),
]
