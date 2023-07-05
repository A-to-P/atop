from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name="chat"),  # 127.0.0.1:8000/chat
    # 127.0.0.1:8000/chat/room_name
    path('room/<int:room_name>/', views.room, name="room"),
]
