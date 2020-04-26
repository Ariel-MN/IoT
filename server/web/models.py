from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class Sensor(models.Model):
    capacity = models.IntegerField()
    battery = models.IntegerField()
    ip = models.GenericIPAddressField()
    location = models.CharField(max_length=200)


class Order(models.Model):
    date = models.DateField()
    dustbins = models.TextField()
    employee_id = models.IntegerField()


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=200, default='')
    truck = models.CharField(max_length=15, default='')
    employee_id = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
