from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pylblr.views.home', name='home'),
    # url(r'^pylblr/', include('pylblr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blogengine.views.getPosts'),
    url(r'^(?P<selected_page>\d+)/?$', 'blogengine.views.getPosts'),
    url(r'^(?P<postSlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getPost'),
)
