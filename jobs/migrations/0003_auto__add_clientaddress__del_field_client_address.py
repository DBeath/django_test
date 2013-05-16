# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClientAddress'
        db.create_table(u'jobs_clientaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jobs.Client'])),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jobs.Address'])),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'jobs', ['ClientAddress'])

        # Deleting field 'Client.address'
        db.delete_column(u'jobs_client', 'address_id')


    def backwards(self, orm):
        # Deleting model 'ClientAddress'
        db.delete_table(u'jobs_clientaddress')

        # Adding field 'Client.address'
        db.add_column(u'jobs_client', 'address',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jobs.Address'], null=True, blank=True),
                      keep_default=False)


    models = {
        u'jobs.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'street_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'jobs.client': {
            'Meta': {'object_name': 'Client'},
            'address': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['jobs.Address']", 'null': 'True', 'through': u"orm['jobs.ClientAddress']", 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'jobs.clientaddress': {
            'Meta': {'object_name': 'ClientAddress'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jobs.Address']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jobs.Client']"}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'jobs.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jobs.Job']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'jobs.job': {
            'Meta': {'object_name': 'Job'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jobs.Address']"}),
            'budget': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jobs.Client']"}),
            'estimated_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['jobs']