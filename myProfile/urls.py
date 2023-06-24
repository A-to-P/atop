from django.urls import path
from . import views

urlpatterns = [
    path('myProfile', views.myProfile, name="myProfile"),  #127.0.0.1:8000/myProfile
    path('editMyprofile', views.editMyprofile, name="editMyprofile"),  #127.0.0.1:8000/editMyprofile
]