from django.contrib import admin
from django.urls import path,include
from . import views

app_name="core"
urlpatterns = [
    path('', views.home, name="home"),
    path('contato/', views.contact, name="contato"),
]
