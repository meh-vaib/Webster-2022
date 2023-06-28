from django.db import models


class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.FloatField(max_length=6)
    product_des=models.TextField()
    product_img=models.FileField(upload_to="product/",max_length=250,null=True,default=None)

    @staticmethod
    def get_products_by_ids(ids):
        return Product.objects.filter(id__in=ids)

# Create your models here.
