from django.shortcuts import render

# Create your views here.

def chargePoint(request):
    return render(request, 'chargePoint.html')

def pointHistory(request):
    return render(request, 'pointHistory.html')