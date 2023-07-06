from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Consulting
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
    user = request.user
    if user.job != 'consultant':
        return redirect('home')
    
    if request.method =="GET":
        history_list = Consulting.objects.filter(consultant=user, done=True, deleted=False)
        result = []
        paginator = Paginator(history_list, 8) # 한 페이지에 최대 8개
        page_number = int(request.GET.get('page', 1))
        page_obj = paginator.get_page(page_number)
        for history in page_obj:            
            tmp = {}
            tmp['consulting_id']=history.id
            tmp['end']=history.end
            tmp['restaurant']=history.restaurant.name
            tmp['res_tag']=history.res_tag['name']
            tmp['con_tag']=history.con_tag['name']
            tmp['final_file']={'filename':history.final_report_filename, 'base64URL':history.final_report_base64URL}
            result.append(tmp)
        return render(request, 'consultingPortfolio.html',
                      {'history_list' :result,
                       "page_number":page_number,
                       'paginator':{'num_pages':paginator.num_pages, 'page_number':page_number}})
    
    return render(request, 'consultingPortfolio.html')


# 컨설팅 삭제
@login_required
def deleteConsulting(request):
    if request.POST.get('_method') == "DELETE":
        consulting_id = request.POST.get('consulting_id')
        print(consulting_id)
        consulting_obj = Consulting.objects.filter(id=consulting_id).first()
        
        if request.user != consulting_obj.consultant:
            return redirect('home') # TODO: 홈으로가기? 
        
        # 삭제하면 안됨.. 컨설턴트에게 보이지 않게만 하기        
        consulting_obj.deleted = True
        consulting_obj.save()        
    return redirect('consultingPortfolio')
