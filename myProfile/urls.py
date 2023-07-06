from django.urls import path
from . import views


urlpatterns = [
    # 127.0.0.1:8000/myProfile
    # 컨설턴트 프로필
    path('consultantProfile/', views.consultantProfile, name="consultantProfile"),
    # 요식업자 프로필
    path('restaurantProfile/', views.restaurantProfile, name="restaurantProfile"),
    # 127.0.0.1:8000/editMyprofile
    path('editConsultProfile/', views.editConsultProfile, name="editConsultProfile"),
    
    path('editRestProfile/', views.editRestProfile, name="editRestProfile"),
    path('profile_template/', views.profile_template, name="profile_template"),
    
    path('myProfile/', views.myProfie, name="myProfile"),
    path('profile/<int:user_id>', views.profie, name="profile"),

  
]
