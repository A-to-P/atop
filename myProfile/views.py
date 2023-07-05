from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth.decorators import login_required
from account.models import RestaurantProfile, ConsultantProfile, User

# Create your views here.

@login_required
def consultantProfile(request):
    con_profile, created = ConsultantProfile.objects.get_or_create(user=request.user)
    return render(request, "consultantProfile.html", {'con_profile' : con_profile})

@login_required
def restaurantProfile(request):
    res_profile, created = RestaurantProfile.objects.get_or_create(user=request.user)
    return render(request, "restaurantProfile.html", {'res_profile' : res_profile})

def editConsultProfile(request):
    con_profile, created = ConsultantProfile.objects.get_or_create(user=request.user)
    user = request.user
    if request.method == "POST":
        con_profile.name = request.POST.get('name')
        con_profile.image = request.FILES.get('profile_image')
        User.email = request.POST.get('email')
        con_profile.birth = request.POST.get('age')
        con_profile.education = request.POST.get('school') 
        con_profile.self_introducing = request.POST.get('introduction')
        # con_profile.contact_at = request.POST.get('inputGroup-sizing-default')
        con_profile.save()
        # 컨설팅 분야

        # 컨설팅 횟수

        return redirect('consultantProfile')
    return render(request, "editConsultProfile.html", {'con_profile' : con_profile})

def editRestProfile(request):
    res_profile, created = RestaurantProfile.objects.get_or_create(user=request.user)
    user = request.user
    if request.method == "POST":

        res_profile.name = request.POST.get('name')
        res_profile.image = request.FILES.get('profile_image')
        User.email = request.POST.get('email')
        res_profile.birth = request.POST.get('age')
        res_profile.career = request.POST.get('career') 
        res_profile.self_introducing = request.POST.get('introduction')
        # contact_at 에러남 -> "IntegrityError, Not NULL constraint failed"
        # res_profile.contact_at = request.POST.get('inputGroup-sizing-default')
        res_profile.menu = request.POST.get('sig_menu')
        res_profile.location = request.POST.get('location')
        res_profile.area = request.POST.get('size')
        res_profile.save()
        return redirect('restaurantProfile')
    return render(request, "editRestProfile.html", {'res_profile' : res_profile})

def profile_template(request):
    return render(request, "profile_template.html")

def consultProfile(request):
    return render(request, "myProfile.html")