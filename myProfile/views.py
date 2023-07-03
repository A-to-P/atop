from django.shortcuts import render, redirect
from django.db import models
from account.models import RestaurantProfile, ConsultantProfile, User
# Create your views here.

def myProfile(request):
    if request.user.is_anonymous:
        return redirect('login')
    profile, created = ConsultantProfile.objects.get_or_create(user=request.user)
    return render(request, "myProfile.html", {'profile' : profile})

def editMyprofile(request):
    return render(request, "editMyprofile.html")

def profile_template(request):
    return render(request, "profile_template.html")

def new_profile_template(request):
    return render(request, "new_profile_template.html")