from django.urls import path
from . import views

urlpatterns = [
    # 로그인 
    path('login', views.login, name="login"),
    
    # 로그아웃 
    path('logout', views.logout, name="logout"),
    
    # 회원가입 선택 
    path('signup', views.signup, name="signup"),
    
    # 요식업자 회원가입 
    path('signup_restaurant', views.signup_restaurant, name="signup_restaurant"),
    
    # 컨설턴트 회원가입
    path('signup_consultant', views.signup_consultant, name="signup_consultant"),
    
]