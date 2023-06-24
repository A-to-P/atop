from django.shortcuts import render

# Create your views here.

def myConsulting(request):
    return render(request, 'myConsulting.html')

def consultingSpace(request):
    return render(request, 'consultingSpace.html')

