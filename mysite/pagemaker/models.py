from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify

from colorful.fields import RGBColorField
from embed_video.fields import EmbedVideoField
from .formatChecker import ContentTypeRestrictedFileField


def get_media_image_path(instance, filename):#todo rmw: there has to be a better way
    return os.path.join(str(instance.webpage.pk), 'images', str(instance.pk),filename)

def get_media_video_path(instance, filename):
    return os.path.join(str(instance.webpage.pk), 'videos',  str(instance.pk),filename)

def get_image_path(instance, filename):#todo rmw: there has to be a better way
    return os.path.join(str(instance.pk), 'images',filename)

def get_video_path(instance, filename):
    return os.path.join(str(instance.pk), 'videos', filename)


class WebPage(models.Model):
    base = models.CharField(max_length=127, blank=True)    # base template
    title = models.CharField(max_length=127)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(WebPage, self).save(*args, **kwargs)


class Gadget(models.Model):
    webpage = models.ForeignKey(WebPage)
    order = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True
        #unique_together = ('webpage', 'order')


class Menu(Gadget):
    title = models.CharField(max_length=127)


class MenuItem(models.Model):
    title = models.CharField(max_length=56)
    url = models.URLField()
    sequence = models.IntegerField(unique=True) #order to display menu item
    menu = models.ForeignKey(Menu, related_name = 'Item')


class Carousel(Gadget):
    title = models.CharField(max_length=127, blank=False)


class Slide(models.Model):

    IMAGE_CHOICES = (
        ('STR', 'Stretch'),
        ('CRP', 'Crop'),
        ('TLE', 'Tile')
    )

    title = models.CharField(max_length=127, blank=True)
    description = models.TextField(blank=True)

    button_text = models.CharField('Push', max_length=56, blank=True)
    button_color = RGBColorField(default = '#FFFFFF', blank=True)

    bg_color = RGBColorField(default = '#000000')
    bg_image =  ContentTypeRestrictedFileField(upload_to=get_image_path, blank=True,
                  max_upload_size = 5000000,content_types= settings.SUPPORTED_IMAGE_MIME_TYPES)

    #sequence = models.IntegerField(unique=True) #TODO tk add order of display inside carousel
    carousel = models.ForeignKey(Carousel, related_name = 'Slide')


class MediaFeature(Gadget):
    title = models.CharField(max_length=127, default='Edit Title', blank=True)
    description = models.TextField(default='Edit Description', blank=True)

    image = ContentTypeRestrictedFileField(upload_to=get_image_path, blank=True,
                max_upload_size = 5000000,content_types= settings.SUPPORTED_IMAGE_MIME_TYPES)
    video= ContentTypeRestrictedFileField(upload_to=get_media_video_path,blank=True,
                max_upload_size = 50242880,content_types=settings.SUPPORTED_VIDEO_MIME_TYPES,
                                          default = 'static/default/default.ogv')
    video_needs_transcode = models.BooleanField(default=False)
    embedded_video = EmbedVideoField(blank=True)
    left_media = models.BooleanField(default=False) # display image/video on left side



class HeadingIcons(Gadget):
    title = models.CharField(max_length=127, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=127, blank=True)

    title1 = models.CharField(max_length=127, blank=True)
    description1 = models.TextField(blank=True)
    icon1 = models.CharField(max_length=127, blank=True)

    title2 = models.CharField(max_length=127, blank=True)
    description2 = models.TextField(blank=True)
    icon2 = models.CharField(max_length=127, blank=True)





