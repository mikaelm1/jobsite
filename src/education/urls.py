from django.conf.urls import url
from .views import (
    # create_new
    CreateNew
)

urlpatterns = [
    url(r'^create/$', CreateNew.as_view(), name='create'),
]
