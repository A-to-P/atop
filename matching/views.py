from django.shortcuts import render, redirect
from account.models import RestaurantProfile
from .models import Request
import datetime
# Create your views here.


def postRequest(request):
    # 요식업자 아니면 리다이렉트
    if request.user.job != "restaurant":
        return redirect('home')
        
    if request.method=="GET":
        # 컨설팅이 진행중이라면 리다이렉트
                
        # 이미 의뢰가 올라가있다면 리다이렉트
        
        # 의뢰글 작성 폼 렌더
        # 객체를 dict형태로 가져오기
        profile = list(RestaurantProfile.objects.filter(
            user=request.user).values())[0]
        # 나이계산
        profile["age"] = datetime.datetime.today().year - profile['birth'].year +1

        return render(request, "postRequest.html", {"profile": profile})
    
    elif request.method=="POST":
        try:
            user = request.user
            name = request.POST['name']
            age = request.POST['age']
            career = request.POST['career']
            menu = request.POST['menu']
            location = request.POST['location']
            area = request.POST['area']
            monthly_avg_rev = request.POST['monthly_avg_rev']
            title = request.POST['title']
            fee = request.POST['fee']
            content = request.POST['content']
            
            # rest_tags
            # consult_tags
            
            Request.objects.create(user=user, name=name, age=age, career=career, menu=menu, location=location, area=area, monthly_avg_rev=monthly_avg_rev, title=title,fee=fee,content=content)
        except Exception as e:
            print(e)
        
        return redirect('detailedRequest')


def detailedRequest(request):
    return render(request, "detailedRequest.html")


def findRequest(request):
    return render(request, "findRequest.html")
