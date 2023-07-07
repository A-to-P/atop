from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse 
from account.models import ConsultantProfile, RestaurantProfile, Tag, User
from .models import Request, Application
from consulting.models import Consulting
from django.utils import timezone
from datetime import datetime

from chat.services.chat_room_service import creat_an_chat_room, get_an_chat_room
# Create your views here.


def postRequest(request):
    # 요식업자 아니면 리다이렉트
    if request.user.job != "restaurant":
        return redirect('home')

    all_con_tags = list(Tag.objects.filter(job="consultant").values())
    self_tag = request.user.get_tag()
    if request.method=="GET":
        # 컨설팅이 진행중이라면 리다이렉트
                
        # 이미 의뢰가 올라가있다면 리다이렉트
        
        # 의뢰글 작성 폼 렌더
        # 객체를 dict형태로 가져오기
        profile = list(RestaurantProfile.objects.filter(
            user=request.user).values())[0]
        # 나이계산
        profile["age"] = datetime.today().year - profile['birth'].year +1
        return render(request, "postRequest.html", {"user":request.user,"profile": profile,'self_tag':self_tag, 'tags':all_con_tags})
    
    elif request.method=="POST":
        try:
            user = request.user
            monthly_avg_rev = request.POST['monthly_avg_rev']
            title = request.POST['title']
            fee = request.POST['fee']
            content = request.POST['content']
            consult_tag_id = request.POST['request_field']
            
            # rest_tags
            # consult_tags
            
            new_reqest = Request(user=user, monthly_avg_rev=monthly_avg_rev, title=title,fee=fee,content=content)
            new_reqest.save()

            new_reqest.rest_tags.add(self_tag['id'])
            new_reqest.consult_tags.add(consult_tag_id)
            
        except Exception as e:
            print(e)
        
        return redirect('detailedRequest')


def detailedRequest(request):
    user = request.user
    if user.job != "restaurant":
        return redirect('home') # TODO: home?
    
    # 현재 진행중인 컨설팅이 있다면
    if Consulting.objects.filter(restaurant=user, done=False).exists():
        print("이미 컨설팅이 진행중입니다.")
        # return redirect('consultingSpace')
    # 현재 의뢰중인 의뢰
    curr_req = Request.current_req(user.id)
    # 현재 의뢰중인 의뢰가 없다면
    if curr_req is None:
        return render(request, 'detailedRequest.html', {'error':'의뢰글이 없습니다.'})
    
    applications = curr_req.applications
    if not applications.exists():
        applications = None 
    return render(request, "detailedRequest.html", {'req':curr_req, 'applications':applications})

# def applyRequest(request):
#     return render(request, "applyRequest.html")

def applyRequest(request, req_id):
    if request.user.job != "consultant":
        return redirect('home')
    
    # TODO: 해당 의뢰가 없을경우 (404) 핸들
    req = get_object_or_404(Request, pk=req_id)
    
    # TODO: 이미 지원한적 있을경우.. 핸들
    
    con_info = ConsultantProfile.objects.get(user=request.user)
    res_info = RestaurantProfile.objects.get(user=req.user)
        
    if request.method == "GET":
        return render(request, "applyRequest.html", {'con_info' : con_info, 'res_info' : res_info, 'req' : req})

    if request.method == "POST":
        apply = Application()
        apply.req = req
        apply.user = request.user
        apply.proposal = request.POST.get('proposal')
        apply.save()
        return redirect('consultingSpace')
        

def findRequest(request):
    tag_list = Tag.objects.filter(job="consultant")
    categorys = list(map(int, request.GET.getlist('categorys'))) # 태그 아이디. 0이면 '전체'
    query = categorys
    
    # [0] 이거나 []인경우
    if (len(query)==1 and query[0]==0) or len(query)==0 :
        req_list=Request.objects.all()
    else:        
        req_list = Request.objects.filter(consult_tags__in=query).distinct()
        
    print(req_list)
    result = []
    # 태그 별 출력
    for req in req_list:
        tmp = {}
        tmp['req_id'] = req.id
        tmp['title'] = req.title
        tmp['rest_tag'] = req.rest_tag['name']
        tmp['consult_tag'] = req.consult_tag['name']
        tmp['fee'] = req.fee
        tmp['application_count'] = len(req.applications)
        tmp['content']=req.content

        now = timezone.now()
        diff =  now - req.deadline
        tmp['deadline']=diff.days # "-7"
        
        result.append(tmp)
    return render(request, "findRequest.html", {'tags':tag_list, "categorys":categorys, 'req_list': result})


def deleteRequest(request):
    user = request.user
    if user.job != "restaurant":
        return redirect('home')
    
    if request.method == "POST":
        req_id = request.POST.get('req_id')
        if req_id is None:
            redirect('detailedRequest') # error
        req = Request.objects.filter(id=req_id).first() 
        if req is not None:
            req.delete()

    return redirect('detailedRequest')

def create_matching(request):
    if request.user.job != "restaurant":
        redirect('home')
    
    if request.method=="POST":
        # 컨설팅 객체 생성
        req_id = request.POST.get('req_id')
        con_id = request.POST.get('con_id')
        
        req = Request.objects.filter(id=req_id).first()
        consultant = User.objects.get(id=con_id)
        
        created = Consulting(req=req,
                             consultant=consultant, restaurant=request.user)
        print(created)
        created.save()
        
        # application 객체 selected=True 해주기
        application_id =request.POST.get('application_id')
        application = Application.objects.get(id=application_id)
        application.selected = True
        application.save()
        
        new_room = creat_an_chat_room(consult_id=consultant, rest_id=request.user)
        print(new_room)
        return redirect('chat')