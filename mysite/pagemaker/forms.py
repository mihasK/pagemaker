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


class HeadingIconsAddForm(forms.ModelForm):
    class Meta:
        model = HeadingIcons

        fields = ['title', 'description', 'title1', 'description1', 'title2', 'description2']


class MediaFeatureAddForm(forms.ModelForm):
    class Meta:
        model = MediaFeature

        fields = ['title', 'description']

        widgets = {'title':forms.HiddenInput(attrs={'class':'mediafeature_title'}),
                   'description':forms.HiddenInput(attrs={'class':'mediafeature_description'})
                   }