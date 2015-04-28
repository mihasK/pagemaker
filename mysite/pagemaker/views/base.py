from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from django.shortcuts import get_object_or_404

from pagemaker.models import *

# base classes

class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        self.webpage_pk = self.kwargs['webpage_pk']
        self.webpage = get_object_or_404(WebPage, pk=self.webpage_pk)
        return super(BaseView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['webpage'] = self.webpage
        return context

    def get_success_url(self):
        return reverse_lazy('webpage.edit', kwargs={'webpage_pk':self.webpage_pk})



class BaseWebPageView(View):
    pk_url_kwarg = 'webpage_pk'


class BaseCarouselView(BaseView):
    pk_url_kwarg = 'carousel_pk'


class BaseHeadingIconsView(BaseView):
    pk_url_kwarg = 'headingicons_pk'


class BaseMediaFeatureView(BaseView):
    pk_url_kwarg = 'mediafeature_pk'

