from django.conf.urls import patterns, include, url
from django.contrib import admin
from clothes.views import all_clothes, detail

urlpatterns = patterns('',
    url(r'^$', all_clothes, name='all_clothes'),
	url(r'^(?P<pk>\d+)/$', detail, name='detail'),
)
