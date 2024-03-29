"""Smithem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Smithem import views
from django.conf import settings
from django.conf.urls.static import static
from .login import Login, logout
from .signup import Signup
from .anvil import Anvil
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage,name="home"),
    path('anvil/',Anvil.as_view(),name="anvil"),
    path('about/',views.About,name="about"),
    path('features/',views.Features),
    path('contact/',views.Contact),
    path('sell/',views.Sell),
    path('signup/',Signup.as_view(),name="signup"),
    path('saveenquiry/',views.saveEnquiry,name="saveenquiry"),
    path('savepro/',views.savePro,name="savepro"),
    path('login/',Login.as_view(),name="login"),
    path('logout/',logout,name="logout"),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)