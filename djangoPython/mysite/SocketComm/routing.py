from django.urls import path
from .consumers import  WSConsumer

ws_urlpatterns=[
    path('listen/<slug:thing_name>',WSConsumer.as_asgi()),
]