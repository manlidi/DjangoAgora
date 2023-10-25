from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('chat/', views.chat, name="chat"),
    path('vocal/', views.vocal, name="vocal"),
    path('', views.connexion,  name='connexion'),
    path('inscription/',views.inscription ,name='inscription'),
]
