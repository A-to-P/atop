from django.urls import path
from . import views

urlpatterns = [
    path('postRequest/', views.postRequest, name="postRequest"),  #127.0.0.1:8000/postRequest
    path('detailedRequest/', views.detailedRequest, name="detailedRequest"),  #127.0.0.1:8000/detailedRequest
    path('applyRequest/', views.applyRequest, name="applyRequest"),  #127.0.0.1:8000/applyRequest
    path('findRequest/', views.findRequest, name="findRequest"),  #127.0.0.1:8000/findRequest
]