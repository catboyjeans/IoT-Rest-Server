from django.urls import path
from .consumers import  WSConsumer

ws_urlpatterns=[
    path('listen/<int:id>',WSConsumer.as_asgi()),
]