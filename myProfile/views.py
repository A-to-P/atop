from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth.decorators import login_required
from account.models import RestaurantProfile, ConsultantProfile, User

# Create your views here.

def consultantProfile(request):
    return render(request, "consultantProfile.html")

@login_required
def restaurantProfile(request):
    res_profile, created = RestaurantProfile.objects.get_or_create(user=request.user)
    return render(request, "restaurantProfile.html", {'res_profile' : res_profile})

def editConsultProfile(request):
    return render(request, "editConsultProfile.html")

def editRestProfile(request):
    res_profile, created = RestaurantProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":

        res_profile.name = request.POST.get('name')
        res_profile.image = request.FILES.get('profile_image')
        User.email = request.POST.get('email')
        res_profile.birth = request.POST.get('age')
        res_profile.career = request.POST.get('career')
        # 밑에 두 개 "IntegrityError, Not NULL constraint failed" 
        # res_profile.self_introducing = request.POST.get('introduction')
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