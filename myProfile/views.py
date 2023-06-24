from django.shortcuts import render

# Create your views here.

def myProfile(request):
    return render(request, "myProfile.html")

def editMyprofile(request):
    return render(request, "editMyprofile.html")