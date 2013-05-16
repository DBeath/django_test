# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table(u'jobs_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('street_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('suburb', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'jobs', ['Address'])

        # Adding model 'Client'
        db.create_table(u'jobs_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['jobs.Address'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'jobs', ['Client'])

        # Adding model 'Job'
        db.create_table(u'jobs_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jobs.Client'])),
            ('address', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['jobs.Address'], unique=True)),
            ('budget', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('estimated_cost', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'jobs', ['Job'])

        # Adding model 'Event'
        db.create_table(u'jobs_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jobs.Job'])),
        ))
        db.send_create_signal(u'jobs', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table(u'jobs_address')

        # Deleting model 'Client'
        db.delete_table(u'jobs_client')

        # Deleting model 'Job'
        db.delete_table(u'jobs_job')

        # Deleting model 'Event'
        db.delete_table(u'jobs_event')


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
            'address': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['jobs.Address']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
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
            'address': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['jobs.Address']", 'unique': 'True'}),
            'budget': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jobs.Client']"}),
            'estimated_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['jobs']