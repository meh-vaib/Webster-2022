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

class Anvil(View):
    def get(self,request):
        productData=Product.objects.all()
        paginator=Paginator(productData,12)
        page_number=request.GET.get('page')
        productData=paginator.get_page(page_number)
        totalpages=productData.paginator.num_pages
    
        if request.method=="GET":
            st=request.GET.get('product')
        if st!=None:
            productData=Product.objects.filter(product_name__icontains=st)
   
        data={
            'totalpages': totalpages,
            'productData': productData,
            'totalpagelist':[n+1 for n in range(totalpages)]
        }
        print('you are:' , request.session.get('email'))
        return render(request,"anvil.html",data)

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

        return redirect('anvil')


