from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import User

# Create your views here.

# 요식업자 포인트 충전 페이지
@login_required
def chargePoint(request):
    if request.method == "PUT":
        print (1)
    if request.method == "GET":
        print (2)
    if request.method == "POST":
        user = request.user
        plus = request.POST.get('point')
        total = request.user.point + int(plus)
        user.point = total
        user.save()
        return render(request, 'chargePoint.html', {'plus' : plus}) 
    return render(request, 'chargePoint.html')

# 컨설턴트 포인트 정산 페이지 
def consultPoint(request):
    return render(request, 'consultPoint.html')



# 
def pointHistory(request):
    return render(request, 'pointHistory.html')