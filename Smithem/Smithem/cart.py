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
        total_price=0
        cart=request.session.get('cart')
        print(cart)
        for p in products:
            print(cart.get(str(p.id)))
            total_price+=(p.product_price)*(cart.get(str(p.id)))

        data={
            'products':products,
            'total_price':total_price
        }
        return render(request,'cart.html',data)
    
    def post(self,request):
        proid=request.POST.get('proid')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if proid:
            if cart:
                quantity=cart.get(proid)
                if quantity:
                    if remove:
                        if quantity<=1:
                            cart.pop(proid)
                        else:
                            cart[proid]=quantity-1
                    else:
                        cart[proid]=quantity+1
                else:
                    cart[proid]=1
            else:
                cart={}
                cart[proid]=1
            request.session['cart']=cart
            print(cart)

        return redirect('cart')
    