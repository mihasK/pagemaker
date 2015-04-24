from django.conf.urls import patterns, include, url
from pagemaker.views import *


urlpatterns = patterns('pagemaker.views',
    url(r'^demo/$', 'demo', name='demo'),
    url(r'^$', WebPageListView.as_view(), name='webpage.list'),
    url(r'^(?P<slug>[-\w]+)/$', WebPageEditView.as_view(), name='webpage.edit'),
    url(r'^(?P<slug>[-\w]+)/carousel/add/$', CarouselAddView.as_view(), name='carousel.add'),
)
