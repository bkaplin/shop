from django.conf.urls import patterns, include, url
from django.contrib import admin
from shop.views import main, contact

urlpatterns = patterns('',
    # Examples:
    url(r'^$', main, name='main'),
	url(r'^contact/$', contact, name='contact'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^clothes/', include('clothes.urls', namespace="clothes")),
)
