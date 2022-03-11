from genericpath import exists
from multiprocessing import context
from black import nullcontext
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import*
import csv
import random
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/')

        login(request, user)
        return redirect('/home')

    return render(request, 'warehouse/login.html')


def home_view(request):
    return render(request, 'warehouse/home.html')

@login_required(login_url='login')
def customer_search_view(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_id = request.POST.get('customer_id')
        if customer_name != '' and customer_id != '':
            ware_house_obj = ware_house_model.objects.filter(
                customer_name=customer_name, customer_id=customer_id)
            if ware_house_obj.exists():
                
                context = {'ware_house_obj': ware_house_obj}
                return render(request, 'warehouse/customer.html', context)
            else:
                messages.success(request, 'Your Entered Data not matched.')
                return redirect( '/customer_search')
        if customer_name != '' and customer_id == '':
            ware_house_obj = ware_house_model.objects.filter(
                customer_name=customer_name)
            if ware_house_obj.exists():
                
                context = {'ware_house_obj': ware_house_obj}
                return render(request, 'warehouse/customer.html', context)
            else:
                messages.success(request, 'Your Entered Data not matched.')
                return redirect( '/customer_search')
        if customer_name == '' and customer_id != '':
            ware_house_obj = ware_house_model.objects.filter(
                customer_id=customer_id)
            if ware_house_obj.exists():
                
                context = {'ware_house_obj': ware_house_obj}
                return render(request, 'warehouse/customer.html', context)
            else:
                messages.success(request, 'Your Entered Data not matched.')
                return redirect( '/customer_search')

    return render(request, 'warehouse/customer_search.html')

@login_required(login_url='login')
def product_search_view(request):
    if request.method == 'POST':
        product_description = request.POST.get('description')
        serial_number = request.POST.get('serial_number')
        print('descripton', product_description)
        if product_description != '' and serial_number != '':

            ware_house_obj = ware_house_model.objects.filter( description=product_description, serial_number=serial_number)
            if ware_house_obj.exists():
                
                context = {'ware_house_obj': ware_house_obj}
                return render(request, 'warehouse/customer.html', context)
            else:
                messages.success(request, 'Your Entered Data not matched.')
                return redirect( '/product_search')

        if product_description != '' and serial_number == '':
            ware_house_obj = ware_house_model.objects.filter(
                description=product_description)
            print('------------------------')
            if ware_house_obj.exists():
                
                context = {'ware_house_obj': ware_house_obj}
                return render(request, 'warehouse/customer.html', context)
            else:
                messages.success(request, 'Your Entered Data not matched.')
                return redirect( '/product_search')
        if product_description == '' and serial_number != '':
            ware_house_obj = ware_house_model.objects.filter(
                serial_number=serial_number)
            if ware_house_obj.exists():
                
                context = {'ware_house_obj': ware_house_obj}
                return render(request, 'warehouse/customer.html', context)
            else:
                messages.success(request, 'Your Entered Data not matched.')
                return redirect( '/product_search')

    return render(request, 'warehouse/product_search.html')


def customer_view(request):
    return render(request, 'warehouse/customer.html')


def warehouse_view(request):
    return render(request, 'warehouse/warehouse_data.html')

@login_required(login_url='login')
def options_view(request):
    all_data = ware_house_model.objects.all()
    list_of_warehouses = []
    for row in all_data:
        location = row.warehouse
        if location in list_of_warehouses:
            print('if statement executed')
        else:

            list_of_warehouses.append(location)
            print('not in location', location)

    print(list_of_warehouses)
    if request.method == 'POST':
        warehouse_no = request.POST.get('storage_name')
        print('storage name:', warehouse_no)
        all_warehouse_data = ware_house_model.objects.filter(
            warehouse=warehouse_no)
        context = {'all_warehouse_data': all_warehouse_data,
                   'warehouse_no': warehouse_no}
        return render(request, 'warehouse/warehouse_data.html', context)

    context = {'list_of_warehouses': list_of_warehouses}
    return render(request, 'warehouse/warehouse_options.html', context)


def export_warehouse_details(request):
    print('export view')
    list_of_data = []
    if request.method == 'POST':
        input_serials = request.POST.get('serial_numbers')
        print(' input serials:', input_serials)
        serial_number = input_serials.split(",")
        length = len(serial_number)
        list_of_data = []
        print('serials', serial_number[0])
        for i in range(length):
            if serial_number[i] != "":
                print(serial_number[i])
                data = ware_house_model.objects.get(serial_number=serial_number[i])

                list_of_data.append({"customer_name": data.customer_name, 'customer_id': data.customer_id, 'serial_number': data.serial_number, 'height': data.height, 'width': data.width,
                                     'length': data.length, 'storage_space': data.storage_space, 'weight': data.weight, 'storage_name': data.storage_name, 'locate': data.locate, 'date': data.date, 'description': data.description, 'quantity': data.quantity, 'warehouse': data.warehouse})
                print('********************')
                print('list:', list_of_data)
                print('data:')
        n = random.randint(0,10000)
        if list_of_data:
            keys = list_of_data[0].keys()

            with open('warehouse'+str(n)+'.csv', 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(list_of_data)

        print(len(serial_number))
        return redirect('/options')
    return render(request, 'warehouse/warehouse_options.html')


def export_customer(request):
    print('export view')
    list_of_data = []
    n = 0
    if request.method == 'POST':
        input_serials = request.POST.get('serial_numbers')
        print(' input serials:', input_serials)
        serial_number = input_serials.split(",")
        length = len(serial_number)
        list_of_data = []
        print('serials', serial_number[0])
        for i in range(length):
            if serial_number[i] != "":
                print(serial_number[i])
                data = ware_house_model.objects.get(serial_number=serial_number[i])

                list_of_data.append({"customer_name": data.customer_name, 'customer_id': data.customer_id, 'serial_number': data.serial_number, 'height': data.height, 'width': data.width,
                                     'length': data.length, 'storage_space': data.storage_space, 'weight': data.weight, 'storage_name': data.storage_name, 'locate': data.locate, 'date': data.date, 'description': data.description, 'quantity': data.quantity, 'warehouse': data.warehouse})
                print('********************')
                print('list:', list_of_data)
                print('data:')
        n = random.randint(0,10000)
        print('************************')
        print('random', n)
        
        if list_of_data:
            keys = list_of_data[0].keys()

            with open('customer'+str(n)+'.csv' , 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(list_of_data)

        print(len(serial_number))
        return redirect('/home')
    
    return render(request, 'warehouse/warehouse_options.html')
