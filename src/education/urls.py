from django.conf.urls import url
from .views import (
    # create_new
    CreateNew,
    delete_ed,
)

urlpatterns = [
    url(r'^create/$', CreateNew.as_view(), name='create'),
    url(r'^delete-ed/(?P<ed_id>\d+)/', delete_ed, name='delete-ed')
]
