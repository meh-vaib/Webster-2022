from django.contrib import admin
from contact.models import contact

class contactAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')

admin.site.register(contact,contactAdmin)
# Register your models here.
