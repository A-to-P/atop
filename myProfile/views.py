from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth.decorators import login_required
from account.models import RestaurantProfile, ConsultantProfile, User, Tag
from django.urls import reverse

# Create your views here.
@login_required
def myProfie(request):
    if request.user.job == "consultant":
        return redirect(reverse('consultantProfile'))
    else:
        return redirect(reverse('restaurantProfile'))

@login_required
def consultantProfile(request):
    if request.user.job != "consultant":
        return redirect('home')
    con_profile, created = ConsultantProfile.objects.get_or_create(user=request.user)
    return render(request, "consultantProfile.html", {'con_profile' : con_profile})

@login_required
def restaurantProfile(request):
    if request.user.job != "restaurant":
        return redirect('home')
    res_profile, created = RestaurantProfile.objects.get_or_create(user=request.user)
    return render(request, "restaurantProfile.html", {'res_profile' : res_profile})

@login_required
def editConsultProfile(request):
    if request.user.job != "consultant":
        return redirect('home')
    
    tags = Tag.objects.filter(job="consultant")
    con_profile, created = ConsultantProfile.objects.get_or_create(user=request.user)
    user = request.user
    if request.method == "POST":
        con_profile.name = request.POST.get('name')
        image =  request.FILES.get('profile_image')
        if image is not None: # 파일 업로드 안하면 수정 안함
            con_profile.image = image
        user.tag.clear()
        user.tag.add(request.POST.get('request_field'))
        user.email = request.POST.get('email')
        user.save()
        con_profile.birth = request.POST.get('birth')
        con_profile.education = request.POST.get('school') 
        con_profile.self_introducing = request.POST.get('introduction')
        if request.POST.get('anytime'): # '언제나' 체크되있다면
            con_profile.contact_at = request.POST.get('anytime')
        else:
            con_profile.contact_at = f"{request.POST.get('start_time')} ~ {request.POST.get('end_time')}"
        con_profile.save()
        # 컨설팅 분야

        # 컨설팅 횟수

        return redirect('consultantProfile')
    return render(request, "editConsultProfile.html", {'con_profile' : con_profile, "tags":tags})

@login_required
def editRestProfile(request):
    if request.user.job != "restaurant":
        return redirect('home')
    
    tags = Tag.objects.filter(job="restaurant")
    res_profile, created = RestaurantProfile.objects.get_or_create(user=request.user)
    user = request.user
    if request.method == "POST":

        res_profile.name = request.POST.get('name')
        image =  request.FILES.get('profile_image')
        if image is not None:
            res_profile.image = image
        user.tag.clear()
        user.tag.add(request.POST.get('restaurant_field'))
        user.email = request.POST.get('email')
        user.save()
        res_profile.birth = request.POST.get('birth')
        res_profile.career = request.POST.get('career') 
        res_profile.self_introducing = request.POST.get('introduction')
        if request.POST.get('anytime'): # '언제나' 체크되있다면
            res_profile.contact_at = request.POST.get('anytime')
        else:
            res_profile.contact_at = f"{request.POST.get('start_time')} ~ {request.POST.get('end_time')}"
        res_profile.menu = request.POST.get('sig_menu')
        res_profile.location = request.POST.get('location')
        res_profile.area = request.POST.get('size')
        res_profile.save()
        return redirect('restaurantProfile')
    return render(request, "editRestProfile.html", {'res_profile' : res_profile, "tags":tags})

def profile_template(request):
    return render(request, "profile_template.html")

def consultProfile(request):
    return render(request, "myProfile.html")

def profie(request, user_id):    
    # return render(request)
    pass