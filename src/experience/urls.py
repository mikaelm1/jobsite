from django.conf.urls import url
from .views import add_experience

urlpatterns = [
    url(r'^add/$', add_experience, name='add-experience'),
]