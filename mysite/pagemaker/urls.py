from django.conf.urls import patterns, include, url
from pagemaker.views import *


urlpatterns = patterns('pagemaker.views',
    url(r'^demo/$', 'demo', name='demo'),
    url(r'^$', WebPageListView.as_view(), name='webpage.list'),
    url(r'^(?P<pk>\d+)/delete/$', WebPageDeleteView.as_view(), name='webpage.delete'),
    url(r'^(?P<pk>\d+)/$', WebPageEditView.as_view(), name='webpage.edit'),
    url(r'^(?P<pk>\d+)/carousel/add/$', CarouselAddView.as_view(), name='Carousel.add'),
    url(r'^(?P<pk>\d+)/carousel/edit/$', CarouselEditView.as_view(), name='Carousel.edit'),
)
