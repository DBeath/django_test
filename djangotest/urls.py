from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    # url(r'^djangotest/', include('djangotest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^jobs/', include('jobs.urls', namespace="jobs")),

    url(r'^admin/', include(admin.site.urls)),
)
