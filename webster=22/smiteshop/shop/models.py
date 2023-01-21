from io import BytesIO
from PIL import Image

from django.core.files import File

from django.db import models

from vendor.models import Vendor


class Product(models.Model):
    #product_id=models.AutoField(max_length=50)
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE, null=True)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="shop/images",default="")
    
    def __str__(self):
         return self.product_name
