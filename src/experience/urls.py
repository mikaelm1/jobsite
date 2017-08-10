from django.conf.urls import url
from .views import add_experience, delete_exp

urlpatterns = [
    url(r'^add/$', add_experience, name='add-experience'),
    url(r'^delete-ex/(?P<ex_id>\d+)/$', delete_exp, name='delete-ex'),
]