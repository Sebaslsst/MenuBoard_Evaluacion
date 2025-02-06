from django.contrib import admin
from django.urls import path,include
from facturacionapp import views

urlpatterns = [
    path('menu/',views.menu)



]