from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Product
from math import ceil
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('ShopHome')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,'shop/register.html', context={"register_form":form})

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
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")



