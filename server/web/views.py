from django.shortcuts import render, redirect, Http404
from .models import Sensor, Order, Employee
from django.contrib.auth.models import auth
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/')

    else:
        return render(request, 'index.html')


def home(request):
    if request.method == 'GET':
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
            try:
                order = Order.objects.get(number=int(find_order))
                return render(request, 'home.html', {'order': order, 'employees': employees})
            except Order.DoesNotExist:
                raise Http404("Item does not exist")

        elif find_id != 'Employee ID':
            try:
                order = Order.objects.get(employee_id=int(find_id))
                return render(request, 'home.html', {'order': order, 'employees': employees})
            except Order.DoesNotExist:
                raise Http404("Item does not exist")

        elif find_dustbin != '':
            try:
                sensor = Sensor.objects.get(number=int(find_dustbin))
                # Change battery color indicator
                if sensor.battery <= 20:
                    battery_level = 'low'
                elif 20 < sensor.battery <= 80:
                    battery_level = 'medium'
                else:
                    battery_level = 'full'
                return render(request, 'home.html', {'sensor': sensor, 'level': battery_level, 'employees': employees})
            except Sensor.DoesNotExist:
                raise Http404("Item does not exist")

    else:
        return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('/')
