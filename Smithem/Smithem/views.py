from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product
from django.core.paginator import Paginator
from contact.models import contact

def HomePage(request):
    return render(request,"index.html");

def Anvil(request):
    request.method=="GET"
    productData=Product.objects.all()
    
    paginator=Paginator(productData,4)
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
    return render(request,"anvil.html",data);    

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
