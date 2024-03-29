
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Vendor
# from shop.models import Product

# from .forms import ProductForm

def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            vendor = Vendor.objects.create(name=request.user.username, created_by=request.user)

            return redirect('ShopHome')
        else:
            return HttpResponse("invalid Credentials!!")
    else:
        form = UserCreationForm()

    return render(request, 'vendor/become_vendor.html', {'form': form})

@login_required
def vendor_admin(request):
    vendor = Vendor.objects.create(name=request.user.username, created_by=request.user)
    vendor = request.user.vendor

    # products = vendor.products.all()
    return render(request, 'vendor/vendor_admin.html', {'vendor': vendor})

    # return render(request, 'vendor/vendor_admin.html', {'vendor': vendor,'products': products})

# @login_required
# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)

#         if form.is_valid():
#             product = form.save(commit=False)
#             product.vendor = request.user.vendor
#             product.slug = slugify(product.title)
#             product.save()

#             return redirect('vendor_admin')
#     else:
#         form = ProductForm()
    
#     return render(request,'vendor/add_product.html', {'form': form})
