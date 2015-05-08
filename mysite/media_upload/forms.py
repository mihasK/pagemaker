import os
from django import forms
from .settings import *
from .models import Media

def construct_form(**kwargs):
    class MediaForm(forms.ModelForm):
        file = forms.FileField(required=False)

        class Meta:
            fields = ['embedded_video'] + kwargs['form_fields']
            model = kwargs['model']
            widgets = kwargs['form_widgets']

        def clean_file(self):
            file_upload = self.cleaned_data.get('file', None)
            if file_upload:
                name, extension = os.path.splitext(file_upload.name)
                if extension.lower() in IMAGE_EXTENSIONS:
                    self.instance.image = file_upload
                    self.instance.most_recently_updated = 'IMG'
                elif extension.lower() in VIDEO_EXTENSIONS:
                    self.instance.video = file_upload
                    self.instance.most_recently_updated = 'VID'
                    self.instance.video_needs_transcode = True

        def clean_embedded_video(self):
            if self.cleaned_data['embedded_video']:
                self.instance.most_recently_updated = 'EBD'
            return self.cleaned_data['embedded_video']

        def save(self, commit=True):
            media = super(MediaForm, self).save(commit)

            return media


    return MediaForm

