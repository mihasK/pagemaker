from django.conf.urls import patterns, include, url
from pagemaker.views import *


urlpatterns = patterns('pagemaker.views',
    url(r'^demo/$', 'demo', name='demo'),
    url(r'^$', WebPageListView.as_view(), name='webpage.list'),
    url(r'^(?P<webpage_pk>\d+)/delete/$', WebPageDeleteView.as_view(), name='webpage.delete'),
    url(r'^(?P<webpage_pk>\d+)/$', WebPageEditView.as_view(), name='webpage.edit'),

    url(r'^(?P<webpage_pk>\d+)/$', WebPageEditGadgetsView.as_view(), name='webpage.gadgets'),

    url(r'^(?P<webpage_pk>\d+)/carousel/add/$', CarouselAddView.as_view(), name='carousel.add'),
    url(r'^(?P<webpage_pk>\d+)/(?P<carousel_pk>\d+)/carousel/edit/$', CarouselEditView.as_view(), name='carousel.edit'),
    url(r'^(?P<webpage_pk>\d+)/(?P<carousel_pk>\d+)/carousel/delete/$', CarouselDeleteView.as_view(),
        name='carousel.delete'),
    url(r'^(?P<webpage_pk>\d+)/(?P<carousel_pk>\d+)/carousel/slide/add/$', SlideAddView.as_view(), name='slide.add'),

    url(r'^(?P<webpage_pk>\d+)/headingicons/add/$', HeadingIconsAddView.as_view(), name='headingicons.add'),
    url(r'^(?P<webpage_pk>\d+)/(?P<headingicons_pk>\d+)/headingicons/edit/$', HeadingIconsEditView.as_view(),
        name='headingicons.edit'),
    url(r'^(?P<webpage_pk>\d+)/(?P<headingicons_pk>\d+)/headingicons/delete/$', HeadingIconsDeleteView.as_view(),
        name='headingicons.delete'),

    url(r'^(?P<webpage_pk>\d+)/mediafeature/add/$', MediaFeatureAddView.as_view(), name='mediafeature.add'),
    url(r'^(?P<webpage_pk>\d+)/(?P<mediafeature_pk>\d+)/mediafeature/edit/$', MediaFeatureEditView.as_view(),
        name='mediafeature.edit'),
    url(r'^(?P<webpage_pk>\d+)/(?P<mediafeature_pk>\d+)/mediafeature/delete/$', MediaFeatureDeleteView.as_view(),
        name='mediafeature.delete'),

)
