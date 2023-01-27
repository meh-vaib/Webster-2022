from django.db import models
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.FloatField(max_length=6)
    product_des=models.TextField()
# Create your models here.
