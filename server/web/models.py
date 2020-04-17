from django.db import models

# Create your models here.


class Sensor:
    capacity: int
    battery: int
    number: int
    ip: str
    location: str


class Order:
    number: int
    date: str
    dustbins: str
    employee_id: int


class Employee:
    name: str
    lastname: str
    phone: str
    adress: str
    id: int
    truck: str
