from django.contrib import admin
from .models import Sensor, Order, Employee

# Register your models here.
myModels = [Sensor, Order, Employee]

admin.site.register(myModels)
