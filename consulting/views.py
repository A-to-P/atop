from django.shortcuts import render

# Create your views here.

def myConsulting(request):
    return render(request, 'myConsulting.html')

def consultingSpace(request):
    return render(request, 'consultingSpace.html')

def consultingHistory(request):
    return render(request, 'consultingHistory.html')


def consultingPortfolio(request):
    return render(request, 'consultingPortfolio.html')