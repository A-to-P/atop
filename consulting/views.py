from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Consulting, Accusation, Review
from account.models import User
from chat.models import Message
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.utils import timezone
# Create your views here.


def myConsulting(request):
    return render(request, 'myConsulting.html')


def consultingSpace(request):
    return render(request, 'consultingSpace.html')

def render_consulting(reqest):
    return redirect('chat')

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


# 파일 다운로드 

# 리뷰
def review(request):
    if request.method == "POST":
        user=request.user
        add_review = Review()
        consulting = Consulting.objects.get(restaurant=user, done=False)
        consulting.done = "True"
        add_review.consulting = consulting
        add_review.rating = len(request.POST.getlist('score'))
        print(add_review.rating)
        add_review.comment = request.POST.get("review_content")
        print(add_review.comment)
        consulting.save()
        add_review.save()

        return redirect('myConsulting')

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

# 컨설팅 삭제
@login_required
def deleteConsulting(request):
    if request.method=="POST":
        consulting_id = request.POST.get('consulting_id')
        print(consulting_id)
        consulting_obj = Consulting.objects.filter(id=consulting_id).first()
        
        if request.user != consulting_obj.consultant:
            return redirect('home') # TODO: 홈으로가기? 
        
        # 삭제하면 안됨.. 컨설턴트에게 보이지 않게만 하기        
        consulting_obj.deleted = True
        consulting_obj.save()        
    return redirect('consultingPortfolio')

def doneConsulting(request):
    message_id = int(request.POST.get('final_report')) # value=해당 파일이 들어있는 message 객체의 id
    message_obj = Message.objects.get(id=message_id)
    consulting = Consulting.objects.filter(restaurant=request.user).last()
    consulting.end = timezone.now()
    consulting.done = True
    consulting.final_report_filename = message_obj.filename
    consulting.final_report_base64URL= message_obj.base64URL
    
    print(consulting)
    consulting.save()
    return redirect('myConsulting') 