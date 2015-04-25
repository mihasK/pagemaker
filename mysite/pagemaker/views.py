from django.core.urlresolvers import reverse, reverse_lazy
from django.db.transaction import atomic
from django.db.models import Max
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DeleteView, FormView, TemplateView

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
    template_name = 'webpage_confirm_delete.html'


class WebPageEditView(TemplateView):
    template_name = 'webpage_edit.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super(WebPageEditView, self).get_context_data(**kwargs)
        webpage = WebPage.objects.get(slug=slug)
        context['webpage'] = webpage
        context['gadgets'] = Gadgets.objects.filter(webpage=webpage)
        return context


class CarouselAddView(CreateView):
    form_class = CarouselAddForm
    template_name = 'carousel_add.html'

    def dispatch(self, request, *args, **kwargs):
        self.slug = self.kwargs['slug']
        self.webpage = get_object_or_404(WebPage, slug=self.slug)
        return super(CarouselAddView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CarouselAddView, self).get_context_data(**kwargs)
        context['webpage'] = WebPage.objects.get(slug=self.slug)
        return context

    @atomic
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.webpage_id = self.webpage.id
        form_valid_result = super(CarouselAddView, self).form_valid(form)

        # add to gadgets list
        last_gadget = Gadgets.objects.filter(webpage_id=self.webpage.id).aggregate(Max('order'))
        try:
            myorder = last_gadget['order__max']+1
        except:
            myorder = 1

        Gadgets.objects.create(webpage_id=self.webpage.id,
                               identifier=obj.pk,
                               type='Carousel',
                               order = myorder,
                               )

        return form_valid_result


    def get_success_url(self):
        return reverse_lazy('webpage.edit', kwargs={'slug':self.slug})