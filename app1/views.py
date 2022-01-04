from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Student


def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect('login')
def Login(request):
    if request.method== 'POST':
        users = authenticate(username=request.POST['login'],password=request.POST['parol'])
        if users is None:
            return redirect('login')
        else:
            login(request,users)
            return redirect('home')

    return render(request,'login.html')
def registr(request):
    if request.method=='POST':
        a = User.objects.create_user(
            username=request.POST['login'],
            password=request.POST['parol']
        )
        Student.objects.create(
            ism=request.POST['ism'],
            yosh=request.POST['yosh'],
            guruh=request.POST['guruh'],
            foydalanuvchi=a
        )
        login(request,a)
        return redirect('home')
    return render(request,'registr.html')


def Logout(request):
    logout(request)
    return redirect('login')
