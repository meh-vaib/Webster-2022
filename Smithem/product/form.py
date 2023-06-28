from django import forms
from .models import Product

class ImageForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=("product_img") 