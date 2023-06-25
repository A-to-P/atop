from django.urls import path
from . import views


urlpatterns = [
    # 127.0.0.1:8000/myProfile
    path('myProfile', views.myProfile, name="myProfile"),
    # 127.0.0.1:8000/editMyprofile
    path('editMyprofile', views.editMyprofile, name="editMyprofile"),
]
