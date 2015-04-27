from django.core.urlresolvers import reverse, reverse_lazy
from django.db.transaction import atomic
from django.db.models import Max
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, TemplateView

from pagemaker.views.base import *
from pagemaker.forms import *
from pagemaker.models import *


# Create your views here.
def demo(request):
    return render(request, 'demo.html')

class WebPageListView(BaseWebPageView, CreateView):
    model = WebPage
    form_class = WebPageAddForm
    template_name = 'webpage_list.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(WebPageListView, self).get_context_data(**kwargs)
        context['webpages'] = WebPage.objects.all()
        return context


class WebPageDeleteView(BaseWebPageView, DeleteView):
    model = WebPage
    success_url = reverse_lazy('webpage.list')
    template_name = 'webpage_confirm_delete.html'


class WebPageEditView(BaseWebPageView, UpdateView):
    model = WebPage
    form_class = WebPageAddForm
    template_name = 'webpage_edit.html'

    def get_success_url(self):
        return reverse_lazy('webpage.edit', kwargs={'pk':self.kwargs['pk']})


class CarouselAddView(BaseCarouselView, CreateView):
    form_class = CarouselAddForm
    template_name = 'carousel_add.html'

    def dispatch(self, request, *args, **kwargs):
        self.webpage_pk = self.kwargs['webpage_pk']
        self.webpage = get_object_or_404(WebPage, pk=self.webpage_pk)
        return super(CarouselAddView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CarouselAddView, self).get_context_data(**kwargs)
        context['webpage'] = self.webpage
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.webpage_id = self.kwargs['webpage_pk']
        obj.order = 0
        return super(CarouselAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('webpage.edit', kwargs={'webpage_pk':self.webpage_pk})


class CarouselEditView(BaseCarouselView, UpdateView):
    model = Carousel
    fields = ['title']
    form_class = CarouselAddForm
    template_name = 'carousel_edit.html'

    def get_success_url(self):
        return reverse_lazy('carousel.edit', kwargs={'carousel_pk':self.kwargs['carousel_pk']})


class CarouselDeleteView(BaseCarouselView, DeleteView):
    model = Carousel
    template_name = 'carousel_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        self.carousel_pk = self.kwargs['carousel_pk']
        self.carousel = get_object_or_404(Carousel, pk=self.carousel_pk)
        self.webpage = self.carousel.webpage
        return super(CarouselDeleteView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CarouselDeleteView, self).get_context_data(**kwargs)
        context['webpage'] = self.webpage
        return context

    def get_success_url(self):
        return reverse_lazy('webpage.edit', kwargs={'webpage_pk':self.webpage.pk})


class SlideAddView(CreateView):
    form_class = SlideAddForm
    template_name = 'slide_add.html'

    def dispatch(self, request, *args, **kwargs):
        self.carousel_pk = self.kwargs['carousel_pk']
        self.carousel = get_object_or_404(Carousel, pk=self.carousel_pk)
        return super(SlideAddView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SlideAddView, self).get_context_data(**kwargs)
        context['object'] = self.carousel
        context['slides'] = Slide.objects.filter(carousel_pk = self.carousel_pk)
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.carousel_id = self.kwargs['carousel_pk']
        return super(SlideAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('carousel.edit', kwargs={'carousel_pk':self.carousel_pk})
