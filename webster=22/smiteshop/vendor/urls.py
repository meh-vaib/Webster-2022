from django.urls import path
from . import views

urlpatterns = [
path('become_vendor/',views.become_vendor,name='become_vendor')
]
