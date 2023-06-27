from django.shortcuts import render

# Create your views here.

# 요식업자 포인트 충전 페이지
def chargePoint(request):
    return render(request, 'chargePoint.html')

# 컨설턴트 포인트 정산 페이지 
def consultPoint(request):
    return render(request, 'consultPoint.html')


# 
def pointHistory(request):
    return render(request, 'pointHistory.html')