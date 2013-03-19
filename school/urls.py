from django.conf.urls import patterns, include, url

# Static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# TastyPie API
from django.conf.urls.defaults import *
from tastypie.api import Api
from classroom.api import TeacherResource, StudentResource, ClassResource

# Django Admin
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(TeacherResource())
v1_api.register(StudentResource())
v1_api.register(ClassResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^school/', include('school.foo.urls')),
    url(r'^$', 'client.views.index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Classroom API URLs
    url(r'^classroom/(?P<pk>\d+)', 'classroom.views.index'),
    url(r'^classroom/', 'classroom.views.index'),
    url(r'^api/', include(v1_api.urls)),

    # Common Core Standards
    url(r'commoncore/(?P<coreString>.+)', 'commoncore.views.index'),
    url(r'commoncore/', 'commoncore.views.index'),
)

urlpatterns += staticfiles_urlpatterns()
