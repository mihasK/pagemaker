import os , errno

from django.core.files.storage import default_storage
from django.db import models

from .settings import *

def silent_remove_file(filename):
    try:
        os.remove(filename)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise

def image_or_video(filename):
    extension = os.path.splitext(filename)[1]
    if extension in IMAGE_EXTENSIONS:
        return 'images'
    if extension in VIDEO_EXTENSIONS:
        return 'videos'

def file_cleanup(sender, **kwargs):
    for fieldname in sender._meta.get_all_field_names():
        try:
            field = sender._meta.get_field(fieldname)
        except:
            field = None
        if field and isinstance(field, models.FileField):
            instance = kwargs['instance']
            file = getattr(instance, fieldname)
            manager = instance.__class__._default_manager
            if hasattr(file, 'path') and os.path.exists(file.path)\
                and not manager.filter(**{'%s__exact' % fieldname: getattr(instance, fieldname)})\
                .exclude(pk=instance._get_pk_val()):
                    try:
                        default_storage.delete(file.path)
                    except Exception as e:
                        test = e