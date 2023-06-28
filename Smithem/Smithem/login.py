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


class Login(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        error=None
        email=request.POST.get('email')
        password=request.POST.get('password')
        obj=Customer.get_customer_by_email(email)
        print(email,password)
        print(obj)

        if obj:
            flag=check_password(password,obj.password)
            if not flag:
                error="Email or Password Incorrect"  
        else:
            error="Email or Password Incorrect"

        
        if not error:
            request.session['customer']=obj.id
            
            return render(request,'index.html')
        else:
            return render(request,'login.html',{'error':error})

def logout(request):
    request.session.clear()
    return redirect('home')