from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000/postRequest
    path('postRequest/', views.postRequest, name="postRequest"),
    path('detailedRequest/', views.detailedRequest,
         name="detailedRequest"),  # 127.0.0.1:8000/detailedRequest
    path('applyRequest/<int:req_id>/', views.applyRequest,
         name="applyRequest"),  # 127.0.0.1:8000/applyRequest
    # 127.0.0.1:8000/findRequest
    path('findRequest/', views.findRequest, name="findRequest"),
    path('deleteRequest', views.deleteRequest, name="deleteRequest"),
    path("create_matching/", views.create_matching, name="create_matching")
]
