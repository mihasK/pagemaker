from django import forms
from pagemaker.models import *


class WebPageCreateForm(forms.ModelForm):
    class Meta:
        model = WebPage

        fields = ['title']

