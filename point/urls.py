from django.urls import path
from . import views

urlpatterns = [
    path('chargePoint', views.chargePoint, name="chargePoint"),
    path('pointHistory', views.pointHistory, name="pointHistory"),
]