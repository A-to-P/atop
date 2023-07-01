"""
ASGI config for atop project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atop.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    # websocket 프로토콜 타입으로 요청받으면 'config.asgi.application' 실행 (settings에 추가)
    "websocket": AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns)),
})
