# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'URLMinify.short_url'
        db.alter_column(u'minify_urlminify', 'short_url', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

    def backwards(self, orm):

        # Changing field 'URLMinify.short_url'
        db.alter_column(u'minify_urlminify', 'short_url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    models = {
        u'minify.domain': {
            'Meta': {'object_name': 'Domain'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'minify.urlminify': {
            'Meta': {'unique_together': "(('short_url', 'short_url_domain'),)", 'object_name': 'URLMinify'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_url': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'long_url_domain': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'long_url_domain'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['minify.Domain']"}),
            'short_url': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'short_url_domain': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'short_url_domain'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['minify.Domain']"})
        }
    }

    complete_apps = ['minify']