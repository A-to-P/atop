from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from .models import User, Tag, ConsultantProfile, RestaurantProfile
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
def signupForm(request):
    return render(request, 'signupForm.html')

# 요식업자 폼
def signup_restaurant(request):
    tags = list(Tag.objects.filter(job="restaurant").values())
    if request.method =="GET":
        return render(request, 'signup_restaurant.html', {'tags':tags})
    
    if request.method == "POST":
        tag_value = request.POST['restaurant_field']
        username = request.POST['username']
        password = request.POST['password']
        password_check = request.POST['password_check']
        email = request.POST['email']
        

        if not username or not password:
            error_username = '아이디와 비밀번호를 모두 입력해주세요.'
            return render(request, 'signup_restaurant.html', {'error': error_username, 'tags':tags})
        if User.objects.filter(username=username).exists():
            error_username = '이미 사용중인 아이디입니다.'
            return render(request, 'signup_restaurant.html', {'error': error_username, 'tags':tags})
        if password != password_check:
            error_password = '비밀번호와 비밀번호 확인이 일치하지 않습니다.'
            return render(request, 'signup_restaurant.html', {'error': error_password, 'tags':tags})
        else:   
            tag = Tag.objects.get(value=tag_value)
            user = User.objects.create(username=username,password=password,email=email,job='restaurant')
            user.tag.add(tag.id)
            
            auth.login(request,user)
            return redirect('home')
    

#컨설턴트 회원가입폼
def signup_consultant(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password_check = request.POST['password_check']
        email = request.POST['email']

        if not username or not password:
            error_username = '아이디와 비밀번호를 모두 입력해주세요.'
            return render(request, 'signup_consultant.html', {'error': error_username})
        if User.objects.filter(username=username).exists():
            error_username = '이미 사용중인 아이디입니다.'
            return render(request, 'signup_consultant.html', {'error': error_username})
        if password != password_check:
            error_password = '비밀번호와 비밀번호 확인이 일치하지 않습니다.'
            return render(request, 'signup_consultant.html', {'error': error_password})
        else:   
            user = User(username=username, password=password,email=email,job='consultant')
            user.save()

            auth.login(request,user)
            return redirect('home')
    return render(request, 'signup_consultant.html')
