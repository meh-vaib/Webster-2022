from django.contrib import admin
from customer.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display=('username','phone','email','password')

admin.site.register(Customer,CustomerAdmin)
# Register your models here.
