"""wordladders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include

from pages.views import home_view, contact_view
from testAPP.views import product_detail_view, product_form_view, product_delete_view, prod_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('home/',home_view), 
    path('contact/',contact_view,name='contact'),
    path('product/<int:my_id>/',product_detail_view,name='product-detail'),
    path('createForm/',product_form_view),
    path('product/delete/<int:id>/',product_delete_view),
    path('products',prod_list_view),
    path('chat/',include('chat.urls'))
]
