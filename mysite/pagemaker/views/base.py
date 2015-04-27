from django.views.generic import View

# base classes

class BaseWebPageView(View):
    pk_url_kwarg = 'webpage_pk'


class BaseCarouselView(View):
    pk_url_kwarg = 'carousel_pk'