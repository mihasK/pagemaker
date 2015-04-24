from django.conf.urls import patterns, include, url
from pagemaker.views import *


urlpatterns = patterns('pagemaker.views',
    # Examples:
    url(r'^demo/$', 'demo', name='demo'),
    url(r'^$', WebPageListView.as_view(), name='webpage.list'),
)
