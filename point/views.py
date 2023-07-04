from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import User

# Create your views here.

# 요식업자 포인트 충전 페이지
@login_required
def chargePoint(request):
    if request.method == "GET":
        user = request.user
        return render(request, 'chargePoint.html', {'user': user })
    if request.method == "POST":
        # PUT을 쓰려면 요청은 post로 날리고 hidden input을 사용함
        if request.POST.get('_method') == "PUT": 
            user = request.user
            plus = request.POST.get('point')
            total = request.user.point + int(plus)
            user.point = total
            user.save()
        return render(request, 'chargePoint.html')

# 컨설턴트 포인트 정산 페이지 
def consultPoint(request):
    return render(request, 'consultPoint.html')



# 
def pointHistory(request):
    return render(request, 'pointHistory.html')