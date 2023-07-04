from django.shortcuts import render, redirect
from account.models import RestaurantProfile, Tag
from .models import Request
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
    return render(request, "detailedRequest.html")

def applyRequest(request):
    return render(request, "applyRequest.html")


def findRequest(request):
    return render(request, "findRequest.html")
