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


class SlideAddForm(forms.ModelForm):
    class Meta:
        model = Slide

        fields = ['title', 'description']


class MediaFeatureAddForm(forms.ModelForm):
    class Meta:
        model = MediaFeature

        fields = ['title', 'description']