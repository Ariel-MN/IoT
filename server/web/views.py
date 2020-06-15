from django.shortcuts import render, redirect, Http404
from .models import Sensor, Order, Employee
from django.contrib.auth.models import auth
from django.contrib import messages
from datetime import datetime


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            if not username or not password:
                messages.info(request, 'Both the Username and Password are required.')
            else:
                messages.info(request, 'Invalid credentials.')
            return redirect('login')
    else:
        return render(request, 'login.html')


def data(req):
    employees = Employee.objects.all()
    try:
        all_orders = Order.objects.all().order_by('date')
        today = datetime.now()
        name = req.user.get_full_name()
        id = [i.employee_id for i in employees if f'{i.name} {i.lastname}' == name]
        orders = [i for i in all_orders if i.employee_id == id[0] and i.date >= today.date()]
        for i in orders:
            i.date = i.date.strftime('%d/%m/%Y')
        return employees, orders
    except:
        return employees, ''


def home(request):
    if request.method == 'GET':
        employees, orders = data(request)
        return render(request, 'home.html', {'employees': employees, 'orders': orders})


def info(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        find_order = request.POST['find_order']
        find_dustbin = request.POST['find_dustbin']
        find_id = request.POST['find_id']
        if find_order != '':
            try:
                order = Order.objects.get(id=int(find_order))
                order.date = order.date.strftime('%d/%m/%Y')
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
                sensor = Sensor.objects.get(id=int(find_dustbin))
                # Change battery color indicator from: 1 to 20; 21 to 79; 80 to 100
                if sensor.battery < 21:
                    battery_level = 'low'
                elif sensor.battery > 79:
                    battery_level = 'full'
                else:
                    battery_level = 'medium'
                return render(request, 'home.html', {'sensor': sensor, 'level': battery_level, 'employees': employees})
            except Sensor.DoesNotExist:
                raise Http404("Item does not exist")
    else:
        return redirect('home', {'employees': employees})


def inf(request):
    _, orders = data(request)
    if request.method == 'POST':
        find_dustbin = request.POST['find_dustbin']
        find_orders = request.POST['find_orders']
        if find_dustbin != '':
            try:
                sensor = Sensor.objects.get(id=int(find_dustbin))
                # Change battery color indicator from: 1 to 20; 21 to 79; 80 to 100
                if sensor.battery < 21:
                    battery_level = 'low'
                elif sensor.battery > 79:
                    battery_level = 'full'
                else:
                    battery_level = 'medium'
                return render(request, 'home.html', {'sensor': sensor, 'level': battery_level, 'orders': orders})
            except Sensor.DoesNotExist:
                raise Http404("Item does not exist")
        elif find_orders != 'User Orders':
            try:
                id, _ = find_orders.split('#')
                order = Order.objects.get(id=id)
                order.date = order.date.strftime('%d/%m/%Y')
                if order:
                    return render(request, 'home.html', {'order': order, 'orders': orders})
                else:
                    return render(request, 'home.html', {'orders': orders})
            except Order.DoesNotExist:
                raise Http404("Item does not exist")
    else:
        return redirect('home', {'orders': orders})


def logout(request):
    auth.logout(request)
    return redirect('/')
