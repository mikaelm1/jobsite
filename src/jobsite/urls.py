"""jobsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import page.views as page_views


urlpatterns = [
    url(r'^$', page_views.index, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^seeker/', include('seeker.urls', namespace='seeker')),
    url(r'^education/', include('education.urls', namespace='education')),
    url(r'^experience/', include('experience.urls', namespace='experience')),
    url(r'^employer/', include('employer.urls', namespace='employer')),
    url(r'^jobs/', include('jobs.urls', namespace='jobs')),
]
