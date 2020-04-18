from django.shortcuts import render, Http404
from .models import Sensor, Order, Employee
# Create your views here.


def index(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    return render(request, 'index.html')


def home(request):
    employees = Employee.objects.all()

    return render(request, 'home.html', {'employees': employees})


def info(request):
    employees = Employee.objects.all()

    if request.method == 'POST':
        # Inputs for search
        find_order = request.POST['find_order']
        find_dustbin = request.POST['find_dustbin']
        find_id = request.POST['find_id']

        if find_order != '':
            find_order = int(find_order)
            try:
                order = Order.objects.get(number=find_order)
            except Order.DoesNotExist:
                raise Http404("Item does not exist")
            return render(request, 'home.html', {'order': order, 'employees': employees})

        elif find_id != 'Employee ID':
            find_id = int(find_id)
            try:
                order = Order.objects.get(employee_id=find_id)
            except Order.DoesNotExist:
                raise Http404("Item does not exist")
            return render(request, 'home.html', {'order': order, 'employees': employees})

        elif find_dustbin != '':
            find_dustbin = int(find_dustbin)
            try:
                sensor = Sensor.objects.get(number=find_dustbin)
            except Sensor.DoesNotExist:
                raise Http404("Item does not exist")

            battery_level = ''
            if sensor:
                # Change battery color indicator   TODO: MOVE THIS TO JS
                if sensor.battery <= 20:
                    battery_level = 'low'
                elif 20 < sensor.battery <= 80:
                    battery_level = 'medium'
                else:
                    battery_level = 'full'

                return render(request, 'home.html', {'sensor': sensor, 'level': battery_level, 'employees': employees})
