from django.urls import path
from . import views

urlpatterns = [
    path('myConsulting', views.myConsulting, name="myConsulting"),  #127.0.0.1:8000/myConsulting 
    path('consultingSpace', views.consultingSpace, name="consultingSpace"),  #127.0.0.1:8000/consultingSpace
]