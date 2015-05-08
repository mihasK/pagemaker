import os
from django.db import models
from django.db.models.signals import post_delete , post_save

from .formatChecker import ContentTypeRestrictedFileField
from embed_video.fields import EmbedVideoField
from .signals import file_cleanup_signal, route_to_transcoder_signal
from .settings import *
from .utils import image_or_video

def get_base_pk(instance, lookup_list):
    old = [instance]
    for attr_string in lookup_list:
        obj = old[-1]
        attr = getattr(obj, attr_string)
        old.append(attr)
    return old[-1]

def get_media_path(instance,filename):
    type = image_or_video(filename)
    custom_paths = os.path.join(*instance.paths)
    base_pk = get_base_pk(instance, instance.base_path_pk_lookup )
    return os.path.join(str(base_pk), custom_paths, str(instance.pk), type, filename)

class Media(models.Model):
    most_recently_updated_choices = (
        ('IMG','Image'),
        ('VID','Video'),
        ('EBD','Embedded Video')
    )

    image = ContentTypeRestrictedFileField(upload_to=get_media_path, null=True, blank=True, max_upload_size = 5000000,content_types= SUPPORTED_IMAGE_MIME_TYPES)
    video= ContentTypeRestrictedFileField(upload_to=get_media_path, null=True, blank=True,max_upload_size = 50242880,content_types=SUPPORTED_VIDEO_MIME_TYPES)
    video_needs_transcode = models.BooleanField(default=False)
    embedded_video = EmbedVideoField(blank=True, null=True)
    most_recently_updated = models.CharField(max_length=3, choices=most_recently_updated_choices)

    class Meta:
        abstract = True

post_save.connect(route_to_transcoder_signal)
post_delete.connect(file_cleanup_signal)