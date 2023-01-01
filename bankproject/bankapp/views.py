from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def enquiry(request):
    return render(request,'enquiry.html')

def create(request):
    if request.method=='POST':
        messages.info(request,'application accepted')
        return redirect('bankapp:create')
    return render(request,'create.html')
