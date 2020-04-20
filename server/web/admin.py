from django.contrib import admin
from .models import Sensor, Order, Employee
from django.contrib.auth.models import Group

admin.site.site_header = 'Administration Panel'
admin.site.site_title = 'Dustbin IoT'
admin.site.index_title = 'Admin'
admin.site.site_url = '/home/'

admin.site.register([Sensor, Order, Employee])
admin.site.unregister(Group)
