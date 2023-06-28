from django.shortcuts import render

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
    return render(request, 'signup_restaurant.html') 

# 컨설턴트 회원가입 폼
def signup_consultant(request):
    return render(request, 'signup_consultant.html')


    