from django.shortcuts import render
from account.models import User, Tag
from consulting.models import Consulting, Review

from queue import PriorityQueue, Queue

# Create your views here.

def home(request):
    # 분야별 컨설팅 횟수에 따라 리스트 가져오기
    tag_list = list(Tag.objects.filter(job="consultant"))
    ranking = []
    
    for tag in tag_list:
        # 최대 5명 우선순위큐
        que = PriorityQueue(maxsize=5)
        user_list = User.objects.filter(tag__in=[tag])
        for user in user_list:
            cnt = len(Consulting.objects.filter(consultant=user))
            # 컨설팅 횟수 내림차순으로 우선순위큐에 추가
            que.put((-cnt, user))
        
        # (임시) 유저가 5명 이하인경우
        iter = 5 
        if len(user_list)<5:
            iter=len(user_list)     
        
        ranking_list = []
        for _ in range(iter):
            ranking_list.append(que.get()[1])
        
        if len(ranking_list):
            lst = []
            order=0
            for user in ranking_list:
                tmp={}
                tmp['order']=0
                tmp['id'] = user.id
                tmp['name'] = user.name
                lst.append(tmp)
                order+=1
            ranking.append({'key':tag.name, 'value':lst})
    
    reviews = []
    review_list = Review.objects.all().order_by('-created_at')[:4]
    for review in review_list:
        con = review.consulting.consultant
        res = review.consulting.restaurant
        print (review)
    #     # cnt = len(Consulting.objects.filter(consultant=user))
    #     # 컨설팅 횟수 내림차순으로 우선순위큐에 추가
        reviews.append({'con' : con.name, 'res' : res.name, 'score' : review.rating, 'tag' : con.tag, 'comment' : review.comment})
    print(ranking)
    return render(request, 'home.html', {'ranking':ranking, 'reviews': reviews})