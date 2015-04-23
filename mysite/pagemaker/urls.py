from django.conf.urls import patterns, include, url


urlpatterns = patterns('pagemaker.views',
    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    url(r'^$', 'demo', name='demo'),
)
