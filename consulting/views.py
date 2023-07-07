from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Consulting, Accusation, Review
from account.models import User
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.


def myConsulting(request):
    return render(request, 'myConsulting.html')


def consultingSpace(request):
    return render(request, 'consultingSpace.html')

# 요식업자의 포트폴리오 페이지
@login_required
def consultingHistory(request):
    user = request.user
    if user.job != 'restaurant':
        return redirect('home')
    if request.method =="GET":
        history_list = Consulting.objects.filter(restaurant=user, done=True)
        result = []
        paginator = Paginator(history_list, 8) # 한 페이지에 최대 8개
        page_number = int(request.GET.get('page', 1))
        page_obj = paginator.get_page(page_number)
        for history in page_obj:
            tmp = {}
            tmp['consulting_id']=history.id
            tmp['end']=history.end
            tmp['consultant']=history.consultant.name
            tmp['tag']=history.tags[0].name
            tmp['fee']=history.fee
            result.append(tmp)
        return render(request, 'consultingHistory.html',
                      {'history_list' :result,
                       "page_number":page_number,
                       'paginator':{'num_pages':paginator.num_pages, 'page_number':page_number}})
    
    return render(request, 'consultingHistory.html')

# 컨설턴트의 포트폴리오 페이지
def consultingPortfolio(request):
    return render(request, 'consultingPortfolio.html')


# 파일 다운로드 

# 신고
def accuse(request):
    if request.method == "POST":
        user = request.user
        if user.job == "restaurant":
            consulting = Consulting.objects.get(restaurant=user, done=False)
            accusation = Accusation()
            accusation.complainant = request.user
            accusation.defendant = consulting.consultant
        elif user.job == "consultant":
            consulting = Consulting.objects.get(consultant=user, done=False)
            accusation = Accusation()
            accusation.complainant = request.user
            accusation.defendant = consulting.restaurant
        accusation.evidence = request.FILES.get('declaration-info')
        accusation.comment = request.POST.get('declaration_content')
        accusation.save()

        return HttpResponse('ok')

