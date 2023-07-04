from django.shortcuts import render

# Create your views here.

def consultantProfile(request):
    return render(request, "consultantProfile.html")
def restaurantProfile(request):
    return render(request, "restaurantProfile.html")

def editConsultProfile(request):
    return render(request, "editConsultProfile.html")

def editRestProfile(request):
    return render(request, "editRestProfile.html")

def profile_template(request):
    return render(request, "profile_template.html")

def consultProfile(request):
    return render(request, "myProfile.html")