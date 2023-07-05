from django.shortcuts import render

# Create your views here.


def myConsulting(request):
    return render(request, 'myConsulting.html')


def consultingSpace(request):
    return render(request, 'consultingSpace.html')

# 요식업자의 포트폴리오 페이지
def consultingHistory(request):
    return render(request, 'consultingHistory.html')

# 컨설턴트의 포트폴리오 페이지
def consultingPortfolio(request):
    return render(request, 'consultingPortfolio.html')
