from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('credentialsapp:login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if cpassword==password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('credentialsapp:register')

            user=User.objects.create_user(username=username,password=password)
            user.save()
            return redirect('credentialsapp:login')
        else:
            messages.info(request,'password not matching')
            return redirect('credentialsapp:register')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
