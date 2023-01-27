from django.contrib import admin
from product.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','product_price','product_des')

admin.site.register(Product,ProductAdmin)