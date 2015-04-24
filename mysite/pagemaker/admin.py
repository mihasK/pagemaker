from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(WebPage)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Carousel)
admin.site.register(Slide)
admin.site.register(MediaFeature)
admin.site.register(HeadingIcons)
