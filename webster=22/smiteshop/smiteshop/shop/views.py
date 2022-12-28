from django.shortcuts import render
from django.http import HttpResponse

from . models import Product,Contact
from math import ceil

def anvil(request):
    products=Product.objects.filter(category='anvil')
    params={'product': products}
    return render(request,"shop/anvils.html", params)

def hammer(request):
    products=Product.objects.filter(category='hammer')
    params={'product': products}
    return render(request,"shop/hammer.html", params)

def nuts(request):
    products=Product.objects.filter(category='nuts')
    params={'product': products}
    return render(request,"shop/nuts.html", params)


def chains(request):
    products=Product.objects.filter(category='chains')
    params={'product': products}
    return render(request,"shop/chains.html", params)


def misc(request):
    products=Product.objects.filter(category='misc')
    params={'misc': products}
    return render(request,"shop/misc.html", params)



def index(request):
    return render(request,'shop/index.html')

    
def about(request):
    return HttpResponse("We are at about")

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        subject=request.POST.get('subject', '')
        message=request.POST.get('message', '')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return HttpResponse("Successful submission")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")

