from django.urls import path
from . import views

urlpatterns = [
    path('chat', views.chat, name="chat"),  # 127.0.0.1:8000/chat
]
