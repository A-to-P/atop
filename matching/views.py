from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse 
from account.models import ConsultantProfile, RestaurantProfile, Tag
from .models import Request, Application
from consulting.models import Consulting
import datetime
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
        profile["age"] = datetime.datetime.today().year - profile['birth'].year +1
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
        print(0)
        return redirect('consultingSpace')
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
        

# Json data로 만들기 위한 함수
def requestDictionary(request_list):
    output = {}
    output["title"] = request_list.title
    output["rest_tag"] = request_list.rest_tag
    output["fee"] = request_list.fee
    # 지원자 수 고민해보기
    output["content"] = request_list.content
    return output

def findRequest(request):
    tag_list = list(Tag.objects.filter(job="consultant"))

    # 태그 별 출력
    # for tag in tag_list:
    #     tmp = []
    #     request_list = Request.objects.filter(consult_tag=tag)
    #     for i in range(len(request_list)):
    #         tmp.append(requestDictionary(request_list[i]))
        
    #     request_list = tmp
        
    #     data = {
    #         "request_list" : request_list
    #     }
    #     return JsonResponse(data)
    return render(request, "findRequest.html")