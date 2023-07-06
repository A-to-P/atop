from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Consulting
from django.core.paginator import Paginator
# Create your views here.


def myConsulting(request):
    return render(request, 'myConsulting.html')


# def consultingSpace(request):
#     return render(request, 'consultingSpace.html')

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
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # print(paginator.count, paginator.num_pages )
        for history in page_obj:
            print('history:', history)
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
                       'paginator':{'num_pages':paginator.num_pages, 'page_number':int(page_number)}})
    
    # return render(request, 'consultingHistory.html')

# 컨설턴트의 포트폴리오 페이지
def consultingPortfolio(request):
    return render(request, 'consultingPortfolio.html')


# 파일 다운로드 


def rest_ConsultingSpace(request):
    return render(request, 'rest_ConsultingSpace.html')