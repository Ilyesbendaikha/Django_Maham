from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import register,addorder,addcustomer,addoffer
from .models import *
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group
# Create your views here.

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            message = messages.info(request,'Password Or Username Incorrect')

    return render(request,'login/login.html')


@unauthenticated_user
def registerpage(request):
    form = register()
    if request.method == 'POST':
        form = register(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            message = messages.success(request,'Account Created Succesfully')
            group = Group.objects.get(name='admin')
            user.groups.add(group)
            return redirect('login')
    context={'form':form}
    return render(request,'login/signup.html',context)

def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def addorders(request):
    form = addorder()
    if request.method == 'POST':
        form = addorder(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request,'main/addorder.html',context)

@login_required(login_url='login')
def home(request):
    orders = order.objects.all()
    order_count = order.objects.count()
    clients = client.objects.count()
    context = {'orders' : orders,'count':order_count,'count_client':clients}
    return render(request,'main/home.html',context)

def update_order(request,pk):
    old = order.objects.get(id=pk)
    form = addorder(instance=old)
    if request.method == 'POST':
        form = addorder(request.POST, instance=old)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request,'main/addorder.html',context)

def delete_order(request,pk):
    deleted = order.objects.get(id=pk)
    if request.method == 'POST':
        deleted.delete()
        return redirect('home')
    
    context = {'delete':deleted}

    return render(request,'main/delete_order.html',context)

@login_required(login_url='login')
def showcustomers(request):
    clients = client.objects.all()
    client_count = client.objects.count()
    context = {'client' : clients ,'count':client_count}

    return render(request,'show/showcustomer.html',context)

@login_required(login_url='login')
def addcustomers(request):
    form = addcustomer()
    if request.method == 'POST':
        form = addcustomer(request.POST)
        username = request.POST.get('name')
        if form.is_valid():
            if client.objects.filter(name=username).exists():
                message = messages.error(request,'Client Already Exists')
                return redirect('addcus')
            else: 
                form.save()
                return redirect('home')
        
    context = {'form' : form}
    return render(request,'main/addcus.html',context)

def update_customer(request,pk):
    old = client.objects.get(id=pk)
    form = addcustomer(instance=old)
    if request.method == 'POST':
        form = addcustomer(request.POST, instance=old)
        if form.is_valid():
            form.save()
            return redirect('showcustomer')
    
    context = {'form':form}
    return render(request,'main/addcus.html',context)

def delete_customer(request,pk):
    deleted_cus = client.objects.get(id=pk)
    if request.method == 'POST':
        deleted_cus.delete()
        return redirect('showcustomer')
    
    context = {'deleted' : deleted_cus}
    return render(request,'main/delete_cus.html',context)

def addoffers(request):
    form = addoffer()
    place = request.POST.get('name_country')
    if request.method == 'POST':
        form = addoffer(request.POST, request.FILES)
        if Place.objects.filter(name_country = place).exists():
            message = messages.error(request,'Offer is Already Exists')
            return redirect('addoffer')
        else:
            form.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request,'main/addoffre.html',context)

def showoffer(request):
    place = Place.objects.all()
    place_count = Place.objects.count()

    context = {'place':place,'count':place_count}
    return render(request,'show/showoffer.html',context)


def update_offer(request,pk):
    old = Place.objects.get(id=pk)
    form = addoffer(instance=old)

    if request.method == 'POST':
        form = addoffer(request.POST, request.FILES, instance=old)
        if form.is_valid():
            form.save()
            return redirect('offers')
        
    context = {'form':form}
    return render(request,'main/addoffre.html',context)

def delete_offer(request,pk):
    deleted_offer = Place.objects.get(id=pk)
    if request.method == 'POST':
        deleted_offer.delete()
        return redirect('offers')
    
    context = {'deleted':deleted_offer}
    return render(request,'main/delete_offer.html',context)
        
