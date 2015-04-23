from django.conf.urls import patterns, include, url


urlpatterns = patterns('pagemaker.views',
    # Examples:
    url(r'^demo/$', 'demo', name='demo'),
    url(r'^$', 'main', name='main'),
)
