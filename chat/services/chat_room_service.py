from typing import Tuple

from django.db.models import QuerySet

from chat.models import Room


def creat_an_chat_room(consult_id, rest_id) -> Room:
    return Room.objects.create(consultant=consult_id, restaurant=rest_id)


def get_an_chat_room(room_id) -> Room:
    return Room.objects.get(id=room_id)


def get_an_chat_room_list(user_id: int, job) -> QuerySet[Room]:
    if job == "consultant":
        return Room.objects.filter(consultant=user_id)
    return Room.objects.filter(restaurant=user_id)


def get_chat_room_user(room_id: int) -> QuerySet[Room]:
    return Room.objects.filter(room_id=room_id)


def confirm_user_chat_room_join(user_id: int, room_id: int, job) -> Room:
    if job == "consultant":
        return Room.objects.get(consultant=user_id, id=room_id)
    return Room.objects.get(restaurant=user_id, id=room_id)
