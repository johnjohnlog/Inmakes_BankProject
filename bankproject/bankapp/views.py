from django.shortcuts import render, redirect
from django.contrib import messages
from bankapp.models import Account

# Create your views here.
def index(request):
    account=Account.objects.all()
    return render(request,'index.html',{'account':account})
def enquiry(request):
    return render(request,'enquiry.html')
def detail(request,id):
    account = Account.objects.get(id=id)
    return render(request,'detail.html',{'account':account})

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        date = request.POST.get('date')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        account=Account(name=name,age=age,date=date,address=address,phone=phone,email=email)
        account.save()
        messages.info(request,'application accepted')
        return redirect('bankapp:create')
    return render(request,'create.html')
