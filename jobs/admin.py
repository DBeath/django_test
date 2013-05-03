from django.contrib import admin
from jobs.models import Client, Job, Address

admin.site.register(Client)
admin.site.register(Job)
admin.site.register(Address)