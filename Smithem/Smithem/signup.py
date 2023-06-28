from django.http import HttpResponse
from django.shortcuts import render, redirect
from product.models import Product
from customer.models import Customer
from django.core.paginator import Paginator
from contact.models import contact
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request,"signup.html")
    def post(self,request):
        error=None
        
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        repassword=request.POST.get('repassword')
       
        if password!=repassword:
            error='Passwords are not matching'
        password=make_password(password)    
        en=Customer(username=username,email=email,phone=phone,password=password)    
        
        if len(phone)!=10:
            error='Please Enter Valid Phone Number'
        if Customer.objects.filter(email=email):
            error='User Already Exists'
            

        if not error:  
            en.save()
            return render(request,"index.html")
        else:
            return render(request,"signup.html",{'error':error})
    
