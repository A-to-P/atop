from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('signup', views.signup, name="signup"),
    path('signup_restaurant', views.signup_restaurant, name="signup_restaurant"),
    path('signup_consultant', views.signup_consultant, name="signup_consultant"),
    
    
    # 컨설턴트 개인정보
    path('consultant_info', views.consultant_info, name="consultant_info"),
    # 요식업자 개인정보
    path('restaurant_info', views.restaurant_info, name="restaurant_info"),
    path('info_template', views.info_template, name="info_template"),
    path('edit_info', views.edit_info, name="edit_info"),
    
]
