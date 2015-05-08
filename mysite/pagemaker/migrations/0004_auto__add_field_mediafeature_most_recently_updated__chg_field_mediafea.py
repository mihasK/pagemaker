# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MediaFeature.most_recently_updated'
        db.add_column(u'pagemaker_mediafeature', 'most_recently_updated',
                      self.gf('django.db.models.fields.CharField')(default='EBD', max_length=3),
                      keep_default=False)


        # Changing field 'MediaFeature.image'
        db.alter_column(u'pagemaker_mediafeature', 'image', self.gf('media_upload.formatChecker.ContentTypeRestrictedFileField')(content_types=['image/png', 'image/gif', 'image/jpeg', 'image/pjpeg'], max_upload_size=5000000, null=True, max_length=100))

        # Changing field 'MediaFeature.embedded_video'
        db.alter_column(u'pagemaker_mediafeature', 'embedded_video', self.gf('embed_video.fields.EmbedVideoField')(max_length=200, null=True))

        # Changing field 'MediaFeature.video'
        db.alter_column(u'pagemaker_mediafeature', 'video', self.gf('media_upload.formatChecker.ContentTypeRestrictedFileField')(content_types=['video/quicktime', 'video/mpeg', 'video/mp4', 'video/avi', 'video/x-ms-wmv', 'video/x-flv', 'video/3gpp', 'video/webm', 'video/ogg'], max_upload_size=50242880, null=True, max_length=100))

    def backwards(self, orm):
        # Deleting field 'MediaFeature.most_recently_updated'
        db.delete_column(u'pagemaker_mediafeature', 'most_recently_updated')


        # Changing field 'MediaFeature.image'
        db.alter_column(u'pagemaker_mediafeature', 'image', self.gf('pagemaker.formatChecker.ContentTypeRestrictedFileField')(content_types=['image/png', 'image/gif', 'image/jpeg', 'image/pjpeg'], max_upload_size=5000000, default=' ', max_length=100))

        # Changing field 'MediaFeature.embedded_video'
        db.alter_column(u'pagemaker_mediafeature', 'embedded_video', self.gf('embed_video.fields.EmbedVideoField')(default='', max_length=200))

        # Changing field 'MediaFeature.video'
        db.alter_column(u'pagemaker_mediafeature', 'video', self.gf('pagemaker.formatChecker.ContentTypeRestrictedFileField')(max_upload_size=50242880, max_length=100, content_types=['video/quicktime', 'video/mpeg', 'video/mp4', 'video/avi', 'video/x-ms-wmv', 'video/x-flv', 'video/3gpp', 'video/webm', 'video/ogg']))

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
            'description': ('django.db.models.fields.TextField', [], {'default': "'Edit Description'", 'blank': 'True'}),
            'embedded_video': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('media_upload.formatChecker.ContentTypeRestrictedFileField', [], {'content_types': "['image/png', 'image/gif', 'image/jpeg', 'image/pjpeg']", 'max_upload_size': '5000000', 'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'left_media': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'most_recently_updated': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Edit Title'", 'max_length': '127', 'blank': 'True'}),
            'video': ('media_upload.formatChecker.ContentTypeRestrictedFileField', [], {'content_types': "['video/quicktime', 'video/mpeg', 'video/mp4', 'video/avi', 'video/x-ms-wmv', 'video/x-flv', 'video/3gpp', 'video/webm', 'video/ogg']", 'max_upload_size': '50242880', 'null': 'True', 'max_length': '100', 'blank': 'True'}),
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