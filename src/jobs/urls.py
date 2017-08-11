from django.conf.urls import url
from .views import (
    index,
    add,
    delete_job,
    job_detail
)


urlpatterns = [
    url(r'^jobs/$', index, name='index'),
    url(r'^add-job/$', add, name='add-job'),
    url(r'^delete-job/(?P<j_id>\d+)/$', delete_job, name='delete-job'),
    url(r'^job-detail/(?P<j_id>\d+)/$', job_detail, name='job-detail'),
]
