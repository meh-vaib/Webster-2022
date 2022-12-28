from django.db import models
# from vendor.models import Vendor


class Product(models.Model):
    # product_id=models.AutoField(max_length=50,primary_key= True)
    product_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50,default ="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    # vendor=models.ForeignKey(Vendor,related_name='products',on_delete=models.CASCADE,)
    image1= models.ImageField(upload_to="shop/images",default="")
    image2= models.ImageField(upload_to="shop/images",default="")
    image3= models.ImageField(upload_to="shop/images",default="")
    image4= models.ImageField(upload_to="shop/images",default="")
    
    def __str__(self):
         return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
    

