# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gadgets'
        db.create_table(u'pagemaker_gadgets', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('webpage', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pagemaker.WebPage'], unique=True)),
            ('ident', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('order', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal(u'pagemaker', ['Gadgets'])

        # Deleting field 'MediaFeature.order'
        db.delete_column(u'pagemaker_mediafeature', 'order')

        # Deleting field 'Carousel.order'
        db.delete_column(u'pagemaker_carousel', 'order')

        # Deleting field 'HeadingIcons.order'
        db.delete_column(u'pagemaker_headingicons', 'order')


    def backwards(self, orm):
        # Deleting model 'Gadgets'
        db.delete_table(u'pagemaker_gadgets')

        # Adding field 'MediaFeature.order'
        db.add_column(u'pagemaker_mediafeature', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=0, unique=True),
                      keep_default=False)

        # Adding field 'Carousel.order'
        db.add_column(u'pagemaker_carousel', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=0, unique=True),
                      keep_default=False)

        # Adding field 'HeadingIcons.order'
        db.add_column(u'pagemaker_headingicons', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=0, unique=True),
                      keep_default=False)


    models = {
        u'pagemaker.carousel': {
            'Meta': {'object_name': 'Carousel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'webpage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Carousel'", 'to': u"orm['pagemaker.WebPage']"})
        },
        u'pagemaker.gadgets': {
            'Meta': {'object_name': 'Gadgets'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.IntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'webpage': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pagemaker.WebPage']", 'unique': 'True'})
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        }
    }

    complete_apps = ['pagemaker']