from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

# from chat.models import Room
from chat.services.chat_room_service import get_an_chat_room_list, get_chat_room_user, confirm_user_chat_room_join, \
    creat_an_chat_room
from chat.services.message_service import get_an_message_list

from collections import Counter

from account.models import User, ConsultantProfile, RestaurantProfile



# Create your views here.

@login_required
def chat(request):
    # 사용자가 있는지 없는지 판단
    user = request.user.is_authenticated
    # 사용자가 있으면 사용자가 속해있는 채팅방 list 표시
    if user:
        # 유저가 참여하고 있는 채팅방 목록
        if request.user.job=="consultant":
            chat_room_list = get_an_chat_room_list(request.user.id, job="consultant")
        else:
            chat_room_list = get_an_chat_room_list(request.user.id, job="restaurant")

        # chat_info = {}
        # for chat_room in chat_room_list:
        #     room_id = chat_room.id
        #     # 채팅방에 참여중인 유저 list
        #     username_list = [chat_room.consultant.username, chat_room.restaurant.username]
        #     # chat_info 변수에 딕셔너리 형태로 저장
        #     chat_info[room_id] = username_list

        # if chat_info == {}:
        #     chat_info = None

        # return render(request, "chat.html", {'chat_info': chat_info})
        
        # 가장 최근에 만들어진 room 가져오기
        room = chat_room_list.last()
        if room is None:
            if request.user.job =="consultant":
                return redirect('findRequest')
            else:
                return redirect('postRequest')
        room_id = room.id
        # 룸으로 이동하기
        return redirect(f'/room/{room_id}')
        
        
    # 사용자가 없으면 로그인화면
    else:
        return redirect(("login"))


# room 함수를 호출하면 room.html 을 렌더해주는 함수 / dict 형태로 room_name value 를 전송
@login_required
def room(request, room_name):
    room_id = int(room_name)
    job = request.user.job
    try:
        if job=="consultant":
            confirm_user_chat_room_join(request.user.id, room_id, job="consultant")
        else:
            confirm_user_chat_room_join(request.user.id, room_id, job="restaurant")

        message = get_an_message_list(room_id)
        
        if job=="consultant":        
            user_profile = ConsultantProfile.objects.get(user=request.user).image
        else:
            user_profile = RestaurantProfile.objects.get(user=request.user).image

        return render_room(request, {"room_name": room_name, "message": message, "user_profile": user_profile})

    except Exception as e:
        print('예외가 발생했습니다.', e)
        return redirect(("home"))


def render_room(request, payload):
    if request.user.job=="consultant":
        payload['baseHTML']="consultingSpace.html"
    else:
        payload['baseHTML']='myConsulting.html'
    return render(request, "room.html", payload)