from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, TemplateView

from pagemaker.forms import *
from pagemaker.models import *


# Create your views here.
def demo(request):
    return render(request, 'demo.html')

class WebPageListView(CreateView):
    form_class = WebPageCreateForm
    template_name = 'webpage_list.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(WebPageListView, self).get_context_data(**kwargs)
        context['webpages'] = WebPage.objects.all()
        return context


class WebPageEditView(TemplateView):
    template_name = 'webpage_edit.html'

