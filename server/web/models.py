from django.db import models


class Sensor(models.Model):
    capacity = models.IntegerField()
    battery = models.IntegerField()
    number = models.IntegerField()
    ip = models.GenericIPAddressField()
    location = models.CharField(max_length=200)


class Order(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    dustbins = models.TextField()
    employee_id = models.IntegerField()


class Employee(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=200)
    truck = models.CharField(max_length=15)
    employee_id = models.IntegerField()
