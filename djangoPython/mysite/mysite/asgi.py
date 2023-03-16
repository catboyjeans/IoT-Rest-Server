"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import django

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

#   Watch out!, the environment needs to be set here, otherwise uninitialized settings exceptions might arise
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.core.asgi import get_asgi_application
from SocketComm.routing import ws_urlpatterns 

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})