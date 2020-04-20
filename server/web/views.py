from django.shortcuts import render, redirect, Http404
from .models import Sensor, Order, Employee
from django.contrib.auth.models import auth
from django.contrib import messages
from datetime import datetime


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
        find_order = request.POST['find_order']
        find_dustbin = request.POST['find_dustbin']
        find_id = request.POST['find_id']

        #  TODO: ogni utente deve vedere tutti i suoi ordini, ordinati per data su un nuovo <select> nel template
        # orders = Order.objects.all().order_by('date')
        # order = [i for i in all_orders if i.employee_id == int(find_id) and i.date >= today.date()]

        if find_order != '':
            try:
                order = Order.objects.get(number=int(find_order))
                if order:
                    return render(request, 'home.html', {'order': order, 'employees': employees})
                else:
                    return render(request, 'home.html', {'employees': employees})
            except Order.DoesNotExist:
                raise Http404("Item does not exist")

        elif find_id != 'Employee ID':
            try:
                today = datetime.now()
                all_orders = Order.objects.all().order_by('date')
                order = [i for i in all_orders if i.employee_id == int(find_id) and i.date >= today.date()]  # find closest date
                order[0].date = order[0].date.strftime('%d/%m/%Y')
                if order:
                    return render(request, 'home.html', {'order': order[0], 'employees': employees})
                else:
                    return render(request, 'home.html', {'employees': employees})
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
