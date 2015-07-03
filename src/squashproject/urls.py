"""squashproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views

from rest_framework.urlpatterns import format_suffix_patterns
from squashapp import views

urlpatterns = [
    # for squash app
    # name will be referenced in the templates as
    # <a href="{% url 'login' %}"></a><
    # url(r'^$', 'squashapp.views.login', name='login'),
    url(r'^$', 'squashapp.views.home', name='home'),
    url(r'^home', 'squashapp.views.home', name='home'),

    # for project list and details
    url(r'^api/projects/$', views.ProjectList.as_view(), name='ProjectList'),
    url(r'^api/projects/(?P<project_primary_sqa>[a-z.]+)/$', views.ProjectDetails.as_view(lookup_field='project_primary_sqa'), name='MyProjectList'),

    # url(r'^accounts/login/$', auth_views.login),
    # This is an example of how to reference an inbuilt existing view in django
    # url(r'^$', auth_views.login),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]


urlpatterns = format_suffix_patterns(urlpatterns)
