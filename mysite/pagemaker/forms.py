from django import forms
from pagemaker.models import *


class WebPageAddForm(forms.ModelForm):
    class Meta:
        model = WebPage

        fields = ['title']


class CarouselAddForm(forms.ModelForm):
    class Meta:
        model = Carousel

        fields = ['title']

