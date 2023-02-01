from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('fin', views.fin, name='fin'),
    path('', views.index , name='index')
]
