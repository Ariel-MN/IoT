from django.shortcuts import render, redirect, Http404
from .models import Sensor, Order, Employee, Responsable
from django.contrib.auth.models import auth
from django.contrib import messages
from datetime import datetime, timedelta


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


def resposable():
    resp_name = ""
    resp_phone = ""

    resp = Responsable.objects.first()
    if resp:
        resp_name = resp.user.get_full_name()
        resp_phone = Employee.objects.get(user=resp.user).phone
    return resp_name, resp_phone


def data(req):
    employees = Employee.objects.all().exclude(employee_id=0)
    yesterday = datetime.now() - timedelta(days=1)
    orders = ""

    try:
        id = Employee.objects.get(user=req.user).employee_id
        if id:
            orders = Order.objects.all().filter(employee_id=id).order_by('date').exclude(date__lte=yesterday.date())
            for i in orders:
                i.date = i.date.strftime('%d/%m/%Y')
        return employees, orders
    except:
        return employees, orders


def home(request):
    if request.method == 'GET':
        employees, orders = data(request)
        resp_name, resp_phone = resposable()
        return render(request, 'home.html', {'employees': employees, 'orders': orders, 'resp_name': resp_name, 'resp_phone': resp_phone})


def info(request):
    employees = Employee.objects.all().exclude(employee_id=0)
    yesterday = datetime.now() - timedelta(days=1)
    resp_name, resp_phone = resposable()

    if request.method == 'POST':
        find_order = request.POST['find_order']
        find_dustbin = request.POST['find_dustbin']
        find_id = request.POST['find_id']
        if find_order != '':
            try:
                order = Order.objects.get(id=int(find_order))
                order.date = order.date.strftime('%d/%m/%Y')
                if order:
                    return render(request, 'home.html', {'order': order, 'employees': employees, 'resp_name': resp_name, 'resp_phone': resp_phone})
                else:
                    return render(request, 'home.html', {'employees': employees, 'resp_name': resp_name, 'resp_phone': resp_phone})
            except Order.DoesNotExist:
                return render(request, 'home.html', {'employees': employees, 'resp_name': resp_name, 'resp_phone': resp_phone, 'message': 'find_order'})
        elif find_id != 'Employee ID':
            try:
                order = Order.objects.all().filter(employee_id=int(find_id)).order_by('date').exclude(date__lte=yesterday.date())
                if order:
                    order[0].date = order[0].date.strftime('%d/%m/%Y')
                    return render(request, 'home.html', {'order': order[0], 'employees': employees, 'resp_name': resp_name, 'resp_phone': resp_phone})
                else:
                    return render(request, 'home.html', {'employees': employees, 'resp_name': resp_name, 'resp_phone': resp_phone})
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
                return render(request, 'home.html', {'sensor': sensor, 'level': battery_level, 'employees': employees, 'resp_name': resp_name, 'resp_phone': resp_phone})
            except Sensor.DoesNotExist:
                return render(request, 'home.html', {'employees': employees, 'resp_name': resp_name, 'resp_phone': resp_phone, 'message': 'find_dustbin'})
                # raise Http404("Item does not exist")
    else:
        return redirect('home', {'employees': employees, 'resp_name': resp_name, 'resp_phone': resp_phone})


def inf(request):
    _, orders = data(request)
    resp_name, resp_phone = resposable()
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
                return render(request, 'home.html', {'sensor': sensor, 'level': battery_level, 'orders': orders, 'resp_name': resp_name, 'resp_phone': resp_phone})
            except Sensor.DoesNotExist:
                return render(request, 'home.html', {'orders': orders, 'resp_name': resp_name, 'resp_phone': resp_phone, 'message': 'find_dustbin'})
        elif find_orders != 'User Orders':
            try:
                id, _ = find_orders.split('#')
                order = Order.objects.get(id=id)
                order.date = order.date.strftime('%d/%m/%Y')
                if order:
                    return render(request, 'home.html', {'order': order, 'orders': orders, 'resp_name': resp_name, 'resp_phone': resp_phone})
                else:
                    return render(request, 'home.html', {'orders': orders, 'resp_name': resp_name, 'resp_phone': resp_phone})
            except Order.DoesNotExist:
                raise Http404("Item does not exist")
    else:
        return redirect('home', {'orders': orders, 'resp_name': resp_name, 'resp_phone': resp_phone})


def logout(request):
    auth.logout(request)
    return redirect('/')
