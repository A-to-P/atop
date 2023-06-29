from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import User

# Create your views here.

# 로그인 
def login(request):
    return render(request, 'login.html')

# 회원가입 
def signup(request):
    return render(request, 'signup.html')

# 기본 회원가입 폼
def signupFrom(request):
    return render(request, 'signupForm.html')

# 요식업자 회원가입 폼
def signup_restaurant(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        username = request.POST.get['username',None]   
        password = request.POST.get['password',None]
        re_password = request.POST.get['re_password',None]
        res_data = {} 
        if not (username and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password :
            res_data['error'] = '비밀번호가 다릅니다.'
        else :
            user = User(username=username, password=make_password(password))
            user.save()
    return render(request, 'signup_restaurant.html') 

# 컨설턴트 회원가입 폼
def signup_consultant(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        username = request.POST.get['username',None]  
        password = request.POST.get['password',None]
        re_password = request.POST.get['re_password',None]
        res_data = {} 
        if not (username and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password :
            res_data['error'] = '비밀번호가 다릅니다.'
        else :
            user = User(username=username, password=make_password(password))
            user.save()
    return render(request, 'signup_consultant.html')

# 요식업 분야 선택
def restaurant_part(request):
    if request.POST:
        list_item = request.POST.getlist('요식업분야')
        print(list_item)

# 컨설팅 희망 분야 선택
def consultant_part(request):
    if request.POST:
        list_item = request.POST.getlist('컨설팅분야')
        print(list_item)


    