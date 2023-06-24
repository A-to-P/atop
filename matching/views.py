from django.shortcuts import render

# Create your views here.

def postRequest(request):
    return render(request, "postRequest.html")

def detailedRequest(request):
    return render(request, "detailedRequest.html")

def findRequest(request):
    return render(request, "findRequest.html")