from django.shortcuts import render

# Create your views here.

def myProfile(request):
    return render(request, "myProfile.html")

def editMyprofile(request):
    return render(request, "editMyprofile.html")

def profile_template(request):
    return render(request, "profile_template.html")

def new_profile_template(request):
    return render(request, "new_profile_template.html")