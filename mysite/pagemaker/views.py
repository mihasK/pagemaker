from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, TemplateView

from pagemaker.forms import *
from pagemaker.models import *


# Create your views here.
def demo(request):
    return render(request, 'demo.html')

class WebPageListView(CreateView):
    form_class = WebPageAddForm
    template_name = 'webpage_list.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(WebPageListView, self).get_context_data(**kwargs)
        context['webpages'] = WebPage.objects.all()
        return context


class WebPageDeleteView(DeleteView):
    model = WebPage
    success_url = reverse_lazy('webpage.list')


class WebPageEditView(TemplateView):
    template_name = 'webpage_edit.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super(WebPageEditView, self).get_context_data(**kwargs)
        context['webpage'] = WebPage.objects.get(slug=slug)
        return context


class CarouselAddView(CreateView):
    form_class = CarouselAddForm
    template_name = 'carousel_add.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super(CarouselAddView, self).get_context_data(**kwargs)
        context['webpage'] = WebPage.objects.get(slug=slug)
        return context

    def form_valid(self, form):
        return super(CarouselAddView, self).form_valid(form)

    def form_invalid(self, form):
        return super(CarouselAddView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('webpage.edit', kwargs={'slug':slug})