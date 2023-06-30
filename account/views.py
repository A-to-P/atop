from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth

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

def signup_restaurant(request):
    # if request.method == "GET":
    #     return render(request, 'signup_restaurant.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password_check = request.POST['password_check']
        email = request.POST['email']

        if not username or not password:
            error_username = '아이디와 비밀번호를 모두 입력해주세요.'
            return render(request, 'account/signup_restaurant.html', {'error_username': error_username})
        if User.objects.filter(username=username).exists():
            error_username = '이미 사용중인 아이디입니다.'
            return render(request, 'account/signup_restaurant.html', {'error_username': error_username})
        if password != password_check:
            error_password = '비밀번호와 비밀번호 확인이 일치하지 않습니다.'
            return render(request, 'account/signup_restaurant.html', {'error_password': error_password})
        else:   
            user = User.objects.create_normaluser(username=username, password=password)

            user = User(user=user)
            user.save()

            auth.login(request,user)
            return render('home')
    return render(request, 'signup_restaurant.html')

#컨설턴트 회원가입폼
def signup_consultant(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password_check = request.POST['password_check']
        email = request.POST['email']

        if not username or not password:
            error_username = '아이디와 비밀번호를 모두 입력해주세요.'
            return render(request, 'account/signup_consultant.html', {'error_username': error_username})
        if User.objects.filter(username=username).exists():
            error_username = '이미 사용중인 아이디입니다.'
            return render(request, 'account/signup_consultant.html', {'error_username': error_username})
        if password != password_check:
            error_password = '비밀번호와 비밀번호 확인이 일치하지 않습니다.'
            return render(request, 'account/signup_consultant.html', {'error_password': error_password})
        else:   
            user = User.objects.create_normaluser(username=username, password=password)
            user = User(user=user)
            user.save()

            auth.login(request,user)
            return render('home')
    return render(request, 'signup_consultant.html')