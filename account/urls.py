from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"), 
    path('signup_restaurant', views.signup_restaurant, name="signup_restaurant"),
    path('signup_consultant', views.signup_consultant, name="signup_consultant"),
    
]