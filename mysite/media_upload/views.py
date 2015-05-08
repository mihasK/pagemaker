from django.views.generic import UpdateView , CreateView ,View
from django.core.urlresolvers import reverse
from .forms import construct_form

class MediaBaseView(View):
    template_name = 'base.html'

    def get_form_class(self):
        form_class = construct_form(model = self.model, form_fields = self.form_fields, form_widgets = self.form_widgets)
        return form_class

    def get_success_url(self):
        return reverse(self.request.resolver_match.url_name, kwargs=self.request.resolver_match.kwargs)

    def get_context_data(self, **kwargs):
        context = super(MediaBaseView, self).get_context_data(**kwargs)
        context['form_url'] = self.request.resolver_match.url_name

        for key , value in self.kwargs.iteritems():
            context[key] = value

        return context

class MediaCreateView(MediaBaseView, CreateView):
    pass

class MediaUpdateView(MediaBaseView, UpdateView):
    pass