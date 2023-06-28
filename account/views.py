# from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404

from .models import User
from .forms import CustomUserSignupForm, CustomUserSigninForm

# Create your views here.

# 로그인
def login(request):
    form = CustomUserSigninForm()
    if request.method == 'POST':
        form = CustomUserSigninForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    return render(request, "login.html")

# 회원가입 
def signup(request):
    return render(request, 'signup.html')

# 기본 회원가입 폼
def signupFrom(request):
    return render(request, 'signupForm.html')

# 요식업자 회원가입 폼
def signup_restaurant(request):
    return render(request, 'signup_restaurant.html') 

# 컨설턴트 회원가입 폼
def signup_consultant(request):
    return render(request, 'signup_consultant.html')


    