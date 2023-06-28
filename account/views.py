from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from .models import User

# Create your views here.

# 로그인
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        id = request.POST['id']
        pw = request.POST['pw']
        user = authenticate(request, username=id, password=pw)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        
        else:
            return render(request, 'login.html', {'error':'아이디 또는 비밀번호가 틀립니다.'})
        
# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('home')

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


    