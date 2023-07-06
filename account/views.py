from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Tag, ConsultantProfile, RestaurantProfile
from django.contrib.auth.hashers import make_password

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
        name = request.POST['name']
        tag_id = request.POST['restaurant_field']
        username = request.POST['id']
        password = request.POST['pw']
        password_check = request.POST['pw_check']
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
            user = User.objects.create(username=username,password=make_password(password),email=email,job='restaurant')
            user.tag.add(tag_id)
            
            profile = RestaurantProfile.objects.create(user=user, name=name)
            print(profile)
            auth_login(request,user)
            return redirect('home')
    

#컨설턴트 회원가입폼
def signup_consultant(request):
    tags = list(Tag.objects.filter(job="consultant").values())
    if request.method =="GET":
        return render(request, 'signup_consultant.html', {'tags':tags})
    
    if request.method == "POST":
        name = request.POST['name']
        tag_id = request.POST['request_field']
        username = request.POST['id']
        password = request.POST['pw']
        password_check = request.POST['pw_check']
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
            user = User.objects.create(username=username, password=make_password(password),email=email,job='consultant')
            user.tag.add(tag_id)
            
            profile = ConsultantProfile.objects.create(user=user, name=name)
            print(profile)
            auth_login(request,user)
            return redirect('home')


@login_required
def consultant_info(request):
    if request.user.job != "consultant":
        return redirect('home')
    
    return render(request, 'consultant_info.html')

@login_required
def restaurant_info(request):
    if request.user.job != "restaurant":
        return redirect('home')
    return render(request, "restaurant_info.html") 

@login_required
def info_template(request):
    return render(request, "info_template.html") 


@login_required
def edit_info(request):
    if request.method == "POST":
        user = request.user
        user.username = request.POST['user_id']
        user.email = request.POST['email']
        user.point = request.POST['point']
        new_password = request.POST['user_pw']
        user.set_password(new_password)
        user.save()
        auth_login(request, user)
        if user.job == "restaurant":
            return redirect ('restaurant_info')
        elif user.job == "consultant":
            return redirect ('consultant_info')
    return render(request, "edit_info.html")

def changePassword(request):
    return render(request, 'changePassword.html')