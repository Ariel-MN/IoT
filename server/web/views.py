from django.shortcuts import render
from .models import Sensor, Order, Employee
# Create your views here.


def index(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    return render(request, 'index.html')


def home(request):
    order = Order()
    sensor = Sensor()
    employees = Employee()
    order_upd = Order()

    if request.method == 'POST':
        # Inputs for search
        find_order = request.POST.get('find_order')
        find_dustbin = request.POST.get('find_dustbin')

    # delete after db is config
    sensor.capacity = 10
    sensor.battery = 28
    sensor.number = 1
    sensor.ip = '102.130.2.50'
    sensor.location = 'Central Park Avenue - NY'

    order.number = 1
    order.date = '12/10/2020'
    order.dustbins = 10, 19, 20
    order.employee_id = 1001

    employee1 = Employee()
    employee1.name = 'Alex'
    employee1.lastname = 'Crux'
    employee1.phone = '01 304 954 86'
    employee1.adress = 'Grand Palace, 2 - NY'
    employee1.id = 1001
    employee1.truck = 'NY333D'

    employee2 = Employee()
    employee2.name = 'Brian'
    employee2.lastname = 'Dale'
    employee2.phone = '01 234 765 45'
    employee2.adress = 'Big Plaza, 6 - NY'
    employee2.id = 1002
    employee2.truck = 'NY498A'

    employees = [employee1, employee2]


    # Change battery color indicator
    if sensor.battery <= 20:
        battery_level = 'low'
    elif 20 < sensor.battery <= 80:
        battery_level = 'medium'
    else:
        battery_level = 'full'

    return render(request, 'home.html', {'sensor': sensor, 'order': order, 'order_upd': order_upd, 'employees': employees, 'level': battery_level})


def preview(request):
    order_upd = Order()

    # Inputs for updates
    order_upd.number = request.POST.get('number_upd')
    order_upd.dustbins = request.POST.get('dustbins_upd')
    order_upd.employee_id = request.POST.get('employee_upd')
    order_upd.date = request.POST.get('date_upd')

    return render(request, 'home.html', {'order_upd': order_upd})
