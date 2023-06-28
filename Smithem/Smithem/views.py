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

def HomePage(request):
    if request.method=='GET':
        send_mail(
        'Testing mail',
        'Here is the message',
        'smithem2k22@gmail.com',
        ['smithem2k22@gmail.com'],
        fail_silently=True,
        )
        return render(request,"index.html")
    if request.method=="POST":
        product=request.POST.get('cart')
        print(product)
        return redirect('anvil')
    
def About(request):
    return render(request,"about.html"); 

def Features(request):
    return render(request,"features.html"); 

def Contact(request):
    return render(request,"contact.html");   

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        en=contact(name=name,email=email,subject=subject,message=message)  
        en.save()  
    return render(request,"contact.html");    

def Sell(request):
    return render(request,"sell.html");   

def savePro(request):
    if request.method=="POST":
        name=request.POST.get('name')
        price=request.POST.get('price')
        des=request.POST.get('des')
    
        if len(request.FILES) != 0:
            img=request.FILES['image']
            en=Product(product_name=name,product_price=price,product_des=des,product_img=img)  
            en.save()
    return render(request,"sell.html")
    


        
    
         





