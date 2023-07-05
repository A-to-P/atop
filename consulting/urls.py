from django.urls import path
from . import views

urlpatterns = [
    path('myConsulting/', views.myConsulting, name="myConsulting"),  #127.0.0.1:8000/myConsulting 
    path('consultingSpace/', views.consultingSpace, name="consultingSpace"),  #127.0.0.1:8000/consultingSpace
    
    # 컨설팅 히스토리 페이지
    path('consultingHistory/', views.consultingHistory, name="consultingHistory"),  
    
]