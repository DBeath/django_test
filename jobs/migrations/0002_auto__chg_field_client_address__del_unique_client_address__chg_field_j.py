# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Job', fields ['address']
        db.delete_unique(u'jobs_job', ['address_id'])

        # Removing unique constraint on 'Client', fields ['address']
        db.delete_unique(u'jobs_client', ['address_id'])


        # Changing field 'Client.address'
        db.alter_column(u'jobs_client', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jobs.Address'], null=True))

        # Changing field 'Job.address'
        db.alter_column(u'jobs_job', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jobs.Address']))

    def backwards(self, orm):

        # Changing field 'Client.address'
        db.alter_column(u'jobs_client', 'address_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['jobs.Address'], unique=True, null=True))
        # Adding unique constraint on 'Client', fields ['address']
        db.create_unique(u'jobs_client', ['address_id'])


        # Changing field 'Job.address'
        db.alter_column(u'jobs_job', 'address_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['jobs.Address'], unique=True))
        # Adding unique constraint on 'Job', fields ['address']
        db.create_unique(u'jobs_job', ['address_id'])


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
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jobs.Address']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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