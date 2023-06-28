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
from product.models import Product

class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_ids(ids)
        print(products)
        return render(request,'cart.html', {'products':products})
    