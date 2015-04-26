# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WebPage'
        db.create_table(u'pagemaker_webpage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('base', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'pagemaker', ['WebPage'])

        # Adding model 'Gadgets'
        db.create_table(u'pagemaker_gadgets', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('webpage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagemaker.WebPage'])),
            ('identifier', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'pagemaker', ['Gadgets'])

        # Adding unique constraint on 'Gadgets', fields ['webpage', 'order']
        db.create_unique(u'pagemaker_gadgets', ['webpage_id', 'order'])

        # Adding model 'Menu'
        db.create_table(u'pagemaker_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('webpage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Menu', to=orm['pagemaker.WebPage'])),
        ))
        db.send_create_signal(u'pagemaker', ['Menu'])

        # Adding model 'MenuItem'
        db.create_table(u'pagemaker_menuitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=56)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('sequence', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Item', to=orm['pagemaker.Menu'])),
        ))
        db.send_create_signal(u'pagemaker', ['MenuItem'])

        # Adding model 'Carousel'
        db.create_table(u'pagemaker_carousel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('webpage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Carousel', to=orm['pagemaker.WebPage'])),
        ))
        db.send_create_signal(u'pagemaker', ['Carousel'])

        # Adding model 'Slide'
        db.create_table(u'pagemaker_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('button_text', self.gf('django.db.models.fields.CharField')(max_length=56, blank=True)),
            ('button_color', self.gf(u'colorful.fields.RGBColorField')()),
            ('bg_color', self.gf(u'colorful.fields.RGBColorField')()),
            ('bg_image', self.gf('pagemaker.formatChecker.ContentTypeRestrictedFileField')(content_types=['image/png', 'image/gif', 'image/jpeg', 'image/pjpeg'], max_upload_size=5000000, max_length=100, blank=True)),
            ('sequence', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('carousel', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Slide', to=orm['pagemaker.Carousel'])),
        ))
        db.send_create_signal(u'pagemaker', ['Slide'])

        # Adding model 'MediaFeature'
        db.create_table(u'pagemaker_mediafeature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('pagemaker.formatChecker.ContentTypeRestrictedFileField')(content_types=['image/png', 'image/gif', 'image/jpeg', 'image/pjpeg'], max_upload_size=5000000, max_length=100, blank=True)),
            ('video', self.gf('pagemaker.formatChecker.ContentTypeRestrictedFileField')(default='static/default/default.ogv', max_upload_size=50242880, max_length=100, content_types=['video/quicktime', 'video/mpeg', 'video/mp4', 'video/avi', 'video/x-ms-wmv', 'video/x-flv', 'video/3gpp', 'video/webm', 'video/ogg'], blank=True)),
            ('video_needs_transcode', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('embedded_video', self.gf('embed_video.fields.EmbedVideoField')(max_length=200, blank=True)),
            ('left_media', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('webpage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='MediaFeature', to=orm['pagemaker.WebPage'])),
        ))
        db.send_create_signal(u'pagemaker', ['MediaFeature'])

        # Adding model 'HeadingIcons'
        db.create_table(u'pagemaker_headingicons', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title1', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('description1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('icon1', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('title2', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('description2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('icon2', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('title3', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('description3', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('icon3', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('webpage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='HeadingIcons', to=orm['pagemaker.WebPage'])),
        ))
        db.send_create_signal(u'pagemaker', ['HeadingIcons'])


    def backwards(self, orm):
        # Removing unique constraint on 'Gadgets', fields ['webpage', 'order']
        db.delete_unique(u'pagemaker_gadgets', ['webpage_id', 'order'])

        # Deleting model 'WebPage'
        db.delete_table(u'pagemaker_webpage')

        # Deleting model 'Gadgets'
        db.delete_table(u'pagemaker_gadgets')

        # Deleting model 'Menu'
        db.delete_table(u'pagemaker_menu')

        # Deleting model 'MenuItem'
        db.delete_table(u'pagemaker_menuitem')

        # Deleting model 'Carousel'
        db.delete_table(u'pagemaker_carousel')

        # Deleting model 'Slide'
        db.delete_table(u'pagemaker_slide')

        # Deleting model 'MediaFeature'
        db.delete_table(u'pagemaker_mediafeature')

        # Deleting model 'HeadingIcons'
        db.delete_table(u'pagemaker_headingicons')


    models = {
        u'pagemaker.carousel': {
            'Meta': {'object_name': 'Carousel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'webpage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Carousel'", 'to': u"orm['pagemaker.WebPage']"})
        },
        u'pagemaker.gadgets': {
            'Meta': {'unique_together': "(('webpage', 'order'),)", 'object_name': 'Gadgets'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.IntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'webpage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pagemaker.WebPage']"})
        },
        u'pagemaker.headingicons': {
            'Meta': {'object_name': 'HeadingIcons'},
            'description1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description3': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'icon1': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'icon2': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'icon3': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title1': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'title2': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'title3': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'webpage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'HeadingIcons'", 'to': u"orm['pagemaker.WebPage']"})
        },
        u'pagemaker.mediafeature': {
            'Meta': {'object_name': 'MediaFeature'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'embedded_video': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('pagemaker.formatChecker.ContentTypeRestrictedFileField', [], {'content_types': "['image/png', 'image/gif', 'image/jpeg', 'image/pjpeg']", 'max_upload_size': '5000000', 'max_length': '100', 'blank': 'True'}),
            'left_media': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'video': ('pagemaker.formatChecker.ContentTypeRestrictedFileField', [], {'default': "'static/default/default.ogv'", 'max_upload_size': '50242880', 'max_length': '100', 'content_types': "['video/quicktime', 'video/mpeg', 'video/mp4', 'video/avi', 'video/x-ms-wmv', 'video/x-flv', 'video/3gpp', 'video/webm', 'video/ogg']", 'blank': 'True'}),
            'video_needs_transcode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'webpage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'MediaFeature'", 'to': u"orm['pagemaker.WebPage']"})
        },
        u'pagemaker.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'webpage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Menu'", 'to': u"orm['pagemaker.WebPage']"})
        },
        u'pagemaker.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Item'", 'to': u"orm['pagemaker.Menu']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '56'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'pagemaker.slide': {
            'Meta': {'object_name': 'Slide'},
            'bg_color': (u'colorful.fields.RGBColorField', [], {}),
            'bg_image': ('pagemaker.formatChecker.ContentTypeRestrictedFileField', [], {'content_types': "['image/png', 'image/gif', 'image/jpeg', 'image/pjpeg']", 'max_upload_size': '5000000', 'max_length': '100', 'blank': 'True'}),
            'button_color': (u'colorful.fields.RGBColorField', [], {}),
            'button_text': ('django.db.models.fields.CharField', [], {'max_length': '56', 'blank': 'True'}),
            'carousel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Slide'", 'to': u"orm['pagemaker.Carousel']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'})
        },
        u'pagemaker.webpage': {
            'Meta': {'object_name': 'WebPage'},
            'base': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        }
    }

    complete_apps = ['pagemaker']