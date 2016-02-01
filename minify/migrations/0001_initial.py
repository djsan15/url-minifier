# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Domain'
        db.create_table(u'minify_domain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'minify', ['Domain'])

        # Adding model 'URLMinify'
        db.create_table(u'minify_urlminify', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('long_url', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('long_url_domain', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='long_url_domain', null=True, on_delete=models.PROTECT, to=orm['minify.Domain'])),
            ('short_url_domain', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='short_url_domain', null=True, on_delete=models.PROTECT, to=orm['minify.Domain'])),
        ))
        db.send_create_signal(u'minify', ['URLMinify'])


    def backwards(self, orm):
        # Deleting model 'Domain'
        db.delete_table(u'minify_domain')

        # Deleting model 'URLMinify'
        db.delete_table(u'minify_urlminify')


    models = {
        u'minify.domain': {
            'Meta': {'object_name': 'Domain'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'minify.urlminify': {
            'Meta': {'object_name': 'URLMinify'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_url': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'long_url_domain': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'long_url_domain'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['minify.Domain']"}),
            'short_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'short_url_domain': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'short_url_domain'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['minify.Domain']"})
        }
    }

    complete_apps = ['minify']