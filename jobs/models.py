from django.db import models
import datetime

class Address(models.Model):
	number = models.CharField(max_length=10)
	street = models.CharField(max_length=50)
	street_type_choices = (
		('st', 'Street'),
		('rd', 'Road'),
		('av', 'Avenue'),
		('cs', 'Crescent'),
		('bv', 'Boulevard'),
	)
	street_type = models.CharField(max_length=2, choices=street_type_choices)
	suburb = models.CharField(max_length=30,blank=True)
	city = models.CharField(max_length=30)

	def __unicode__(self):
		address_string = self.number + self.street + self.street_type
		return address_string

class Client(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(blank=True)
	address = models.OneToOneField(Address,blank=True)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

class Job(models.Model):
	client = models.ForeignKey(Client)
	address = models.OneToOneField(Address)
	budget = models.IntegerField(blank=True)
	estimated_cost = models.IntegerField(blank=True)

class Event(models.Model):
	status_choices = (
		('pr', 'Priced'),
		('sl', 'Sold'),
		('ds', 'Designed'),
		('ws', 'Work Started'),
		('wf', 'Work Finished'),
	)
	status = models.CharField(max_length=2, choices=status_choices)
	date = models.DateField()
	job = models.ForeignKey(Job)

