from django.db import models
from django.template.defaultfilters import slugify


class WebPage(models.Model):
    base = models.CharField(max_length=127, blank=True)    # base template
    title = models.CharField(max_length=127)
    slug = models.SlugField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(WebPage, self).save(*args, **kwargs)

class Menu(models.Model):
    title = models.CharField(max_length=127)
    webpage = models.ForeignKey(WebPage, related_name='carousel')


class MenuItem(models.Model):
    title = models.CharField(max_length=56)
    url = models.URLField()
    sequence = models.IntegerField() #order to display menu item
    menu = models.ForeignKey(Menu, related_name = 'item')


class Carousel(models.Model):
    title = models.CharField(max_length=127, blank=False)
    order = models.IntegerField() #order of display on webpage
    webpage = models.ForeignKey(WebPage, related_name='carousel')


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
    bg_image =  ContentTypeRestrictedFileField(upload_to=get_school_image_path, blank=True,
                  max_upload_size = 5000000,content_types= settings.SUPPORTED_IMAGE_MIME_TYPES)

    sequence = models.IntegerField() #order of display inside carousel
    carousel = models.ForeignKey(Carousel, related_name = 'slide')


class MediaFeature(models.Model):
    title = models.CharField(blank=True)
    description = models.TextField(blank=True)

    image = ContentTypeRestrictedFileField(upload_to=get_school_image_path, blank=True,
                max_upload_size = 5000000,content_types= settings.SUPPORTED_IMAGE_MIME_TYPES)
    video= ContentTypeRestrictedFileField(upload_to=get_school_media_video_path,blank=True,
                max_upload_size = 50242880,content_types=settings.SUPPORTED_VIDEO_MIME_TYPES,
                                          default = 'static/default/default.ogv')
    video_needs_transcode = models.BooleanField(default=False)
    embedded_video = EmbedVideoField(blank=True)
    left_media = models.BooleanField(default=False) # display image/video on left side

    order = models.IntegerField() #order of display on webpage
    webpage = models.ForeignKey(WebPage, related_name='carousel')


class HeadingIcons(models.Model):
    title1 = models.CharField(blank=True)
    description1 = models.TextField(blank=True)
    icon1 = models.CharField(blank=True)

    title2 = models.CharField(blank=True)
    description2 = models.TextField(blank=True)
    icon2 = models.CharField(blank=True)

    title3 = models.CharField(blank=True)
    description3 = models.TextField(blank=True)
    icon3 = models.CharField(blank=True)

    order = models.IntegerField() #order of display on webpage
    webpage = models.ForeignKey(WebPage, related_name='carousel')




