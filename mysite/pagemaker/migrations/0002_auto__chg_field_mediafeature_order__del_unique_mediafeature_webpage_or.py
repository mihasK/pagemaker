# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Menu', fields ['webpage', 'order']
        db.delete_unique(u'pagemaker_menu', ['webpage_id', 'order'])

        # Removing unique constraint on 'HeadingIcons', fields ['webpage', 'order']
        db.delete_unique(u'pagemaker_headingicons', ['webpage_id', 'order'])

        # Removing unique constraint on 'Carousel', fields ['webpage', 'order']
        db.delete_unique(u'pagemaker_carousel', ['webpage_id', 'order'])

        # Removing unique constraint on 'MediaFeature', fields ['webpage', 'order']
        db.delete_unique(u'pagemaker_mediafeature', ['webpage_id', 'order'])


        # Changing field 'MediaFeature.order'
        db.alter_column(u'pagemaker_mediafeature', 'order', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Carousel.order'
        db.alter_column(u'pagemaker_carousel', 'order', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'HeadingIcons.order'
        db.alter_column(u'pagemaker_headingicons', 'order', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Menu.order'
        db.alter_column(u'pagemaker_menu', 'order', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'MediaFeature.order'
        db.alter_column(u'pagemaker_mediafeature', 'order', self.gf('django.db.models.fields.IntegerField')(default=0))
        # Adding unique constraint on 'MediaFeature', fields ['webpage', 'order']
        db.create_unique(u'pagemaker_mediafeature', ['webpage_id', 'order'])


        # Changing field 'Carousel.order'
        db.alter_column(u'pagemaker_carousel', 'order', self.gf('django.db.models.fields.IntegerField')(default=0))
        # Adding unique constraint on 'Carousel', fields ['webpage', 'order']
        db.create_unique(u'pagemaker_carousel', ['webpage_id', 'order'])


        # Changing field 'HeadingIcons.order'
        db.alter_column(u'pagemaker_headingicons', 'order', self.gf('django.db.models.fields.IntegerField')(default=0))
        # Adding unique constraint on 'HeadingIcons', fields ['webpage', 'order']
        db.create_unique(u'pagemaker_headingicons', ['webpage_id', 'order'])


        # Changing field 'Menu.order'
        db.alter_column(u'pagemaker_menu', 'order', self.gf('django.db.models.fields.IntegerField')(default=0))
        # Adding unique constraint on 'Menu', fields ['webpage', 'order']
        db.create_unique(u'pagemaker_menu', ['webpage_id', 'order'])


    models = {
        u'pagemaker.carousel': {
            'Meta': {'object_name': 'Carousel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'webpage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pagemaker.WebPage']"})
        },
        u'pagemaker.headingicons': {
            'Meta': {'object_name': 'HeadingIcons'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'icon1': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'icon2': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'title1': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'title2': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'webpage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pagemaker.WebPage']"})
        },
        u'pagemaker.mediafeature': {
            'Meta': {'object_name': 'MediaFeature'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'embedded_video': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('pagemaker.formatChecker.ContentTypeRestrictedFileField', [], {'content_types': "['image/png', 'image/gif', 'image/jpeg', 'image/pjpeg']", 'max_upload_size': '5000000', 'max_length': '100', 'blank': 'True'}),
            'left_media': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'video': ('pagemaker.formatChecker.ContentTypeRestrictedFileField', [], {'default': "'static/default/default.ogv'", 'max_upload_size': '50242880', 'max_length': '100', 'content_types': "['video/quicktime', 'video/mpeg', 'video/mp4', 'video/avi', 'video/x-ms-wmv', 'video/x-flv', 'video/3gpp', 'video/webm', 'video/ogg']", 'blank': 'True'}),
            'video_needs_transcode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'webpage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pagemaker.WebPage']"})
        },
        u'pagemaker.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'webpage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pagemaker.WebPage']"})
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