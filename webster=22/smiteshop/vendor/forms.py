from django.forms import ModelForm

from shop.models import Product

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields=['category','image','product_name','desc','price']