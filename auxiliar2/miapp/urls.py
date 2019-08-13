from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pestaña/', views.pestaña, name='pestaña'),
	path('TicsDesafio1/', views.TicsDesafio1, name='TicsDesafio1')
]