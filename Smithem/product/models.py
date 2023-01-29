from django.db import models


class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.FloatField(max_length=6)
    product_des=models.TextField()
    product_img=models.FileField(upload_to="product/",max_length=250,null=True,default=None)



# Create your models here.
