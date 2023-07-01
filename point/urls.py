from django.urls import path
from . import views

urlpatterns = [
    path('chargePoint', views.chargePoint, name="chargePoint"),
    path('consultPoint', views.consultPoint, name="consultPoint"),
    # path('calculatePoint', views.calculatePoint, name="calculatePoint"),
    
    path('pointHistory', views.pointHistory, name="pointHistory"),  
    
]